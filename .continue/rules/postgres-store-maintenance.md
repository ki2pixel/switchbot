---
name: postgres-store-maintenance
description: Guide pour maintenir PostgresStore (migrations, bascule JsonStore, validation pool psycopg) et opérations PostgreSQL avancées via switchbot-postgres MCP.
globs:
  - "**/config_store.py"
  - "**/models.py"
alwaysApply: false
---

# Maintenance PostgresStore & Opérations PostgreSQL

Utiliser ce skill pour toute opération sur le stockage Postgres (Neon) et son fallback, maintenant avec intégration prioritaire du serveur MCP switchbot-postgres pour les opérations avancées.

## 1. Préparation
- Lire `switchbot_dashboard/config_store.py` (classes PostgresStore, JsonStore).
- Vérifier `.env` : `STORE_BACKEND=postgres`, `POSTGRES_URL`, `POSTGRES_SSL_MODE`.
- Consulter `memory-bank/decisionLog.md` pour les derniers choix architecturaux.
- Script santé : `.windsurf/skills/postgres-store-maintenance/scripts/store_health.py` pour inspecter settings/state stores (`python .windsurf/skills/postgres-store-maintenance/scripts/store_health.py`).
- **NOUVEAU** : Utiliser `postgres-ops-manager` skill pour analyse santé avancée, optimisation indexes et requêtes sécurisées via switchbot-postgres MCP.
- Référence incidents : `.windsurf/skills/postgres-store-maintenance/references/postgres_incident.md` (fallback, migration, corruption).

## 2. Migrations / Scripts
1. Lancer `.windsurf/skills/postgres-store-maintenance/scripts/migrate_to_postgres.py --dry-run` avant toute modification.
2. Appliquer les scripts SQL (`.windsurf/skills/postgres-store-maintenance/scripts/create_history_table.sql`, etc.) via `psql` ou Neon console.
3. **NOUVEAU** : Pour migrations complexes, utiliser `execute_sql` du MCP switchbot-postgres pour exécution sécurisée et monitoring.
4. Après migration, tester lecture/écriture :
   ```python
   store = current_app.extensions["settings_store"]
   data = store.read()
   store.write(data)
   ```

## 3. Opérations PostgreSQL Avancées (via switchbot-postgres MCP)
**Priorité** : Utiliser les outils MCP pour toutes les opérations analytiques et de maintenance.

### Analyse Santé Base de Données
```python
# Diagnostic complet (remplace scripts manuels)
from switchbot_postgres import analyze_db_health

health = analyze_db_health(checks="all")  # index, connection, vacuum, sequence, replication, buffer
print(f"Status général: {health.overall_status}")
```

### Exploration Schémas et Objets
```python
# Lister schémas et explorer structure
schemas = list_schemas()
objects = list_objects(schema="public", object_type="table")

# Détails objets spécifiques
table_info = get_object_details(schema="public", name="history_entries", object_type="table")
```

### Optimisation Indexes
```python
# Analyse workload et recommandations
workload_analysis = analyze_workload_indexes()

# Analyse requêtes spécifiques
query_analysis = analyze_query_indexes(queries=[
    "SELECT * FROM automation_state WHERE device_id = ?",
    "SELECT COUNT(*) FROM history_entries WHERE timestamp > ?"
])
```

### Requêtes Sécurisées
```python
# Exécution SQL read-only avec analyse plan
plan = explain_query("SELECT * FROM history_entries WHERE created_at > NOW() - INTERVAL '24 hours'")
result = execute_sql("SELECT COUNT(*) FROM history_entries")  # Automatiquement read-only
```

### Monitoring Requêtes
```python
# Identifier requêtes lentes
slow_queries = get_top_queries(limit=10, sort_by="total_time")
for query in slow_queries:
    print(f"Query: {query.sql}, Time: {query.total_time}ms")
```

## 4. Gestion incidents
- Si `psycopg_pool` KO :
  1. Observer les logs `[store]`.
  2. Régénérer le pool via `store._pool.wait()` (dans shell).
  3. **NOUVEAU** : Utiliser `analyze_db_health(checks="connection")` pour diagnostiquer problèmes connexion.
  4. Si échec répété, basculer `STORE_BACKEND=filesystem` temporairement et documenter.
- Sur perte Neon : activer fallback JsonStore mais planifier la resynchronisation (script dédié pour reimporter settings/state).
- **NOUVEAU** : Pour corruption suspectée, utiliser `analyze_db_health(checks="constraint")` pour vérifier contraintes.

## 5. Validation & tests
- `tests/test_postgres_store.py`, `tests/test_config_store.py` pour s’assurer que les mocks passent.
- **NOUVEAU** : Tests intégration MCP dans `tests/test_postgres_ops.py` pour valider outils switchbot-postgres.
- Vérifier `HistoryService` si Postgres indisponible (service doit se désactiver proprement).

## 6. Intégration Render-PostgreSQL
- **NOUVEAU** : Pour opérations cross-environnements (migrations staging→prod), utiliser `render-postgres-integration` skill.
- Coordination backups avec déploiements Render via cron jobs automatisés.
- Monitoring intégré métriques Render + PostgreSQL.

## 7. Documentation
- Mettre à jour `docs/core/configuration.md` + `docs/core/deployment.md` + Memory Bank (decisionLog + progress) après toute modification structurelle.
- Référencer les incidents dans `memory-bank/activeContext.md` si investigation en cours.
- **NOUVEAU** : Documenter utilisation outils MCP switchbot-postgres dans guides opérationnels.
