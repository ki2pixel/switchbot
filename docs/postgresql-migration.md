# PostgreSQL Migration Guide

## Overview

This guide describes migrating from Redis-based storage to PostgreSQL (Neon) for the SwitchBot Dashboard persistence layer.

## Why PostgreSQL?

- **Simplified Architecture**: Single PostgreSQL instance vs Redis primary/secondary + filesystem fallback
- **Cost Predictable**: Neon's free tier (100h-CU/month, 0.5GB storage) is sufficient for dashboard data
- **Advanced Features**: JSONB support, PITR (6h window), branching, extensions
- **Better Integration**: Native PostgreSQL support on Render platform

## Prerequisites

- Neon PostgreSQL account (free tier sufficient)
- PostgreSQL connection string from Neon dashboard
- Existing Redis/JSON data to migrate

## Migration Steps

### 1. Create Neon Database

1. Sign up at [Neon Console](https://console.neon.tech/)
2. Create new project (free tier)
3. Generate connection string:
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

## Migration Timeline

Typical migration timeline:
- **Preparation**: 30 minutes (Neon setup, dependencies)
- **Migration**: 5-15 minutes (depending on data size)
- **Testing**: 30-60 minutes (functionality verification)
- **Cleanup**: 15 minutes (optional Redis removal)

Total: ~2-3 hours for complete migration
