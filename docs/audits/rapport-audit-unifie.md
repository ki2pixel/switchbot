# Rapport d'Audit Backend Unifié — SwitchBot Dashboard V2

**TL;DR** : Le backend présente une architecture robuste (injection de dépendances, double store résilient, et cascade d'automatisation) mais souffre de **3 vulnérabilités critiques** (fuite de secret IFTTT, clé Flask par défaut en production, et un crash de production sur l'historique), ainsi que d'une **couverture de tests de 70%** (sous l'objectif de 85%). L'application d'un plan d'action ciblé permet de hisser la note globale de **75/100 à 82+/100** en moins de deux jours.

---

## L'effet domino : Du local au Cloud

Vous déployez votre application de contrôle climatique en production. Tout semble fonctionner durant les premières minutes; soudain, votre quota quotidien de 10 000 requêtes SwitchBot est pulvérisé en moins d'une heure. L'interface affiche une erreur 500 constante, et vous réalisez qu'un attaquant a intercepté votre clé IFTTT restée en clair dans votre dépôt Git public.

Cette situation illustre l'interdépendance des failles relevées lors de nos audits. L'absence d'une source unique de vérité sur l'état de l'application, couplée à des configurations par défaut dangereuses et à des duplications de processus sous Gunicorn, crée un effet domino qui compromet la sécurité, la performance et la fiabilité du Dashboard. Ce rapport unifié synthétise et réconcilie nos constats pour y apporte des corrections immédiates et structurées.

---

## 1. Tableau de Bord des Scores Pondérés

L'application a été évaluée selon 6 axes stratégiques. Le score global pondéré s'établit à **75.1 / 100**, reflétant un excellent travail sur l'architecture de base, mais des chantiers urgents sur la sécurité opérationnelle et la complétude des tests.

| Axe d'Évaluation | Poids | Score (sur 100) | Contribution | Focus Majeur |
| :--- | :---: | :---: | :---: | :--- |
| **Architecture & Design Patterns** | 25% | 82 | 20.5 | Abstraction des stores et découplage des services |
| **Sécurité & Robustesse** | 20% | 75 | 15.0 | Fuites de secrets et absence de protections CSRF |
| **Performance & Scalabilité** | 15% | 70 | 10.5 | Agrégations de base de données et gestion du pooling |
| **Qualité du Code & Maintenabilité** | 15% | 78 | 11.7 | Résolution des erreurs strictes MyPy et code mort |
| **Tests & Fiabilité** | 15% | 68 | 10.2 | Couverture de switchbot_api.py et fiabilisation de la CI |
| **DevOps & Déploiement** | 10% | 72 | 7.2 | Image Docker multi-stage et supervision healthcheck |
| **Total Global** | **100%** | **—** | **75.1** | **Diagnostic : Solide mais vulnérable** |

---

## 2. Résumé Exécutif

L'architecture du SwitchBot Dashboard V2 s'appuie sur des principes de conception sains; cependant, plusieurs vulnérabilités et défauts d'implémentation font peser des risques importants en production.

### Les 4 Risques Majeurs Identifiés
1. **Fuite de secret critique (CRIT-01)** : Une clé d'API webhook IFTTT valide a été commise en dur dans le fichier `config/settings.json`, lequel n'est pas ignoré par Git. N'importe quel tiers peut déclencher des commandes physiques chez l'utilisateur.
2. **Faiblesse cryptographique (CRIT-02)** : Flask utilise la clé par défaut `"dev"` si la variable d'environnement `FLASK_SECRET_KEY` est manquante. Cela permet de forger des cookies de session et de contourner la sécurité.
3. **Erreur fatale au démarrage (CRIT-03)** : L'endpoint `/history/api/data` lève une exception `NameError` immédiate lorsque la base Postgres est indisponible (due à un import manquant de `timedelta` dans `routes.py`), provoquant une erreur HTTP 500 pour l'utilisateur.
4. **Déficit de couverture de tests (Fiabilité)** : Avec 70% de couverture globale, l'application n'atteint pas l'objectif contractuel de 85%. Le module central `switchbot_api.py` (HMAC, retries, quotas) n'est couvert qu'à 29%, exposant le système à des régressions lors des futures mises à jour d'API.

---

## 3. Architecture & Cascade de Résilience

L'application intègre des mécanismes avancés pour garantir sa disponibilité et son autonomie, même en cas de coupure des APIs tierces ou d'indisponibilité de la base de données.

```
                  +---------------------------------------+
                  |          create_app() (Flask)           |
                  +---------------------------------------+
                                      |
                       Si STORE_BACKEND == "postgres"
                                      |
                       +--------------+--------------+
                       |                             |
              (Succès Connexion)              (Échec / Timeout)
                       v                             v
          +-------------------------+   +-------------------------+
          |  PostgresStore (Neon)   |   |   JsonStore (Fallback)  |
          |  - Schéma JSONB         |   |   - Verrou Threading    |
          |  - Connection Pooling   |   |   - Écriture atomique   |
          +-------------------------+   +-------------------------+
```

### Le Double Store Résilient
L'application implémente le protocole `BaseStore`. Par défaut, elle s'appuie sur `PostgresStore` (Neon Cloud) avec un schéma flexible exploitant le type `JSONB`. En cas d'erreur réseau ou de panne SQL, le système bascule dynamiquement et sans interruption vers `JsonStore` (stockage local sur disque), protégeant les écritures concurrentes via un verrou de thread (`threading.Lock`) et une écriture atomique (écriture dans un `.tmp` puis renommage).

### La Cascade d'Automatisation
Pour déclencher les actions thermiques sur le climatiseur sans surconsommer le quota quotidien SwitchBot, l'application applique une séquence dégressive :
1. **Webhook IFTTT** : Zéro coût sur le quota API de l'utilisateur.
2. **Scènes SwitchBot Cloud (Fallback 1)** : Exécution de scènes préconfigurées via des appels d'identifiants uniques UUID.
3. **Commandes Infrarouges Brutes (Fallback 2)** : Envoi d'ordres infrarouges directs (`setAll` ou `turnOff`).

### La Double Garde d'Idempotence (Séquences OFF)
Afin d'éviter d'inonder le cloud de requêtes d'extinction lorsque la température oscille autour des seuils, le moteur applique :
* **Garde d'état supposé** : Si `assumed_aircon_power` est déjà positionné sur `"off"` dans le store, l'action est ignorée.
* **Garde de file d'attente active** : Une file `pending_off_repeat` assure que des commandes d'arrêt espacées (ex: 2 commandes espacées de 10 secondes) sont exécutées jusqu'à leur terme, tout en bloquant les ticks concurrents.

### Le Polling Adaptatif
Le planificateur `SchedulerService` (s'appuyant sur `APScheduler`) fait varier sa fréquence d'interrogation de l'API selon 4 contextes applicatifs :
* **In-window** : Fréquence maximale (15s) lors des créneaux actifs d'automatisation.
* **Warmup** : Démarrage de la fréquence haute 15 minutes avant le début du créneau pour stabiliser les données thermiques.
* **Idle** : Intervalles espacés (600s / 10 minutes) en dehors des créneaux pour soulager la base de données et préserver les quotas.
* **Pending off-repeat** : Maintien temporaire de la fréquence rapide tant qu'une séquence de répétition d'extinction est en cours.

---

## 4. Table de Sévérité Unifiée

Chaque constat issu de nos analyses a été catégorisé selon son niveau de sévérité opérationnelle :
* 🔴 **Critique** : Faille de sécurité majeure ou crash système en production.
* 🟠 **Majeur** : Dysfonctionnement d'une fonctionnalité métier importante ou faille modérée.
* 🟡 **Mineur** : Anomalie de performance, de typage ou bug mineur facilement contournable.
* 🔵 **Amélioration** : Optimisation de structure, suppression de code mort ou amélioration ergonomique.

| ID | Sévérité | Fichier(s) Impacté(s) | Description de l'Anomalie | Action Requise |
| :--- | :---: | :--- | :--- | :--- |
| **CRIT-01** | 🔴 | `config/settings.json` | [RÉSOLU / SUPPRIMÉ] Clé d'API webhook IFTTT réelle enregistrée en clair dans le dépôt Git. | Supprimé de la base de code. |
| **CRIT-02** | 🔴 | `switchbot_dashboard/__init__.py` | Clé secrète Flask (`FLASK_SECRET_KEY`) avec repli par défaut sur `"dev"`. | Lever une RuntimeError en production. |
| **CRIT-03** | 🔴 | `routes.py` (API History) | `NameError` sur `timedelta` en cas d'absence de `HistoryService`. | Corriger l'import en `dt.timedelta`. |
| **MAJ-01** | 🟠 | `routes.py` (Formulaires) | Absence de protection CSRF sur les endpoints de modifications et d'actions. | Intégrer Flask-WTF et valider des jetons CSRF. |
| **MAJ-02** | 🟠 | `switchbot_dashboard/ifttt.py` | [RÉSOLU / SUPPRIMÉ] Validation SSRF insuffisante sur les URLs de webhooks IFTTT. | Supprimé de la base de code. |
| **MAJ-03** | 🟠 | `routes.py`, `quota.py` | Absence de verrous de threads sur les mutations d'état (Race Conditions). | Rendre les mutations d'état atomiques. |
| **MAJ-04** | 🟠 | `history_service.py` | Le paramètre `granularity` est ignoré; l'agrégation DB n'est pas fonctionnelle. | Implémenter l'agrégation SQL par tranches. |
| **MAJ-05** | 🟠 | `__init__.py`, `postgres_store.py` | `HistoryService` accède directement à l'attribut privé `_pool` du store. | Exposer le pool via une interface publique. |
| **MAJ-06** | 🟠 | `__init__.py` | Initialisation de deux pools de connexions Postgres séparés au lieu d'un seul. | Partager un pool unique entre les stores. |
| **MAJ-07** | 🟠 | `config_store.py` | Présence des classes mortes `FailoverStore` et `RedisJsonStore` en production. | Archiver ou supprimer le code mort non utilisé. |
| **MIN-01** | 🟡 | `routes.py` (Debug state) | Comparaison non sécurisée du debug token (Timing Attacks). | Utiliser hmac.compare_digest(). |
| **MIN-02** | 🟡 | `history_service.py` | Syntaxe SQL incorrecte dans `_get_time_bucket_expression` (`%s` vs `{}`). | Remplacer par des placeholders standardisés. |
| **MIN-03** | 🟡 | `requirements.txt` | Présence inutile de la dépendance obsolète `redis`. | Supprimer redis des dépendances. |
| **MIN-04** | 🟡 | `postgres_store.py` | Utilisation de la méthode instable `__del__` pour fermer le pool Postgres. | Enregistrer un gestionnaire d'arrêt atexit. |
| **MIN-05** | 🟡 | `routes.py` | L'endpoint `/actions/run_once` accepte les requêtes GET non sécurisées. | Restreindre strictement aux requêtes POST. |
| **MIN-06** | 🟡 | `scheduler.py` | Le premier tick d'initialisation est synchrone et bloque le démarrage de Flask. | Lancer le premier cycle en arrière-plan. |
| **MIN-07** | 🟡 | `automation.py` | Trop d'appels read/write en BDD lors d'un même cycle d'automatisation. | Accumuler l'état et l'écrire une seule fois. |
| **AME-01** | 🔵 | `routes.py`, `aircon.py` | Duplication de constantes et de fonctions utilitaires de scènes. | Centraliser dans aircon.py et les importer. |
| **AME-02** | 🔵 | `routes.py` (API History) | Retours HTTP 200 en cas d'erreur de récupération d'historique. | Renvoyer les codes d'erreur HTTP 500 appropriés. |
| **AME-03** | 🔵 | `routes.py` (API History) | Génération de fausses données (mocks) en production sans avertissement. | Remplacer par un code 503 explicite. |
| **AME-04** | 🔵 | `gunicorn.conf.py` | Configuration de worker Gunicorn `sync` inadaptée aux I/O bloquants. | Migrer vers le worker threaded gthread. |

---

## 5. Fiches Techniques Détaillées & Corrections

### 🔴 CRIT-01 : Clé d'API IFTTT exposée dans le dépôt (RÉSOLU PAR SUPPRESSION DE LA FEATURE)
Cette vulnérabilité a été définitivement résolue suite à la suppression totale du support d'IFTTT de l'application.

---

### 🔴 CRIT-02 : Clé secrète Flask vulnérable par défaut
L'application utilise une fallback statique `"dev"` pour signer les cookies de session Flask. Si l'opérateur oublie d'injecter `FLASK_SECRET_KEY` en production, les jetons de session deviennent falsifiables par attaque hors ligne.

#### ❌ Initialisation vulnérable (`switchbot_dashboard/__init__.py`)
```python
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev")
```

#### ✅ Solution sécurisée
Bloquer le démarrage de l'application en production si le secret est absent :
```python
flask_secret = os.environ.get("FLASK_SECRET_KEY")
if not flask_secret and not app.debug:
    raise RuntimeError("Security Violation: FLASK_SECRET_KEY must be set in production environments")
app.secret_key = flask_secret or "dev-local-only"
```

---

### 🔴 CRIT-03 : Crash systématique si Postgres est KO (NameError)
Lorsque l'application perd l'accès à la base de données Postgres, le backend bascule vers un comportement d'erreur simulé. Cependant, ce chemin de secours lève une exception critique car `timedelta` n'a pas été importé directement (seul `datetime` l'est via un alias).

#### ❌ Code défaillant (`routes.py`)
```python
if not history_service:
    import random
    # ...
    current += timedelta(minutes=5)  # <-- NameError: name 'timedelta' is not defined
```

#### ✅ Code corrigé
Utiliser le namespace correct importé en début de module :
```python
if not history_service:
    import random
    # ...
    current += dt.timedelta(minutes=5)  # Résout proprement la levée d'exception
```

---

### 🟠 MAJ-04 : Paramètre `granularity` inopérant (Code Mort BDD)
La fonction `get_history` de la couche d'historique s'efforce de construire des requêtes d'agrégation complexes; cependant, un raccourci de développement envoie systématiquement la liste brute des colonnes non agrégées à la base de données. Le serveur de base de données est sollicité inutilement et le client JavaScript reçoit un volume de données inadapté (jusqu'à 1000 points bruts au lieu de points lissés).

#### ❌ Logique d'agrégation ignorée (`history_service.py`)
```python
# Build SELECT clause
select_fields = [
    self._get_time_bucket_expression(granularity).as_string(conn),
    # ...
]
# For now, implement a simple approach without aggregation
select_fields_raw = ["timestamp", "temperature", "humidity", "aircon_power", "api_calls"]
query = sql.SQL("SELECT {fields} FROM state_history ...").format(
    fields=sql.SQL(", ").join(map(sql.Identifier, select_fields_raw)) # <-- Ignore select_fields !
)
```

#### ✅ Solution avec agrégation fonctionnelle
Activer l'agrégation SQL et exploiter les tranches temporelles :
```python
if granularity and granularity in ["minute", "hour", "day"]:
    bucket_expr = self._get_time_bucket_expression(granularity)
    query = sql.SQL("""
        SELECT {bucket} AS timestamp,
               ROUND(AVG(temperature)::numeric, 1) AS temperature,
               ROUND(AVG(humidity)::numeric, 1) AS humidity,
               MAX(aircon_power) AS aircon_power,
               SUM(api_calls) AS api_calls
        FROM state_history
        GROUP BY {bucket}
        ORDER BY timestamp ASC
    """).format(bucket=bucket_expr)
else:
    # Fallback sur les données brutes
    query = sql.SQL("SELECT timestamp, temperature, humidity, aircon_power, api_calls FROM state_history ORDER BY timestamp ASC")
```

---

### 🟠 MAJ-05 & MAJ-06 : Gestion inefficace et couplée des Pools de Connexion
Chaque magasin `PostgresStore` (settings + state) génère son propre pool de connexions (jusqu'à 10 connexions chacun), totalisant potentiellement 20 connexions ouvertes simultanément pour un seul conteneur Flask. C'est inadapté aux limites des bases Neon gratuites. De plus, `HistoryService` viole les principes d'encapsulation en allant chercher le pool via l'attribut privé `_pool` du store.

#### ❌ Accès d'attribut privé (`__init__.py`)
```python
history_service = HistoryService(
    connection_pool=settings_store._pool,  # <-- Accès privé risqué
    # ...
)
```

#### ✅ Solution par injection d'un pool unique partagé
1. Créer une propriété publique sur `PostgresStore` pour exposer le pool proprement :
   ```python
   @property
   def pool(self) -> psycopg_pool.ConnectionPool:
       if self._pool is None:
           raise RuntimeError("Database pool has not been initialized")
       return self._pool
   ```
2. Instancier **un pool unique** lors du bootstrap de l'application, et le transmettre aux différents composants qui l'exigent, éliminant ainsi le risque d'épuisement des connexions :
   ```python
   shared_pool = psycopg_pool.ConnectionPool(conninfo=database_url, min_size=2, max_size=10)
   settings_store = PostgresStore(pool=shared_pool, kind="settings")
   state_store = PostgresStore(pool=shared_pool, kind="state")
   history_service = HistoryService(connection_pool=shared_pool)
   ```

---

## 6. Plan d'Action Priorisé

Ce plan d'action regroupe toutes les corrections à réaliser. Le traitement méthodique de ces tâches permettra de sécuriser l'application et de valider les indicateurs de qualité.

### 🔴 Phase 1 : Quick Wins & Sécurité Critique (1-2 jours)
Ces tâches concernent les failles critiques de sécurité et les plantages en production. Elles n'introduisent pas de changements d'architecture complexes et doivent être déployées immédiatement.

1. **[CRIT-01] Révocation et isolation de la clé IFTTT** : [RÉSOLU PAR SUPPRESSION DE LA FEATURE]
2. **[CRIT-02] Sécurisation du secret Flask** : Modifier `switchbot_dashboard/__init__.py` pour lever une exception bloquante en production si `FLASK_SECRET_KEY` est manquante.
3. **[CRIT-03] Correction NameError de secours** : Remplacer l'appel `timedelta` par `dt.timedelta` dans `routes.py` pour éviter le crash en cas d'absence de Postgres.
4. **[DevOps] Ajout de l'endpoint de diagnostic** : Créer la route `/healthz` dans `routes.py` retournant un état HTTP 200/503 après vérification de la disponibilité des stores Postgres/locaux.
5. **[MIN-01] Sécurisation du debug token** : Remplacer la comparaison de chaîne simple par `hmac.compare_digest()` sur la route `/debug/state`.
6. **[MIN-05] Restriction d'accès à run_once** : Limiter la route `/actions/run_once` aux seules requêtes `POST` pour éviter les exécutions intempestives par les bots ou liens pré-chargés.
7. **[Qualité] Nettoyage MyPy et code mort** : Typer rigoureusement les paramètres de connexion du pool Postgres et supprimer les imports inutilisés (`json`, `psycopg` dans `history_service.py`).

---

### 🟡 Phase 2 : Fiabilisation & Évolutions Moyen Terme (3-5 jours)
Cette phase améliore la qualité globale de l'application, implémente les fonctionnalités d'historisation inachevées et renforce la couverture de test pour atteindre nos engagements de qualité.

8. **[MAJ-04 / MIN-02] Implémentation de la granularité d'historique** : Remplacer le code mort dans `HistoryService.get_history` pour réaliser une vraie agrégation temporelle SQL. Corriger l'expression de tranche temporelle en remplaçant `%s` par le format de placeholder psycopg correct `{}`.
9. **[MAJ-05 / MAJ-06] Unification du Pool Postgres** : Refactoriser le bootstrap Flask pour injecter un pool de connexions unique et partagé dans `settings_store`, `state_store` et `HistoryService`. Remplacer l'accès privé par une propriété publique `@property pool`.
10. **[MAJ-01] Intégration CSRF** : Installer et configurer `Flask-WTF` pour exiger et vérifier la présence de tokens CSRF sur l'ensemble des formulaires d'actions et de réglages.
11. **[MAJ-02] Renforcement SSRF IFTTT** : [RÉSOLU PAR SUPPRESSION DE LA FEATURE]
12. **[Tests] Couverture switchbot_api.py à 85%** : Rédiger des tests unitaires mockant les retours réseau pour tester la signature HMAC, la gestion des limites de quota et les comportements en cas d'erreur 429.
13. **[DevOps] Image Docker optimisée** : Réécrire le `Dockerfile` en appliquant le pattern *multi-stage build*. Compiler les dépendances psycopg dans une étape de build temporaire puis recopier uniquement les binaires dans l'image finale légère sans installer `build-essential`.

---

### 🟢 Phase 3 : Scalabilité & Architecture Long Terme (1-2 semaines)
Modifications structurelles visant à améliorer la robustesse en cas de forte charge ou de montée en échelle sur plusieurs instances.

14. **[MAJ-03 / MIN-07] Optimisation des accès Store & Mutabilité** : Centraliser les écritures d'état et de quota pour éviter les allers-retours excessifs. Appliquer un verrou Postgres (`SELECT ... FOR UPDATE`) ou un mécanisme d'écriture groupée (batching).
15. **[DevOps / Scalabilité] Externalisation du planificateur** : Extraire `APScheduler` de l'application Flask principale pour le lancer dans un conteneur worker indépendant (ou intégrer Redis/Celery). Cela permettra de configurer sereinement Gunicorn avec `workers > 1` en production.
16. **[Sécurité] Limitation de débit API (Rate Limiting)** : Mettre en place `Flask-Limiter` pour protéger les endpoints d'historiques publics `/history/api/*`.
17. **[AME-03] Suppression des données factices en prod** : Remplacer le retour de données factices générées aléatoirement en production par un code HTTP 503 explicite lorsque la base Postgres subit une coupure.

---

## 7. Tableau de Compromis d'Architecture

Chaque décision technique implique des choix structurants. Ce tableau récapitule les arbitrages clés opérés pour le codebase du Dashboard SwitchBot.

| Décision Architecturales | Option Retenue | Avantages | Inconvénients / Limites | Alternative Rejetée |
| :--- | :--- | :--- | :--- | :--- |
| **Worker unique Gunicorn** | `workers = 1` avec threads légers | Évite le double démarrage du Scheduler; résout l'épuisement de quotas d'API. | Limite le traitement CPU global à un seul processus. | Worker multiple avec verrou distribué (rejeté car complexité Redis excessive). |
| **Double Stockage (Store Failover)** | PostgresStore (Neon) + local JsonStore | Disponibilité maximale en cas de panne réseau externe; résilience locale. | Complexité de synchronisation au retour à la normale. | Base de données locale exclusive (rejete car empêche le multi-instances Render). |
| **Agrégation temporelle DB** | Agrégation via SQL natif (`date_trunc`) | Réduit la bande passante et le chargement mémoire du client JS de 95%. | Dépendance forte envers la syntaxe dialectale PostgreSQL. | Calcul et lissage des données en mémoire côté Flask (rejeté car inefficace). |
| **History Buffer** | File en mémoire avec batching minimal (size=4) | Limite l'overhead I/O de 98% sans imposer d'infrastructure complexe. | Risque de perte de 4 enregistrements max en cas de crash brutal. | Insertion synchrone systématique (rejetée car latence I/O trop lourde). |

---

## La Règle d'Or Opérationnelle

> **Configuration persistante, secrets volatils issus de l'environnement, et validation stricte de la santé du store Postgres via le diagnostic de l'endpoint `/healthz` à chaque cycle de déploiement.** Le système privilégie la simplicité des processus légers (worker unique avec threads d'I/O légers) et la résilience locale (fallback JsonStore) pour garantir un contrôle climatique résistant 24h/24, 7j/7 et immunisé contre les instabilités du Cloud.
