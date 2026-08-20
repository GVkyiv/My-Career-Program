"""Загрузка config.json и .env. Без внешних зависимостей."""

from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_env(path: Path | None = None) -> None:
    """Читает .env в os.environ. Уже выставленные переменные не перетирает."""
    env_path = path or ROOT / ".env"
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def load_config(path: Path | None = None) -> dict:
    cfg = json.loads((path or ROOT / "config.json").read_text(encoding="utf-8"))
    cfg["_root"] = ROOT
    return cfg


def require(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(
            f"Не задана переменная {name}. Скопируй .env.example в .env и заполни."
        )
    return value


def profile_text(cfg: dict) -> str:
    """Склеенный текст профиля кандидата и файла рынка — контекст для скоринга."""
    chunks = []
    for rel in cfg["profile_files"]:
        p = (ROOT / rel).resolve()
        if p.exists():
            chunks.append(f"### Файл: {p.name}\n\n{p.read_text(encoding='utf-8')}")
    return "\n\n".join(chunks)


def data_dir(cfg: dict) -> Path:
    d = ROOT / "data"
    d.mkdir(exist_ok=True)
    return d
