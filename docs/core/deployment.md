# Déploiement SwitchBot Dashboard v2

**TL;DR** : Build Docker sur GitHub Actions → push GHCR → webhook Render → déploiement automatique avec monitoring santé intégré.

## Pourquoi ce déploiement ?

Vous avez un dashboard qui doit tourner 24/7 sans intervention manuelle. Chaque push sur main doit déclencher un déploiement immédiat, et vous voulez surveiller la santé de l'application sans vous connecter à Render.

Le problème classique ? Les déploiements manuels oublient des variables d'environnement. Les webhooks IFTTT tombent en silence. Le quota API s'épuise sans alerte. Vous perdez des heures à diagnostiquer pourquoi l'automatisation ne fonctionne plus.

## L'architecture : Docker + GHCR + Render

La solution repose sur trois piliers :

1. **Dockerfile** : Image Python 3.11-slim avec Gunicorn, worker unique obligatoire pour éviter les ticks APScheduler dupliqués
2. **GitHub Actions** : Build + push sur GHCR, puis webhook Render avec fallback API
3. **Render** : Service Web avec santé intégrée via `/healthz`, logs structurés et variables d'environnement sécurisées

Le flux est simple : push → build → deploy → monitor. Aucune intervention manuelle après la configuration initiale.

## Le code et la configuration

### Dockerfile à la racine

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN adduser --disabled-password --gecos '' appuser
USER appuser

EXPOSE 8000

CMD ["gunicorn", "switchbot_dashboard:create_app()", \
     "--bind", "0.0.0.0:${PORT:-8000}", \
     "--workers", "1", \
     "--threads", "2", \
     "--timeout", "120", \
     "--log-level", "${LOG_LEVEL:-info}", \
     "--access-logfile", "-", \
     "--error-logfile", "-"]
```

**Variables critiques** :
- `PORT` : Render fournit automatiquement la valeur
- `WEB_CONCURRENCY=1` : Obligatoire, toute autre valeur est ignorée
- `LOG_LEVEL` : `warning` en production, `debug` temporairement pour diagnostics

### Workflow GitHub Actions

```yaml
name: Build and Deploy

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
        
      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
          
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: |
            ghcr.io/ki2pixel/switchbot:latest
            ghcr.io/ki2pixel/switchbot:${{ github.sha }}
            
      - name: Trigger Render
        run: |
          curl -X POST ${{ secrets.RENDER_DEPLOY_WEBHOOK_URL }} \
            -H "Content-Type: application/json" \
            -d '{"sha":"${{ github.sha }}","image":"ghcr.io/ki2pixel/switchbot:${{ github.sha }}"}' || \
          curl -X POST https://api.render.com/v1/services/${{ secrets.RENDER_SERVICE_ID }}/deploys \
            -H "Authorization: Bearer ${{ secrets.RENDER_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{"imageUrl":"ghcr.io/ki2pixel/switchbot:${{ github.sha }}"}'
```

**Secrets GitHub requis** :
- `RENDER_DEPLOY_WEBHOOK_URL` : URL webhook Render (obligatoire)
- `RENDER_API_KEY` : Clé API pour fallback
- `RENDER_SERVICE_ID` : ID du service Render

### Configuration Render

**Variables d'environnement** :

```bash
# SwitchBot API
SWITCHBOT_TOKEN=votre_token_ici
SWITCHBOT_SECRET=votre_secret_ici

# Flask
FLASK_SECRET_KEY=clé_aléatoire_32_caractères

# Base de données (recommandé)
STORE_BACKEND=postgres
POSTGRES_URL=postgresql://user:pass@host/db
POSTGRES_SSL_MODE=require

# Gunicorn
WEB_CONCURRENCY=1
LOG_LEVEL=warning

# Scheduler
SCHEDULER_ENABLED=true

# IFTTT (optionnel)
IFTTT_TIMEOUT_SECONDS=10
IFTTT_RETRY_ATTEMPTS=1
```

**Commande de démarrage Render** :
```
gunicorn 'switchbot_dashboard:create_app()' --bind 0.0.0.0:${PORT} --workers 1 --threads 2 --timeout 120
```

## Monitoring santé intégré

### Endpoint `/healthz`

L'application expose un endpoint de santé complet :

```bash
curl https://votre-app.onrender.com/healthz
```

**Réponse attendue** :
```json
{
  "status": "ok",
  "scheduler_running": true,
  "automation_enabled": true,
  "last_tick": "2026-02-08T14:30:00Z",
  "last_read_at": "2026-02-08T14:29:45Z",
  "temperature_stale": false,
  "api_requests_total": 42,
  "api_requests_remaining": 958,
  "api_quota_day": "2026-02-08",
  "version": "2.0.0"
}
```

**Alertes recommandées** :
- `status != "ok"` → Critique
- `scheduler_running == false` → Avertissement  
- `last_tick` > 10 minutes → Critique
- `api_requests_remaining` < 100 → Avertissement

### Logs structurés

Les logs utilisent des préfixes pour faciliter le diagnostic :

```bash
[ifttt] IFTTT webhook triggered successfully | status_code=200
[automation] Automation tick started | trigger=scheduler, interval=60s
[health] Health check completed | status=ok, scheduler_running=true
[store] PostgreSQL connection established | pool_size=5
```

**Commandes de diagnostic Render** :
```bash
# Filtrer les logs IFTTT
grep "\[ifttt\]" logs

# Rechercher les fallbacks
grep "fallback" logs

# Surveiller les erreurs
grep -i "error\|failed" logs
```

## Tableau Comparatif des Approches de Déploiement

| Approche | Complexité | Coût | Résilience | Cas d'usage idéal |
|----------|------------|------|------------|-------------------|
| **Render + GHCR** | Moyenne | Payant (~$7/mois) | Élevée (auto-restart) | Production, petit projet |
| **Docker local** | Faible | Gratuit | Moyenne (manuel) | Développement, testing |
| **VPS dédié** | Élevée | Payant (~$5/mois) | Élevée (contrôle total) | Gros projet, custom |

## Pièges courants et solutions

### ❌ Le piège du worker multiple

Avec `WEB_CONCURRENCY > 1`, APScheduler lance plusieurs ticks simultanés :

```bash
# Configuration incorrecte
WEB_CONCURRENCY=4  # 4 workers = 4 ticks dupliqués
```

**Logs observés** :
```
[automation] Multiple scheduler instances detected | workers=4
[automation] Duplicate tick prevention activated
```

### ✅ La solution worker unique

```bash
# Configuration correcte
WEB_CONCURRENCY=1  # Un seul worker, 2 threads pour les requêtes
```

**Résultat** : Un tick par minute, état cohérent, quota prévisible.

### ❌ Le piège des webhooks IFTTT

HTTP non sécurisé ou timeout trop court :

```bash
# Configuration incorrecte
IFTTT_WEBHOOK_URL=http://example.com/webhook  # HTTP refusé
IFTTT_TIMEOUT_SECONDS=2  # Timeout trop court
```

**Logs observés** :
```
[ifttt] HTTPS required for IFTTT webhooks | url=http://example.com
[ifttt] Webhook timeout after 2s | action_key=winter
```

### ✅ La solution IFTTT robuste

```bash
# Configuration correcte
IFTTT_WEBHOOK_URL=https://maker.ifttt.com/trigger/winter/with/key/xxx
IFTTT_TIMEOUT_SECONDS=10
IFTTT_RETRY_ATTEMPTS=1
```

**Résultat** : Webhooks fiables, fallbacks uniquement quand nécessaire.

### ❌ Le piège Redis legacy

Configuration Redis obsolète depuis janvier 2026 :

```bash
# Ne plus utiliser
STORE_BACKEND=redis
REDIS_URL_PRIMARY=rediss://...
```

**Logs observés** :
```
[store] Redis backend deprecated, falling back to JsonStore
[store] Consider migrating to PostgreSQL for production
```

### ✅ La solution PostgreSQL moderne

```bash
# Configuration recommandée
STORE_BACKEND=postgres
POSTGRES_URL=postgresql://user:pass@host/db?sslmode=require
```

**Résultat** : Persistance fiable, migrations gérées, monitoring intégré.

## Processus de déploiement complet

1. **Configuration initiale** (une seule fois) :
   - Créer service Render avec image GHCR
   - Configurer secrets GitHub et variables Render
   - Tester endpoint `/healthz`

2. **Déploiement automatique** (chaque push) :
   ```bash
   git add .
   git commit -m "feat: nouvelle fonctionnalité"
   git push origin main
   ```

3. **Vérification post-déploiement** :
   ```bash
   # Santé de l'application
   curl https://votre-app.onrender.com/healthz
   
   # Logs de déploiement
   # Dashboard Render > Logs
   ```

## Tests et validation

### Local avec Docker

```bash
# Build local
docker build -t switchbot:local .

# Test avec variables
docker run -it --rm -p 8000:8000 \
  -e SWITCHBOT_TOKEN=test \
  -e SWITCHBOT_SECRET=test \
  -e STORE_BACKEND=filesystem \
  switchbot:local

# Vérifier santé
curl http://localhost:8000/healthz
```

### GitHub Actions

```bash
# Lancer manuellement
# GitHub > Actions > Build and Deploy > Run workflow

# Vérifier image GHCR
# https://github.com/ki2pixel/switchbot/pkgs/container/switchbot
```

### Render

```bash
# Tests post-déploiement
curl -s https://votre-app.onrender.com/healthz | jq '.status'

# Test IFTTT
curl -X POST https://maker.ifttt.com/trigger/test/with/key/YOUR_KEY \
  -H "Content-Type: application/json" \
  -d '{"test": "deployment"}'
```

## La Règle d'Or : Un Worker, Une Source de Vérité

**Worker unique** : `WEB_CONCURRENCY=1` évite les ticks dupliqués et garantit l'état cohérent. Cette règle résume tous les trade-offs du tableau ci-dessus - la simplicité prime sur la complexité pour la fiabilité en production.

**Source de vérité** : PostgreSQL avec migrations gérées, fallback JsonStore en secours.

**Monitoring proactif** : `/healthz` avant que les utilisateurs ne remarquent le problème.

---

*Ce guide complète `quickstart.md` (installation locale) et s'intègre aux standards de `.windsurf/rules/codingstandards.md`.*
