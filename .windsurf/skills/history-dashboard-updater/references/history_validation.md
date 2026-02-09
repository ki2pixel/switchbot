# Checklist Validation History Dashboard

## Backend / Postgres
1. **Schéma** : synchroniser `scripts/create_history_table.sql` (colonnes, index, rétention 6h).
2. **Batch** : vérifier `HistoryService.FLUSH_INTERVAL_SECONDS` ≤ 30s et `BATCH_SIZE` cohérent.
3. **Nettoyage** : confirmer qu'un `DELETE ... WHERE observed_at < now() - interval '6 hours'` est programmé.
4. **EXPLAIN ANALYZE** : viser < 30 ms pour requêtes agrégats 6h (index `observed_at`).

## API Flask
- Endpoints attendus :
  - `GET /history/api/records?minutes=360`
  - `GET /history/api/aggregates?metrics=temperature,humidity`
  - `GET /history/api/latest`
- Paramètres : valider `minutes` (15-360), `metrics` (csv limité à `temperature`, `humidity`, `assumed_aircon_power`).
- Réponses vides → `{ "data": [] }` sans erreur 500.

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
