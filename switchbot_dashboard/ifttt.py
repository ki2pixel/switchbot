from __future__ import annotations

import logging
from typing import Any
from urllib.parse import urlparse

import requests


logger = logging.getLogger(__name__)


class IFTTTWebhookError(Exception):
    pass


def validate_webhook_url(url: str) -> bool:
    if not url or not isinstance(url, str):
        return False
    url = url.strip()
    if not url:
        return False
    try:
        parsed = urlparse(url)
        return parsed.scheme == "https" and bool(parsed.netloc)
    except Exception:
        return False


def extract_ifttt_webhooks(settings: dict[str, Any]) -> dict[str, str]:
    """Extract and normalize IFTTT webhook URLs from settings.

    Args:
        settings: Configuration dictionary containing 'ifttt_webhooks' mapping

    Returns:
        Dictionary with normalized webhook URLs for keys: 'winter', 'summer', 'fan', 'off'
        Empty strings are used for missing or invalid entries

    Example:
        >>> settings = {"ifttt_webhooks": {"winter": "https://maker.ifttt.com/trigger/..."}}
        >>> extract_ifttt_webhooks(settings)
        {"winter": "https://maker.ifttt.com/trigger/...", "summer": "", "fan": "", "off": ""}
    """
    raw_webhooks = settings.get("ifttt_webhooks", {})
    if not isinstance(raw_webhooks, dict):
        raw_webhooks = {}

    sanitized: dict[str, str] = {}
    for key in ("winter", "summer", "fan", "off"):
        value = raw_webhooks.get(key, "")
        sanitized[key] = str(value).strip() if isinstance(value, str) else ""
    return sanitized


class IFTTTWebhookClient:
    def __init__(
        self,
        *,
        timeout: float = 10.0,
        logger_instance: logging.Logger | None = None,
    ) -> None:
        self._timeout = timeout
        self._logger = logger_instance or logger

    def _log(self, level: int, message: str, **details: Any) -> None:
        payload = f"[ifttt] {message}"
        if details:
            formatted_details = " | ".join(f"{k}={v!r}" for k, v in sorted(details.items()))
            payload = f"{payload} | {formatted_details}"
        self._logger.log(level, payload)

    def trigger_webhook(
        self,
        webhook_url: str,
        *,
        event_data: dict[str, Any] | None = None,
    ) -> None:
        webhook_url = webhook_url.strip()
        if not validate_webhook_url(webhook_url):
            raise IFTTTWebhookError(f"Invalid webhook URL: {webhook_url}")

        payload = event_data or {}

        self._log(
            logging.DEBUG,
            "Triggering IFTTT webhook",
            url=webhook_url[:50] + "..." if len(webhook_url) > 50 else webhook_url,
            payload_keys=list(payload.keys()) if payload else [],
        )

        try:
            response = requests.post(
                webhook_url,
                json=payload,
                timeout=self._timeout,
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()

            self._log(
                logging.INFO,
                "IFTTT webhook triggered successfully",
                status_code=response.status_code,
            )

        except requests.exceptions.Timeout:
            self._log(logging.ERROR, "IFTTT webhook timeout", url=webhook_url[:50])
            raise IFTTTWebhookError(f"Webhook request timeout after {self._timeout}s")
        except requests.exceptions.RequestException as exc:
            self._log(
                logging.ERROR,
                "IFTTT webhook request failed",
                error=str(exc),
                url=webhook_url[:50],
            )
            raise IFTTTWebhookError(f"Webhook request failed: {exc}")
