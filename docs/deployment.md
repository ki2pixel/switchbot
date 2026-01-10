# Déploiement Render + GitHub Container Registry

Ce guide décrit comment construire l'image Docker du SwitchBot Dashboard, la publier sur GitHub Container Registry (GHCR) via GitHub Actions, puis déclencher un déploiement Render (plan Free).

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
- Variables :
  - `PORT` (Render fournit automatiquement la valeur).
  - `WEB_CONCURRENCY` (défaut 2, ajustable via Render env var).

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
   - Commande de démarrage : `gunicorn 'switchbot_dashboard:create_app()' --bind 0.0.0.0:${PORT} --workers ${WEB_CONCURRENCY:-2} --timeout 120`.
2. Variables d'environnement Render :
   - `SWITCHBOT_TOKEN` (secret).
   - `SWITCHBOT_SECRET` (secret).
   - `SWITCHBOT_RETRY_ATTEMPTS`, `SWITCHBOT_RETRY_DELAY_SECONDS` si besoin.
   - `SWITCHBOT_POLL_INTERVAL_SECONDS` pour override.
   - `WEB_CONCURRENCY` (optionnel, exemple `1` pour plan Free).
   - `LOG_LEVEL` (optionnel) : Niveau de log pour Gunicorn (DEBUG, INFO, WARNING, ERROR, CRITICAL), défaut `info`.
   - `FLASK_SECRET_KEY` (secret aléatoire).
   - `STORE_BACKEND=redis` pour activer la persistance externe des réglages/état.
   - `REDIS_URL` (obligatoire si `STORE_BACKEND=redis`). Render fournit une URL TLS sous la forme `rediss://default:<password>@host:6379/0`.
   - `REDIS_PREFIX` (optionnel, ex. `switchbot_dashboard:prod` pour isoler les clés).
   - `REDIS_TTL_SECONDS` (optionnel) si vous souhaitez expirer automatiquement les données (laisser vide pour stockage permanent).
3. Activer les logs sur Render : par défaut, Gunicorn écrit sur stdout/stderr, visibles dans l'onglet Logs.

## 5. Processus de déploiement

1. Commit + push sur `main` (ou lancer manuellement le workflow).
2. GitHub Actions construit et pousse l'image sur GHCR.
3. Le workflow appelle le webhook Render ; en cas d'échec il utilise l'API (fallback).
4. Render déploie la nouvelle image. Suivre la progression dans Render Dashboard.

## 6. Tests & validation

### Local
- `docker build -t switchbot:local .`
- `docker run -it --rm -p 8000:8000 --env-file=.env switchbot:local`
- Ouvrir `http://localhost:8000` pour vérifier l'UI.

### GitHub Actions
- Lancer `workflow_dispatch` en fournissant la branche.
- Vérifier que l'image apparaît dans `https://github.com/ki2pixel/switchbot/pkgs/container/switchbot`.

### Render
- Après déclenchement, vérifier :
  - Logs déploiement dans Render (pas d'erreurs Gunicorn/APScheduler).
  - Page `/` fonctionne, scheduler actif.

## 7. Checklist de secrets

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
- **Logs** : Gunicorn utilise `--access-logfile -` et `--error-logfile -` pour être visibles dans Render.
- **Fallback** : surveiller la sortie du job GitHub pour voir si le webhook a réussi ou si le fallback API a été nécessaire.

---

*Ce guide complète `docs/setup.md` (installation locale) et `docs/testing.md` (scénarios de validation).*
