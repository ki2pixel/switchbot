# Mise à jour du contexte actif

# Contexte Actif - En attente de nouvelle tâche

## Objectifs
- Aucun objectif actif.

## Décisions Clés
- **Polling adaptatif implémenté** : SchedulerService calcule intervalles effectifs (idle/warmup/in-window) avec auto-reschedule et garantie réveil warmup. Tests unitaires OK (12 passed). Plan d'action UI/Postgres créé dans `docs/adaptive-polling-settings-plan.md`.
- **Intégration UI/Postgres des réglages de polling adaptatif terminée** : Toggle + champs idle/warmup ajoutés dans settings.html, validation backend via `_as_bool/_as_int`, documentation complète (configuration.md + scheduler.md), tests couvrant persistance UI et mode fixe. 33 tests passants.

## Questions/Problèmes Ouverts
- Aucun problème ouvert.

## Prochaines Étapes
- En attente d'une nouvelle tâche utilisateur.