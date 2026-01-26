---
name: quota-alerting
description: Runbook pour ajuster le suivi et les alertes de quota SwitchBot (ApiQuotaTracker, bandeau UI, tests BeautifulSoup).
---

# Gestion des quotas API

Utiliser ce skill pour toute évolution du suivi de quota (backend + UI + tests).

## 1. Contexte à charger
- Backend : `switchbot_dashboard/quota.py`, usages dans `automation.py` et `routes.py` (`_build_quota_context`).
- UI : `templates/index.html` (bandeau), `static/css/theme.css` (styles), `static/js/loaders.js` pour loaders POST.
- Tests : `tests/test_dashboard_routes.py` (scénarios quota), `tests/test_quota.py` si existant.
- Script snapshot : `scripts/quota_snapshot.py` pour rafraîchir l'état (`python .windsurf/skills/quota-alerting/scripts/quota_snapshot.py`).
- Checklist : `references/quota_checklist.md` (backend/UI/tests).

## 2. Workflow
1. **Backends** :
   - Ajouter/ajuster les champs `api_quota_*` dans `state.json` via `state_store`.
   - S'assurer que `ApiQuotaTracker` met à jour local + headers `X-RateLimit-*`.
2. **Seuils & configuration** :
   - Paramètre `api_quota_warning_threshold` dans `settings`; valider via `_as_int`.
   - Ajouter doc dans `docs/configuration.md` si nouveau champ.
3. **Frontend** :
   - Bandeau conditionnel (classes `sb-alert`), accessible (`role="alert"`).
   - Afficher métadonnées : jour suivis, reset.
4. **Tests** :
   - Cases BeautifulSoup : < seuil, == seuil, > seuil, désactivé.
   - Tests unitaires pour la logique tracker (reset quotidien, fallback local).

## 3. Bonnes pratiques
- Jamais de "N/A" sur l’UI : fournir fallback textuel.
- Logs `[quota]` pour chaque reset/alerte.
- Documenter modifications dans Memory Bank et `docs/history-monitoring.md` si impact sur graphiques.
