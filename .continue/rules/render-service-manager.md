---
name: render-service-manager
description: Gestion complète des services Render.com pour SwitchBot Dashboard (déploiement, monitoring, environnements, bases de données). Utiliser pour créer/gérer web services, cron jobs, static sites, PostgreSQL et monitoring via render-switchbot-mcp.
globs:
  - "**/render*.py"
  - "**/deploy*.py"
  - "**/*.env"
alwaysApply: false
---

# Render Service Manager - Règle Continue

Expert en gestion des services Render.com pour SwitchBot Dashboard via le serveur MCP render-switchbot-mcp.

## Quand utiliser cette règle

**Déclencheurs**: `render`, `deploy`, `cron`, `web service`, `static site`, `key value`, `environment variables`, `monitoring`, `metrics`, `logs`

**Cas d'usage**:
- **Déploiement initial** : Création de web services, static sites, cron jobs pour SwitchBot
- **Gestion environnements** : Configuration variables d'environnement, secrets, clés API
- **Monitoring production** : Métriques performance, logs, diagnostics santé
- **Maintenance base de données** : Gestion instances PostgreSQL Render, requêtes, monitoring
- **Scaling et optimisation** : Ajustement ressources, analyse métriques, optimisation coûts

## Workflow obligatoire

### 1. Préparation workspace
```bash
# Vérifier workspace et services existants
select_workspace(workspace_id="switchbot-prod")
list_services()
list_postgres_instances()
```

### 2. Configuration base de données
```python
# Créer instance PostgreSQL
create_postgres(
    name="switchbot-db",
    plan="starter",
    region="oregon"
)

# Variables d'environnement essentielles
update_environment_variables(
    service_id="web-service-id",
    env_vars={
        "DATABASE_URL": "postgres://...",
        "STORE_BACKEND": "postgres",
        "POSTGRES_SSL_MODE": "require"
    }
)
```

### 3. Déploiement web service
```python
# Service Flask principal
create_web_service(
    name="switchbot-dashboard",
    env="python",
    build_command="pip install -r requirements.txt",
    start_command="gunicorn -w 1 -b 0.0.0.0:$PORT app:app",
    source_dir="./",
    branch="main",
    auto_deploy=True
)
```

### 4. Monitoring et alerting
```python
# Health checks automatisés
create_cron_job(
    name="health-monitor",
    schedule="*/5 * * * *",
    command="python health_check.py",
    env="python"
)

# Métriques de base
get_metrics(
    resource_id="web-service-id",
    metrics=["cpu", "memory", "requests"],
    resolution="1h"
)
```

## Variables d'environnement SwitchBot

**Obligatoire** pour tous les déploiements :
```python
update_environment_variables(
    service_id="web-service-id",
    env_vars={
        "SWITCHBOT_API_BASE": "https://api.switch-bot.com",
        "SWITCHBOT_TOKEN": "${SWITCHBOT_TOKEN}",
        "AUTOMATION_ENABLED": "true",
        "SCHEDULER_ENABLED": "true",
        "API_QUOTA_LIMIT": "1000",
        "LOG_LEVEL": "INFO"
    }
)
```

## Monitoring production

### Logs et diagnostics
```python
# Recherche erreurs
list_logs(
    service_id="web-service-id",
    filter='level:"ERROR"',
    limit=100
)

# Métriques performance
get_metrics(
    resource_id="web-service-id",
    metrics=["cpu_percent", "memory_percent", "http_requests_count"]
)
```

### Base de données
```python
# Métriques PostgreSQL
get_metrics(
    resource_id="postgres-id",
    metrics=["active_connections", "buffer_hit_ratio"]
)
```

## Gestion déploiements

### Zero-downtime deployment
1. **Créer nouvelle version** : Branch feature ou staging
2. **Tester staging** : Variables d'environnement séparées
3. **Migration base** : Via `render-postgres-integration` si nécessaire
4. **Redirection traffic** : Mise à jour DNS/load balancer
5. **Monitoring rollout** : Alertes automatiques si anomalies
6. **Rollback automatique** : En cas d'erreurs détectées

### Rollback procedure
```python
# Revenir à version précédente
update_web_service(
    id="web-service-id",
    branch="main",  # branch stable
    auto_deploy=True
)
```

## Bonnes pratiques sécurité

- **Secrets** : Jamais en dur dans le code, toujours via variables d'environnement
- **SSL/TLS** : Obligatoire pour toutes les connexions PostgreSQL
- **Firewall** : Configuration réseau appropriée
- **Access** : Principe least privilege pour toutes les ressources

## Optimisation coûts

- **Plans adaptés** : starter/standard/pro selon charge
- **Monitoring usage** : Métriques CPU/Memory continues
- **Cron jobs** : Fréquence optimisée (pas trop fréquente)
- **Nettoyage** : Logs et données anciennes régulièrement

## Intégration avec autres règles

- **postgres-store-maintenance** : Pour migrations base de données
- **render-postgres-integration** : Pour orchestration cross-environnements
- **scheduler-ops** : Pour configuration APScheduler en production
- **automation-diagnostics** : Pour monitoring automation en production
