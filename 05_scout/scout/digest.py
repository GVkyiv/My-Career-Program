"""Сборка дайджеста в markdown."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


def _verdict(row) -> dict:
    try:
        return json.loads(row["verdict"] or "{}")
    except json.JSONDecodeError:
        return {}


def build(conn, cfg, profile: str, drafts: int = 0, verbose: bool = True) -> Path:
    from . import config, score, store

    rows = store.top(conn, cfg["score_threshold"])
    st = store.stats(conn)
    today = datetime.now().strftime("%Y-%m-%d")

    lines = [
        f"# Дайджест вакансий — {today}",
        "",
        f"Рынок: **{cfg['market']}**. Порог показа: {cfg['score_threshold']}/100.",
        f"Всего в базе {st['total']}, оценено {st['scored']}, "
        f"выше порога и ещё не разобрано — {len(rows)}.",
        "",
        "Подача — руками. Скрипт ничего никуда не отправляет.",
        "",
    ]

    if not rows:
        lines += ["Ничего выше порога. Либо тихая неделя, либо порог/ключевые слова", 
                  "в `config.json` настроены слишком узко.", ""]

    for n, row in enumerate(rows, 1):
        v = _verdict(row)
        lines += [
            f"## {n}. {row['title']} — {row['company']}  ·  {row['score']}/100",
            "",
            f"- Локация: {row['location'] or '—'}",
            f"- Занятость: {row['employment'] or '—'}",
            f"- Оплата: {row['salary'] or 'не указана'}",
            f"- Источник: {row['source']}, письмо от {row['received'] or '—'}",
            f"- id: `{row['key']}`",
            "",
            f"**Вердикт.** {v.get('verdict', '—')}",
            "",
        ]
        if v.get("red_flags"):
            lines += ["**Красные флаги:**"] + [f"- {f}" for f in v["red_flags"]] + [""]
        if v.get("gaps"):
            lines += ["**Гэпы:**"] + [f"- {g}" for g in v["gaps"]] + [""]
        if row["description"]:
            lines += [f"> {row['description']}", ""]
        lines += [f"[Открыть вакансию]({row['url']})", ""]

        if n <= drafts:
            if verbose:
                print(f"  черновик письма для «{row['title']}»...")
            try:
                letter = score.draft_letter(row, cfg, profile)
                lines += ["<details><summary>Черновик cover letter</summary>", "",
                          letter, "", "</details>", ""]
            except Exception as exc:
                lines += [f"*Черновик не собран: {exc}*", ""]
        lines += ["---", ""]

    lines += [
        "## Что дальше",
        "",
        "```bash",
        "py -m scout mark <id> applied      # подался",
        "py -m scout mark <id> ignored      # не интересно",
        "py -m scout draft <id>             # черновик письма для конкретной вакансии",
        "```",
        "",
    ]

    out_dir = config.data_dir(cfg) / "digests"
    out_dir.mkdir(exist_ok=True)
    path = out_dir / f"{today}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
