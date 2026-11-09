from __future__ import annotations

import datetime as dt
import logging
import threading
from typing import Any, Optional

from psycopg import sql
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb
from psycopg_pool import ConnectionPool



class HistoryServiceError(RuntimeError):
    """Raised when history service operations fail."""


class HistoryService:
    """Service for collecting and retrieving historical monitoring data."""

    def __init__(
        self,
        connection_pool: ConnectionPool,
        *,
        logger: logging.Logger,
        retention_hours: int = 24,
        batch_size: int = 4,
        flush_interval_seconds: int = 60,
    ) -> None:
        """
        Initialize history service with PostgreSQL connection pool.

        Args:
            connection_pool: PostgreSQL connection pool from PostgresStore
            logger: Logger instance for error reporting
            retention_hours: Data retention period (default: 24 hours so the UI
                "last 24h" range is fully covered).
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
                last_action VARCHAR(255),
                api_requests_today INTEGER DEFAULT 0,
                error_count INTEGER DEFAULT 0,
                last_temperature_stale BOOLEAN DEFAULT FALSE,
                timezone VARCHAR(50) DEFAULT 'UTC',
                metadata JSONB DEFAULT '{}'
            );
            CREATE INDEX IF NOT EXISTS idx_state_history_timestamp ON state_history(timestamp DESC);
            CREATE INDEX IF NOT EXISTS idx_state_history_aircon_power ON state_history(assumed_aircon_power);
        """)

        try:
            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(create_table_query)
                    cur.execute("""
                        SELECT character_maximum_length 
                        FROM information_schema.columns 
                        WHERE table_name = 'state_history' AND column_name = 'last_action';
                    """)
                    row = cur.fetchone()
                    if row and row[0] != 255:
                        cur.execute("ALTER TABLE state_history ALTER COLUMN last_action TYPE VARCHAR(255);")
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

        should_flush = False
        with self._pending_lock:
            self._pending_records.append(record_tuple)

            if len(self._pending_records) >= self._batch_size:
                should_flush = True
            else:
                self._schedule_flush_timer_locked()

        if should_flush or force_flush:
            self.flush_pending_records(force=True)

    def _build_select_fields(self, metrics: list[str], time_bucket: sql.SQL) -> list[sql.SQL]:
        select_fields = []
        timestamp_included = False
        
        for metric in metrics:
            if metric == "timestamp":
                select_fields.append(sql.SQL("{} as timestamp").format(time_bucket))
                timestamp_included = True
            elif metric in ["temperature", "humidity"]:
                select_fields.append(sql.SQL("ROUND(AVG({})::numeric, 1) as {}").format(
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

        if not timestamp_included:
            select_fields.insert(0, sql.SQL("{} as timestamp").format(time_bucket))
            
        return select_fields

    def _format_history_results(self, results: list[dict[str, Any]]) -> list[dict[str, Any]]:
        from decimal import Decimal
        for result in results:
            if "timestamp" in result and result["timestamp"]:
                result["timestamp"] = result["timestamp"].isoformat()
            for k, v in result.items():
                if isinstance(v, Decimal):
                    result[k] = float(v)
        return results

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
                "timestamp", "temperature", "humidity", "assumed_aircon_power",
                "last_action", "api_requests_today", "error_count", "last_temperature_stale",
            ]

        time_bucket = self._get_time_bucket_expression(granularity)
        select_fields = self._build_select_fields(metrics, time_bucket)

        if not select_fields:
            self._logger.warning("[history] No valid metrics specified")
            return []

        query = sql.SQL("""
            SELECT {fields}
            FROM state_history
            WHERE timestamp >= %s AND timestamp < %s
            GROUP BY {bucket}
            ORDER BY timestamp DESC
            LIMIT %s
        """).format(
            fields=sql.SQL(", ").join(select_fields),
            bucket=time_bucket
        )

        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, [start, end, limit])
                    results = cur.fetchall()
                    formatted_results = self._format_history_results(results)
                    self._logger.debug("[history] Retrieved %d records", len(formatted_results))
                    return formatted_results

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
        from decimal import Decimal

        query = sql.SQL("""
            SELECT 
                COUNT(*) as total_records,
                ROUND(AVG(temperature)::numeric, 1) as avg_temperature,
                MIN(temperature) as min_temperature,
                MAX(temperature) as max_temperature,
                ROUND(AVG(humidity)::numeric, 1) as avg_humidity,
                MIN(humidity) as min_humidity,
                MAX(humidity) as max_humidity,
                MODE() WITHIN GROUP (ORDER BY assumed_aircon_power) as common_aircon_state,
                COUNT(DISTINCT last_action) as distinct_actions,
                COALESCE(SUM(error_count), 0) as total_errors,
                COALESCE(MAX(api_requests_today), 0) as max_api_requests
            FROM state_history
            WHERE timestamp >= NOW() - make_interval(hours => %s)
        """)

        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, (period_hours,))
                    result = cur.fetchone()
                    if not result:
                        return {}
                    return {
                        key: float(value) if isinstance(value, Decimal) else value
                        for key, value in result.items()
                    }

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
        """Flush buffered records without holding the lock during network I/O."""
        with self._pending_lock:
            if not self._pending_records:
                return 0

            if not force and len(self._pending_records) < self._batch_size:
                return 0

            records = list(self._pending_records)
            self._pending_records.clear()
            self._cancel_flush_timer_locked()

        try:
            self._insert_records(records)
        except Exception as exc:
            with self._pending_lock:
                # Preserve ordering: failed records must be retried before
                # records appended while the INSERT was in flight.
                self._pending_records = records + self._pending_records
                max_cache = 100
                if len(self._pending_records) > max_cache:
                    self._logger.warning(
                        "[history] Buffer limit exceeded (%d > %d), discarding oldest records",
                        len(self._pending_records),
                        max_cache,
                    )
                    self._pending_records = self._pending_records[-max_cache:]

                # Reschedule the timer to retry later
                self._schedule_flush_timer_locked()

            self._logger.error("[history] Failed to flush records (%s)", exc)
            raise HistoryServiceError("Failed to flush buffered records") from exc

        return len(records)

    def _build_record_tuple(
        self,
        state_data: dict[str, Any],
        timezone: str,
    ) -> tuple[Any, ...]:
        timestamp = dt.datetime.now(dt.timezone.utc)
        temperature = state_data.get("last_temperature")
        humidity = state_data.get("last_humidity")
        aircon_power = state_data.get("assumed_aircon_power", "unknown")
        last_action = state_data.get("last_action")
        # Mapping: the state store holds "api_requests_total" (authoritative estimate),
        # which is recorded in the "api_requests_today" database column for historical schema compatibility.
        api_requests = state_data.get("api_requests_total", 0)
        error_count = state_data.get("error_count", 0)
        temp_stale = state_data.get("last_temperature_stale", False)

        metadata = {
            "last_read_at": state_data.get("last_read_at"),
            "last_tick": state_data.get("last_tick"),
            "automation_active": state_data.get("automation_active"),
            "pending_off_repeat": state_data.get("pending_off_repeat"),
            "assumed_aircon_mode": state_data.get("assumed_aircon_mode"),
        }

        return (
            timestamp,
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
        """Flush callback triggered by the timer, outside the lock."""
        with self._pending_lock:
            self._flush_timer = None
            if not self._pending_records:
                return

        try:
            self.flush_pending_records(force=True)
        except HistoryServiceError as exc:
            self._logger.error("[history] Timed flush failed (%s)", exc)

    def _cancel_flush_timer_locked(self) -> None:
        """Cancel the scheduled flush timer if it exists."""
        if self._flush_timer is not None:
            self._flush_timer.cancel()
            self._flush_timer = None

    def _insert_records(self, records: list[tuple[Any, ...]]) -> None:
        """Insert a batch of records. Must be called without ``_pending_lock``."""
        if not records:
            return

        column_count = len(records[0])
        placeholders = "(" + ", ".join(["%s"] * column_count) + ")"
        values_segment = ", ".join([placeholders] * len(records))
        insert_query = sql.SQL(
            """
            INSERT INTO state_history (
                timestamp, temperature, humidity, assumed_aircon_power, last_action,
                api_requests_today, error_count, last_temperature_stale,
                timezone, metadata
            ) VALUES {}
            """
        ).format(sql.SQL(values_segment))
        flat_params: list[Any] = []
        for record in records:
            flat_params.extend(record)

        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(insert_query, flat_params)
                conn.commit()

        self._logger.debug("[history] Flushed %d buffered records", len(records))

    def _get_time_bucket_expression(self, granularity: str) -> sql.SQL:
        """Get PostgreSQL time bucket expression for given granularity."""
        if granularity == "5min":
            return sql.SQL("date_trunc('hour', timestamp) + floor(extract(minute from timestamp) / 5) * 5 * interval '1 minute'")
        elif granularity == "15min":
            return sql.SQL("date_trunc('hour', timestamp) + floor(extract(minute from timestamp) / 15) * 15 * interval '1 minute'")

        granularity_map = {
            "minute": "minute",
            "hour": "hour",
            "day": "day",
        }
        bucket = granularity_map.get(granularity, "minute")
        return sql.SQL("date_trunc({}, timestamp)").format(sql.Literal(bucket))

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
        from decimal import Decimal

        # Restrict the sort to a small indexed window before deduplicating by
        # minute. The previous query sorted the whole table on every refresh.
        query = sql.SQL("""
            SELECT DISTINCT ON (date_trunc('minute', sub.timestamp)) sub.*
            FROM (
                SELECT *
                FROM state_history
                ORDER BY timestamp DESC
                LIMIT %s
            ) sub
            ORDER BY date_trunc('minute', sub.timestamp) DESC, sub.timestamp DESC
            LIMIT %s
        """)

        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, (max(limit * 60, 600), limit))
                    results = cur.fetchall()

                    # Convert datetime objects to ISO strings
                    for result in results:
                        if "timestamp" in result and result["timestamp"]:
                            result["timestamp"] = result["timestamp"].isoformat()
                        if "metadata" in result and result["metadata"]:
                            result["metadata"] = dict(result["metadata"])
                        for key, value in result.items():
                            if isinstance(value, Decimal):
                                result[key] = float(value)

                    return results

        except Exception as exc:
            self._logger.error("[history] Failed to get latest records (%s)", exc)
            raise HistoryServiceError("Failed to get latest records") from exc
