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
- Consulter `/healthz` pour confirmer `last_tick` et `last_scheduler_tick`.
- Script diagnostic : `.agents/skills/scheduler-ops/scripts/scheduler_snapshot.py` → `python .agents/skills/scheduler-ops/scripts/scheduler_snapshot.py > debug/scheduler.json`.
- Checklist détaillée : `references/scheduler_checklist.md` (reschedule, pause, restart, incidents).

## 2. Opérations courantes

1. **Reschedule** : appeler `scheduler.reschedule()` **sans argument** après modification des réglages ; le scheduler relit automatiquement les paramètres depuis `settings_store`.
2. **Auto-reschedule** : après chaque tick, le scheduler recalcule automatiquement l'intervalle via `_maybe_reschedule_after_tick()` si le polling adaptatif est activé.
3. **Pause** : définir `SCHEDULER_ENABLED=false` avant restart pour maintenance; logguer l'action.
4. **Restart manuel** : si `is_running()` est faux alors que Gunicorn tourne, inspecter `current_app.logger` pour les garde-fous (mode dev, worker multiples).

## 3. Vérifications après action

- Log `[scheduler] Job scheduled with interval=X seconds` ou `[scheduler] Adaptive polling reschedule: A -> B seconds (mode=...)` présent.
- `state_store` mis à jour (`last_tick` au format ISO-8601).
- Tests ciblés : `tests/test_scheduler_service.py` (ou sections correspondantes dans `test_automation_service.py`).

## 4. Bonnes pratiques

- Jamais de `BackgroundScheduler` multiple : `WEB_CONCURRENCY=1`, `gunicorn.conf.py` (1 worker, 4 threads).
- Sur incident Postgres : `ResilientStore` alerte au 3e échec (`STORE_FAILURE_THRESHOLD`) et bascule vers JSON uniquement si autorisé (hors production ou `STORE_RUNTIME_FALLBACK=true`) ; sinon les routes répondent `503`.
- Toute modification durable doit être notée dans `docs/architecture/scheduler.md` + Memory Bank decisionLog.
- **Polling adaptatif** : désactiver (`adaptive_polling_enabled=false`) uniquement pour debugging ou tests spécifiques.
