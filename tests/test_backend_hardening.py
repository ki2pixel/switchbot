from __future__ import annotations

import datetime as dt
import decimal
import ipaddress
import socket
import sys
from unittest.mock import MagicMock, patch

import pytest
from flask import Flask

from switchbot_dashboard import create_app
from switchbot_dashboard.__init__ import _build_store
from switchbot_dashboard.config_store import JsonStore, StoreError
from switchbot_dashboard.postgres_store import PostgresStore, PostgresStoreError
from switchbot_dashboard.quota import ApiQuotaTracker
from switchbot_dashboard.history_service import HistoryService, HistoryServiceError


class TestFlaskSecretKeyHardening:
    def test_boot_aborts_with_insecure_key(self, monkeypatch, tmp_path) -> None:
        settings_path = tmp_path / "settings.json"
        state_path = tmp_path / "state.json"
        settings_path.write_text("{}", encoding="utf-8")
        state_path.write_text("{}", encoding="utf-8")

        monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
        monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
        monkeypatch.setenv("STORE_BACKEND", "filesystem")
        
        # Insecure key
        monkeypatch.setenv("FLASK_SECRET_KEY", "change-me")
        monkeypatch.delenv("FLASK_DEBUG", raising=False)
        monkeypatch.delenv("WERKZEUG_RUN_MAIN", raising=False)
        
        orig_argv = sys.argv
        sys.argv = [arg for arg in sys.argv if "pytest" not in arg]
        
        orig_modules = sys.modules
        class MockedModules(dict):
            def __contains__(self, item):
                if item == "pytest":
                    return False
                return super().__contains__(item)
                
        try:
            sys.modules = MockedModules(orig_modules)
            with pytest.raises(RuntimeError, match="FLASK_SECRET_KEY must be set in production"):
                create_app()
        finally:
            sys.modules = orig_modules
            sys.argv = orig_argv


class TestApiQuotaTracker:
    def test_quota_tracker_normal_behavior(self) -> None:
        store = MagicMock()
        store.read.return_value = {
            "api_quota_day": dt.datetime.now(dt.timezone.utc).date().isoformat(),
            "api_requests_total": 5,
            "api_requests_limit": 1000,
            "api_requests_remaining": 995
        }
        
        tracker = ApiQuotaTracker(state_store=store, default_daily_limit=1000)
        tracker.record_call(increment=5)
        
        store.write.assert_called_once()
        written_data = store.write.call_args[0][0]
        assert written_data["api_requests_total"] == 10
        assert written_data["api_requests_remaining"] == 990

    def test_quota_tracker_daily_reset(self) -> None:
        store = MagicMock()
        # Yesterday's data
        store.read.return_value = {
            "api_quota_day": "2000-01-01",
            "api_requests_total": 50,
            "api_requests_limit": 1000,
            "api_requests_remaining": 950
        }
        
        tracker = ApiQuotaTracker(state_store=store, default_daily_limit=1000)
        tracker.record_call(increment=1)
        
        # Should reset stats and write updated state
        store.write.assert_called_once()
        written_data = store.write.call_args[0][0]
        assert written_data["api_quota_day"] == dt.datetime.now(dt.timezone.utc).date().isoformat()
        assert written_data["api_requests_total"] == 1
        assert written_data["api_requests_remaining"] == 999


class TestHistoryServiceBufferResiliency:
    @patch("switchbot_dashboard.history_service.HistoryService._ensure_table_exists")
    def test_buffer_retention_on_postgres_ko(self, mock_ensure) -> None:
        pool_mock = MagicMock()
        # Simulate Postgres exception on pool connection
        pool_mock.connection.side_effect = Exception("PostgreSQL server went away")
        
        logger_mock = MagicMock()
        service = HistoryService(
            connection_pool=pool_mock,
            logger=logger_mock,
            batch_size=2,
            flush_interval_seconds=60
        )
        
        # Initial pending records should be empty
        assert len(service._pending_records) == 0
        
        state_data = {
            "last_temperature": 24.5,
            "last_humidity": 50.0,
            "assumed_aircon_power": "on",
            "last_action": "automation_winter_on",
            "api_requests_today": 12,
            "error_count": 0,
            "last_temperature_stale": False,
            "last_read_at": "2026-07-04T12:00:00Z"
        }
        
        # When we record state (not triggering batch size 2 yet)
        service.record_state(state_data)
        assert len(service._pending_records) == 1
        
        # When we record another state (triggers flush_pending_records_locked)
        # It should catch HistoryServiceError and NOT throw, but keep records in buffer
        with pytest.raises(HistoryServiceError):
            service.record_state(state_data, force_flush=True)
        
        # Verification: records were NOT cleared because the flush failed!
        # Both records are still pending in the queue, waiting for retry.
        assert len(service._pending_records) == 2
        
        # If postgres recovers
        pool_mock.connection.side_effect = None
        conn_context = pool_mock.connection.return_value
        conn = conn_context.__enter__.return_value
        cursor = conn.cursor.return_value.__enter__.return_value
        
        # Triggering a force flush should succeed and clear the buffer
        service.flush_pending_records(force=True)
        assert len(service._pending_records) == 0


class TestStoreFailoverAndBuild:
    def test_build_store_fallback_on_unhealthy_postgres(self, monkeypatch, tmp_path) -> None:
        app = Flask("test_app")
        settings_path = tmp_path / "settings.json"
        
        monkeypatch.setenv("STORE_BACKEND", "postgres")
        monkeypatch.setenv("POSTGRES_URL", "postgresql://localhost/fake")
        
        # Mock PostgresStore health_check to return False (unhealthy)
        with patch("switchbot_dashboard.__init__.PostgresStore") as MockPostgresStore:
            postgres_mock = MagicMock()
            postgres_mock.health_check.return_value = False
            MockPostgresStore.return_value = postgres_mock
            
            store = _build_store(
                app,
                kind="settings",
                default_path=str(settings_path),
                path_env="SWITCHBOT_SETTINGS_PATH",
            )
            
            # Should have fallen back to JsonStore because Postgres was unhealthy
            assert isinstance(store, JsonStore)
            postgres_mock.close.assert_called_once()

    def test_build_store_fallback_on_postgres_exception(self, monkeypatch, tmp_path) -> None:
        app = Flask("test_app")
        settings_path = tmp_path / "settings.json"
        
        monkeypatch.setenv("STORE_BACKEND", "postgres")
        monkeypatch.setenv("POSTGRES_URL", "postgresql://localhost/fake")
        
        # Mock PostgresStore constructor to raise PostgresStoreError
        with patch("switchbot_dashboard.__init__.PostgresStore", side_effect=PostgresStoreError("Connection failed")):
            store = _build_store(
                app,
                kind="settings",
                default_path=str(settings_path),
                path_env="SWITCHBOT_SETTINGS_PATH",
            )
            
            # Should fall back to JsonStore
            assert isinstance(store, JsonStore)


class TestHistoryServiceAggregates:
    @patch("switchbot_dashboard.history_service.HistoryService._ensure_table_exists")
    def test_get_aggregates_and_latest_records(self, mock_ensure) -> None:
        pool_mock = MagicMock()
        conn_context = pool_mock.connection.return_value
        conn = conn_context.__enter__.return_value
        cursor = conn.cursor.return_value.__enter__.return_value
        
        # Mock aggregates query results
        cursor.fetchone.return_value = {
            "total_records": 100,
            "avg_temperature": decimal.Decimal("23.5"),
            "min_temperature": decimal.Decimal("21.0"),
            "max_temperature": decimal.Decimal("25.5"),
            "avg_humidity": decimal.Decimal("45.2"),
            "min_humidity": decimal.Decimal("40.0"),
            "max_humidity": decimal.Decimal("50.0"),
            "common_aircon_state": "on",
            "distinct_actions": 3,
            "total_errors": 0,
            "max_api_requests": 150
        }
        
        service = HistoryService(connection_pool=pool_mock, logger=MagicMock())
        aggregates = service.get_aggregates(period_hours=6)
        
        assert aggregates["total_records"] == 100
        assert aggregates["avg_temperature"] == 23.5
        assert aggregates["common_aircon_state"] == "on"

        # Mock latest records results
        cursor.fetchall.return_value = [
            {
                "id": 1,
                "timestamp": dt.datetime(2026, 7, 4, 12, 0, 0, tzinfo=dt.timezone.utc),
                "temperature": decimal.Decimal("24.5"),
                "humidity": decimal.Decimal("50.0"),
                "assumed_aircon_power": "on",
                "last_action": "automation_winter_on",
                "metadata": {"last_tick": "2026-07-04T12:00:00Z"}
            }
        ]
        
        latest = service.get_latest_records(limit=5)
        assert len(latest) == 1
        assert latest[0]["temperature"] == 24.5
        assert latest[0]["timestamp"] == "2026-07-04T12:00:00+00:00"
