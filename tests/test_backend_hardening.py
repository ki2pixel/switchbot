from __future__ import annotations

import datetime as dt
import decimal
import sys
from unittest.mock import MagicMock, patch

import pytest
from flask import Flask

from switchbot_dashboard import create_app
from switchbot_dashboard.__init__ import _build_store
from switchbot_dashboard.config_store import JsonStore
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
        
        # Triggering a force flush should succeed and clear the buffer
        service.flush_pending_records(force=True)
        assert len(service._pending_records) == 0


class TestStoreFailoverAndBuild:
    def test_build_store_fallback_on_unhealthy_postgres(self, monkeypatch, tmp_path) -> None:
        app = Flask("test_app")
        app.config["TESTING"] = True
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
        app.config["TESTING"] = True
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


class TestDashboardAuthentication:
    def test_routes_require_authentication_when_password_configured(self, monkeypatch, tmp_path) -> None:
        settings_path = tmp_path / "settings.json"
        state_path = tmp_path / "state.json"
        settings_path.write_text("{}", encoding="utf-8")
        state_path.write_text("{}", encoding="utf-8")

        monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
        monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
        monkeypatch.setenv("STORE_BACKEND", "filesystem")
        monkeypatch.setenv("DASHBOARD_PASSWORD", "securepassword")
        monkeypatch.setenv("SCHEDULER_ENABLED", "false")
        
        app = create_app()
        app.config["WTF_CSRF_ENABLED"] = False
        
        with app.test_client() as client:
            # Protected page redirects to login
            response = client.get("/")
            assert response.status_code == 302
            assert response.headers["Location"].endswith("/login")

            # Public page healthz does not redirect
            response = client.get("/healthz")
            assert response.status_code == 200

            # Get login page works
            response = client.get("/login")
            assert response.status_code == 200
            assert b"Veuillez saisir votre mot de passe" in response.data

            # Login with wrong password fails
            response = client.post("/login", data={"password": "wrongpassword"})
            assert response.status_code == 200
            assert b"Mot de passe incorrect." in response.data

            # Login with correct password succeeds and redirects to index
            response = client.post("/login", data={"password": "securepassword"})
            assert response.status_code == 302
            assert response.headers["Location"].endswith("/")

            # Accessing protected page now succeeds
            response = client.get("/")
            assert response.status_code == 200

            # Logout redirects to login
            response = client.get("/logout")
            assert response.status_code == 302
            assert response.headers["Location"].endswith("/login")

            # Accessing protected page again redirects to login
            response = client.get("/")
            assert response.status_code == 302

    def test_debug_state_authorization_bearer_token(self, monkeypatch, tmp_path) -> None:
        settings_path = tmp_path / "settings.json"
        state_path = tmp_path / "state.json"
        settings_path.write_text("{}", encoding="utf-8")
        state_path.write_text("{}", encoding="utf-8")

        monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
        monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
        monkeypatch.setenv("STORE_BACKEND", "filesystem")
        monkeypatch.setenv("STATE_DEBUG_TOKEN", "mydebugtoken")
        
        app = create_app()
        with app.test_client() as client:
            # No token in headers -> 404
            response = client.get("/debug/state")
            assert response.status_code == 404

            # Token in URL query -> 404 (removed from query args!)
            response = client.get("/debug/state?token=mydebugtoken")
            assert response.status_code == 404

            # Token in Authorization header as Bearer -> 200
            response = client.get("/debug/state", headers={"Authorization": "Bearer mydebugtoken"})
            assert response.status_code == 200

            # Wrong token in Authorization header -> 404
            response = client.get("/debug/state", headers={"Authorization": "Bearer wrongtoken"})
            assert response.status_code == 404


class TestPostgresSslAndFailover:
    def test_postgres_pool_receives_sslmode(self, monkeypatch, tmp_path) -> None:
        from unittest.mock import MagicMock, patch
        
        monkeypatch.setenv("STORE_BACKEND", "postgres")
        monkeypatch.setenv("POSTGRES_URL", "postgresql://localhost/fake")
        monkeypatch.setenv("POSTGRES_SSL_MODE", "verify-full")
        
        with patch("switchbot_dashboard.postgres_store.ConnectionPool") as mock_pool, \
             patch("switchbot_dashboard.postgres_store.PostgresStore._ensure_table_exists"):
            
            PostgresStore(
                connection_string="postgresql://localhost/fake",
                kind="settings",
                logger=MagicMock(),
                ssl_mode="verify-full"
            )
            
            called_kwargs = mock_pool.call_args[1]
            assert "kwargs" in called_kwargs
            assert called_kwargs["kwargs"]["sslmode"] == "verify-full"

    def test_build_store_production_fails_on_unhealthy_db(self, monkeypatch, tmp_path) -> None:
        app = Flask("test_app")
        app.config["ENV"] = "production"
        settings_path = tmp_path / "settings.json"
        
        monkeypatch.setenv("FLASK_ENV", "production")
        monkeypatch.setenv("STORE_BACKEND", "postgres")
        monkeypatch.setenv("POSTGRES_URL", "postgresql://localhost/fake")
        
        with patch("switchbot_dashboard.__init__.PostgresStore") as MockPostgresStore:
            postgres_mock = MagicMock()
            postgres_mock.health_check.return_value = False
            MockPostgresStore.return_value = postgres_mock
            
            with pytest.raises(PostgresStoreError, match="PostgreSQL health check failed"):
                _build_store(
                    app,
                    kind="settings",
                    default_path=str(settings_path),
                    path_env="SWITCHBOT_SETTINGS_PATH",
                )


class TestAutomationConcurrencyLock:
    def test_run_once_acquires_and_releases_lock(self) -> None:
        from switchbot_dashboard.automation import AutomationService
        from unittest.mock import MagicMock
        
        settings_store = MagicMock()
        state_store = MagicMock()
        client = MagicMock()
        
        state_store.read.return_value = {
            "automation_in_progress": False
        }
        
        service = AutomationService(
            settings_store=settings_store,
            state_store=state_store,
            switchbot_client=client,
            logger=MagicMock()
        )
        
        def mock_impl():
            assert state_store.write.call_count >= 1
            last_written = state_store.write.call_args[0][0]
            assert last_written["automation_in_progress"] is True
            assert last_written["automation_lock_owner"] == "scheduler"
            
        service._run_once_impl = mock_impl
        
        service.run_once()
        
        assert state_store.write.call_count >= 2
        final_written = state_store.write.call_args_list[-1][0][0]
        assert final_written["automation_in_progress"] is False
        assert final_written["automation_lock_owner"] is None

    def test_run_once_skips_when_lock_held(self) -> None:
        from switchbot_dashboard.automation import AutomationService
        from unittest.mock import MagicMock
        
        settings_store = MagicMock()
        state_store = MagicMock()
        client = MagicMock()
        
        state_store.read.return_value = {
            "automation_in_progress": True,
            "automation_locked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "automation_lock_owner": "http:manual"
        }
        
        service = AutomationService(
            settings_store=settings_store,
            state_store=state_store,
            switchbot_client=client,
            logger=MagicMock()
        )
        
        called_impl = False
        def mock_impl():
            nonlocal called_impl
            called_impl = True
            
        service._run_once_impl = mock_impl
        
        service.run_once()
        
        assert not called_impl
        assert not state_store.write.called


class TestQuotaActualRefresh:
    def test_quota_refresh_route_makes_api_call(self, monkeypatch, tmp_path) -> None:
        settings_path = tmp_path / "settings.json"
        state_path = tmp_path / "state.json"
        settings_path.write_text("{}", encoding="utf-8")
        state_path.write_text("{}", encoding="utf-8")

        monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
        monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
        monkeypatch.setenv("STORE_BACKEND", "filesystem")
        monkeypatch.setenv("DASHBOARD_PASSWORD", "securepassword")
        
        app = create_app()
        app.config["WTF_CSRF_ENABLED"] = False
        
        mock_client = MagicMock()
        app.extensions["switchbot_client"] = mock_client
        
        with app.test_client() as client:
            # Login to establish an authenticated session
            login_resp = client.post("/login", data={"password": "securepassword"})
            assert login_resp.status_code == 302
            
            response = client.post("/quota/refresh")
            
            assert response.status_code == 302
            assert response.headers["Location"].endswith("/quota")
            mock_client.get_devices.assert_called_once()
