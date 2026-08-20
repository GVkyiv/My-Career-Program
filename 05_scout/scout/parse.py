"""Разбор писем-алертов в отдельные вакансии.

Структура писем IrishJobs подтверждена на реальных письмах (август 2026):
    <Заголовок>
    <ссылка click.irishjobs.ie>
    <Компания>
    <Локация>
    [<размер компании>]
    <пусто>
    <тип занятости>
    <зарплата>
    <пусто>
    <краткое описание>
    more
    <ссылка click.irishjobs.ie>

Ссылки в письмах персонализированные (содержат профиль поиска), поэтому
для дедупликации используется хеш «заголовок|компания|локация», не URL.
"""

from __future__ import annotations

import hashlib
import re

SKIP_TITLES = {
    "more", "see all matching jobs", "manage all your subscriptions",
    "unsubscribe from this email", "view job", "apply now", "see all jobs",
    "see more jobs", "view all jobs",
}
SKIP_PREFIXES = (
    "criteria:", "terms of use:", "privacy policy:", "contact us:",
    "facebook:", "instagram:", "youtube:", "blog:", "©", "hi ", "we found",
)
EMPLOYMENT_RE = re.compile(
    r"^(permanent|contract|temporary|part[- ]time|full[- ]time|internship|graduate)\b", re.I
)
SALARY_RE = re.compile(r"(€|\bper annum\b|\bper hour\b|\bper day\b|\bnegotiable\b|\$)", re.I)
SIZE_RE = re.compile(r"^\d[\d,\s\-–+]*employees$", re.I)

SOURCES = {
    "irishjobs": "https://click.irishjobs.ie/",
    "linkedin": "https://www.linkedin.com/comm/jobs/view/",
    "jobs_ie": "https://www.jobs.ie/",
}


def job_key(title: str, company: str, location: str) -> str:
    norm = "|".join(re.sub(r"\s+", " ", x or "").strip().lower() for x in (title, company, location))
    return hashlib.sha1(norm.encode("utf-8")).hexdigest()[:16]


def _is_title(line: str) -> bool:
    low = line.strip().lower()
    if not low or len(low) > 160:
        return False
    if low in SKIP_TITLES or low.startswith(SKIP_PREFIXES):
        return False
    return not low.startswith("http")


def _parse_by_anchor(lines: list[str], url_prefix: str, source: str) -> list[dict]:
    """Заголовок = строка, за которой сразу идёт ссылка на вакансию."""
    anchors = [
        i for i in range(len(lines) - 1)
        if lines[i + 1].startswith(url_prefix) and _is_title(lines[i])
    ]
    jobs: list[dict] = []
    for n, i in enumerate(anchors):
        end = anchors[n + 1] if n + 1 < len(anchors) else len(lines)
        segment = [l.strip() for l in lines[i + 2 : end]]
        meta = []
        for line in segment:
            if line.lower() == "more":
                break
            if line and not line.startswith("http"):
                meta.append(line)
        if not meta:
            continue

        company = meta[0]
        location = meta[1] if len(meta) > 1 and not SIZE_RE.match(meta[1]) else ""
        employment = next((m for m in meta if EMPLOYMENT_RE.match(m)), "")
        salary = next((m for m in meta if SALARY_RE.search(m) and m != employment), "")
        described = [
            m for m in meta[1:]
            if m not in (location, employment, salary) and not SIZE_RE.match(m)
        ]
        description = described[-1] if described else ""

        title = lines[i].strip()
        jobs.append(
            {
                "key": job_key(title, company, location),
                "source": source,
                "title": title,
                "company": company,
                "location": location,
                "employment": employment,
                "salary": salary,
                "description": description,
                "url": lines[i + 1].strip(),
            }
        )
    return jobs


def parse_email(msg: dict) -> tuple[list[dict], str]:
    """Возвращает (вакансии, имя парсера). Парсер 'unknown' — письмо не распознано."""
    lines = msg["body"].split("\n")
    sender = msg.get("sender", "")
    for source, prefix in SOURCES.items():
        if any(l.startswith(prefix) for l in lines):
            jobs = _parse_by_anchor(lines, prefix, source)
            if jobs:
                for j in jobs:
                    j["message_id"] = msg["message_id"]
                    j["received"] = msg.get("date", "")
                return jobs, source
    return [], f"unknown:{sender}"
