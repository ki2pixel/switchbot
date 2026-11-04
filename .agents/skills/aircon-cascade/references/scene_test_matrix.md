# Matrice de test cascade Scènes → Commandes directes

## Cas Scènes
| Cas | Entrée | Résultat attendu |
| --- | --- | --- |
| Scène valide | `aircon_scenes[winter]` configuré | `run_scene` appelé, `state.last_action = scene(...)` |
| Scène absente | Aucune scène configurée | Fallback commande directe si `aircon_device_id` présent |
| Scène invalide | ID inconnu ou refusé par l'API | `SwitchBotApiError`, log `[automation] Scene execution failed`, fallback direct |

## Cas Commandes directes
1. Vérifier `aircon_device_id` présent.
2. Vérifier le bon couple `setAll` (ON) / `turnOff` (OFF).
3. Cooldown respecté (`assumed_aircon_power`, `last_action_at`).

## Cas Idempotence OFF
1. `assumed_aircon_power == "off"` → aucun nouvel ordre OFF.
2. `pending_off_repeat` actif → respecter `remaining`, `interval_seconds`, `next_run_at`.
3. Action ON → `_clear_off_repeat_task()`.

## Scripts utiles
```bash
source /mnt/venv_ext4/venv_switchbot/bin/activate
python -m pytest tests/test_automation_service.py tests/test_aircon_presets.py tests/test_adaptive_cooldown.py
```

## Observabilité
- Inspecter `state_store` (`pending_off_repeat`, `last_error`, `assumed_aircon_power`).
- Vérifier les flashs UI sur `/actions` (succès/erreur).
- Logs `[automation]` : chemin scène, fallback direct, cooldown, capteur indisponible.
