"""Tests pour la route /actions/run_once avec GET et POST."""
from __future__ import annotations

import copy
from flask import Flask

from switchbot_dashboard.routes import dashboard_bp


class MemoryStore:
    def __init__(self, initial: dict[str, object]) -> None:
        self._data = copy.deepcopy(initial)

    def read(self) -> dict[str, object]:
        return copy.deepcopy(self._data)

    def write(self, new_data: dict[str, object]) -> None:
        self._data = copy.deepcopy(new_data)


class DummyScheduler:
    def __init__(self) -> None:
        self.running = True

    def is_running(self) -> bool:
        return self.running


class DummyAutomationService:
    def __init__(self) -> None:
        self.run_once_called = False

    def run_once(self) -> None:
        self.run_once_called = True


def _build_test_app() -> tuple[Flask, DummyAutomationService]:
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.secret_key = "test"

    settings_store = MemoryStore({"automation_enabled": True})
    state_store = MemoryStore({})
    scheduler = DummyScheduler()
    automation_service = DummyAutomationService()

    app.extensions["settings_store"] = settings_store
    app.extensions["state_store"] = state_store
    app.extensions["scheduler_service"] = scheduler
    app.extensions["automation_service"] = automation_service

    app.register_blueprint(dashboard_bp)

    return app, automation_service


def test_run_once_accepts_post_method() -> None:
    """Vérifie que POST /actions/run_once fonctionne (comportement existant)."""
    app, automation_service = _build_test_app()

    with app.test_client() as client:
        response = client.post("/actions/run_once", follow_redirects=False)

    assert response.status_code == 302  # Redirect
    assert automation_service.run_once_called


def test_run_once_accepts_get_method() -> None:
    """Vérifie que GET /actions/run_once fonctionne (pour cron jobs)."""
    app, automation_service = _build_test_app()

    with app.test_client() as client:
        response = client.get("/actions/run_once", follow_redirects=False)

    assert response.status_code == 302  # Redirect
    assert automation_service.run_once_called


def test_run_once_get_no_405_error() -> None:
    """Vérifie que GET ne retourne pas 405 (erreur méthode non autorisée)."""
    app, automation_service = _build_test_app()

    with app.test_client() as client:
        response = client.get("/actions/run_once", follow_redirects=False)

    # Vérifie que ce n'est PAS une erreur 405
    assert response.status_code != 405
    assert response.status_code == 302  # Redirect vers index
    assert automation_service.run_once_called
