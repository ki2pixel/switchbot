---
name: postgres-store-maintenance
description: Guide pour maintenir PostgresStore (migrations, bascule JsonStore, validation pool psycopg) et scripts Neon.
---

# Maintenance PostgresStore

Utiliser ce skill pour toute opération sur le stockage Postgres (Neon) et son fallback.

## 1. Préparation
- Lire `switchbot_dashboard/postgres_store.py` (`PostgresStore`) et `switchbot_dashboard/config_store.py` (`JsonStore`, `BaseStore`).
- Vérifier `.env` : `STORE_BACKEND=postgres`, `POSTGRES_URL`, `POSTGRES_SSL_MODE`.
- Consulter `decisionLog.md` via `fast_read_file(path="/home/kidpixel/SwitchBot/memory-bank/decisionLog.md")` pour les derniers choix architecturaux.
- Script santé : `.agents/skills/postgres-store-maintenance/scripts/store_health.py` (`python .agents/skills/postgres-store-maintenance/scripts/store_health.py`).
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
4. **Gestion du Pool** : Manipuler explicitement les contextes de transaction du `psycopg_pool`. Garantir la libération des connexions via `with self.pool.connection() as conn:` ou via contexte manager.

## 3. Gestion incidents
- Si `psycopg_pool` KO :
  1. Observer les logs `[store]`.
  2. Régénérer le pool via `store._pool.wait()` (dans shell).
  3. Hors production, basculer `STORE_BACKEND=filesystem` temporairement et documenter. En production, `ResilientStore` alerte et laisse les routes répondre `503` ; n'activer `STORE_RUNTIME_FALLBACK=true` qu'en connaissance de cause.
- Sur perte Neon : hors production, le fallback `JsonStore` est automatique ; en production, alerter (`[store] CRITICAL`) et rétablir Neon. Si un fallback JSON a été utilisé, planifier la resynchronisation (script dédié pour réimporter settings/state).

## 4. Validation & tests
- `tests/test_postgres_store.py`, `tests/test_config_store_failover.py` pour s’assurer que les mocks passent.
- Vérifier `HistoryService` si Postgres indisponible (service doit se désactiver proprement).

## 5. Documentation
- Mettre à jour `docs/core/configuration.md` + `docs/core/deployment.md` + Memory Bank (decisionLog + progress) après toute modification structurelle.
- Référencer les incidents dans `activeContext.md` via `edit_file(path="/home/kidpixel/SwitchBot/memory-bank/activeContext.md")` si investigation en cours.
