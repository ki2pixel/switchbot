from __future__ import annotations

import json
import logging
import threading
from typing import Any

import psycopg
from psycopg import sql
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb
from psycopg_pool import ConnectionPool


class PostgresStoreError(RuntimeError):
    """Raised when PostgreSQL storage backend cannot satisfy an operation."""


class PostgresStore:
    """PostgreSQL JSON store implementing BaseStore interface for Neon PostgreSQL."""

    def __init__(
        self,
        connection_string: str,
        kind: str,
        *,
        logger: logging.Logger,
        ssl_mode: str = "require",
        max_connections: int = 10,
    ) -> None:
        """
        Initialize PostgreSQL store with connection pooling.

        Args:
            connection_string: PostgreSQL connection URL (Neon format)
            kind: Store kind ('settings' or 'state')
            logger: Logger instance for error reporting
            ssl_mode: SSL mode for connections (default: 'require')
            max_connections: Maximum connections in pool
        """
        self._kind = kind
        self._logger = logger
        self._lock = threading.Lock()

        # Configure connection parameters for Neon
        self._connection_params = {
            "conninfo": connection_string,
            "min_size": 1,
            "max_size": max_connections,
        }

        # Initialize connection pool
        self._pool = None
        self._initialize_pool()
        self._ensure_table_exists()

    def _initialize_pool(self) -> None:
        """Initialize PostgreSQL connection pool with retry logic."""
        try:
            self._pool = ConnectionPool(**self._connection_params)
            self._logger.info(
                "[postgres] Connection pool initialized for %s store", self._kind
            )
        except Exception as exc:
            self._logger.error(
                "[postgres] Failed to initialize connection pool for %s store (%s)",
                self._kind,
                exc,
            )
            raise PostgresStoreError(
                f"Failed to initialize PostgreSQL connection pool for {self._kind} store"
            ) from exc

    def _ensure_table_exists(self) -> None:
        """Create json_store table if it doesn't exist."""
        create_table_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS json_store (
                kind VARCHAR(50) PRIMARY KEY,
                data JSONB NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
            );
            CREATE INDEX IF NOT EXISTS idx_json_store_kind ON json_store(kind);
            CREATE INDEX IF NOT EXISTS idx_json_store_updated_at ON json_store(updated_at);
        """)

        try:
            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(create_table_query)
                    conn.commit()
                    self._logger.info(
                        "[postgres] Table ensured for %s store", self._kind
                    )
        except Exception as exc:
            self._logger.error(
                "[postgres] Failed to ensure table exists for %s store (%s)",
                self._kind,
                exc,
            )
            raise PostgresStoreError(
                f"Failed to ensure table exists for {self._kind} store"
            ) from exc

    def read(self) -> dict[str, Any]:
        """
        Read JSON data from PostgreSQL.

        Returns:
            Dictionary containing stored data or empty dict if not found

        Raises:
            PostgresStoreError: If read operation fails
        """
        query = sql.SQL("SELECT data FROM json_store WHERE kind = %s")

        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, (self._kind,))
                    result = cur.fetchone()

                    if result is None:
                        self._logger.debug(
                            "[postgres] No data found for %s store, returning empty dict",
                            self._kind,
                        )
                        return {}

                    # Parse JSONB data
                    data = result["data"]
                    if isinstance(data, str):
                        return json.loads(data)
                    if isinstance(data, dict):
                        return data
                    raise PostgresStoreError(
                        f"Invalid data type in PostgreSQL for {self._kind} store"
                    )

        except PostgresStoreError:
            raise
        except Exception as exc:
            self._logger.error(
                "[postgres] Read failed for %s store (%s)", self._kind, exc
            )
            raise PostgresStoreError(
                f"PostgreSQL read failed for {self._kind} store"
            ) from exc

    def write(self, data: dict[str, Any]) -> None:
        """
        Write JSON data to PostgreSQL.

        Args:
            data: Dictionary to store

        Raises:
            PostgresStoreError: If write operation fails
        """
        query = sql.SQL("""
            INSERT INTO json_store (kind, data, updated_at)
            VALUES (%s, %s, NOW())
            ON CONFLICT (kind)
            DO UPDATE SET
                data = EXCLUDED.data,
                updated_at = EXCLUDED.updated_at
        """)

        try:
            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    # Convert data to JSONB
                    jsonb_data = Jsonb(data)
                    cur.execute(query, (self._kind, jsonb_data))
                    conn.commit()
                    self._logger.debug(
                        "[postgres] Data written successfully for %s store", self._kind
                    )

        except Exception as exc:
            self._logger.error(
                "[postgres] Write failed for %s store (%s)", self._kind, exc
            )
            raise PostgresStoreError(
                f"PostgreSQL write failed for {self._kind} store"
            ) from exc

    def close(self) -> None:
        """Close connection pool and cleanup resources."""
        if self._pool:
            try:
                self._pool.close()
                self._logger.info("[postgres] Connection pool closed for %s store", self._kind)
            except Exception as exc:
                self._logger.warning(
                    "[postgres] Error closing connection pool for %s store (%s)",
                    self._kind,
                    exc,
                )
            finally:
                self._pool = None

    def health_check(self) -> bool:
        """
        Perform health check on PostgreSQL connection.

        Returns:
            True if connection is healthy, False otherwise
        """
        if not self._pool:
            return False

        try:
            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT 1")
                    cur.fetchone()
                    return True
        except Exception as exc:
            self._logger.warning(
                "[postgres] Health check failed for %s store (%s)", self._kind, exc
            )
            return False

    def __del__(self) -> None:
        """Cleanup on garbage collection."""
        self.close()
