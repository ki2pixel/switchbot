# Checklist Opérations SchedulerService

## Préparation
- Variable `SCHEDULER_ENABLED` définie ? (true/false)
- Commande d’inspection :
  ```bash
  python .windsurf/skills/scheduler-ops/scripts/scheduler_snapshot.py > debug/scheduler.json
  ```
- Endpoint `/healthz` accessible.

## Scénarios
| Action | Étapes | Validation |
| --- | --- | --- |
| Reschedule après modification intervalle | POST /settings → `scheduler_service.reschedule()` | Log `[scheduler] Rescheduled...`, `state.last_tick_at` mis à jour |
| Pause scheduler | `SCHEDULER_ENABLED=false`, restart app | `/healthz` doit refléter `scheduler_enabled=false` |
| Restart manuel | `scheduler.stop()` → `scheduler.start()` | `scheduler.is_running()` True, tick immédiat |

## Points de contrôle
1. `poll_interval_seconds` ≥ 15 s.
2. Aucun `BackgroundScheduler` multiple (`WEB_CONCURRENCY=1`).
3. Logs : `[scheduler] Job scheduled with interval=X`.
4. `state.json` : champs `last_tick_status`, `last_tick_error` (si présent).

## Incident Response
- Si Postgres indisponible → reschedule repoussé. Vérifier `StoreError` dans logs.
- Si scheduler non démarré sous Gunicorn → vérifier `SERVER_SOFTWARE` et `FLASK_DEBUG`.

## Documentation
- Reporter toute intervention dans `docs/scheduler.md` + Memory Bank (decisionLog/progress).
