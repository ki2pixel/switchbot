# Progrès du Projet - SwitchBot Dashboard

## Terminé
- **[2026-07-11 03:45:00] - Remédiation Audit Frontend (Navigation SPA, Ergonomie Mobile, Accessibilité, et Performances)**
  - **Phase 1** : Gestion dynamique des CSS dans `spa-router.js` (injection et retrait au vol, attente des chargements). Refonte de `loaders.js` avec délégation globale d'événements pour éliminer les écouteurs dupliqués et perdus. CTA mobile repositionné pour éviter le chevauchement, cibles tactiles passées à 44px min.
  - **Phase 2** : Accessibilité de l'overlay de chargement (`aria-busy="true"`, `role="status"` et text `sr-only`). Alternatives textuelles dynamiques résumant les moyennes/extrema des graphiques dans `history.js` et `history.html`. Landmark `<main>` unique et cascade de titres (`h1` -> `h2`) restaurés sur tous les templates.
  - **Phase 3** : Allègement de `performance-optimizer.js` et `advanced-optimizer.js` en retirant les loops, observers et workers. Déclarations de polices Space Grotesk passées en local dans `critical.css` et synchronisées avec le bloc `<style>` inline de `index.html`.
  - **Correctif Darkmode** : Résolution des incohérences de style (fonds clairs, textes illisibles) sur la page `/history` en définissant les variables de Design System manquantes (`--sb-surface`, `--sb-text-primary`, etc.) au niveau global dans `theme.css`, `critical.css` et `index.html`.
  - **Tests** : Validation de la suite de tests unitaires (163 tests passés, 1 échec existant lié à l'authentification backend).

- **[2026-07-11 03:05:00] - Remédiation Audit Backend (Sécurité, Concurrence et Fiabilité)**
  - **Phase 1** : Authentification globale par mot de passe de session, page `/login` glassmorphic premium, route `/debug/state` sécurisée via token en en-tête `Authorization: Bearer <token>`, dépendance Gunicorn mise à jour à version `>=22.0.0`.
  - **Phase 2** : Configuration SSL (`sslmode`) explicite via kwargs dans psycopg pool, arrêt strict en production si pool Postgres ou health check HS (pas de fallback JSON silencieux).
  - **Phase 3** : Isolation transactionnelle (appels API hors transaction Postgres), verrouillage d'état concurrent distribué de 2 minutes pour éviter les chevauchements d'automatisation et de commandes de l'UI.
  - **Phase 4** : Correction du quota d'historique en utilisant `api_requests_total`, vrai rafraîchissement des compteurs via `client.get_devices()`, rate-limiting de sécurité sur `/login`, `/settings` et toutes les routes d'actions de contrôle direct.
  - **Tests** : Ajout de nouveaux tests d'intégration et unitaires dans `test_backend_hardening.py` et `test_dashboard_routes.py`. L'ensemble de la suite pytest de 164 tests passe à 100% de réussite.

- **[2026-07-10 15:43:00] - Optimisation du quota de l'API SwitchBot via un cooldown de sondage AC et validation physique critique**
- **[2026-07-08 14:58:00] - Polling temps réel du statut AC pour corriger l'incohérence d'état en mode direct**
- **[2026-07-04 12:30:00] - Implémentation du plan d'action d'audit unifié (Amortissement PostgreSQL et correctifs Chart.js)**
- **[2026-07-02 18:20:00] - Suppression complète d'IFTTT et mode direct exclusif**

## En cours
- Aucun. Tout est complété avec succès.

## À faire / Étapes Futures
- En attente de nouvelles instructions de l'utilisateur.
