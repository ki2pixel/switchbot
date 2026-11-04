from __future__ import annotations

import json
import sys
import types

from unittest.mock import MagicMock

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


def test_create_app_csp_nonce_replaces_unsafe_inline(monkeypatch, tmp_path):
    """script-src must use a per-request nonce instead of 'unsafe-inline'."""
    settings_path = tmp_path / "settings.json"
    state_path = tmp_path / "state.json"
    settings_path.write_text("{}", encoding="utf-8")
    state_path.write_text("{}", encoding="utf-8")

    monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
    monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
    monkeypatch.setenv("STORE_BACKEND", "filesystem")
    monkeypatch.setenv("FLASK_DEBUG", "1")
    monkeypatch.setenv("SCHEDULER_ENABLED", "false")
    monkeypatch.delenv("WERKZEUG_RUN_MAIN", raising=False)
    monkeypatch.delenv("DASHBOARD_PASSWORD", raising=False)

    monkeypatch.setattr(AutomationService, "poll_meter", lambda self: None)

    app = create_app()

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200

    csp = response.headers["Content-Security-Policy"]
    script_src = csp.split("script-src", 1)[1].split(";", 1)[0]
    assert "'unsafe-inline'" not in script_src
    assert "'nonce-" in script_src

    nonce = script_src.split("'nonce-", 1)[1].split("'", 1)[0]
    assert nonce

    # Every inline <script> of the rendered page must carry that nonce.
    html = response.get_data(as_text=True)
    assert f'nonce="{nonce}"' in html
    assert 'nonce=""' not in html


def test_create_app_csp_nonce_is_per_request(monkeypatch, tmp_path):
    """Two consecutive responses must not reuse the same nonce."""
    settings_path = tmp_path / "settings.json"
    state_path = tmp_path / "state.json"
    settings_path.write_text("{}", encoding="utf-8")
    state_path.write_text("{}", encoding="utf-8")

    monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
    monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
    monkeypatch.setenv("STORE_BACKEND", "filesystem")
    monkeypatch.setenv("FLASK_DEBUG", "1")
    monkeypatch.setenv("SCHEDULER_ENABLED", "false")
    monkeypatch.delenv("WERKZEUG_RUN_MAIN", raising=False)
    monkeypatch.delenv("DASHBOARD_PASSWORD", raising=False)

    monkeypatch.setattr(AutomationService, "poll_meter", lambda self: None)

    app = create_app()

    with app.test_client() as client:
        first = client.get("/")
        second = client.get("/")

    def _nonce(response):
        csp = response.headers["Content-Security-Policy"]
        script_src = csp.split("script-src", 1)[1].split(";", 1)[0]
        return script_src.split("'nonce-", 1)[1].split("'", 1)[0]

    assert _nonce(first) != _nonce(second)


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


# ---------------------------------------------------------------------------
# WSGI runtime must ignore FLASK_DEBUG
#
# | Case ID | Input / Precondition            | Perspective      | Expected Result                        |
# |---------|---------------------------------|------------------|----------------------------------------|
# | WSGI-01 | FLASK_DEBUG=1 + gunicorn loaded | Normal (prod)    | app.debug False, Secure cookie + HSTS  |
# | WSGI-02 | FLASK_DEBUG=1, no WSGI marker   | Equivalence (dev)| app.debug True, cookie not Secure      |
# | WSGI-03 | FLASK_DEBUG=1 + RENDER=true     | Boundary (alt)   | app.debug False                        |
# | WSGI-04 | FLASK_DEBUG=1 + SERVER_SOFTWARE | Boundary (alt)   | app.debug False                        |
# ---------------------------------------------------------------------------


def _empty_pool() -> MagicMock:
    """A pool double whose stores read as an empty JSON document."""
    cursor = MagicMock()
    cursor.fetchone.return_value = {"data": {}}
    connection = MagicMock()
    connection.cursor.return_value.__enter__.return_value = cursor
    pool = MagicMock()
    pool.connection.return_value.__enter__.return_value = connection
    return pool


def _prepare_app_env(monkeypatch, tmp_path, *, backend: str = "filesystem") -> None:
    settings_path = tmp_path / "settings.json"
    state_path = tmp_path / "state.json"
    settings_path.write_text("{}", encoding="utf-8")
    state_path.write_text("{}", encoding="utf-8")

    monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
    monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
    monkeypatch.setenv("STORE_BACKEND", backend)
    if backend == "postgres":
        # conftest mocks ConnectionPool/_ensure_table_exists for this module;
        # the shared pool created inside create_app needs the same treatment.
        monkeypatch.setenv("POSTGRES_URL", "postgresql://test:test@localhost/test")
        monkeypatch.setenv("POSTGRES_SSL_MODE", "disable")
        monkeypatch.setattr(
            "switchbot_dashboard.ConnectionPool", lambda **kwargs: _empty_pool()
        )
    monkeypatch.setenv("SCHEDULER_ENABLED", "false")
    monkeypatch.setenv("FLASK_SECRET_KEY", "test-secret-4f8c1e2a9b7d")
    monkeypatch.setenv("DASHBOARD_PASSWORD", "prod-password")
    monkeypatch.delenv("FLASK_ENV", raising=False)
    monkeypatch.delenv("RENDER", raising=False)
    monkeypatch.delenv("SERVER_SOFTWARE", raising=False)
    monkeypatch.delenv("STORE_RUNTIME_FALLBACK", raising=False)
    monkeypatch.delitem(sys.modules, "gunicorn", raising=False)
    monkeypatch.delitem(sys.modules, "uwsgi", raising=False)
    monkeypatch.setattr(AutomationService, "poll_meter", lambda self: None)


def test_gunicorn_runtime_forces_debug_off(monkeypatch, tmp_path):
    _prepare_app_env(monkeypatch, tmp_path, backend="postgres")
    monkeypatch.setenv("FLASK_DEBUG", "1")
    monkeypatch.setitem(sys.modules, "gunicorn", types.ModuleType("gunicorn"))

    # Given/When: a stray FLASK_DEBUG=1 is set while gunicorn serves the app
    app = create_app()

    # Then: debug is disabled and production cookie/HSTS guards are active
    assert app.debug is False
    assert app.config["SESSION_COOKIE_SECURE"] is True
    assert app.extensions["settings_store"].fallback_enabled is False

    app.config["WTF_CSRF_ENABLED"] = False
    with app.test_client() as client:
        login_page = client.get("/login")
        login = client.post("/login", data={"password": "prod-password"})

    assert "Strict-Transport-Security" in login_page.headers
    assert "Secure" in login.headers.get("Set-Cookie", "")
    assert "HttpOnly" in login.headers.get("Set-Cookie", "")


def test_dev_runtime_keeps_debug_enabled(monkeypatch, tmp_path):
    _prepare_app_env(monkeypatch, tmp_path)
    monkeypatch.setenv("FLASK_DEBUG", "1")

    # Given/When: the same flag runs without any WSGI marker (local dev)
    app = create_app()

    # Then: debug stays on and the Secure cookie is not forced over plain HTTP
    assert app.debug is True
    assert app.config["SESSION_COOKIE_SECURE"] is False


def test_render_runtime_forces_debug_off(monkeypatch, tmp_path):
    _prepare_app_env(monkeypatch, tmp_path, backend="postgres")
    monkeypatch.setenv("FLASK_DEBUG", "1")
    monkeypatch.setenv("RENDER", "true")

    # Given/When: Render marks the runtime even if gunicorn is not importable
    app = create_app()

    # Then: production guards apply
    assert app.debug is False
    assert app.config["SESSION_COOKIE_SECURE"] is True


def test_server_software_marker_forces_debug_off(monkeypatch, tmp_path):
    _prepare_app_env(monkeypatch, tmp_path, backend="postgres")
    monkeypatch.setenv("FLASK_DEBUG", "1")
    monkeypatch.setenv("SERVER_SOFTWARE", "gunicorn/22.0.0")

    # Given/When: a WSGI server exports SERVER_SOFTWARE
    app = create_app()

    # Then: production guards apply
    assert app.debug is False
    assert app.config["SESSION_COOKIE_SECURE"] is True

