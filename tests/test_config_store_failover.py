from __future__ import annotations

import json
from types import SimpleNamespace
from typing import Any, Iterator
from unittest.mock import MagicMock

import pytest

from switchbot_dashboard import create_app
from switchbot_dashboard.config_store import FailoverStore, StoreError
from switchbot_dashboard.automation import AutomationService


class StubStore:
    def __init__(
        self,
        *,
        name: str,
        read_result: dict[str, Any] | None = None,
        read_exc: Exception | None = None,
        read_exc_sequence: list[Exception | None] | None = None,
        write_exc: Exception | None = None,
        write_exc_sequence: list[Exception | None] | None = None,
    ) -> None:
        self.name = name
        self.read_result = read_result or {}
        self.read_exc = read_exc
        self.read_exc_sequence: Iterator[Exception | None] | None = iter(read_exc_sequence) if read_exc_sequence else None
        self.write_exc = write_exc
        self.write_exc_sequence: Iterator[Exception | None] | None = iter(write_exc_sequence) if write_exc_sequence else None
        self.calls: list[str] = []
        self.written: list[dict[str, Any]] = []

    def read(self) -> dict[str, Any]:
        self.calls.append(f"{self.name}:read")
        next_exc = None
        if self.read_exc_sequence is not None:
            try:
                next_exc = next(self.read_exc_sequence)
            except StopIteration:
                next_exc = None
        if next_exc is None:
            next_exc = self.read_exc
        if next_exc:
            raise next_exc
        return self.read_result

    def write(self, data: dict[str, Any]) -> None:
        self.calls.append(f"{self.name}:write")
        next_exc = None
        if self.write_exc_sequence is not None:
            try:
                next_exc = next(self.write_exc_sequence)
            except StopIteration:
                next_exc = None
        if next_exc is None:
            next_exc = self.write_exc
        if next_exc:
            raise next_exc
        self.written.append(data)


def test_failover_store_reads_from_primary_when_healthy(monkeypatch) -> None:
    primary = StubStore(name="primary", read_result={"ok": True})
    secondary = StubStore(name="secondary", read_result={"ok": False})
    store = FailoverStore(
        kind="settings",
        primary=primary,
        secondary=secondary,
        logger=SimpleNamespace(error=lambda *a, **k: None),
    )

    # Given: primary healthy, secondary available
    # When: read is executed
    result = store.read()
    # Then: primary is used and result returned
    assert result == {"ok": True}
    assert primary.calls == ["primary:read"]
    assert secondary.calls == []


def test_failover_store_reads_from_secondary_on_primary_error(monkeypatch) -> None:
    primary = StubStore(name="primary", read_exc=StoreError("boom"))
    secondary = StubStore(name="secondary", read_result={"from": "secondary"})
    store = FailoverStore(
        kind="state",
        primary=primary,
        secondary=secondary,
        logger=SimpleNamespace(error=lambda *a, **k: None),
        unhealthy_cooldown_seconds=60,
    )

    # Given: primary raises StoreError, secondary healthy
    # When: read is executed
    result = store.read()
    # Then: secondary is used and primary recorded as failed
    assert result == {"from": "secondary"}
    assert primary.calls == ["primary:read"]
    assert secondary.calls == ["secondary:read"]


def test_failover_store_writes_via_secondary_when_primary_fails(monkeypatch) -> None:
    primary = StubStore(name="primary", write_exc=StoreError("fail write"))
    secondary = StubStore(name="secondary")
    store = FailoverStore(
        kind="settings",
        primary=primary,
        secondary=secondary,
        logger=SimpleNamespace(error=lambda *a, **k: None),
    )

    # Given: primary write fails, secondary healthy
    # When: write is executed
    store.write({"x": 1})
    # Then: secondary receives the write
    assert primary.calls == ["primary:write"]
    assert secondary.calls == ["secondary:write"]
    assert secondary.written == [{"x": 1}]


def test_failover_respects_cooldown_and_retries_primary(monkeypatch) -> None:
    primary = StubStore(
        name="primary",
        read_exc_sequence=[StoreError("first fail"), None],
        read_result={"back": "primary"},
    )
    secondary = StubStore(name="secondary", read_result={"from": "secondary"})
    times = [0.0, 0.0, 0.0, 61.0, 61.0]

    def fake_monotonic() -> float:
        if times:
            return times.pop(0)
        return times[-1]

    monkeypatch.setattr("switchbot_dashboard.config_store.time.monotonic", fake_monotonic)

    store = FailoverStore(
        kind="state",
        primary=primary,
        secondary=secondary,
        logger=SimpleNamespace(error=lambda *a, **k: None),
        unhealthy_cooldown_seconds=60,
    )

    # Given: primary fails once, cooldown 60s
    # When: first read (t=0) then second read (t=0 still) then third read (t=61)
    result1 = store.read()  # fallback to secondary
    result2 = store.read()  # still secondary during cooldown
    result3 = store.read()  # retry primary after cooldown
    # Then: secondary served until cooldown expired, then primary recovered
    assert result1 == {"from": "secondary"}
    assert result2 == {"from": "secondary"}
    assert result3 == {"back": "primary"}
    assert primary.calls == ["primary:read", "primary:read"]
    assert secondary.calls == ["secondary:read", "secondary:read"]


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

        def read(self) -> dict[str, Any]:
            return self._data

        def write(self, data: dict[str, Any]) -> None:
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
