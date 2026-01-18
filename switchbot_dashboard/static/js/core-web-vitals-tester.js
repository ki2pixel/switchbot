/**
 * Core Web Vitals Testing Script
 * Tests and validates performance metrics for Phase 5 optimizations
 */
(function() {
  'use strict';
  
  class CoreWebVitalsTester {
    constructor() {
      this.metrics = {
        lcp: 0,
        fid: 0,
        cls: 0,
        ttfb: 0,
        fcp: 0,
        loadTime: 0
      };
      
      this.thresholds = {
        lcp: { good: 2500, needsImprovement: 4000 },
        fid: { good: 100, needsImprovement: 300 },
        cls: { good: 0.1, needsImprovement: 0.25 },
        ttfb: { good: 800, needsImprovement: 1800 },
        fcp: { good: 1800, needsImprovement: 3000 }
      };
      
      this.testResults = [];
      this.init();
    }
    
    init() {
      console.log('🧪 Core Web Vitals Tester initialized');
      this.setupPerformanceObservers();
      this.measurePageLoad();
      this.runAutomatedTests();
      this.generateReport();
    }
    
    setupPerformanceObservers() {
      // LCP Observer
      if ('PerformanceObserver' in window) {
        const lcpObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          const lastEntry = entries[entries.length - 1];
          this.metrics.lcp = lastEntry.renderTime || lastEntry.loadTime;
          console.log('🎨 LCP measured:', this.metrics.lcp.toFixed(2), 'ms');
        });
        lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
        
        // FID Observer
        const fidObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          entries.forEach(entry => {
            this.metrics.fid = entry.processingStart - entry.startTime;
            console.log('⚡ FID measured:', this.metrics.fid.toFixed(2), 'ms');
          });
        });
        fidObserver.observe({ entryTypes: ['first-input'] });
        
        // CLS Observer
        let clsValue = 0;
        const clsObserver = new PerformanceObserver((list) => {
          list.getEntries().forEach(entry => {
            if (!entry.hadRecentInput) {
              clsValue += entry.value;
            }
          });
          this.metrics.cls = clsValue;
          console.log('📐 CLS measured:', this.metrics.cls.toFixed(3));
        });
        clsObserver.observe({ entryTypes: ['layout-shift'] });
        
        // FCP Observer
        const fcpObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          entries.forEach(entry => {
            if (entry.name === 'first-contentful-paint') {
              this.metrics.fcp = entry.startTime;
              console.log('🖼️ FCP measured:', this.metrics.fcp.toFixed(2), 'ms');
            }
          });
        });
        fcpObserver.observe({ entryTypes: ['paint'] });
      }
    }
    
    measurePageLoad() {
      window.addEventListener('load', () => {
        setTimeout(() => {
          const navigation = performance.getEntriesByType('navigation')[0];
          if (navigation) {
            this.metrics.ttfb = navigation.responseStart - navigation.requestStart;
            this.metrics.loadTime = navigation.loadEventEnd - navigation.startTime;
            
            console.log('🌐 TTFB measured:', this.metrics.ttfb.toFixed(2), 'ms');
            console.log('⏱️ Load Time measured:', this.metrics.loadTime.toFixed(2), 'ms');
          }
          
          // Run tests after page is fully loaded
          setTimeout(() => {
            this.runPerformanceTests();
          }, 1000);
        }, 0);
      });
    }
    
    runAutomatedTests() {
      console.log('🔬 Running automated performance tests...');
      
      // Test 1: Critical CSS Inlining
      this.testCriticalCSSInlining();
      
      // Test 2: Resource Loading
      this.testResourceLoading();
      
      // Test 3: Font Loading
      this.testFontLoading();
      
      // Test 4: Image Optimization
      this.testImageOptimization();
      
      // Test 5: JavaScript Execution
      this.testJavaScriptExecution();
    }
    
    testCriticalCSSInlining() {
      const criticalCSS = document.querySelector('style');
      const hasCriticalCSS = criticalCSS && criticalCSS.textContent.includes('Critical CSS');
      
      this.addTestResult({
        name: 'Critical CSS Inlining',
        passed: hasCriticalCSS,
        details: hasCriticalCSS ? '✅ Critical CSS found inline' : '❌ Critical CSS not found',
        impact: hasCriticalCSS ? 'Positive impact on LCP' : 'Negative impact on LCP'
      });
    }
    
    testResourceLoading() {
      const preloads = document.querySelectorAll('link[rel="preload"]');
      const preconnects = document.querySelectorAll('link[rel="preconnect"]');
      
      this.addTestResult({
        name: 'Resource Loading Optimization',
        passed: preloads.length > 0 && preconnects.length > 0,
        details: `Found ${preloads.length} preloads and ${preconnects.length} preconnects`,
        impact: 'Reduces network latency for critical resources'
      });
    }
    
    testFontLoading() {
      const fontPreload = document.querySelector('link[href*="fonts.googleapis.com"]');
      const fontDisplay = document.querySelector('style')?.textContent.includes('font-display: swap');
      
      this.addTestResult({
        name: 'Font Loading Optimization',
        passed: fontPreload && fontDisplay,
        details: fontPreload ? '✅ Font preloading enabled' : '❌ Font preloading missing',
        impact: 'Improves FCP and reduces FOIT/FOUT'
      });
    }
    
    testImageOptimization() {
      const images = document.querySelectorAll('img');
      const optimizedImages = Array.from(images).filter(img => 
        img.loading || img.style.width || img.style.height
      );
      
      this.addTestResult({
        name: 'Image Optimization',
        passed: optimizedImages.length === images.length,
        details: `${optimizedImages.length}/${images.length} images optimized`,
        impact: 'Reduces CLS and improves LCP'
      });
    }
    
    testJavaScriptExecution() {
      const scripts = document.querySelectorAll('script');
      const hasAdvancedOptimizer = Array.from(scripts).some(script => 
        script.src.includes('advanced-optimizer.js')
      );
      
      this.addTestResult({
        name: 'JavaScript Optimization',
        passed: hasAdvancedOptimizer,
        details: hasAdvancedOptimizer ? '✅ Advanced optimizer loaded' : '❌ Advanced optimizer missing',
        impact: 'Improves FID and main thread performance'
      });
    }
    
    runPerformanceTests() {
      console.log('🚀 Running performance tests...');
      
      // Test DOM readiness
      this.testDOMReadiness();
      
      // Test rendering performance
      this.testRenderingPerformance();
      
      // Test memory usage
      this.testMemoryUsage();
      
      // Test network performance
      this.testNetworkPerformance();
    }
    
    testDOMReadiness() {
      const domContentLoaded = performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart;
      const isOptimal = domContentLoaded < 1000;
      
      this.addTestResult({
        name: 'DOM Readiness',
        passed: isOptimal,
        details: `DOM Content Loaded: ${domContentLoaded.toFixed(2)}ms`,
        impact: isOptimal ? 'Good DOM parsing performance' : 'Slow DOM parsing detected'
      });
    }
    
    testRenderingPerformance() {
      const renderTime = performance.timing.loadEventEnd - performance.timing.domContentLoadedEventEnd;
      const isOptimal = renderTime < 500;
      
      this.addTestResult({
        name: 'Rendering Performance',
        passed: isOptimal,
        details: `Render time: ${renderTime.toFixed(2)}ms`,
        impact: isOptimal ? 'Good rendering performance' : 'Slow rendering detected'
      });
    }
    
    testMemoryUsage() {
      if (performance.memory) {
        const memoryUsage = performance.memory.usedJSHeapSize / 1048576; // MB
        const isOptimal = memoryUsage < 50;
        
        this.addTestResult({
          name: 'Memory Usage',
          passed: isOptimal,
          details: `Memory usage: ${memoryUsage.toFixed(2)}MB`,
          impact: isOptimal ? 'Good memory efficiency' : 'High memory usage detected'
        });
      }
    }
    
    testNetworkPerformance() {
      const resources = performance.getEntriesByType('resource');
      const totalSize = resources.reduce((sum, resource) => sum + (resource.transferSize || 0), 0);
      const totalSizeKB = totalSize / 1024;
      const isOptimal = totalSizeKB < 500;
      
      this.addTestResult({
        name: 'Network Performance',
        passed: isOptimal,
        details: `Total transfer size: ${totalSizeKB.toFixed(2)}KB`,
        impact: isOptimal ? 'Good network efficiency' : 'Large payload detected'
      });
    }
    
    addTestResult(result) {
      this.testResults.push(result);
      console.log(`${result.passed ? '✅' : '❌'} ${result.name}: ${result.details}`);
    }
    
    evaluateMetrics() {
      const evaluation = {};
      
      Object.keys(this.metrics).forEach(metric => {
        const value = this.metrics[metric];
        const threshold = this.thresholds[metric];
        
        if (threshold) {
          if (value <= threshold.good) {
            evaluation[metric] = 'good';
          } else if (value <= threshold.needsImprovement) {
            evaluation[metric] = 'needs-improvement';
          } else {
            evaluation[metric] = 'poor';
          }
        } else {
          evaluation[metric] = 'measured';
        }
      });
      
      return evaluation;
    }
    
    generateReport() {
      // Wait for all metrics to be collected
      setTimeout(() => {
        console.log('\n📊 CORE WEB VITALS REPORT');
        console.log('================================');
        
        const evaluation = this.evaluateMetrics();
        
        console.log('\n🎯 Metrics:');
        Object.keys(this.metrics).forEach(metric => {
          const value = this.metrics[metric];
          const status = evaluation[metric];
          const emoji = status === 'good' ? '🟢' : status === 'needs-improvement' ? '🟡' : '🔴';
          console.log(`${emoji} ${metric.toUpperCase()}: ${value.toFixed(2)}${metric === 'cls' ? '' : 'ms'} (${status})`);
        });
        
        console.log('\n🧪 Test Results:');
        this.testResults.forEach(test => {
          const emoji = test.passed ? '✅' : '❌';
          console.log(`${emoji} ${test.name}: ${test.details}`);
        });
        
        console.log('\n📈 Summary:');
        const passedTests = this.testResults.filter(t => t.passed).length;
        const totalTests = this.testResults.length;
        console.log(`Tests passed: ${passedTests}/${totalTests} (${((passedTests/totalTests)*100).toFixed(1)}%)`);
        
        const goodMetrics = Object.values(evaluation).filter(s => s === 'good').length;
        const totalMetrics = Object.keys(evaluation).length;
        console.log(`Good metrics: ${goodMetrics}/${totalMetrics} (${((goodMetrics/totalMetrics)*100).toFixed(1)}%)`);
        
        // Overall assessment
        const overallScore = ((passedTests/totalTests) * 0.5 + (goodMetrics/totalMetrics) * 0.5) * 100;
        console.log(`\n🏆 Overall Performance Score: ${overallScore.toFixed(1)}%`);
        
        if (overallScore >= 90) {
          console.log('🎉 EXCELLENT: Phase 5 optimizations successful!');
        } else if (overallScore >= 75) {
          console.log('👍 GOOD: Phase 5 optimizations mostly successful');
        } else if (overallScore >= 60) {
          console.log('⚠️ NEEDS IMPROVEMENT: Some optimizations need attention');
        } else {
          console.log('❌ POOR: Significant optimization issues detected');
        }
        
        console.log('\n💡 Recommendations:');
        this.generateRecommendations(evaluation);
        
        // Store results for later analysis
        this.storeResults();
        
      }, 3000); // Wait 3 seconds for all metrics
    }
    
    generateRecommendations(evaluation) {
      const recommendations = [];
      
      if (evaluation.lcp === 'poor') {
        recommendations.push('• Optimize largest contentful paint: reduce image sizes, improve server response time');
      }
      
      if (evaluation.fid === 'poor') {
        recommendations.push('• Reduce first input delay: minimize JavaScript execution time, use code splitting');
      }
      
      if (evaluation.cls === 'poor') {
        recommendations.push('• Fix cumulative layout shift: specify image dimensions, avoid dynamic content insertion');
      }
      
      if (evaluation.ttfb === 'poor') {
        recommendations.push('• Improve time to first byte: optimize server response, use CDN');
      }
      
      if (recommendations.length === 0) {
        recommendations.push('• All Core Web Vitals are within good thresholds!');
      }
      
      recommendations.forEach(rec => console.log(rec));
    }
    
    storeResults() {
      const results = {
        timestamp: new Date().toISOString(),
        url: window.location.href,
        metrics: this.metrics,
        evaluation: this.evaluateMetrics(),
        testResults: this.testResults,
        userAgent: navigator.userAgent,
        viewport: {
          width: window.innerWidth,
          height: window.innerHeight
        }
      };
      
      // Store in localStorage for analysis
      localStorage.setItem('core-web-vitals-results', JSON.stringify(results));
      
      // Send to console for easy copying
      console.log('\n📋 Results stored in localStorage under key: core-web-vitals-results');
    }
    
    // Public API
    getResults() {
      return {
        metrics: this.metrics,
        evaluation: this.evaluateMetrics(),
        testResults: this.testResults
      };
    }
    
    runManualTest() {
      console.log('🔧 Running manual performance test...');
      this.runPerformanceTests();
      setTimeout(() => this.generateReport(), 1000);
    }
  }
  
  // Initialize tester
  window.CoreWebVitalsTester = CoreWebVitalsTester;
  window.coreWebVitalsTester = new CoreWebVitalsTester();
  
  // Expose manual testing
  window.runPerformanceTest = () => {
    window.coreWebVitalsTester.runManualTest();
  };
  
  console.log('🧪 Core Web Vitals Tester ready. Run window.runPerformanceTest() for manual testing.');
})();
