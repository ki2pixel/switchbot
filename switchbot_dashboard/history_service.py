from __future__ import annotations

import datetime as dt
import json
import logging
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
    ) -> None:
        """
        Initialize history service with PostgreSQL connection pool.

        Args:
            connection_pool: PostgreSQL connection pool from PostgresStore
            logger: Logger instance for error reporting
            retention_hours: Data retention period (default: 6 hours for Neon PITR)
        """
        self._pool = connection_pool
        self._logger = logger
        self._retention_hours = retention_hours
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
            CREATE INDEX IF NOT EXISTS idx_state_history_date_bucket ON state_history(date_trunc('hour', timestamp));
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

    def record_state(self, state_data: dict[str, Any], timezone: str = "UTC") -> None:
        """
        Record a new state snapshot in history.

        Args:
            state_data: State dictionary from automation service
            timezone: Timezone used for timestamp calculations

        Raises:
            HistoryServiceError: If recording fails
        """
        insert_query = sql.SQL("""
            INSERT INTO state_history (
                temperature, humidity, assumed_aircon_power, last_action,
                api_requests_today, error_count, last_temperature_stale,
                timezone, metadata
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """)

        try:
            # Extract relevant fields from state data
            temperature = state_data.get("last_temperature")
            humidity = state_data.get("last_humidity")
            aircon_power = state_data.get("assumed_aircon_power", "unknown")
            last_action = state_data.get("last_action")
            api_requests = state_data.get("api_requests_today", 0)
            error_count = state_data.get("error_count", 0)
            temp_stale = state_data.get("last_temperature_stale", False)

            # Prepare metadata with additional fields
            metadata = {
                "last_read_at": state_data.get("last_read_at"),
                "last_tick": state_data.get("last_tick"),
                "automation_active": state_data.get("automation_active"),
                "pending_off_repeat": state_data.get("pending_off_repeat"),
            }

            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        insert_query,
                        (
                            temperature,
                            humidity,
                            aircon_power,
                            last_action,
                            api_requests,
                            error_count,
                            temp_stale,
                            timezone,
                            Jsonb(metadata),
                        ),
                    )
                    conn.commit()
                    self._logger.debug("[history] State recorded successfully")

        except Exception as exc:
            self._logger.error("[history] Failed to record state (%s)", exc)
            raise HistoryServiceError("Failed to record state in history") from exc

    def get_history(
        self,
        start: dt.datetime,
        end: dt.datetime,
        metrics: Optional[list[str]] = None,
        granularity: str = "minute",
        limit: int = 1000,
    ) -> list[dict[str, Any]]:
        """
        Retrieve historical data with optional filtering and aggregation.

        Args:
            start: Start datetime (inclusive)
            end: End datetime (exclusive)
            metrics: List of metrics to retrieve (default: all)
            granularity: Time granularity ('minute', '5min', '15min', 'hour')
            limit: Maximum number of records to return

        Returns:
            List of historical records

        Raises:
            HistoryServiceError: If retrieval fails
        """
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
        for metric in metrics:
            if metric == "timestamp":
                select_fields.append(sql.SQL("date_trunc(%s, timestamp) as timestamp").format(
                    sql.Literal(granularity)
                ))
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

        query = sql.SQL("""
            SELECT {}
            FROM state_history
            WHERE timestamp >= %s AND timestamp < %s
            GROUP BY date_trunc(%s, timestamp)
            ORDER BY timestamp DESC
            LIMIT %s
        """).format(
            sql.SQL(", ").join(select_fields),
            sql.Literal(granularity),
            sql.Literal(limit)
        )

        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, (start, end, granularity, limit))
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
            WHERE timestamp >= NOW() - INTERVAL '%s hours'
        """).format(sql.Literal(period_hours))

        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query)
                    result = cur.fetchone()
                    return result or {}

        except Exception as exc:
            self._logger.error("[history] Failed to get aggregates (%s)", exc)
            raise HistoryServiceError("Failed to get aggregated statistics") from exc

    def cleanup_old_records(self) -> int:
        """
        Clean up records older than retention period.

        Returns:
            Number of records deleted

        Raises:
            HistoryServiceError: If cleanup fails
        """
        delete_query = sql.SQL("""
            DELETE FROM state_history
            WHERE timestamp < NOW() - INTERVAL '%s hours'
        """).format(sql.Literal(self._retention_hours))

        try:
            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(delete_query)
                    deleted_count = cur.rowcount
                    conn.commit()
                    self._logger.info("[history] Cleaned up %d old records", deleted_count)
                    return deleted_count

        except Exception as exc:
            self._logger.error("[history] Failed to cleanup old records (%s)", exc)
            raise HistoryServiceError("Failed to cleanup old records") from exc

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
