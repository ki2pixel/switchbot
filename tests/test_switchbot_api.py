"""
Tests for SwitchBotClient module.

Covers:
- HMAC headers generation (t, nonce, Authorization, sign)
- Request retry behavior on HTTP 429 and 500
- Quota headers parsing (x-ratelimit-limit, x-ratelimit-remaining)
- SwitchBot custom API status codes (100, 190)
"""

from __future__ import annotations

import base64
import hashlib
import hmac
from unittest.mock import MagicMock, patch

import pytest
import requests

from switchbot_dashboard.switchbot_api import SwitchBotClient, SwitchBotApiError


@pytest.fixture
def mock_quota_tracker():
    """Mock quota tracker fixture."""
    tracker = MagicMock()
    tracker.record_from_headers.return_value = True
    return tracker


@pytest.fixture
def client(mock_quota_tracker) -> SwitchBotClient:
    """Create a standard client for testing."""
    return SwitchBotClient(
        token="test-token-12345",
        secret="test-secret-67890",
        retry_attempts=2,
        retry_delay_seconds=1,  # Set delay > 0 to enable retry logic
        quota_tracker=mock_quota_tracker,
    )


@pytest.fixture(autouse=True)
def mock_sleep():
    """Mock time.sleep globally for all tests in this module to run instantly."""
    with patch("time.sleep") as mock_s:
        yield mock_s




class TestSwitchBotClientInit:
    """Test initialization behavior of SwitchBotClient."""

    def test_init_params(self, mock_quota_tracker) -> None:
        c = SwitchBotClient(
            token=" token-abc ",
            secret=" secret-xyz ",
            base_url="https://custom.api.switch-bot.com/",
            retry_attempts=3,
            retry_delay_seconds=5,
            quota_tracker=mock_quota_tracker,
        )
        assert c._token == "token-abc"
        assert c._secret == "secret-xyz"
        assert c._base_url == "https://custom.api.switch-bot.com"
        assert c._retry_attempts == 3
        assert c._retry_delay_seconds == 5
        assert c._quota_tracker == mock_quota_tracker


class TestHMACHeaders:
    """Test HMAC header generation logic."""

    @patch("time.time")
    @patch("uuid.uuid4")
    def test_build_headers(self, mock_uuid, mock_time, client) -> None:
        mock_time.return_value = 1716800000.0  # static t = 1716800000000 ms
        mock_uuid.return_value = "static-uuid-1111"

        headers = client._build_headers()

        assert headers["Authorization"] == "test-token-12345"
        assert headers["Content-Type"] == "application/json; charset=utf-8"
        assert headers["t"] == "1716800000000"
        assert headers["nonce"] == "static-uuid-1111"

        # Verify HMAC signature
        string_to_sign = "test-token-123451716800000000static-uuid-1111".encode("utf-8")
        secret_bytes = "test-secret-67890".encode("utf-8")
        expected_sign = base64.b64encode(
            hmac.new(secret_bytes, msg=string_to_sign, digestmod=hashlib.sha256).digest()
        ).decode("utf-8")

        assert headers["sign"] == expected_sign

    def test_build_headers_missing_credentials(self) -> None:
        c = SwitchBotClient(token="", secret="")
        with pytest.raises(SwitchBotApiError, match="Missing SwitchBot credentials"):
            c._build_headers()


class TestQuotaTracking:
    """Test header quota extraction and metadata capture."""

    def test_capture_quota_metadata_present(self, client, mock_quota_tracker) -> None:
        mock_response = MagicMock(spec=requests.Response)
        mock_response.headers = {
            "x-ratelimit-limit": "10000",
            "x-ratelimit-remaining": "9950",
        }

        updated = client._capture_quota_metadata(mock_response)

        assert updated is True
        assert client.get_last_quota_snapshot() == {"limit": 10000, "remaining": 9950}
        mock_quota_tracker.record_from_headers.assert_called_once_with(limit=10000, remaining=9950)

    def test_capture_quota_metadata_absent(self, client, mock_quota_tracker) -> None:
        mock_response = MagicMock(spec=requests.Response)
        mock_response.headers = {}

        updated = client._capture_quota_metadata(mock_response)

        assert updated is True
        assert client.get_last_quota_snapshot() is None
        mock_quota_tracker.record_call.assert_called_once()

    def test_capture_quota_metadata_alternative_headers(self, client, mock_quota_tracker) -> None:
        mock_response = MagicMock(spec=requests.Response)
        mock_response.headers = {
            "ratelimit-limit": "5000",
            "ratelimit-remaining": "4000",
        }

        updated = client._capture_quota_metadata(mock_response)
        assert updated is True
        assert client.get_last_quota_snapshot() == {"limit": 5000, "remaining": 4000}


class TestClientRequestOperations:
    """Test requests retry behavior, error codes, and main API methods."""

    @patch("requests.request")
    def test_request_success(self, mock_request, client) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {}
        mock_response.json.return_value = {
            "statusCode": 100,
            "message": "success",
            "body": {"deviceList": []},
        }
        mock_request.return_value = mock_response

        res = client.get_devices()

        assert res["statusCode"] == 100
        assert mock_request.call_count == 1

    @patch("requests.request")
    def test_request_retries_on_500(self, mock_request, client) -> None:
        mock_response_500 = MagicMock()
        mock_response_500.status_code = 500
        mock_response_500.headers = {}

        mock_response_ok = MagicMock()
        mock_response_ok.status_code = 200
        mock_response_ok.headers = {}
        mock_response_ok.json.return_value = {
            "statusCode": 100,
            "message": "success",
            "body": {},
        }

        mock_request.side_effect = [mock_response_500, mock_response_ok]

        res = client._request("GET", "/test")

        assert res["statusCode"] == 100
        assert mock_request.call_count == 2

    @patch("requests.request")
    def test_request_fails_after_max_retries(self, mock_request, client) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.headers = {}
        mock_request.return_value = mock_response

        with pytest.raises(SwitchBotApiError, match="SwitchBot HTTP 500"):
            client._request("GET", "/test")

        assert mock_request.call_count == 2

    @patch("requests.request")
    def test_request_network_exception_retries(self, mock_request, client) -> None:
        mock_request.side_effect = [
            requests.RequestException("Network timeout"),
            requests.RequestException("Network timeout"),
        ]

        with pytest.raises(SwitchBotApiError, match="SwitchBot request failed"):
            client._request("GET", "/test")

        assert mock_request.call_count == 2

    @patch("requests.request")
    def test_request_status_190_retries(self, mock_request, client) -> None:
        mock_response_190 = MagicMock()
        mock_response_190.status_code = 200
        mock_response_190.headers = {}
        mock_response_190.json.return_value = {
            "statusCode": 190,
            "message": "device internal error",
        }

        mock_response_ok = MagicMock()
        mock_response_ok.status_code = 200
        mock_response_ok.headers = {}
        mock_response_ok.json.return_value = {
            "statusCode": 100,
            "message": "success",
        }

        mock_request.side_effect = [mock_response_190, mock_response_ok]

        res = client._request("GET", "/test")
        assert res["statusCode"] == 100
        assert mock_request.call_count == 2

    @patch("requests.request")
    def test_request_invalid_json(self, mock_request, client) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {}
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_request.return_value = mock_response

        with pytest.raises(SwitchBotApiError, match="Invalid JSON response"):
            client._request("GET", "/test")

    def test_get_device_status_validation(self, client) -> None:
        with pytest.raises(SwitchBotApiError, match="Missing device_id"):
            client.get_device_status("")

    def test_send_command_validation(self, client) -> None:
        with pytest.raises(SwitchBotApiError, match="Missing device_id"):
            client.send_command("", command="turnOff")

    def test_run_scene_validation(self, client) -> None:
        with pytest.raises(SwitchBotApiError, match="Missing scene_id"):
            client.run_scene("")

    @patch("requests.request")
    def test_run_scene_request(self, mock_request, client) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {}
        mock_response.json.return_value = {"statusCode": 100, "message": "success"}
        mock_request.return_value = mock_response

        client.run_scene("scene-uuid")

        mock_request.assert_called_once()
        assert "scenes/scene-uuid/execute" in mock_request.call_args[1]["url"]

    @patch("requests.request")
    def test_request_429_forces_remaining_to_zero(self, mock_request, client, mock_quota_tracker) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.headers = {}
        mock_response.json.return_value = {"message": "Too Many Requests"}
        mock_request.return_value = mock_response

        with pytest.raises(SwitchBotApiError, match="SwitchBot HTTP 429"):
            client.get_devices()

        mock_quota_tracker.record_from_headers.assert_any_call(limit=None, remaining=0)
