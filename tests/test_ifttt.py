from __future__ import annotations

from unittest.mock import Mock, patch

import pytest
import requests

from switchbot_dashboard.ifttt import (
    IFTTTWebhookClient,
    IFTTTWebhookError,
    extract_ifttt_webhooks,
    validate_webhook_url,
)


class TestValidateWebhookUrl:
    def test_valid_https_url(self) -> None:
        assert validate_webhook_url("https://maker.ifttt.com/trigger/event/with/key")

    def test_http_not_allowed(self) -> None:
        assert not validate_webhook_url("http://maker.ifttt.com/trigger/event")

    def test_empty_string(self) -> None:
        assert not validate_webhook_url("")

    def test_none(self) -> None:
        assert not validate_webhook_url(None)  # type: ignore

    def test_whitespace_only(self) -> None:
        assert not validate_webhook_url("   ")

    def test_invalid_url(self) -> None:
        assert not validate_webhook_url("not-a-url")


class TestExtractIftttWebhooks:
    def test_extract_all_keys(self) -> None:
        settings = {
            "ifttt_webhooks": {
                "winter": "https://maker.ifttt.com/winter",
                "summer": "https://maker.ifttt.com/summer",
                "fan": "https://maker.ifttt.com/fan",
                "off": "https://maker.ifttt.com/off",
            }
        }
        result = extract_ifttt_webhooks(settings)
        assert result == {
            "winter": "https://maker.ifttt.com/winter",
            "summer": "https://maker.ifttt.com/summer",
            "fan": "https://maker.ifttt.com/fan",
            "off": "https://maker.ifttt.com/off",
        }

    def test_missing_webhooks_key(self) -> None:
        settings: dict = {}
        result = extract_ifttt_webhooks(settings)
        assert result == {"winter": "", "summer": "", "fan": "", "off": ""}

    def test_partial_webhooks(self) -> None:
        settings = {"ifttt_webhooks": {"winter": "https://maker.ifttt.com/winter"}}
        result = extract_ifttt_webhooks(settings)
        assert result["winter"] == "https://maker.ifttt.com/winter"
        assert result["summer"] == ""
        assert result["fan"] == ""
        assert result["off"] == ""

    def test_strips_whitespace(self) -> None:
        settings = {"ifttt_webhooks": {"winter": "  https://maker.ifttt.com/winter  "}}
        result = extract_ifttt_webhooks(settings)
        assert result["winter"] == "https://maker.ifttt.com/winter"


class TestIFTTTWebhookClient:
    @patch("switchbot_dashboard.ifttt.requests.post")
    def test_trigger_webhook_success(self, mock_post: Mock) -> None:
        url = "https://maker.ifttt.com/trigger/test_event/with/key/12345"
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        client = IFTTTWebhookClient()
        client.trigger_webhook(url)

        mock_post.assert_called_once()
        assert mock_post.call_args[0][0] == url

    @patch("switchbot_dashboard.ifttt.requests.post")
    def test_trigger_webhook_with_payload(self, mock_post: Mock) -> None:
        url = "https://maker.ifttt.com/trigger/test_event/with/key/12345"
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        client = IFTTTWebhookClient()
        client.trigger_webhook(url, event_data={"value1": "test", "value2": 42})

        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args[1]
        assert call_kwargs["json"] == {"value1": "test", "value2": 42}
        assert call_kwargs["headers"]["Content-Type"] == "application/json"

    @patch("switchbot_dashboard.ifttt.requests.post")
    def test_trigger_webhook_http_error(self, mock_post: Mock) -> None:
        url = "https://maker.ifttt.com/trigger/test_event/with/key/12345"
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("400 Client Error")
        mock_post.return_value = mock_response

        client = IFTTTWebhookClient()
        with pytest.raises(IFTTTWebhookError, match="Webhook request failed"):
            client.trigger_webhook(url)

    def test_trigger_webhook_invalid_url(self) -> None:
        client = IFTTTWebhookClient()
        with pytest.raises(IFTTTWebhookError, match="Invalid webhook URL"):
            client.trigger_webhook("http://insecure.com")

    def test_trigger_webhook_empty_url(self) -> None:
        client = IFTTTWebhookClient()
        with pytest.raises(IFTTTWebhookError, match="Invalid webhook URL"):
            client.trigger_webhook("")

    @patch("switchbot_dashboard.ifttt.requests.post")
    def test_trigger_webhook_timeout(self, mock_post: Mock) -> None:
        url = "https://maker.ifttt.com/trigger/test_event/with/key/12345"
        mock_post.side_effect = requests.exceptions.Timeout("Connection timeout")

        client = IFTTTWebhookClient(timeout=0.1)
        with pytest.raises(IFTTTWebhookError, match="Webhook request timeout"):
            client.trigger_webhook(url)
