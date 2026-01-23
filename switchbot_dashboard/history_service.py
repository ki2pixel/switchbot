from __future__ import annotations

import datetime as dt
import json
import logging
import threading
from typing import Any, Optional

import psycopg
from psycopg import sql
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb
from psycopg_pool import ConnectionPool

from .postgres_store import PostgresStoreError


class HistoryServiceError(RuntimeError):
    """Raised when history service operations fail."""


class HistoryService:
    """Service for collecting and retrieving historical monitoring data."""

    def __init__(
        self,
        connection_pool: ConnectionPool,
        *,
        logger: logging.Logger,
        retention_hours: int = 6,
        batch_size: int = 4,
        flush_interval_seconds: int = 60,
    ) -> None:
        """
        Initialize history service with PostgreSQL connection pool.

        Args:
            connection_pool: PostgreSQL connection pool from PostgresStore
            logger: Logger instance for error reporting
            retention_hours: Data retention period (default: 6 hours for Neon PITR)
            batch_size: Number of records to buffer before flushing (default: 4)
            flush_interval_seconds: Maximum seconds to keep buffered data before flushing
        """
        self._pool = connection_pool
        self._logger = logger
        self._retention_hours = retention_hours
        self._batch_size = max(1, batch_size)
        self._flush_interval_seconds = max(0, flush_interval_seconds)
        self._pending_records: list[tuple[Any, ...]] = []
        self._pending_lock = threading.Lock()
        self._flush_timer: threading.Timer | None = None
        self._ensure_table_exists()

    def _ensure_table_exists(self) -> None:
        """Create state_history table if it doesn't exist."""
        create_table_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS state_history (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                temperature DECIMAL(4,1),
                humidity DECIMAL(4,1),
                assumed_aircon_power VARCHAR(10),
                last_action VARCHAR(50),
                api_requests_today INTEGER DEFAULT 0,
                error_count INTEGER DEFAULT 0,
                last_temperature_stale BOOLEAN DEFAULT FALSE,
                timezone VARCHAR(50) DEFAULT 'UTC',
                metadata JSONB DEFAULT '{}'
            );
            CREATE INDEX IF NOT EXISTS idx_state_history_timestamp ON state_history(timestamp DESC);
            CREATE INDEX IF NOT EXISTS idx_state_history_aircon_power ON state_history(assumed_aircon_power);
            CREATE INDEX IF NOT EXISTS idx_state_history_metadata ON state_history USING GIN(metadata);
        """)

        try:
            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(create_table_query)
                    conn.commit()
                    self._logger.info("[history] Table state_history ensured")
        except Exception as exc:
            self._logger.error("[history] Failed to create table (%s)", exc)
            raise HistoryServiceError("Failed to ensure history table exists") from exc

    def record_state(
        self,
        state_data: dict[str, Any],
        timezone: str = "UTC",
        *,
        force_flush: bool = False,
    ) -> None:
        record_tuple = self._build_record_tuple(state_data, timezone)

        with self._pending_lock:
            self._pending_records.append(record_tuple)

            if len(self._pending_records) >= self._batch_size:
                self._flush_pending_records_locked()
            else:
                self._schedule_flush_timer_locked()

        if force_flush:
            self.flush_pending_records(force=True)

    def get_history(
        self,
        start: dt.datetime,
        end: dt.datetime,
        metrics: Optional[list[str]] = None,
        granularity: str = "minute",
        limit: int = 1000,
    ) -> list[dict[str, Any]]:
        if metrics is None:
            metrics = [
                "timestamp",
                "temperature",
                "humidity",
                "assumed_aircon_power",
                "last_action",
                "api_requests_today",
                "error_count",
                "last_temperature_stale",
            ]

        # Build time bucket expression based on granularity
        time_bucket = self._get_time_bucket_expression(granularity)

        # Build SELECT clause
        select_fields = []
        timestamp_included = False
        
        for metric in metrics:
            if metric == "timestamp":
                select_fields.append(sql.SQL("date_trunc(%s, timestamp) as timestamp"))
                timestamp_included = True
            elif metric in ["temperature", "humidity"]:
                select_fields.append(sql.SQL("AVG({}) as {}").format(
                    sql.Identifier(metric), sql.Identifier(metric)
                ))
            elif metric == "assumed_aircon_power":
                select_fields.append(sql.SQL("MODE() WITHIN GROUP (ORDER BY assumed_aircon_power) as assumed_aircon_power"))
            elif metric == "last_action":
                select_fields.append(sql.SQL("MODE() WITHIN GROUP (ORDER BY last_action) as last_action"))
            elif metric == "api_requests_today":
                select_fields.append(sql.SQL("MAX(api_requests_today) as api_requests_today"))
            elif metric == "error_count":
                select_fields.append(sql.SQL("SUM(error_count) as error_count"))
            elif metric == "last_temperature_stale":
                select_fields.append(sql.SQL("BOOL_OR(last_temperature_stale) as last_temperature_stale"))

        # Always include timestamp for ordering
        if not timestamp_included:
            select_fields.insert(0, sql.SQL("date_trunc(%s, timestamp) as timestamp"))

        # If no metrics specified, return empty result
        if not select_fields:
            self._logger.warning("[history] No valid metrics specified: %s", metrics)
            return []

        # Build query using subqueries for each metric to avoid GROUP BY issues
        if not metrics:
            self._logger.warning("[history] No valid metrics specified: %s", metrics)
            return []

        # For now, implement a simple approach without aggregation
        # Get raw data and let frontend handle the aggregation
        select_fields_raw = []
        
        # Always include timestamp
        select_fields_raw.append(sql.SQL("timestamp"))
        
        for metric in metrics:
            if metric in ["temperature", "humidity", "assumed_aircon_power", "last_action", "api_requests_today", "error_count", "last_temperature_stale"]:
                select_fields_raw.append(sql.Identifier(metric))

        query = sql.SQL("""
            SELECT {}
            FROM state_history
            WHERE timestamp >= %s AND timestamp < %s
            ORDER BY timestamp DESC
            LIMIT %s
        """).format(
            sql.SQL(", ").join(select_fields_raw)
        )

        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    # Simple parameters: start + end + limit
                    params = [start, end, limit]
                    cur.execute(query, params)
                    results = cur.fetchall()

                    # Convert datetime objects to ISO strings for JSON serialization
                    for result in results:
                        if "timestamp" in result and result["timestamp"]:
                            result["timestamp"] = result["timestamp"].isoformat()

                    self._logger.debug("[history] Retrieved %d records", len(results))
                    return results

        except Exception as exc:
            self._logger.error("[history] Failed to retrieve history (%s)", exc)
            raise HistoryServiceError("Failed to retrieve historical data") from exc

    def get_aggregates(self, period_hours: int = 1) -> dict[str, Any]:
        """
        Get aggregated statistics for a recent period.

        Args:
            period_hours: Number of hours to aggregate (default: 1)

        Returns:
            Dictionary with aggregated metrics

        Raises:
            HistoryServiceError: If aggregation fails
        """
        query = sql.SQL("""
            SELECT 
                COUNT(*) as total_records,
                AVG(temperature) as avg_temperature,
                MIN(temperature) as min_temperature,
                MAX(temperature) as max_temperature,
                AVG(humidity) as avg_humidity,
                MIN(humidity) as min_humidity,
                MAX(humidity) as max_humidity,
                MODE() WITHIN GROUP (ORDER BY assumed_aircon_power) as common_aircon_state,
                COUNT(DISTINCT last_action) as distinct_actions,
                SUM(error_count) as total_errors,
                MAX(api_requests_today) as max_api_requests
            FROM state_history
            WHERE timestamp >= NOW() - make_interval(hours => %s)
        """)

        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, (period_hours,))
                    result = cur.fetchone()
                    return result or {}

        except Exception as exc:
            self._logger.error("[history] Failed to get aggregates (%s)", exc)
            raise HistoryServiceError("Failed to get aggregated statistics") from exc

    def cleanup_old_records(self) -> int:
        delete_query = sql.SQL("""
            DELETE FROM state_history
            WHERE timestamp < NOW() - make_interval(hours => %s)
        """)

        try:
            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(delete_query, (self._retention_hours,))
                    deleted_count = cur.rowcount
                    conn.commit()
                    self._logger.info("[history] Cleaned up %d old records", deleted_count)
                    return deleted_count

        except Exception as exc:
            self._logger.error("[history] Failed to cleanup old records (%s)", exc)
            raise HistoryServiceError("Failed to cleanup old records") from exc

    def flush_pending_records(self, *, force: bool = False) -> int:
        """Flush buffered records to PostgreSQL."""
        with self._pending_lock:
            if not self._pending_records:
                return 0

            if not force and len(self._pending_records) < self._batch_size:
                return 0

            return self._flush_pending_records_locked()

    def _build_record_tuple(
        self,
        state_data: dict[str, Any],
        timezone: str,
    ) -> tuple[Any, ...]:
        temperature = state_data.get("last_temperature")
        humidity = state_data.get("last_humidity")
        aircon_power = state_data.get("assumed_aircon_power", "unknown")
        last_action = state_data.get("last_action")
        api_requests = state_data.get("api_requests_today", 0)
        error_count = state_data.get("error_count", 0)
        temp_stale = state_data.get("last_temperature_stale", False)

        metadata = {
            "last_read_at": state_data.get("last_read_at"),
            "last_tick": state_data.get("last_tick"),
            "automation_active": state_data.get("automation_active"),
            "pending_off_repeat": state_data.get("pending_off_repeat"),
        }

        return (
            temperature,
            humidity,
            aircon_power,
            last_action,
            api_requests,
            error_count,
            temp_stale,
            timezone,
            Jsonb(metadata),
        )

    def _schedule_flush_timer_locked(self) -> None:
        """Schedule a timer-based flush if needed (lock must be held)."""
        if self._flush_interval_seconds <= 0:
            return

        if self._flush_timer is not None:
            return

        timer = threading.Timer(self._flush_interval_seconds, self._flush_due)
        timer.daemon = True
        timer.start()
        self._flush_timer = timer

    def _flush_due(self) -> None:
        """Flush callback triggered by the timer."""
        with self._pending_lock:
            self._flush_timer = None
            if not self._pending_records:
                return

            try:
                self._flush_pending_records_locked()
            except HistoryServiceError as exc:
                self._logger.error("[history] Timed flush failed (%s)", exc)

    def _cancel_flush_timer_locked(self) -> None:
        """Cancel the scheduled flush timer if it exists."""
        if self._flush_timer is not None:
            self._flush_timer.cancel()
            self._flush_timer = None

    def _flush_pending_records_locked(self) -> int:
        """Flush pending records to PostgreSQL (lock must be held)."""
        if not self._pending_records:
            return 0

        records = list(self._pending_records)
        self._pending_records.clear()
        self._cancel_flush_timer_locked()

        column_count = len(records[0])
        placeholders = "(" + ", ".join(["%s"] * column_count) + ")"
        values_segment = ", ".join([placeholders] * len(records))
        insert_query = sql.SQL(
            """
            INSERT INTO state_history (
                temperature, humidity, assumed_aircon_power, last_action,
                api_requests_today, error_count, last_temperature_stale,
                timezone, metadata
            ) VALUES {}
            """
        ).format(sql.SQL(values_segment))
        flat_params: list[Any] = []
        for record in records:
            flat_params.extend(record)

        try:
            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(insert_query, flat_params)
                    conn.commit()
                    self._logger.debug(
                        "[history] Flushed %d buffered records", len(records)
                    )
        except Exception as exc:
            self._logger.error("[history] Failed to flush records (%s)", exc)
            raise HistoryServiceError("Failed to flush buffered records") from exc

        return len(records)

    def _get_time_bucket_expression(self, granularity: str) -> sql.SQL:
        """Get PostgreSQL time bucket expression for given granularity."""
        granularity_map = {
            "minute": "minute",
            "5min": "5 minutes",
            "15min": "15 minutes",
            "hour": "hour",
        }
        bucket = granularity_map.get(granularity, "minute")
        return sql.SQL("date_trunc(%s, timestamp)").format(sql.Literal(bucket))

    def get_latest_records(self, limit: int = 10) -> list[dict[str, Any]]:
        """
        Get the most recent records.

        Args:
            limit: Maximum number of records to return

        Returns:
            List of recent records

        Raises:
            HistoryServiceError: If retrieval fails
        """
        query = sql.SQL("""
            SELECT *
            FROM state_history
            ORDER BY timestamp DESC
            LIMIT %s
        """)

        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, (limit,))
                    results = cur.fetchall()

                    # Convert datetime objects to ISO strings
                    for result in results:
                        if "timestamp" in result and result["timestamp"]:
                            result["timestamp"] = result["timestamp"].isoformat()
                        if "metadata" in result and result["metadata"]:
                            result["metadata"] = dict(result["metadata"])

                    return results

        except Exception as exc:
            self._logger.error("[history] Failed to get latest records (%s)", exc)
            raise HistoryServiceError("Failed to get latest records") from exc
