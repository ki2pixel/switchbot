# Configuration du Dashboard

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Vue d'ensemble

Ce guide couvre la configuration complète du SwitchBot Dashboard, y compris les variables d'environnement, les paramètres applicatifs, et les décisions architecturales qui ont façonné l'implémentation.

> 📝 **Décisions connexes** : Les patterns de configuration sont documentés dans `memory-bank/systemPatterns.md` et `memory-bank/decisionLog.md`. Voir notamment les décisions du 2026-01-10 sur les quotas et du 2026-01-11 sur les webhooks IFTTT.

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
SCHEDULER_ENABLED=true
```

> ⚠️ **Sécurité** : Ne jamais commiter `.env`. Utiliser `.env.example` comme modèle.

#### Override du poll interval

- Lorsqu'une valeur `SWITCHBOT_POLL_INTERVAL_SECONDS` est définie, `create_app()` force l'écriture immédiate de cette valeur (minimum 15 s) dans `config/settings.json` au démarrage pour garantir la cohérence des ticks scheduler.  
- Mettre à jour `.env` suffit donc pour overrider durablement le poll interval, même si l'UI affiche encore l'ancienne valeur avant rafraîchissement.

#### Valeurs par défaut et clés Flask

- `SWITCHBOT_RETRY_ATTEMPTS` et `SWITCHBOT_RETRY_DELAY_SECONDS` retombent respectivement sur `2` et `10` secondes si la valeur fournie n'est pas un entier valide.  
- Définir `FLASK_SECRET_KEY` dans `.env` est indispensable : en production, cela évite le fallback `"dev"` utilisé uniquement pour le développement et protège les sessions/flash messages.
- `LOG_LEVEL` contrôle le niveau de log de Gunicorn (valeurs possibles : DEBUG, INFO, WARNING, ERROR, CRITICAL), appliqué via le Dockerfile en production et via `switchbot_dashboard/__init__.py` en développement.
- `SCHEDULER_ENABLED` (défaut: `true`) : Active/désactive le scheduler interne. Mettre à `false` pour utiliser un cron externe ou pour le debugging.

### 2. Paramètres applicatifs (`config/settings.json`)

Ce fichier contient les réglages métier persistés :

```json
{
  "automation_enabled": true,
  "mode": "summer",
  "poll_interval_seconds": 60,
  "command_cooldown_seconds": 60,
  "action_on_cooldown_seconds": 300,
  "action_off_cooldown_seconds": 60,
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
  "off_repeat_count": 2,
  "off_repeat_interval_seconds": 10,
  "timezone": "Europe/Paris",
  "turn_off_outside_windows": true
}
```

> ℹ️ **Production et conteneurs Render** : lorsque `STORE_BACKEND=postgres` ou `redis` est activé, les fichiers `config/settings.json` et `config/state.json` empaquetés dans l'image Docker ne servent qu'à fournir des valeurs initiales. Toutes les modifications effectuées via l'interface sont écrites dans PostgreSQL/Redis et survivent aux redeploy/scale. Ne modifiez les fichiers locaux que pour préparer un premier déploiement ou dépanner hors ligne.

#### Arrêt automatique en dehors des fenêtres (`turn_off_outside_windows`) – [2026-01-25]

- **Objectif** : forcer l'extinction du climatiseur lorsque l'on se trouve en dehors de toutes les fenêtres horaires configurées, même si la température dépasse toujours les seuils.
- **Pré-requis** : disposer d'au moins une scène OFF (`aircon_scenes.off`) **ou** d'un `aircon_device_id` valide pour le fallback `turnOff`. Comme les autres actions, l'automatisation suit la cascade **IFTTT → scène → commande directe**.
- **Implémentation** : `AutomationService.run_once()` évalue d'abord les fenêtres via `_is_now_in_windows(...)`. Si `in_window` est `False` et que `turn_off_outside_windows=true` :
  1. Lecture du `state_store` pour vérifier `assumed_aircon_power`.
  2. Si l'état supposé est déjà `"off"`, aucun appel n'est effectué (`Skipping off automation outside window: already assumed off`).
  3. Sinon, la logique de cooldown est respectée (`command_cooldown_seconds`, `action_off_cooldown_seconds`). En cas de cooldown actif, le tick se contente de faire un `poll_meter()`.
  4. Lorsque l'action OFF est envoyée, `state_reason="automation_off_outside_window"` est propagé et `run_once()` planifie également la file de répétitions (`_schedule_off_repeat_task`) si `off_repeat_count > 1`.
- **Logs & observabilité** : les ticks concernés se terminent avec `outcome="turned_off_outside_window"` (ou `already_off` / `outside_window`). Les traces `[automation] Time window evaluation ... turn_off_outside_windows=true` puis `Outside configured window — polling meter` permettent de diagnostiquer le flux. L'état `pending_off_repeat` inclut `state_reason="automation_off_outside_window"` pour distinguer cette origine d'un OFF hiver/été classique.
- **Tests associés** : `tests/test_automation_service.py::test_turn_off_outside_window_prefers_off_scene` couvre la cascade lorsqu'on est hors fenêtre.

> 💡 **Bonnes pratiques** : activez cette option uniquement si vos fenêtres horaires sont correctement calibrées (ex. "08:00-22:00") et que vous souhaitez garantir un OFF strict en dehors des plages. En production, surveillez le quota SwitchBot lorsque cette option est activée avec des fenêtres très courtes : chaque tick hors fenêtre peut déclencher un OFF + répétitions.

#### Fuseau horaire (`timezone`) - [2026-01-12]

- **Objectif** : interpréter les fenêtres horaires (`time_windows`) dans votre fuseau (ex. heure de Paris), indépendamment du fuseau du serveur (Render est souvent en UTC).
- **Valeur par défaut** : `Europe/Paris`
- **Format** : identifiant IANA (ex: `Europe/Paris`, `UTC`, `Europe/London`).
- **Validation** : si la valeur est invalide, l'interface affiche une erreur et la configuration précédente est conservée ; l'automatisation retombe explicitement sur le fuseau UTC pour continuer à fonctionner.
- **Implémentation** : Utilise `zoneinfo` pour la validation et la conversion des heures. `run_once()` calcule l'heure actuelle dans le fuseau configuré pour évaluer les fenêtres horaires.

#### Gestion du quota API (`api_quota_warning_threshold`)

- **Valeur par défaut** : `250` (≈2,5 % d'une limite quotidienne **10 000** suivie par `ApiQuotaTracker`)
- **Comportement** :
  - Déclenche une alerte visuelle (bannière) dans l'interface utilisateur lorsque le nombre de requêtes restantes tombe en dessous de ce seuil
  - Permet d'anticiper l'épuisement du quota quotidien SwitchBot (10 000 appels/jour par défaut, mais ajusté dynamiquement si SwitchBot transmet d'autres valeurs via les headers `X-RateLimit-*`)
  - Configurable via l'interface utilisateur ou directement dans `settings.json`
  - Se réinitialise à minuit UTC avec le compteur de quota
  - Le champ `api_requests_limit` persistant dans `state.json` est automatiquement mis à jour par `ApiQuotaTracker` lorsqu'une valeur différente est fournie par SwitchBot ; sinon, il reste sur 10 000. Pour forcer manuellement une autre limite (ex. 5000), définissez `state["api_requests_limit"]` puis utilisez le bouton **« Rafraîchir le quota »** sur `/quota` (route POST `/quota/refresh`) afin de refléter immédiatement la nouvelle estimation.

#### Webhooks IFTTT (priorité) + Scènes SwitchBot (fallback) - [2026-01-11]

Le dashboard implémente un système de **cascade à trois niveaux** pour déclencher vos actions de climatisation :

1. **Webhooks IFTTT** (priorité) → déclenche un applet IFTTT qui exécute une scène SwitchBot
2. **Scènes SwitchBot** (fallback 1) → appelle directement l'API SwitchBot `/scenes/{id}/execute`
3. **Commandes directes** (fallback 2) → utilise `turnOff` ou `setAll` sur le device IR

**Configuration dans `settings.json` :**

```json
{
  "ifttt_webhooks": {
    "winter": "https://maker.ifttt.com/trigger/switchbot_winter/with/key/YOUR_KEY",
    "summer": "https://maker.ifttt.com/trigger/switchbot_summer/with/key/YOUR_KEY",
    "fan": "https://maker.ifttt.com/trigger/switchbot_fan/with/key/YOUR_KEY",
    "off": "https://maker.ifttt.com/trigger/switchbot_off/with/key/YOUR_KEY"
  },
  "aircon_scenes": {
    "winter": "SCENE_WINTER_UUID",
    "summer": "SCENE_SUMMER_UUID",
    "fan": "SCENE_FAN_UUID",
    "off": "SCENE_OFF_UUID"
  }
}
```

**Validation des URLs IFTTT :**
- Les URLs doivent commencer par `https://` (HTTP non autorisé)
- Validation automatique dans `ifttt.py:17-27`
- Timeout configurable : 10 secondes par défaut

**Avantages des webhooks IFTTT :**
- ✅ **Fiabilité accrue** : contourne les bugs de l'API SwitchBot native pour l'exécution de scènes
- ✅ **Flexibilité** : créez des applets complexes (notifications, logs, chaînes d'actions)
- ✅ **Pas de quota** : les appels IFTTT ne consomment pas le quota d'API SwitchBot
- ✅ **Fallback automatique** : bascule sur les scènes natives si IFTTT échoue

**Configuration recommandée :**
1. **IFTTT** : Créez des applets IFTTT (Webhooks → SwitchBot Scene) - voir [docs/ifttt-integration.md](./ifttt-integration.md)
2. **Scènes** : Configurez les UUID de scènes SwitchBot comme fallback
3. **Device ID** : Définissez `aircon_device_id` pour le fallback ultime (commandes directes)

**Comportement de l'automatisation :**
- L'`AutomationService` privilégie **toujours** les webhooks IFTTT
- En cas d'échec (timeout, erreur HTTP), bascule sur la scène SwitchBot
- Si la scène échoue ou est absente, utilise `setAll`/`turnOff` (action `off` uniquement)

### Dépannage des webhooks et scènes

**Si un webhook ne fonctionne pas :**
1. Vérifiez que l'URL commence par `https://` (HTTP non autorisé)
2. Testez l'URL dans votre navigateur ou avec `curl`
3. Consultez les logs : `[ifttt] Triggering IFTTT webhook`
4. Vérifiez l'historique de l'applet dans IFTTT

**Si une scène ne fonctionne pas :**
1. Vérifiez l'UUID dans les paramètres
2. Testez la scène depuis l'application SwitchBot
3. Activez `LOG_LEVEL=debug` pour voir les détails
4. Consultez les logs : `[automation] Using SwitchBot scene (webhook unavailable)`

> ⚠️ **Sécurité** : Ne partagez jamais votre clé webhook IFTTT publiquement. Si elle est compromise, régénérez-la dans IFTTT → Webhooks → Settings.

> 📚 **Documentation complète** : Consultez [docs/ifttt-integration.md](./ifttt-integration.md) pour le guide pas-à-pas complet de l'intégration IFTTT, exemples d'applets et dépannage.
> 📚 **Migration PostgreSQL** : Voir [docs/postgresql-migration.md](./postgresql-migration.md) pour migrer depuis Redis/JSON vers Neon.

#### Répétition OFF paramétrable - [2026-01-11]

Pour garantir l'extinction fiable du climatiseur, le système peut envoyer plusieurs commandes OFF consécutives avec un intervalle configurable :

**Paramètres dans `settings.json` :**
```json
{
  "off_repeat_count": 2,
  "off_repeat_interval_seconds": 10
}
```

**Validation et bornes :**
- `off_repeat_count` : 1-10 (défaut : 1)
- `off_repeat_interval_seconds` : 1-600 secondes (défaut : 10)
- Validation automatique dans `routes.py:408-419`

**Comportement détaillé :**
- La première commande OFF est envoyée immédiatement
- Les commandes suivantes sont planifiées via `AutomationService._schedule_off_repeat_task()`
- L'état des répétitions en cours est stocké dans `state.json` sous `pending_off_repeat`
- Les logs détaillent chaque exécution : `[automation] Executing scheduled off repeat`

**Structure de l'état des répétitions :**
```json
{
  "pending_off_repeat": {
    "remaining": 1,
    "interval_seconds": 10,
    "next_run_at": "2026-01-11T21:30:10Z",
    "state_reason": "automation_winter_off"
  }
}
```

**Cas d'usage typique :**
- `off_repeat_count: 2` et `off_repeat_interval_seconds: 10` reproduit le comportement de l'application SwitchBot
- Utile pour les climatiseurs qui n'arrêtent pas toujours du premier coup
- Les répétitions sont automatiquement annulées si une nouvelle action est déclenchée

**Impact sur l'automatisation :**
- Les actions OFF (manuelles ou automatiques) déclenchent la file de répétitions
- **Protection contre les déclenchements multiples** : Si une température reste au-dessus du seuil `max_temp + hysteresis` (ou en dessous de `min_temp - hysteresis` en mode été), l'automatisation **ne redéclenche pas** de nouvelle action OFF tant qu'une répétition est en attente. Vous verrez dans les logs : `Skipping winter_off: off repeat already pending`.
- Les actions ON annulent les répétitions OFF en attente via `_clear_off_repeat_task()`
- L'état est traçable via `state.json` pour diagnostiquer les répétitions en cours
- Les répétitions utilisent le même système de fallback (IFTTT → scène → commande directe)

**Monitoring et logs :**
```bash
# Planification des répétitions
[automation] Scheduled repeated off action | pending_repeats=1, interval_seconds=10, state_reason=automation_winter_off

# Exécution des répétitions
[automation] Executing scheduled off repeat | trigger=scheduler, state_reason=automation_winter_off, remaining_before=1

# Annulation des répétitions
[automation] Cleared pending off repeat task
```

#### Idempotence des actions OFF - [2026-01-12]

Pour éviter les déclenchements excessifs, le système implémente une protection d'idempotence basée sur l'état supposé du climatiseur (`assumed_aircon_power`) :

**Principe de fonctionnement :**
- Une fois qu'une action OFF est déclenchée (manuellement ou automatiquement), `assumed_aircon_power` est mis à `"off"`
- Tant que cet état est `"off"`, le système **refusera** de déclencher de nouvelles actions OFF, même si la température reste dans la zone de déclenchement
- Les logs indiqueront : `Skipping winter_off: already assumed off` ou `Skipping summer_off: already assumed off`

**Cas d'usage typique :**
- Température à 28°C, seuil max à 27°C, hysteresis à 0.3°C
- Premier déclenchement à 28°C → `assumed_aircon_power="off"`
- Température reste à 28°C après les répétitions OFF → **aucun nouveau déclenchement**
- Température baisse à 26°C → action ON possible → `assumed_aircon_power="on"`

**Avantages de cette protection :**
- ✅ **Évite la saturation** des webhooks IFTTT et de l'API SwitchBot
- ✅ **Préserve le quota** API en évitant les appels inutiles
- ✅ **Stabilise l'automatisation** en cas de climatisation inefficace
- ✅ **Logs clairs** pour diagnostiquer les comportements attendus

**Réinitialisation de l'état :**
- Les actions ON (`winter_on`, `summer_on`, `fan_on`) remettent `assumed_aircon_power` à `"on"`
- Un redémarrage de l'application réinitialise l'état à `"unknown"`
- L'état est visible dans `state.json` sous la clé `assumed_aircon_power`

### Dépannage de l'automatisation

Pour diagnostiquer un cycle d'automatisation qui ne déclenche pas l'action attendue :

1. **Activer les logs détaillés** : définir `LOG_LEVEL=debug` (dans `.env` ou la configuration Render). Les logs incluent désormais le déclencheur (`scheduler` ou `http:actions.run_once`), les fenêtres horaires évaluées, les seuils calculés (min/max/hysteresis), ainsi que chaque action (scène ou fallback `setAll`/`turnOff`).
2. **Utiliser `Run once`** : depuis la page d’accueil, cliquer sur « Exécuter une fois » pour forcer un tick et observer en direct les messages `[automation]`.
3. **Suivre les étapes clés** :
   - `Automation tick started` : confirme que l’automatisation s’exécute et rappelle l’intervalle.
   - `Time window evaluation` : affiche les fenêtres interprétées (`[0,1,2] 08:00-22:00`), si l’on est en dehors, et si `turn_off_outside_windows` s’appliquera (présence des champs `turn_off_outside_windows` et `timezone`).
   - `Temperature evaluation` : loggue `mode`, `current_temp`, `min/max`, `target` et `hysteresis`.
   - Messages `Winter/Summer mode: ... threshold` + `Requesting aircon scene`/`setAll`/`turnOff` : détaillent l’action choisie et le fallback éventuel.
   - `Automation tick finished` : fournit l’`outcome` (`winter_on`, `summer_off`, `turned_off_outside_window`, `no_action`, `cooldown`, etc.) pour résumer la décision.
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

## Monitoring et Observabilité

### Logs structurés
- **Préfixes standards** : `[api]`, `[automation]`, `[scheduler]`, `[store]`, `[history]`, `[ifttt]`
- **Niveaux configurables** : DEBUG, INFO, WARNING, ERROR, CRITICAL via `LOG_LEVEL`
- **Format structuré** : Message + champs contextuels + trigger + stack trace si erreur
- **Exemple** : `[automation] Winter mode triggered | current_temp=17.5, min_temp=18.0, trigger=scheduler`

### Health Check `/healthz`
L'application expose un endpoint de monitoring pour les systèmes externes :

```json
{
  "status": "ok",
  "scheduler_running": true,
  "automation_enabled": true,
  "last_tick": "2024-01-10T14:30:00Z",
  "last_read_at": "2024-01-10T14:29:00Z",
  "temperature_stale": false,
  "api_requests_total": 42,
  "api_requests_remaining": 958,
  "api_quota_day": "2024-01-10",
  "version": "1.0.0"
}
```

**Champs de monitoring :**
- `status` : "ok", "warning", ou "error"
- `scheduler_running` : État du planificateur d'automatisation
- `temperature_stale` : Indique si les données sont obsolètes
- `api_requests_*` : Métriques de quota pour surveillance

### Gestion des Exceptions
Le dashboard implémente une gestion d'erreurs multicouche :

#### Hiérarchie des Exceptions
- **`SwitchBotApiError`** : Erreurs API SwitchBot avec retry automatique
- **`IFTTTWebhookError`** : Erreurs webhooks IFTTT avec fallback
- **`PostgresStoreError`** : Erreurs PostgreSQL avec bascule automatique
- **`StoreError`** : Erreurs génériques de stockage

#### Patterns de Résilience
- **Retry avec backoff exponentiel** : 2 tentatives max, délai 10s * 2^attempt
- **Fallback cascade** : IFTTT → scène SwitchBot → commande directe
- **Wrapper global scheduler** : Capture toutes les exceptions sans crasher
- **Bascule automatique store** : PostgreSQL → filesystem en cas d'erreur

#### Monitoring des Erreurs
```bash
# Logs structurés par préfixe
tail -f logs/app.log | grep "\[automation\]"  # Logs d'automatisation
tail -f logs/app.log | grep "\[api\]"          # Logs API
tail -f logs/app.log | grep "\[scheduler\]"    # Logs scheduler

# Health check pour monitoring externe
curl -s http://localhost:5000/healthz | jq '.status, .api_requests_remaining'
```

### Intégration Monitoring Externe
Pour la production, configurez votre outil de monitoring :

**Prometheus (exemple) :**
```yaml
scrape_configs:
  - job_name: 'switchbot-dashboard'
    static_configs:
      - targets: ['localhost:5000']
    metrics_path: '/healthz'
    scrape_interval: 30s
```

**Alertes recommandées :**
- Quota API < 100 requêtes restantes
- Scheduler not running
- Temperature stale > 10 minutes
- Taux d'erreurs > 1%

> 📚 **Documentation complète** : Consultez [Gestion des Erreurs](switchbot/error-handling.md) pour les patterns détaillés, [Optimisations Performance](switchbot/performance-optimizations.md) pour le monitoring avancé, et [Patterns d'Automatisation](automation-patterns.md) pour la cascade IFTTT.

## Performance Frontend & Core Web Vitals

### Optimisations Phase 5 (Core Web Vitals Avancées)
- **Critical CSS Inlining** : CSS essentiel inlined dans `<head>` pour rendu immédiat
- **Resource Hints** : Preconnects CDN, preloads CSS/JS/fonts critiques
- **Font Loading** : `font-display: swap` + preloads pour éliminer FOIT/FOUT
- **GPU Acceleration** : Transform `translateZ(0)` et animations optimisées
- **CLS Prevention** : Skeleton screens et dimensions explicites
- **Performance Monitoring** : PerformanceObserver API pour LCP/FID/CLS temps réel

### Système de Loaders Frontend
- **Loaders non bloquants** : Feedback visuel immédiat lors actions utilisateur
- **Timeouts configurés** : 5s formulaires, 3s actions, 2s navigation
- **Accessibilité** : Attributs ARIA complets, gestion clavier
- **Performance** : Animations GPU avec `transform` et `opacity`

## Performance & Résilience (Post-Audit Backend)

> 🎯 **Audit Backend Validé** : Score 95/100 - Voir [Rapport Complet d'Audit](backend-audit-report.md) pour l'analyse détaillée

### Batch insert HistoryService
Le service d'historique utilise un buffer thread-safe pour optimiser les performances :
- Buffer `_pending_records` avec verrou `_pending_lock`
- Flush automatique sur `batch_size` (4) ou timer (60 secondes)
- Remplacement de `psycopg.extras.execute_values` par SQL manuel
- Réduction de 50% de la latence par tick d'automatisation

### Tests robustes avec mocks centralisés
- `tests/conftest.py` fournit une fixture autouse pour patcher `ConnectionPool`
- 122 tests passants (99% de réussite) avec mocks PostgreSQL optimisés
- BaseStore marqué `@runtime_checkable` pour les assertions isinstance

### Cache timezone AutomationService
Pour éviter les résolutions répétées de fuseau horaire :
- Cache simple : `_cached_timezone_key` et `_cached_timezone_value`
- Invalidation automatique lors du changement des settings
- Utilisation de `ZoneInfo` avec fallback UTC

### Wrapper try/catch global SchedulerService
Pour une résilience maximale du scheduler :
- Méthode `_run_tick_safe()` enveloppe `_tick_callable`
- Toutes les exceptions loguées avec `exc_info=True`
- Pas de crash du scheduler en cas d'erreur dans l'automatisation

## History Monitoring Dashboard

Le dashboard expose un système de monitoring temps réel accessible via `/history` :

### Fonctionnalités
- **Graphiques temps réel** : Température & Humidité, État climatisation
- **Filtres interactifs** : Plages horaires, granularité (minute/5min/15min/heure)
- **Rétention 6 heures** : Alignée sur PITR Neon avec cleanup automatique
- **API REST** : 3 endpoints `/history/api/*` pour les données

### Configuration requise
- Backend PostgreSQL (Neon recommandé)
- Variables existantes : `POSTGRES_URL`, `STORE_BACKEND=postgres`

> 📚 **Documentation complète** : Consultez [History Monitoring Guide](history-monitoring.md)
> 📚 **Audit Backend** : Voir [Audit Backend - Rapport Complet](backend-audit-report.md) pour l'analyse détaillée des performances et résilience

### 3. Stockage persistant (PostgreSQL par défaut)

Le tableau de bord utilise PostgreSQL comme backend principal avec fallback filesystem automatique :

#### Configuration par défaut (Recommandée)
| Variable | Description | Valeur par défaut |
|----------|-------------|-------------------|
| `STORE_BACKEND` | Backend de stockage | `postgres` |
| `POSTGRES_URL` | URL PostgreSQL Neon | `postgresql://...` |
| `POSTGRES_SSL_MODE` | Mode SSL | `require` |

#### PostgreSQL (Recommandé)

**Avantages :**
- Architecture simplifiée (un seul backend)
- Coût prévisible (Neon free tier suffisant)
- Fonctionnalités avancées (JSONB, PITR, extensions)
- Meilleure intégration avec Render

**Configuration PostgreSQL optimisée** :
```bash
STORE_BACKEND=postgres
POSTGRES_URL=postgresql://user:password@ep-xxx.aws.neon.tech/dbname?sslmode=require
POSTGRES_SSL_MODE=require
```

**Performances** :
- Connection pooling via `psycopg_pool.ConnectionPool` (1-10 connexions)
- Batch insert HistoryService pour -50% latence
- Indexes temporels optimisés pour requêtes monitoring
- Fallback automatique vers JsonStore en cas d'indisponibilité

**Migration** : Voir [PostgreSQL Migration Guide](postgresql-migration.md)

#### Backend legacy (déprécié)

| Variable | Description | Statut |
|----------|-------------|--------|
| `STORE_BACKEND` | `redis` ou `filesystem` | Déprécié/Fallback |
| `REDIS_URL_PRIMARY` | URL Redis principale | Déprécié |
| `REDIS_URL_SECONDARY` | URL Redis secondaire | Déprécié |
| `REDIS_URL` | Legacy URL Redis unique | Déprécié |
| `REDIS_PREFIX` | Préfixe pour les clés | Déprécié |
| `REDIS_TTL_SECONDS` | Durée de vie des clés | Déprécié |
| `SWITCHBOT_SETTINGS_PATH` | Chemin du fichier de configuration | Fallback |
| `SWITCHBOT_STATE_PATH` | Chemin du fichier d'état | Fallback |

> ⚠️ **Note** : PostgreSQL est maintenant le backend recommandé. Redis reste disponible pour compatibilité mais est considéré comme déprécié.
> 
> 📝 **Note historique** : Redis était le backend recommandé avant la migration PostgreSQL du 14 janvier 2026. Il reste disponible pour compatibilité mais PostgreSQL offre une architecture simplifiée et de meilleures performances.

> ❗️ **Depuis la build du 25 janvier 2026, `STORE_BACKEND=redis` n'est plus honoré.**
> `create_app()` (@switchbot_dashboard/__init__.py#78-85) force désormais un retour immédiat vers `JsonStore` avec un warning `[store] Redis backend is deprecated...`. Gardez ces variables uniquement pour les anciennes versions du projet ; dans la branche principale actuelle, elles n'ont plus d'effet au runtime.

#### Recommandations de déploiement

**Pour les environnements conteneurisés (Docker, Render) :**
- Utilisez PostgreSQL (Neon) pour une persistance fiable et simplifiée
- Configurez `STORE_BACKEND=postgres` et `POSTGRES_URL`
- Le mode `redis` est déprécié mais reste disponible pour compatibilité

**Pour le développement local :**
- Le mode `filesystem` est suffisant
- Les données sont stockées dans `config/settings.json` et `config/state.json`

#### Migration vers PostgreSQL

1. **Prérequis** : Compte Neon PostgreSQL (free tier suffisant)
2. **Migration** : Utilisez le script de migration automatique
   ```bash
   python scripts/migrate_to_postgres.py \
       --postgres-url "postgresql://user:password@ep-xxx.aws.neon.tech/dbname?sslmode=require" \
       --dry-run  # Validation d'abord
   ```
3. **Documentation** : Voir [PostgreSQL Migration Guide](postgresql-migration.md)

#### Migration vers Redis (historique, non supporté sur `main`)

Ces étapes sont conservées pour documenter les anciennes versions (< 2026-01-25). Elles **ne fonctionnent plus** sur la branche courante : même avec `STORE_BACKEND=redis`, l'application reviendra sur `JsonStore`.

1. *(Legacy)* Sauvegardez vos fichiers de configuration actuels :
   ```bash
   cp config/settings.json config/settings.json.bak
   cp config/state.json config/state.json.bak
   ```

2. *(Legacy)* Créez une instance Redis (par exemple via Render ou Upstash)

3. *(Legacy)* Exportez les variables d'environnement :
   ```bash
   export STORE_BACKEND=redis
   export REDIS_URL_PRIMARY=rediss://default:password@host:port
   export REDIS_URL_SECONDARY=rediss://default:password@host2:port2
   export REDIS_PREFIX=switchbot_dashboard
   ```

4. *(Legacy)* (Optionnel) Importez les données existantes :
   ```bash
   redis-cli -u $REDIS_URL_PRIMARY SET ${REDIS_PREFIX}:settings "$(cat config/settings.json)"
   redis-cli -u $REDIS_URL_PRIMARY SET ${REDIS_PREFIX}:state "$(cat config/state.json)"
   redis-cli -u $REDIS_URL SET ${REDIS_PREFIX}:settings "$(cat config/settings.json)"
   redis-cli -u $REDIS_URL SET ${REDIS_PREFIX}:state "$(cat config/state.json)"
   ```

5. *(Legacy)* Redémarrez le service et vérifiez que les paramètres sont chargés correctement

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

### Cooldown adaptatif

Le système de cooldown empêche les commandes répétées trop rapprochées. Le **cooldown adaptatif** (introduit le 2026-01-11) différencie le délai selon le type d'action :

**Nouveaux paramètres** :
- `action_on_cooldown_seconds` : Durée de blocage après un **démarrage** (chauffage/climatisation ON)
  - Recommandé : `300` (5 minutes) pour laisser le climatiseur monter en température
- `action_off_cooldown_seconds` : Durée de blocage après un **arrêt** (climatisation OFF)
  - Recommandé : `60` (1 minute) car l'arrêt est instantané
- `command_cooldown_seconds` : Valeur par défaut (rétro-compatibilité) si les paramètres adaptatifs ne sont pas définis

**Comportement** :

Scénario hiver (température < min_temp) :
```
1. Tick à 14:00:00 : Lance "winter" → assumed_aircon_power="on"
2. Tick à 14:01:00 : Température encore < min_temp
   → Cooldown ON actif (1min < 5min) → Aucune action
   → Log : [automation] Cooldown active (ON action) | remaining_time='4m0s'
3. Ticks suivants : Cooldowns actifs pendant 5 minutes
   → Laisse le temps au climatiseur de diffuser la chaleur
4. Tick à 14:05:01 : Cooldown expiré (5min01s > 5min) 
   → Nouvelle action possible si nécessaire
```

**Rationale** :
- ✅ **5 minutes après démarrage** : Latence physique de la pompe à chaleur (~5min pour diffuser aux splits intérieurs)
- ✅ **1 minute après arrêt** : Réactivité maintenue car l'arrêt est instantané
- ✅ **Économie de quotas API** : Évite les appels inutiles pendant la stabilisation
- ✅ **Logs explicites** : Affiche le type de cooldown (ON/OFF/default) et le temps restant

**Configuration recommandée** :
```json
{
  "command_cooldown_seconds": 60,
  "action_on_cooldown_seconds": 300,
  "action_off_cooldown_seconds": 60
}
```

**Rétro-compatibilité** : Si les paramètres adaptatifs ne sont pas définis, le système utilise `command_cooldown_seconds` pour toutes les actions.

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

### Endpoints utilitaires (Quota & Debug)

#### POST `/quota/refresh`
- **Objectif** : Normaliser l'instantané du quota même si aucune requête SwitchBot n'a encore eu lieu depuis minuit.
- **Fonctionnement** :
  - Appelle `ApiQuotaTracker.record_call()` (pour s'assurer que le compteur reste cohérent) puis `refresh_snapshot()` qui réécrit `api_quota_day`, `api_requests_limit`, `api_requests_total` et `api_requests_remaining`.
  - Redirige vers `/quota` avec un flash `success` (“Quota mis à jour.”). Le formulaire côté UI utilise `data-loader="card"` pour afficher un loader local.
- **Cas d'usage** :
  - Après modification manuelle de `api_requests_limit` (ex. import de sauvegarde).
  - Avant une journée de forte utilisation pour repartir d'un compteur propre.
  - Lorsque `api_quota_day` semble ne pas refléter la date actuelle suite à un redeploy.
- **Tests** : `tests/test_dashboard_routes.py::test_quota_refresh_normalizes_state_and_shows_flash`.

#### GET `/debug/state`
- **Objectif** : Offrir une lecture JSON formatée de `state.json` pour le support/diagnostic (lecture seule).
- **Sécurité** :
  - Protégé par `STATE_DEBUG_TOKEN` (défini dans l'environnement Render/Gunicorn dans `create_app()`).
  - Accès via `/debug/state?token=<STATE_DEBUG_TOKEN>`. Sans token valide → `404`.
- **Contenu** : Retourne toutes les clés persistées (`pending_off_repeat`, `api_requests_*`, `assumed_aircon_power`, flags stale, etc.) avec indentation.
- **Bonnes pratiques** :
  - N'activer le token que lorsque nécessaire et le régénérer régulièrement.
  - Garder cet endpoint privé (support interne, outils de supervision) puisqu'il expose l'état opérationnel complet.
- **Lecture seule** : aucun moyen de modifier le state via ce point d'entrée.

---

*Voir aussi [Guide UI](ui-guide.md) pour l'interaction avec les formulaires, [Tests](testing.md) pour la validation, et `memory-bank/systemPatterns.md` pour les patterns architecturaux.*

## Timezone-Aware Automation

The system now handles timezones explicitly for automation windows:

- **Default Timezone**: Europe/Paris
- **Configuration**: Set via `timezone` field in settings (IANA identifier)
- **Fallback**: UTC if invalid timezone provided
- **Implementation**:
  - `AutomationService` uses `zoneinfo` for conversions
  - Windows evaluated in local time
  - Logs include timezone context

## OFF Repeat Functionality

Parameters:
- `off_repeat_count`: Number of OFF commands to send (default: 2)
- `off_repeat_interval_seconds`: Delay between OFF commands (default: 10)

Behavior:
- Scheduled via `AutomationService._schedule_off_repeat_task()`
- State tracked in `pending_off_repeat`
- Idempotence: No new OFF actions if `assumed_aircon_power == "off"`
- Cancelled by ON actions

## Idempotence for OFF Actions

The system prevents duplicate OFF actions when:
- Aircon is already assumed OFF
- Pending OFF repeats exist
- Within cooldown period

Log messages clearly indicate when actions are skipped due to idempotence checks.

---

## Références croisées

### Documentation technique
- [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) – Standards de développement obligatoires
- [DOCUMENTATION.md](DOCUMENTATION.md) – Architecture et métriques
- [setup.md](setup.md) – Installation et configuration initiale

### Guides spécialisés
- [Intégration IFTTT](ifttt-integration.md) – Configuration webhooks et cascade
- [Migration PostgreSQL](postgresql-migration.md) – Guide de migration vers Neon
- [Guide du scheduler](scheduler.md) – Configuration et dépannage

### Memory Bank (décisions architecturales)
- `memory-bank/decisionLog.md` – Décisions de configuration (quotas, webhooks, timezone)
- `memory-bank/systemPatterns.md` – Patterns de stockage et cascade
- `memory-bank/productContext.md` – Vue d'ensemble du projet

---

*Ce document fait partie de la documentation structurée du SwitchBot Dashboard. Retour au [README principal](README.md).*
