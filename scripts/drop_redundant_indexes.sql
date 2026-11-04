-- Optional cleanup for indexes created by older SwitchBot Dashboard versions.
--
-- Run manually during a maintenance window. The application no longer creates
-- these indexes:
--   * idx_json_store_kind duplicates the json_store primary key index.
--   * idx_state_history_metadata is a GIN index that no query uses.
--
-- Dropping them is safe; CREATE INDEX statements were removed from the
-- application startup path in the V2 audit remediation.
--
-- Preferred runner (reads POSTGRES_URL from .env, dry-run by default):
--     python scripts/drop_redundant_indexes.py
--     python scripts/drop_redundant_indexes.py --apply
--
-- Or with psql:
--     psql "$POSTGRES_URL" -f scripts/drop_redundant_indexes.sql

DROP INDEX IF EXISTS idx_json_store_kind;
DROP INDEX IF EXISTS idx_state_history_metadata;
