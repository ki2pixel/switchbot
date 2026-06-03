/**
 * SwitchBot Dashboard v2 - Performance Web Worker
 * Offloads continuous performance tracking, metric aggregation,
 * and sustained resource degradation warnings from the main thread.
 */
'use strict';

// Performance samples history
const metricsHistory = [];
const MAX_HISTORY_SIZE = 120; // Keep ~1 hour of samples at 30s intervals

function checkMemory(memory) {
  if (!memory) return;
  const memoryRatio = memory.used / memory.limit;
  if (memoryRatio > 0.8) {
    console.warn(`[PerfWorker] ⚠️ High memory usage detected: ${memory.used}MB / ${memory.limit}MB (${Math.round(memoryRatio * 100)}%)`);
    globalThis.postMessage({
      type: 'warning',
      metric: 'memory',
      message: 'High memory usage detected',
      details: memory
    });
  }
}

function checkFps(fps) {
  if (fps === undefined) return;
  
  if (fps < 30) {
    console.warn(`[PerfWorker] ⚠️ Low FPS detected: ${fps} FPS`);
    globalThis.postMessage({
      type: 'warning',
      metric: 'fps',
      message: 'Low FPS detected',
      details: { fps }
    });
  }
  
  if (metricsHistory.length >= 3) {
    const lastThree = metricsHistory.slice(-3);
    const allLow = lastThree.every(m => m.fps !== undefined && m.fps < 40);
    if (allLow) {
      const avgFps = Math.round(lastThree.reduce((sum, m) => sum + m.fps, 0) / lastThree.length);
      console.warn(`[PerfWorker] 🚨 Sustained performance degradation detected! Average FPS: ${avgFps}`);
      globalThis.postMessage({
        type: 'alert',
        metric: 'fps_sustained',
        message: `Sustained performance drop: Average ${avgFps} FPS`,
        details: { averageFps: avgFps }
      });
    }
  }
}

function handleMetrics(data) {
  const { fps, memory, timestamp } = data;
  
  metricsHistory.push({
    timestamp: timestamp || Date.now(),
    fps,
    memory
  });
  
  if (metricsHistory.length > MAX_HISTORY_SIZE) {
    metricsHistory.shift();
  }
  
  checkMemory(memory);
  checkFps(fps);
}

function generateReport() {
  const validFpsSamples = metricsHistory.filter(m => m.fps !== undefined);
  const avgFps = validFpsSamples.length > 0
    ? validFpsSamples.reduce((sum, m) => sum + m.fps, 0) / validFpsSamples.length
    : 60;
    
  const maxMemory = metricsHistory.reduce((max, m) => Math.max(max, m.memory ? m.memory.used : 0), 0);
  
  globalThis.postMessage({
    type: 'report',
    report: {
      samplesCount: metricsHistory.length,
      averageFps: Math.round(avgFps),
      maxMemoryUsedMb: maxMemory,
      history: metricsHistory
    }
  });
}

globalThis.onmessage = function(event) {
  const { type, data } = event.data;
  if (type === 'metrics') {
    handleMetrics(data);
  } else if (type === 'getReport') {
    generateReport();
  }
};
