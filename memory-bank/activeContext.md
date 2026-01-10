[2026-01-10 15:39:00] - Session de migration des presets vers scènes terminée

## Current Focus
- Migration complète de la logique des `aircon_presets` vers `aircon_scenes`
- Nettoyage du code et de la documentation

## Recent Changes
- Suppression complète des `aircon_presets` du fichier de configuration
- Nettoyage du code backend (routes.py) pour ne garder que la logique des scènes
- Mise à jour de l'interface utilisateur pour ne conserver que la configuration des scènes
- Mise à jour de la documentation pour refléter ces changements

## Open Questions / Issues
- Aucun problème identifié lors de la migration
- Les tests ont été mis à jour pour refléter les changements

## Next Steps
- Vérifier que tous les tests passent avec succès
- S'assurer que la documentation est complète et à jour
- Prévoir une vérification manuelle des fonctionnalités modifiées
