"""CLI: py -m scout <команда>"""

from __future__ import annotations

import sys

from . import config, digest, mail, parse, score, store

USAGE = """Job Scout — мониторинг вакансий из почтовых алертов.

  py -m scout run [--drafts N]   всё сразу: забрать почту, оценить, собрать дайджест
  py -m scout fetch              только забрать письма и разложить в базу
  py -m scout score              только оценить неоценённое
  py -m scout digest [--drafts N] только собрать дайджест
  py -m scout draft <id>         черновик cover letter для вакансии
  py -m scout mark <id> <статус> статус: applied | ignored | shortlisted
  py -m scout status             сводка по базе
"""


def _arg_int(args: list[str], flag: str, default: int) -> int:
    if flag in args:
        i = args.index(flag)
        if i + 1 < len(args):
            return int(args[i + 1])
    return default


def cmd_fetch(conn, cfg) -> None:
    print("Забираю письма...")
    messages = mail.fetch(cfg)
    all_jobs, unparsed = [], []
    for msg in messages:
        jobs, parser = parse.parse_email(msg)
        if jobs:
            all_jobs.extend(jobs)
        else:
            unparsed.append((parser, msg["subject"]))
    added = store.add_jobs(conn, all_jobs)
    print(f"Писем: {len(messages)}. Вакансий найдено: {len(all_jobs)}, из них новых: {added}.")
    if unparsed:
        print(f"Не распознано писем: {len(unparsed)} (парсер под этот источник ещё не написан):")
        for parser, subject in unparsed[:10]:
            print(f"  - [{parser}] {subject}")


def cmd_score(conn, cfg) -> None:
    profile = config.profile_text(cfg)
    print("Оцениваю...")
    counts = score.run_scoring(conn, cfg, profile)
    print(
        f"Отсеяно предфильтром: {counts['prefiltered']}, "
        f"оценено моделью: {counts['scored']}."
    )
    if counts["skipped_no_key"]:
        print(
            f"Пропущено {counts['skipped_no_key']} — не задан ANTHROPIC_API_KEY. "
            "Работает только предфильтр."
        )


def cmd_digest(conn, cfg, drafts: int) -> None:
    path = digest.build(conn, cfg, config.profile_text(cfg), drafts=drafts)
    print(f"Дайджест: {path}")


def cmd_draft(conn, cfg, key: str) -> None:
    row = store.get(conn, key)
    if not row:
        raise SystemExit(f"Вакансия {key} не найдена.")
    print(score.draft_letter(row, cfg, config.profile_text(cfg)))


def cmd_mark(conn, key: str, status: str) -> None:
    if status not in ("applied", "ignored", "shortlisted", "new"):
        raise SystemExit("Статус: applied | ignored | shortlisted | new")
    if store.set_status(conn, key, status):
        print(f"{key} → {status}")
    else:
        raise SystemExit(f"Вакансия {key} не найдена.")


def cmd_status(conn) -> None:
    st = store.stats(conn)
    print(f"Всего вакансий: {st['total']}, оценено: {st['scored']}")
    for k, v in sorted(st.items()):
        if k not in ("total", "scored"):
            print(f"  {k}: {v}")


def main(argv: list[str]) -> None:
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(USAGE)
        return

    config.load_env()
    cfg = config.load_config()
    conn = store.connect(config.data_dir(cfg))
    command, args = argv[0], argv[1:]
    drafts = _arg_int(args, "--drafts", 0)

    if command == "fetch":
        cmd_fetch(conn, cfg)
    elif command == "score":
        cmd_score(conn, cfg)
    elif command == "digest":
        cmd_digest(conn, cfg, drafts)
    elif command == "run":
        cmd_fetch(conn, cfg)
        cmd_score(conn, cfg)
        cmd_digest(conn, cfg, drafts)
    elif command == "draft":
        cmd_draft(conn, cfg, args[0])
    elif command == "mark":
        cmd_mark(conn, args[0], args[1])
    elif command == "status":
        cmd_status(conn)
    else:
        print(USAGE)


if __name__ == "__main__":
    main(sys.argv[1:])
