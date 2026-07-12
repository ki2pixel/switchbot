# Contexte Actif

## Objectifs
- [x] Phase 1 : Sécurité, Session & Hardening (Complété)
  - Implémentation des en-têtes de sécurité HTTP (S-01) et cookies de session sécurisés SameSite/Secure (S-02).
  - Alerte sur le stockage Rate Limit en production (S-04), validation du mode de fonctionnement et des IDs d'appareils (S-05, S-06).
  - Rotation de session post-connexion (S-07), allowlist stricte sur le debug (S-08) et page 503 personnalisée pour StoreError (Q-04).
- [x] Phase 2 : Architecture, Nettoyage & Refactoring IFTTT (Complété)
  - Retrait du code mort lié aux webhooks et IFTTT (A-01, S-03).
  - Suppression de psycopg pool __del__ non déterministe (A-02) et des anciens stores JsonStore / FailoverStore inutilisés (A-03, A-04).
  - Planification horaire de la purge d'historique hors de la boucle principale (A-06).
- [x] Phase 3 : Optimisations de Performance (Complété)
  - Cache en mémoire de 60s pour `get_devices()` et `get_device_status()` afin d'éliminer les requêtes N+1 (P-01).
  - Plafonnement des temps de sommeil à 3s maximum lors des retries SwitchBot (P-02).
  - Encapsulation transactionnelle des lectures-écritures de paramètres dans `routes.py` (P-03).
  - Proxy `CachedStoreWrapper` pour éliminer les lectures redondantes en base durant un tick (P-04) avec cohérence de cache liée au quota tracker.
- [x] Phase 4 : Qualité du Code & Robustesse (Complété)
  - Analyse Ruff 100% propre (Q-01) et centralisation des fonctions utilitaires dans `utils.py` (Q-02, A-05).
  - Importation des constantes/fonctions à responsabilité unique pour éliminer la duplication de code (Q-03).
  - Documentation du mapping historique entre api_requests_total (état) et api_requests_today (base de données) (Q-05).
- [x] Phase 5 : Tests de Non-Régression & CI (Complété)
  - Intégration de PostgreSQL et exécution des tests unitaires dans le workflow GitHub Actions (T-01).
  - Ajout des cas de tests pour la rotation de session, la validation de paramètres et le cache (T-02, T-03).
  - Suite de tests unitaire de 166 tests verte à 100%.

## Décisions Clés
- Utilisation de `CachedStoreWrapper` pour encapsuler settings et state store dans `AutomationService` et redirection de la référence de store de `quota_tracker` pour assurer une cohérence parfaite et éliminer les requêtes de quota redondantes.
- Utilisation de `_transaction_context` pour encapsuler de façon optionnelle les transactions dans les blueprints Flask afin de supporter à la fois les stores réels et les MemoryStore de test.
- Limitation des temps de retry de l'API à 3s pour éviter d'occuper les threads du serveur de production en cas d'erreur de service externe.
- Contournement automatique de la requête d'état de l'API pour les appareils infrarouges virtuels (identifiés par leur ID long à tirets) car l'API SwitchBot ne supporte pas l'état en lecture (erreur 190 systématique). Cela évite le gaspillage du quota d'API et le bruit dans les logs.


- [x] Phase F1 : Routage SPA & Mécanismes de Navigation (Complété)
  - Correction désynchronisation CSS / doublons preload links dans `spa-router.js`.
  - Suppression du double footer lors des transitions SPA.
  - Robustification du filtre `globalScripts` contre les query strings `?v=`.
  - Correction du chevauchement CTA mobile / footer bar.
  - Suppression de `bottom-nav.js` (fichier mort) et consolidation visibilité desktop/mobile.
- [x] Phase F2 : Optimisation des Assets & Performance (Complété - PurgeCSS différé)
  - Suppression de Font Awesome Brands (320 Ko inutilisés) et du TTF fa-solid.
  - Suppression des fichiers morts : `performance-optimizer.js`, `advanced-optimizer.js`, `perf-worker.js`, `critical.css`.
  - Conversion Space Grotesk TTF → WOFF2 (−62%) et correction référence Roboto.
  - [ ] Purge Bootstrap via PurgeCSS — DIFFÉRÉ (nécessite validation visuelle étendue).
- [x] Phase F3 : Accessibilité WCAG 2.1 AA & Conformité UX (Complété)
  - Réparation `aria-hidden` loaders + région `aria-live` pour les annonces.
  - Définition globale de `.sr-only` / `.visually-hidden` dans `theme.css`.
  - Structuration sémantique (hiérarchie titres, landmarks `<main>`, skip-links, `scope` table).
  - Gestion du focus après transition SPA.
  - Suppression du délai artificiel de 1s dans `loaders.js`.
- [x] Phase F4 : Sécurité Frontend & Robustesse Dynamique (Complété)
  - Validation same-origin dans `loadScriptDynamic()` + sélecteur CSS sûr.
  - Refactoring `innerHTML` → DOM API dans `history.js` (zéro innerHTML).
  - Implémentation CSP minimale (ajout de `font-src 'self'`).
  - `AbortController` + timeout 10s pour les fetch history.
  - Nettoyage des `console.log` de debug en production (passage en console.debug).
- [x] Phase F5 : Couverture de Tests Frontend (Complété)
  - Tests SPA (doublons CSS, filtre scripts, fallback full-page).
  - Tests accessibilité (`.sr-only`, skip-link, `<main>`, `scope`).
  - Tests performance (fichiers morts absents, FA brands absent, CSP font-src, AbortController).
  - Suite de 31 tests unitaires/intégration frontend 100% verte.

## Prochaines Étapes
- [ ] Lancer et surveiller le tableau de bord en production.
- [ ] Valider visuellement le rendu responsive global sur mobile réel.

**Plan détaillé :** [remediation_frontend_plan.md](file:///home/kidpixel/SwitchBot/docs/remediation/remediation_frontend_plan.md)
