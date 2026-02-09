# Architecture de la Couche de Stockage

**TL;DR**: Le SwitchBot Dashboard utilise PostgreSQL (Neon) comme stockage principal avec fallback automatique vers JSON filesystem, offrant une architecture simplifiée et résiliente sans complexité Redis.

## Le Problème : Pourquoi changer l'architecture ?

Vous gérez un dashboard d'automation avec des paramètres utilisateur et des états de devices. Votre architecture actuelle ressemble à ça :

❌ **Architecture Redis complexe**
- Redis primaire + secondaire pour la haute disponibilité
- Fallback filesystem JSON si Redis indisponible
- Configuration complexe avec multiples endpoints
- Coûts imprévisibles selon l'utilisation

Chaque ajout de fonctionnalité vous fait craindre une rupture de la chaîne de stockage. La maintenance devient un casse-tête.

## La Solution : PostgreSQL comme Single Source of Truth

✅ **Architecture PostgreSQL unifiée**
- Instance PostgreSQL unique (Neon free tier)
- Schema JSONB simple et efficace
- Fallback filesystem JSON automatique
- Coût prévisible : gratuit jusqu'à 100h-CU/mois

C'est comme remplacer un système de fichiers distribué complexe par une base de données robuste que tout le monde comprend.

## L'Architecture : Comment ça fonctionne ?

### Schema PostgreSQL

Une seule table, deux types de données :

```sql
CREATE TABLE json_store (
    kind VARCHAR(50) PRIMARY KEY,  -- 'settings' ou 'state'
    data JSONB NOT NULL,           -- Données JSON avec indexation
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### Pattern Store Abstrait

```python
# Interface unifiée
class StoreInterface:
    def get(self, key: str) -> dict: ...
    def set(self, key: str, data: dict) -> None: ...
    def health_check(self) -> bool: ...

# Implémentations
class PostgresStore(StoreInterface):  # Prioritaire
class JsonStore(StoreInterface):     # Fallback
```

### Fallback Automatique

```python
def get_store() -> StoreInterface:
    if STORE_BACKEND == "postgres":
        try:
            return PostgresStore()
        except Exception as e:
            logger.warning(f"[store] PostgreSQL indisponible, fallback vers JSON: {e}")
            return JsonStore()
    return JsonStore()
```

## L'Implémentation : Configuration et Code

### Variables d'environnement (.env)

```bash
# Configuration PostgreSQL (prioritaire)
STORE_BACKEND=postgres
POSTGRES_URL=postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require
POSTGRES_SSL_MODE=require

# Fallback automatique vers JSON si PostgreSQL KO
# Pas de configuration supplémentaire requise
```

### Configuration JSON (config/settings.json)

```json
{
    "automation_enabled": true,
    "poll_interval_seconds": 30,
    "ifttt_webhooks": [...],
    "aircon_scenes": [...]
}
```

### Migration des données

```bash
# Validation avant migration
python scripts/migrate_to_postgres.py \
    --postgres-url "postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require" \
    --settings-path "config/settings.json" \
    --state-path "config/state.json" \
    --dry-run

# Migration réelle
python scripts/migrate_to_postgres.py \
    --postgres-url "postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require" \
    --settings-path "config/settings.json" \
    --state-path "config/state.json"
```

### Dépendances Python

```bash
# requirements.txt
psycopg[binary]>=3.2,<4
psycopg-pool>=3.2,<4
```

## Les Pièges : Ce qu'il faut surveiller

### ❌ Erreur de configuration SSL

```python
# Incorrect : Neon exige SSL
POSTGRES_URL=postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname

# Correct : SSL obligatoire pour Neon
POSTGRES_URL=postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require
```

### ❌ Ignorer le cold start Neon

```python
# Sans gestion du cold start
def get_data():
    return store.get("settings")  # 500ms-2s si inactivité

# Avec gestion du cold start
def get_data():
    try:
        return store.get("settings")
    except SlowConnectionError:
        logger.warning("[store] Cold start PostgreSQL, utilisation cache")
        return cache.get("settings")
```

### ❌ Oublier le fallback

```python
# Sans fallback
store = PostgresStore()  # Crash si PostgreSQL KO

# Avec fallback automatique
store = get_store()  # PostgresStore ou JsonStore selon santé
```

## Performance et Monitoring

### Connection Pooling

```python
# PostgresStore gère automatiquement le pooling
# 1-10 connections par défaut pour :
# - Gérer les cold starts (Neon sleep après 5min inactivité)
# - Requêtes concurrentes
# - Réutilisation des connections
```

### Monitoring de santé

```python
# Vérification santé store
store.health_check()  # True/False

# Monitoring via endpoint /healthz
# Inclut statut PostgreSQL store
```

### Latences typiques

- **Cold start** : 500ms-2s après inactivité
- **Connections chaudes** : <50ms pour read/write
- **Réutilisation connection** : Overhead minimal

## Déploiement Production

### Configuration Render

```bash
# Variables environnement Render
STORE_BACKEND=postgres
POSTGRES_URL=postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require
POSTGRES_SSL_MODE=require
```

### Health Checks

L'endpoint `/healthz` inclut automatiquement le statut PostgreSQL store pour le monitoring externe.

### Tableau Comparatif des Approches de Stockage

| Approche | Performance | Coût | Maintenance | Résilience |
|----------|-------------|------|-------------|------------|
| **PostgreSQL Neon** | Élevée | Gratuit (100h CU) | Faible | Élevée (PITR) |
| **Redis Cloud** | Très élevée | Payant | Moyenne | Moyenne |
| **JSON Fichiers** | Moyenne | Gratuit | Faible | Faible |

## La Règle d'Or : Stockage Unifié, Fallback Transparent

**Principe** : Une seule source de vérité PostgreSQL avec fallback JSON invisible pour l'application.

**Application** : Tous les services utilisent `current_app.extensions["settings_store"]` et `current_app.extensions["state_store"]` sans se soucier de l'implémentation sous-jacente.

**Résultat** : Architecture simplifiée, maintenance réduite, résilience garantie.

---

## Références techniques

### Standards de développement
- [`.windsurf/rules/codingstandards.md`](../../.windsurf/rules/codingstandards.md) – Règles de codage obligatoires
- [`.windsurf/skills/postgres-store-maintenance/`](../../.windsurf/skills/postgres-store-maintenance/) – Guide maintenance PostgreSQL

### Documentation backend
- [DOCUMENTATION.md](../../docs/DOCUMENTATION.md) – Architecture complète et métriques
- [switchbot/README.md](../../docs/switchbot/README.md) – API SwitchBot et quotas

### Scripts et outils
- [`scripts/migrate_to_postgres.py`](../../scripts/migrate_to_postgres.py) – Script migration automatisée
- [`scripts/create_history_table.sql`](../../scripts/create_history_table.sql) – Schema History Service

### Memory Bank (décisions architecturales)
- `memory-bank/decisionLog.md` – Décisions migration PostgreSQL
- `memory-bank/systemPatterns.md` – Patterns stockage PostgreSQL
- `memory-bank/productContext.md` – Architecture produit complète
