
# Maintenance PostgresStore

Utiliser ce skill pour toute opération sur le stockage Postgres (Neon) et son fallback.

## 1. Préparation
- Lire `switchbot_dashboard/config_store.py` (classes PostgresStore, JsonStore).
- Vérifier `.env` : `STORE_BACKEND=postgres`, `POSTGRES_URL`, `POSTGRES_SSL_MODE`.
- Consulter `memory-bank/decisionLog.md` pour les derniers choix architecturaux.
- Script santé : `scripts/store_health.py` pour inspecter settings/state stores (`python .sixthskills/postgres-store-maintenance/scripts/store_health.py`).
- Référence incidents : `references/postgres_incident.md` (fallback, migration, corruption).

## 2. Migrations / Scripts
1. Lancer `scripts/migrate_to_postgres.py --dry-run` avant toute modification.
2. Appliquer les scripts SQL (`scripts/create_history_table.sql`, etc.) via `psql` ou Neon console.
3. Après migration, tester lecture/écriture :
   ```python
   store = current_app.extensions["settings_store"]
   data = store.read()
   store.write(data)
   ```

## 3. Gestion incidents
- Si `psycopg_pool` KO :
  1. Observer les logs `[store]`.
  2. Régénérer le pool via `store._pool.wait()` (dans shell).
  3. Si échec répété, basculer `STORE_BACKEND=filesystem` temporairement et documenter.
- Sur perte Neon : activer fallback JsonStore mais planifier la resynchronisation (script dédié pour reimporter settings/state).

## 4. Validation & tests
- `tests/test_postgres_store.py`, `tests/test_config_store.py` pour s’assurer que les mocks passent.
- Vérifier `HistoryService` si Postgres indisponible (service doit se désactiver proprement).

## 5. Documentation
- Mettre à jour `docs/core/configuration.md` + `docs/core/deployment.md` + Memory Bank (decisionLog + progress) après toute modification structurelle.
- Référencer les incidents dans `memory-bank/activeContext.md` si investigation en cours.
