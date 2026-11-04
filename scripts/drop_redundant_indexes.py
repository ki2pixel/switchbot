#!/usr/bin/env python3
"""Drop the redundant indexes created by older SwitchBot Dashboard versions.

Rationale (see docs audit V2):
  * ``idx_json_store_kind`` duplicates the ``json_store`` primary key index.
  * ``idx_state_history_metadata`` is a GIN index that no query uses; it only
    adds write amplification (it reached 122 MB for ~1.5k rows in production).

The application no longer creates either index, but existing databases keep
them until this script is run. Nothing is dropped unless ``--apply`` is passed.

Usage:
    python scripts/drop_redundant_indexes.py                 # dry run
    python scripts/drop_redundant_indexes.py --apply         # execute
    python scripts/drop_redundant_indexes.py --apply --index idx_json_store_kind
    python scripts/drop_redundant_indexes.py --env /path/to/.env --apply

The PostgreSQL URL is read from ``POSTGRES_URL`` (``.env`` file or environment).
Use ``postgresql+psycopg://``-free DSNs only: ``postgresql://...``.
"""

from __future__ import annotations

import argparse
import logging
import os
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

DEFAULT_TARGETS: tuple[str, ...] = (
    "idx_json_store_kind",
    "idx_state_history_metadata",
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def setup_logging(verbose: bool = False) -> logging.Logger:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger("drop_indexes")


def load_env_file(path: Path) -> dict[str, str]:
    """Minimal .env reader (no external dependency)."""
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        if key:
            values[key] = value.strip().strip('"').strip("'")
    return values


def describe_url(url: str | None) -> str:
    """Log-safe URL: scheme, host, port and database only."""
    if not url:
        return "None"

    parsed = urlsplit(url)
    if not parsed.scheme or not parsed.hostname:
        return "<invalid-url>"

    netloc = parsed.hostname
    if parsed.port:
        netloc = f"{netloc}:{parsed.port}"
    return urlunsplit((parsed.scheme, netloc, parsed.path, "", ""))


def resolve_dsn(env_path: Path) -> str:
    """Environment variables win over the .env file."""
    dsn = os.environ.get("POSTGRES_URL", "").strip()
    if dsn:
        return dsn
    if env_path.is_file():
        return load_env_file(env_path).get("POSTGRES_URL", "").strip()
    return ""


def inspect_indexes(cursor, targets: tuple[str, ...]) -> list[tuple[str, str, str]]:
    """Return ``(indexname, tablename, size)`` for existing targets."""
    cursor.execute(
        """
        SELECT i.indexname, i.tablename, pg_size_pretty(pg_relation_size(c.oid))
        FROM pg_indexes i
        JOIN pg_class c ON c.relname = i.indexname
        JOIN pg_namespace n ON n.oid = c.relnamespace AND n.nspname = i.schemaname
        WHERE i.schemaname = 'public'
          AND i.indexname = ANY(%s)
        ORDER BY i.indexname
        """,
        (list(targets),),
    )
    return [(row[0], row[1], row[2]) for row in cursor.fetchall()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--env",
        default=str(REPO_ROOT / ".env"),
        help="Path to the .env file (default: <repo>/.env)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually drop the indexes (without this flag the script is a dry run)",
    )
    parser.add_argument(
        "--index",
        action="append",
        choices=list(DEFAULT_TARGETS),
        help="Restrict to one index (repeatable)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="Connection timeout in seconds (default: 10)",
    )
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    logger = setup_logging(args.verbose)
    targets = tuple(args.index) if args.index else DEFAULT_TARGETS

    dsn = resolve_dsn(Path(args.env))
    if not dsn:
        logger.error(
            "POSTGRES_URL is not set (checked environment and %s)", args.env
        )
        return 2

    logger.info("Target database: %s", describe_url(dsn))
    logger.info("Indexes targeted: %s", ", ".join(targets))

    try:
        import psycopg
    except ImportError:
        logger.error(
            "psycopg is required: pip install 'psycopg[binary,pool]'"
        )
        return 2

    # DROP INDEX CONCURRENTLY cannot run inside a transaction block.
    with psycopg.connect(dsn, connect_timeout=args.timeout, autocommit=True) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_database(), current_user")
            database, user = cur.fetchone()
            logger.info("Connected to db=%s as %s", database, user)

            existing = inspect_indexes(cur, targets)
            if not existing:
                logger.info("Nothing to do: none of the targeted indexes exist")
                return 0

            logger.info("Existing targeted indexes:")
            for indexname, tablename, size in existing:
                logger.info("  - %s on %s (%s)", indexname, tablename, size)

            if not args.apply:
                logger.info(
                    "Dry run: no changes applied. Re-run with --apply to drop them."
                )
                return 0

            for indexname, _tablename, size in existing:
                logger.info("Dropping %s (%s)...", indexname, size)
                # Identifiers come from a fixed allow-list (argparse choices),
                # never from user input.
                cur.execute(f"DROP INDEX CONCURRENTLY IF EXISTS public.{indexname}")
                logger.info("Dropped %s", indexname)

            remaining = inspect_indexes(cur, targets)
            if remaining:
                logger.warning(
                    "Indexes still present: %s",
                    ", ".join(name for name, _table, _size in remaining),
                )
                return 1

            logger.info("All targeted indexes dropped successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
