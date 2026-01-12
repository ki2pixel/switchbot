# Mise à jour du contexte actif

# Contexte Actif - Session debug terminée

## Objectifs
- Déboguer et corriger la logique `winter_off` pour éviter les déclenchements excessifs des scènes OFF.
- Assurer que `winter_off` se déclenche uniquement lorsque la température dépasse `max_temp + hysteresis`, suivi de répétitions OFF après l'intervalle configuré, sans déclenchements multiples dus aux cooldowns.

## Décisions Clés
- Implémentation de l'idempotence pour les actions OFF : vérifier `assumed_aircon_power == "off"` avant de déclencher de nouvelles actions OFF, même après expiration du cooldown si la température reste élevée.
- Purge automatique des tâches `off_repeat` lors des actions ON pour éviter des conflits.
- Ajout de tests unitaires pour couvrir les scénarios de répétition et d'idempotence.

## Questions/Problèmes Ouverts
- Aucun problème ouvert. Le comportement est désormais stable selon les logs utilisateur.

## Prochaines Étapes
- Surveillance des logs en production pour confirmer la stabilité.
- En attente d'une nouvelle tâche utilisateur.