-- PostgreSQL schema for SwitchBot Dashboard
-- Compatible with Neon PostgreSQL and other managed PostgreSQL services

-- Main storage table for JSON data
CREATE TABLE IF NOT EXISTS json_store (
    kind VARCHAR(50) PRIMARY KEY,  -- 'settings' or 'state'
    data JSONB NOT NULL,           -- JSON data with indexing support
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_json_store_kind ON json_store(kind);
CREATE INDEX IF NOT EXISTS idx_json_store_updated_at ON json_store(updated_at);

-- Optional: GIN index for JSONB queries (if needed in future)
-- CREATE INDEX IF NOT EXISTS idx_json_store_data_gin ON json_store USING GIN (data);

-- Table comment for documentation
COMMENT ON TABLE json_store IS 'Storage table for SwitchBot Dashboard configuration and state data';
COMMENT ON COLUMN json_store.kind IS 'Type of stored data: settings or state';
COMMENT ON COLUMN json_store.data IS 'JSON data with full PostgreSQL JSONB support';
COMMENT ON COLUMN json_store.updated_at IS 'Last update timestamp with timezone';

-- Sample data (for testing)
-- INSERT INTO json_store (kind, data) VALUES 
--     ('settings', '{"automation_enabled": true, "poll_interval_seconds": 60}'),
--     ('state', '{"last_temperature": 22.5, "last_read_at": "2026-01-14T12:00:00Z"}')
-- ON CONFLICT (kind) DO UPDATE SET 
--     data = EXCLUDED.data,
--     updated_at = EXCLUDED.updated_at;
