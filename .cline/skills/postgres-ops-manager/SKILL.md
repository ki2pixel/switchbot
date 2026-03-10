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
 SELECT * FROM state_history
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
 "SELECT * FROM state_history WHERE created_at > $1",
 "SELECT COUNT(*) FROM history_entries WHERE timestamp > $1"
])
```

## Intégration SwitchBot

### Tables spécifiques du projet

- **`state_history`** : Historique des états (temperature, humidity, assumed_aircon_power, timestamp)
- **`history_entries`** : Entrées d'historique (si utilisée)

```sql
-- État history récent
execute_sql("""
 SELECT timestamp, temperature, humidity, assumed_aircon_power
 FROM state_history
 WHERE timestamp > NOW() - INTERVAL '24 hours'
 ORDER BY timestamp DESC
 LIMIT 100
""")

-- Statistiques par état clim
execute_sql("""
 SELECT assumed_aircon_power, COUNT(*) as count,
 AVG(temperature) as avg_temp,
 AVG(humidity) as avg_humidity
 FROM state_history
 WHERE timestamp > NOW() - INTERVAL '7 days'
 GROUP BY assumed_aircon_power
 ORDER BY count DESC
""")
```

### Optimisations métier

- **Indexes composites** : (timestamp) pour queries temporelles sur state_history
- **Nettoyage automatique** : Historique nettoyé après 6h via HistoryService.cleanup_old_records()
- **Partitionnement** : Tables history par mois/semaine (optionnel pour grosses volumétries)

## Scripts et références

- **Scripts SQL** : `scripts/schema.sql`, `scripts/create_history_table.sql`
- **Documentation** : `docs/architecture/storage-layer.md`, `docs/core/configuration.md`
- **Tests** : `tests/test_postgres_store.py`, `tests/test_history_service.py`

## Alerting et monitoring

### Métriques clés
```sql
-- Taille tables
execute_sql("""
 SELECT relname as table_name,
 pg_size_pretty(pg_total_relation_size(relid)) as size
 FROM pg_catalog.pg_statio_user_tables
 ORDER BY pg_total_relation_size(relid) DESC
""")

-- Connexions actives
execute_sql("""
 SELECT count(*) as active_connections
 FROM pg_stat_activity
 WHERE state = 'active'
""")
```

## Bonnes pratiques

### Sécurité
- **Encryption** : Toutes connexions SSL/TLS (POSTGRES_SSL_MODE=require)
- **Credentials** : Rotation automatique via variables d'environnement
- **Audit** : Logging complet modifications sensibles

### Performance
- **Connection pooling** : psycopg_pool avec pool size configurable
- **Read-only** : Requêtes de diagnostic via MCP sont read-only
- **Timeouts** : Configurer timeouts appropriés pour requêtes longues
