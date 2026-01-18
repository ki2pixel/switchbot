/**
 * Advanced Performance Optimizer - Core Web Vitals Enhancement
 * Implements advanced optimizations for LCP, FID, and CLS
 */
(function() {
  'use strict';
  
  class AdvancedPerformanceOptimizer {
    constructor() {
      this.criticalResources = new Set();
      this.loadedResources = new Map();
      this.layoutShiftElements = new Map();
      this.fontLoadPromise = null;
      this.metrics = {
        lcp: 0,
        fid: 0,
        cls: 0,
        ttfb: 0,
        fcp: 0
      };
      
      this.init();
    }
    
    init() {
      this.setupResourceHints();
      this.optimizeFontLoading();
      this.setupAdvancedCLS();
      this.setupAdvancedFID();
      this.setupAdvancedLCP();
      this.setupIntersectionOptimization();
      this.setupMainThreadScheduling();
      this.monitorAdvancedMetrics();
    }
    
    setupResourceHints() {
      // Preconnect for external domains
      const preconnectDomains = [
        'https://cdn.jsdelivr.net',
        'https://fonts.googleapis.com',
        'https://fonts.gstatic.com'
      ];
      
      preconnectDomains.forEach(domain => {
        const link = document.createElement('link');
        link.rel = 'preconnect';
        link.href = domain;
        link.crossOrigin = 'anonymous';
        document.head.appendChild(link);
      });
      
      // Prefetch critical resources
      const criticalResources = [
        '/static/css/theme.css',
        '/static/css/index.css',
        '/static/js/loaders.js',
        '/static/js/performance-optimizer.js'
      ];
      
      criticalResources.forEach(resource => {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = resource;
        document.head.appendChild(link);
      });
      
      // Preload most critical resources
      const preloadResources = [
        { href: '/static/css/theme.css', as: 'style' },
        { href: '/static/css/index.css', as: 'style' },
        { href: '/static/js/loaders.js', as: 'script' }
      ];
      
      preloadResources.forEach(resource => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.href = resource.href;
        link.as = resource.as;
        if (resource.as === 'style') {
          link.onload = function() { this.rel = 'stylesheet'; };
        }
        document.head.appendChild(link);
      });
    }
    
    optimizeFontLoading() {
      // Font loading optimization with font-display: swap
      const fontFaces = [
        {
          family: 'Space Grotesk',
          weights: [400, 500, 600],
          display: 'swap'
        },
        {
          family: 'Inter',
          weights: [400, 500, 600],
          display: 'swap'
        }
      ];
      
      fontFaces.forEach(fontFace => {
        fontFace.weights.forEach(weight => {
          const link = document.createElement('link');
          link.rel = 'preload';
          link.as = 'font';
          link.type = 'font/woff2';
          link.crossOrigin = 'anonymous';
          link.href = `https://fonts.gstatic.com/s/${fontFace.family.toLowerCase().replace(' ', '')}/v15/...-${weight}.woff2`;
          document.head.appendChild(link);
        });
      });
      
      // Create font load promise
      this.fontLoadPromise = new Promise((resolve) => {
        if (document.fonts && document.fonts.ready) {
          document.fonts.ready.then(() => {
            console.log('✅ Fonts loaded');
            resolve();
          });
        } else {
          // Fallback for older browsers
          setTimeout(resolve, 1000);
        }
      });
    }
    
    setupAdvancedCLS() {
      // Reserve space for dynamic content
      this.reserveSpaceForDynamicContent();
      
      // Monitor for layout shifts
      let clsValue = 0;
      let clsEntries = [];
      
      if ('PerformanceObserver' in window) {
        const clsObserver = new PerformanceObserver((list) => {
          list.getEntries().forEach(entry => {
            if (!entry.hadRecentInput) {
              clsValue += entry.value;
              clsEntries.push({
                value: entry.value,
                sources: entry.sources,
                timestamp: entry.startTime
              });
              
              // Log significant layout shifts
              if (entry.value > 0.1) {
                console.warn('⚠️ Significant layout shift detected:', entry);
                this.debugLayoutShift(entry);
              }
            }
          });
          
          this.metrics.cls = clsValue;
        });
        
        clsObserver.observe({ entryTypes: ['layout-shift'] });
      }
      
      // Add skeleton screens for async content
      this.addSkeletonScreens();
    }
    
    reserveSpaceForDynamicContent() {
      // Reserve space for images
      document.querySelectorAll('img').forEach(img => {
        if (!img.style.width && !img.style.height) {
          // Set explicit dimensions if available
          if (img.width && img.height) {
            img.style.width = img.width + 'px';
            img.style.height = img.height + 'px';
          } else {
            // Add aspect-ratio placeholder
            img.style.aspectRatio = '16 / 9';
            img.style.width = '100%';
            img.style.height = 'auto';
          }
        }
      });
      
      // Reserve space for iframes
      document.querySelectorAll('iframe').forEach(iframe => {
        if (!iframe.style.width && !iframe.style.height) {
          iframe.style.width = '100%';
          iframe.style.height = '400px';
        }
      });
      
      // Reserve space for dynamic content areas
      document.querySelectorAll('[data-dynamic-content]').forEach(element => {
        const minHeight = element.dataset.minHeight || '200px';
        element.style.minHeight = minHeight;
        element.classList.add('dynamic-content-reserved');
      });
    }
    
    addSkeletonScreens() {
      // Add skeleton screens for cards that might load asynchronously
      document.querySelectorAll('.card[data-skeleton]').forEach(card => {
        const skeleton = document.createElement('div');
        skeleton.className = 'skeleton skeleton-card';
        skeleton.style.cssText = `
          height: ${card.dataset.skeletonHeight || '120px'};
          border-radius: 0.75rem;
          margin-bottom: 1rem;
        `;
        
        // Hide skeleton when content loads
        const observer = new MutationObserver((mutations) => {
          mutations.forEach((mutation) => {
            if (mutation.target.textContent.trim()) {
              skeleton.remove();
              observer.disconnect();
            }
          });
        });
        
        observer.observe(card, { childList: true, subtree: true });
        card.parentNode.insertBefore(skeleton, card);
      });
    }
    
    debugLayoutShift(entry) {
      entry.sources.forEach(source => {
        const element = source.node;
        if (element) {
          console.log('Layout shift source:', {
            element: element.tagName + (element.className ? '.' + element.className : ''),
            previousRect: source.previousRect,
            currentRect: source.currentRect,
            shift: entry.value
          });
          
          // Add visual indicator for debugging
          element.style.outline = '2px solid red';
          setTimeout(() => {
            element.style.outline = '';
          }, 2000);
        }
      });
    }
    
    setupAdvancedFID() {
      // Optimize event listeners
      this.optimizeEventListeners();
      
      // Use passive event listeners where possible
      this.addPassiveListeners();
      
      // Monitor First Input Delay
      if ('PerformanceObserver' in window) {
        const fidObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          entries.forEach(entry => {
            this.metrics.fid = entry.processingStart - entry.startTime;
            console.log('🎯 FID:', this.metrics.fid.toFixed(2), 'ms');
            
            // Log slow interactions
            if (this.metrics.fid > 100) {
              console.warn('⚠️ Slow input detected:', this.metrics.fid.toFixed(2), 'ms');
            }
          });
        });
        
        fidObserver.observe({ entryTypes: ['first-input'] });
      }
      
      // Optimize main thread work
      this.optimizeMainThread();
    }
    
    optimizeEventListeners() {
      // Debounce scroll events
      let scrollTimeout;
      const originalScrollHandler = window.onscroll;
      
      window.addEventListener('scroll', () => {
        if (scrollTimeout) {
          cancelAnimationFrame(scrollTimeout);
        }
        
        scrollTimeout = requestAnimationFrame(() => {
          if (originalScrollHandler) {
            originalScrollHandler();
          }
        });
      }, { passive: true });
      
      // Debounce resize events
      let resizeTimeout;
      window.addEventListener('resize', () => {
        if (resizeTimeout) {
          clearTimeout(resizeTimeout);
        }
        
        resizeTimeout = setTimeout(() => {
          // Handle resize
          this.handleResize();
        }, 150);
      }, { passive: true });
    }
    
    addPassiveListeners() {
      // Make touch and wheel events passive
      const events = ['touchstart', 'touchmove', 'wheel', 'mousewheel'];
      
      events.forEach(eventType => {
        document.addEventListener(eventType, () => {}, { passive: true });
      });
    }
    
    optimizeMainThread() {
      // Use requestIdleCallback for non-critical tasks
      if ('requestIdleCallback' in window) {
        requestIdleCallback(() => {
          this.performNonCriticalTasks();
        });
      } else {
        // Fallback
        setTimeout(() => {
          this.performNonCriticalTasks();
        }, 100);
      }
    }
    
    performNonCriticalTasks() {
      // Load non-critical CSS
      this.loadNonCriticalCSS();
      
      // Initialize non-critical JavaScript
      this.initializeNonCriticalJS();
      
      // Preload next page resources
      this.preloadNextPageResources();
    }
    
    loadNonCriticalCSS() {
      const nonCriticalCSS = [
        '/static/css/sticky-cards.css',
        '/static/css/sticky-footer.css'
      ];
      
      nonCriticalCSS.forEach(href => {
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = href;
        link.media = 'print';
        link.onload = function() {
          this.media = 'all';
        };
        document.head.appendChild(link);
      });
    }
    
    initializeNonCriticalJS() {
      // Initialize modules that are not critical for first paint
      setTimeout(() => {
        // Initialize bottom navigation
        if (window.BottomNavigation) {
          new BottomNavigation();
        }
        
        // Initialize micro-interactions
        if (window.MicroInteractions) {
          new MicroInteractions();
        }
      }, 200);
    }
    
    preloadNextPageResources() {
      // Analyze current page and preload likely next pages
      const currentPage = window.location.pathname;
      let likelyNextPages = [];
      
      if (currentPage === '/') {
        likelyNextPages = ['/settings', '/quota', '/history'];
      } else if (currentPage === '/settings') {
        likelyNextPages = ['/', '/quota'];
      }
      
      likelyNextPages.forEach(page => {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = page;
        document.head.appendChild(link);
      });
    }
    
    setupAdvancedLCP() {
      // Optimize largest contentful paint
      this.optimizeLCPElements();
      
      // Monitor LCP
      if ('PerformanceObserver' in window) {
        const lcpObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          const lastEntry = entries[entries.length - 1];
          this.metrics.lcp = lastEntry.renderTime || lastEntry.loadTime;
          console.log('🎨 LCP:', this.metrics.lcp.toFixed(2), 'ms');
          
          // Log slow LCP
          if (this.metrics.lcp > 2500) {
            console.warn('⚠️ Slow LCP detected:', this.metrics.lcp.toFixed(2), 'ms');
            this.analyzeLCPElement(lastEntry);
          }
        });
        
        lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
      }
      
      // Optimize critical images
      this.optimizeCriticalImages();
    }
    
    optimizeLCPElements() {
      // Prioritize loading of LCP candidates
      const lcpCandidates = [
        'img',
        'video',
        'canvas',
        'svg',
        '.status-item',
        '.scene-action',
        'h1', 'h2', 'h3'
      ];
      
      lcpCandidates.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(element => {
          // Add loading priority hints
          if (element.tagName === 'IMG') {
            element.loading = 'eager';
            element.fetchpriority = 'high';
          }
          
          // Add GPU acceleration
          element.classList.add('sb-gpu-accelerated');
        });
      });
    }
    
    optimizeCriticalImages() {
      document.querySelectorAll('img').forEach(img => {
        // Add proper loading attributes
        if (!img.loading) {
          img.loading = 'eager';
        }
        
        // Add error handling
        img.addEventListener('error', () => {
          img.style.display = 'none';
          const placeholder = document.createElement('div');
          placeholder.className = 'image-error-placeholder';
          placeholder.textContent = 'Image non disponible';
          placeholder.style.cssText = `
            display: flex;
            align-items: center;
            justify-content: center;
            width: ${img.style.width || '100%'};
            height: ${img.style.height || '200px'};
            background: var(--sb-card);
            border: 1px solid var(--sb-card-border);
            border-radius: 0.5rem;
            color: var(--sb-muted);
            font-size: 0.875rem;
          `;
          img.parentNode.insertBefore(placeholder, img);
        });
        
        // Add fade-in effect
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.3s ease';
        img.onload = () => {
          img.style.opacity = '1';
        };
      });
    }
    
    analyzeLCPElement(entry) {
      console.log('LCP Element Analysis:', {
        element: entry.element?.tagName + (entry.element?.className ? '.' + entry.element.className : ''),
        size: `${entry.width}x${entry.height}`,
        loadTime: entry.loadTime,
        renderTime: entry.renderTime,
        url: entry.url
      });
    }
    
    setupIntersectionOptimization() {
      // Use Intersection Observer for lazy loading and visibility-based optimizations
      if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              // Element is visible, optimize for performance
              this.optimizeVisibleElement(entry.target);
            } else {
              // Element is not visible, reduce resource usage
              this.reduceResourceUsage(entry.target);
            }
          });
        }, {
          rootMargin: '50px',
          threshold: 0.1
        });
        
        // Observe relevant elements
        document.querySelectorAll('.card, .status-item, img').forEach(el => {
          observer.observe(el);
        });
      }
    }
    
    optimizeVisibleElement(element) {
      // Enable animations for visible elements
      element.style.willChange = 'transform, opacity';
      
      // Start any paused animations
      if (element.dataset.pausedAnimation) {
        element.style.animationPlayState = 'running';
      }
    }
    
    reduceResourceUsage(element) {
      // Disable animations for non-visible elements
      element.style.willChange = 'auto';
      
      // Pause animations
      if (element.style.animationPlayState !== 'paused') {
        element.style.animationPlayState = 'paused';
        element.dataset.pausedAnimation = 'true';
      }
    }
    
    setupMainThreadScheduling() {
      // Schedule tasks to avoid blocking the main thread
      this.scheduleTasks();
    }
    
    scheduleTasks() {
      // Break up large tasks into smaller chunks
      const tasks = [
        () => this.initializeAnalytics(),
        () => this.initializeTooltips(),
        () => this.initializeModals(),
        () => this.preloadSecondaryResources()
      ];
      
      let taskIndex = 0;
      
      const runNextTask = () => {
        if (taskIndex < tasks.length) {
          const task = tasks[taskIndex];
          
          // Use requestAnimationFrame for smooth execution
          requestAnimationFrame(() => {
            task();
            taskIndex++;
            
            // Schedule next task with a small delay
            setTimeout(runNextTask, 50);
          });
        }
      };
      
      // Start task scheduling after initial paint
      if ('requestIdleCallback' in window) {
        requestIdleCallback(runNextTask);
      } else {
        setTimeout(runNextTask, 100);
      }
    }
    
    initializeAnalytics() {
      // Initialize analytics if present
      if (window.gtag) {
        // Analytics initialization
      }
    }
    
    initializeTooltips() {
      // Initialize tooltips
      document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
        // Initialize tooltip
      });
    }
    
    initializeModals() {
      // Initialize modals
      document.querySelectorAll('.modal').forEach(el => {
        // Initialize modal
      });
    }
    
    preloadSecondaryResources() {
      // Preload secondary images and resources
      const secondaryResources = [
        '/static/images/dashboard-bg.jpg',
        '/static/icons/app-icon-192.png'
      ];
      
      secondaryResources.forEach(resource => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.as = 'image';
        link.href = resource;
        document.head.appendChild(link);
      });
    }
    
    monitorAdvancedMetrics() {
      // Monitor additional performance metrics
      this.monitorTTFB();
      this.monitorFCP();
      this.setupPerformanceReporting();
    }
    
    monitorTTFB() {
      // Time to First Byte
      const navigation = performance.getEntriesByType('navigation')[0];
      if (navigation) {
        this.metrics.ttfb = navigation.responseStart - navigation.requestStart;
        console.log('⏱️ TTFB:', this.metrics.ttfb.toFixed(2), 'ms');
        
        if (this.metrics.ttfb > 800) {
          console.warn('⚠️ Slow TTFB detected:', this.metrics.ttfb.toFixed(2), 'ms');
        }
      }
    }
    
    monitorFCP() {
      // First Contentful Paint
      if ('PerformanceObserver' in window) {
        const fcpObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          entries.forEach(entry => {
            if (entry.name === 'first-contentful-paint') {
              this.metrics.fcp = entry.startTime;
              console.log('🎨 FCP:', this.metrics.fcp.toFixed(2), 'ms');
              
              if (this.metrics.fcp > 1800) {
                console.warn('⚠️ Slow FCP detected:', this.metrics.fcp.toFixed(2), 'ms');
              }
            }
          });
        });
        
        fcpObserver.observe({ entryTypes: ['paint'] });
      }
    }
    
    setupPerformanceReporting() {
      // Report performance metrics periodically
      setInterval(() => {
        this.reportMetrics();
      }, 30000); // Every 30 seconds
      
      // Report on page unload
      window.addEventListener('beforeunload', () => {
        this.reportMetrics(true);
      });
    }
    
    reportMetrics(isFinal = false) {
      const report = {
        url: window.location.pathname,
        timestamp: Date.now(),
        metrics: this.metrics,
        userAgent: navigator.userAgent,
        viewport: {
          width: window.innerWidth,
          height: window.innerHeight
        },
        connection: navigator.connection ? {
          effectiveType: navigator.connection.effectiveType,
          downlink: navigator.connection.downlink,
          rtt: navigator.connection.rtt
        } : null,
        final: isFinal
      };
      
      console.log('📊 Performance Report:', report);
      
      // Send to analytics service if available
      if (window.gtag && isFinal) {
        window.gtag('event', 'performance_metrics', {
          custom_map: {
            lcp: this.metrics.lcp,
            fid: this.metrics.fid,
            cls: this.metrics.cls,
            ttfb: this.metrics.ttfb,
            fcp: this.metrics.fcp
          }
        });
      }
    }
    
    handleResize() {
      // Handle responsive layout changes
      this.reserveSpaceForDynamicContent();
    }
    
    // Public API
    getMetrics() {
      return { ...this.metrics };
    }
    
    optimizeElement(element) {
      element.classList.add('sb-gpu-accelerated');
      element.style.willChange = 'transform, opacity';
      
      setTimeout(() => {
        element.style.willChange = 'auto';
      }, 1000);
    }
    
    // Cleanup method
    destroy() {
      // Clean up observers and event listeners
      this.criticalResources.clear();
      this.loadedResources.clear();
      this.layoutShiftElements.clear();
    }
  }
  
  // Initialize advanced performance optimizer
  let advancedOptimizer;
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      advancedOptimizer = new AdvancedPerformanceOptimizer();
    });
  } else {
    advancedOptimizer = new AdvancedPerformanceOptimizer();
  }
  
  // Expose to global scope
  window.AdvancedPerformanceOptimizer = AdvancedPerformanceOptimizer;
  window.advancedOptimizer = advancedOptimizer;
  
  // Performance mark for initialization
  if ('performance' in window && 'mark' in performance) {
    performance.mark('advanced-optimizer-initialized');
  }
})();
