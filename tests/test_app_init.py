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
    monkeypatch.setenv("STORE_BACKEND", "filesystem")
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


def test_create_app_requires_secret_key_in_production(monkeypatch, tmp_path):
    import pytest
    import sys
    
    settings_path = tmp_path / "settings.json"
    state_path = tmp_path / "state.json"
    settings_path.write_text("{}", encoding="utf-8")
    state_path.write_text("{}", encoding="utf-8")

    monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
    monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
    monkeypatch.setenv("STORE_BACKEND", "filesystem")
    
    # Simulate production (no FLASK_DEBUG, no WERKZEUG_RUN_MAIN, and no FLASK_SECRET_KEY)
    monkeypatch.delenv("FLASK_DEBUG", raising=False)
    monkeypatch.delenv("FLASK_SECRET_KEY", raising=False)
    monkeypatch.delenv("WERKZEUG_RUN_MAIN", raising=False)
    
    # We monkeypatch the check so it thinks we are not in pytest
    # In __init__.py:
    # "is_pytest = "pytest" in sys.modules or any("pytest" in arg for arg in sys.argv)"
    # We can temporarily patch the "sys" module or argv/modules.
    # An easy way is to patch sys.argv to not contain 'pytest' and patch the 'pytest' key out of sys.modules temporarily.
    orig_argv = sys.argv
    sys.argv = [arg for arg in sys.argv if "pytest" not in arg]
    
    # We need to simulate the environment where "pytest" in sys.modules returns False
    # Since we can't easily remove pytest from sys.modules without breaking the current test runner,
    # we can monkeypatch os.environ to not have a secret key and override the is_pytest check using patch or monkeypatch.
    # Wait, instead of hacking sys.modules, we can patch the specific logic or let the check evaluate.
    # Wait, in switchbot_dashboard/__init__.py, let's see how is_pytest is checked.
    # Let's mock the "sys.modules" check or the sys check!
    # Let's use patch to mock sys.modules:
    orig_modules = sys.modules
    # We don't want to break the whole system, so we can mock the 'sys.modules' container or just subclass dict:
    class MockedModules(dict):
        def __contains__(self, item):
            if item == "pytest":
                return False
            return super().__contains__(item)
            
    try:
        sys.modules = MockedModules(orig_modules)
        with pytest.raises(RuntimeError) as exc_info:
            create_app()
        assert "Security Violation: FLASK_SECRET_KEY must be set in production" in str(exc_info.value)
    finally:
        sys.modules = orig_modules
        sys.argv = orig_argv

