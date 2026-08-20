"""SQLite-хранилище вакансий и их статусов."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    key         TEXT PRIMARY KEY,
    source      TEXT,
    title       TEXT,
    company     TEXT,
    location    TEXT,
    employment  TEXT,
    salary      TEXT,
    description TEXT,
    url         TEXT,
    message_id  TEXT,
    received    TEXT,
    first_seen  TEXT,
    score       INTEGER,
    verdict     TEXT,
    status      TEXT DEFAULT 'new',
    note        TEXT
);
CREATE INDEX IF NOT EXISTS idx_jobs_score ON jobs(score DESC);
CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs(status);
"""


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def connect(data_dir: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(data_dir / "jobs.db")
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def add_jobs(conn: sqlite3.Connection, jobs: list[dict]) -> int:
    """Вставляет новые вакансии, уже известные не трогает. Возвращает число новых."""
    added = 0
    for j in jobs:
        cur = conn.execute(
            """INSERT OR IGNORE INTO jobs
               (key, source, title, company, location, employment, salary,
                description, url, message_id, received, first_seen, status)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?, 'new')""",
            (
                j["key"], j["source"], j["title"], j["company"], j["location"],
                j["employment"], j["salary"], j["description"], j["url"],
                j.get("message_id", ""), j.get("received", ""), now(),
            ),
        )
        added += cur.rowcount
    conn.commit()
    return added


def unscored(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute("SELECT * FROM jobs WHERE score IS NULL").fetchall()


def save_score(conn: sqlite3.Connection, key: str, score: int, verdict: dict) -> None:
    conn.execute(
        "UPDATE jobs SET score = ?, verdict = ? WHERE key = ?",
        (score, json.dumps(verdict, ensure_ascii=False), key),
    )
    conn.commit()


def top(conn: sqlite3.Connection, threshold: int, limit: int = 30) -> list[sqlite3.Row]:
    return conn.execute(
        """SELECT * FROM jobs
           WHERE status = 'new' AND score >= ?
           ORDER BY score DESC, first_seen DESC LIMIT ?""",
        (threshold, limit),
    ).fetchall()


def set_status(conn: sqlite3.Connection, key: str, status: str, note: str = "") -> bool:
    cur = conn.execute(
        "UPDATE jobs SET status = ?, note = ? WHERE key = ?", (status, note, key)
    )
    conn.commit()
    return cur.rowcount > 0


def get(conn: sqlite3.Connection, key: str) -> sqlite3.Row | None:
    return conn.execute("SELECT * FROM jobs WHERE key = ?", (key,)).fetchone()


def stats(conn: sqlite3.Connection) -> dict:
    rows = conn.execute("SELECT status, COUNT(*) c FROM jobs GROUP BY status").fetchall()
    out = {r["status"]: r["c"] for r in rows}
    out["total"] = conn.execute("SELECT COUNT(*) c FROM jobs").fetchone()["c"]
    out["scored"] = conn.execute(
        "SELECT COUNT(*) c FROM jobs WHERE score IS NOT NULL"
    ).fetchone()["c"]
    return out
