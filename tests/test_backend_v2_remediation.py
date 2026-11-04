"""Cross-cutting regression tests for the V2 backend audit remediation.

Test perspectives
-----------------
| Case ID | Input / Precondition | Perspective | Expected Result |
| --- | --- | --- | --- |
| SEC-05-a | `_safe_int(True)` | Boundary (bool) | Returns the default, not 1 |
| SEC-05-b | naive start + aware end | Equivalence | Parsed as aware UTC, no TypeError |
| SEC-05-c | `metrics=evil` | Error | ValueError (400 on the route) |
| SEC-05-d | 40-day range | Boundary | ValueError |
| SEC-05-e | mixed valid/invalid metrics | Equivalence | Only whitelisted metrics kept |
| SEC-05-f | `limit=999999` | Boundary | Clamped to 10000 |
| AUTH-a | non-ASCII password match | Boundary (UTF-8) | 302, no TypeError/500 |
| AUTH-b | non-ASCII wrong password | Error | 200 with error message |
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import pytest

from switchbot_dashboard.config_store import StoreError


def test_safe_int_rejects_bool() -> None:
    from switchbot_dashboard.utils import _safe_int

    # Given/When: a bool is a subclass of int in Python
    result = _safe_int(True, default=42)

    # Then: it must not be silently coerced to 1
    assert result == 42


def test_history_params_accept_mixed_naive_and_aware_dates() -> None:
    from switchbot_dashboard.routes import _parse_history_query_params

    # Given: one naive and one aware datetime
    args = {
        "start": "2026-01-01T08:00:00",
        "end": "2026-01-01T12:00:00+02:00",
    }

    # When: parsing
    start, end, metrics, granularity, limit = _parse_history_query_params(args)

    # Then: both are aware, no TypeError
    assert start.tzinfo is not None
    assert end.tzinfo is not None
    assert start == dt.datetime(2026, 1, 1, 8, 0, tzinfo=dt.timezone.utc)
    assert end == dt.datetime(2026, 1, 1, 10, 0, tzinfo=dt.timezone.utc)
    assert metrics is None
    assert granularity == "minute"
    assert limit == 1000


def test_history_params_reject_unknown_metrics() -> None:
    from switchbot_dashboard.routes import _parse_history_query_params

    # Given/When/Then: only invalid metrics were requested
    with pytest.raises(ValueError, match="no valid metrics"):
        _parse_history_query_params({"metrics": "evil,__class__"})


def test_history_params_filter_metrics_whitelist() -> None:
    from switchbot_dashboard.routes import _parse_history_query_params

    # Given/When: one valid and one payload-like metric
    _start, _end, metrics, _granularity, _limit = _parse_history_query_params(
        {
            "start": "2026-01-01T00:00:00Z",
            "end": "2026-01-01T01:00:00Z",
            "metrics": "temperature,evil",
        }
    )

    # Then: only the whitelisted metric survives
    assert metrics == ["temperature"]


def test_history_params_reject_range_over_31_days() -> None:
    from switchbot_dashboard.routes import _parse_history_query_params

    # Given/When/Then: a 40-day range exceeds the documented maximum
    with pytest.raises(ValueError, match="31 days"):
        _parse_history_query_params(
            {
                "start": "2026-01-01T00:00:00Z",
                "end": "2026-02-10T00:00:00Z",
            }
        )


def test_history_params_clamp_limit() -> None:
    from switchbot_dashboard.routes import _parse_history_query_params

    # Given/When: an oversized limit
    _start, _end, _metrics, _granularity, limit = _parse_history_query_params(
        {"limit": "999999"}
    )

    # Then: the hard cap applies
    assert limit == 10000


def test_login_accepts_non_ascii_password(monkeypatch, tmp_path) -> None:
    from switchbot_dashboard import create_app

    settings_path = tmp_path / "settings.json"
    state_path = tmp_path / "state.json"
    settings_path.write_text("{}", encoding="utf-8")
    state_path.write_text("{}", encoding="utf-8")

    monkeypatch.setenv("SWITCHBOT_SETTINGS_PATH", str(settings_path))
    monkeypatch.setenv("SWITCHBOT_STATE_PATH", str(state_path))
    monkeypatch.setenv("STORE_BACKEND", "filesystem")
    monkeypatch.setenv("DASHBOARD_PASSWORD", "pässwörd-€")
    monkeypatch.setenv("SCHEDULER_ENABLED", "false")

    app = create_app()
    app.config["WTF_CSRF_ENABLED"] = False
    app.config["RATELIMIT_ENABLED"] = False

    with app.test_client() as client:
        # Given/When: the matching non-ASCII password is submitted
        response = client.post("/login", data={"password": "pässwörd-€"})

        # Then: constant-time comparison handles UTF-8 instead of raising
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/")

    with app.test_client() as client:
        # Given/When: a wrong non-ASCII password is submitted
        response = client.post("/login", data={"password": "möt-de-passe"})

        # Then: the login form is re-rendered, not a 500
        assert response.status_code == 200
        assert b"Mot de passe incorrect." in response.data


def _load_script_module(name: str, filename: str):
    import importlib.util

    path = Path(__file__).resolve().parents[1] / "scripts" / filename
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_migration_module():
    return _load_script_module("migrate_to_postgres_test", "migrate_to_postgres.py")


def _load_drop_indexes_module():
    return _load_script_module("drop_redundant_indexes_test", "drop_redundant_indexes.py")


def test_migration_url_description_never_leaks_credentials() -> None:
    module = _load_migration_module()

    # Given/When: a Neon URL containing userinfo and query parameters
    description = module._describe_url(
        "postgresql://alice:s3cr3t@ep-neon.example.com:5432/switchbot?sslmode=require"
    )

    # Then: only scheme/host/port/database remain
    assert description == "postgresql://ep-neon.example.com:5432/switchbot"
    assert "alice" not in description
    assert "s3cr3t" not in description
    assert "sslmode" not in description


def test_migration_url_description_handles_at_sign_in_password() -> None:
    module = _load_migration_module()

    # Given/When: a password containing '@' (the old regex leaked the suffix)
    description = module._describe_url("postgresql://alice:p@ss@ep-neon.example.com/db")

    # Then: no credential fragment survives
    assert description == "postgresql://ep-neon.example.com/db"
    assert "p@ss" not in description


def test_migration_closes_all_stores(monkeypatch, tmp_path) -> None:
    module = _load_migration_module()
    from unittest.mock import MagicMock, patch

    settings_store = MagicMock()
    state_store = MagicMock()
    created = [settings_store, state_store]

    def _factory(**kwargs):
        return created.pop(0)

    settings_path = tmp_path / "settings.json"
    state_path = tmp_path / "state.json"
    settings_path.write_text("{}", encoding="utf-8")
    state_path.write_text("{}", encoding="utf-8")

    # Given: two stores created during the migration
    with patch.object(module, "PostgresStore", side_effect=_factory), patch.object(
        module, "_read_and_validate_data", side_effect=[{"a": 1}, {"b": 2}]
    ):
        # When: the migration runs
        result = module.migrate_to_postgres(
            postgres_url="postgresql://user:pass@host/db",
            redis_url=None,
            settings_path=str(settings_path),
            state_path=str(state_path),
            dry_run=False,
            logger=MagicMock(),
        )

    # Then: both stores are closed even on the success path
    assert result is True
    settings_store.close.assert_called_once()
    state_store.close.assert_called_once()


class _FakePrimaryStore:
    def __init__(self, *, failures: int = 0, data: dict | None = None) -> None:
        self.failures = failures
        self.data = data or {"source": "primary"}
        self.calls = 0
        self.writes: list[dict] = []

    def _maybe_fail(self) -> None:
        self.calls += 1
        if self.failures > 0:
            self.failures -= 1
            raise StoreError("primary down")

    def read(self) -> dict:
        self._maybe_fail()
        return dict(self.data)

    def write(self, data: dict) -> None:
        self._maybe_fail()
        self.writes.append(dict(data))
        self.data = dict(data)

    def transaction(self):
        return _FakeTransaction()

    def health_check(self) -> bool:
        return self.failures == 0


class _FakeTransaction:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


class _FailingTransaction(_FakeTransaction):
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise StoreError("commit failed")


class _FakeFallbackStore:
    def __init__(self) -> None:
        self.data: dict = {}
        self.reads = 0
        self.writes: list[dict] = []

    def read(self) -> dict:
        self.reads += 1
        return dict(self.data)

    def write(self, data: dict) -> None:
        self.writes.append(dict(data))
        self.data = dict(data)

    def transaction(self):
        return _FakeTransaction()


def _make_resilient(primary, fallback, *, allow=True, threshold=3, caplog=None):
    from switchbot_dashboard.store_resilience import ResilientStore

    return ResilientStore(
        primary,
        fallback,
        logger=__import__("logging").getLogger("test.store"),
        name="state",
        failure_threshold=threshold,
        allow_fallback=allow,
    )


def test_resilient_store_switches_after_three_failures(caplog) -> None:
    import logging

    primary = _FakePrimaryStore(failures=3)
    fallback = _FakeFallbackStore()
    store = _make_resilient(primary, fallback)
    caplog.set_level(logging.CRITICAL)

    # Given/When: the primary fails three consecutive times
    with pytest.raises(StoreError):
        store.read()
    with pytest.raises(StoreError):
        store.read()
    result = store.read()

    # Then: the third failure switches to the fallback
    assert result == {}
    assert store.degraded is True
    assert store.consecutive_failures == 3
    assert any("CRITICAL" in record.message for record in caplog.records)
    assert any("Switching state store" in record.message for record in caplog.records)

    # Then: subsequent reads do not touch the primary anymore
    calls_before = primary.calls
    store.read()
    assert primary.calls == calls_before
    assert fallback.reads >= 2


def test_resilient_store_resets_counter_on_success() -> None:
    primary = _FakePrimaryStore(failures=1)
    store = _make_resilient(primary, _FakeFallbackStore())

    # Given/When: one failure followed by a success
    with pytest.raises(StoreError):
        store.read()
    assert store.consecutive_failures == 1
    store.read()

    # Then: the consecutive counter is reset
    assert store.consecutive_failures == 0
    assert store.degraded is False


def test_resilient_store_alerts_without_switching_when_disabled(caplog) -> None:
    import logging

    primary = _FakePrimaryStore(failures=3)
    fallback = _FakeFallbackStore()
    store = _make_resilient(primary, fallback, allow=False)
    caplog.set_level(logging.CRITICAL)

    # Given/When: production mode (no automatic fallback)
    for _ in range(3):
        with pytest.raises(StoreError):
            store.read()

    # Then: it alerts but never degrades
    assert store.degraded is False
    assert any("CRITICAL" in record.message for record in caplog.records)
    assert fallback.reads == 0


def test_resilient_store_does_not_switch_mid_transaction() -> None:
    import logging

    from switchbot_dashboard.store_resilience import ResilientStore

    class _TxFailingReadPrimary(_FakePrimaryStore):
        def read(self) -> dict:
            self.calls += 1
            raise StoreError("read inside tx")

    primary = _TxFailingReadPrimary()
    fallback = _FakeFallbackStore()
    store = ResilientStore(
        primary,
        fallback,
        logger=logging.getLogger("test.store"),
        name="state",
        failure_threshold=1,
        allow_fallback=True,
    )

    # Given/When: a read fails inside an open transaction
    with store.transaction():
        with pytest.raises(StoreError):
            store.read()
        # Then: the backend is not switched while the transaction is open
        assert store.degraded is False

    # Then: the switch is deferred until the transaction exits
    assert store.degraded is True


def test_resilient_store_seeds_fallback_with_last_good_snapshot() -> None:
    primary = _FakePrimaryStore(failures=0, data={"value": 42})
    fallback = _FakeFallbackStore()
    store = _make_resilient(primary, fallback)

    # Given: a successful read populates the snapshot
    assert store.read() == {"value": 42}

    # When: the primary then fails three times
    primary.failures = 3
    with pytest.raises(StoreError):
        store.read()
    with pytest.raises(StoreError):
        store.read()
    result = store.read()

    # Then: the fallback starts from the last known good state
    assert result == {"value": 42}
    assert fallback.data == {"value": 42}


def test_resilient_store_recovery_inside_transaction_cancels_pending_switch() -> None:
    primary = _FakePrimaryStore(failures=1)
    fallback = _FakeFallbackStore()
    store = _make_resilient(primary, fallback, threshold=1)

    # Given/When: a read fails inside a transaction, then a retry succeeds
    with store.transaction():
        with pytest.raises(StoreError):
            store.read()
        assert store.degraded is False
        store.read()

    # Then: the successful retry cancelled the pending switch
    assert store.degraded is False
    assert store.consecutive_failures == 0
    assert fallback.reads == 0


def test_resilient_store_does_not_switch_while_other_thread_in_transaction() -> None:
    import logging
    import threading

    from switchbot_dashboard.store_resilience import ResilientStore

    class _SlowTxPrimary(_FakePrimaryStore):
        def transaction(self):
            return _SlowTransaction(tx_started, tx_release)

    tx_started = threading.Event()
    tx_release = threading.Event()

    primary = _SlowTxPrimary(failures=1)
    fallback = _FakeFallbackStore()
    store = ResilientStore(
        primary,
        fallback,
        logger=logging.getLogger("test.store"),
        name="state",
        failure_threshold=1,
        allow_fallback=True,
    )

    def _hold_transaction() -> None:
        with store.transaction():
            tx_started.set()
            tx_release.wait(5)

    worker = threading.Thread(target=_hold_transaction)
    worker.start()
    assert tx_started.wait(5)

    # Given/When: another thread hits the threshold while a transaction is open
    with pytest.raises(StoreError):
        store.read()

    # Then: the switch waits for the transaction to finish
    assert store.degraded is False

    tx_release.set()
    worker.join(5)
    assert store.degraded is True


class _SlowTransaction:
    def __init__(self, started, release) -> None:
        self._started = started
        self._release = release

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


def test_redundant_indexes_are_not_created_anymore() -> None:
    root = Path(__file__).resolve().parents[1]

    sources = {
        "postgres_store.py": root / "switchbot_dashboard" / "postgres_store.py",
        "history_service.py": root / "switchbot_dashboard" / "history_service.py",
        "schema.sql": root / "scripts" / "schema.sql",
        "create_history_table.sql": root / "scripts" / "create_history_table.sql",
    }
    contents = {name: path.read_text(encoding="utf-8") for name, path in sources.items()}

    # Given/Then: the duplicated PK index and unused GIN index are gone from
    # both the runtime bootstrap and the manual bootstrap scripts
    assert "idx_json_store_kind" not in contents["postgres_store.py"]
    assert "idx_json_store_kind" not in contents["schema.sql"]
    assert "idx_state_history_metadata" not in contents["history_service.py"]
    assert "idx_state_history_metadata" not in contents["create_history_table.sql"]


class _MemoryStore:
    def __init__(self, initial: dict | None = None) -> None:
        import copy

        self._data = copy.deepcopy(initial or {})

    def read(self) -> dict:
        import copy

        return copy.deepcopy(self._data)

    def write(self, data: dict) -> None:
        import copy

        self._data = copy.deepcopy(data)


class _StolenLockAutomation:
    def __init__(self) -> None:
        from types import SimpleNamespace

        self._local = SimpleNamespace(current_lock_token=None)
        self.released = False

    def _acquire_lock(self) -> bool:
        return True

    def _release_lock(self) -> None:
        self.released = True

    def apply_state_updates(self, **updates) -> None:
        from switchbot_dashboard.automation import LockLostError

        raise LockLostError("lock stolen")


class _DummySwitchBotClient:
    def send_command(self, *args, **kwargs) -> None:
        return None

    def run_scene(self, *args, **kwargs) -> None:
        return None


def _build_minimal_action_app(automation_service) -> object:
    from flask import Flask

    from switchbot_dashboard.extensions import limiter
    from switchbot_dashboard.routes import dashboard_bp

    app = Flask(__name__)
    app.secret_key = "test"
    app.config["WTF_CSRF_ENABLED"] = False
    app.config["RATELIMIT_ENABLED"] = False
    limiter.init_app(app)
    app.extensions["settings_store"] = _MemoryStore(
        {"aircon_device_id": "aircon-1", "aircon_scenes": {}}
    )
    app.extensions["state_store"] = _MemoryStore({})
    app.extensions["automation_service"] = automation_service
    app.extensions["switchbot_client"] = _DummySwitchBotClient()
    app.register_blueprint(dashboard_bp)
    return app


def test_manual_action_catches_lock_lost_and_clears_token() -> None:
    automation = _StolenLockAutomation()
    app = _build_minimal_action_app(automation)

    with app.test_client() as client:
        # Given/When: the lock is stolen before the state write
        response = client.post("/actions/aircon_off")

    # Then: the route returns a redirect instead of a 500, releases the lock
    assert response.status_code == 302
    assert automation.released is True
    assert automation._local.current_lock_token is None


def test_run_once_route_rejects_concurrent_cycle() -> None:
    from switchbot_dashboard import routes as routes_module

    class _Automation:
        def __init__(self) -> None:
            self.called = False

        def run_once(self) -> None:
            self.called = True

    automation = _Automation()
    app = _build_minimal_action_app(automation)
    app.extensions["scheduler_service"] = object()

    acquired = routes_module._run_once_lock.acquire(blocking=False)
    assert acquired is True
    try:
        with app.test_client() as client:
            # Given/When: a cycle is already running
            response = client.post("/actions/run_once")
    finally:
        routes_module._run_once_lock.release()

    # Then: no second thread is spawned
    assert response.status_code == 302
    assert automation.called is False


# ---------------------------------------------------------------------------
# scripts/drop_redundant_indexes.py
#
# | Case ID | Input / Precondition                      | Perspective      | Expected Result                                   |
# |---------|-------------------------------------------|------------------|---------------------------------------------------|
# | DROP-01 | URL with userinfo + query                 | Security         | userinfo/query never appear in the description    |
# | DROP-02 | no POSTGRES_URL                           | Error (missing)  | exit code 2, no connection attempted              |
# | DROP-03 | existing indexes, no --apply              | Normal (dry run) | exit 0, zero DROP statements                      |
# | DROP-04 | existing indexes, --apply                 | Normal           | both indexes dropped, exit 0                      |
# | DROP-05 | indexes already absent, --apply           | Boundary (empty) | exit 0, zero DROP statements                      |
# | DROP-06 | --index restricts target                  | Boundary         | one DROP only, the other index survives           |
# | DROP-07 | .env with comments, blanks, quotes        | Equivalence      | parsed values only, comments ignored              |
# ---------------------------------------------------------------------------


class _FakePgCursor:
    def __init__(self, state: dict) -> None:
        self._state = state
        self._rows: list = []

    def execute(self, sql: str, params=None) -> None:
        self._state["log"].append((sql, params))
        normalized = " ".join(sql.split())

        if "current_database" in normalized:
            self._rows = [("switchbot", "tester")]
            return

        if "FROM pg_indexes" in normalized:
            wanted = set(params[0]) if params else set()
            self._rows = [
                row for row in self._state["indexes"] if row[0] in wanted
            ]
            return

        if normalized.startswith("DROP INDEX"):
            dropped = normalized.split(".")[-1].strip()
            self._state["indexes"] = [
                row for row in self._state["indexes"] if row[0] != dropped
            ]
            self._state["dropped"].append(dropped)
            self._rows = []
            return

        self._rows = []

    def fetchone(self):
        return self._rows[0] if self._rows else None

    def fetchall(self):
        return list(self._rows)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class _FakePgConnection:
    def __init__(self, state: dict) -> None:
        self._state = state

    def cursor(self) -> _FakePgCursor:
        return _FakePgCursor(self._state)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


def _install_fake_psycopg(monkeypatch, indexes: list[tuple[str, str, str]]) -> dict:
    import sys
    import types

    state: dict = {"indexes": list(indexes), "log": [], "dropped": [], "connect": 0}

    def _connect(*args, **kwargs):
        state["connect"] += 1
        state["connect_kwargs"] = kwargs
        return _FakePgConnection(state)

    module = types.ModuleType("psycopg")
    module.connect = _connect  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "psycopg", module)
    return state


def test_drop_indexes_url_description_masks_credentials() -> None:
    module = _load_drop_indexes_module()

    # Given/When: a production URL with userinfo and query parameters
    description = module.describe_url(
        "postgresql://postgres:p4ss@aws-1-eu-central-1.pooler.supabase.com:5432/postgres?sslmode=require"
    )

    # Then: only scheme/host/port/database survive
    assert description == (
        "postgresql://aws-1-eu-central-1.pooler.supabase.com:5432/postgres"
    )
    assert "p4ss" not in description
    assert "sslmode" not in description


def test_drop_indexes_requires_postgres_url(monkeypatch, caplog) -> None:
    module = _load_drop_indexes_module()
    monkeypatch.delenv("POSTGRES_URL", raising=False)
    caplog.set_level("INFO")

    # Given/When: no DSN in the environment and an empty .env
    exit_code = module.main(["--env", "/nonexistent/.env"])

    # Then: it fails fast with code 2 and explains what is missing
    assert exit_code == 2
    assert any(
        "POSTGRES_URL is not set" in record.getMessage()
        for record in caplog.records
    )


def test_drop_indexes_dry_run_never_drops(monkeypatch, caplog) -> None:
    module = _load_drop_indexes_module()
    monkeypatch.setenv("POSTGRES_URL", "postgresql://u:p@host:5432/db")
    state = _install_fake_psycopg(
        monkeypatch,
        [("idx_json_store_kind", "json_store", "16 kB")],
    )
    caplog.set_level("INFO")

    # Given/When: the default invocation (no --apply)
    exit_code = module.main([])

    # Then: the index is reported but no DROP is executed
    assert exit_code == 0
    assert state["dropped"] == []
    assert any(
        "Dry run: no changes applied" in record.getMessage()
        for record in caplog.records
    )


def test_drop_indexes_apply_drops_both_targets(monkeypatch) -> None:
    module = _load_drop_indexes_module()
    monkeypatch.setenv("POSTGRES_URL", "postgresql://u:p@host:5432/db")
    state = _install_fake_psycopg(
        monkeypatch,
        [
            ("idx_json_store_kind", "json_store", "16 kB"),
            ("idx_state_history_metadata", "state_history", "122 MB"),
        ],
    )

    # Given/When: --apply is passed
    exit_code = module.main(["--apply"])

    # Then: both indexes are dropped concurrently in autocommit mode
    assert exit_code == 0
    assert sorted(state["dropped"]) == [
        "idx_json_store_kind",
        "idx_state_history_metadata",
    ]
    assert state["connect"] == 1
    assert state["connect_kwargs"]["autocommit"] is True
    drop_sql = [sql for sql, _ in state["log"] if sql.lstrip().startswith("DROP INDEX")]
    assert drop_sql and all("CONCURRENTLY" in sql for sql in drop_sql)


def test_drop_indexes_apply_is_noop_when_indexes_absent(monkeypatch) -> None:
    module = _load_drop_indexes_module()
    monkeypatch.setenv("POSTGRES_URL", "postgresql://u:p@host:5432/db")
    state = _install_fake_psycopg(monkeypatch, [])

    # Given/When: the cleanup already ran
    exit_code = module.main(["--apply"])

    # Then: nothing is executed and the script succeeds
    assert exit_code == 0
    assert state["dropped"] == []


def test_drop_indexes_index_option_restricts_scope(monkeypatch) -> None:
    module = _load_drop_indexes_module()
    monkeypatch.setenv("POSTGRES_URL", "postgresql://u:p@host:5432/db")
    state = _install_fake_psycopg(
        monkeypatch,
        [
            ("idx_json_store_kind", "json_store", "16 kB"),
            ("idx_state_history_metadata", "state_history", "122 MB"),
        ],
    )

    # Given/When: only the duplicated PK index is selected
    exit_code = module.main(["--apply", "--index", "idx_json_store_kind"])

    # Then: the GIN index is left untouched
    assert exit_code == 0
    assert state["dropped"] == ["idx_json_store_kind"]
    assert ("idx_state_history_metadata", "state_history", "122 MB") in state["indexes"]


def test_drop_indexes_env_parser_ignores_comments_and_quotes(tmp_path) -> None:
    module = _load_drop_indexes_module()
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "# comment",
                "",
                'POSTGRES_URL="postgresql://u:p@host:5432/db"',
                "POSTGRES_SSL_MODE='require'",
                "  SPACED_KEY = value  ",
                "MALFORMED_LINE",
            ]
        ),
        encoding="utf-8",
    )

    # Given/When: the minimal .env reader parses the file
    values = module.load_env_file(env_file)

    # Then: quotes are stripped, comments and malformed lines ignored
    assert values["POSTGRES_URL"] == "postgresql://u:p@host:5432/db"
    assert values["POSTGRES_SSL_MODE"] == "require"
    assert values["SPACED_KEY"] == "value"
    assert "MALFORMED_LINE" not in values



