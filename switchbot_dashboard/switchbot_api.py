from __future__ import annotations

import base64
import hashlib
import hmac
import ipaddress
import time
import threading
import uuid
import logging
from dataclasses import dataclass
from typing import Any, Protocol
from urllib.parse import urlsplit

import requests
from requests import Response


logger = logging.getLogger(__name__)


_FORBIDDEN_IP_FLAGS = (
    "is_private",
    "is_loopback",
    "is_link_local",
    "is_reserved",
    "is_unspecified",
    "is_multicast",
)


def _validate_url_parts(parsed: Any, cleaned: str) -> str:
    """Reject non-HTTPS URLs and embedded credentials/fragments/queries."""
    if parsed.scheme.lower() != "https" or not parsed.hostname:
        raise SwitchBotApiError(
            f"[api] Invalid SwitchBot base_url (HTTPS required): {cleaned!r}"
        )
    if parsed.username is not None or parsed.password is not None:
        raise SwitchBotApiError("[api] Credentials in base_url are forbidden")
    if parsed.fragment:
        raise SwitchBotApiError("[api] Fragment is forbidden in base_url")
    if parsed.query:
        raise SwitchBotApiError("[api] Query string is forbidden in base_url")
    return parsed.hostname.lower()


def _validate_public_hostname(hostname: str) -> None:
    """Reject local hostnames and private/loopback/reserved IP addresses."""
    if (
        hostname in {"localhost", "localhost.localdomain"}
        or hostname.endswith(".localhost")
        or hostname.endswith(".local")
        or hostname.endswith(".internal")
    ):
        raise SwitchBotApiError(
            f"[api] Local hostname forbidden in base_url: {hostname}"
        )

    try:
        ip_obj = ipaddress.ip_address(hostname)
    except ValueError:
        return

    if any(getattr(ip_obj, flag) for flag in _FORBIDDEN_IP_FLAGS):
        raise SwitchBotApiError(
            f"[api] Private or loopback IP forbidden in base_url: {hostname}"
        )


def _validate_https_base_url(raw_url: str) -> str:
    """Validate an operator-provided SwitchBot base URL.

    ``base_url`` is trusted configuration, but a typo must never leak the
    ``Authorization``/``sign`` headers to a local or private endpoint.
    """
    cleaned = raw_url.strip()
    parsed = urlsplit(cleaned)
    hostname = _validate_url_parts(parsed, cleaned)
    _validate_public_hostname(hostname)
    return cleaned.rstrip("/")


@dataclass(frozen=True)
class SwitchBotResponse:
    status_code: int
    message: str
    body: Any


class SwitchBotApiError(RuntimeError):
    pass


class QuotaTracker(Protocol):
    def record_call(self, *, increment: int = 1) -> None:
        ...

    def record_from_headers(self, *, limit: int | None, remaining: int | None) -> bool:
        ...


class SwitchBotClient:
    def __init__(
        self,
        token: str,
        secret: str,
        base_url: str | None = None,
        retry_attempts: int = 2,
        retry_delay_seconds: int = 10,
        quota_tracker: QuotaTracker | None = None,
    ) -> None:
        self._token = token.strip()
        self._secret = secret.strip()
        self._base_url = _validate_https_base_url(
            base_url or "https://api.switch-bot.com"
        )
        self._retry_attempts = max(int(retry_attempts), 1)
        self._retry_delay_seconds = max(int(retry_delay_seconds), 0)
        self._last_quota: dict[str, int] | None = None
        self._quota_tracker = quota_tracker
        # Caches for API calls (P-01)
        self._status_cache: dict[str, tuple[float, Any]] = {}
        self._devices_cache: tuple[float, Any] | None = None
        self._cache_lock = threading.Lock()
        # One requests.Session per worker thread: sessions are not thread-safe.
        self._session_local = threading.local()

    def _get_session(self) -> requests.Session:
        session = getattr(self._session_local, "session", None)
        if session is None:
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter(
                pool_connections=4,
                pool_maxsize=10,
                max_retries=0,
            )
            session.mount("https://", adapter)
            session.mount("http://", adapter)
            self._session_local.session = session
        return session

    def _build_headers(self) -> dict[str, str]:
        if not self._token or not self._secret:
            raise SwitchBotApiError(
                "[api] Missing SwitchBot credentials. Set SWITCHBOT_TOKEN and SWITCHBOT_SECRET."
            )

        t = int(round(time.time() * 1000))
        nonce = str(uuid.uuid4())
        string_to_sign = f"{self._token}{t}{nonce}".encode("utf-8")
        secret_bytes = self._secret.encode("utf-8")
        sign = base64.b64encode(
            hmac.new(secret_bytes, msg=string_to_sign, digestmod=hashlib.sha256).digest()
        ).decode("utf-8")

        return {
            "Authorization": self._token,
            "Content-Type": "application/json; charset=utf-8",
            "t": str(t),
            "sign": sign,
            "nonce": nonce,
        }

    def _decode_response_json(self, response: Response) -> Any:
        """Decode the response body, raising on HTTP or JSON errors."""
        try:
            data = response.json()
        except ValueError as exc:
            if response.status_code >= 400:
                raise SwitchBotApiError(
                    f"SwitchBot HTTP {response.status_code}: invalid JSON error payload."
                ) from exc
            raise SwitchBotApiError(
                f"Invalid JSON response from SwitchBot ({response.status_code})."
            ) from exc

        if response.status_code >= 400:
            raise SwitchBotApiError(
                f"SwitchBot HTTP {response.status_code}: {data!r}"
            )
        return data

    def _record_implicit_quota_call(self, tracker_updated: bool) -> None:
        """Record one call when no quota headers were available."""
        if self._quota_tracker and not tracker_updated:
            try:
                self._quota_tracker.record_call()
            except Exception as exc:
                logger.warning("[api] Failed to record quota call (%s)", exc)

    def _process_response(self, response: Response, path: str, tracker_updated: bool) -> tuple[bool, Any]:
        """Returns (retry_needed, data)."""
        data = self._decode_response_json(response)

        if not isinstance(data, dict) or "statusCode" not in data:
            raise SwitchBotApiError(f"Unexpected SwitchBot response: {data!r}")

        status_code = data.get("statusCode")
        logger.debug(
            "[api] SwitchBot API payload parsed: statusCode=%s message=%s path=%s",
            status_code,
            data.get("message"),
            path,
        )
        if status_code == 100:
            self._record_implicit_quota_call(tracker_updated)
            return False, data

        if status_code == 190:
            return True, None

        raise SwitchBotApiError(f"SwitchBot API error: {data!r}")

    def _send_once(
        self,
        method: str,
        url: str,
        json_body: dict[str, Any] | None,
        timeout: float,
    ) -> Response:
        """Perform a single HTTP request with fresh HMAC headers."""
        return self._get_session().request(
            method=method,
            url=url,
            headers=self._build_headers(),
            json=json_body,
            timeout=timeout,
        )

    def _transport_retry_delay(self, attempt_index: int) -> float:
        """Compute exponential backoff with jitter for transport errors."""
        import random as _rand

        delay = min(self._retry_delay_seconds * (2 ** attempt_index), 5)
        return delay + _rand.uniform(0, 0.5)

    def _retry_transport_error(self, attempt_index: int) -> bool:
        """Sleep and return True when a transport error can be retried."""
        if (
            attempt_index >= (self._retry_attempts - 1)
            or self._retry_delay_seconds <= 0
        ):
            return False
        time.sleep(self._transport_retry_delay(attempt_index))
        return True

    def _evaluate_http_response(
        self,
        response: Response,
        *,
        method: str,
        path: str,
        attempt_index: int,
        is_get: bool,
    ) -> tuple[str, Any]:
        """Return ("data", payload), ("retry", delay) or ("exhausted", None)."""
        # Capture quota metadata before any retry branch: a 429 followed by
        # a transport timeout must still persist remaining=0.
        tracker_updated = self._capture_quota_metadata(response)

        logger.debug(
            "[api] SwitchBot %s %s -> HTTP %s",
            method,
            path,
            response.status_code,
        )

        retryable_http = response.status_code == 429 or 500 <= response.status_code <= 599
        can_retry = is_get and attempt_index < (self._retry_attempts - 1)

        if retryable_http and can_retry:
            return "retry", self._parse_retry_after(response, attempt_index)

        retry_needed, data = self._process_response(
            response, path, tracker_updated
        )
        if retry_needed and can_retry:
            return "retry", self._parse_retry_after(response, attempt_index)
        if not retry_needed:
            return "data", data
        return "exhausted", None

    def _request(self, method: str, path: str, json_body: dict[str, Any] | None = None, *, timeout: float = 15) -> Any:
        url = f"{self._base_url}{path}"
        is_get = method.upper() == "GET"

        for attempt_index in range(self._retry_attempts):
            try:
                response = self._send_once(method, url, json_body, timeout)
            except requests.RequestException as exc:
                # REL-04: Transport errors are always retryable
                if self._retry_transport_error(attempt_index):
                    continue
                raise SwitchBotApiError(
                    f"[api] SwitchBot request failed: {exc}"
                ) from exc

            outcome, value = self._evaluate_http_response(
                response,
                method=method,
                path=path,
                attempt_index=attempt_index,
                is_get=is_get,
            )
            if outcome == "data":
                return value
            if outcome == "retry":
                time.sleep(value)
                continue

        raise SwitchBotApiError("[api] SwitchBot request failed")

    def _parse_retry_after(self, response: Response, attempt_index: int) -> float:
        """Parse Retry-After header with exponential backoff and jitter (REL-04)."""
        import random as _rand

        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                delay = min(float(retry_after), 5.0)
            except (ValueError, TypeError):
                delay = min(self._retry_delay_seconds * (2 ** attempt_index), 5.0)
        else:
            delay = min(self._retry_delay_seconds * (2 ** attempt_index), 5.0)
        delay += _rand.uniform(0, 0.5)  # jitter
        return delay

    def get_devices(self, *, force: bool = False) -> Any:
        now = time.monotonic()
        if not force:
            with self._cache_lock:
                if self._devices_cache is not None:
                    cached_time, cached_val = self._devices_cache
                    if now - cached_time < 60.0:
                        return cached_val

        devices = self._request("GET", "/v1.1/devices")
        with self._cache_lock:
            self._devices_cache = (now, devices)
        return devices

    def get_scenes(self) -> Any:
        return self._request("GET", "/v1.1/scenes")

    def get_device_status(self, device_id: str) -> Any:
        device_id = device_id.strip()
        if not device_id:
            raise SwitchBotApiError("Missing device_id")

        # 60s cache to avoid N+1 API abuse on /devices page (P-01)
        now = time.monotonic()
        with self._cache_lock:
            if device_id in self._status_cache:
                cached_time, cached_val = self._status_cache[device_id]
                if now - cached_time < 60.0:
                    return cached_val

        status = self._request("GET", f"/v1.1/devices/{device_id}/status")
        with self._cache_lock:
            self._status_cache[device_id] = (now, status)
        return status

    def send_command(
        self,
        device_id: str,
        command: str,
        parameter: str = "default",
        command_type: str = "command",
    ) -> Any:
        device_id = device_id.strip()
        if not device_id:
            raise SwitchBotApiError("Missing device_id")

        body = {
            "command": command,
            "parameter": parameter,
            "commandType": command_type,
        }
        return self._request("POST", f"/v1.1/devices/{device_id}/commands", json_body=body)

    def run_scene(self, scene_id: str) -> Any:
        scene_id = scene_id.strip()
        if not scene_id:
            raise SwitchBotApiError("Missing scene_id")

        return self._request("POST", f"/v1.1/scenes/{scene_id}/execute", json_body={})

    def _extract_quota_values(
        self, response: Response
    ) -> tuple[int | None, int | None]:
        """Extract quota limit/remaining from the supported header aliases."""
        header_map = {key.lower(): value for key, value in response.headers.items()}
        limit_raw = (
            header_map.get("x-ratelimit-limit")
            or header_map.get("x-rate-limit-limit")
            or header_map.get("ratelimit-limit")
        )
        remaining_raw = (
            header_map.get("x-ratelimit-remaining")
            or header_map.get("x-rate-limit-remaining")
            or header_map.get("ratelimit-remaining")
        )

        limit = self._safe_int(limit_raw)
        remaining = self._safe_int(remaining_raw)

        if getattr(response, "status_code", None) == 429:
            remaining = 0
        return limit, remaining

    def _record_quota_without_headers(self) -> bool:
        """Record a call when the response exposes no quota headers."""
        tracker_updated = False
        if self._quota_tracker:
            try:
                self._quota_tracker.record_call()
                tracker_updated = True
            except Exception as exc:
                logger.warning("[api] Failed to record quota call (%s)", exc)
        logger.debug("[api] SwitchBot quota headers absent on latest response.")
        return tracker_updated

    def _record_quota_headers(
        self, limit: int | None, remaining: int | None
    ) -> bool:
        """Persist a quota snapshot and forward it to the tracker."""
        self._last_quota = {}
        if limit is not None:
            self._last_quota["limit"] = limit
        if remaining is not None:
            self._last_quota["remaining"] = remaining

        logger.info(
            "[api] SwitchBot quota snapshot captured: remaining=%s limit=%s",
            remaining if remaining is not None else "unknown",
            limit if limit is not None else "unknown",
        )

        if not self._quota_tracker:
            return False

        try:
            return self._quota_tracker.record_from_headers(
                limit=limit, remaining=remaining
            )
        except Exception as exc:
            logger.warning("[api] Failed to persist quota headers (%s)", exc)
            return False

    def _capture_quota_metadata(self, response: Response) -> bool:
        limit, remaining = self._extract_quota_values(response)
        if limit is None and remaining is None:
            return self._record_quota_without_headers()
        return self._record_quota_headers(limit, remaining)

    @staticmethod
    def _safe_int(value: str | None) -> int | None:
        if value is None:
            return None
        try:
            return int(value)
        except (TypeError, ValueError):
            return None

    def get_last_quota_snapshot(self) -> dict[str, int] | None:
        if self._last_quota is None:
            return None
        return dict(self._last_quota)
