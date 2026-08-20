"""Скоринг вакансий под профиль кандидата и черновики cover letter.

Два слоя:
1. Дешёвый предфильтр по ключевым словам из config.json — отсекает явный мусор
   без обращения к API.
2. Claude оценивает оставшееся против candidate.md + файла рынка.

Без ANTHROPIC_API_KEY второй слой отключается, остаётся только предфильтр.
"""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request

API_URL = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"

SCORING_SYSTEM = """Ты — трезвый хедхантер, оценивающий вакансии под конкретного кандидата.

Тебе дан профиль кандидата и описание целевого рынка. Оцени каждую вакансию.

Правила:
- Оценка 0-100: насколько кандидат реально пройдёт скрининг и захочет эту работу.
- Не подыгрывай. Кандидату не нужны лестные оценки, ему нужно не тратить время.
- Учитывай явно исключённые из таргетинга роли из профиля — они получают низкий балл,
  даже если формально пересекаются по навыкам.
- Учитывай отсутствие локального track record на этом рынке и правовой статус.
- red_flags — конкретные препятствия из текста вакансии (требуемое гражданство,
  security clearance, уровень явно ниже/выше, неподходящий домен). Пустой список,
  если препятствий не видно.
- gaps — чего у кандидата не хватает под эту роль по подтверждённым фактам профиля.
- Не выдумывай факты о кандидате, которых нет в профиле.

Верни ТОЛЬКО JSON-массив, по объекту на вакансию, в том же порядке:
[{"id": "<id из запроса>", "score": <0-100>, "verdict": "<одно предложение, почему>",
  "red_flags": ["..."], "gaps": ["..."]}]"""

DRAFT_SYSTEM = """Ты пишешь cover letter под конкретную вакансию от имени кандидата.

Жёсткие правила:
- Используй ТОЛЬКО факты и цифры из профиля кандидата. Ни одной новой метрики,
  ни одного нового достижения. Если хочется усилить письмо цифрой, которой в профиле
  нет — не пиши её, а поставь маркер [НУЖНЫ ДАННЫЕ: что именно нужно].
- Деловой английский, без американских клише и раздутых self-praise формулировок.
- Максимум 200 слов. Три абзаца: зачем именно эта роль и компания, чем закрываешь
  их задачу (конкретика из профиля), правовой статус и следующий шаг.
- Не пересказывай резюме. Пиши то, чего в резюме не видно.

Верни только текст письма, без темы и подписи-шапки."""


def _prefilter(row, cfg) -> tuple[int, str] | None:
    """Возвращает (score, причина), если вакансия отсеяна без обращения к API."""
    haystack = " ".join(
        str(row[f] or "") for f in ("title", "company", "location", "employment", "description")
    ).lower()
    for bad in cfg["prefilter"]["hard_exclude"]:
        if bad.lower() in haystack:
            return 0, f"предфильтр: стоп-слово «{bad}»"
    positives = cfg["prefilter"]["must_match_any"]
    if positives and not any(p.lower() in haystack for p in positives):
        return 15, "предфильтр: нет ни одного профильного ключевого слова"
    return None


def _call_api(model: str, system: str, prompt: str, max_tokens: int = 4000) -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY не задан")
    payload = json.dumps(
        {
            "model": model,
            "max_tokens": max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "x-api-key": key,
            "anthropic-version": API_VERSION,
            "content-type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"Claude API {exc.code}: {exc.read().decode('utf-8')[:400]}") from exc
    return "".join(b.get("text", "") for b in body.get("content", []))


def _extract_json(text: str):
    match = re.search(r"\[.*\]", text, re.S)
    if not match:
        raise RuntimeError(f"Ответ модели не содержит JSON-массив: {text[:200]}")
    return json.loads(match.group(0))


def _job_block(row) -> str:
    return (
        f"id: {row['key']}\n"
        f"Заголовок: {row['title']}\n"
        f"Компания: {row['company']}\n"
        f"Локация: {row['location']}\n"
        f"Занятость: {row['employment']}\n"
        f"Оплата: {row['salary']}\n"
        f"Описание: {row['description']}"
    )


def score_batch(rows, cfg, profile: str) -> list[dict]:
    """Оценивает пачку вакансий одним обращением к API."""
    prompt = (
        f"# Профиль кандидата и рынок\n\n{profile}\n\n"
        f"# Вакансии для оценки ({len(rows)} шт.)\n\n"
        + "\n\n---\n\n".join(_job_block(r) for r in rows)
    )
    results = _extract_json(_call_api(cfg["scoring_model"], SCORING_SYSTEM, prompt))
    by_id = {r.get("id"): r for r in results}
    out = []
    for row in rows:
        r = by_id.get(row["key"], {})
        out.append(
            {
                "key": row["key"],
                "score": int(r.get("score", 0)),
                "verdict": r.get("verdict", "модель не вернула оценку для этой вакансии"),
                "red_flags": r.get("red_flags", []),
                "gaps": r.get("gaps", []),
            }
        )
    return out


def draft_letter(row, cfg, profile: str) -> str:
    prompt = (
        f"# Профиль кандидата и рынок\n\n{profile}\n\n"
        f"# Вакансия\n\n{_job_block(row)}\n\n"
        "Напиши cover letter под эту вакансию."
    )
    return _call_api(cfg["drafting_model"], DRAFT_SYSTEM, prompt, max_tokens=1500).strip()


def run_scoring(conn, cfg, profile: str, verbose: bool = True) -> dict:
    from . import store

    rows = store.unscored(conn)
    counts = {"prefiltered": 0, "scored": 0, "skipped_no_key": 0}
    pending = []
    for row in rows:
        pre = _prefilter(row, cfg)
        if pre:
            store.save_score(conn, row["key"], pre[0], {"verdict": pre[1], "red_flags": [], "gaps": []})
            counts["prefiltered"] += 1
        else:
            pending.append(row)

    if not pending:
        return counts
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        counts["skipped_no_key"] = len(pending)
        return counts

    size = cfg.get("batch_size", 8)
    for i in range(0, len(pending), size):
        batch = pending[i : i + size]
        if verbose:
            print(f"  скоринг {i + 1}-{i + len(batch)} из {len(pending)}...")
        for res in score_batch(batch, cfg, profile):
            store.save_score(
                conn,
                res["key"],
                res["score"],
                {"verdict": res["verdict"], "red_flags": res["red_flags"], "gaps": res["gaps"]},
            )
            counts["scored"] += 1
    return counts
