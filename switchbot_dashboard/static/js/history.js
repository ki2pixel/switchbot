/**
 * History Dashboard JavaScript
 * Handles real-time monitoring charts and data visualization
 */

(() => {
class HistoryDashboard {
    constructor() {
        this.charts = {};
        this.updateInterval = null;
        this.activeController = null; // AbortController for fetch cancellation (P3.6)
        this.isSmallMobile = globalThis.innerWidth <= 480;
        this.defaultGranularity = this.isSmallMobile ? '5min' : 'minute';
        this.currentFilters = {
            timeRange: '6h',
            granularity: this.defaultGranularity,
            metrics: ['temperature', 'humidity', 'assumed_aircon_power']
        };
        
        this.init();
    }

    init() {
        this.applyResponsiveDefaults();
        this.initCharts();
        this.bindEvents();
        this.loadInitialData();
        this.startRealTimeUpdates();
    }

    applyResponsiveDefaults() {
        if (!this.isSmallMobile) {
            return;
        }

        const granularitySelect = document.getElementById('granularity');
        if (granularitySelect) {
            granularitySelect.value = '5min';
        }
    }

    initCharts() {
        // Viewport-based responsive configuration
        const isMobile = globalThis.innerWidth <= 768;
        const isSmallMobile = globalThis.innerWidth <= 480;
        
        const chartOptions = {
            responsive: true,
            maintainAspectRatio: false,
            parsing: false,
            normalized: true,
            animation: false,
            interaction: {
                mode: 'index',
                intersect: false,
            },
            plugins: {
                legend: {
                    position: isMobile ? 'bottom' : 'top',
                    labels: {
                        color: '#e9ecef',
                        font: {
                            size: isSmallMobile ? 10 : (isMobile ? 11 : 12)
                        },
                        padding: isSmallMobile ? 10 : 20,
                        boxWidth: isSmallMobile ? 12 : 15
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(33, 37, 41, 0.9)',
                    titleColor: '#ffffff',
                    bodyColor: '#e9ecef',
                    borderColor: '#495057',
                    borderWidth: 1,
                    titleFont: {
                        size: isSmallMobile ? 11 : 12
                    },
                    bodyFont: {
                        size: isSmallMobile ? 10 : 11
                    },
                    padding: isSmallMobile ? 6 : 10
                },
                decimation: {
                    enabled: true,
                    algorithm: 'lttb',
                    samples: 100
                }
            },
            scales: {
                x: {
                    type: 'time',
                    time: {
                        displayFormats: {
                            minute: isSmallMobile ? 'H:mm' : 'HH:mm',
                            hour: isSmallMobile ? 'H:mm' : 'HH:mm'
                        }
                    },
                    ticks: {
                        color: '#6c757d',
                        font: {
                            size: isSmallMobile ? 9 : 10
                        },
                        maxTicksLimit: isSmallMobile ? 6 : 8
                    },
                    grid: {
                        color: 'rgba(108, 117, 125, 0.2)'
                    }
                }
            }
        };

        // Temperature & Humidity Chart
        this.charts.tempHumidity = new Chart(document.getElementById('tempHumidityChart'), {
            type: 'line',
            data: {
                datasets: [
                    {
                        label: 'Température (°C)',
                        data: [],
                        borderColor: '#dc3545',
                        backgroundColor: 'rgba(220, 53, 69, 0.1)',
                        tension: 0.4,
                        yAxisID: 'y'
                    },
                    {
                        label: 'Humidité (%)',
                        data: [],
                        borderColor: '#0d6efd',
                        backgroundColor: 'rgba(13, 110, 253, 0.1)',
                        tension: 0.4,
                        yAxisID: 'y1'
                    }
                ]
            },
            options: {
                ...chartOptions,
                scales: {
                    ...chartOptions.scales,
                    y: {
                        type: 'linear',
                        display: true,
                        position: 'left',
                        title: {
                            display: !isMobile,
                            text: 'Température (°C)',
                            color: '#dc3545',
                            font: {
                                size: isSmallMobile ? 9 : 10
                            }
                        },
                        ticks: {
                            color: '#6c757d',
                            font: {
                                size: isSmallMobile ? 9 : 10
                            },
                            maxTicksLimit: isSmallMobile ? 4 : 6
                        },
                        grid: {
                            color: 'rgba(108, 117, 125, 0.2)'
                        }
                    },
                    y1: {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        title: {
                            display: !isMobile,
                            text: 'Humidité (%)',
                            color: '#0d6efd',
                            font: {
                                size: isSmallMobile ? 9 : 10
                            }
                        },
                        ticks: {
                            color: '#6c757d',
                            font: {
                                size: isSmallMobile ? 9 : 10
                            },
                            maxTicksLimit: isSmallMobile ? 4 : 6
                        },
                        grid: {
                            drawOnChartArea: false
                        }
                    }
                }
            }
        });

        // Aircon State Chart
        this.charts.airconState = new Chart(document.getElementById('airconStateChart'), {
            type: 'doughnut',
            data: {
                labels: ['ON', 'OFF', 'Unknown'],
                datasets: [{
                    data: [0, 0, 0],
                    backgroundColor: [
                        '#198754',
                        '#dc3545',
                        '#6c757d'
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: '#e9ecef',
                            padding: isSmallMobile ? 10 : 20,
                            font: {
                                size: isSmallMobile ? 10 : 11
                            },
                            boxWidth: isSmallMobile ? 12 : 15
                        }
                    },
                    tooltip: {
                        backgroundColor: 'rgba(33, 37, 41, 0.9)',
                        titleColor: '#ffffff',
                        bodyColor: '#e9ecef',
                        borderColor: '#495057',
                        borderWidth: 1,
                        titleFont: {
                            size: isSmallMobile ? 11 : 12
                        },
                        bodyFont: {
                            size: isSmallMobile ? 10 : 11
                        },
                        padding: isSmallMobile ? 6 : 10
                    }
                }
            }
        });
    }

    bindEvents() {
        // Filter form submission
        document.getElementById('filtersForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.applyFilters();
        });

        // Time range change
        document.getElementById('timeRange').addEventListener('change', (e) => {
            const customGroups = ['customStartGroup', 'customEndGroup'];
            customGroups.forEach(id => {
                document.getElementById(id).style.display = 
                    e.target.value === 'custom' ? 'block' : 'none';
            });
        });

        // Reset zoom button
        const resetZoomBtn = document.getElementById('resetZoomTemp');
        if (resetZoomBtn) {
            const isZoomPluginRegistered = typeof Chart !== 'undefined' && 
                                           Chart.registry && 
                                           Chart.registry.plugins && 
                                           Chart.registry.plugins.get('zoom');
            if (!isZoomPluginRegistered) {
                resetZoomBtn.style.display = 'none';
            } else {
                resetZoomBtn.addEventListener('click', () => {
                    if (typeof this.charts.tempHumidity.resetZoom === 'function') {
                        this.charts.tempHumidity.resetZoom();
                    }
                });
            }
        }

        // Refresh latest records
        document.getElementById('refreshLatest').addEventListener('click', () => {
            this.loadLatestRecords();
        });

        // Metric checkboxes
        document.querySelectorAll('.metric-checkboxes input').forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                this.updateMetrics();
            });
        });

        // Page Visibility API to pause updates when tab is hidden
        this.visibilityHandler = () => {
            if (document.hidden) {
                console.debug('[history] Page hidden: pausing network polling.');
                this.stopRealTimeUpdates();
            } else {
                console.debug('[history] Page visible: resuming network polling and refreshing data.');
                this.startRealTimeUpdates();
                this.loadInitialData();
            }
        };
        document.addEventListener('visibilitychange', this.visibilityHandler);
    }

    async loadInitialData() {
        try {
            const [historyData, aggregates, latestRecords] = await Promise.all([
                this.loadHistoryData(),
                this.loadAggregates(),
                this.loadLatestRecords()
            ]);
            
            // Check if data is mocked (handle undefined safely)
            const isMockData = (historyData && historyData.mock) || 
                              (aggregates && aggregates.mock) || 
                              (latestRecords && latestRecords.mock);
            if (isMockData) {
                this.showMockDataWarning();
            }
            
            this.updateStatus('success', 'Données chargées');
        } catch (error) {
            console.error('Error loading initial data:', error);
            this.updateStatus('error', 'Erreur de chargement');
        }
    }

    showMockDataWarning() {
        // Add a warning banner for mock data (DOM API instead of innerHTML)
        const banner = document.createElement('div');
        banner.className = 'alert alert-warning alert-dismissible fade show mb-3';

        const strong = document.createElement('strong');
        strong.textContent = '\u26a0\ufe0f Mode d\u00e9monstration';
        banner.appendChild(strong);
        banner.appendChild(document.createElement('br'));
        banner.appendChild(document.createTextNode(
            "Le service d'historique n'est pas disponible. Donn\u00e9es simul\u00e9es affich\u00e9es."
        ));
        const closeBtn = document.createElement('button');
        closeBtn.type = 'button';
        closeBtn.className = 'btn-close';
        closeBtn.setAttribute('data-bs-dismiss', 'alert');
        banner.appendChild(closeBtn);
        
        const container = document.querySelector('.container');
        container.insertBefore(banner, container.firstChild);
    }

    async loadHistoryData() {
        // Cancel any previous in-flight request (P3.6 AbortController)
        if (this.activeController) {
            this.activeController.abort();
        }
        this.activeController = new AbortController();
        const signal = this.activeController.signal;
        const timeoutId = setTimeout(() => this.activeController.abort(), 10000);

        const params = new URLSearchParams({
            start: this.getTimeRangeStart(),
            end: new Date().toISOString(),
            granularity: this.currentFilters.granularity,
            metrics: this.currentFilters.metrics
        });

        try {
            const response = await fetch(`/history/api/data?${params}`, { signal });
            clearTimeout(timeoutId);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();
            this.updateCharts(data.data || []);
            return data;
        } catch (error) {
            clearTimeout(timeoutId);
            if (error.name === 'AbortError') {
                console.warn('[History] Request aborted (timeout or new request)');
                return;
            }
            console.error('Failed to load history data:', error);
            this.updateStatus('error', 'Erreur de chargement des donn\u00e9es');
            this.renderChartErrorState(error);
            throw error;
        } finally {
            this.activeController = null;
        }
    }

    renderChartErrorState(error) {
        document.querySelectorAll('.chart-container').forEach((container) => {
            container.textContent = '';
            const wrapper = document.createElement('div');
            wrapper.className = 'd-flex flex-column align-items-center justify-content-center text-muted py-4';
            const icon = document.createElement('div');
            icon.className = 'fs-3 mb-2';
            icon.textContent = '\u26a0\ufe0f';
            const msg = document.createElement('div');
            msg.className = 'text-center';
            msg.textContent = 'Impossible de charger les donn\u00e9es';
            const detail = document.createElement('small');
            detail.className = 'd-block mt-2';
            detail.textContent = error.message;
            wrapper.append(icon, msg, detail);
            container.appendChild(wrapper);
        });
    }

    async loadAggregates() {
        const response = await fetch('/history/api/aggregates?period_hours=6');
        if (!response.ok) throw new Error('Failed to load aggregates');
        
        const data = await response.json();
        this.updateStatusCards(data.aggregates || {});
        return data; // Return the full response for mock checking
    }

    async loadLatestRecords() {
        const response = await fetch('/history/api/latest?limit=10');
        if (!response.ok) throw new Error('Failed to load latest records');
        
        const data = await response.json();
        this.updateLatestTable(data.latest || []);
        return data; // Return the full response for mock checking
    }

    updateCharts(historyData) {
        if (!historyData || historyData.length === 0) {
            const tempDescriptionEl = document.getElementById('tempHumidityChartDescription');
            if (tempDescriptionEl) {
                tempDescriptionEl.textContent = "Graphique de température et humidité. Aucune donnée sur la période sélectionnée.";
            }
            const airconDescriptionEl = document.getElementById('airconStateChartDescription');
            if (airconDescriptionEl) {
                airconDescriptionEl.textContent = "Graphique de l'état de la climatisation. Aucune donnée sur la période sélectionnée.";
            }
            return;
        }

        // Clone and reverse the data array for chronological order (ASC)
        const sortedData = [...historyData].reverse();

        // Update temperature & humidity chart
        const tempData = sortedData.map(d => ({
            x: new Date(d.timestamp),
            y: d.temperature !== null && d.temperature !== undefined ? parseFloat(d.temperature) : null
        })).filter(d => d.y !== null);

        const humidityData = sortedData.map(d => ({
            x: new Date(d.timestamp),
            y: d.humidity !== null && d.humidity !== undefined ? parseFloat(d.humidity) : null
        })).filter(d => d.y !== null);

        this.charts.tempHumidity.data.datasets[0].data = tempData;
        this.charts.tempHumidity.data.datasets[1].data = humidityData;
        this.charts.tempHumidity.update('none');

        // Update aircon state chart
        const airconStates = historyData.reduce((acc, d) => {
            const state = d.assumed_aircon_power || 'unknown';
            acc[state] = (acc[state] || 0) + 1;
            return acc;
        }, {});

        this.charts.airconState.data.datasets[0].data = [
            airconStates['on'] || 0,
            airconStates['off'] || 0,
            airconStates['unknown'] || 0
        ];
        this.charts.airconState.update('none');

        // Update descriptions for A11y
        const tempDescriptionEl = document.getElementById('tempHumidityChartDescription');
        if (tempDescriptionEl) {
            if (tempData.length > 0) {
                const temps = tempData.map(d => d.y);
                const humidities = humidityData.map(d => d.y);
                
                const minTemp = Math.min(...temps).toFixed(1);
                const maxTemp = Math.max(...temps).toFixed(1);
                const avgTemp = (temps.reduce((sum, val) => sum + val, 0) / temps.length).toFixed(1);
                
                const minHum = humidities.length > 0 ? Math.min(...humidities).toFixed(1) : '--';
                const maxHum = humidities.length > 0 ? Math.max(...humidities).toFixed(1) : '--';
                const avgHum = humidities.length > 0 ? (humidities.reduce((sum, val) => sum + val, 0) / humidities.length).toFixed(1) : '--';
                
                tempDescriptionEl.textContent = `Graphique de température et humidité. Température : minimale ${minTemp}°C, maximale ${maxTemp}°C, moyenne ${avgTemp}°C. Humidité relative : minimale ${minHum}%, maximale ${maxHum}%, moyenne ${avgHum}%.`;
            } else {
                tempDescriptionEl.textContent = "Graphique de température et humidité. Aucune donnée sur la période sélectionnée.";
            }
        }

        const airconDescriptionEl = document.getElementById('airconStateChartDescription');
        if (airconDescriptionEl) {
            const onTicks = airconStates['on'] || 0;
            const offTicks = airconStates['off'] || 0;
            const unknownTicks = airconStates['unknown'] || 0;
            const totalTicks = onTicks + offTicks + unknownTicks;
            
            if (totalTicks > 0) {
                const onPct = Math.round((onTicks / totalTicks) * 100);
                const offPct = Math.round((offTicks / totalTicks) * 100);
                airconDescriptionEl.textContent = `Graphique de l'état de la climatisation. Climatisation allumée pendant ${onPct}% du temps, éteinte pendant ${offPct}% du temps.`;
            } else {
                airconDescriptionEl.textContent = "Graphique de l'état de la climatisation. Aucune donnée sur la période sélectionnée.";
            }
        }
    }

    updateStatusCards(aggregates) {
        const avgTemp = aggregates.avg_temperature ? parseFloat(aggregates.avg_temperature).toFixed(1) : '--';
        const avgHumidity = aggregates.avg_humidity ? parseFloat(aggregates.avg_humidity).toFixed(1) : '--';
        
        const tempElement = document.getElementById('avgTemp');
        const humidityElement = document.getElementById('avgHumidity');
        
        if (tempElement) tempElement.textContent = avgTemp;
        if (humidityElement) humidityElement.textContent = avgHumidity;
    }

    updateLatestTable(latestRecords) {
        const tbody = document.getElementById('latestTableBody');
        
        if (!latestRecords || latestRecords.length === 0) {
            tbody.textContent = '';
            const tr = document.createElement('tr');
            const td = document.createElement('td');
            td.colSpan = 5;
            td.className = 'text-center text-muted';
            td.textContent = 'Aucun enregistrement trouv\u00e9';
            tr.appendChild(td);
            tbody.appendChild(tr);
            return;
        }

        tbody.textContent = '';
        latestRecords.forEach(record => {
            const timestamp = new Date(record.timestamp).toLocaleString('fr-FR');
            const temp = record.temperature ? `${record.temperature}\u00b0C` : '--';
            const humidity = record.humidity ? `${record.humidity}%` : '--';
            const action = record.last_action || '--';
            
            const tr = document.createElement('tr');
            
            const tdTime = document.createElement('td');
            tdTime.textContent = timestamp;
            
            const tdTemp = document.createElement('td');
            tdTemp.textContent = temp;
            
            const tdHum = document.createElement('td');
            tdHum.textContent = humidity;
            
            const tdState = document.createElement('td');
            tdState.appendChild(this.formatAirconState(record.assumed_aircon_power));
            
            const tdAction = document.createElement('td');
            tdAction.textContent = action;
            
            tr.append(tdTime, tdTemp, tdHum, tdState, tdAction);
            tbody.appendChild(tr);
        });
    }

    formatAirconState(state) {
        const stateConfig = {
            'on':      { text: 'ON',  cls: 'bg-success' },
            'off':     { text: 'OFF', cls: 'bg-danger' },
            'unknown': { text: '?',   cls: 'bg-secondary' }
        };
        const config = stateConfig[state] || stateConfig['unknown'];
        const badge = document.createElement('span');
        badge.className = `badge ${config.cls}`;
        badge.textContent = config.text;
        return badge;
    }

    getTimeRangeStart() {
        const now = new Date();
        const range = this.currentFilters.timeRange;
        
        switch (range) {
            case '1h':
                return new Date(now.getTime() - 60 * 60 * 1000).toISOString();
            case '6h':
                return new Date(now.getTime() - 6 * 60 * 60 * 1000).toISOString();
            case '24h':
                return new Date(now.getTime() - 24 * 60 * 60 * 1000).toISOString();
            case 'custom':
                const customStart = document.getElementById('customStart').value;
                return customStart ? new Date(customStart).toISOString() : this.getTimeRangeStart();
            default:
                return this.getTimeRangeStart();
        }
    }

    applyFilters() {
        const timeRange = document.getElementById('timeRange').value;
        const granularity = document.getElementById('granularity').value;
        const metrics = Array.from(document.querySelectorAll('.metric-checkboxes input:checked'))
            .map(cb => cb.value);

        this.currentFilters = { timeRange, granularity, metrics };
        this.loadHistoryData();
        this.updateStatus('loading', 'Application des filtres...');
    }

    updateMetrics() {
        const checkedMetrics = Array.from(document.querySelectorAll('.metric-checkboxes input:checked'))
            .map(cb => cb.value);
        this.currentFilters.metrics = checkedMetrics;
        this.loadHistoryData();
    }

    updateStatus(type, message) {
        const indicator = document.getElementById('statusIndicator');
        const text = document.getElementById('statusText');
        const lastUpdate = document.getElementById('lastUpdate');

        // Update indicator
        indicator.className = 'status-indicator';
        if (type === 'success') {
            indicator.classList.add('status-success');
        } else if (type === 'error') {
            indicator.classList.add('status-error');
        } else if (type === 'loading') {
            indicator.classList.add('status-loading');
        }

        // Update text
        text.textContent = message;
        lastUpdate.textContent = new Date().toLocaleTimeString('fr-FR');
    }

    startRealTimeUpdates() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
        }
        // Update every 30 seconds
        this.updateInterval = setInterval(() => {
            this.loadHistoryData();
            this.loadAggregates();
            this.loadLatestRecords();
        }, 30000);
    }

    stopRealTimeUpdates() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
            this.updateInterval = null;
        }
    }

    destroy() {
        this.stopRealTimeUpdates();
        
        if (this.visibilityHandler) {
            document.removeEventListener('visibilitychange', this.visibilityHandler);
            this.visibilityHandler = null;
        }
        
        // Destroy charts
        Object.values(this.charts).forEach(chart => {
            if (chart) chart.destroy();
        });
    }
}

// Initialize dashboard safely
const initHistoryDashboard = () => {
    if (globalThis.historyDashboard) {
        globalThis.historyDashboard.destroy();
    }
    globalThis.historyDashboard = new HistoryDashboard();
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHistoryDashboard);
} else {
    initHistoryDashboard();
}

// Cleanup on page unload
globalThis.addEventListener('beforeunload', () => {
    if (globalThis.historyDashboard) {
        globalThis.historyDashboard.destroy();
    }
});
})();
