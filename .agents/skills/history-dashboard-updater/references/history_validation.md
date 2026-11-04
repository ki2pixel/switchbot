# Checklist Validation History Dashboard

## Backend / Postgres
1. **Schéma** : synchroniser `scripts/create_history_table.sql` (colonnes, index, rétention par défaut 24h, configurable via `HISTORY_RETENTION_HOURS`).
2. **Batch** : vérifier `HistoryService.FLUSH_INTERVAL_SECONDS` ≤ 30s et `BATCH_SIZE` cohérent.
3. **Nettoyage** : confirmer qu'un `DELETE ... WHERE timestamp < now() - interval '<retention> hours'` est programmé (job APScheduler `history_cleanup`, toutes les heures).
4. **EXPLAIN ANALYZE** : viser < 30 ms pour requêtes agrégats 6h (index `observed_at`).

## API Flask
- Endpoints attendus :
  - `GET /history/api/data?start=<iso>&end=<iso>&metrics=temperature,humidity&granularity=minute&limit=1000`
  - `GET /history/api/aggregates?period_hours=6`
  - `GET /history/api/latest?limit=10`
- Paramètres : valider `start`/`end` (ISO-8601, `start < end`), `metrics` (csv limité à `temperature`, `humidity`, `assumed_aircon_power`), `granularity` (`minute`, `5min`, `15min`, `hour`), `limit` (1-10000).
- Réponses vides ou service indisponible → `{ "data": [], "degraded": true }` en HTTP 200, jamais de 500/503 bloquant le rendu.

## Frontend Chart.js
- Charger `switchbot_dashboard/static/js/history.js` + `switchbot_dashboard/static/css/history.css`.
- Activer décimation LTTB (`decimation.enabled = true`).
- `prefers-reduced-motion` : désactiver animations si vrai.
- Loaders : attribut `data-loader` sur filtres, overlay 15s.

## Tests incontournables
| Type | Fichier | Objectif |
| --- | --- | --- |
| Service | `tests/test_history_service.py` | flush batch, cleanup, erreurs Postgres |
| Routes | `tests/test_history_routes.py` ou `tests/test_dashboard_routes.py` | paramètres invalides / data vide |
| JS (optionnel) | `switchbot_dashboard/static/js/history.js` via Jest ou snapshot | interactions filtres |

## Documentation
- Mettre à jour `docs/guides/monitoring-dashboard.md` (schémas, API, captures).
- Logger les décisions dans Memory Bank (decisionLog + progress).
