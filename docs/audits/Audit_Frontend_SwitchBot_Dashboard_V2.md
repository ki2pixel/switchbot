L'audit frontend multidimensionnel de l'application SwitchBot Dashboard v2 met en évidence une architecture orientée performance et sécurité (protection CSRF globale, en-têtes Content Security Policy stricts, design dark glassmorphism modulaire), mais révèle plusieurs écarts architecturaux et anomalies techniques entre les spécifications des référentiels internes, le backend Flask et les composants statiques.

*Note méthodologique sur le périmètre d'inspection* : L'archive du projet fournie est tronquée au milieu de la feuille de style history.css. L'analyse ci-dessous couvre exhaustivement l'arborescence complète des 119 fichiers, le code Python d'initialisation et de routage, les feuilles CSS visibles (actions.css, devices.css, history.css) ainsi que les contrats d'interface liant le backend aux scripts JavaScript et aux templates Jinja2.

## 1. Inventaire et cartographie des assets & Conformité Offline-First

### Cartographie des templates et composants statiques

L'inspection de l'arborescence du dépôt permet de recenser précisément les ressources frontend suivantes :

* **Templates Jinja2** (9 fichiers dans le dossier templates) :
* 503.html : page d'erreur rendue lors d'une défaillance de stockage.


* _footer_nav.html : composant partiel de barre de navigation mobile sticky.


* actions.html : vue dédiée aux déclencheurs manuels et aux scènes climatisation.


* devices.html : vue d'inventaire et d'état temps réel des équipements SwitchBot.


* history.html : tableau de bord de télémétrie et de graphiques historiques.


* index.html : tableau de bord principal et résumé d'état.


* login.html : formulaire d'authentification par mot de passe.


* quota.html : vue détaillée de consommation des quotas API SwitchBot.


* settings.html : interface de paramétrage de l'automatisation et des profils thermiques.




* **Feuilles de style CSS** (8 fichiers dans le dossier static/css) :
* actions.css, devices.css, history.css, index.css, settings.css, sticky-cards.css, sticky-footer.css et theme.css.




* **Scripts JavaScript** (6 fichiers dans le dossier static/js) :
* alerts.js, devices.js, history.js, loaders.js, settings.js et spa-router.js.




* **Suites de tests frontend** (4 fichiers dans le dossier tests) :
* test_frontend_accessibility.py, test_frontend_loaders.py, test_frontend_performance.py et test_frontend_spa.py.





### Vérification de la politique Offline-First

* **Absence du répertoire static/vendor dans l'arborescence versionnée** : Bien que les référentiels techniques imposent de servir Bootstrap, FontAwesome, Chart.js et la police Space Grotesk depuis le dossier static/vendor, ce répertoire ne figure pas dans l'arborescence des 119 fichiers du projet. Or, le fichier Dockerfile exécute uniquement l'installation des roues Python et copie le répertoire courant sans étape de téléchargement d'assets frontaux. Si le dossier static/vendor est ignoré par Git ou absent lors du build de l'image Docker, l'application subira des erreurs 404 sur toutes ses dépendances tierces en production.


* **Fichiers d'optimisation référencés mais absents** : Les référentiels internes mentionnent l'existence des fichiers critical.css, performance-optimizer.js et advanced-optimizer.js, mais aucun de ces trois fichiers n'est présent dans les répertoires static/css et static/js.


* **Verrouillage réseau par Content Security Policy (CSP)** : Dans le fichier d'initialisation de l'application Flask, le hook `@app.after_request` applique l'en-tête suivant sur chaque réponse HTTP :
`default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; font-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`.
Cette directive bloque au niveau du navigateur toute tentative de chargement de script, feuille de style, police ou requête AJAX vers un CDN externe HTTP/HTTPS, garantissant techniquement qu'aucune fuite vers un CDN tiers ne peut s'exécuter silencieusement. Aucune règle `@import` externe n'est présente dans les feuilles CSS inspectées.



## 2. Audit de l'architecture JavaScript & SPA Router

### Gestion de la navigation, des erreurs réseau et du cycle de session

* **Collision entre l'expiration de session (Redirection 302) et le fetch SPA** : La durée de vie de la session est configurée à 30 minutes (`PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)`). Dans le middleware `check_auth()`, lorsque la session a expiré, seules les requêtes ciblant `/history/api/` reçoivent un code HTTP 401 en JSON ; toutes les routes de pages HTML renvoient une redirection HTTP 302 vers la route de connexion. Lors d'une navigation interceptée par spa-router.js via `fetch()`, l'API Fetch suit nativement la redirection 302 et retourne une réponse `200 OK` contenant le HTML de login.html. Si spa-router.js ne contrôle pas la propriété `response.redirected` ou l'URL finale `response.url`, le formulaire de connexion est injecté dans le conteneur partiel alors que `history.pushState` conserve l'URL de la page protégée.


* **Gestion des erreurs HTTP 429 et 503 lors du routage partiel** :
* La route GET `/devices` est soumise à une limitation stricte de débit (`@limiter.limit("10 per minute")`). Une navigation SPA rapide entre les onglets dépassant 10 requêtes par minute reçoit une réponse HTTP 429 de Flask-Limiter.


* En cas d'indisponibilité de la base de données (`StoreError`), le gestionnaire d'erreurs global renvoie la vue HTML 503.html avec un code HTTP 503 pour toute requête n'ayant pas l'en-tête `Accept: application/json`. Le routeur SPA doit impérativement vérifier `response.ok` avant de muter le DOM.




* **Latence synchrone sur la transition vers la vue des appareils** : La route `/devices` appelle `client.get_devices()` puis instancie un `ThreadPoolExecutor(max_workers=4)` pour interroger séquentiellement le statut de chaque appareil via `client.get_device_status(device_id)` avant de générer le template. En navigation SPA, cette attente bloque la résolution de la promesse `fetch()` pendant plusieurs secondes.



### Ré-initialisation des pages (`window.init*`) et prévention des fuites mémoire

* **Accumulation d'écouteurs globaux** : Le pattern d'architecture impose l'encapsulation asynchrone des fonctions d'initialisation de page (telles que `window.initSettings`) appelées dynamiquement par spa-router.js à chaque transition. Si ces fonctions attachent des écouteurs sur `window` (comme l'événement `resize` pour adapter les graphiques dans history.js) ou sur `document` sans `AbortController` ni nettoyage au démontage de la vue précédente, les écouteurs se dupliquent à chaque navigation.


* **Destruction des instances Chart.js** : Lors des allers-retours SPA sur la vue historique, toute instance existante de Chart.js rattachée au canvas doit être explicitement détruite via `.destroy()` avant d'instancier un nouveau graphique, sous peine de fuite mémoire du contexte WebGL/Canvas 2D et de superposition d'événements de survol.



### Contrôle de l'intercepteur CSRF global

* **Protection universelle activée** : `CSRFProtect` est initialisé globalement sur l'application Flask.


* **Risque de désynchronisation du token CSRF après reconnexion** : Lors d'un POST réussi sur `/login`, le backend effectue une rotation de session (`session.clear()`) pour prévenir la fixation de session. Si le token CSRF est lu par l'intercepteur Fetch/XHR depuis une balise `<meta name="csrf-token">` située dans le `<head>` et que spa-router.js ne met à jour que le corps de la page lors des transitions, le token en mémoire devient invalide après une reconnexion sans rechargement complet.



## 3. Audit du système de Loaders et de l'accessibilité UX

### Couverture des formulaires et déclencheurs avec `data-loader`

Le backend expose 10 routes POST soumises à validation CSRF et limitation de débit (`Flask-Limiter`) qui doivent obligatoirement comporter l'attribut `data-loader="submit"` dans leurs templates respectifs, ainsi qu'un import de loaders.js :

1. `POST /settings` (limité à 5 par minute) dans settings.html.


2. `POST /quota/refresh` (limité à 5 par minute, exécute un appel réseau `get_devices()`) dans quota.html.


3. `POST /login` et `POST /logout` dans login.html et les barres de navigation.


4. `POST /actions/run_once` (lance un thread d'automatisation en arrière-plan) dans index.html et actions.html.


5. `POST /actions/aircon_off`, `POST /actions/aircon_on`, `POST /actions/aircon_on_winter`, `POST /actions/aircon_on_summer`, `POST /actions/aircon_on_fan` et `POST /actions/quick_off` (exécutent des appels API SwitchBot synchrones avec prise de verrou `_acquire_lock()`) dans index.html et actions.html.



* **Synchronisation entre loaders.js et spa-router.js** : Le mécanisme de failsafe de 15 secondes et l'attribut `aria-busy="true"` sur l'élément racine doivent être nettoyés via `clearTimeout` dès qu'une transition SPA se termine, afin qu'un timer résiduel de 15 secondes issu d'une action précédente ne masque pas prématurément un nouveau loader déclenché quelques secondes plus tard.



### Accessibilité ARIA et contrastes en mode Dark Glassmorphism

* **Incohérence critique des variables CSS (Tokens) dans history.css** :
* Les feuilles actions.css et devices.css utilisent la nomenclature de tokens `--sb-text`, `--sb-muted`, `--sb-card`, `--sb-card-border`, `--sb-outline` et `--sb-accent`.


* En revanche, history.css utilise une nomenclature différente : `--sb-text-primary`, `--sb-text-secondary`, `--sb-text-muted`, `--sb-border-color`, `--sb-surface`, `--sb-surface-elevated` et `--sb-primary`.


* Si ces variables secondaires ne sont pas toutes déclarées comme alias dans theme.css, les textes des cartes de statut (`.status-card__value`, `.status-card__label`, `.status-card__unit`) et des filtres (`.form-check-label`) héritent de la couleur par défaut du navigateur, rendant le texte illisible sur le fond sombre et violant le ratio de contraste WCAG AA (4.5:1).




* **Indicateurs de focus clavier (`:focus-visible`) insuffisants ou absents** :
* Dans actions.css, les classes `.action-btn` et `.scene-btn` définissent des styles `:hover` (`transform: translateY(-2px)` et `box-shadow`), mais aucun style `:focus-visible` n'est prévu pour la navigation au clavier.


* Dans devices.css, `.btn-copy:focus-visible` applique uniquement `background: rgba(255, 255, 255, 0.08)` sans contour visible (`outline`), ce qui offre un contraste inférieur au seuil minimal de 3:1 exigé par WCAG 2.2.




* **Pollution vocale des lecteurs d'écran par les pseudo-éléments CSS** : Dans devices.css, les accordéons `.device-details summary::after` et `.raw-block summary::after` injectent le caractère `content: '▶'`. Le contenu textuel généré en CSS étant lu par les technologies d'assistance en plus de l'état natif de la balise `<details>`, il est préférable d'utiliser une icône SVG portant `aria-hidden="true"` ou une bordure CSS géométrique.



## 4. Audit de performance & Core Web Vitals

### Séparation Critical CSS et animations CSS

* **Utilisation prohibée de `transition: all**` :
* Alors que le référentiel de performance impose de restreindre les transitions aux seules propriétés composites (`transform` et `opacity`), on relève `transition: all 0.2s ease` dans actions.css (sur `.action-btn, .scene-btn`) et `transition: all var(--sb-transition-normal) ease` dans devices.css (sur `.device-details` et `.raw-block`).


* De plus, devices.css anime la propriété géométrique `left` de `-100%` à `100%` sur les pseudo-éléments `.device-details::before` et `.raw-block::before` (`transition: left var(--sb-transition-slow) ease`), ce qui déclenche des opérations de Layout et de Paint sur le thread principal au lieu d'utiliser `transform: translateX()` sur le GPU.




* **Sur-allocation de couches GPU (Layer Explosion)** : Dans actions.css, la règle `.action-btn, .scene-btn, .status-item` force `transform: translateZ(0)`, `backface-visibility: hidden` et `perspective: 1000px` en permanence, combinée à `backdrop-filter: blur(20px)` sur chaque `.status-item`. Sur un appareil mobile modeste, l'empilement de multiples surfaces `backdrop-filter: blur(20px)` promues en couches 3D permanentes dégrade fortement le temps de trame (INP/FID) lors du défilement.


* **Respect partiel de `prefers-reduced-motion**` :
* La feuille actions.css désactive correctement les transitions et transformations lorsque `@media (prefers-reduced-motion: reduce)` est actif.


* En revanche, devices.css et le début de history.css ne contiennent aucune règle `@media (prefers-reduced-motion: reduce)` : les animations de balayage lumineux (`::before`), les rotations d'accordéons et les élévations au survol (`.status-card:hover { transform: translateY(-2px); }`) restent actives malgré la préférence système de l'utilisateur.





### Graphiques Chart.js et décimation LTTB

* **Inversion de l'ordre chronologique SQL pour la décimation LTTB** : Dans history_service.py, la méthode `get_history()` exécute la requête PostgreSQL avec un tri décroissant : `ORDER BY timestamp DESC LIMIT %s`. Or, le plugin natif de décimation **LTTB (Largest Triangle Three Buckets)** de Chart.js requiert impérativement un jeu de données trié par ordre chronologique **croissant (`ASC`)** avec des coordonnées `x` numériques (timestamps epoch en millisecondes). Si history.js ne retourne pas le tableau (`.reverse()`) et ne convertit pas les dates ISO en millisecondes avant de les passer au dataset Chart.js, la décimation LTTB ne s'active pas ou fausse le tracé.


* **Divergence de nommage d'endpoint API** : La checklist du skill history-dashboard-updater mentionne l'endpoint `GET /history/api/records?minutes=360`, tandis que routes.py expose en réalité `GET /history/api/data` avec les paramètres `start`, `end`, `metrics`, `granularity` et `limit`.



## 5. Audit de sécurité frontend & hygiène du code

### Politique CSP et prévention des injections DOM (XSS)

* **Présence de `'unsafe-inline'` dans `script-src**` : La politique CSP définie dans `set_security_headers` (`script-src 'self' 'unsafe-inline'`) autorise l'exécution de scripts inline. Si cette configuration facilite le chargement asynchrone des feuilles CSS (`onload`) et les scripts d'initialisation dans les templates, elle affaiblit le second rideau de défense contre les failles XSS. Le respect absolu de l'interdiction de `innerHTML` et `insertAdjacentHTML` avec des données non nettoyées dans les 6 fichiers JS (notamment lors du rendu des cartes d'appareils dans devices.js, des alertes dans alerts.js et des lignes d'historique dans history.js) est donc critique.



### Gestion défensive des erreurs API et intégrité des données History

* **Rupture du pattern Fail-Safe UX en production sans PostgreSQL** : Lorsque `history_service` vaut `None` (cas où PostgreSQL est indisponible et l'application a basculé sur le fallback `JsonStore`), les trois routes `/history/api/data`, `/history/api/aggregates` et `/history/api/latest` renvoient une erreur HTTP 503 (`{"error": "Service Historique indisponible..."}`) dès lors que l'application n'est ni en mode `debug` ni en mode `testing`. Ce comportement contredit le standard du projet qui exige de toujours retourner une structure de données vide (`"data": []`) pour ne jamais faire planter l'interface graphique.


* **Bogue de sérialisation ISO 8601 (`+00:00Z`) dans les données de secours et `/healthz**` :
* Dans routes.py, les fonctions `_generate_mock_history_data()`, `history_api_data()`, `history_api_latest()` et `healthz()` construisent des objets `datetime` déjà dotés du fuseau UTC (`dt.timezone.utc`), puis concatènent manuellement `"Z"` au résultat de `.isoformat()` (`current.isoformat() + "Z"`).


* Comme `.isoformat()` sur un objet conscient du fuseau UTC génère déjà le suffixe `+00:00`, la chaîne résultante prend la forme invalide `2026-11-04T12:00:00+00:00Z`. En JavaScript, `new Date("...+00:00Z")` retourne `Invalid Date` (`NaN`), ce qui provoque l'échec du rendu de l'axe temporel dans Chart.js.




* **Trous de données historiques hors fenêtres d'automatisation** : Dans automation.py, l'appel `self._history_service.record_state(current_state, timezone_name)` est placé tout à la fin de `_run_once_impl()`, après les retours anticipés (`return`) exécutés lorsque `automation_enabled` est `False` ou lorsque l'heure courante est hors des créneaux horaires (`not in_window`). Bien que le capteur soit interrogé (`self.poll_meter()`) durant ces périodes, aucune donnée n'est enregistrée dans `state_history`, créant des plages vides de plusieurs heures sur les graphiques de history.html.


* **Écart de durée de rétention** : Le fichier d'initialisation instancie `HistoryService` avec `retention_hours=24`, alors que les standards d'architecture, la documentation SQL et la valeur par défaut de la classe stipulent une rétention de 6 heures alignée sur Neon PITR.



## 6. Synthèse et matrice de recommandations

### Synthèse des constats par niveau de sévérité

| ID | Composant | Catégorie | Sévérité |
| --- | --- | --- | --- |
| AUD-01 | static/vendor et Dockerfile | Offline-First & Build | Critique |
| AUD-02 | routes.py (Dates ISO) | Intégrité JS / Chart.js | Critique |
| AUD-03 | routes.py et spa-router.js | Auth & Navigation SPA | Majeur |
| AUD-04 | history.css et theme.css | Accessibilité & Tokens CSS | Majeur |
| AUD-05 | automation.py (History) | Complétude des données | Majeur |
| AUD-06 | routes.py (API History 503) | Résilience Fail-Safe UX | Majeur |
| AUD-07 | devices.css et history.css | Accessibilité (Reduced Motion) | Mineur |
| AUD-08 | actions.css et devices.css | Performance CSS & Focus | Mineur |
| AUD-09 | **init**.py (CSP & Rétention) | Sécurité & Conformité | Suggestion |

* **AUD-01 (Critique)** : L'absence du dossier static/vendor dans l'arborescence versionnée combinée à l'absence d'étape de récupération des librairies frontales dans le Dockerfile expose le déploiement conteneurisé à l'indisponibilité de Bootstrap, FontAwesome, Chart.js et Space Grotesk.


* **AUD-02 (Critique)** : La concaténation `.isoformat() + "Z"` sur des objets `datetime` en UTC génère le suffixe illégal `+00:00Z` dans routes.py, produisant des valeurs `NaN` lors du parsing `Date` en JavaScript.


* **AUD-03 (Majeur)** : L'expiration de la session de 30 minutes renvoie une redirection HTTP 302 vers `/login` sur les routes de pages, ce qui risque d'être injecté comme contenu partiel par `fetch()` dans spa-router.js et de désynchroniser le token CSRF après reconnexion.


* **AUD-04 (Majeur)** : Le fichier history.css utilise des noms de variables CSS (`--sb-text-primary`, `--sb-surface`, `--sb-border-color`) distincts du reste de l'application (`--sb-text`, `--sb-card`, `--sb-card-border`), menaçant la lisibilité et les contrastes WCAG en mode sombre.


* **AUD-05 (Majeur)** : La méthode `_run_once_impl()` dans automation.py quitte la fonction avant d'appeler `record_state()` lorsque l'automatisation est désactivée ou hors fenêtre horaire, privant les graphiques Chart.js de mesures pendant ces périodes.


* **AUD-06 (Majeur)** : En production, lorsque `history_service` est inactif (mode dégradé `JsonStore`), les endpoints `/history/api/*` retournent une erreur HTTP 503 au lieu d'une structure vide fail-safe.


* **AUD-07 (Mineur)** : Les feuilles devices.css et history.css n'implémentent pas la requête média `@media (prefers-reduced-motion: reduce)`.


* **AUD-08 (Mineur)** : Utilisation de `transition: all` et d'animations sur la propriété `left` dans devices.css, promotion GPU permanente avec `backdrop-filter: blur(20px)` dans actions.css, et absence d'anneau de focus `:focus-visible` à fort contraste sur `.action-btn`, `.scene-btn` et `.btn-copy`.


* **AUD-09 (Suggestion)** : Renforcer la directive `script-src` de la CSP en remplaçant `'unsafe-inline'` par un mécanisme de nonces cryptographiques, et harmoniser le paramètre `retention_hours` (24h dans `__init__.py` contre 6h dans les spécifications).



### Matrice d'actions correctives priorisée (P0, P1, P2)

| Priorité | ID | Action corrective recommandée | Effort | Impact |
| --- | --- | --- | --- | --- |
| P0 | AUD-01 | Versionner static/vendor et vérifier les fichiers dans test_frontend_performance.py | Faible | Critique |
| P0 | AUD-02 | Remplacer `isoformat() + "Z"` par `_utc_now_iso()` ou `.isoformat()` dans routes.py | Faible | Critique |
| P0 | AUD-03 | Détecter `response.redirected` vers `/login` dans spa-router.js et forcer la redirection | Faible | Élevé |
| P1 | AUD-04 | Unifier les variables CSS de history.css sur les tokens standards de theme.css | Faible | Élevé |
| P1 | AUD-05 | Déplacer l'enregistrement `record_state()` juste après `poll_meter()` dans automation.py | Moyen | Élevé |
| P1 | AUD-06 | Retourner un payload JSON vide HTTP 200 dans `/history/api/*` si `history_service` est absent | Faible | Moyen |
| P1 | AUD-08 | Remplacer `transition: all` et `left` par `transform`/`opacity` et ajouter `:focus-visible` | Faible | Moyen |
| P2 | AUD-07 | Ajouter `@media (prefers-reduced-motion: reduce)` dans devices.css et history.css | Faible | Moyen |
| P2 | AUD-09 | Aligner la documentation des skills (critical.css, endpoints history) avec le code réel | Faible | Faible |

* **Détail des actions P0 (Immédiat)** :
1. Vérifier la présence effective de toutes les ressources dans switchbot_dashboard/static/vendor/ et s'assurer qu'elles sont embarquées dans l'image Docker.


2. Dans switchbot_dashboard/routes.py, supprimer la concaténation ` + "Z"` sur les timestamps déjà porteurs de `dt.timezone.utc` (ou utiliser `.strftime("%Y-%m-%dT%H:%M:%SZ")`) et s'assurer que history.js trie les points par timestamp croissant avant la décimation LTTB.


3. Dans switchbot_dashboard/static/js/spa-router.js, vérifier `if (response.redirected && response.url.includes('/login')) { window.location.href = response.url; return; }` et rafraîchir le `<meta name="csrf-token">` du document à chaque transition SPA.




* **Détail des actions P1 (Court terme)** :
1. Aligner les variables CSS de switchbot_dashboard/static/css/history.css sur celles de theme.css et ajouter un `outline: 2px solid var(--sb-accent); outline-offset: 2px;` sur `:focus-visible` pour tous les boutons interactifs.


2. Enregistrer systématiquement les relevés du capteur dans `HistoryService` à chaque appel réussi de `poll_meter()`, même hors fenêtre horaire, et retourner des tableaux vides (`data: []`, `latest: []`) avec statut 200 lorsque PostgreSQL est remplacé par `JsonStore`.




* **Détail des actions P2 (Moyen terme)** :
1. Étendre `@media (prefers-reduced-motion: reduce)` à l'ensemble des feuilles de style et nettoyer les références obsolètes aux fichiers `performance-optimizer.js`, `advanced-optimizer.js` et `/history/api/records` dans les guides `.agents/skills/`.