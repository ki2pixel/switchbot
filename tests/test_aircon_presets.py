from __future__ import annotations

from switchbot_dashboard.routes import AIRCON_SCENE_KEYS, _extract_aircon_scenes


def test_extract_aircon_scenes_returns_empty_strings_when_missing() -> None:
    scenes = _extract_aircon_scenes({})

    assert scenes == {key: "" for key in AIRCON_SCENE_KEYS}


def test_extract_aircon_scenes_trims_and_validates_values() -> None:
    settings = {
        "aircon_scenes": {
            "winter": "  abc-123  ",
            "summer": 42,
            "fan": "fan-scene",
            "off": "  999-off ",
        }
    }

    scenes = _extract_aircon_scenes(settings)

    assert scenes["winter"] == "abc-123"
    assert scenes["summer"] == ""
    assert scenes["fan"] == "fan-scene"
    assert scenes["off"] == "999-off"
