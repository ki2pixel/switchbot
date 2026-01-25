# PostgreSQL Migration Guide

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Vue d'ensemble

Ce guide décrit la migration depuis le stockage Redis vers PostgreSQL (Neon) pour la couche de persistance du SwitchBot Dashboard.

> 📝 **Décisions connexes** : Les patterns de migration PostgreSQL sont documentés dans `memory-bank/systemPatterns.md` et `memory-bank/decisionLog.md`. Voir notamment les décisions du 2026-01-14 sur la migration PostgreSQL Neon.

## Pourquoi PostgreSQL ?

- **Architecture simplifiée** : Instance PostgreSQL unique vs Redis primaire/secondaire + fallback filesystem
- **Coût prévisible** : Free tier Neon (100h-CU/mois, 0.5GB stockage) suffisant pour les données du dashboard
- **Fonctionnalités avancées** : Support JSONB, PITR (fenêtre 6h), branching, extensions
- **Meilleure intégration** : Support PostgreSQL natif sur plateforme Render

## Prérequis

- Compte Neon PostgreSQL (free tier suffisant)
- Chaîne de connexion PostgreSQL depuis dashboard Neon
- Données Redis/JSON existantes à migrer

## Migration Steps

### 1. Créer la base de données Neon

1. Inscrivez-vous sur [Neon Console](https://console.neon.tech/)
2. Créez un nouveau projet (free tier)
3. Générez la chaîne de connexion :
   ```
   postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require
   ```

### 2. Update Configuration

Add to your `.env` file:
```bash
# Use PostgreSQL backend
STORE_BACKEND=postgres
POSTGRES_URL=postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require
POSTGRES_SSL_MODE=require
```

### 3. Install Dependencies

```bash
pip install psycopg[binary]>=3.2,<4
```

Or update `requirements.txt`:
```
psycopg[binary]>=3.2,<4
```

### 4. Run Migration Script

```bash
# Dry run (validation only)
python scripts/migrate_to_postgres.py \
    --postgres-url "postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require" \
    --redis-url "rediss://default:password@host:6379/0" \
    --dry-run

# Actual migration
python scripts/migrate_to_postgres.py \
    --postgres-url "postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require" \
    --redis-url "rediss://default:password@host:6379/0"
```

### 5. Deploy and Test

1. Deploy updated application with PostgreSQL configuration
2. Verify all functionality works:
   - Settings persistence
   - State tracking
   - Automation service
   - UI interactions

### 6. Cleanup (Optional)

After successful migration:
- Remove Redis dependencies from `requirements.txt`
- Remove Redis configuration variables
- Update documentation

## Schema

The PostgreSQL schema uses a single table:

```sql
CREATE TABLE json_store (
    kind VARCHAR(50) PRIMARY KEY,  -- 'settings' or 'state'
    data JSONB NOT NULL,           -- JSON data with indexing
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## Migration Script Options

The migration script supports various options:

```bash
python scripts/migrate_to_postgres.py --help

Options:
  --postgres-url     PostgreSQL connection string (required)
  --redis-url        Redis connection string (optional)
  --settings-path    Path to settings.json (default: config/settings.json)
  --state-path       Path to state.json (default: config/state.json)
  --dry-run          Validate data without writing
  --verbose          Enable verbose logging
```

## Data Validation

The migration script validates:
- JSON structure and syntax
- Required keys for settings (`automation_enabled`, `poll_interval_seconds`)
- Data types and formats
- Timestamp formats in state data

## Fallback and Rollback

### Automatic Fallback

If PostgreSQL is unavailable, the application automatically falls back to filesystem JSON storage.

### Manual Rollback

To rollback to Redis/Filesystem:
```bash
# Update .env
STORE_BACKEND=filesystem  # or redis

# Restart application
```

## Performance Considerations

### Connection Pooling

PostgresStore uses connection pooling (default: 1-10 connections) to handle:
- Cold starts (Neon sleep after 5min inactivity)
- Concurrent requests
- Connection reuse

### Latency

- **Cold start**: 500ms-2s after inactivity
- **Warm connections**: <50ms for read/write operations
- **Connection reuse**: Minimal overhead after initial connection

### Monitoring

Monitor PostgreSQL health via:
```python
store.health_check()  # Returns True/False
```

## Troubleshooting

### Common Issues

1. **Connection Errors**
   - Verify POSTGRES_URL format
   - Check SSL mode (require for Neon)
   - Ensure network connectivity

2. **Migration Failures**
   - Validate JSON syntax in existing files
   - Check Redis connection if migrating from Redis
   - Use `--dry-run` to validate first

3. **Performance Issues**
   - Monitor connection pool usage
   - Check for connection leaks
   - Consider increasing `max_connections`

### Debug Logging

Enable verbose logging:
```bash
LOG_LEVEL=debug python scripts/migrate_to_postgres.py --verbose
```

## Production Deployment

### Render Configuration

Add to Render environment variables:
```bash
STORE_BACKEND=postgres
POSTGRES_URL=postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require
POSTGRES_SSL_MODE=require
```

### Health Checks

The `/healthz` endpoint includes PostgreSQL store health status.

### Monitoring

Monitor:
- Connection pool health
- Query latency
- Error rates
- Storage usage (0.5GB limit on free tier)

## Security Considerations

- **Connection Strings**: Store as environment variables, never in code
- **SSL/TLS**: Always use `sslmode=require` for cloud connections
- **Network**: Neon provides secure connections by default
- **Access**: Use least-privilege database roles

## Support

For issues:
1. Check application logs
2. Verify Neon console status
3. Test connection string with `psql` client
4. Review migration script output

## Chronologie de migration

Chronologie de migration typique :
- **Préparation** : 30 minutes (configuration Neon, dépendances)
- **Migration** : 5-15 minutes (selon la taille des données)
- **Tests** : 30-60 minutes (vérification fonctionnalité)
- **Nettoyage** : 15 minutes (suppression Redis optionnelle)

Total : ~2-3 heures pour migration complète

---

## Références croisées

### Documentation technique
- [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) – Standards de développement obligatoires
- [DOCUMENTATION.md](DOCUMENTATION.md) – Architecture et métriques
- [setup.md](setup.md) – Installation et configuration initiale

### Guides spécialisés
- [Configuration](configuration.md) – Variables d'environnement et paramètres
- [Deployment](deployment.md) – Configuration production et Render
- [Testing](testing.md) – Tests et validation PostgreSQL

### Memory Bank (décisions architecturales)
- `memory-bank/decisionLog.md` – Décisions de migration PostgreSQL (simplification architecture)
- `memory-bank/systemPatterns.md` – Patterns de stockage PostgreSQL
- `memory-bank/progress.md` – Historique des améliorations backend

---

*Last updated: January 25, 2026*
