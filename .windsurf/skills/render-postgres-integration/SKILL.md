---
name: render-postgres-integration
description: Orchestration entre Render.com et PostgreSQL pour SwitchBot Dashboard (migrations cross-environnements, backups coordonnés, monitoring intégré, synchronisation données).
---

# Render-PostgreSQL Integration

Orchestrateur expert pour l'intégration Render.com + PostgreSQL dans SwitchBot Dashboard, gérant migrations, backups, monitoring croisé et synchronisation environnements.

## Quand utiliser ce skill

- **Migrations environnements** : Synchronisation base de données entre staging/production
- **Stratégie backup** : Coordination backups PostgreSQL avec déploiements Render
- **Monitoring intégré** : Corrélations métriques Render + PostgreSQL
- **Déploiement zero-downtime** : Coordination migrations base pendant déploiement
- **Récupération disaster** : Restoration backups avec reconfiguration services Render

## Workflow migration environnements

### 1. Préparation migration
```python
# Vérifier workspace cible
select_workspace(workspace_id="switchbot-prod")

# Snapshot base source
source_backup = query_render_postgres("""
    SELECT pg_start_backup('migration_backup', true);
    -- Copie fichiers via pg_basebackup ou outil équivalent
    SELECT pg_stop_backup();
""")

# Créer instance cible si nécessaire
target_db = create_postgres(
    name="switchbot-prod-db",
    plan="standard",
    region="oregon"
)
```

### 2. Migration données
```bash
# Export schéma et données
pg_dump --schema-only --no-owner --clean source_db > schema.sql
pg_dump --data-only --no-owner --disable-triggers source_db > data.sql

# Import dans cible
psql target_db < schema.sql
psql target_db < data.sql
```

### 3. Validation et switch
```python
# Vérifier intégrité données
source_count = query_render_postgres("SELECT COUNT(*) FROM history_entries")
target_count = query_render_postgres("SELECT COUNT(*) FROM history_entries", db_id="target")

assert source_count == target_count

# Mise à jour variables environnement
update_environment_variables(
    service_id="web-service-prod",
    env_vars={"DATABASE_URL": target_db.connection_string}
)

# Redémarrage service
update_web_service(
    id="web-service-prod",
    auto_deploy=True
)
```

## Stratégie backup coordonné

### Backup automatisé
```python
# Cron job backup quotidien
create_cron_job(
    name="postgres-backup-daily",
    schedule="0 2 * * *",  # 2h du matin UTC
    command="""
    pg_dump --format=custom --compress=9 --no-owner \\
            --file=/backups/switchbot-$(date +%Y%m%d).dump \\
            $DATABASE_URL
    """,
    env="python"
)

# Cron job nettoyage anciens backups
create_cron_job(
    name="cleanup-old-backups",
    schedule="0 3 * * 0",  # dimanche 3h
    command="find /backups -name '*.dump' -mtime +30 -delete"
)
```

### Backup avant déploiement
```python
def deploy_with_backup():
    # Backup automatique avant déploiement
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"pre_deploy_{timestamp}"

    # Créer backup
    execute_sql(f"""
        SELECT pg_start_backup('{backup_name}', true);
        -- Backup logique pour sécurité
        CREATE TABLE {backup_name}_snapshot AS
        SELECT * FROM automation_state;
        SELECT pg_stop_backup();
    """)

    # Déployer nouvelle version
    update_web_service(id="web-service", branch="new-feature")

    # Vérifier santé post-déploiement
    health_check = get_metrics(
        resource_id="web-service",
        metrics=["http_5xx_count"],
        start_time="-5m"
    )

    if health_check.error_rate > 0.01:  # >1% erreurs
        # Rollback automatique
        update_web_service(id="web-service", branch="main")
        return False

    return True
```

## Monitoring intégré

### Corrélations métriques
```python
# Métriques Render + PostgreSQL synchronisées
def monitor_integrated_health():
    # Métriques service web
    web_metrics = get_metrics(
        resource_id="web-service",
        metrics=["cpu_percent", "memory_percent", "http_requests_count"],
        start_time="-1h"
    )

    # Métriques base de données
    db_metrics = analyze_db_health(checks="connection,buffer")

    # Requêtes lentes corrélées
    slow_queries = get_top_queries(limit=5)

    # Alerte si corrélation négative détectée
    if web_metrics.cpu_percent > 80 and db_metrics.buffer_hit_ratio < 0.95:
        alert("High CPU + Low Buffer Hit Ratio - Possible DB Contention")

    return {
        "web": web_metrics,
        "db": db_metrics,
        "queries": slow_queries
    }
```

### Dashboard monitoring unifié
```python
# Collecte métriques toutes les 5 minutes
create_cron_job(
    name="integrated-monitoring",
    schedule="*/5 * * * *",
    command="""
    python -c "
    from render_service_manager import monitor_integrated_health
    from postgres_ops_manager import analyze_db_health

    health = monitor_integrated_health()
    db_health = analyze_db_health()

    # Stocker métriques pour dashboard
    store_metrics(health | db_health)
    "
    """
)
```

## Déploiement zero-downtime

### Stratégie blue-green
```python
def blue_green_deploy(new_version_branch):
    # Créer nouveau service (green)
    green_service = create_web_service(
        name="switchbot-green",
        branch=new_version_branch,
        env_vars={"DATABASE_URL": current_db_url}
    )

    # Attendre santé green
    while not is_service_healthy(green_service.id):
        time.sleep(30)

    # Test canari (10% traffic)
    switch_traffic(service_a=current_service, service_b=green_service, ratio=0.1)
    monitor_errors(duration="10m")

    # Si OK, switch 100%
    if no_critical_errors():
        switch_traffic(service_a=current_service, service_b=green_service, ratio=1.0)

        # Nettoyer ancien service après validation
        time.sleep(3600)  # 1h observation
        if still_healthy():
            delete_service(current_service.id)
            rename_service(green_service.id, "switchbot-main")

    else:
        # Rollback immédiat
        switch_traffic(service_a=current_service, service_b=green_service, ratio=0.0)
        delete_service(green_service.id)
```

### Gestion migrations base
```python
def migrate_with_zero_downtime(migration_script):
    # Créer réplica pour migration
    replica_db = create_postgres(
        name="migration-replica",
        plan="standard"
    )

    # Setup réplication
    setup_replication(source_db=current_db, replica_db=replica_db)

    # Migration sur réplica
    execute_sql(migration_script, db_id=replica_db.id)

    # Validation migration
    validate_migration(current_db, replica_db)

    # Switch atomique
    switch_database_url(replica_db.connection_string)

    # Promotion réplica
    promote_replica(replica_db)

    # Cleanup ancien
    time.sleep(86400)  # 24h validation
    delete_postgres(current_db.id)
```

## Récupération disaster

### Plan recovery automatisé
```python
def disaster_recovery(backup_timestamp=None):
    # Créer nouvelle instance PostgreSQL
    recovery_db = create_postgres(
        name=f"recovery-{datetime.now().strftime('%Y%m%d')}",
        plan="standard"
    )

    # Restaurer depuis backup
    if backup_timestamp:
        restore_from_backup(backup_timestamp, recovery_db)
    else:
        # Backup le plus récent
        latest_backup = find_latest_backup()
        restore_from_backup(latest_backup, recovery_db)

    # Recréer service web avec nouvelle DB
    recovery_service = create_web_service(
        name="switchbot-recovery",
        env_vars={"DATABASE_URL": recovery_db.connection_string}
    )

    # Validation recovery
    if validate_recovery(recovery_service):
        # Switch traffic vers recovery
        switch_traffic_to_recovery(recovery_service)
        return True

    return False
```

### Test recovery régulier
```python
# Cron job test recovery mensuel
create_cron_job(
    name="monthly-recovery-test",
    schedule="0 2 1 * *",  # 1er du mois, 2h
    command="""
    python -c "
    from render_postgres_integration import disaster_recovery
    # Test sur petit dataset
    test_db = create_postgres(name='test-recovery', plan='starter')
    # ... logique test ...
    delete_postgres(test_db.id)
    "
    """
)
```

## Synchronisation environnements

### Staging → Production
```python
def promote_staging_to_prod():
    # Vérifier staging healthy
    staging_health = get_service(service_id="staging-service")
    staging_db_health = analyze_db_health(db_id="staging-db")

    if not (staging_health.status == "healthy" and staging_db_health.overall == "good"):
        raise Exception("Staging not ready for promotion")

    # Migration base staging → prod
    migrate_database(
        source_db="staging-db",
        target_db="prod-db",
        strategy="online"  # zero-downtime
    )

    # Mise à jour service prod
    update_web_service(
        id="prod-service",
        env_vars={"DATABASE_URL": "prod-db-url"}
    )

    # Validation post-promotion
    monitor_post_promotion(duration="1h")
```

### Configuration multi-environnement
```python
ENV_CONFIGS = {
    "dev": {
        "db_plan": "starter",
        "service_plan": "starter",
        "auto_deploy": False
    },
    "staging": {
        "db_plan": "standard",
        "service_plan": "starter",
        "auto_deploy": True
    },
    "prod": {
        "db_plan": "pro",
        "service_plan": "standard",
        "auto_deploy": True
    }
}

def create_environment(env_name):
    config = ENV_CONFIGS[env_name]

    # Créer base de données
    db = create_postgres(
        name=f"switchbot-{env_name}-db",
        plan=config["db_plan"]
    )

    # Créer service web
    service = create_web_service(
        name=f"switchbot-{env_name}",
        plan=config["service_plan"],
        auto_deploy=config["auto_deploy"],
        env_vars={"DATABASE_URL": db.connection_string}
    )

    return {"db": db, "service": service}
```

## Bonnes pratiques

### Sécurité
- **Encryption** : Toutes connexions SSL/TLS
- **Accès réseau** : Firewall restrictif, VPN pour admin
- **Credentials** : Rotation automatique, pas de stockage local
- **Audit** : Logging complet migrations et accès

### Performance
- **Connection pooling** : pgbouncer pour haute disponibilité
- **Read replicas** : Répartition charge lecture/écriture
- **Caching** : Redis pour données fréquentes
- **Compression** : Backups compressés, WAL compression

### Observabilité
- **Métriques unifiées** : Render + PostgreSQL dans même dashboard
- **Alerting intelligent** : Seuils dynamiques selon charge
- **Tracing distribué** : Correlation requêtes web ↔ DB
- **Logging structuré** : JSON logs pour analyse

## Scripts et références

- **Scripts** : `scripts/migrate_environments.py` - Migration automatisée staging→prod
- **Références** : `references/zero_downtime_deploy.md` - Guide déploiement sans interruption
- **Assets** : `assets/backup_strategy.sql` - Templates backup PostgreSQL

Voir la documentation complète dans les sous-répertoires scripts/, references/, assets/.
