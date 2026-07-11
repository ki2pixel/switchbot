# Contexte Actif

## Objectifs
- [x] Résolution des vulnérabilités de sécurité P0 et P1 (mot de passe en clair DASHBOARD_PASSWORD, session authentifiée avec CSRF, page login glassmorphic, retrait du jeton de l'URL pour Bearer token).
- [x] Durcissement du stockage et SSL (sslmode explicite via kwargs, blocage de démarrage sans fallback JSON en production).
- [x] Optimisation des verrous et de la concurrence (appel API hors transaction PostgreSQL, verrou d'état distribué de 2 minutes pour éviter les conflits d'automatisation et d'UI).
- [x] Fiabilité des quotas et rate-limiting (correction de la métrique history_service.py vers api_requests_total, rafraîchissement réel des quotas via get_devices, rate-limiting global configurable).
- [x] Campagne d'intégration de tests unitaires et de non-régression complétée (164 tests passed, 0 failed).
- [x] Remédiation des défauts, vulnérabilités et ergonomie frontend de l'audit complétée (Navigation SPA, CTA mobile, A11y loaders et graphiques, sémantique HTML, allègement optimiseurs, local fonts et CSS critique).

## Décisions Clés
- Gestion dynamique et synchronisée des feuilles de style CSS de page dans `spa-router.js` pour éviter le FOUC et éliminer les accumulations de styles.
- Délégation d'événements globale sur `document` pour les loaders (`loaders.js`), stabilisant les écouteurs d'événements et protégeant contre les écouteurs dupliqués dans la SPA.
- Accessibilité enrichie : attribut `aria-busy` pendant le chargement, live region `role="status"` avec étiquettes vocales sur les spinners, et alternatives textuelles dynamiques (statistiques calculées en JS) pour les graphiques d'historique.
- Optimiseurs de performance simplifiés pour éliminer les boucles en arrière-plan et le Web Worker, et désactivation de toutes les connexions externes CDN/Google pour un offline-first strict.
- Polices Space Grotesk hébergées et référencées localement dans `critical.css` et `index.html`.

## Prochaines Étapes
- En attente de nouveaux retours de l'utilisateur sur les modifications frontend ou pour démarrer une nouvelle tâche.
