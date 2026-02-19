---
name: render-service-manager
description: Gestion complète des services Render.com pour SwitchBot Dashboard (déploiement, monitoring, environnements, bases de données). Utiliser pour créer/gérer web services, cron jobs, static sites, PostgreSQL et monitoring via render-switchbot-mcp.
---

# Render Service Manager

Expert en gestion des services Render.com pour SwitchBot Dashboard via le serveur MCP render-switchbot-mcp.

## Quand utiliser ce skill

- **Déploiement initial** : Création de web services, static sites, cron jobs pour SwitchBot
- **Gestion environnements** : Configuration variables d'environnement, secrets, clés API
- **Monitoring production** : Métriques performance, logs, diagnostics santé
- **Maintenance base de données** : Gestion instances PostgreSQL Render, requêtes, monitoring
- **Scaling et optimisation** : Ajustement ressources, analyse métriques, optimisation coûts

## Workflow déploiement initial

### 1. Préparation workspace
```bash
# Sélectionner le workspace approprié
select_workspace(workspace_id="switchbot-prod")

# Vérifier services existants
list_services()
list_postgres_instances()
```

### 2. Création base de données PostgreSQL
```python
# Créer instance PostgreSQL
create_postgres(
    name="switchbot-db",
    plan="starter",  # ou "standard", "pro"
    region="oregon"  # ou "frankfurt", "singapore"
)

# Configurer variables d'environnement
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
# Créer web service Flask
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

### 4. Configuration monitoring et alerting
```python
# Créer cron job pour health checks
create_cron_job(
    name="health-monitor",
    schedule="*/5 * * * *",  # toutes les 5 minutes
    command="python health_check.py",
    env="python"
)

# Configurer métriques monitoring
get_metrics(
    resource_id="web-service-id",
    start_time="2024-01-01T00:00:00Z",
    end_time="2024-01-02T00:00:00Z",
    metrics=["cpu", "memory", "requests"]
)
```

## Gestion environnements

### Variables d'environnement
```python
# Mise à jour sécurisée des secrets
update_environment_variables(
    service_id="web-service-id",
    env_vars={
        "SWITCHBOT_TOKEN": "secret-token",
        "API_QUOTA_LIMIT": "1000",
        "LOG_LEVEL": "INFO"
    },
    replace=False  # merge avec existantes
)
```

### Key-Value stores
```python
# Créer store pour cache/configuration
create_key_value(
    name="switchbot-cache",
    plan="starter"
)

# Récupérer configuration
kv_store = get_key_value(id="kv-store-id")
```

## Monitoring et diagnostics

### Analyse logs
```python
# Recherche logs erreurs
list_logs(
    service_id="web-service-id",
    start_time="2024-01-01T00:00:00Z",
    end_time="2024-01-02T00:00:00Z",
    filter='level:"ERROR"'
)

# Labels de logs disponibles
list_log_label_values(
    service_id="web-service-id",
    label="method"
)
```

### Métriques performance
```python
# CPU/Memory/Requests
get_metrics(
    resource_id="web-service-id",
    metrics=["cpu_percent", "memory_percent", "http_requests_count"],
    resolution="1h"
)

# Base de données
get_metrics(
    resource_id="postgres-id",
    metrics=["active_connections", "buffer_hit_ratio"]
)
```

## Maintenance base de données

### Requêtes et analyse
```sql
-- Via query_render_postgres
SELECT schemaname, tablename, n_tup_ins, n_tup_upd, n_tup_del
FROM pg_stat_user_tables
ORDER BY n_tup_ins + n_tup_upd + n_tup_del DESC
LIMIT 10;
```

### Gestion instances
```python
# Lister toutes les instances
postgres_instances = list_postgres_instances()

# Détails instance spécifique
instance_details = get_postgres(id="postgres-id")

# Mise à jour instance
update_postgres(
    id="postgres-id",
    plan="standard"  # upgrade
)
```

## Gestion des déploiements

### Suivi déploiements
```python
# Status déploiement récent
deploy_status = get_deploy(deploy_id="deploy-id")

# Historique déploiements
deploys = list_deploys(
    service_id="web-service-id",
    limit=10
)
```

### Rollback et mises à jour
```python
# Mise à jour service existant
update_web_service(
    id="web-service-id",
    branch="feature-branch",
    auto_deploy=False  # déploiement manuel pour test
)

# Mise à jour cron job
update_cron_job(
    id="cron-job-id",
    schedule="0 */6 * * *",  # toutes les 6h
    command="python backup.py"
)
```

## Bonnes pratiques

### Sécurité
- Jamais stocker credentials en dur dans le code
- Utiliser variables d'environnement pour tous les secrets
- Activer SSL/TLS pour toutes les connexions PostgreSQL
- Configurer firewall et accès réseau appropriés

### Performance
- Monitorer métriques CPU/Memory en continu
- Optimiser plans de requête PostgreSQL régulièrement
- Utiliser connection pooling pour bases de données
- Configurer auto-scaling selon charge

### Monitoring
- Alertes sur erreurs 5xx et timeouts
- Surveillance utilisation quota API SwitchBot
- Logs centralisés pour debugging production
- Health checks automatisés toutes les 5 minutes

### Gestion coûts
- Choisir plans appropriés (starter/standard/pro)
- Monitorer utilisation ressources
- Optimiser fréquence cron jobs
- Nettoyer logs et données anciennes régulièrement

## Intégration SwitchBot

### Variables spécifiques
```python
update_environment_variables(
    service_id="web-service-id",
    env_vars={
        "SWITCHBOT_API_BASE": "https://api.switch-bot.com",
        "SWITCHBOT_TOKEN": "${SWITCHBOT_TOKEN}",
        "AUTOMATION_ENABLED": "true",
        "SCHEDULER_ENABLED": "true"
    }
)
```

### Déploiement zero-downtime
1. Créer nouvelle version du service
2. Tester sur staging environment
3. Rediriger traffic progressivement
4. Monitorer métriques pendant rollout
5. Rollback automatique si anomalies détectées

## Scripts et références

- **Scripts** : `scripts/deploy_switchbot.py` - Déploiement automatisé complet
- **Références** : `references/render_monitoring.md` - Guide monitoring avancé
- **Assets** : `assets/dockerfile` - Configuration Docker optimisée

Voir la documentation complète dans les sous-répertoires scripts/, references/, assets/.
