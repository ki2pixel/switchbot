---
name: postgres-ops-manager
description: Gestion complète des opérations PostgreSQL via switchbot-postgres MCP (analyse santé, optimisation indexes, requêtes sécurisées, schémas). Utiliser pour maintenance base de données, diagnostics performance, et exécution SQL sécurisée.
---

# PostgreSQL Operations Manager

Expert en gestion et optimisation des bases de données PostgreSQL pour SwitchBot Dashboard via le serveur MCP switchbot-postgres.

## Quand utiliser ce skill

- **Analyse santé base de données** : Diagnostics complets, indexes, vacuum, connexions
- **Optimisation performance** : Analyse requêtes lentes, recommandations indexes, plans d'exécution
- **Maintenance schémas** : Exploration structures, détails objets, modifications sécurisées
- **Exécution SQL sécurisée** : Requêtes read-only avec validation et monitoring
- **Troubleshooting production** : Investigation problèmes performance, blocages, corruptions

## Workflow analyse santé

### 1. Diagnostic complet
```python
# Analyse santé globale
health_report = analyze_db_health(checks="all")

# Focus sur problèmes critiques
index_health = analyze_db_health(checks="index")
vacuum_health = analyze_db_health(checks="vacuum")
connection_health = analyze_db_health(checks="connection")
```

### 2. Requêtes problématiques
```python
# Identifier requêtes lentes
slow_queries = get_top_queries(
    limit=10,
    sort_by="total_time"
)

# Analyser plan d'exécution
query_plan = explain_query("""
    SELECT * FROM history_entries
    WHERE created_at > NOW() - INTERVAL '24 hours'
    ORDER BY created_at DESC
""")
```

### 3. Optimisation indexes
```python
# Analyse workload complète
index_recommendations = analyze_workload_indexes()

# Analyse requête spécifique
query_indexes = analyze_query_indexes(queries=[
    "SELECT * FROM automation_state WHERE device_id = $1",
    "SELECT COUNT(*) FROM history_entries WHERE timestamp > $1"
])
```

## Exploration base de données

### Structure schémas
```python
# Lister tous les schémas
schemas = list_schemas()

# Explorer objets d'un schéma
objects = list_objects(schema="public")
objects = list_objects(schema="switchbot", object_type="table")
```

### Détails objets
```python
# Informations détaillées table
table_details = get_object_details(
    schema="public",
    name="automation_state",
    object_type="table"
)

# Structure indexes
index_details = get_object_details(
    schema="public",
    name="idx_automation_device_timestamp",
    object_type="index"
)
```

## Exécution SQL sécurisée

### Requêtes read-only
```sql
-- Analyse données automation
execute_sql("""
    SELECT device_id, COUNT(*) as actions_count,
           MIN(created_at) as first_action,
           MAX(created_at) as last_action
    FROM history_entries
    WHERE action_type IN ('turn_on', 'turn_off')
    GROUP BY device_id
    ORDER BY actions_count DESC
    LIMIT 20
""")

-- Statistiques quota API
execute_sql("""
    SELECT DATE_TRUNC('hour', timestamp) as hour,
           COUNT(*) as requests_count,
           SUM(CASE WHEN response_status >= 400 THEN 1 ELSE 0 END) as errors_count
    FROM api_quota_log
    WHERE timestamp > NOW() - INTERVAL '24 hours'
    GROUP BY DATE_TRUNC('hour', timestamp)
    ORDER BY hour DESC
""")
```

### Validation avant exécution
```python
# Toujours analyser le plan avant exécution complexe
plan = explain_query("SELECT * FROM large_table WHERE complex_condition")
# Vérifier coût estimé < seuil acceptable

# Utiliser EXPLAIN ANALYZE pour requêtes de test
execute_sql("EXPLAIN ANALYZE SELECT * FROM history_entries LIMIT 1000")
```

## Optimisation performance

### Indexes stratégiques
```python
# Recommandations basées sur workload
workload_indexes = analyze_workload_indexes()

# Création indexes recommandés
execute_sql("""
    CREATE INDEX CONCURRENTLY idx_history_device_timestamp
    ON history_entries (device_id, timestamp DESC)
    WHERE timestamp > NOW() - INTERVAL '30 days'
""")

# Indexes partiels pour queries fréquentes
execute_sql("""
    CREATE INDEX idx_automation_active
    ON automation_state (device_id)
    WHERE is_active = true
""")
```

### Maintenance routine
```sql
-- Analyse statistiques
execute_sql("ANALYZE VERBOSE history_entries")

-- Reconstruction indexes fragmentés
execute_sql("REINDEX INDEX CONCURRENTLY idx_history_timestamp")

-- Vacuum pour récupérer espace
execute_sql("VACUUM (VERBOSE, ANALYZE) automation_state")
```

## Monitoring et alerting

### Métriques clés
```python
# Tables les plus actives
execute_sql("""
    SELECT schemaname, tablename,
           seq_scan, idx_scan,
           n_tup_ins, n_tup_upd, n_tup_del,
           n_live_tup, n_dead_tup
    FROM pg_stat_user_tables
    ORDER BY n_tup_ins + n_tup_upd + n_tup_del DESC
    LIMIT 10
""")

# Indexes inefficaces
execute_sql("""
    SELECT schemaname, tablename, indexname,
           idx_scan, idx_tup_read, idx_tup_fetch
    FROM pg_stat_user_indexes
    WHERE idx_scan = 0
    ORDER BY pg_relation_size(indexrelid) DESC
""")
```

### Alertes santé
- **Connexions** : > 80% utilisation max
- **Cache buffer** : < 95% hit ratio
- **Vacuum** : âge transaction > 1M
- **Indexes** : scan ratio < 10%
- **Réplication** : lag > 1 minute

## Sécurité et bonnes pratiques

### Règles exécution SQL
- **Read-only uniquement** : Pas de INSERT/UPDATE/DELETE sauf maintenance planifiée
- **Limites résultats** : Toujours LIMIT sur queries exploratoires
- **Timeout** : Configurer statement_timeout pour éviter blocages
- **Transactions** : Utiliser BEGIN/COMMIT pour modifications groupées

### Audit et logging
```sql
-- Audit modifications sensibles
execute_sql("""
    SELECT * FROM pg_stat_activity
    WHERE state = 'active'
    AND query LIKE '%UPDATE%'
    AND query NOT LIKE '%pg_stat%'
""")
```

### Backup et recovery
- **Sauvegardes automatisées** : Via cron job Render
- **Point-in-time recovery** : Testé régulièrement
- **Validation backups** : Restauration test mensuelle

## Intégration SwitchBot

### Tables spécifiques
```sql
-- État automation
execute_sql("""
    SELECT device_id, device_type, power_state,
           last_seen, firmware_version
    FROM device_registry
    WHERE last_seen > NOW() - INTERVAL '1 hour'
""")

-- Historique actions
execute_sql("""
    SELECT DATE_TRUNC('day', timestamp) as day,
           action_type, COUNT(*) as count
    FROM history_entries
    WHERE timestamp > NOW() - INTERVAL '7 days'
    GROUP BY DATE_TRUNC('day', timestamp), action_type
    ORDER BY day DESC, count DESC
""")

-- Quota API
execute_sql("""
    SELECT endpoint, SUM(requests_count) as total_requests,
           SUM(errors_count) as total_errors,
           ROUND(AVG(response_time), 2) as avg_response_time
    FROM api_quota_log
    WHERE timestamp > NOW() - INTERVAL '24 hours'
    GROUP BY endpoint
    ORDER BY total_requests DESC
""")
```

### Optimisations métier
- **Indexes composites** : (device_id, timestamp) pour queries temporelles
- **Partitionnement** : Tables history par mois/semaine
- **Archivage** : Données anciennes vers tables archive
- **Caching** : Résultats fréquents en Redis/Memory

## Scripts et références

- **Scripts** : `scripts/postgres_health_check.py` - Diagnostic automatisé complet
- **Références** : `references/postgres_optimization.md` - Guide optimisation avancé
- **Assets** : `assets/postgres_queries.sql` - Bibliothèque requêtes communes

Voir la documentation complète dans les sous-répertoires scripts/, references/, assets/.
