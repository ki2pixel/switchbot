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


class PostgresStoreTransactionContext:
    def __init__(self, store: PostgresStore):
        self._store = store
        self._conn_ctx = None
        self._conn = None
        self._cur = None
        self._cached_data = None
        self._dirty = False
        self._previous_transaction = None

    def __enter__(self):
        self._previous_transaction = getattr(self._store._local, "active_transaction", None)
        self._store._local.active_transaction = self
        
        try:
            self._conn_ctx = self._store.pool.connection()
            self._conn = self._conn_ctx.__enter__()
            self._conn.autocommit = False
            self._cur = self._conn.cursor(row_factory=dict_row)
            
            # Row-level locking on json_store
            self._cur.execute("SELECT data FROM json_store WHERE kind = %s FOR UPDATE", (self._store._kind,))
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
        except Exception as exc:
            self._store._local.active_transaction = self._previous_transaction
            if self._cur:
                try:
                    self._cur.close()
                except Exception:
                    pass
            if self._conn_ctx:
                try:
                    self._conn_ctx.__exit__(type(exc), exc, exc.__traceback__)
                except Exception:
                    pass
            raise PostgresStoreError(f"Failed to start transaction for {self._store._kind} store") from exc
        return self

    def read(self) -> dict[str, Any]:
        import copy
        return copy.deepcopy(self._cached_data)

    def write(self, data: dict[str, Any]) -> None:
        import copy
        self._cached_data = copy.deepcopy(data)
        self._dirty = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._store._local.active_transaction = self._previous_transaction
        
        try:
            if exc_type is not None:
                self._conn.rollback()
                self._store._logger.info(
                    "[postgres] Transaction rolled back for %s store due to exception: %s",
                    self._store._kind,
                    exc_val,
                )
            else:
                if self._dirty:
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
                    self._store._logger.debug("[postgres] Transaction committed with write for %s store", self._store._kind)
                else:
                    self._conn.commit()
                    self._store._logger.debug("[postgres] Transaction committed (no write) for %s store", self._store._kind)
        except Exception as exc:
            self._store._logger.error("[postgres] Failed to finalize transaction for %s store (%s)", self._store._kind, exc)
            if exc_type is None:
                raise PostgresStoreError(f"Failed to commit PostgreSQL transaction for {self._store._kind} store") from exc
        finally:
            if self._cur:
                try:
                    self._cur.close()
                except Exception:
                    pass
            if self._conn_ctx:
                try:
                    self._conn_ctx.__exit__(exc_type, exc_val, exc_tb)
                except Exception:
                    pass


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
            self._connection_params: dict[str, Any] = {
                "conninfo": connection_string,
                "min_size": 1,
                "max_size": max_connections,
                "kwargs": {"sslmode": ssl_mode},
            }
            self._initialize_pool()
        else:
            self._logger.info(
                "[postgres] Reusing shared connection pool for %s store", self._kind
            )

        self._ensure_table_exists()

    def _initialize_pool(self) -> None:
        """Initialize PostgreSQL connection pool (single attempt)."""
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
            with self.pool.connection() as conn:
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
                        "[postgres] Data written successfully for %s store", self._kind
                    )

        except Exception as exc:
            self._logger.error(
                "[postgres] Write failed for %s store (%s)", self._kind, exc
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
                self._logger.info("[postgres] Connection pool closed for %s store", self._kind)
            except Exception as exc:
                self._logger.warning(
                    "[postgres] Error closing connection pool for %s store (%s)",
                    self._kind,
                    exc,
                )
            finally:
                self._pool = None
        elif self._pool:
            self._logger.debug("[postgres] Skipping closing shared pool for %s store", self._kind)
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
                "[postgres] Health check failed for %s store (%s)", self._kind, exc
            )
            return False

    def __del__(self) -> None:
        """Cleanup on garbage collection."""
        self.close()
