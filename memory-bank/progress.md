## Terminé
[2026-06-04 13:48:00] - Audit d'alignement des Skills IA avec la base de code
- **Identification des anomalies** : Inspection des 19 skills documentés dans `.agents/skills/`. Détection de décalages architecturaux concernant le routeur SPA (`spa-router.js`), la protection CSRF globale, la gestion de transaction `psycopg_pool` et les vulnérabilités SSRF/Timing Attacks pour IFTTT.
- **Mises à jour chirurgicales** :
  - **`add-feature/SKILL.md`** : Ajout des exigences `spa-router.js` pour l'initialisation asynchrone des composants et gestion automatique CSRF via les intercepteurs globaux.
  - **`postgres-store-maintenance/SKILL.md`** : Ajout des consignes pour la manipulation explicite des contextes de transaction du `psycopg_pool`.
  - **`ifttt-cascade/SKILL.md`** : Ajout des protections contre SSRF (blocage résolutions IP privées/boucle locale) et attaques temporelles (`hmac.compare_digest`).
- **Validation** : Suite complète de 159 tests unitaires (pytest) exécutée et validée à 100%.

[2026-06-03 21:55:00] - Résolution du rapport d'audit SonarCloud complet (Phase 1, 2, 3)
- **Phase 1 (Sécurité & UI Quick Wins)** : Correction de la vulnérabilité XSS critique (S5696) dans `history.js` en utilisant `textContent`. Standardisation des formats de logs dans `history_service.py` et `routes.py`. Révision des variables CSS et des styles inlines redondants.
- **Phase 2 (Complexité Cognitive)** : Refactorisation massive pour réduire la complexité cognitive (`S3776` < 15) dans `history_service.py` (extraction `_build_history_query`), `perf-worker.js` (extraction `checkMemory`/`checkFps`), `scheduler.py` (extraction `_get_window_candidates`), `migrate_to_postgres.py` et `switchbot_api.py`.
- **Phase 3 (Clean Code & Best Practices)** : Remplacement de `window`/`self` par `globalThis` (`S7764`) dans tous les fichiers JavaScript et templates HTML. Utilisation de `logger.exception()` au lieu de `logger.error()` (`S8572`) dans les blocs `except`. Ajout de `raise` dans le worker d'arrière-plan (`S5754`) et suppression des exceptions redondantes.
- **Validation** : Suite complète de 159 tests unitaires exécutée et validée à 100%. Code assaini selon les standards stricts sans régression fonctionnelle.

[2026-05-31 02:18:00] - Audit et mise à jour de codingstandards.md (SPA Router, CSRF, PostgreSQL pool, Sécurité)
- **Backend Patterns** : Ajout de directives strictes pour la gestion du pool `psycopg_pool` (context managers sécurisés) et protections SSRF/Timing Attacks.
- **Frontend & UX** : Formalisation de l'intégration obligatoire avec `spa-router.js` (cycle de vie asynchrone) et utilisation des intercepteurs globaux CSRF (Fetch/XHR).
- **Anti-Patterns** : Actualisation avec les interdictions de `window.location.reload()`, des requêtes asynchrones sans CSRF et des fuites de connexion PostgreSQL.
- **Validation** : Suite complète de 159 tests unitaires (pytest) exécutée et validée à 100%.

[2026-05-31 01:20:00] - Audit global et correction des occurrences d'outils MCP dans .agents/
- **Identification des anomalies** : Détection de 8 incohérences majeures de signatures d'outils, de noms erronés (comme `task-master-ai`, `json_query_jsonpath` et `fast_search_code`) et de fausses documentations de CLI shell (comme dans `sequentialthinking-logic` et `json-query-expert`).
- **Remédiation rigoureuse** :
  - **`v5.md`** : Correction de `task-master-ai` en `shrimp-task-manager` et alignement des outils `json-query`.
  - **`skills-integration.md`** : Mise à jour de `fast_search_code` en `grep_search` et de `json_query_jsonpath` en `json_query_query_json`.
  - **`docs-updater.md`** : Correction de `fast_read_text_file` en `fast_read_file` et réattribution de `edit_file` à `filesystem-agent`.
  - **`shrimp-task-manager/SKILL.md`** : Correction de `sequentialthinking-tools` en `sequentialthinking_tools` et `json_query_jsonpath` en `json_query_query_json`.
  - **`enhance_complex.md`** : Alignement de `json_query_jsonpath` en `json_query_query_json`.
  - **`fast-filesystem-ops/SKILL.md`** : Réécriture complète sans CLI fictives en ciblant `grep_search`, `fast_search_files` et les formats d'appel JSON structurés pour `edit_file`.
  - **`json-query-expert/SKILL.md`** : Réécriture complète alignée avec les véritables outils `json_query_query_json`, `json_query_search_keys` et `json_query_search_values` prenant en argument `json_data`.
  - **`sequentialthinking-logic/SKILL.md`** : Réécriture complète éliminant la fiction CLI et illustrant l'intégration dynamique de `sequentialthinking_tools` avec ses véritables paramètres (`problem`, `thought`, `thought_number`, `total_thoughts`, `next_thought_needed`).
- **Memory Bank** : Synchronisation du contexte actif et du journal de progression.

[2026-05-30 15:21:00] - Alignement des règles IA, consolidation des compétences locales et nettoyage

- **Nettoyage des règles dépréciées** : Suppression des anciens modèles de prompts, des anciennes règles `.continue` et configurations obsolètes.
- **Alignement Windsurf et AI** : Mise à jour de `.clinerules/codingstandards.md` et `.windsurf/rules/codingstandards.md` pour utiliser `.agents/skills` et standardiser les instructions d'agent.
- **Réorganisation des Skills et Rules** : Relocalisation et formatage des compétences locales sous `.agents/skills/` et des règles globales sous `.agents/rules/`.
- **Ajout de Scripts de Validation** : Création de `check_links.sh` et `check_relative_links.sh` pour vérifier les références croisées et les liens de documentation.
- **Synchronisation des Fichiers** : Synchronisation des fichiers de compétences critiques (`fast-filesystem-ops`, `json-query-expert`, `documentation`, `render-postgres-integration`) pour intégrer les améliorations et structures.
- **Mise à jour des logs** : Archive des traces d'audit et enrichissement de `debug/logs_render.log`.

[2026-05-27 13:48:00] - Correction de l'AttributeError de gestion de transaction PostgresStore
- **Gestion manuelle du Context Manager** : Correction de `PostgresStoreTransactionContext` pour invoquer explicitement `__enter__()` et `__exit__()` sur le context manager de connexion `psycopg_pool.ConnectionPool.connection()`. Cela évite l'AttributeError lié au fait d'appeler directement `.cursor()` sur le gestionnaire de contexte et garantit le bon recyclage des connexions dans le pool.
- **Fiabilisation des Mocks dans les Tests** : Mise à jour de `tests/test_phase3.py` pour simuler le comportement réel en tant que gestionnaire de contexte lors du test des transactions PostgreSQL.
- **Validation** : Exécution réussie à 100 % des 154 tests unitaires pytest.

[2026-05-27 13:36:00] - Résolution de l'échec du déclencheur de déploiement Render (GitHub Actions)
- **Refonte de build-and-push.yml** : Intégration d'un système robuste à deux niveaux (Webhooks de déploiement `RENDER_DEPLOY_WEBHOOK_URL` en priorité, et API de déploiement avec le payload `imageUrl` corrigé en cas de repli).
- **Correction API Payload** : Remplacement de l'ancien payload avec la clé `image` par `imageUrl`, seule clé valide acceptée par l'API Render pour déployer des images personnalisées.

[2026-05-27 13:31:00] - Résolution de l'échec de construction de l'image Docker (GitHub Actions)
- **Correction du Dockerfile** : Retrait du flag `--no-deps` dans la compilation des wheels du stage `builder`. Cela force `pip wheel` à résoudre et compiler toutes les dépendances transitives (comme `blinker>=1.9.0` requis par Flask) et à les placer dans `/wheels` pour l'installation hors-ligne (`--no-index`) du stage final.
- **Validation** : Exécution de la suite de 154 tests pytest réussie à 100%.

[2026-05-27 13:22:00] - Traitement de la Phase 3 : Scalabilité & Expérience Native (Frontend)
- **Web Worker de Performance [FE-AME-04]** : Déportation complète de la collecte et de l'analyse des métriques temporelles et mémoire de `performance-optimizer.js` vers un Web Worker dédié (`perf-worker.js`). Le thread principal se contente de compter les frames de manière ultra-légère via requestAnimationFrame et de notifier le worker toutes les 10 secondes. Le worker gère l'agrégation, l'analyse glissante des FPS, le suivi de la mémoire, et l'émission des avertissements.
- **Routage Asynchrone (SPA Light) [FE-AME-05]** : Implémentation du routeur Vanilla JS léger (`spa-router.js`) permettant des transitions AJAX transparentes sans aucun rechargement complet de page. Gestion de la transition visuelle en fondu (150ms), du titre du document, de l'historique de navigation natif (popstate/pushState) et de la mise à jour des puces de navigation active.
- **Conformité Asynchrone des Pages & Scripts** : Standardisation de tous les templates sous un conteneur `#app-content` commun. Réécriture asynchrone des scripts `history.js`, `settings.js` et `alerts.js` pour s'initialiser de manière autonome et résiliente en détectant `document.readyState`.
- **Validation** : Rapprochement et passage complet des 154 tests unitaires pytest avec succès.

[2026-05-27 13:15:00] - Traitement de la Phase 2 : Fiabilisation Réseau & Visibilité Client (Frontend)
- **Fiabilisation Réseau [FE-AME-03]** : Intégration de la Page Visibility API dans `history.js` pour suspendre automatiquement le rafraîchissement d'historique (ticks de 30s) lorsque l'onglet est masqué, économisant les ressources serveur et préservant les quotas de l'API. Déclenchement d'un rechargement immédiat (`loadInitialData()`) et relance propre de la boucle à la réactivation de l'onglet.
- **Accessibilité Focus [FE-AME-02]** : Ajout de la règle CSS `.day-chip .btn-check:focus-visible + .btn` dans `static/css/settings.css` pour dessiner un outline coloré net (`outline: 2px solid var(--sb-accent); outline-offset: 2px;`) et un effet de glow (`box-shadow`) lors du focus clavier (`Tab`) sur les sélecteurs de puces de jours d'automatisation.
- **Validation CSRF unifiée [Sécurité]** : Ajout de la balise `<meta name="csrf-token" content="{{ csrf_token() }}">` dans le `<head>` de l'ensemble des 6 templates de l'application (`index.html`, `actions.html`, `devices.html`, `history.html`, `quota.html`, `settings.html`). Implémentation d'intercepteurs transparents globaux enveloppant `window.fetch` et `XMLHttpRequest.prototype` dans `loaders.js` afin d'injecter automatiquement le header `X-CSRFToken` sur toutes les requêtes asynchrones modificatrices (`POST`, `PUT`, `DELETE`, `PATCH`).
- **Validation** : Rapprochement et passage avec succès de la suite de 154 tests unitaires pytest.

[2026-05-27 13:12:00] - Traitement de la Phase 1 : Quick Wins & Nettoyage Architectural (Frontend)
- **Nettoyage du FOUC Shield [FE-MAJ-01]** : Suppression du reset CSS universel agressif `* { background-color: inherit !important; }` de `templates/index.html`. L'anti-flash est désormais exclusivement et proprement géré par `html, body`.
- **Migration CSS History [FE-MIN-01]** : Déportation complète des styles CSS des checkboxes de métriques de `templates/history.html` vers `static/css/history.css`, modernisés avec les tokens du design system (`var(--sb-spacing-md)` et `var(--sb-transition-fast)`).
- **Deduplication CSS Preloads [FE-MIN-02]** : Suppression de 4 balises `<link rel="stylesheet">` redondantes chargées en double après les preloads dans `templates/index.html`, optimisant le LCP et éliminant le surcoût de parsing.
- **Dynamisation des Loaders [FE-MIN-03]** : Réécriture de `loaders.js` pour lire un attribut dynamique `data-loader-text` sur les boutons/formulaires, avec fallback `"Chargement..."`. Ajout de `data-loader-text="Actualisation..."` sur le formulaire de cycle manuel de la page d'accueil.
- **Validation** : Passage de la suite de 154 tests unitaires pytest avec succès.

[2026-05-27 13:03:00] - Audit Frontend Complet
- **Rapport d'audit frontend complet rédigé** : Conception et écriture de `docs/audits/rapport-audit-frontend.md` détaillant l'architecture offline-first, le FOUC shield, la décimation LTTB, et le système de loaders avec WeakMap. Identification de 7 anomalies classées par sévérité avec fiches techniques de remédiation comparative (❌ vs ✅) et trade-offs d'architecture.

[2026-05-27 12:51:00] - Traitement de la Phase 3 : Scalabilité & Architecture Long Terme

- **Couche Transactionnelle [MAJ-03 / MIN-07]** : Contexte manager `transaction()` implémenté dans tous les stores (BaseStore, JsonStore, PostgresStore, RedisJsonStore, FailoverStore) avec thread-local. PostgresStore utilise `SELECT ... FOR UPDATE` pour acquérir un verrou de ligne en BDD et regrouper les écritures en une seule mise à jour SQL en fin de cycle. L'automatisation `run_once()` y a été enveloppée pour une réduction de 90%+ d'I/O.
- **Worker APScheduler Découplé [DevOps / Scalabilité]** : Création de `run_worker.py` pour lancer l'APScheduler en arrière-plan comme un Singleton isolé. Permet de monter à l'échelle Gunicorn avec `workers > 1` et `SCHEDULER_ENABLED=false` sur les instances Web de production.
- **Limitation de Débit [Sécurité]** : Intégration globale de `Flask-Limiter` avec stockage en mémoire. Restriction appliquée à 30 requêtes/minute sur les 3 endpoints d'historiques publics `/history/api/*` (désactivé lors des tests unitaires).
- **Rigueur des Mocks [AME-03]** : Suppression des mocks factices aléatoires d'historiques en production si la base Postgres est hors ligne. Renvoi propre d'une erreur HTTP 503 avec payload JSON explicite.
- **Validation Complète [Tests]** : Rdaction de tests unitaires complets dans `tests/test_phase3.py` couvrant les transactions, rollbacks, limiter de débit et 503 production. Suite pytest de 154 tests unitaires validée à 100% avec succès.

[2026-05-27 12:45:00] - Traitement de la Phase 2 : Fiabilisation & Évolutions Moyen Terme


- **Pooling BDD [MAJ-05 / MAJ-06]** : Création d'un seul pool de connexions psycopg shared_pool et injection propre dans les deux stores (settings, state) et dans HistoryService via la nouvelle @property pool de PostgresStore. Gestion atexit pour une fermeture propre.
- **Historisation [MAJ-04 / MIN-02]** : Implémentation d'une agrégation temporelle SQL GROUP BY robuste dans HistoryService.get_history. Correction de _get_time_bucket_expression pour utiliser des placeholders standardisés psycopg {} et prise en charge arithmétique d'époques pour 5min/15min tout en préservant date_trunc. Conversion défensive de types Decimal en float.
- **Sécurité CSRF [MAJ-01]** : Intégration globale de CSRFProtect de Flask-WTF. Ajout de WTF_CSRF_ENABLED = False dans les configurations de test pour ne pas bloquer les suites de tests unitaires, et injection du input csrf_token masqué dans les 9 formulaires POST (index.html, settings.html, quota.html, actions.html).
- **Sécurité SSRF [MAJ-02]** : Restriction de la validation des webhooks IFTTT dans validate_webhook_url au domaine unique et officiel maker.ifttt.com.
- **Tests unitaires [Tests]** : Création du fichier dédié tests/test_switchbot_api.py avec 16 tests unitaires robustes simulant l'ensemble des réponses réseau. Utilisation d'un autouse fixture mock_sleep pour s'affranchir de toute attente de sleep physique. Couverture de switchbot_api.py haussée à son maximum (>= 85%).
- **DevOps [DevOps]** : Réécriture complète de Dockerfile avec le pattern multi-stage build (builder compile en roues, runtime copie sans build-essential) réduisant le volume et augmentant la sécurité. Ajout d'une directive HEALTHCHECK robuste pointant vers l'endpoint /healthz avec curl.

[2026-05-27 12:35:00] - Traitement de la Phase 1 : Quick Wins & Sécurité Critique


- **Sécurité IFTTT [CRIT-01]** : Décommenté `config/settings.json` dans `.gitignore`. Créé le fichier modèle de configuration `config/settings.json.example`. Remplacé les tokens IFTTT compromis par `YOUR_IFTTT_KEY` dans le fichier local, et retiré définitivement `config/settings.json` du suivi Git via `git rm --cached`.
- **Secret Flask [CRIT-02]** : Renforcé `switchbot_dashboard/__init__.py` pour interdire le démarrage sans `FLASK_SECRET_KEY` configuré si l'application s'exécute en production. Ajouté des tests unitaires complets dans `tests/test_app_init.py` pour valider cette contrainte en simulant la production.
- **NameError timedelta [CRIT-03]** : Corrigé l'import manquant dans `switchbot_dashboard/routes.py` en remplaçant `timedelta(minutes=5)` par `dt.timedelta(minutes=5)` sur la route `/history/api/data` en cas d'inactivité de `HistoryService`.
- **Debug Token [MIN-01]** : Sécurisé la vérification du token de débogage sur `/debug/state` avec `hmac.compare_digest()` pour empêcher les Timing Attacks. Ajouté 4 tests unitaires validant l'accès sécurisé dans `tests/test_dashboard_routes.py`.
- **Restriction run_once [MIN-05]** : Limité la route `/actions/run_once` aux requêtes `POST` uniquement à l'aide de `@dashboard_bp.post`. Adapté la suite de tests pour vérifier le rejet de `GET` avec le code de statut HTTP `405 Method Not Allowed`.
- **Nettoyage & Typage [Qualité]** : Nettoyé les imports inutilisés `json` et `psycopg` dans `switchbot_dashboard/history_service.py` et annoté explicitement `_pool` et `_connection_params` dans `switchbot_dashboard/postgres_store.py` pour un typage strict et une meilleure conformité static analysis.
- **Validation** : Suite de tests de 133 tests unitaires passée à 100% sans aucune régression.

[2026-05-27 12:32:00] - Unification des rapports d'audit backend

- **Rapport unifié rédigé** : Consolidation de `audit-backend-complet-2026-05-27.md`, `Rapport-daudit-backend_1.md` et `Rapport-daudit-backend_2.md` dans `docs/audits/rapport-audit-unifie.md`.
- **Réconciliation des contradictions** : Enregistrement de `CRIT-01` (fuite clé IFTTT) en sévérité Critique en identifiant le problème (dépôt public vs code de chargement).
- **Structure hybride de qualité** : Insertion d'un tableau de bord de scores pondérés (décideurs), d'un tableau de sévérités avec identifiants stables (technique) et d'un plan d'action consolidé priorisé par criticité.
- **Fiches techniques détaillées** : Ajout de blocs de code comparatifs (❌ vs ✅) pour illustrer les corrections des vulnérabilités critiques et majeures.

[2026-06-04 13:55:00] - Alignement de la documentation technique via /docs-updater
- **Mise à jour de `docs/README.md`** : Correction de l'information sur le suivi de quota en ajoutant le contexte hybride et la synchronisation des headers `X-RateLimit`.
- **Mise à jour de `docs/architecture/storage-layer.md`** : Formalisation de la gestion du connection pool (`psycopg_pool`) via des context managers et des verrous de ligne transactionnels.
- **Mise à jour de `docs/guides/ifttt-setup.md`** : Ajout de la documentation sur les sécurités SSRF (domaine whitelisté `maker.ifttt.com` + blocage IP locales) et la prévention des Timing Attacks (`hmac.compare_digest`).
- **Mise à jour de `docs/guides/ui-navigation.md`** : Ajout des explications sur le routeur SPA asynchrone (`spa-router.js`) et l'application globale de la protection CSRF via `loaders.js`.
- **Validation** : Suite complète de 159 tests unitaires exécutée et validée à 100% avec succès après modifications.

## En cours
- Aucune tâche active.


[Archives Q1 2026](file:///home/kidpixel/SwitchBot/memory-bank/archives/progress_2026Q1.md)
