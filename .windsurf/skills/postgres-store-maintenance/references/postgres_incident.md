# Incident PostgresStore

## Pré-checks
1. `POSTGRES_URL` défini, SSL `POSTGRES_SSL_MODE` (require par défaut).
2. Lancer l'inspecteur :
   ```bash
   python scripts/store_health.py > debug/store_health.json
   ```
3. Vérifier logs `[store]` pour bascule éventuelle.

## Scénario : Health check KO
- Étapes :
  1. Confirmer `health_check()` False dans `store_health.json`.
  2. Basculer temporairement `STORE_BACKEND=filesystem` pour rétablir l'app.
  3. Inspecter Neon Dashboard (connexions, quotas, maintenance).
  4. Relancer `scripts/migrate_to_postgres.py --dry-run` avant retour Postgres.

## Scénario : Données corrompues
- Utiliser `store.read()` dans shell Flask.
- Comparer avec backup JSON.
- Réécrire via `store.write(validated_data)` ; vérifier `updated_at`.

## Scénario : Migration
1. `scripts/migrate_to_postgres.py --dry-run`
2. `scripts/migrate_to_postgres.py --apply`
3. Vérifier `json_store` table (`SELECT kind, updated_at FROM json_store;`).

## Documentation
- MAJ `docs/core/configuration.md`, `docs/core/deployment.md` + Memory Bank (decisionLog).
- Si fallback prolongé : noter dans `activeContext.md`.
