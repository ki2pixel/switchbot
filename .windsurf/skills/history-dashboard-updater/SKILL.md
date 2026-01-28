---
name: history-dashboard-updater
description: Workflow complet pour étendre le module History (service, API Flask, frontend Chart.js) sans régression.
---

# Mise à jour du dashboard d'historique

Déclencher ce skill pour toute évolution du monitoring (backend/postgres → API → frontend).

## 1. Cartographier l’existant
- Backend : `switchbot_dashboard/history_service.py`, `automation.py` (integration), `routes.py` (/history et `/history/api/*`).
- Frontend : `templates/history.html`, `switchbot_dashboard/static/js/history.js`, `switchbot_dashboard/static/css/history.css`.
- Tests : `tests/test_history_service.py`, `tests/test_history_routes.py` (si présent).
- Référence : `references/history_validation.md` pour checklist complète backend/API/frontend/tests.

## 2. Plan d’attaque multi-couches
1. **Schéma/Postgres** : ajuster `scripts/create_history_table.sql`, vérifier index + nettoyage 6h.
2. **Service** : mettre à jour `HistoryService` (batch, agrégations, filtres), ajouter tests unitaires.
3. **Routes API** : respecter la validation des paramètres (plages, métriques). Retourner JSON prêt à consommer (labels + datasets).
4. **Frontend** : utiliser Chart.js offline, décimation LTTB, loaders. Tenir compte de `prefers-reduced-motion`.

## 3. Vérifications obligatoires
- Données vides → graphiques affichent fallback (texte "Pas de données").
- Temps de réponse API < 300 ms pour 6h de données (utiliser EXPLAIN si besoin).
- Tests Pytest ciblés (service + routes + JS si snapshot) doivent passer.

## 4. Documentation & communication
- Mettre à jour `docs/history-monitoring.md` + Memory Bank (productContext + decisionLog).
- Ajouter captures/metrics si nouvelles visualisations.
- Mentionner dans progress l’état des tests et déploiements.
