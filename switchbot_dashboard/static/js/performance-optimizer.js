/**
 * Performance Optimizations Module
 * Implements lazy loading, code splitting, and performance monitoring
 */
(function() {
  'use strict';
  
  class PerformanceOptimizer {
    constructor() {
      this.observers = new Map();
      this.loadedAssets = new Set();
      this.performanceMetrics = {
        navigationStart: performance.timing.navigationStart,
        domContentLoaded: performance.timing.domContentLoadedEventEnd,
        loadComplete: performance.timing.loadEventEnd
      };
      
      this.init();
    }
    
    init() {
      this.setupLazyLoading();
      this.setupCodeSplitting();
      this.setupPerformanceMonitoring();
      this.optimizeImages();
      this.setupResourceHints();
    }
    
    setupLazyLoading() {
      // Lazy load images and iframes
      if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              this.loadImage(entry.target);
              imageObserver.unobserve(entry.target);
            }
          });
        }, {
          rootMargin: '50px 0px',
          threshold: 0.01
        });
        
        // Observe all images with data-src
        document.querySelectorAll('img[data-src]').forEach(img => {
          imageObserver.observe(img);
        });
        
        this.observers.set('images', imageObserver);
      }
    }
    
    loadImage(img) {
      const src = img.dataset.src;
      if (src && !this.loadedAssets.has(src)) {
        img.src = src;
        img.classList.remove('lazy-load');
        img.classList.add('loaded');
        this.loadedAssets.add(src);
        
        // Add fade-in effect
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.3s ease';
        setTimeout(() => {
          img.style.opacity = '1';
        }, 10);
      }
    }
    
    setupCodeSplitting() {
      // Dynamic import for non-critical JavaScript modules
      this.loadModuleWhenNeeded = async (moduleName, element) => {
        try {
          const module = await import(`/static/js/modules/${moduleName}.js`);
          if (module.default) {
            module.default(element);
          }
        } catch (error) {
          console.warn(`Failed to load module ${moduleName}:`, error);
        }
      };
      
      // Load history chart module only when history page is visited
      if (window.location.pathname.includes('/history')) {
        this.loadModuleWhenNeeded('history-chart');
      }
      
      // Load device management module only on devices page
      if (window.location.pathname.includes('/devices')) {
        this.loadModuleWhenNeeded('device-manager');
      }
    }
    
    setupPerformanceMonitoring() {
      // Monitor Core Web Vitals
      this.measureCoreWebVitals();
      
      // Monitor memory usage
      if (performance.memory) {
        setInterval(() => {
          const memoryUsage = {
            used: Math.round(performance.memory.usedJSHeapSize / 1048576),
            total: Math.round(performance.memory.totalJSHeapSize / 1048576),
            limit: Math.round(performance.memory.jsHeapSizeLimit / 1048576)
          };
          
          // Log memory warnings
          if (memoryUsage.used / memoryUsage.limit > 0.8) {
            console.warn('High memory usage detected:', memoryUsage);
          }
        }, 30000); // Check every 30 seconds
      }
      
      // Monitor FPS
      this.monitorFPS();
    }
    
    measureCoreWebVitals() {
      // Largest Contentful Paint (LCP)
      if ('PerformanceObserver' in window) {
        const lcpObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          const lastEntry = entries[entries.length - 1];
          console.log('LCP:', lastEntry.renderTime || lastEntry.loadTime);
        });
        lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
        
        // First Input Delay (FID)
        const fidObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          entries.forEach(entry => {
            console.log('FID:', entry.processingStart - entry.startTime);
          });
        });
        fidObserver.observe({ entryTypes: ['first-input'] });
        
        // Cumulative Layout Shift (CLS)
        let clsValue = 0;
        const clsObserver = new PerformanceObserver((list) => {
          list.getEntries().forEach(entry => {
            if (!entry.hadRecentInput) {
              clsValue += entry.value;
            }
          });
          console.log('CLS:', clsValue);
        });
        clsObserver.observe({ entryTypes: ['layout-shift'] });
      }
    }
    
    monitorFPS() {
      let lastTime = performance.now();
      let frameCount = 0;
      
      const measureFPS = () => {
        frameCount++;
        const currentTime = performance.now();
        
        if (currentTime >= lastTime + 1000) {
          const fps = Math.round((frameCount * 1000) / (currentTime - lastTime));
          
          // Log FPS warnings
          if (fps < 30) {
            console.warn('Low FPS detected:', fps);
          }
          
          frameCount = 0;
          lastTime = currentTime;
        }
        
        requestAnimationFrame(measureFPS);
      };
      
      requestAnimationFrame(measureFPS);
    }
    
    optimizeImages() {
      // Add loading="lazy" to all images that don't have it
      document.querySelectorAll('img:not([loading])').forEach(img => {
        img.loading = 'lazy';
      });
      
      // Optimize existing images
      document.querySelectorAll('img').forEach(img => {
        // Add error handling
        img.addEventListener('error', () => {
          img.src = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSIjMzA3MEE4Ii8+CjxwYXRoIGQ9Ik0xMiA2VjZIMTJWMTJWMTJaIiBmaWxsPSIjRkZGIi8+Cjwvc3ZnPgo=';
        });
        
        // Add CSS for smooth loading
        img.style.transition = 'opacity 0.3s ease';
      });
    }
    
    setupResourceHints() {
      // Add prefetch for critical resources
      const criticalResources = [
        '/static/css/theme.css',
        '/static/js/loaders.js'
      ];
      
      criticalResources.forEach(resource => {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = resource;
        document.head.appendChild(link);
      });
      
      // Add preconnect for external domains
      const externalDomains = [
        'https://cdn.jsdelivr.net'
      ];
      
      externalDomains.forEach(domain => {
        const link = document.createElement('link');
        link.rel = 'preconnect';
        link.href = domain;
        document.head.appendChild(link);
      });
    }
    
    // Public API for manual optimization
    optimizeElement(element) {
      // Add GPU acceleration for animations
      element.style.willChange = 'transform, opacity';
      element.style.transform = 'translateZ(0)';
      
      // Remove will-change after animation completes
      setTimeout(() => {
        element.style.willChange = 'auto';
      }, 1000);
    }
    
    // Cleanup method
    destroy() {
      this.observers.forEach(observer => observer.disconnect());
      this.observers.clear();
    }
  }
  
  // Initialize performance optimizer
  let performanceOptimizer;
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      performanceOptimizer = new PerformanceOptimizer();
    });
  } else {
    performanceOptimizer = new PerformanceOptimizer();
  }
  
  // Expose to global scope for manual usage
  window.PerformanceOptimizer = PerformanceOptimizer;
  window.performanceOptimizer = performanceOptimizer;
})();
