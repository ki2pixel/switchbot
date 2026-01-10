from __future__ import annotations

import copy

from switchbot_dashboard.routes import _extract_aircon_presets, DEFAULT_AIRCON_PRESETS


def test_extract_aircon_presets_returns_defaults_when_missing() -> None:
    settings: dict[str, object] = {}

    presets = _extract_aircon_presets(settings)

    assert presets == DEFAULT_AIRCON_PRESETS


def test_extract_aircon_presets_uses_custom_values() -> None:
    settings = {
        "aircon_presets": {
            "winter": {
                "target_temp": 26.0,
                "ac_mode": 5,
                "fan_speed": 4,
            },
            "summer": {
                "target_temp": 19.0,
                "ac_mode": 2,
                "fan_speed": 2,
            },
        }
    }

    presets = _extract_aircon_presets(settings)

    assert presets["winter"] == {"target_temp": 26.0, "ac_mode": 5, "fan_speed": 4}
    assert presets["summer"] == {"target_temp": 19.0, "ac_mode": 2, "fan_speed": 2}


def test_extract_aircon_presets_clamps_out_of_range_values() -> None:
    settings = {
        "aircon_presets": {
            "winter": {
                "target_temp": 4.0,  # below min 10°C
                "ac_mode": 9,  # above max 5
                "fan_speed": -1,  # below min 1
            },
            "summer": {
                "target_temp": 55.0,  # above max 40°C
                "ac_mode": 0,  # below min 1
                "fan_speed": 99,  # above max 4
            },
        }
    }

    presets = _extract_aircon_presets(settings)

    assert presets["winter"] == {"target_temp": 10.0, "ac_mode": 5, "fan_speed": 1}
    assert presets["summer"] == {"target_temp": 40.0, "ac_mode": 1, "fan_speed": 4}


def test_extract_aircon_presets_does_not_mutate_defaults() -> None:
    settings = {
        "aircon_presets": {
            "winter": {
                "target_temp": 23.0,
                "ac_mode": 4,
                "fan_speed": 2,
            }
        }
    }

    before = copy.deepcopy(DEFAULT_AIRCON_PRESETS)
    _extract_aircon_presets(settings)

    assert DEFAULT_AIRCON_PRESETS == before
