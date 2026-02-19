---
name: scheduler-ops
description: Runbook SchedulerService (start/stop/reschedule) avec APScheduler, détection Gunicorn vs flask run et healthchecks. Intégration cron jobs Render pour production.
globs:
  - "**/scheduler_service.py"
  - "**/scheduler.py"
alwaysApply: false
---

# Pilotage SchedulerService & Cron Jobs Render

Déclencher ce skill pour manipuler APScheduler en toute sécurité et gérer les tâches planifiées en production via Render cron jobs.

## 1. État actuel
- Vérifier `SCHEDULER_ENABLED` et `SERVER_SOFTWARE`.
- Depuis un shell Flask :
  ```python
  scheduler = current_app.extensions["scheduler_service"]
  scheduler.is_running()
  ```
- Consulter `/healthz` pour confirmer `last_tick_at`.
- Script diagnostic : `.windsurf/skills/scheduler-ops/scripts/scheduler_snapshot.py` → `python .windsurf/skills/scheduler-ops/scripts/scheduler_snapshot.py > debug/scheduler.json`.
- **NOUVEAU** : Utiliser `render-service-manager` skill pour gérer les cron jobs Render en production.
- Checklist détaillée : `.windsurf/skills/scheduler-ops/references/scheduler_checklist.md` (reschedule, pause, restart, incidents).

## 2. Opérations courantes APScheduler
1. **Reschedule** : appeler `scheduler.reschedule(poll_interval_seconds)` après modification des réglages; gérer `StoreError` éventuels.
2. **Pause** : définir `SCHEDULER_ENABLED=false` avant restart pour maintenance; logguer l'action.
3. **Restart manuel** : si `is_running()` est faux alors que Gunicorn tourne, inspecter `current_app.logger` pour les garde-fous (mode dev, worker multiples).

## 3. Intégration Cron Jobs Render (Production)
**Priorité** : Pour production, utiliser les cron jobs Render via render-switchbot-mcp au lieu d'APScheduler local.

### Création Cron Jobs Production
```python
# Cron job automation SwitchBot (remplace APScheduler)
from render_switchbot_mcp import create_cron_job

cron_job = create_cron_job(
    name="switchbot-automation",
    schedule="*/15 * * * *",  # toutes les 15 minutes
    command="python -c 'from switchbot_dashboard.automation import run_automation; run_automation()'",
    env="python"
)
```

### Migration APScheduler → Render Cron
```python
def migrate_to_render_cron():
    # Désactiver APScheduler local
    update_environment_variables(
        service_id="web-service",
        env_vars={"SCHEDULER_ENABLED": "false"}
    )

    # Créer cron jobs Render équivalents
    create_cron_job(
        name="automation-main",
        schedule="*/15 * * * *",
        command="python automation/main.py"
    )

    create_cron_job(
        name="health-check",
        schedule="*/5 * * * *",
        command="python health_check.py"
    )

    # Supprimer anciennes tâches APScheduler
    scheduler = current_app.extensions["scheduler_service"]
    scheduler.remove_all_jobs()
```

### Gestion Cron Jobs Render
```python
# Mise à jour fréquence automation
update_cron_job(
    id="automation-cron-id",
    schedule="*/10 * * * *"  # changement fréquence
)

# Monitoring exécutions
logs = list_logs(
    service_id="cron-job-service",
    start_time="-1h",
    filter='job:"automation-main"'
)
```

### Synchronisation Environnements
```python
# Staging vs Production cron jobs
STAGING_CRON = {
    "automation": "*/30 * * * *",  # moins fréquent en staging
    "backup": "0 */4 * * *"       # backups toutes les 4h
}

PROD_CRON = {
    "automation": "*/15 * * * *",  # fréquence normale prod
    "backup": "0 */2 * * *"       # backups toutes les 2h
}

def sync_cron_jobs(environment):
    config = STAGING_CRON if environment == "staging" else PROD_CRON

    # Synchroniser tous les cron jobs
    for job_name, schedule in config.items():
        update_cron_job(
            id=f"{job_name}-cron-id",
            schedule=schedule
        )
```

## 4. Vérifications après action
- Log `[scheduler] Rescheduled to Xs` présent.
- `state.json` mis à jour (`last_tick_at`, `last_tick_status`).
- **NOUVEAU** : Vérifier exécutions cron jobs Render dans les logs de service.
- Tests ciblés : `tests/test_scheduler_service.py` (ou sections correspondantes dans `test_automation_service.py`).

## 5. Bonnes pratiques
- Jamais de `BackgroundScheduler` multiple : `WEB_CONCURRENCY=1`, `gunicorn.conf.py` (1 worker, 2 threads).
- **NOUVEAU** : Cron jobs Render sont plus fiables que APScheduler local pour production (pas de redémarrage app qui tue les tâches).
- Après une erreur Postgres, attendre 3 échecs consécutifs avant fallback JsonStore; consigner dans Memory Bank.
- **NOUVEAU** : Monitorer échecs cron jobs via métriques Render et alertes automatiques.
- Toute modification durable doit être notée dans `docs/architecture/scheduler.md` + Memory Bank decisionLog. 
