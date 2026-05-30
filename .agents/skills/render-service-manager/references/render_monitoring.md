# Guide de Monitoring Render.com

Ce document couvre l'utilisation des fonctionnalités de monitoring intégrées à Render pour notre application.

## Indicateurs Clés
1. **CPU Usage** : Une utilisation élevée peut indiquer un polling de l'API trop intensif.
2. **Memory Usage** : Surveiller les fuites de mémoire (ex: dans le `HistoryService`).
3. **HTTP Error Rate (5xx)** : A surveiller lors des redéploiements.

## Accès aux Logs
- Utiliser le dashboard Render ou configurer un export vers Datadog/Logtail si nécessaire.
