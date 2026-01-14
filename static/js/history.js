/**
 * History Dashboard JavaScript
 * Handles real-time monitoring charts and data visualization
 */

class HistoryDashboard {
    constructor() {
        this.charts = {};
        this.updateInterval = null;
        this.currentFilters = {
            timeRange: '6h',
            granularity: 'minute',
            metrics: ['temperature', 'humidity', 'assumed_aircon_power']
        };
        
        this.init();
    }

    init() {
        this.initCharts();
        this.bindEvents();
        this.loadInitialData();
        this.startRealTimeUpdates();
    }

    initCharts() {
        const chartOptions = {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false,
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#e9ecef',
                        font: {
                            size: 12
                        }
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(33, 37, 41, 0.9)',
                    titleColor: '#ffffff',
                    bodyColor: '#e9ecef',
                    borderColor: '#495057',
                    borderWidth: 1
                }
            },
            scales: {
                x: {
                    type: 'time',
                    time: {
                        displayFormats: {
                            minute: 'HH:mm',
                            hour: 'HH:mm'
                        }
                    },
                    ticks: {
                        color: '#6c757d'
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
                            display: true,
                            text: 'Température (°C)',
                            color: '#dc3545'
                        },
                        ticks: {
                            color: '#6c757d'
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
                            display: true,
                            text: 'Humidité (%)',
                            color: '#0d6efd'
                        },
                        ticks: {
                            color: '#6c757d'
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
                            padding: 20
                        }
                    }
                }
            }
        });

        // API Usage Chart
        this.charts.apiUsage = new Chart(document.getElementById('apiUsageChart'), {
            type: 'line',
            data: {
                datasets: [{
                    label: 'Requêtes API cumulées',
                    data: [],
                    borderColor: '#ffc107',
                    backgroundColor: 'rgba(255, 193, 7, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                ...chartOptions,
                scales: {
                    ...chartOptions.scales,
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Requêtes',
                            color: '#ffc107'
                        },
                        ticks: {
                            color: '#6c757d'
                        },
                        grid: {
                            color: 'rgba(108, 117, 125, 0.2)'
                        }
                    }
                }
            }
        });

        // Error Distribution Chart
        this.charts.errors = new Chart(document.getElementById('errorChart'), {
            type: 'bar',
            data: {
                labels: [],
                datasets: [{
                    label: 'Erreurs',
                    data: [],
                    backgroundColor: 'rgba(220, 53, 69, 0.6)',
                    borderColor: '#dc3545',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            color: '#6c757d'
                        },
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Nombre d\'erreurs',
                            color: '#dc3545'
                        },
                        ticks: {
                            color: '#6c757d'
                        },
                        grid: {
                            color: 'rgba(108, 117, 125, 0.2)'
                        }
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
        document.getElementById('resetZoomTemp').addEventListener('click', () => {
            this.charts.tempHumidity.resetZoom();
        });

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
    }

    async loadInitialData() {
        try {
            await Promise.all([
                this.loadHistoryData(),
                this.loadAggregates(),
                this.loadLatestRecords()
            ]);
            this.updateStatus('success', 'Données chargées');
        } catch (error) {
            console.error('Error loading initial data:', error);
            this.updateStatus('error', 'Erreur de chargement');
        }
    }

    async loadHistoryData() {
        const params = new URLSearchParams({
            start: this.getTimeRangeStart(),
            end: new Date().toISOString(),
            granularity: this.currentFilters.granularity,
            metrics: this.currentFilters.metrics
        });

        const response = await fetch(`/history/api/data?${params}`);
        if (!response.ok) throw new Error('Failed to load history data');
        
        const data = await response.json();
        this.updateCharts(data.data);
    }

    async loadAggregates() {
        const response = await fetch('/history/api/aggregates?period_hours=6');
        if (!response.ok) throw new Error('Failed to load aggregates');
        
        const data = await response.json();
        this.updateStatusCards(data.aggregates);
    }

    async loadLatestRecords() {
        const response = await fetch('/history/api/latest?limit=10');
        if (!response.ok) throw new Error('Failed to load latest records');
        
        const data = await response.json();
        this.updateLatestTable(data.latest);
    }

    updateCharts(historyData) {
        if (!historyData || historyData.length === 0) return;

        // Update temperature & humidity chart
        const tempData = historyData.map(d => ({
            x: d.timestamp,
            y: d.temperature
        })).filter(d => d.y !== null);

        const humidityData = historyData.map(d => ({
            x: d.timestamp,
            y: d.humidity
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

        // Update API usage chart
        const apiData = historyData.map(d => ({
            x: d.timestamp,
            y: d.api_requests_today || 0
        })).filter(d => d.y > 0);

        this.charts.apiUsage.data.datasets[0].data = apiData;
        this.charts.apiUsage.update('none');

        // Update error chart
        const errorCounts = historyData.reduce((acc, d) => {
            const errors = d.error_count || 0;
            if (errors > 0) {
                const hour = new Date(d.timestamp).getHours();
                const label = `${hour}h`;
                acc[label] = (acc[label] || 0) + errors;
            }
            return acc;
        }, {});

        this.charts.errors.data.labels = Object.keys(errorCounts);
        this.charts.errors.data.datasets[0].data = Object.values(errorCounts);
        this.charts.errors.update('none');
    }

    updateStatusCards(aggregates) {
        document.getElementById('avgTemp').textContent = 
            aggregates.avg_temperature ? aggregates.avg_temperature.toFixed(1) : '--';
        document.getElementById('avgHumidity').textContent = 
            aggregates.avg_humidity ? aggregates.avg_humidity.toFixed(1) : '--';
        document.getElementById('totalRecords').textContent = 
            aggregates.total_records || '--';
        document.getElementById('totalErrors').textContent = 
            aggregates.total_errors || '--';
    }

    updateLatestTable(latestRecords) {
        const tbody = document.getElementById('latestTableBody');
        
        if (!latestRecords || latestRecords.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="6" class="text-center text-muted">
                        Aucun enregistrement trouvé
                    </td>
                </tr>
            `;
            return;
        }

        tbody.innerHTML = latestRecords.map(record => {
            const timestamp = new Date(record.timestamp).toLocaleString('fr-FR');
            const temp = record.temperature ? `${record.temperature}°C` : '--';
            const humidity = record.humidity ? `${record.humidity}%` : '--';
            const airconState = this.formatAirconState(record.assumed_aircon_power);
            const action = record.last_action || '--';
            const errors = record.error_count || 0;
            
            return `
                <tr>
                    <td>${timestamp}</td>
                    <td>${temp}</td>
                    <td>${humidity}</td>
                    <td>${airconState}</td>
                    <td>${action}</td>
                    <td>${errors}</td>
                </tr>
            `;
        }).join('');
    }

    formatAirconState(state) {
        const stateMap = {
            'on': '<span class="badge bg-success">ON</span>',
            'off': '<span class="badge bg-danger">OFF</span>',
            'unknown': '<span class="badge bg-secondary">?</span>'
        };
        return stateMap[state] || stateMap['unknown'];
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
        // Update every 30 seconds
        this.updateInterval = setInterval(() => {
            this.loadHistoryData();
            this.loadAggregates();
            this.loadLatestRecords();
        }, 30000);
    }

    destroy() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
        }
        
        // Destroy charts
        Object.values(this.charts).forEach(chart => {
            if (chart) chart.destroy();
        });
    }
}

// Initialize dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.historyDashboard = new HistoryDashboard();
});

// Cleanup on page unload
window.addEventListener('beforeunload', () => {
    if (window.historyDashboard) {
        window.historyDashboard.destroy();
    }
});
