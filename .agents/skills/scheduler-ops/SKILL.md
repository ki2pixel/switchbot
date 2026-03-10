---
name: scheduler-ops
description: Runbook SchedulerService (start/stop/reschedule) avec APScheduler, polling adaptatif (idle/warmup/in-window), détection Gunicorn vs flask run et healthchecks.
---

# Pilotage SchedulerService

Déclencher ce skill pour manipuler APScheduler en toute sécurité.

## 1. État actuel

- Vérifier `SCHEDULER_ENABLED` et `SERVER_SOFTWARE`.
- **Polling adaptatif** : modes `idle` (hors fenêtre), `warmup` (approche fenêtre), `in_window` (actif).
- **Paramètres de polling** :
  - `poll_interval_seconds` : intervalle de base (défaut: 120s)
  - `adaptive_polling_enabled` : active le polling adaptatif (défaut: true)
  - `idle_poll_interval_seconds` : intervalle en mode idle (défaut: 600s)
  - `poll_warmup_minutes` : minutes avant fenêtre pour passer en warmup (défaut: 15)
- Depuis un shell Flask :
 ```python
 scheduler = current_app.extensions["scheduler_service"]
 scheduler.is_running()
 ```
- Consulter `/healthz` pour confirmer `last_tick_at`.
- Script diagnostic : `scripts/scheduler_snapshot.py` → `python scripts/scheduler_snapshot.py > debug/scheduler.json`.
- Checklist détaillée : `references/scheduler_checklist.md` (reschedule, pause, restart, incidents).

## 2. Opérations courantes

1. **Reschedule** : appeler `scheduler.reschedule()` **sans argument** après modification des réglages ; le scheduler relit automatiquement les paramètres depuis `settings_store`.
2. **Auto-reschedule** : après chaque tick, le scheduler recalcule automatiquement l'intervalle via `_maybe_reschedule_after_tick()` si le polling adaptatif est activé.
3. **Pause** : définir `SCHEDULER_ENABLED=false` avant restart pour maintenance; logguer l'action.
4. **Restart manuel** : si `is_running()` est faux alors que Gunicorn tourne, inspecter `current_app.logger` pour les garde-fous (mode dev, worker multiples).

## 3. Vérifications après action

- Log `[scheduler] Rescheduled to Xs` ou `[scheduler] Job scheduled with interval=X seconds` présent.
- `state.json` mis à jour (`last_tick_at`, `last_tick_status`).
- Tests ciblés : `tests/test_scheduler_service.py` (ou sections correspondantes dans `test_automation_service.py`).

## 4. Bonnes pratiques

- Jamais de `BackgroundScheduler` multiple : `WEB_CONCURRENCY=1`, `gunicorn.conf.py` (1 worker, 2 threads).
- Après une erreur Postgres, attendre 3 échecs consécutifs avant fallback JsonStore; consigner dans Memory Bank.
- Toute modification durable doit être notée dans `docs/architecture/scheduler.md` + Memory Bank decisionLog.
- **Polling adaptatif** : désactiver (`adaptive_polling_enabled=false`) uniquement pour debugging ou tests spécifiques.
