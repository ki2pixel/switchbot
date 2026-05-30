# Guide de Débogage en Production

Pratiques sûres pour investiguer les problèmes sur les environnements de production.

## Principes
- Ne jamais modifier le code en direct sur le serveur de production.
- Utiliser les logs Render pour l'analyse a posteriori.
- Isoler les anomalies via les dashboards de monitoring (CPU, RAM).
- Si une requête échoue, consulter `HistoryService` ou l'API SwitchBot.
