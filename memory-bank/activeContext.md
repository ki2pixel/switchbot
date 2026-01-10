[2026-01-10 20:15:00] - Système d'alerte de quota et métadonnées implémentés

## Current Focus
- Surveillance du comportement de l'automatisation avec les scènes SwitchBot
- Vérification des métriques de quota d'API
- Documentation des bonnes pratiques d'utilisation des scènes
- Surveillance de l'efficacité du système d'alerte de quota
- Collecte de retours sur l'expérience utilisateur des nouvelles fonctionnalités de quota

## Recent Changes
- **Système d'alerte de quota** :
  - Ajout d'un seuil d'avertissement configurable (`api_quota_warning_threshold`) dans `config/settings.json`
  - Affichage d'une alerte visuelle lorsque le nombre de requêtes restantes est faible
  - Tests d'intégration avec BeautifulSoup pour vérifier le comportement de l'alerte
  - Documentation des bonnes pratiques dans `configuration.md`

- **Métadonnées de quota** :
  - Affichage du jour de suivi (`api_quota_day`) et de l'heure de réinitialisation (`api_quota_reset_at`)
  - Mise à jour de `quota.py` pour stocker systématiquement l'heure de réinitialisation
  - Styles CSS pour une intégration visuelle harmonieuse
  - Tests d'intégration pour vérifier l'affichage correct des informations

- **Automatisation par scènes SwitchBot** :
  - Suppression des actions rapides "Chauffage (Hiver)" et "Clim (Été)" au profit des scènes SwitchBot
  - Implémentation de l'automatisation pilotée par scènes avec fallback sur les commandes de base
  - Améliorations de la robustesse et de la documentation

- **Améliorations de la robustesse** :
  - Gestion des scènes manquantes avec fallback sur `setAll`/`turnOff`
  - Vérification de la configuration requise (`aircon_device_id`)
  - Meilleure gestion des erreurs et journalisation des problèmes potentiels
  - Mise à jour des métriques de quota d'API

## Open Questions / Issues
- Aucun problème critique identifié
- Les tests unitaires couvrent les principaux cas d'utilisation
- La documentation a été mise à jour pour refléter les changements

## Next Steps
- Surveiller les journaux pour détecter tout problème potentiel avec le point de terminaison de santé
- Envisager d'ajouter des métriques supplémentaires au point de terminaison de santé si nécessaire
