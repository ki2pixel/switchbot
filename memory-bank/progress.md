# Progrès du Projet - SwitchBot Dashboard

## Terminé
- **[2026-07-12 13:25:00] - Exécution complète de la remédiation Frontend (Phases 1 à 5)**
  - **Routage SPA & Navigation** : Correction de la désynchronisation CSS/preload, suppression du double footer, correction du CTA mobile sticky via `--sb-footer-height`, retrait de `bottom-nav.js` et robustification du filtre de scripts.
  - **Assets & Performance** : Suppression des brands de Font Awesome (−320 Ko), suppression de fa-solid.ttf, conversion Space Grotesk en WOFF2 (−62% de poids), suppression de tous les fichiers JS/CSS morts.
  - **Accessibilité (WCAG 2.1 AA)** : Annonces aria-live dynamiques pour les loaders, classe `.sr-only` et `.visually-hidden` globales dans `theme.css`, structure sémantique validée (landmarks `<main>`, skip-links claviers, scope sur tableaux, hiérarchie titres H1-H3).
  - **Sécurité & Robustesse** : Sécurisation de `loadScriptDynamic` (same-origin strict), élimination totale de `innerHTML` dans `history.js` via DOM API, ajout de `font-src 'self'` dans la CSP backend, intégration d'AbortController avec timeout sur l'historique, nettoyage des logs console en console.debug.
  - **Couverture de Tests** : Création de 3 suites de tests dédiées (`test_frontend_spa.py`, `test_frontend_accessibility.py`, `test_frontend_performance.py`), 31 tests ajoutés et 100% verts, portant le total à 198 tests réussis dans la CI.
- **[2026-07-12 12:50:00] - Correction de la détection de l'environnement de test en CI**
  - Correction de l'évaluation fausse-positive de `is_production` lors de l'absence du fichier `.env` (donc pas de `FLASK_DEBUG=1`) dans les runners CI en se basant explicitement sur `app.testing` et `FLASK_ENV=testing`.
  - Configuration explicite de `app.config["TESTING"] = True` sur les applications Flask de test simulant les fallbacks.
- **[2026-07-12 12:41:00] - Finalisation des Phases 3, 4 et 5 du plan d'implémentation**
  - **Performance (P-01 à P-04)** : Implémentation du cache de 60s sur les requêtes d'appareils, limitation des retries bloquants à 3s, transactions sur les modifications de paramètres dans les routes, et optimisation du logger de quota via un proxy de store `CachedStoreWrapper` avec cohérence de cache dynamique pour le quota tracker.
  - **Qualité (Q-01 à Q-05, A-05)** : Nettoyage complet via Ruff (14 corrections automatiques), unification des convertisseurs numériques (`_safe_int`, `_safe_float`, `_safe_bool`) et helpers temporels dans `utils.py`, retrait des constantes dupliquées, et documentation du mapping base de données/état.
  - **Validation & CI (T-01 à T-03)** : Intégration de PostgreSQL dans GitHub Actions et automatisation des tests pytest dans la CI. Ajout de tests de non-régression robustes pour le cache d'API, le plafonnement de retries, la validation de paramètres et la rotation de session. Suite de tests verte à 100% (166/166).
- **[2026-07-12 12:35:00] - Implémentation des Phases 1 et 2 du plan d'implémentation**
  - **Sécurité (S-01 à S-08)** : Ajout des en-têtes HTTP de sécurité, configuration stricte SameSite/Secure pour les cookies de session Flask, alertes Rate-Limit, validations rigoureuses de paramètres et des IDs de capteurs/AC, rotation de session post-connexion, allowlist stricte sur le debug et gestion globale de StoreError (page 503 personnalisée).
  - **Nettoyage (A-01 à A-06)** : Nettoyage du code IFTTT/webhooks mort, suppression du destructeur non déterministe de pool psycopg, purge de RedisJsonStore/FailoverStore, et migration de la purge périodique de l'historique vers APScheduler (job horaire).
- **[2026-07-12 12:29:00] - Restructuration du plan d'audit en plan d'implémentation**
  - **Audit de plan.md** : Réécriture complète de plan.md pour le convertir d'un document de constatations d'audit en un plan d'implémentation découpé en 5 phases actionnables.
  - **Adaptation IFTTT** : Redéfinition des tâches S-03 (SSRF) et A-01 (cascade IFTTT) vers le nettoyage de documentation et l'audit de code mort, suite à la suppression préalable d'IFTTT.
  - **Fichiers Liés** : Tâches documentées avec leurs chemins absolus, détails d'implémentation et critères d'acceptation de test précis.
- **[2026-07-12 12:18:00] - Intégration et Configuration de l'écosystème Codex**
  - **Règles Déclaratives** : Création de `.codex/rules/development.rules` en Starlark pour pré-approuver les commandes de développement (activation venv, pytest, git, python, ripgrep) sans invites répétitives.
  - **Instructions Hiérarchiques** : Division des instructions pour rester dans le budget de 32 KiB, avec un `AGENTS.md` à la racine pour les règles système globales et un `tests/AGENTS.md` spécifique à la stratégie de test.
  - **Guide d'Intégration** : Rédaction d'un guide complet `docs/codex/integration-guide.md` comparant la sécurité Windsurf vs Codex, détaillant la compatibilité des skills Open Agent Skills et la configuration locale.
  - **Correction Test** : Correction du test unitaire `test_quota_refresh_route_makes_api_call` (authentification de session manquante), rendant la suite de 164 tests de nouveau verte à 100%.

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
- Aucun (Toutes les tâches de remédiation frontend planifiées sont complétées et validées).

## À faire / Backlog Frontend
- [ ] **Phase F2.4** : Bootstrap purge (PurgeCSS) — DIFFÉRÉ (nécessite validation visuelle étendue sur tous les composants).

## Étapes Futures (Hors Scope Immédiat)
- Subsetting Font Awesome solid (~15 icônes → ~30 Ko WOFF2).
- Migration CSS inline → nonces CSP pour éliminer `'unsafe-inline'`.
- Implémentation d'un thème clair (`prefers-color-scheme: light`).

