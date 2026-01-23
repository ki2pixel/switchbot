# History Monitoring Guide

## Overview

The History Monitoring feature provides a comprehensive dashboard for visualizing and analyzing historical data from your SwitchBot devices. It offers real-time charts, aggregated statistics, and filtered data exploration with a 6-hour retention period aligned with Neon PostgreSQL's PITR (Point-in-Time Recovery) capabilities.

## Features

### 📊 Interactive Dashboard
- **Real-time charts** with 30-second auto-refresh
- **Visualisations actuelles** : Température & Humidité (line chart), État climatisation (aire/ligne discrète)
- **Responsive design** optimisé pour desktop et mobile
- **Dark theme** cohérent avec le dashboard principal
- **Bannière “mode démo”** : si `HistoryService` n’est pas injecté (ex. fallback JSON en local), un bandeau jaune s’affiche en haut de la page indiquant que des données mockées sont proposées. Cette bannière est pilotée par `static/js/history.js` (section `showDemoBanner()`) et disparaît automatiquement dès que la connexion PostgreSQL est restaurée.

### 🔍 Advanced Filtering
- **Time ranges**: 1h, 6h, 24h, or custom date ranges
- **Granularity options**: Minute, 5-minute, 15-minute, or hourly aggregation
- **Metric selection**: Choose which data points to display
- **Live updates**: Apply filters without page reload

### 📈 Data Visualizations
1. **Temperature & Humidity**: Dual-axis line chart with smooth animations
2. **Aircon State Timeline**: Ligne empilée (ou zone) montrant l’évolution ON/OFF/Auto
- *(Les anciens graphiques API Usage & Error Distribution ont été retirés du template pour simplifier l’interface. Ils restent mentionnés ici uniquement comme pistes futures — voir section “Future Enhancements”.)*

### 📋 Statistics & Tables
- **Status cards**: Température moyenne, humidité moyenne, total d’enregistrements
- **Latest records table**: Derniers snapshots (température, humidité, état clim, action)
- **Aggregated metrics**: Statistiques pour la période sélectionnée (sans compteur d’erreurs)

## Architecture

### Data Storage
```sql
CREATE TABLE state_history (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    temperature DECIMAL(4,1),
    humidity DECIMAL(4,1),
    assumed_aircon_power VARCHAR(10),
    last_action VARCHAR(50),
    api_requests_today INTEGER DEFAULT 0,
    error_count INTEGER DEFAULT 0,
    last_temperature_stale BOOLEAN DEFAULT FALSE,
    timezone VARCHAR(50) DEFAULT 'UTC',
    metadata JSONB DEFAULT '{}'
);
```

### Service Layer
- **HistoryService**: Handles data collection, aggregation, and cleanup
- **AutomationService Integration**: Automatic state recording after each automation tick
- **REST API**: Three endpoints for data retrieval (`/history/api/*`)
- **Frontend**: Chart.js-based dashboard with real-time updates

### Data Flow
```
AutomationService.run_once() 
    ↓
HistoryService.record_state() 
    ↓
PostgreSQL (state_history table)
    ↓
REST API (/history/api/*)
    ↓
Frontend Dashboard (Chart.js)
```

## Setup and Configuration

### Prerequisites
- PostgreSQL backend (Neon recommended)
- Existing SwitchBot Dashboard installation
- PostgreSQL connection pool available

### Database Setup

#### Automatic Table Creation
The HistoryService automatically creates the `state_history` table on first use. No manual setup required.

#### Manual Setup (Optional)
If you prefer to create the table manually:

```bash
# Apply the migration script
psql $POSTGRES_URL -f scripts/create_history_table.sql
```

### Application Configuration

#### Enable History Service
In your `switchbot_dashboard/__init__.py`, ensure the HistoryService is injected:

```python
from .history_service import HistoryService

# In create_app() function, after PostgresStore setup:
if isinstance(settings_store, PostgresStore):
    history_service = HistoryService(
        connection_pool=settings_store._pool,
        logger=app.logger,
        retention_hours=6,
    )
    app.extensions["history_service"] = history_service
    
    # Inject into AutomationService
    automation_service = AutomationService(
        settings_store=settings_store,
        state_store=state_store,
        switchbot_client=switchbot_client,
        ifttt_client=ifttt_client,
        history_service=history_service,
        logger=app.logger,
    )
```

#### Environment Variables
No additional environment variables required. Uses existing PostgreSQL configuration.

## Usage Guide

### Accessing the Dashboard
1. Navigate to your SwitchBot Dashboard
2. Click the "Historique" button in the main navigation
3. The monitoring dashboard will load with the last 6 hours of data

### Using Filters

#### Time Range Selection
- **Dernière heure**: Most recent 60 minutes
- **Dernières 6 heures**: Default view, optimal for performance
- **Dernières 24 heures**: Full day overview
- **Personnalisé**: Custom start/end dates and times

#### Granularity Control
- **Par minute**: Highest detail, best for recent data
- **Par 5 minutes**: Good balance of detail and performance
- **Par 15 minutes**: Medium-term trends
- **Par heure**: Long-term patterns

#### Metric Selection
Toggle individual metrics to customize the display:
- ✅ **Température**: Temperature readings and trends
- ✅ **Humidité**: Humidity percentage data
- ✅ **Climatisation**: Aircon power state changes
- ⬜ **Quota API**: API usage consumption (optional)

### Chart Interactions

#### Temperature & Humidity Chart
- **Zoom**: Click and drag to zoom into specific time periods
- **Pan**: Click and drag after zooming to navigate
- **Reset**: Use "Réinitialiser zoom" button to return to full view
- **Tooltip**: Hover over data points for detailed values

#### Aircon State Chart
- **Distribution**: Shows percentage of time in each state
- **Legend**: Click legend items to show/hide categories
- **Animation**: Smooth transitions when data updates

#### API Usage Chart
- **Cumulative**: Shows total API requests over time
- **Trend**: Identify usage patterns and potential quota issues

#### Error Distribution
- **Hourly**: Groups errors by hour of day
- **Patterns**: Identify recurring issues or peak error times

### Real-time Features

#### Auto-refresh
- Dashboard updates every 30 seconds automatically
- Status indicator shows connection health
- Last update timestamp displayed

#### Live Status Indicators
- 🟢 **Success**: Data loaded successfully
- 🔴 **Error**: Connection or data issues
- 🟡 **Loading**: Data refresh in progress

## API Reference

### Endpoints

#### GET `/history/api/data`
Retrieve filtered historical data.

**Query Parameters:**
- `start` (string, optional): ISO datetime start (default: 6 hours ago)
- `end` (string, optional): ISO datetime end (default: now)
- `metrics` (array, optional): Metrics to include
- `granularity` (string): `minute`, `5min`, `15min`, `hour` (default: `minute`)
- `limit` (integer): Maximum records (default: 1000, max: 1000)

**Response:**
```json
{
  "data": [
    {
      "timestamp": "2026-01-14T15:30:00Z",
      "temperature": 23.5,
      "humidity": 45.0,
      "assumed_aircon_power": "on",
      "last_action": "automation_winter_on",
      "api_requests_today": 150,
      "error_count": 0
    }
  ],
  "start": "2026-01-14T09:30:00Z",
  "end": "2026-01-14T15:30:00Z",
  "granularity": "minute",
  "metrics": ["temperature", "humidity", "assumed_aircon_power"],
  "count": 360
}
```

#### GET `/history/api/aggregates`
Get aggregated statistics for a time period.

**Query Parameters:**
- `period_hours` (integer): Period in hours (1-24, default: 1)

**Response:**
```json
{
  "period_hours": 6,
  "aggregates": {
    "total_records": 360,
    "avg_temperature": 23.5,
    "min_temperature": 20.0,
    "max_temperature": 26.0,
    "avg_humidity": 45.0,
    "min_humidity": 40.0,
    "max_humidity": 50.0,
    "common_aircon_state": "on",
    "distinct_actions": 3,
    "total_errors": 2,
    "max_api_requests": 150
  }
}
```

#### GET `/history/api/latest`
Retrieve most recent records.

**Query Parameters:**
- `limit` (integer): Number of records (1-100, default: 10)

**Response:**
```json
{
  "latest": [
    {
      "id": 1234,
      "timestamp": "2026-01-14T15:30:00Z",
      "temperature": 23.5,
      "humidity": 45.0,
      "assumed_aircon_power": "on",
      "last_action": "automation_winter_on",
      "error_count": 0,
      "metadata": {
        "last_read_at": "2026-01-14T15:30:00Z",
        "automation_active": true
      }
    }
  ],
  "count": 10
}
```

## Performance and Optimization

### Data Retention
- **Default retention**: 6 hours (aligned with Neon PITR)
- **Automatic cleanup**: HistoryService.cleanup_old_records()
- **Storage optimization**: Indexed queries and efficient data types

### Query Optimization
- **Time-based indexes**: `idx_state_history_timestamp`, `idx_state_history_date_bucket`
- **JSONB indexing**: GIN index on metadata for complex queries
- **Connection pooling**: Reuses PostgreSQL connections from PostgresStore

### Frontend Performance
- **Chart.js optimization**: Efficient rendering with `update('none')`
- **Debounced filters**: Prevent excessive API calls
- **Lazy loading**: Charts update only when visible
- **Responsive design**: Optimized for mobile devices

## Troubleshooting

### Common Issues

#### No Data Displayed
**Symptoms**: Charts show empty or "No data found"
**Causes**: 
- History service not properly injected
- PostgreSQL connection issues
- No automation ticks recorded yet

**Solutions**:
1. Check application logs for `[history]` entries
2. Verify PostgreSQL backend is active
3. Ensure automation is running and recording states

#### Slow Loading
**Symptoms**: Dashboard takes >10 seconds to load
**Causes**:
- Large time range with minute granularity
- Database connection issues
- High concurrent load

**Solutions**:
1. Reduce time range or increase granularity
2. Check PostgreSQL performance metrics
3. Consider caching for frequently accessed data

#### Chart Rendering Issues
**Symptoms**: Charts appear distorted or don't update
**Causes**:
- Browser compatibility issues
- JavaScript errors
- Invalid data format

**Solutions**:
1. Check browser console for errors
2. Verify Chart.js library loaded correctly
3. Test with different browsers

### Debug Mode

Enable debug logging by setting `LOG_LEVEL=DEBUG`:
```bash
export LOG_LEVEL=DEBUG
python app.py
```

Look for these log patterns:
- `[history]` - History service operations
- `[automation]` - State recording attempts
- Database connection errors

### Health Checks

Monitor the history service health:
```bash
# Check if history service is available
curl http://localhost:5000/history/api/latest

# Verify database connectivity
curl http://localhost:5000/healthz
```

## Development and Testing

### Running Tests
```bash
# Run history service tests
python -m pytest tests/test_history_service.py -v

# Run all tests with coverage
python -m pytest --cov=switchbot_dashboard.history_service tests/
```

### Test Coverage
The test suite covers:
- ✅ CRUD operations (Create, Read, Update, Delete)
- ✅ Data aggregation and filtering
- ✅ Time-based queries with different granularities
- ✅ Error handling and edge cases
- ✅ Integration with AutomationService
- ✅ Cleanup operations

### Mock Testing
Tests use mocked PostgreSQL connections to avoid database dependencies:
```python
@pytest.fixture
def mock_connection_pool():
    pool = MagicMock()
    pool.connection.return_value.__enter__.return_value = MagicMock()
    return pool
```

## Security Considerations

### Data Access
- **Authentication**: Uses existing Flask session management
- **Authorization**: Read-only access to historical data
- **Data isolation**: User-specific data through existing store isolation

### Privacy
- **Retention limits**: Automatic cleanup after 6 hours
- **No PII**: Only device metrics and automation state
- **Secure transport**: HTTPS recommended for production

### Rate Limiting
- **API limits**: Built-in query limits (max 1000 records)
- **Frontend throttling**: 30-second refresh intervals
- **Database protection**: Indexed queries prevent full table scans

## Future Enhancements

### Planned Features
- 📊 **Advanced analytics**: Correlation analysis between temperature and actions
- 📱 **Mobile app**: Native mobile application for monitoring
- 🔔 **Alerts**: Configurable alerts for unusual patterns
- 📈 **Predictions**: Machine learning for temperature forecasting
- 🗄️ **Extended retention**: Optional longer storage periods

### API Extensions
- **WebSocket support**: Real-time push updates
- **Export functionality**: CSV/JSON data export
- **Advanced filtering**: Complex query builder
- **Custom dashboards**: User-configurable layouts

### Performance Improvements
- **Caching layer**: Redis for frequently accessed aggregates
- **Data compression**: Efficient storage for historical data
- **Batch processing**: Optimized bulk operations
- **Horizontal scaling**: Multi-instance support

## Support and Contributing

### Getting Help
- **Documentation**: Check this guide and related documentation
- **Issues**: Report bugs via GitHub issues
- **Community**: Join discussions for feature requests

### Contributing
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request with documentation

### Code Standards
- Follow existing coding standards (see `.windsurf/rules/codingstandards.md`)
- Add comprehensive tests for new features
- Update documentation for API changes
- Ensure dark theme consistency

---

*Last updated: January 14, 2026*
