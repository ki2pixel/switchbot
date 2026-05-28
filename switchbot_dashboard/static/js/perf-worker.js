/**
 * SwitchBot Dashboard v2 - Performance Web Worker
 * Offloads continuous performance tracking, metric aggregation,
 * and sustained resource degradation warnings from the main thread.
 */
'use strict';

// Performance samples history
const metricsHistory = [];
const MAX_HISTORY_SIZE = 120; // Keep ~1 hour of samples at 30s intervals

self.onmessage = function(event) {
  const { type, data } = event.data;
  
  if (type === 'metrics') {
    const { fps, memory, timestamp } = data;
    
    // Add to local history
    metricsHistory.push({
      timestamp: timestamp || Date.now(),
      fps,
      memory
    });
    
    if (metricsHistory.length > MAX_HISTORY_SIZE) {
      metricsHistory.shift();
    }
    
    // 1. Analyze Memory
    if (memory) {
      const memoryRatio = memory.used / memory.limit;
      if (memoryRatio > 0.8) {
        console.warn(`[PerfWorker] ⚠️ High memory usage detected: ${memory.used}MB / ${memory.limit}MB (${Math.round(memoryRatio * 100)}%)`);
        self.postMessage({
          type: 'warning',
          metric: 'memory',
          message: 'High memory usage detected',
          details: memory
        });
      }
    }
    
    // 2. Analyze FPS
    if (fps !== undefined) {
      if (fps < 30) {
        console.warn(`[PerfWorker] ⚠️ Low FPS detected: ${fps} FPS`);
        self.postMessage({
          type: 'warning',
          metric: 'fps',
          message: 'Low FPS detected',
          details: { fps }
        });
      }
      
      // Analyze sustained performance degradation (e.g., last 3 updates all < 40 FPS)
      if (metricsHistory.length >= 3) {
        const lastThree = metricsHistory.slice(-3);
        const allLow = lastThree.every(m => m.fps !== undefined && m.fps < 40);
        if (allLow) {
          const avgFps = Math.round(lastThree.reduce((sum, m) => sum + m.fps, 0) / lastThree.length);
          console.warn(`[PerfWorker] 🚨 Sustained performance degradation detected! Average FPS: ${avgFps}`);
          self.postMessage({
            type: 'alert',
            metric: 'fps_sustained',
            message: `Sustained performance drop: Average ${avgFps} FPS`,
            details: { averageFps: avgFps }
          });
        }
      }
    }
  } else if (type === 'getReport') {
    // Generate aggregated performance report
    const validFpsSamples = metricsHistory.filter(m => m.fps !== undefined);
    const avgFps = validFpsSamples.length > 0
      ? validFpsSamples.reduce((sum, m) => sum + m.fps, 0) / validFpsSamples.length
      : 60;
      
    const maxMemory = metricsHistory.reduce((max, m) => Math.max(max, m.memory ? m.memory.used : 0), 0);
    
    self.postMessage({
      type: 'report',
      report: {
        samplesCount: metricsHistory.length,
        averageFps: Math.round(avgFps),
        maxMemoryUsedMb: maxMemory,
        history: metricsHistory
      }
    });
  }
};
