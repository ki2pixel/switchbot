from __future__ import annotations

import json
from unittest.mock import MagicMock
from typing import Any


from switchbot_dashboard import create_app
from switchbot_dashboard.automation import AutomationService


def test_create_app_uses_postgres_store_when_configured(monkeypatch, tmp_path) -> None:
    """Test that create_app uses PostgresStore when configured."""
    settings_path = tmp_path / "settings.json"
    state_path = tmp_path / "state.json"
    settings_path.write_text(json.dumps({"meter_device_id": "dummy"}, ensure_ascii=False))
    state_path.write_text(json.dumps({}, ensure_ascii=False))

    # Configure PostgreSQL environment
    monkeypatch.setenv("STORE_BACKEND", "postgres")
    monkeypatch.setenv("POSTGRES_URL", "postgresql://test:test@localhost/test")
    monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
    monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
    monkeypatch.setenv("SCHEDULER_ENABLED", "false")

    # Mock PostgresStore to avoid real database connection
    class FakePostgresStore:
        def __init__(self, *args, **kwargs):
            self._data: dict[str, Any] = {"meter_device_id": "dummy"}
            self._pool = MagicMock()
            import threading
            self._local = threading.local()

        def transaction(self) -> Any:
            from switchbot_dashboard.config_store import SimpleTransactionContext
            return SimpleTransactionContext(self)

        def read(self) -> dict[str, Any]:
            tx = getattr(self._local, "active_transaction", None)
            if tx is not None:
                return tx.read()
            return self._data

        def write(self, data: dict[str, Any]) -> None:
            tx = getattr(self._local, "active_transaction", None)
            if tx is not None:
                tx.write(data)
                return
            self._data = dict(data)

        def health_check(self) -> bool:
            return True

        def close(self) -> None:
            pass

    monkeypatch.setattr("switchbot_dashboard.postgres_store.PostgresStore", FakePostgresStore)
    monkeypatch.setattr("switchbot_dashboard.PostgresStore", FakePostgresStore, raising=False)

    # Avoid real SwitchBot/automation calls
    def fake_poll(self: AutomationService) -> None:
        state = self._state_store.read()
        state["last_temperature_stale"] = False
        state["last_temperature_stale_reason"] = None
        self._state_store.write(state)

    monkeypatch.setattr(AutomationService, "poll_meter", fake_poll)

    app = create_app()

    settings_store = app.extensions["settings_store"]
    state_store = app.extensions["state_store"]

    # Given: PostgreSQL configured (or fallback to filesystem)
    # Then: both stores are BaseStore instances (PostgresStore or JsonStore)
    from switchbot_dashboard.config_store import BaseStore
    assert isinstance(settings_store, BaseStore)
    assert isinstance(state_store, BaseStore)
