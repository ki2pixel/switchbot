# Contexte Actif

## Objectifs
- [x] Résolution des vulnérabilités de sécurité P0 et P1 (mot de passe en clair DASHBOARD_PASSWORD, session authentifiée avec CSRF, page login glassmorphic, retrait du jeton de l'URL pour Bearer token).
- [x] Durcissement du stockage et SSL (sslmode explicite via kwargs, blocage de démarrage sans fallback JSON en production).
- [x] Optimisation des verrous et de la concurrence (appel API hors transaction PostgreSQL, verrou d'état distribué de 2 minutes pour éviter les conflits d'automatisation et d'UI).
- [x] Fiabilité des quotas et rate-limiting (correction de la métrique history_service.py vers api_requests_total, rafraîchissement réel des quotas via get_devices, rate-limiting global configurable).
- [x] Campagne d'intégration de tests unitaires et de non-régression complétée (164 tests passed, 0 failed).

## Décisions Clés
- Utilisation de `DASHBOARD_PASSWORD` en variable d'environnement (valeur comparée de manière sécurisée en temps constant via `hmac.compare_digest`).
- Blocage strict en production en cas de base PostgreSQL KO ou de mot de passe non défini pour empêcher des expositions ou comportements dégradés non contrôlés.
- Utilisation de l'en-tête standard `Authorization: Bearer <token>` sur `/debug/state` et suppression du query paramètre `token` de l'URL.
- Verrouillage concurrent en base de données (`automation_in_progress` et `automation_locked_at`) avec expiration automatique après 2 minutes, protégeant à la fois le tick d'automatisation et les commandes manuelles de l'UI.
- Intégration de rate-limiting (Flask-Limiter) sur les points d'entrée sensibles (5/min pour la connexion et les réglages, 10/min pour le contrôle).

## Prochaines Étapes
- En attente de nouveaux retours de l'utilisateur sur la livraison des corrections de l'audit.
