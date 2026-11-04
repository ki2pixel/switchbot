---
name: aircon-cascade
description: Runbook pour orchestrer la cascade Scènes SwitchBot → Commandes directes (fallback, idempotence OFF, tests).
---

# Cascade Scènes / Commandes directes

Déclencher ce skill pour configurer, diagnostiquer ou étendre les actions de climatisation.

## 1. Contexte
- Modules : `switchbot_dashboard/automation.py` (`_trigger_aircon_action`, `_trigger_scene`, `_send_aircon_setall`, `_send_aircon_off`) et `switchbot_dashboard/aircon.py` (`extract_aircon_scenes`).
- Actions manuelles : `switchbot_dashboard/routes.py` (`_execute_aircon_action` → `_handle_direct_action`).
- Config : `settings["aircon_scenes"]` (`winter`, `summer`, `fan`, `off`) et `settings["aircon_device_id"]`.
- UI : page `/reglages` (`templates/settings.html`) pour les scènes, page `/actions` (`templates/actions.html`) pour les déclenchements manuels.

## 2. Workflow
1. **Validation entrées** :
   - IDs de scènes : non vides, alphanumériques + tirets, max 50 caractères (`routes.py:_update_scene_ids`).
   - `aircon_device_id` : requis pour le fallback en commande directe.
   - Validation des formulaires via `_safe_*` / alias `_as_*`.
2. **Implémentation** :
   - Priorité Scène SwitchBot : `_trigger_scene` → `SwitchBotClient.run_scene(scene_id)`.
   - Fallback commande directe : `_send_aircon_setall` (ON) ou `_send_aircon_off` (OFF).
   - Idempotence OFF : ne pas renvoyer d'ordre si `assumed_aircon_power == "off"`, sauf `force_direct`.
3. **Observation** :
   - Logs `[automation]` indiquent le chemin emprunté (scène, fallback direct, cooldown).
   - `state_store` : `last_action`, `last_error`, `assumed_aircon_power`, `assumed_aircon_mode`, `pending_off_repeat`.

## 3. Tests
- Unitaires : `tests/test_automation_service.py`, `tests/test_aircon_presets.py`, `tests/test_adaptive_cooldown.py`.
- Routes/UI : `tests/test_dashboard_routes.py`, `tests/test_frontend_loaders.py`.
- Manuels : déclencher chaque action (winter/summer/fan/off) via `/actions`.
- Edge cases : scène absente ou invalide, `aircon_device_id` vide, cooldown actif, capteur indisponible.
- Référence : `references/scene_test_matrix.md` pour les scénarios scènes/commandes.

## 4. Bonnes pratiques
- Toujours conserver le fallback direct : une scène en échec ne doit pas bloquer l'action.
- Respecter l'idempotence OFF et les cooldowns (`command_cooldown_seconds`, `action_on/off_cooldown_seconds`).
- Documenter tout ajout dans `docs/architecture/automation-engine.md` + Memory Bank.
- Ne jamais exposer les identifiants de scènes ou de devices dans les logs publics.
