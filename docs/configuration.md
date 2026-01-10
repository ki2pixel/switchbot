# Configuration du Dashboard

## Fichiers de configuration

### 1. Identifiants SwitchBot (`.env`)

Les identifiants API sont stockés dans `.env` et jamais sérialisés dans les fichiers JSON :

```bash
SWITCHBOT_TOKEN=votre_token_ici
SWITCHBOT_SECRET=votre_secret_ici
SWITCHBOT_RETRY_ATTEMPTS=2
SWITCHBOT_RETRY_DELAY_SECONDS=10
SWITCHBOT_POLL_INTERVAL_SECONDS=60
LOG_LEVEL=info
FLASK_SECRET_KEY=change_me
```

> ⚠️ **Sécurité** : Ne jamais commiter `.env`. Utiliser `.env.example` comme modèle.

#### Override du poll interval

- Lorsqu'une valeur `SWITCHBOT_POLL_INTERVAL_SECONDS` est définie, `create_app()` force l'écriture immédiate de cette valeur (minimum 15 s) dans `config/settings.json` au démarrage pour garantir la cohérence des ticks scheduler.  
- Mettre à jour `.env` suffit donc pour overrider durablement le poll interval, même si l'UI affiche encore l'ancienne valeur avant rafraîchissement.

#### Valeurs par défaut et clés Flask

- `SWITCHBOT_RETRY_ATTEMPTS` et `SWITCHBOT_RETRY_DELAY_SECONDS` retombent respectivement sur `2` et `10` secondes si la valeur fournie n'est pas un entier valide.  
- Définir `FLASK_SECRET_KEY` dans `.env` est indispensable : en production, cela évite le fallback `"dev"` utilisé uniquement pour le développement et protège les sessions/flash messages.
- `LOG_LEVEL` contrôle le niveau de log de Gunicorn (valeurs possibles : DEBUG, INFO, WARNING, ERROR, CRITICAL), appliqué via le Dockerfile en production et via `switchbot_dashboard/__init__.py` en développement.

### 2. Paramètres applicatifs (`config/settings.json`)

Ce fichier contient les réglages métier persistés :

```json
{
  "automation_enabled": true,
  "mode": "summer",
  "poll_interval_seconds": 60,
  "command_cooldown_seconds": 30,
  "hysteresis_celsius": 0.5,
  "meter_device_id": "C271111EC0AB",
  "aircon_device_id": "02-202008110034-13",
  "time_windows": [
    {
      "days": [0, 1, 2, 3, 4, 5, 6],
      "start": "08:00",
      "end": "22:00"
    }
  ],
  "winter": {
    "min_temp": 18.0,
    "max_temp": 22.0,
    "target_temp": 20.0,
    "ac_mode": 5,
    "fan_speed": 3
  },
  "summer": {
    "min_temp": 22.0,
    "max_temp": 26.0,
    "target_temp": 24.0,
    "ac_mode": 2,
    "fan_speed": 2
  },
  "api_quota_warning_threshold": 250,
  "aircon_scenes": {
    "winter": "SCENE_WINTER_UUID",
    "summer": "SCENE_SUMMER_UUID",
    "fan": "SCENE_FAN_UUID",
    "off": "SCENE_OFF_UUID"
  },
  "turn_off_outside_windows": true
}
```

> ℹ️ **Production et conteneurs Render** : lorsque `STORE_BACKEND=redis` est activé, les fichiers `config/settings.json` et `config/state.json` empaquetés dans l'image Docker ne servent qu'à fournir des valeurs initiales. Toutes les modifications effectuées via l'interface sont écrites dans Redis et survivent aux redeploy/scale. Ne modifiez les fichiers locaux que pour préparer un premier déploiement ou dépanner hors ligne.

#### Gestion du quota API (`api_quota_warning_threshold`)

- **Valeur par défaut** : `250` (10% d'une limite quotidienne typique de 2500 appels)
- **Comportement** :
  - Déclenche une alerte visuelle (bannière rouge) dans l'interface utilisateur lorsque le nombre de requêtes restantes tombe en dessous de ce seuil
  - Permet d'anticiper l'épuisement du quota quotidien SwitchBot (limite de 2500 appels/jour)
  - Configurable via l'interface utilisateur ou directement dans `settings.json`
  - Se réinitialise à minuit UTC avec le compteur de quota

#### Scènes SwitchBot (automatisation + boutons rapides)

La configuration des scènes permet de déclencher des actions complexes pré-configurées dans l'application SwitchBot officielle. Chaque scène est identifiée par un UUID unique.

**Configuration des scènes :**

- **Scènes disponibles :**
  - `winter` : Mode chauffage (scène personnalisable dans l'application SwitchBot)
  - `summer` : Mode climatisation (scène personnalisable)
  - `fan` : Mode ventilation (scène personnalisable)
  - `off` : Arrêt du climatiseur (scène personnalisable)

- **Comportement :**
  - Les boutons de l'interface déclenchent directement les scènes correspondantes
  - **L'Automation utilise ces scènes en priorité** : 
    - Lorsque la température franchit les seuils définis, `AutomationService` tente d'exécuter les scènes `winter`/`summer`
    - Si `turn_off_outside_windows` est activé, la scène `off` est utilisée en dehors des plages horaires configurées
  - **Fallback aux commandes bas niveau :**
    - Si une scène n'est pas configurée, le système utilise automatiquement les commandes `setAll`/`turnOff`
    - Un `aircon_device_id` valide est nécessaire pour ce mode de secours
    - L'interface affiche un avertissement si des scènes obligatoires sont manquantes
    - Les boutons correspondants aux scènes manquantes sont désactivés dans l'interface
  - **Gestion de l'état :**
    - La scène `off` est utilisée par le bouton "Quick off" pour un arrêt contrôlé
    - L'état des scènes est vérifié au démarrage et après chaque modification des paramètres
    - Les erreurs d'exécution des scènes sont journalisées et affichées dans l'interface
    - L'état de l'appareil est suivi via `assumed_aircon_power` dans l'état de l'application
    - L'interface affiche des indicateurs visuels pour chaque scène (configurée/manquante)

**Configuration recommandée :**
1. Créez les scènes dans l'application SwitchBot officielle
2. Récupérez les UUID via l'API (`GET /v1.1/scenes`)
3. Saisissez les UUID dans l'interface d'administration ou directement dans `settings.json`
4. Activez `turn_off_outside_windows` pour une gestion automatique de l'arrêt en dehors des plages horaires

### Dépannage des scènes

Si une scène ne fonctionne pas comme prévu :
1. Vérifiez que l'UUID est correct dans les paramètres
2. Testez la scène directement depuis l'application SwitchBot
3. Consultez les logs de l'application pour les erreurs d'exécution
4. Si nécessaire, activez le mode debug avec `LOG_LEVEL=debug` pour plus de détails

> ⚠️ **Remarque :** Un `aircon_device_id` valide reste nécessaire pour le mode de secours (fallback) des commandes `setAll`/`turnOff` lorsque les scènes ne sont pas configurées. Sans configuration, un message d'avertissement s'affiche dans l'interface.

> ℹ️ **Historique :** La logique `aircon_presets` a été remplacée par ce système de scènes plus flexible. Voir `memory-bank/decisionLog.md` pour plus de détails.

### Dépannage de l'automatisation

Pour diagnostiquer un cycle d'automatisation qui ne déclenche pas l'action attendue :

1. **Activer les logs détaillés** : définir `LOG_LEVEL=debug` (dans `.env` ou la configuration Render). Les logs incluent désormais le déclencheur (`scheduler` ou `http:actions.run_once`), les fenêtres horaires évaluées, les seuils calculés (min/max/hysteresis), ainsi que chaque action (scène ou fallback `setAll`/`turnOff`).
2. **Utiliser `Run once`** : depuis la page d’accueil, cliquer sur « Exécuter une fois » pour forcer un tick et observer en direct les messages `[automation]`.
3. **Suivre les étapes clés** :
   - `Automation tick started` : confirme que l’automatisation s’exécute et rappelle l’intervalle.
   - `Time window evaluation` : affiche les fenêtres interprétées (`[0,1,2] 08:00-22:00`), si l’on est en dehors, et si `turn_off_outside_windows` s’appliquera.
   - `Temperature evaluation` : loggue `mode`, `current_temp`, `min/max`, `target` et `hysteresis`.
   - Messages `Winter/Summer mode: ... threshold` + `Requesting aircon scene`/`setAll`/`turnOff` : détaillent l’action choisie et le fallback éventuel.
   - `Automation tick finished` : fournit l’`outcome` (`winter_on`, `summer_off`, `no_action`, `cooldown`, etc.) pour résumer la décision.
4. **Inspecter les quotas** : chaque appel SwitchBot (lecture Meter, scène, commande) se termine par `Quota snapshot updated context=...` avec `used/remaining/limit`, utile pour vérifier que les requêtes partent réellement.

> 💡 **Astuce** : combiner ces logs avec `/quota` permet de repérer rapidement un cooldown actif, une fenêtre mal configurée ou un seuil d’hysteresis trop large (par exemple `27.9°C` vs `max=27 + hysteresis=0.3`).

## Endpoint de santé (`/healthz`)

Le tableau de bord expose un endpoint de santé qui renvoie des métriques essentielles pour le monitoring :

```json
{
  "status": "ok",
  "scheduler_running": true,
  "automation_enabled": true,
  "last_tick": "2024-01-10T14:30:00Z",
  "api_requests_total": 42,
  "api_requests_remaining": 958,
  "api_quota_day": "2024-01-10",
  "version": "1.0.0"
}
```

### Champs de réponse

- `status` (chaîne) : "ok" si le service fonctionne normalement, "error" en cas de problème critique
- `scheduler_running` (booléen) : Indique si le planificateur d'automatisation est actif
- `automation_enabled` (booléen) : Reflète le paramètre `automation_enabled` des paramètres
- `last_tick` (ISO 8601) : Horodatage de la dernière exécution de l'automatisation
- `last_read_at` (ISO 8601) : Dernière lecture réussie du capteur de température
- `temperature_stale` (booléen) : Indique si la température actuelle est potentiellement obsolète
- `api_requests_total` (nombre) : Nombre total de requêtes API effectuées aujourd'hui
- `api_requests_remaining` (nombre) : Estimation des requêtes API restantes (basée sur la limite quotidienne de 10000 requêtes par défaut)
- `api_quota_day` (date) : Jour de référence pour le quota actuel (réinitialisé à minuit UTC)
- `version` (chaîne) : Version de l'application

### Codes d'erreur

- `200 OK` : Le service fonctionne normalement
- `503 Service Unavailable` : Le service rencontre des problèmes critiques (ex: impossibilité d'accéder au stockage)
- `429 Too Many Requests` : Trop de requêtes vers l'endpoint (rate limiting)

### Utilisation recommandée

1. **Monitoring de base** : Vérifier que `status` est `"ok"`
2. **Surveillance des quotas** : Alerter si `api_requests_remaining` est bas
3. **Détection des blocages** : Vérifier que `last_tick` est récent (dans les 5 dernières minutes en fonctionnement normal)
4. **Intégration** : Configurer des vérifications périodiques (ex: toutes les 5 minutes) avec un timeout court (ex: 2 secondes)

### Exemple de vérification

```bash
curl -s https://votre-instance-render.com/healthz | jq '.status == "ok" and .scheduler_running == true and .automation_enabled == true'
```

> 💡 **Astuce** : En production, configurez votre outil de monitoring (Prometheus, Datadog, etc.) pour interroger cet endpoint et alerter en cas de problème.

### 3. Stockage persistant (Redis ou fichiers)

Le tableau de bord prend en charge deux modes de stockage pour les paramètres et l'état :

#### Configuration du backend

| Variable | Description |
|----------|-------------|
| `STORE_BACKEND` | `filesystem` (par défaut) ou `redis` |
| `REDIS_URL` | URL complète Redis (`redis://` ou `rediss://` pour TLS) |
| `REDIS_PREFIX` | Préfixe pour les clés (défaut : `switchbot_dashboard`) |
| `REDIS_TTL_SECONDS` | Durée de vie des clés (optionnel) |
| `SWITCHBOT_SETTINGS_PATH` | Chemin du fichier de configuration (mode filesystem) |
| `SWITCHBOT_STATE_PATH` | Chemin du fichier d'état (mode filesystem) |

#### Recommandations de déploiement

**Pour les environnements conteneurisés (Docker, Render) :**
- Utilisez Redis pour une persistance fiable entre les redémarrages
- Configurez `STORE_BACKEND=redis` et `REDIS_URL`
- Pour des raisons de sécurité, utilisez `rediss://` (TLS) en production

**Pour le développement local :**
- Le mode `filesystem` est suffisant
- Les données sont stockées dans `config/settings.json` et `config/state.json`

#### Migration vers Redis

1. Sauvegardez vos fichiers de configuration actuels :
   ```bash
   cp config/settings.json config/settings.json.bak
   cp config/state.json config/state.json.bak
   ```

2. Créez une instance Redis (par exemple via Render ou Upstash)

3. Exportez les variables d'environnement :
   ```bash
   export STORE_BACKEND=redis
   export REDIS_URL=rediss://default:password@host:port
   export REDIS_PREFIX=switchbot_dashboard
   ```

4. (Optionnel) Importez les données existantes :
   ```bash
   redis-cli -u $REDIS_URL SET ${REDIS_PREFIX}:settings "$(cat config/settings.json)"
   redis-cli -u $REDIS_URL SET ${REDIS_PREFIX}:state "$(cat config/state.json)"
   ```

5. Redémarrez le service et vérifiez que les paramètres sont chargés correctement

#### Gestion des erreurs

- En cas d'erreur de connexion à Redis, le système bascule automatiquement en mode `filesystem`
- Les erreurs sont journalisées avec le niveau `ERROR`
- Vérifiez les logs pour diagnostiquer les problèmes de connexion

**Sécurité** :

- Préférer `rediss://` (TLS) pour tous les environnements accessibles depuis Internet.
- Utiliser un mot de passe unique par environnement et limiter les droits réseau (Render gère automatiquement les ACL internes).

## Navigation principale

- **Page d'accueil (`/`)** : Statut temps réel, actions rapides (scènes, exécution ponctuelle, arrêt rapide).
- **Page Réglages (`/reglages`)** : Tous les formulaires de configuration (automatisation, fenêtres horaires, profils hiver/été, scènes, seuils de quota).
- **Page devices (`/devices`)** : Inventaire complet des devices pour récupérer rapidement les IDs.
- **Page quota (`/quota`)** : Suivi du quota API quotidien calculé par `ApiQuotaTracker`.

## Page d'accueil (`/`)

### En-tête

- Titre + sous-titre rappelant la mission du dashboard.
- Deux boutons principaux :
  - **Quota API** → ouvre la page `/quota`.
  - **Devices** → redirige vers `/devices`.
- L'allègement de l'en-tête libère de l'espace pour les cartes **Current status** et **Settings**.

### Carte Settings

- Le champ `Quota warning threshold` configure `api_quota_warning_threshold`.
- Une valeur de `0` désactive l'alerte.
- Les autres réglages (mode, fenêtres horaires, scènes) restent inchangés.

## Page quota API (`/quota`)

- La vignette "Quota API quotidien" affiche :
  - Requêtes restantes (`api_requests_remaining`) et utilisées (`api_requests_total`) avec la limite (`api_requests_limit`, 10 000 par défaut).
  - Jour suivi (`api_quota_day`) et horaire de reset (`api_quota_reset_at`). Si l'horodatage est absent, l'UI rappelle la réinitialisation à 00:00 UTC.
  - Alerte jaune lorsque `api_requests_remaining` ≤ `api_quota_warning_threshold`.
- Un encadré latéral rappelle le fonctionnement d'`ApiQuotaTracker` :
  - Réinitialisation automatique à minuit (UTC).
  - Fallback local lorsque l'API n'expose pas les en-têtes `X-RateLimit-*`.
  - Comptabilisation des appels issus de l'automatisation, des actions rapides, des scènes et des pages `/devices`.
- **Conseils d'exploitation** :
  - Ajustez `api_quota_warning_threshold` depuis la page d'accueil avant les journées chargées (valeur par défaut : 250).
  - Sous le seuil, réduisez les actions manuelles ou augmentez `poll_interval_seconds`.
  - Contrôlez la page avant un rafraîchissement massif des devices ou un ajustement de scènes.

## Inventaire des devices (`/devices`)

### Workflow de récupération des IDs

1. Ouvrir la page `/devices` (bouton **Devices** dans la barre supérieure)
2. La carte "Inventory snapshot" affiche :
   - Nombre de devices physiques (`deviceList`)
   - Nombre de télécommandes IR (`infraredRemoteList`)
3. Utiliser les cartes individuelles :
   - Bouton **Copier l'ID** pour coller directement dans `settings.json`
   - Badges "Hub/Standalone" pour vérifier la topologie
   - Métadonnées (firmware, statut, batterie) pour diagnostic
4. Pour debug : ouvrir les blocs `<details>` "Afficher le JSON brut"

> 💡 Ce workflow évite les erreurs de copie depuis l'app mobile et garantit l'utilisation des IDs officiels SwitchBot.

### Types de devices requis

- **Capteur de température** : `deviceType: "Meter"` → `meter_device_id`
- **Télécommande IR climatisation** : `remoteType: "Air Conditioner"` → `aircon_device_id`

## Validation et constantes

La validation des formulaires utilise des constantes partagées dans `routes.py` :

```python
# @switchbot_dashboard/routes.py#15-207
DAY_CHOICES = [...]
TIME_CHOICES = [...]
TEMP_CHOICES = [...]
AC_MODE_CHOICES = [...]
FAN_SPEED_CHOICES = [...]
```

### Règles de validation

- `poll_interval_seconds` : 15‑3600 s
- `command_cooldown_seconds` : 0‑3600 s  
- `hysteresis_celsius` : 0‑5 °C
- Températures : 14‑32 °C par pas de 0,5 °C
- Modes AC : 1 (Auto), 2 (Cool), 3 (Dry), 4 (Fan), 5 (Heat)
- Vitesses : 1 (Auto), 2 (Low), 3 (Medium), 4 (High)

> 📝 Les helpers `_as_bool`, `_as_int`, `_as_float` garantissent la cohérence entre UI et stockage JSON. Décision documentée dans `memory-bank/decisionLog.md` (2026-01-09 16:21).

## État opérationnel (`config/state.json`)

Ce fichier journalise l'état courant pour l'affichage UI :

```json
{
  "last_temperature": 23.5,
  "last_humidity": 55,
  "last_action": "setAll",
  "last_action_at": "2026-01-09T17:30:00Z",
  "assumed_aircon_power": "on",
  "api_requests_total": 150,
  "api_requests_remaining": 9850,
  "api_quota_day": "2026-01-10",
  "last_error": null
}
```

## Flag de température obsolète

Le tableau de bord utilise un système de flag pour indiquer quand les données de température sont potentiellement obsolètes :

- `last_temperature_stale` (booléen) : Indique si la dernière lecture de température est obsolète
- `last_temperature_stale_reason` (chaîne) : Raison de l'obsolescence (ex: "startup", "api_error")

Ce système est particulièrement utile lors des redémarrages du service (comme les redeploys sur Render qui prennent environ 1 minute) pour éviter de prendre des décisions d'automatisation basées sur des données potentiellement périmées.

Le flag est automatiquement :
- Positionné à `true` au démarrage du service
- Réinitialisé à `false` après une lecture réussie du capteur via `poll_meter()`
- Positionné à `true` en cas d'erreur d'API avec `last_temperature_stale_reason` défini sur "api_error"

## Sécurité et bonnes pratiques

- **Principe du moindre privilège** : n'exposer que les données nécessaires
- **Accès atomique** : `JsonStore` utilise `threading.Lock` et écriture via fichier temporaire
- **Validation systématique** : jamais de consommation directe de `request.form`
- **Logs sécurisés** : jamais de secrets dans les logs, utilisation de `current_app.logger`

## Quotas & limites API

- L'API SwitchBot applique une limite stricte de **10 000 requêtes/jour** et par compte (référence doc officielle).  
- Le suivi est centralisé via `ApiQuotaTracker` (instancié dans `create_app()` et injecté dans `SwitchBotClient`). Chaque appel au client – peu importe l'origine (scheduler, boutons manuels, pages `/devices`, retries sur erreurs 429/5xx/190) – déclenche automatiquement une incrémentation du compteur :
  - Si les headers `X-RateLimit-*` sont présents, ils sont persistés tels quels (`api_requests_limit`, `api_requests_remaining`, `api_requests_total`) pour refléter l'état exact fourni par SwitchBot.
  - Si les headers sont absents (cas le plus fréquent), le tracker tombe en mode estimation locale en incrémentant `api_requests_total` à chaque requête réussie et en recalculant `api_requests_remaining` en fonction de la limite journalière (10 000 par défaut, ajustée si SwitchBot communique une `limit` différente).  
- Le tracker réinitialise automatiquement `api_quota_day`, `api_requests_total`, `api_requests_remaining` et `api_requests_limit` à minuit UTC, garantissant que l'UI reflète la consommation du jour courant.
- La vignette "Quota API quotidien" (page `/quota`) consomme ces valeurs sans logique supplémentaire. Que les appels proviennent du scheduler, d'un bouton rapide ou de la page `/devices`, l'information reste synchronisée.
- Le champ `api_quota_warning_threshold` (défaut : 250) déclenche l'alerte affichée sur `/quota`. Fixez-le selon vos besoins : valeur plus élevée pour anticiper, `0` pour désactiver l'avertissement.
- Recommandation opérationnelle : surveiller ce compteur avant d'exécuter des rafales d'actions manuelles ou de réduire trop le `poll_interval_seconds`. En dessous de ~200 appels restants, suspendre l'automatisation ou allonger l'intervalle pour éviter de saturer la journée.

---

*Voir aussi [Guide UI](ui-guide.md) pour l'interaction avec les formulaires, [Tests](testing.md) pour la validation, et `memory-bank/systemPatterns.md` pour les patterns architecturaux.*
