---
description: Runbook de diagnostic pour AutomationService (fenêtres horaires, hysteresis, off-repeat, timezone) et état state_store.
globs: 
  - "**/*.{py,js,md}"
alwaysApply: true
---

# Diagnostic AutomationService

Utiliser ce skill pour comprendre pourquoi l'automatisation n'agit pas comme prévu.

## 1. Préparer le contexte
- Lire `switchbot_dashboard/automation.py` (sections run_once, _schedule_off_repeat_task).
- Inspecter `config/settings.json` et `config/state.json` via `current_app.extensions["settings_store"|"state_store"]`.

## 2. Checklist d'analyse
1. **Fenêtres horaires** : vérifier `timezone`, `automation_enabled`, `automation_windows`.
2. **Hysteresis/Seuils** : comparer `temperature`, `winter_min_temperature`, `summer_max_temperature`.
3. **Cool-down & assumed state** : champs `assumed_aircon_*`, `last_action_at`, `pending_off_repeat`.
4. **Off-repeat** : champs `off_repeat_count`, `off_repeat_interval_seconds`, état `pending_off_repeat`.
5. **Cascade actions** : logs `[automation]` indiquant webhook/scene/fallback.

## 3. Outils recommandés
- `.windsurf/skills/automation-diagnostics/scripts/state_snapshot.py` : capture `settings` + `state` en JSON offline.
  ```bash
  python .windsurf/skills/automation-diagnostics/scripts/state_snapshot.py > debug/state_snapshot.json
  ```
- `flask shell` :
  ```python
  store = current_app.extensions["state_store"]
  pprint(store.read())
  ```
- `tests/test_automation_service.py` : lancer les cas ciblés pour reproduire.

## 4. Points d'attention
- Le cache timezone d'`AutomationService` est basé sur la valeur du champ `timezone` (cf. `_cached_timezone_key`). Il n'existe pas de champ `timezone_version` : pour forcer une résolution, modifier temporairement la valeur `timezone` ou redémarrer l'application.
- Ne jamais éditer directement les fichiers JSON si PostgresStore actif; passer via le store.
- Documenter tout changement dans Memory Bank (decisionLog + progress).
