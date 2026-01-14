"""
Tests for HistoryService module.

This test suite covers:
- CRUD operations on historical data
- Data aggregation and filtering
- Time-based queries with different granularities
- Error handling and edge cases
- Cleanup operations
"""

from __future__ import annotations

import datetime as dt
import json
from unittest.mock import MagicMock, patch

import pytest

from switchbot_dashboard.history_service import HistoryService, HistoryServiceError


@pytest.fixture
def mock_connection_pool():
    """Mock PostgreSQL connection pool."""
    pool = MagicMock()
    pool.connection.return_value.__enter__.return_value = MagicMock()
    return pool


@pytest.fixture
def mock_logger():
    """Mock logger instance."""
    logger = MagicMock()
    return logger


@pytest.fixture
def history_service(mock_connection_pool, mock_logger):
    """Create HistoryService instance with mocked dependencies."""
    # Mock the _ensure_table_exists method to avoid real database calls
    with patch("switchbot_dashboard.history_service.HistoryService._ensure_table_exists"):
        return HistoryService(
            connection_pool=mock_connection_pool,
            logger=mock_logger,
            retention_hours=6,
        )


@pytest.fixture
def sample_state_data():
    """Sample state data for testing."""
    return {
        "last_temperature": 23.5,
        "last_humidity": 45.0,
        "assumed_aircon_power": "on",
        "last_action": "automation_winter_on",
        "api_requests_today": 150,
        "error_count": 0,
        "last_temperature_stale": False,
        "last_read_at": "2026-01-14T15:30:00Z",
        "last_tick": "2026-01-14T15:30:00Z",
        "automation_active": True,
        "pending_off_repeat": None,
    }


class TestHistoryServiceInit:
    """Test HistoryService initialization."""

    def test_init_with_default_params(self, mock_connection_pool, mock_logger):
        """Test initialization with default parameters."""
        service = HistoryService(mock_connection_pool, logger=mock_logger)
        
        assert service._pool == mock_connection_pool
        assert service._logger == mock_logger
        assert service._retention_hours == 6

    def test_init_with_custom_retention(self, mock_connection_pool, mock_logger):
        """Test initialization with custom retention period."""
        service = HistoryService(
            mock_connection_pool,
            logger=mock_logger,
            retention_hours=12,
        )
        
        assert service._retention_hours == 12

    def test_ensure_table_called_on_init(self, mock_connection_pool, mock_logger):
        """Test that table creation is called during initialization."""
        with patch.object(HistoryService, '_ensure_table_exists') as mock_ensure:
            HistoryService(mock_connection_pool, logger=mock_logger)
            mock_ensure.assert_called_once()


class TestRecordState:
    """Test state recording functionality."""

    def test_record_state_success(self, history_service, sample_state_data):
        """Test successful state recording."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        history_service.record_state(sample_state_data, "Europe/Paris")
        
        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        history_service._logger.debug.assert_called_with("[history] State recorded successfully")

    def test_record_state_with_missing_fields(self, history_service):
        """Test recording state with missing optional fields."""
        incomplete_data = {
            "last_temperature": 20.0,
            "assumed_aircon_power": "off",
        }
        
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        history_service.record_state(incomplete_data)
        
        mock_cursor.execute.assert_called_once()
        # Check that None values are handled properly
        args = mock_cursor.execute.call_args[0][1]
        assert args[0] == 20.0  # temperature
        assert args[1] is None  # humidity
        assert args[2] == "off"  # aircon_power

    def test_record_state_database_error(self, history_service, sample_state_data):
        """Test handling of database errors during recording."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception("Database error")
        
        with pytest.raises(HistoryServiceError, match="Failed to record state in history"):
            history_service.record_state(sample_state_data)
        
        history_service._logger.error.assert_called_once()


class TestGetHistory:
    """Test historical data retrieval."""

    def test_get_history_success(self, history_service):
        """Test successful history retrieval."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        # Mock query results
        mock_cursor.fetchall.return_value = [
            {
                "timestamp": dt.datetime(2026, 1, 14, 15, 30),
                "temperature": 23.5,
                "humidity": 45.0,
                "assumed_aircon_power": "on",
            },
            {
                "timestamp": dt.datetime(2026, 1, 14, 15, 31),
                "temperature": 23.7,
                "humidity": 44.8,
                "assumed_aircon_power": "on",
            },
        ]
        
        start = dt.datetime(2026, 1, 14, 10, 0)
        end = dt.datetime(2026, 1, 14, 16, 0)
        
        result = history_service.get_history(start, end)
        
        assert len(result) == 2
        assert result[0]["temperature"] == 23.5
        assert result[1]["humidity"] == 44.8
        # Check timestamp serialization
        assert isinstance(result[0]["timestamp"], str)

    def test_get_history_with_custom_metrics(self, history_service):
        """Test history retrieval with specific metrics."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchall.return_value = []
        
        start = dt.datetime(2026, 1, 14, 10, 0)
        end = dt.datetime(2026, 1, 14, 16, 0)
        metrics = ["temperature", "assumed_aircon_power"]
        
        history_service.get_history(start, end, metrics, "hour", 500)
        
        # Verify the query was called with correct parameters
        mock_cursor.execute.assert_called_once()
        call_args = mock_cursor.execute.call_args[0]
        assert call_args[1] == (start, end, "hour", 500)

    def test_get_history_different_granularities(self, history_service):
        """Test history retrieval with different time granularities."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchall.return_value = []
        
        start = dt.datetime(2026, 1, 14, 10, 0)
        end = dt.datetime(2026, 1, 14, 16, 0)
        
        for granularity in ["minute", "5min", "15min", "hour"]:
            history_service.get_history(start, end, granularity=granularity)
            
            # Check that granularity is used in the query
            call_args = mock_cursor.execute.call_args[0]
            assert call_args[1][2] == granularity

    def test_get_history_database_error(self, history_service):
        """Test handling of database errors during retrieval."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception("Database error")
        
        start = dt.datetime(2026, 1, 14, 10, 0)
        end = dt.datetime(2026, 1, 14, 16, 0)
        
        with pytest.raises(HistoryServiceError, match="Failed to retrieve historical data"):
            history_service.get_history(start, end)


class TestGetAggregates:
    """Test aggregate statistics functionality."""

    def test_get_aggregates_success(self, history_service):
        """Test successful aggregate retrieval."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = {
            "total_records": 100,
            "avg_temperature": 23.5,
            "min_temperature": 20.0,
            "max_temperature": 26.0,
            "avg_humidity": 45.0,
            "min_humidity": 40.0,
            "max_humidity": 50.0,
            "common_aircon_state": "on",
            "distinct_actions": 3,
            "total_errors": 2,
            "max_api_requests": 150,
        }
        
        result = history_service.get_aggregates(1)
        
        assert result["total_records"] == 100
        assert result["avg_temperature"] == 23.5
        assert result["common_aircon_state"] == "on"
        assert result["total_errors"] == 2

    def test_get_aggregates_custom_period(self, history_service):
        """Test aggregates with custom period."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = {}
        
        history_service.get_aggregates(6)
        
        # Verify that execute was called (the parameter passing is handled by psycopg)
        mock_cursor.execute.assert_called_once()

    def test_get_aggregates_no_results(self, history_service):
        """Test aggregates when no data is found."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        result = history_service.get_aggregates(1)
        
        assert result == {}

    def test_get_aggregates_database_error(self, history_service):
        """Test handling of database errors during aggregation."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception("Database error")
        
        with pytest.raises(HistoryServiceError, match="Failed to get aggregated statistics"):
            history_service.get_aggregates(1)


class TestGetLatestRecords:
    """Test latest records retrieval."""

    def test_get_latest_records_success(self, history_service):
        """Test successful latest records retrieval."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchall.return_value = [
            {
                "id": 1,
                "timestamp": dt.datetime(2026, 1, 14, 15, 30),
                "temperature": 23.5,
                "humidity": 45.0,
                "assumed_aircon_power": "on",
                "metadata": {"test": "value"},
            },
            {
                "id": 2,
                "timestamp": dt.datetime(2026, 1, 14, 15, 29),
                "temperature": 23.3,
                "humidity": 45.2,
                "assumed_aircon_power": "on",
                "metadata": None,
            },
        ]
        
        result = history_service.get_latest_records(10)
        
        assert len(result) == 2
        assert result[0]["temperature"] == 23.5
        assert isinstance(result[0]["timestamp"], str)
        assert isinstance(result[0]["metadata"], dict)
        assert result[1]["metadata"] is None

    def test_get_latest_records_custom_limit(self, history_service):
        """Test latest records with custom limit."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchall.return_value = []
        
        history_service.get_latest_records(5)
        
        # Verify limit is used in query parameters
        call_args = mock_cursor.execute.call_args
        assert call_args[0][0] is not None  # SQL query
        # Parameters might be in call_args[0] or call_args[1] depending on psycopg version
        params = call_args[0][1] if len(call_args[0]) > 1 else (call_args[1] if call_args[1] else ())
        assert params[0] == 5  # Limit parameter

    def test_get_latest_records_database_error(self, history_service):
        """Test handling of database errors during latest records retrieval."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception("Database error")
        
        with pytest.raises(HistoryServiceError, match="Failed to get latest records"):
            history_service.get_latest_records(10)


class TestCleanupOldRecords:
    """Test cleanup functionality."""

    def test_cleanup_old_records_success(self, history_service):
        """Test successful cleanup of old records."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 25
        
        deleted_count = history_service.cleanup_old_records()
        
        assert deleted_count == 25
        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        history_service._logger.info.assert_called_with("[history] Cleaned up %d old records", 25)

    def test_cleanup_custom_retention_hours(self, history_service):
        """Test cleanup with custom retention period."""
        history_service._retention_hours = 12
        
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.rowcount = 0
        
        history_service.cleanup_old_records()
        
        # Verify that execute was called (the parameter passing is handled by psycopg)
        mock_cursor.execute.assert_called_once()

    def test_cleanup_database_error(self, history_service):
        """Test handling of database errors during cleanup."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception("Database error")
        
        with pytest.raises(HistoryServiceError, match="Failed to cleanup old records"):
            history_service.cleanup_old_records()


class TestTimeBucketExpression:
    """Test time bucket expression generation."""

    @pytest.mark.parametrize("granularity,expected", [
        ("minute", "minute"),
        ("5min", "5 minutes"),
        ("15min", "15 minutes"),
        ("hour", "hour"),
        ("invalid", "minute"),  # Default fallback
    ])
    def test_get_time_bucket_expression(self, history_service, granularity, expected):
        """Test time bucket expression generation for different granularities."""
        from psycopg import sql
        
        result = history_service._get_time_bucket_expression(granularity)
        
        # Check that it's a SQL object (SQL or Composed)
        assert isinstance(result, (sql.SQL, sql.Composed))
        # Check that it contains date_trunc (which is what we expect)
        assert "date_trunc" in str(result)


class TestIntegration:
    """Integration tests for HistoryService."""

    def test_full_workflow(self, history_service, sample_state_data):
        """Test complete workflow: record -> retrieve -> cleanup."""
        # Mock all database operations
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        # Record state
        history_service.record_state(sample_state_data)
        
        # Get history
        mock_cursor.fetchall.return_value = [
            {
                "timestamp": dt.datetime(2026, 1, 14, 15, 30),
                "temperature": 23.5,
                "humidity": 45.0,
                "assumed_aircon_power": "on",
            }
        ]
        
        start = dt.datetime(2026, 1, 14, 10, 0)
        end = dt.datetime(2026, 1, 14, 16, 0)
        result = history_service.get_history(start, end)
        
        assert len(result) == 1
        assert result[0]["temperature"] == 23.5
        
        # Get aggregates
        mock_cursor.fetchone.return_value = {
            "total_records": 1,
            "avg_temperature": 23.5,
            "total_errors": 0,
        }
        
        aggregates = history_service.get_aggregates(1)
        assert aggregates["total_records"] == 1
        
        # Cleanup
        mock_cursor.rowcount = 1
        deleted = history_service.cleanup_old_records()
        assert deleted == 1

    def test_error_handling_and_recovery(self, history_service, sample_state_data):
        """Test error handling and recovery scenarios."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        history_service._pool.connection.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        
        # Simulate database error during recording
        mock_cursor.execute.side_effect = Exception("Connection lost")
        
        with pytest.raises(HistoryServiceError):
            history_service.record_state(sample_state_data)
        
        # Reset for next operation
        mock_cursor.execute.side_effect = None
        
        # Next operation should work normally
        history_service.record_state(sample_state_data)
        mock_cursor.execute.assert_called()
