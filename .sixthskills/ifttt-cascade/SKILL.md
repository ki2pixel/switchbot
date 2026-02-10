---
name: ifttt-cascade
description: Runbook pour orchestrer la cascade IFTTT → Scènes → Commandes directes (validation HTTPS, fallback, tests).
---

# Cascade IFTTT / Scènes / Commandes

Déclencher ce skill pour configurer ou étendre les actions climatisation.

## 1. Contexte
- Modules : `switchbot_dashboard/ifttt.py`, `automation.py` (méthodes `_trigger_aircon_action`, `_execute_aircon_action`).
- Config : `settings["ifttt_webhooks"]`, `settings["aircon_scenes"]`, `settings["aircon_device_id"]`.
- UI : section webhooks & scènes dans `templates/index.html` et `settings.html`.

## 2. Workflow
1. **Validation entrées** :
   - URLs : `validate_webhook_url` (HTTPS uniquement).
   - IDs scènes : non vides, alignés sur l’app SwitchBot.
2. **Implémentation** :
   - Priorité webhooks (client `IFTTTWebhookClient`).
   - Fallback Scenes → `SwitchBotClient.execute_scene(scene_id)`.
   - Dernier recours `setAll`/`turnOff` avec `aircon_device_id`.
3. **Observation** :
   - Logs `[automation]` indiquent le chemin emprunté.
   - `state.json` : `last_action`, `last_error`, `assumed_aircon_power`.

## 3. Tests
- Unitaires : `tests/test_ifttt.py`, sections cascade dans `tests/test_automation_service.py`.
- Manuels : déclencher chaque action (winter/summer/fan/off) via UI ou `flask shell`.
- Edge cases : webhook 500, scène inexistante, absence `aircon_device_id`.
- Référence tests : `references/webhook_test_matrix.md` pour scénarios webhook/scènes/commandes.

## 4. Bonnes pratiques
- Les webhooks doivent répondre < 4 s ; configurer timeouts dans `IFTTTWebhookClient`.
- Documenter tout ajout dans `docs/guides/ifttt-setup.md` + Memory Bank.
- Ne jamais exposer les URLs IFTTT dans les logs ou commits.
