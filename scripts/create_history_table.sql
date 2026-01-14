-- Create state_history table for monitoring dashboard
-- This table stores historical data with 6-hour retention (aligned with Neon PITR)

CREATE TABLE IF NOT EXISTS state_history (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    temperature DECIMAL(4,1),              -- Temperature in Celsius (e.g., 23.5)
    humidity DECIMAL(4,1),                 -- Humidity percentage (e.g., 45.0)
    assumed_aircon_power VARCHAR(10),      -- 'on', 'off', or 'unknown'
    last_action VARCHAR(50),               -- Last automation action taken
    api_requests_today INTEGER DEFAULT 0, -- Daily API quota usage
    error_count INTEGER DEFAULT 0,         -- Number of errors in this tick
    last_temperature_stale BOOLEAN DEFAULT FALSE, -- Temperature freshness flag
    timezone VARCHAR(50) DEFAULT 'UTC',    -- Timezone used for this record
    metadata JSONB DEFAULT '{}'            -- Additional structured data
);

-- Indexes for optimal query performance
CREATE INDEX IF NOT EXISTS idx_state_history_timestamp ON state_history(timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_state_history_date_bucket ON state_history(date_trunc('hour', timestamp));
CREATE INDEX IF NOT EXISTS idx_state_history_aircon_power ON state_history(assumed_aircon_power);
CREATE INDEX IF NOT EXISTS idx_state_history_metadata ON state_history USING GIN(metadata);

-- Comment for documentation
COMMENT ON TABLE state_history IS 'Historical monitoring data for SwitchBot dashboard (6-hour retention)';
COMMENT ON COLUMN state_history.temperature IS 'Temperature reading from Meter device in Celsius';
COMMENT ON COLUMN state_history.humidity IS 'Humidity reading from Meter device in percentage';
COMMENT ON COLUMN state_history.assumed_aircon_power IS 'Assumed aircon state (on/off/unknown)';
COMMENT ON COLUMN state_history.last_action IS 'Last automation action executed';
COMMENT ON COLUMN state_history.api_requests_today IS 'Daily API quota consumption at time of record';
COMMENT ON COLUMN state_history.error_count IS 'Number of errors encountered during this tick';
COMMENT ON COLUMN state_history.last_temperature_stale IS 'Flag indicating if temperature data was stale';
COMMENT ON COLUMN state_history.timezone IS 'Timezone used for timestamp calculations';
COMMENT ON COLUMN state_history.metadata IS 'Additional structured data (JSONB)';
