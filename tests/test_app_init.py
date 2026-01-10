from __future__ import annotations

import json

from switchbot_dashboard import create_app
from switchbot_dashboard.automation import AutomationService


def test_create_app_marks_temperature_stale_then_refresh(monkeypatch, tmp_path):
    settings_path = tmp_path / "settings.json"
    state_path = tmp_path / "state.json"
    settings_path.write_text(json.dumps({"meter_device_id": "dummy"}, ensure_ascii=False))
    state_path.write_text(json.dumps({}, ensure_ascii=False))

    monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
    monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
    monkeypatch.setenv("FLASK_DEBUG", "1")
    monkeypatch.delenv("WERKZEUG_RUN_MAIN", raising=False)

    calls: dict[str, object] = {}

    def fake_poll(self) -> None:
        state_before = self._state_store.read()
        calls["called"] = True
        calls["stale_before_poll"] = state_before.get("last_temperature_stale")
        state_before["last_temperature_stale"] = False
        state_before["last_temperature_stale_reason"] = None
        self._state_store.write(state_before)
        return None

    monkeypatch.setattr(AutomationService, "poll_meter", fake_poll)

    app = create_app()

    state_store = app.extensions["state_store"]
    state = state_store.read()

    assert calls.get("called") is True
    assert calls.get("stale_before_poll") is True
    assert state.get("last_temperature_stale") is False
    assert state.get("last_temperature_stale_reason") is None
