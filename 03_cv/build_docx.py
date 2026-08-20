"""Сборка docx из markdown-исходников CV.

    py 03_cv/build_docx.py            # собрать все CV в 03_cv/current/
    py 03_cv/build_docx.py CV_Ireland_TrackB_AI.md

Из исходника выбрасывается служебное, чего не должно быть в файле,
уходящем работодателю:
  - HTML-комментарий в начале файла (заметки для агента);
  - маркеры `[НУЖНЫ ДАННЫЕ: ...]` — вместе со строкой, если строка
    состоит только из маркера.

Требует pandoc в PATH.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

CURRENT = Path(__file__).resolve().parent / "current"
MARKER = r"\[НУЖНЫ ДАННЫЕ[^\]]*\]"


def clean(text: str) -> tuple[str, int]:
    text = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)

    markers = len(re.findall(MARKER, text))
    kept = []
    for line in text.split("\n"):
        stripped = re.sub(rf"`?{MARKER}`?", "", line)
        # строка была только маркером (возможно, буллетом) — выбросить целиком
        if re.search(MARKER, line) and not stripped.strip(" -*·`"):
            continue
        if re.search(MARKER, line):
            # убрать разделитель, повисший там, где был маркер
            stripped = re.sub(r"[\s·,;—-]+$", "", stripped)
        kept.append(stripped if re.search(MARKER, line) else line)
    return "\n".join(kept), markers


def build(md: Path) -> None:
    body, markers = clean(md.read_text(encoding="utf-8"))
    tmp = md.with_suffix(".build.tmp.md")
    tmp.write_text(body, encoding="utf-8")
    out = md.with_suffix(".docx")
    try:
        result = subprocess.run(
            ["pandoc", str(tmp), "-o", str(out), "--from", "markdown", "--to", "docx"],
            capture_output=True, text=True,
        )
    finally:
        tmp.unlink(missing_ok=True)
    if result.returncode:
        if "permission denied" in result.stderr.lower():
            raise SystemExit(f"  {out.name}: файл открыт в Word — закрой его и повтори.")
        raise SystemExit(
            f"  {out.name}: pandoc не справился\n{result.stderr.strip()[:500]}"
        )
    note = f", вычищено маркеров [НУЖНЫ ДАННЫЕ]: {markers}" if markers else ""
    print(f"  {md.name} -> {out.name} ({out.stat().st_size} байт{note})")


def main(argv: list[str]) -> None:
    targets = [CURRENT / a for a in argv] if argv else sorted(CURRENT.glob("CV_*.md"))
    if not targets:
        raise SystemExit(f"Не найдено ни одного CV_*.md в {CURRENT}")
    for md in targets:
        if not md.exists():
            raise SystemExit(f"Нет файла: {md}")
        build(md)


if __name__ == "__main__":
    main(sys.argv[1:])
