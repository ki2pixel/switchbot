[2026-01-10 18:45:00] - Automatisation par scènes SwitchBot implémentée

## Current Focus
- Surveillance du comportement de l'automatisation avec les scènes SwitchBot
- Vérification des métriques de quota d'API
- Documentation des bonnes pratiques d'utilisation des scènes

## Recent Changes
- Suppression des actions rapides "Chauffage (Hiver)" et "Clim (Été)" au profit des scènes SwitchBot :
  - Suppression des routes `quick_winter` et `quick_summer` dans `routes.py`
  - Mise à jour de l'interface utilisateur dans `index.html`
  - Mise à jour de la documentation dans `ui-guide.md`
- Implémentation de l'automatisation pilotée par scènes SwitchBot :
  - Création du module `aircon.py` pour centraliser la logique des scènes
  - Mise à jour de `AutomationService` pour prioriser les scènes avec fallback
  - Ajout de tests unitaires complets couvrant les cas d'utilisation des scènes
  - Documentation mise à jour dans `configuration.md` et `ui-guide.md`
- Améliorations de la robustesse :
  - Gestion des scènes manquantes avec fallback sur `setAll`/`turnOff`
  - Vérification de la configuration requise (`aircon_device_id`)
  - Mise à jour des métriques de quota d'API

## Open Questions / Issues
- Aucun problème critique identifié
- Les tests unitaires couvrent les principaux cas d'utilisation
- La documentation a été mise à jour pour refléter les changements

## Next Steps
- Surveiller les journaux pour détecter tout problème potentiel avec le point de terminaison de santé
- Envisager d'ajouter des métriques supplémentaires au point de terminaison de santé si nécessaire
