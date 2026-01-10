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
  }
}
```

> ℹ️ **Production et conteneurs Render** : lorsque `STORE_BACKEND=redis` est activé, les fichiers `config/settings.json` et `config/state.json` empaquetés dans l'image Docker ne servent qu'à fournir des valeurs initiales. Toutes les modifications effectuées via l'interface sont écrites dans Redis et survivent aux redeploy/scale. Ne modifiez les fichiers locaux que pour préparer un premier déploiement ou dépanner hors ligne.

#### Aircon scenes (boutons rapides)

- La clé `aircon_scenes` contient trois entrées `winter`, `summer` et `fan`.  
- Chaque entrée correspond à un **sceneId SwitchBot** (copié via l’API `GET /v1.1/scenes`).  
- Les boutons rapides “Aircon ON – Hiver/Été” ainsi que “Aircon ON – Mode neutre (ventilateur)” déclenchent exclusivement ces scènes.  
- L’UI (section “Scènes favorites SwitchBot”) affiche l’état de chaque ID : badge vert “Prêt” lorsque l’ID est renseigné, avertissement sinon (bouton désactivé).  
- Les scènes restent côté SwitchBot : profitez-en pour encapsuler des séquences plus riches qu’un simple `setAll` (ex : délai, combinaison multi-devices).  
- ⚠️ **Pré-requis** : un `aircon_device_id` valide reste nécessaire pour les autres actions (`Aircon OFF`, quick winter/summer). Sans cela, les routes concernées flashent “Missing aircon_device_id”.
- ℹ️ **2026-01-10** : La logique historique `aircon_presets` a été supprimée (voir `memory-bank/decisionLog.md`). Toute personnalisation passe désormais par des scènes SwitchBot configurées dans l’application officielle.

### 3. Backend de stockage (filesystem vs Redis)

| Variable | Description |
| --- | --- |
| `STORE_BACKEND` | `filesystem` (défaut) ou `redis`. Contrôle le backend utilisé pour `settings` et `state`. |
| `REDIS_URL` | URL complète (supporte `redis://` et `rediss://`). Inclure mot de passe Render. |
| `REDIS_PREFIX` | Préfixe utilisé pour composer les clés (`<prefix>:settings`, `<prefix>:state`). |
| `REDIS_TTL_SECONDS` | Optionnel. TTL appliqué aux clés Redis (laisser vide pour persistance illimitée). |
| `SWITCHBOT_SETTINGS_PATH` / `SWITCHBOT_STATE_PATH` | Forcent les chemins JSON si vous restez en mode filesystem. |

**Procédure de migration** :

1. Configurer et tester localement via le backend filesystem.
2. Exporter `config/settings.json` et `config/state.json` si vous souhaitez pré-peupler Redis.
3. Créer une instance Redis (Render → Redis) et récupérer l'URL sécurisée (`rediss://default:<password>@host:6379/0`).
4. Définir `STORE_BACKEND=redis`, `REDIS_URL=<url>`, éventuellement `REDIS_PREFIX`.
5. (Optionnel) Importer les fichiers via `redis-cli` : `SET switchbot_dashboard:settings "$(cat config/settings.json)"`.
6. Redémarrer le service et vérifier depuis l'UI que les réglages persistent après un redeploy.

**Sécurité** :

- Préférer `rediss://` (TLS) pour tous les environnements accessibles depuis Internet.
- Utiliser un mot de passe unique par environnement et limiter les droits réseau (Render gère automatiquement les ACL internes).
- Journaliser les erreurs Redis : l'application repasse automatiquement en filesystem si le backend est indisponible (logs visibles dans Render).

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

## Sécurité et bonnes pratiques

- **Principe du moindre privilège** : n'exposer que les données nécessaires
- **Accès atomique** : `JsonStore` utilise `threading.Lock` et écriture via fichier temporaire
- **Validation systématique** : jamais de consommation directe de `request.form`
- **Logs sécurisés** : jamais de secrets dans les logs, utilisation de `current_app.logger`

## Quotas & limites API

- L'API SwitchBot applique une limite stricte de **10 000 requêtes/jour** et par compte (référence doc officielle).  
- Les réponses importantes exposent idéalement des headers `X-RateLimit-*`. Lorsque disponibles, `AutomationService` lit ces valeurs, les convertit et persiste immédiatement `api_requests_remaining` et `api_requests_total` dans `config/state.json` afin de rendre l'information visible dans l'en-tête de `index.html`.  
- **Fallback local journalier** : si les headers sont absents, chaque appel API déclenché par `AutomationService` (lecture du capteur via `poll_meter()` + envoi de commandes `_send_aircon_off` / `_send_aircon_setall`) incrémente un compteur local. Ce compteur :
  - s'exécute lors de chaque tick ou action manuelle déclenchant un appel SwitchBot,
  - se réinitialise automatiquement à minuit UTC grâce à la clé `api_quota_day`,
  - stocke `api_requests_total`, `api_requests_remaining` et `api_quota_day` dans `config/state.json` pour garantir une visibilité continue.  
- La vignette "Quota API quotidien" affiche ces valeurs (restantes/utilisées) sur 10 000, ou "N/A" si aucun appel n'a encore été effectué depuis le démarrage.  
- Recommandation opérationnelle : surveiller ce compteur avant d'exécuter des rafales d'actions manuelles ou de réduire trop le `poll_interval_seconds`. En dessous de ~200 appels restants, suspendre l'automatisation ou allonger l'intervalle pour éviter de saturer la journée.

---

*Voir aussi [Guide UI](ui-guide.md) pour l'interaction avec les formulaires, [Tests](testing.md) pour la validation, et `memory-bank/systemPatterns.md` pour les patterns architecturaux.*
