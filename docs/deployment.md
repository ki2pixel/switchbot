# Déploiement Render + GitHub Container Registry

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

Ce guide décrit comment construire l'image Docker du SwitchBot Dashboard, la publier sur GitHub Container Registry (GHCR) via GitHub Actions, puis déclencher un déploiement Render (plan Free).

> 📝 **Décisions connexes** : Les patterns de déploiement sont documentés dans `memory-bank/decisionLog.md` (2026-01-09 22:05) et les standards de production dans `.windsurf/rules/codingstandards.md`.

## 1. Pré-requis

- **Compte GitHub** avec accès au repo `ki2pixel/switchbot` et aux GitHub Actions.
- **Compte Render** (plan Free suffisant) avec un service Web existant ou à créer.
- **Secrets Render** :
  - `RENDER_DEPLOY_WEBHOOK_URL` : URL fournie par Render pour déclencher les déploiements.
  - `RENDER_API_KEY` : clé API pour fallback.
  - `RENDER_SERVICE_ID` : identifiant du service Render (visible dans l'URL du dashboard).
- **Secrets SwitchBot** : `SWITCHBOT_TOKEN` et `SWITCHBOT_SECRET` seront définis côté Render (pas dans GitHub Actions).

## 2. Dockerfile

Le fichier `Dockerfile` à la racine :

- Image de base `python:3.11-slim`.
- Installation des dépendances via `requirements.txt` (incluant Gunicorn).
- Création utilisateur non root `appuser`.
- Démarrage via `gunicorn 'switchbot_dashboard:create_app()'` (port 8000, logs stdout/stderr, timeout 120s, niveau de log configurable via LOG_LEVEL).
- Worker unique obligatoire : `gunicorn.conf.py` force `WEB_CONCURRENCY=1` et s'appuie sur 2 threads pour absorber les requêtes tout en laissant APScheduler tourner dans le même process (évite les ticks dupliqués).
- Variables :
  - `PORT` (Render fournit automatiquement la valeur).
  - `WEB_CONCURRENCY` (laissez `1` – toute autre valeur est ignorée et peut provoquer des comportements indésirables).

`.dockerignore` exclut les fichiers inutiles (`.git`, `__pycache__`, JSON locaux...).

## 3. Workflow GitHub Actions (`.github/workflows/build-and-push.yml`)

### Déclencheurs
- `push` sur `main`.
- `workflow_dispatch` (lancement manuel).

### Étapes principales
1. Checkout du repo.
2. Setup Docker Buildx.
3. Login GHCR via `GITHUB_TOKEN`.
4. Build + push de l'image :
   - `ghcr.io/ki2pixel/switchbot:latest`
   - `ghcr.io/ki2pixel/switchbot:${{ github.sha }}`
5. Trigger Render :
   - POST sur `RENDER_DEPLOY_WEBHOOK_URL` (payload JSON avec `sha` et `image`).
   - Si code HTTP non 2xx → fallback API `POST https://api.render.com/v1/services/{SERVICE_ID}/deploys` avec `Authorization: Bearer RENDER_API_KEY`.
   - ⚠️ Le job GitHub échoue immédiatement si le webhook n'est pas défini **ou** si `RENDER_API_KEY` / `RENDER_SERVICE_ID` sont absents (le fallback exige ces deux secrets simultanément).

### Secrets GitHub requis
- `RENDER_DEPLOY_WEBHOOK_URL`
- `RENDER_API_KEY`
- `RENDER_SERVICE_ID`

### Variables GitHub optionnelles
- Aucun besoin spécifique (l'image référence directement `ghcr.io/ki2pixel/switchbot`).

## 4. Configuration du service Render

1. Créer un **Web Service** (plan Free) utilisant une image externe :
   - Image : `ghcr.io/ki2pixel/switchbot:latest` (Render tirera automatiquement la dernière version). 
   - Commande de démarrage : `gunicorn 'switchbot_dashboard:create_app()' --bind 0.0.0.0:${PORT} --workers 1 --threads 2 --timeout 120`.
2. Variables d'environnement Render :
   - `SWITCHBOT_TOKEN` (secret).
   - `SWITCHBOT_SECRET` (secret).
   - `SWITCHBOT_RETRY_ATTEMPTS`, `SWITCHBOT_RETRY_DELAY_SECONDS` si besoin.
   - `SWITCHBOT_POLL_INTERVAL_SECONDS` pour override.
   - `WEB_CONCURRENCY=1` (obligatoire pour aligner Gunicorn sur le worker unique; la configuration du dépôt force déjà cette valeur, mais la redéfinir garantit que l’interface Render reflète le comportement réel).
   - `LOG_LEVEL` (optionnel mais recommandé) : Niveau de log propagé à Gunicorn via `--log-level ${LOG_LEVEL:-info}` dans le `Dockerfile`. Utiliser `warning` ou `error` en production pour réduire le bruit, `debug`/`info` lors des diagnostics.
   - `FLASK_SECRET_KEY` (secret aléatoire).
   - `STORE_BACKEND=postgres` (valeur par défaut côté application). Définir `POSTGRES_URL`/`POSTGRES_SSL_MODE` pour Neon.
   - `REDIS_URL_PRIMARY`, `REDIS_URL_SECONDARY`, `REDIS_URL`, `REDIS_PREFIX`, `REDIS_TTL_SECONDS` : **variables legacy conservées pour les anciennes versions**. Depuis la build du 25 janvier 2026, `create_app()` force un fallback `JsonStore` même si `STORE_BACKEND=redis` est défini ; ces variables n'ont donc plus d'effet sur la branche principale.
   - **IFTTT Webhooks** (optionnel) : Variables pour les timeouts et configuration réseau si nécessaire :
     - `IFTTT_TIMEOUT_SECONDS` : Timeout pour les requêtes IFTTT (défaut : 10s)
     - `IFTTT_RETRY_ATTEMPTS` : Nombre de tentatives pour les webhooks (défaut : 1)
   - `SCHEDULER_ENABLED` : Active/désactive le scheduler interne (défaut : true)
3. Activer les logs sur Render : par défaut, Gunicorn écrit sur stdout/stderr, visibles dans l'onglet Logs.

### Impact des webhooks IFTTT sur le quota et monitoring

**Avantages pour le quota API** :
- Les webhooks IFTTT ne consomment pas le quota SwitchBot (10 000/jour)
- Seuls les fallbacks (scènes ou commandes directes) consomment le quota
- Économie significative en production avec automatisation fréquente

**Monitoring spécifique IFTTT** :
- Logs préfixés `[ifttt]` pour les actions webhook
- Logs préfixés `[automation]` pour les fallbacks
- Surveiller les timeouts : `IFTTT webhook timeout after 10s`
- Vérifier les fallbacks : `Using SwitchBot scene (webhook unavailable)`

**Recommandations de monitoring Render** :
1. **Surveiller les logs IFTTT** : Rechercher `[ifttt]` dans les logs Render
2. **Alertes sur les fallbacks** : Trop de fallbacks peuvent indiquer un problème IFTTT
3. **Quota API** : Avec IFTTT, le quota devrait rester stable même avec forte automatisation

### Configuration Redis haute disponibilité (historique)

> ℹ️ **Référence legacy** : Ces instructions documentent l'ancienne architecture (avant le 25 janvier 2026). Depuis cette date, même avec `STORE_BACKEND=redis`, l'application revient systématiquement sur `JsonStore`. Conservez cette section uniquement pour dépanner des déploiements figés sur d'anciennes releases.

Pour mémoire :

1. **Instance primaire** : Upstash Redis (plan Free suffisant)
2. **Instance secondaire** : Render Redis ou autre fournisseur
3. **Variables Render** :
   ```bash
   STORE_BACKEND=redis
   REDIS_URL_PRIMARY=rediss://default:password@primary-host:6379/0
   REDIS_URL_SECONDARY=rediss://default:password@secondary-host:6379/0
   REDIS_PREFIX=switchbot_dashboard:prod
   ```

**Comportement historiquement observé** : priorité primaire → secondaire → filesystem avec cooldown 60 s et logs `[store] ... failed`.

> ✅ **Branches actives** : Ignorez cette section et utilisez PostgreSQL + fallback filesystem. Seules les variables IFTTT listées ci-dessous restent pertinentes.

**Variables d'environnement recommandées pour IFTTT** :
```bash
# Pour réduire le bruit dans les logs en production
LOG_LEVEL=warning

# Pour augmenter la fiabilité des webhooks (réseau lent)
IFTTT_TIMEOUT_SECONDS=15
```

## 5. Surveillance et santé de l'application - [2026-01-10]

### Endpoint de santé (`/healthz`)

L'application expose un endpoint de santé qui peut être utilisé pour la surveillance et le monitoring :

```
GET /healthz
```

**Réponse en cas de succès (200 OK) :**
```json
{
  "status": "ok",
  "scheduler_running": true,
  "automation_enabled": true,
  "last_tick": "2024-01-10T14:30:00Z",
  "last_read_at": "2024-01-10T14:29:45Z",
  "temperature_stale": false,
  "api_requests_total": 42,
  "api_requests_remaining": 958,
  "api_quota_day": "2024-01-10",
  "version": "1.0.0"
}
```

**Champs de la réponse :**
- `status` : État global de l'application (`ok`, `warning` ou `error`)
- `scheduler_running` : Indique si le planificateur d'automatisation est actif
- `automation_enabled` : Indique si l'automatisation est activée
- `last_tick` : Dernière exécution du planificateur (ISO 8601)
- `last_read_at` : Dernière lecture réussie du capteur de température
- `temperature_stale` : Indique si la température actuelle est potentiellement obsolète
- `api_requests_total` : Nombre total de requêtes API effectuées aujourd'hui
- `api_requests_remaining` : Nombre de requêtes API restantes avant d'atteindre la limite quotidienne
- `api_quota_day` : Date de réinitialisation du quota (minuit UTC)
- `version` : Version de l'application

**Codes de statut HTTP :**
- `200 OK` : L'application fonctionne normalement
- `503 Service Unavailable` : L'application rencontre des problèmes critiques (ex: store inaccessible)

**Utilisation avec des outils de monitoring :**
- **Render** : Configurer des checks de santé dans le dashboard Render
- **Uptime Kuma** : Surveiller la disponibilité avec des requêtes périodiques
- **Prometheus/Grafana** : Récupérer les métriques pour des tableaux de bord avancés

**Exemple de configuration pour Uptime Kuma :**
- URL : `https://votre-app.onrender.com/healthz`
- Méthode : `GET`
- Intervalle : 5 minutes
- Seuil d'alerte : Code de statut != 200 OU `status != "ok"`

### Logs Render et monitoring - [2026-01-12]

#### Logs structurés pour le diagnostic

Le système génère des logs structurés avec préfixes pour faciliter le diagnostic dans les logs Render :

```bash
# Logs IFTTT
[ifttt] IFTTT webhook triggered successfully | status_code=200, url=https://maker.ifttt.com/trigger/...
[ifttt] IFTTT webhook failed | action_key=winter, error=timeout

# Logs d'automatisation
[automation] Automation tick started | trigger=scheduler, interval=60s
[automation] Using SwitchBot scene (webhook unavailable) | action_key=winter, scene_id=scene-w
[automation] Scheduled repeated off action | pending_repeats=1, interval_seconds=10

# Logs de santé
[health] Health check completed | status=ok, scheduler_running=true

# Logs de répétition OFF
[automation] Executing scheduled off repeat | trigger=scheduler, state_reason=automation_winter_off, remaining_before=1
[automation] Cleared pending off repeat task
```

#### Commandes de recherche dans les logs Render

```bash
# Filtrer les logs IFTTT
grep "\[ifttt\]" /var/log/switchbot_dashboard.log

# Rechercher les fallbacks
grep "fallback" /var/log/switchbot_dashboard.log

# Surveiller les erreurs
grep -i "error\|failed" /var/log/switchbot_dashboard.log

# Logs de répétition OFF
grep "off repeat" /var/log/switchbot_dashboard.log

# Logs de quota API
grep "quota" /var/log/switchbot_dashboard.log
```

#### Alertes et seuils recommandés

**Configuration recommandée pour le monitoring :**
- **Fréquence** : Toutes les 5 minutes
- **Seuils d'alerte :**
  - `status != "ok"` → Critique
  - `scheduler_running == false` → Avertissement
  - `last_tick` > 10 minutes → Critique
  - `api_requests_remaining` < 100 → Avertissement
  - `api_requests_remaining` < 50 → Critique
  - `temperature_stale == true` → Avertissement

**Outils recommandés :**
- **Render Health Checks** : Surveillance nat intégrée
- **Uptime Kuma** : Surveillance externe de la disponibilité
- **Prometheus** : Collecte des métriques personnalisées
- **Grafana** : Tableaux de bord de surveillance avancés
- **AlertManager** : Gestion des alertes personnalisées

## 6. Processus de déploiement

1. Commit + push sur `main` (ou lancer manuellement le workflow).
2. GitHub Actions construit et pousse l'image sur GHCR.
3. Le workflow appelle le webhook Render ; en cas d'échec il utilise l'API (fallback).
4. Render déploie la nouvelle image. Suivre la progression dans Render Dashboard.
5. Vérifier que l'endpoint `/healthz` répond avec le statut `200 OK` après le déploiement.

## 6. Tests & validation

### Local
- `docker build -t switchbot:local .`
- `docker run -it --rm -p 8000:8000 --env-file=.env switchbot:local`
- Vérifier l'interface utilisateur : `http://localhost:8000`
- Tester l'endpoint de santé :
  ```bash
  # Vérifier le statut de santé
  curl -v http://localhost:8000/healthz
  
  # Vérifier les métriques de quota
  curl -s http://localhost:8000/healthz | jq '{
    status: .status,
    requests_remaining: .api_requests_remaining,
    last_tick: .last_tick
  }'
  ```
- Vérifier les logs pour les erreurs potentielles : `docker logs <container_id>`
- Tester le comportement en cas d'erreur :
  ```bash
  # Simuler une erreur de store
  docker run -it --rm -p 8000:8000 -e STORE_BACKEND=invalid --env-file=.env switchbot:local
  # Vérifier que /healthz retourne 503
  curl -v http://localhost:8000/healthz
  ```

### GitHub Actions
- Lancer `workflow_dispatch` en fournissant la branche.
- Vérifier que l'image apparaît dans `https://github.com/ki2pixel/switchbot/pkgs/container/switchbot`.

### Render
- Après le déploiement, effectuer les vérifications suivantes :
  - **Logs** : Vérifier les logs de déploiement pour les erreurs Gunicorn/APScheduler
  - **Interface utilisateur** : S'assurer que la page `/` se charge correctement
  - **Scènes SwitchBot** : Vérifier que les scènes sont correctement configurées et accessibles
  - **Endpoint de santé** : Tester `https://<service>.onrender.com/healthz` :
    ```json
    {
      "status": "ok",
      "scheduler_running": true,
      "automation_enabled": true,
      "last_tick": "2024-01-10T15:30:00Z",
      "api_requests_total": 0,
      "api_requests_remaining": 1000,
      "api_quota_day": "2024-01-10",
      "version": "1.0.0"
    }
    ```
  - **Surveillance** : Configurer des vérifications de santé externes (comme UpTimeRobot) pour surveiller l'endpoint `/healthz`
  - **Alertes** : Configurer des alertes pour les problèmes détectés via l'endpoint de santé

## 7. Configuration des scènes en production

### Configuration recommandée

1. **Créer les scènes dans l'application SwitchBot** :
   - Hiver : Configuration de chauffage (ex: 20°C, mode chauffage)
   - Été : Configuration de climatisation (ex: 24°C, mode froid)
   - Ventilation : Mode ventilateur uniquement
   - Arrêt : Éteindre le climatiseur

2. **Récupérer les UUID** :
   - Via l'API SwitchBot (`GET /v1.1/scenes`)
   - Ou depuis l'application mobile (Paramètres > Aide > À propos > Détails de l'API)

3. **Configurer dans Render** :
   - Ajouter les variables d'environnement suivantes :
     ```
     AIRCON_SCENES_WINTER=scene_winter_uuid
     AIRCON_SCENES_SUMMER=scene_summer_uuid
     AIRCON_SCENES_FAN=scene_fan_uuid
     AIRCON_SCENES_OFF=scene_off_uuid
     TURN_OFF_OUTSIDE_WINDOWS=true
     ```
   - Redémarrer le service après configuration

4. **Vérification** :
   - Accéder à l'interface d'administration
   - Vérifier que les boutons de scène sont actifs (verts)
   - Tester chaque scène manuellement
   - Vérifier les logs pour les erreurs potentielles

## 8. Configuration réseau IFTTT

### Exigences réseau

Les webhooks IFTTT nécessitent une configuration réseau spécifique pour fonctionner correctement en production :

- **HTTPS obligatoire** : Les URLs doivent commencer par `https://` (HTTP non autorisé)
- **Sortie TLS 1.2+** : Render supporte TLS 1.2 et 1.3 pour les connexions sortantes
- **Timeout par défaut** : 10 secondes pour les requêtes IFTTT
- **Ports autorisés** : 443 (HTTPS) pour maker.ifttt.com

### Variables de configuration

```bash
# Timeout pour les requêtes IFTTT (optionnel)
IFTTT_TIMEOUT_SECONDS=10

# Nombre de tentatives pour les webhooks (optionnel)
IFTTT_RETRY_ATTEMPTS=1
```

### Test de connectivité

Pour vérifier que votre instance Render peut atteindre IFTTT :

```bash
# Depuis le conteneur Render
curl -I https://maker.ifttt.com

# Test avec un webhook de test
curl -X POST https://maker.ifttt.com/trigger/test/with/key/YOUR_KEY \
  -H "Content-Type: application/json" \
  -d '{"test": "connectivity"}'
```

### Dépannage réseau

- **Timeouts** : Augmentez `IFTTT_TIMEOUT_SECONDS` si les réseaux sont lents
- **DNS** : Vérifiez que `maker.ifttt.com` résout correctement
- **Firewall** : Assurez-vous que le port 443 sortant est autorisé
- **TLS** : Vérifiez la compatibilité des certificats avec Render

## 9. Checklist de secrets

| Emplacement | Secret | Description |
|-------------|--------|-------------|
| GitHub → Settings → Secrets → Actions | `RENDER_DEPLOY_WEBHOOK_URL` | URL pour déclencher un deploy Render (obligatoire même si l'API fallback est utilisée) |
| GitHub → Settings → Secrets → Actions | `RENDER_API_KEY` | Clé API Render pour fallback (doit être présente avec `RENDER_SERVICE_ID`) |
| GitHub → Settings → Secrets → Actions | `RENDER_SERVICE_ID` | Identifiant du service Render (nécessaire avec `RENDER_API_KEY` pour le fallback) |
| Render → Environment | `SWITCHBOT_TOKEN` | Token SwitchBot API |
| Render → Environment | `SWITCHBOT_SECRET` | Secret SwitchBot API |
| Render → Environment | `FLASK_SECRET_KEY` | Secret Flask |
| Render → Environment | `WEB_CONCURRENCY` (optionnel) | Nombre de workers Gunicorn |
| Render → Environment | `STORE_BACKEND` | `filesystem` (défaut) ou `redis`. Recommandé : `redis` pour la persistance |
| Render → Environment | `REDIS_URL` | URL TLS de l'instance Redis Render |
| Render → Environment | `REDIS_PREFIX` (optionnel) | Préfixe de clés pour isoler plusieurs environnements |
| Render → Environment | `REDIS_TTL_SECONDS` (optionnel) | TTL des données stockées dans Redis |

## 8. Bonnes pratiques

- **Pipeline minutes** : le build GHCR côté GitHub évite de consommer les minutes Render.
- **Sécurité** : ne jamais commiter `.env`. Utiliser les secrets Render/GitHub.
- **Logs** :
  - Gunicorn écrit via `--access-logfile -` et `--error-logfile -` (donc visibles dans Render).
  - Ajuster `LOG_LEVEL` selon le contexte : `info` par défaut, `warning` en production stable, `debug` temporairement lors d'une investigation (revenir ensuite à `info` pour limiter la verbosité).
- **Fallback** : surveiller la sortie du job GitHub pour voir si le webhook a réussi ou si le fallback API a été nécessaire.

---

## Références croisées

### Documentation technique
- [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) – Standards de développement obligatoires
- [DOCUMENTATION.md](DOCUMENTATION.md) – Architecture et métriques
- [setup.md](setup.md) – Installation locale et configuration initiale
- [configuration.md](configuration.md) – Variables d'environnement et paramètres

### Guides spécialisés
- [Migration PostgreSQL](postgresql-migration.md) – Configuration Neon
- [Guide du scheduler](scheduler.md) – Configuration APScheduler en production
- [testing.md](testing.md) – Tests et validation post-déploiement

### Memory Bank (décisions architecturales)
- `memory-bank/decisionLog.md` – Décisions de déploiement (Docker, GHCR, Render)
- `memory-bank/systemPatterns.md` – Patterns de stockage et cascade

---

*Ce guide complète `docs/setup.md` (installation locale) et `docs/testing.md` (scénarios de validation).*
