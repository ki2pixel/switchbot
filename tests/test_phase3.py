from __future__ import annotations

from unittest.mock import MagicMock, patch
from flask import Flask

from switchbot_dashboard.config_store import JsonStore
from switchbot_dashboard.postgres_store import PostgresStore


def test_json_store_transaction_success(tmp_path):
    # Setup a JsonStore
    store_file = tmp_path / "test_store.json"
    store = JsonStore(str(store_file))
    
    # Write initial data
    store.write({"key": "initial"})
    assert store_file.exists()
    
    # Enter transaction
    with store.transaction():
        # Read inside transaction
        data = store.read()
        assert data == {"key": "initial"}
        
        # Write inside transaction (multiple times)
        data["key"] = "modified_once"
        store.write(data)
        
        # Read back inside transaction should reflect cached state
        assert store.read() == {"key": "modified_once"}
        
        data["key"] = "modified_final"
        store.write(data)
        
        # Ensure the file on disk is NOT updated yet (Write-Back Cache)
        # We read from a raw store bypass or check the actual file directly
        raw_store = JsonStore(str(store_file))
        assert raw_store.read() == {"key": "initial"}
        
    # After transaction commits, the file should be updated to the final state
    assert store.read() == {"key": "modified_final"}
    raw_store = JsonStore(str(store_file))
    assert raw_store.read() == {"key": "modified_final"}


def test_json_store_transaction_rollback(tmp_path):
    store_file = tmp_path / "test_store.json"
    store = JsonStore(str(store_file))
    store.write({"key": "initial"})
    
    # Transaction raises exception
    try:
        with store.transaction():
            data = store.read()
            data["key"] = "failed_modification"
            store.write(data)
            raise ValueError("Some transaction error")
    except ValueError:
        pass
        
    # State should remain initial
    assert store.read() == {"key": "initial"}
    raw_store = JsonStore(str(store_file))
    assert raw_store.read() == {"key": "initial"}


def test_postgres_store_transaction_success():
    # Mock pool and connection
    mock_pool = MagicMock()
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    
    # psycopg 3 connection pool returns a context manager
    mock_conn_ctx = MagicMock()
    mock_pool.connection.return_value = mock_conn_ctx
    mock_conn_ctx.__enter__.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    
    # SELECT ... FOR UPDATE returns mock row
    mock_cur.fetchone.return_value = {"data": {"key": "initial_db"}}
    
    logger = MagicMock()
    
    # Instantiate PostgresStore
    store = PostgresStore(
        kind="state",
        logger=logger,
        pool=mock_pool,
    )
    
    # Run transaction
    with store.transaction():
        data = store.read()
        assert data == {"key": "initial_db"}
        
        data["key"] = "final_db"
        store.write(data)
        
    # Verify mock calls
    mock_conn.cursor.assert_called()
    mock_cur.execute.assert_any_call("SELECT data FROM json_store WHERE kind = %s FOR UPDATE", ("state",))
    mock_conn.commit.assert_called()
    mock_conn.rollback.assert_not_called()


def test_postgres_store_transaction_rollback():
    mock_pool = MagicMock()
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    
    # psycopg 3 connection pool returns a context manager
    mock_conn_ctx = MagicMock()
    mock_pool.connection.return_value = mock_conn_ctx
    mock_conn_ctx.__enter__.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchone.return_value = {"data": {"key": "initial_db"}}
    
    logger = MagicMock()
    
    store = PostgresStore(
        kind="state",
        logger=logger,
        pool=mock_pool,
    )
    
    try:
        with store.transaction():
            data = store.read()
            data["key"] = "failed_db"
            store.write(data)
            raise RuntimeError("Database crash simulate")
    except RuntimeError:
        pass
        
    # Verify rollback was called instead of commit
    mock_conn.rollback.assert_called()


def test_history_api_503_fallback_in_production():
    from switchbot_dashboard.routes import dashboard_bp
    
    app = Flask(__name__)
    app.secret_key = "test_secret"
    app.config["RATELIMIT_ENABLED"] = False
    
    # Register blueprint
    app.register_blueprint(dashboard_bp)
    
    # Initialize limiter with mock to avoid errors
    from switchbot_dashboard.extensions import limiter
    limiter.init_app(app)
    
    # Simulate production mode (debug=False, testing=False)
    # Since pytest runs with app.testing=True by default, we explicitly set app.testing=False
    app.testing = False
    app.debug = False
    
    # settings_store and state_store must be present in app.extensions
    mock_store = MagicMock()
    mock_store.read.return_value = {}
    app.extensions["settings_store"] = mock_store
    app.extensions["state_store"] = mock_store
    app.extensions["switchbot_client"] = MagicMock()
    app.extensions["scheduler_service"] = MagicMock()
    
    # We do NOT register history_service
    assert "history_service" not in app.extensions
    
    with app.test_client() as client:
        # Check /history/api/data returns 503
        response = client.get("/history/api/data")
        assert response.status_code == 503
        json_data = response.get_json()
        assert "error" in json_data
        assert "La base de données PostgreSQL est déconnectée" in json_data["error"]
        
        # Check /history/api/aggregates returns 503
        response = response = client.get("/history/api/aggregates")
        assert response.status_code == 503
        
        # Check /history/api/latest returns 503
        response = client.get("/history/api/latest")
        assert response.status_code == 503


def test_switchbot_client_status_caching():
    from switchbot_dashboard.switchbot_api import SwitchBotClient
    
    client = SwitchBotClient(token="test", secret="test")
    client._request = MagicMock(return_value={"body": {"temperature": 22.5}})
    
    res1 = client.get_device_status("meter_1")
    res2 = client.get_device_status("meter_1")
    
    client._request.assert_called_once_with("GET", "/v1.1/devices/meter_1/status")
    assert res1 == res2


def test_switchbot_client_devices_caching():
    from switchbot_dashboard.switchbot_api import SwitchBotClient
    
    client = SwitchBotClient(token="test", secret="test")
    client._request = MagicMock(return_value={"body": {"deviceList": []}})
    
    res1 = client.get_devices()
    res2 = client.get_devices()
    
    client._request.assert_called_once_with("GET", "/v1.1/devices")
    assert res1 == res2


def test_switchbot_client_retry_delay_cap():
    from switchbot_dashboard.switchbot_api import SwitchBotClient
    import requests
    
    client = SwitchBotClient(token="test", secret="test", retry_delay_seconds=10, retry_attempts=2)
    
    with patch("requests.request", side_effect=requests.RequestException("failing")), \
         patch("time.sleep") as mock_sleep:
        try:
            client.get_devices()
        except Exception:
            pass
        
        assert mock_sleep.call_count == 1
        args, _ = mock_sleep.call_args
        # With exponential backoff (min(10 * 2^0, 5) = 5) + jitter (0-0.5), delay should be between 5.0 and 5.5
        assert 5.0 <= args[0] <= 5.5


def test_settings_validation_mode_error():
    from switchbot_dashboard.routes import dashboard_bp
    
    app = Flask(__name__)
    app.secret_key = "test"
    app.register_blueprint(dashboard_bp)
    
    from switchbot_dashboard.extensions import limiter
    limiter.init_app(app)
    
    mock_store = MagicMock()
    mock_store.read.return_value = {}
    app.extensions["settings_store"] = mock_store
    app.extensions["state_store"] = mock_store
    app.extensions["switchbot_client"] = MagicMock()
    app.extensions["scheduler_service"] = MagicMock()
    
    with app.test_client() as client:
        response = client.post("/settings", data={"mode": "invalid_mode"})
        assert response.status_code == 302
        with client.session_transaction() as sess:
            flashes = sess.get("_flashes", [])
            assert any("Le mode sélectionné est invalide" in msg[1] for msg in flashes)


def test_settings_validation_device_id_error():
    from switchbot_dashboard.routes import dashboard_bp
    
    app = Flask(__name__)
    app.secret_key = "test"
    app.register_blueprint(dashboard_bp)
    
    from switchbot_dashboard.extensions import limiter
    limiter.init_app(app)
    
    mock_store = MagicMock()
    mock_store.read.return_value = {"mode": "winter"}
    app.extensions["settings_store"] = mock_store
    app.extensions["state_store"] = mock_store
    app.extensions["switchbot_client"] = MagicMock()
    app.extensions["scheduler_service"] = MagicMock()
    
    with app.test_client() as client:
        response = client.post("/settings", data={
            "mode": "winter",
            "meter_device_id": "a" * 51,
            "aircon_device_id": "valid_ac"
        })
        assert response.status_code == 302
        with client.session_transaction() as sess:
            flashes = sess.get("_flashes", [])
            assert any("L'ID du capteur est invalide" in msg[1] for msg in flashes)


def test_session_rotation_post_login_success():
    from switchbot_dashboard.routes import dashboard_bp
    
    app = Flask(__name__)
    app.secret_key = "test_rotation"
    app.config["DASHBOARD_PASSWORD"] = "secret123"
    app.register_blueprint(dashboard_bp)
    
    from switchbot_dashboard.extensions import limiter
    limiter.init_app(app)
    
    mock_store = MagicMock()
    mock_store.read.return_value = {}
    app.extensions["settings_store"] = mock_store
    app.extensions["state_store"] = mock_store
    app.extensions["switchbot_client"] = MagicMock()
    app.extensions["scheduler_service"] = MagicMock()
    
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess["some_pre_existing_data"] = "stays"
            
        response = client.post("/login", data={"password": "secret123"})
        assert response.status_code == 302
        
        with client.session_transaction() as sess:
            assert sess.get("logged_in") is True
            assert sess.get("some_pre_existing_data") == "stays"
