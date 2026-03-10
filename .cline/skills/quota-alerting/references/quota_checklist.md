# Checklist Quota & Bandeau UI

## Backend
1. `ApiQuotaTracker` :
   - `record_call()` incrémente fallback.
   - `record_from_headers()` appelé depuis `SwitchBotClient`.
   - `refresh_snapshot()` utilisé pour forcer affichage.
2. `state.json` doit contenir :
   - `api_quota_day`
   - `api_requests_total`
   - `api_requests_remaining`
   - `api_requests_limit`
   - `api_quota_reset_at`

## UI / Routes
- `routes._build_quota_context()` retourne :
  - `quota_remaining`
  - `quota_limit`
  - `quota_day`
  - `quota_reset`
- Bandeau `/templates/index.html` :
  - `role="alert"`, `aria-live="polite"`.
  - Classes `sb-alert sb-alert-warning`.
  - Texte fallback "quota non disponible" si champs manquants.

## Tests
| Test | Emplacement | Objectif |
| --- | --- | --- |
| BeautifulSoup | `tests/test_dashboard_routes.py` | affichage bandeau <, =, > seuil |
| Tracker | `tests/test_quota.py` (ajouter si manque) | reset quotidien, headers |

## Commandes utiles
```bash
python scripts/quota_snapshot.py
```

## Documentation
- MAJ `docs/core/configuration.md` pour tout nouveau champ/ seuil.
- Journaliser dans Memory Bank (decisionLog + progress).
