from __future__ import annotations

import json
import logging
import threading
from typing import Any

from psycopg import sql
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb
from psycopg_pool import ConnectionPool

from switchbot_dashboard.config_store import StoreError


class PostgresStoreError(StoreError):
    """Raised when PostgreSQL storage backend cannot satisfy an operation."""


class PostgresStoreTransactionContext:
    """Re-entrant, thread-local transaction context for :class:`PostgresStore`.

    A nested transaction joins the transaction already active on the current
    thread. Borrowing a second pooled connection would make the thread wait on
    its own ``FOR UPDATE`` row lock until ``statement_timeout``.
    """

    def __init__(self, store: PostgresStore):
        self._store = store
        self._conn_ctx = None
        self._conn = None
        self._cur = None
        self._conn_entered = False
        self._cached_data: dict[str, Any] | None = None
        self._dirty = False
        self._is_nested = False

    def __enter__(self) -> "PostgresStoreTransactionContext":
        active_tx = getattr(self._store._local, "active_transaction", None)
        if active_tx is not None:
            self._is_nested = True
            return active_tx

        try:
            self._conn_ctx = self._store.pool.connection()
            self._conn = self._conn_ctx.__enter__()
            self._conn_entered = True
            self._conn.autocommit = False
            self._cur = self._conn.cursor(row_factory=dict_row)

            # Guarantee that the row exists so FOR UPDATE actually locks it.
            # Without this INSERT two concurrent transactions would both see
            # no row and could overwrite each other without serialization.
            self._cur.execute(
                """
                INSERT INTO json_store (kind, data, updated_at)
                VALUES (%s, '{}'::jsonb, NOW())
                ON CONFLICT (kind) DO NOTHING
                """,
                (self._store._kind,),
            )
            self._cur.execute(
                "SELECT data FROM json_store WHERE kind = %s FOR UPDATE",
                (self._store._kind,),
            )
            result = self._cur.fetchone()

            if result is None:
                self._cached_data = {}
            else:
                data = result["data"]
                if isinstance(data, str):
                    self._cached_data = json.loads(data)
                elif isinstance(data, dict):
                    self._cached_data = data
                else:
                    self._cached_data = {}

            self._store._local.active_transaction = self
            return self
        except Exception as exc:
            if self._conn is not None:
                try:
                    self._conn.rollback()
                except Exception as rollback_exc:
                    self._store._logger.warning(
                        "[store] Rollback failed while aborting transaction for %s store (%s)",
                        self._store._kind,
                        rollback_exc,
                    )
            self._close_resources()
            raise PostgresStoreError(
                f"Failed to start transaction for {self._store._kind} store"
            ) from exc

    def _close_resources(self) -> None:
        if self._cur is not None:
            try:
                self._cur.close()
            except Exception as cur_exc:
                self._store._logger.warning(
                    "[store] Failed to close cursor for %s store (%s)",
                    self._store._kind,
                    cur_exc,
                )
            finally:
                self._cur = None

        if self._conn_ctx is not None and self._conn_entered:
            try:
                # The transaction was already committed or rolled back above.
                # Exiting without an exception avoids a spurious warning from
                # the pool context manager while still returning the connection.
                self._conn_ctx.__exit__(None, None, None)
            except Exception as conn_exc:
                self._store._logger.warning(
                    "[store] Failed to return connection to pool for %s store (%s)",
                    self._store._kind,
                    conn_exc,
                )
            finally:
                self._conn_ctx = None
                self._conn = None
                self._conn_entered = False

    def read(self) -> dict[str, Any]:
        if self._is_nested:
            return self._store._local.active_transaction.read()
        import copy
        return copy.deepcopy(self._cached_data or {})

    def write(self, data: dict[str, Any]) -> None:
        if self._is_nested:
            self._store._local.active_transaction.write(data)
            return
        import copy
        self._cached_data = copy.deepcopy(data)
        self._dirty = True

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if self._is_nested:
            return

        self._store._local.active_transaction = None

        try:
            if exc_type is not None:
                if self._conn is not None:
                    self._conn.rollback()
                self._store._logger.info(
                    "[store] Transaction rolled back for %s store due to exception: %s",
                    self._store._kind,
                    exc_val,
                )
            elif self._dirty:
                query = sql.SQL("""
                    INSERT INTO json_store (kind, data, updated_at)
                    VALUES (%s, %s, NOW())
                    ON CONFLICT (kind)
                    DO UPDATE SET
                        data = EXCLUDED.data,
                        updated_at = EXCLUDED.updated_at
                """)
                self._cur.execute(query, (self._store._kind, Jsonb(self._cached_data)))
                self._conn.commit()
                self._store._logger.debug(
                    "[store] Transaction committed with write for %s store",
                    self._store._kind,
                )
            else:
                self._conn.commit()
                self._store._logger.debug(
                    "[store] Transaction committed (no write) for %s store",
                    self._store._kind,
                )
        except Exception as exc:
            if self._conn is not None:
                try:
                    self._conn.rollback()
                except Exception as rollback_exc:
                    self._store._logger.warning(
                        "[store] Rollback failed while finalizing transaction for %s store (%s)",
                        self._store._kind,
                        rollback_exc,
                    )
            self._store._logger.error(
                "[store] Failed to finalize transaction for %s store (%s)",
                self._store._kind,
                exc,
            )
            if exc_type is None:
                raise PostgresStoreError(
                    f"Failed to commit PostgreSQL transaction for {self._store._kind} store"
                ) from exc
        finally:
            self._close_resources()


class PostgresStore:
    """PostgreSQL JSON store implementing BaseStore interface for Neon PostgreSQL."""

    def __init__(
        self,
        connection_string: str | None = None,
        kind: str = "settings",
        *,
        logger: logging.Logger,
        ssl_mode: str = "require",
        max_connections: int = 10,
        pool: ConnectionPool | None = None,
    ) -> None:
        self._kind = kind
        self._logger = logger
        self._lock = threading.Lock()
        self._pool = pool
        self._owns_pool = (pool is None)
        self._local = threading.local()

        if self._pool is None:
            if not connection_string:
                raise PostgresStoreError("Either connection_string or pool must be provided")
            # Configure connection parameters for Neon
            # REL-05: connection timeout + statement_timeout for bounded query execution
            self._connection_params: dict[str, Any] = {
                "conninfo": connection_string,
                "min_size": 1,
                "max_size": max_connections,
                "timeout": 5.0,  # pool checkout timeout
                "open": True,
                "kwargs": {
                    "sslmode": ssl_mode,
                    "connect_timeout": 5,
                    "options": "-c statement_timeout=5000",
                },
            }
            self._initialize_pool()
        else:
            self._logger.info(
                "[store] Reusing shared connection pool for %s store", self._kind
            )

        self._ensure_table_exists()

    def _initialize_pool(self) -> None:
        """Initialize PostgreSQL connection pool (single attempt)."""
        try:
            self._pool = ConnectionPool(**self._connection_params)
            self._logger.info(
                "[store] Connection pool initialized for %s store", self._kind
            )
        except Exception as exc:
            self._logger.error(
                "[store] Failed to initialize connection pool for %s store (%s)",
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
            CREATE INDEX IF NOT EXISTS idx_json_store_updated_at ON json_store(updated_at);
        """)

        try:
            with self.pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(create_table_query)
                    conn.commit()
                    self._logger.info(
                        "[store] Table ensured for %s store", self._kind
                    )
        except Exception as exc:
            self._logger.error(
                "[store] Failed to ensure table exists for %s store (%s)",
                self._kind,
                exc,
            )
            raise PostgresStoreError(
                f"Failed to ensure table exists for {self._kind} store"
            ) from exc

    def transaction(self) -> Any:
        return PostgresStoreTransactionContext(self)

    def read(self) -> dict[str, Any]:
        tx = getattr(self._local, "active_transaction", None)
        if tx is not None:
            return tx.read()
        query = sql.SQL("SELECT data FROM json_store WHERE kind = %s")

        try:
            with self.pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, (self._kind,))
                    result = cur.fetchone()

                    if result is None:
                        self._logger.debug(
                            "[store] No data found for %s store, returning empty dict",
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
                "[store] Read failed for %s store (%s)", self._kind, exc
            )
            raise PostgresStoreError(
                f"PostgreSQL read failed for {self._kind} store"
            ) from exc

    def write(self, data: dict[str, Any]) -> None:
        tx = getattr(self._local, "active_transaction", None)
        if tx is not None:
            tx.write(data)
            return
        query = sql.SQL("""
            INSERT INTO json_store (kind, data, updated_at)
            VALUES (%s, %s, NOW())
            ON CONFLICT (kind)
            DO UPDATE SET
                data = EXCLUDED.data,
                updated_at = EXCLUDED.updated_at
        """)

        try:
            with self.pool.connection() as conn:
                with conn.cursor() as cur:
                    # Convert data to JSONB
                    jsonb_data = Jsonb(data)
                    cur.execute(query, (self._kind, jsonb_data))
                    conn.commit()
                    self._logger.debug(
                        "[store] Data written successfully for %s store", self._kind
                    )

        except Exception as exc:
            self._logger.error(
                "[store] Write failed for %s store (%s)", self._kind, exc
            )
            raise PostgresStoreError(
                f"PostgreSQL write failed for {self._kind} store"
            ) from exc

    @property
    def pool(self) -> ConnectionPool:
        if self._pool is None:
            raise RuntimeError("Database pool has not been initialized or has been closed")
        return self._pool

    def close(self) -> None:
        """Close connection pool and cleanup resources if owned."""
        if self._pool and self._owns_pool:
            try:
                self._pool.close()
                self._logger.info("[store] Connection pool closed for %s store", self._kind)
            except Exception as exc:
                self._logger.warning(
                    "[store] Error closing connection pool for %s store (%s)",
                    self._kind,
                    exc,
                )
            finally:
                self._pool = None
        elif self._pool:
            self._logger.debug("[store] Skipping closing shared pool for %s store", self._kind)
            self._pool = None

    def health_check(self) -> bool:
        try:
            pool = self.pool
        except RuntimeError:
            return False

        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT 1")
                    cur.fetchone()
                    return True
        except Exception as exc:
            self._logger.warning(
                "[store] Health check failed for %s store (%s)", self._kind, exc
            )
            return False
