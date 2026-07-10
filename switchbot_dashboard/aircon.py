from __future__ import annotations

from typing import Any, Dict

AIRCON_SCENE_KEYS: tuple[str, ...] = ("winter", "summer", "fan", "off")
AIRCON_SCENE_LABELS: dict[str, str] = {
    "winter": "Aircon ON – Hiver",
    "summer": "Aircon ON – Été",
    "fan": "Aircon ON – Mode neutre",
    "off": "Aircon OFF – Scène",
}


def extract_aircon_scenes(settings: dict[str, Any]) -> Dict[str, str]:
    """Return a sanitized mapping of configured aircon scenes."""

    raw_scenes = settings.get("aircon_scenes", {})
    if not isinstance(raw_scenes, dict):
        raw_scenes = {}

    sanitized: dict[str, str] = {}
    for key in AIRCON_SCENE_KEYS:
        value = raw_scenes.get(key, "")
        sanitized[key] = str(value).strip() if isinstance(value, str) else ""
    return sanitized
