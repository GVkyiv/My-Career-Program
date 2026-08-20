"""Забор писем с job-алертами через Gmail IMAP."""

from __future__ import annotations

import email
import html
import imaplib
import re
from datetime import datetime, timedelta, timezone
from email.header import decode_header, make_header
from email.message import Message

IMAP_HOST = "imap.gmail.com"
_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"[ \t]+")


def _decode(value: str | None) -> str:
    if not value:
        return ""
    try:
        return str(make_header(decode_header(value)))
    except Exception:
        return value


def _html_to_text(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", raw)
    raw = re.sub(r'(?is)<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', r"\2\n\1\n", raw)
    return html.unescape(_TAG_RE.sub(" ", raw))


def _body(msg: Message) -> str:
    plain, rich = [], []
    for part in msg.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if part.get_filename():
            continue
        ctype = part.get_content_type()
        if ctype not in ("text/plain", "text/html"):
            continue
        payload = part.get_payload(decode=True)
        if not payload:
            continue
        charset = part.get_content_charset() or "utf-8"
        try:
            text = payload.decode(charset, errors="replace")
        except LookupError:
            text = payload.decode("utf-8", errors="replace")
        (plain if ctype == "text/plain" else rich).append(text)

    text = "\n".join(plain) if plain else _html_to_text("\n".join(rich))
    text = text.replace("\r\n", "\n").replace("\u00a0", " ").replace("\u200c", "")
    text = _WS_RE.sub(" ", text)
    return "\n".join(line.strip() for line in text.split("\n"))


def fetch(cfg: dict, verbose: bool = True) -> list[dict]:
    """Возвращает письма из указанных лейблов за lookback_days, отфильтрованные по отправителям."""
    from .config import require

    user = require("GMAIL_USER")
    password = require("GMAIL_APP_PASSWORD").replace(" ", "")

    mailboxes = cfg["mailbox"]
    if isinstance(mailboxes, str):
        mailboxes = [mailboxes]
    since = (datetime.now(timezone.utc) - timedelta(days=cfg["lookback_days"])).strftime("%d-%b-%Y")
    senders = [s.lower() for s in cfg.get("senders", [])]

    out: list[dict] = []
    conn = imaplib.IMAP4_SSL(IMAP_HOST)
    try:
        conn.login(user, password)
        for box in mailboxes:
            status, _ = conn.select(f'"{box}"', readonly=True)
            if status != "OK":
                if verbose:
                    print(f"  ! лейбл '{box}' не найден в Gmail, пропускаю")
                continue
            status, data = conn.search(None, "SINCE", since)
            if status != "OK":
                continue
            ids = data[0].split()
            if verbose:
                print(f"  {box}: {len(ids)} писем за {cfg['lookback_days']} дн.")
            for num in ids:
                status, raw = conn.fetch(num, "(RFC822)")
                if status != "OK" or not raw or not isinstance(raw[0], tuple):
                    continue
                msg = email.message_from_bytes(raw[0][1])
                sender = _decode(msg.get("From")).lower()
                if senders and not any(s in sender for s in senders):
                    continue
                out.append(
                    {
                        "message_id": msg.get("Message-ID", f"{box}:{num.decode()}"),
                        "mailbox": box,
                        "sender": sender,
                        "subject": _decode(msg.get("Subject")),
                        "date": _decode(msg.get("Date")),
                        "body": _body(msg),
                    }
                )
    finally:
        try:
            conn.close()
        except Exception:
            pass
        conn.logout()
    return out
