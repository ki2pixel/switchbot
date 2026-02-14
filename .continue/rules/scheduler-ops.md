---
description: Runbook SchedulerService (start/stop/reschedule) avec APScheduler, détection Gunicorn vs flask run et healthchecks.
globs: 
  - "**/scheduler_service.py"
  - "**/scheduler.py"
alwaysApply: false
---

# Pilotage SchedulerService

Déclencher ce skill pour manipuler APScheduler en toute sécurité.

## 1. État actuel
- Vérifier `SCHEDULER_ENABLED` et `SERVER_SOFTWARE`.
- Depuis un shell Flask :
  ```python
  scheduler = current_app.extensions["scheduler_service"]
  scheduler.is_running()
  ```
- Consulter `/healthz` pour confirmer `last_tick_at`.
- Script diagnostic : `.windsurf/skills/scheduler-ops/scripts/scheduler_snapshot.py` → `python .windsurf/skills/scheduler-ops/scripts/scheduler_snapshot.py > debug/scheduler.json`.
- Checklist détaillée : `.windsurf/skills/scheduler-ops/references/scheduler_checklist.md` (reschedule, pause, restart, incidents).

## 2. Opérations courantes
1. **Reschedule** : appeler `scheduler.reschedule(poll_interval_seconds)` après modification des réglages; gérer `StoreError` éventuels.
2. **Pause** : définir `SCHEDULER_ENABLED=false` avant restart pour maintenance; logguer l'action.
3. **Restart manuel** : si `is_running()` est faux alors que Gunicorn tourne, inspecter `current_app.logger` pour les garde-fous (mode dev, worker multiples).

## 3. Vérifications après action
- Log `[scheduler] Rescheduled to Xs` présent.
- `state.json` mis à jour (`last_tick_at`, `last_tick_status`).
- Tests ciblés : `tests/test_scheduler_service.py` (ou sections correspondantes dans `test_automation_service.py`).

## 4. Bonnes pratiques
- Jamais de `BackgroundScheduler` multiple : `WEB_CONCURRENCY=1`, `gunicorn.conf.py` (1 worker, 2 threads).
- Après une erreur Postgres, attendre 3 échecs consécutifs avant fallback JsonStore; consigner dans Memory Bank.
- Toute modification durable doit être notée dans `docs/architecture/scheduler.md` + Memory Bank decisionLog. 
