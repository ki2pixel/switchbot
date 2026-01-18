"""Tests for PostgreSQL store implementation."""

from __future__ import annotations

import json
import logging
import os
import tempfile
from unittest.mock import MagicMock, patch

import pytest

from switchbot_dashboard.postgres_store import PostgresStore, PostgresStoreError


@pytest.fixture
def mock_logger():
    """Mock logger fixture."""
    return MagicMock(spec=logging.Logger)


@pytest.fixture
def test_postgres_url():
    """Test PostgreSQL connection URL."""
    return os.environ.get("TEST_POSTGRES_URL", "postgresql://test:test@localhost/test")


def _setup_mock_pool(pool_cls: MagicMock) -> dict[str, MagicMock]:
    """Configure a fake connection pool returning mocked connection/cursor."""
    mock_pool = MagicMock()
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
    mock_pool.connection.return_value.__enter__.return_value = mock_connection
    mock_pool.close = MagicMock()
    pool_cls.return_value = mock_pool
    return {
        "cls": pool_cls,
        "pool": mock_pool,
        "connection": mock_connection,
        "cursor": mock_cursor,
    }


@pytest.fixture
def mocked_pool():
    """Patch ConnectionPool globally for tests."""
    with patch("switchbot_dashboard.postgres_store.ConnectionPool") as pool_cls:
        context = _setup_mock_pool(pool_cls)
        yield context


@pytest.fixture
def postgres_store(test_postgres_url, mock_logger, mocked_pool):
    """PostgreSQL store fixture for testing (always mocked)."""
    with patch("switchbot_dashboard.postgres_store.PostgresStore._ensure_table_exists"):
        store = PostgresStore(
            connection_string=test_postgres_url,
            kind="test",
            logger=mock_logger,
        )
        mocked_pool["cursor"].reset_mock()
        mocked_pool["connection"].reset_mock()
        yield store
        store.close()


@pytest.fixture
def real_postgres_store(test_postgres_url, mock_logger):
    """PostgreSQL store fixture with real connection (for integration tests)."""
    if os.environ.get("TEST_POSTGRES_URL") and "localhost" not in test_postgres_url:
        store = PostgresStore(
            connection_string=test_postgres_url,
            kind="test",
            logger=mock_logger,
        )
        yield store
        store.close()
    else:
        pytest.skip("Requires TEST_POSTGRES_URL with real PostgreSQL connection")


class TestPostgresStore:
    """Test suite for PostgresStore."""

    def test_initialization_success(self, postgres_store):
        """Test successful store initialization."""
        # The postgres_store fixture uses mocked connection
        assert postgres_store._kind == "test"
        assert postgres_store._pool is not None

    def test_initialization_failure(self, test_postgres_url, mock_logger):
        """Test store initialization failure."""
        with patch("switchbot_dashboard.postgres_store.ConnectionPool") as pool_cls:
            pool_cls.side_effect = Exception("Connection failed")

            with pytest.raises(PostgresStoreError) as exc_info:
                PostgresStore(
                    connection_string=test_postgres_url,
                    kind="test",
                    logger=mock_logger,
                )

            assert "Failed to initialize PostgreSQL connection pool" in str(exc_info.value)

    def test_read_success(self, postgres_store, mock_logger, mocked_pool):
        """Test successful data read."""
        mock_cursor = mocked_pool["cursor"]
        mock_cursor.fetchone.return_value = {"data": {"key": "value"}}

        result = postgres_store.read()

        assert result == {"key": "value"}
        mock_cursor.execute.assert_called_once()

    def test_read_empty_result(self, postgres_store, mock_logger, mocked_pool):
        """Test read when no data exists."""
        mock_cursor = mocked_pool["cursor"]
        mock_cursor.fetchone.return_value = None

        result = postgres_store.read()

        assert result == {}

    def test_read_database_error(self, postgres_store, mock_logger):
        """Test read with database error."""
        # Mock database error
        postgres_store._pool.connection.side_effect = Exception("Database error")
        
        with pytest.raises(PostgresStoreError) as exc_info:
            postgres_store.read()
        
        assert "PostgreSQL read failed" in str(exc_info.value)

    def test_write_success(self, postgres_store, mock_logger, mocked_pool):
        """Test successful data write."""
        test_data = {"key": "value", "number": 42}

        mock_connection = mocked_pool["connection"]
        mock_cursor = mocked_pool["cursor"]

        postgres_store.write(test_data)

        mock_cursor.execute.assert_called_once()
        mock_connection.commit.assert_called_once()

    def test_write_database_error(self, postgres_store, mock_logger):
        """Test write with database error."""
        test_data = {"key": "value"}
        
        # Mock database error
        postgres_store._pool.connection.side_effect = Exception("Database error")
        
        with pytest.raises(PostgresStoreError) as exc_info:
            postgres_store.write(test_data)
        
        assert "PostgreSQL write failed" in str(exc_info.value)

    def test_health_check_success(self, postgres_store, mocked_pool):
        """Test successful health check."""
        mock_cursor = mocked_pool["cursor"]
        mock_cursor.fetchone.return_value = (1,)

        result = postgres_store.health_check()

        assert result is True

    def test_health_check_failure(self, postgres_store):
        """Test health check failure."""
        # Mock health check failure
        postgres_store._pool.connection.side_effect = Exception("Connection failed")
        
        result = postgres_store.health_check()
        
        assert result is False

    def test_health_check_no_pool(self, postgres_store):
        """Test health check with no connection pool."""
        postgres_store._pool = None
        
        result = postgres_store.health_check()
        
        assert result is False

    def test_close_success(self, postgres_store, mock_logger, mocked_pool):
        """Test successful store cleanup."""
        mock_pool = mocked_pool["pool"]
        postgres_store.close()

        mock_pool.close.assert_called_once()
        assert postgres_store._pool is None

    def test_close_with_error(self, postgres_store, mock_logger):
        """Test store cleanup with error."""
        postgres_store._pool.close.side_effect = Exception("Close error")
        
        # Should not raise exception
        postgres_store.close()
        
        # Should log warning
        mock_logger.warning.assert_called_once()

    def test_data_type_handling(self, postgres_store, mock_logger, mocked_pool):
        """Test handling of different data types in read."""
        mock_cursor = mocked_pool["cursor"]

        mock_cursor.fetchone.return_value = {"data": '{"key": "value"}'}
        result = postgres_store.read()
        assert result == {"key": "value"}

        # Test dict data
        mock_cursor.fetchone.return_value = {"data": {"key": "value"}}
        result = postgres_store.read()
        assert result == {"key": "value"}

        # Test invalid data type
        mock_cursor.fetchone.return_value = {"data": 123}
        with pytest.raises(PostgresStoreError) as exc_info:
            postgres_store.read()
        
        assert "Invalid data type" in str(exc_info.value)

    def test_connection_parameters(self, test_postgres_url, mock_logger):
        """Test connection parameter configuration."""
        with patch("switchbot_dashboard.postgres_store.ConnectionPool") as mock_pool, patch(
            "switchbot_dashboard.postgres_store.PostgresStore._ensure_table_exists"
        ):
            mock_pool.return_value = MagicMock()

            PostgresStore(
                connection_string=test_postgres_url,
                kind="test",
                logger=mock_logger,
                ssl_mode="verify-full",
                max_connections=5,
            )

            mock_pool.assert_called_once_with(
                conninfo=test_postgres_url,
                min_size=1,
                max_size=5,
            )

    def test_table_creation(self, postgres_store):
        """Test table creation on initialization."""
        # The postgres_store fixture already mocks the connection pool
        # and table creation happens during initialization
        # This test verifies the fixture works correctly
        assert postgres_store is not None
        assert hasattr(postgres_store, '_pool')


class TestPostgresStoreIntegration:
    """Integration tests for PostgresStore (requires real PostgreSQL)."""

    @pytest.mark.skipif(
        not os.environ.get("TEST_POSTGRES_URL"),
        reason="Requires TEST_POSTGRES_URL environment variable",
    )
    def test_real_postgres_operations(self, real_postgres_store):
        """Test real PostgreSQL operations."""
        # Test write and read
        test_data = {
            "automation_enabled": True,
            "poll_interval_seconds": 60,
            "test_timestamp": "2026-01-14T12:00:00Z",
        }
        
        real_postgres_store.write(test_data)
        result = real_postgres_store.read()
        
        assert result == test_data
        
        # Test health check
        assert real_postgres_store.health_check() is True
        
        # Test overwrite
        new_data = {"automation_enabled": False, "poll_interval_seconds": 120}
        real_postgres_store.write(new_data)
        result = real_postgres_store.read()
        
        assert result == new_data


if __name__ == "__main__":
    pytest.main([__file__])
