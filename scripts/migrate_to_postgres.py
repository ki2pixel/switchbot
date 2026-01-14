#!/usr/bin/env python3
"""
Migration script from Redis/JSON to PostgreSQL for SwitchBot Dashboard.

This script migrates existing settings.json and state.json data from Redis or
local filesystem to PostgreSQL (Neon) with validation and rollback capabilities.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from switchbot_dashboard.config_store import JsonStore, RedisJsonStore, StoreError
from switchbot_dashboard.postgres_store import PostgresStore, PostgresStoreError


def setup_logging(verbose: bool = False) -> logging.Logger:
    """Setup logging configuration."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(__name__)


def read_redis_data(redis_url: str, kind: str, logger: logging.Logger) -> dict[str, Any] | None:
    """Read data from Redis store."""
    try:
        from redis import Redis
        from redis.exceptions import RedisError

        client = Redis.from_url(redis_url)
        key = f"switchbot_dashboard:{kind}"
        
        raw_value = client.get(key)
        if raw_value is None:
            logger.info(f"No data found in Redis for {kind}")
            return None

        raw_text = raw_value.decode("utf-8") if isinstance(raw_value, bytes) else str(raw_value)
        data = json.loads(raw_text)
        logger.info(f"Successfully read {kind} from Redis ({len(data)} keys)")
        return data

    except (RedisError, json.JSONDecodeError) as exc:
        logger.error(f"Failed to read {kind} from Redis: {exc}")
        return None


def read_json_data(file_path: str, logger: logging.Logger) -> dict[str, Any]:
    """Read data from local JSON file."""
    try:
        path = Path(file_path)
        if not path.exists():
            logger.warning(f"JSON file not found: {file_path}")
            return {}

        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
            logger.info(f"Successfully read {file_path} ({len(data)} keys)")
            return data

    except (json.JSONDecodeError, OSError) as exc:
        logger.error(f"Failed to read {file_path}: {exc}")
        return {}


def validate_data(data: dict[str, Any], kind: str, logger: logging.Logger) -> bool:
    """Validate data structure and content."""
    if not isinstance(data, dict):
        logger.error(f"Invalid data type for {kind}: expected dict, got {type(data)}")
        return False

    # Basic validation for settings
    if kind == "settings":
        required_keys = ["automation_enabled", "poll_interval_seconds"]
        missing_keys = [key for key in required_keys if key not in data]
        if missing_keys:
            logger.warning(f"Missing recommended keys in settings: {missing_keys}")

    # Basic validation for state
    elif kind == "state":
        if "last_read_at" in data and not isinstance(data["last_read_at"], str):
            logger.error(f"Invalid last_read_at type in state: expected string")

    logger.info(f"Data validation passed for {kind}")
    return True


def migrate_to_postgres(
    postgres_url: str,
    redis_url: str | None,
    settings_path: str,
    state_path: str,
    dry_run: bool,
    logger: logging.Logger,
) -> bool:
    """
    Migrate data from Redis/JSON to PostgreSQL.

    Args:
        postgres_url: PostgreSQL connection string
        redis_url: Redis connection string (optional)
        settings_path: Path to settings.json
        state_path: Path to state.json
        dry_run: If True, only validate without writing
        logger: Logger instance

    Returns:
        True if migration successful, False otherwise
    """
    try:
        # Initialize PostgreSQL store
        if not dry_run:
            postgres_store = PostgresStore(
                connection_string=postgres_url,
                kind="temp",  # Temporary kind for health check
                logger=logger,
            )
            
            if not postgres_store.health_check():
                logger.error("PostgreSQL health check failed")
                return False
            
            logger.info("PostgreSQL connection established successfully")

        # Read settings data
        logger.info("=== Migrating settings ===")
        settings_data = None

        # Try Redis first if available
        if redis_url:
            settings_data = read_redis_data(redis_url, "settings", logger)

        # Fallback to JSON file
        if not settings_data:
            settings_data = read_json_data(settings_path, logger)

        if not settings_data:
            logger.error("No settings data found to migrate")
            return False

        if not validate_data(settings_data, "settings", logger):
            return False

        # Read state data
        logger.info("=== Migrating state ===")
        state_data = None

        # Try Redis first if available
        if redis_url:
            state_data = read_redis_data(redis_url, "state", logger)

        # Fallback to JSON file
        if not state_data:
            state_data = read_json_data(state_path, logger)

        if not state_data:
            logger.warning("No state data found, will create empty state")

        if state_data and not validate_data(state_data, "state", logger):
            return False

        # Write to PostgreSQL if not dry run
        if not dry_run:
            logger.info("=== Writing to PostgreSQL ===")
            
            # Migrate settings
            settings_store = PostgresStore(
                connection_string=postgres_url,
                kind="settings",
                logger=logger,
            )
            settings_store.write(settings_data)
            logger.info("Settings migrated successfully")

            # Migrate state
            state_store = PostgresStore(
                connection_string=postgres_url,
                kind="state",
                logger=logger,
            )
            state_store.write(state_data or {})
            logger.info("State migrated successfully")

            # Cleanup
            settings_store.close()
            state_store.close()
        else:
            logger.info("=== Dry run completed - no data written ===")

        return True

    except (PostgresStoreError, Exception) as exc:
        logger.error(f"Migration failed: {exc}")
        return False


def main() -> None:
    """Main migration script entry point."""
    parser = argparse.ArgumentParser(
        description="Migrate SwitchBot Dashboard data from Redis/JSON to PostgreSQL"
    )
    parser.add_argument(
        "--postgres-url",
        required=True,
        help="PostgreSQL connection string (Neon format)",
    )
    parser.add_argument(
        "--redis-url",
        help="Redis connection string (optional, for reading existing data)",
    )
    parser.add_argument(
        "--settings-path",
        default="config/settings.json",
        help="Path to settings.json file",
    )
    parser.add_argument(
        "--state-path",
        default="config/state.json",
        help="Path to state.json file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate data without writing to PostgreSQL",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()
    logger = setup_logging(args.verbose)

    logger.info("Starting migration from Redis/JSON to PostgreSQL")
    logger.info(f"PostgreSQL URL: {args.postgres_url[:20]}...")
    if args.redis_url:
        logger.info(f"Redis URL: {args.redis_url[:20]}...")
    logger.info(f"Settings path: {args.settings_path}")
    logger.info(f"State path: {args.state_path}")
    logger.info(f"Dry run: {args.dry_run}")

    success = migrate_to_postgres(
        postgres_url=args.postgres_url,
        redis_url=args.redis_url,
        settings_path=args.settings_path,
        state_path=args.state_path,
        dry_run=args.dry_run,
        logger=logger,
    )

    if success:
        logger.info("Migration completed successfully!")
        sys.exit(0)
    else:
        logger.error("Migration failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
