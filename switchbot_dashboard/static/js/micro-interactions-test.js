/**
 * Micro-interactions Test Script
 * Tests the CSS animations and micro-interactions
 * Used for validation during development
 */

class MicroInteractionsTest {
  constructor() {
    this.testResults = [];
    this.animationClasses = [
      'sb-pulse',
      'sb-success-flash',
      'sb-temp-change',
      'sb-data-update',
      'sb-loading',
      'sb-cooldown'
    ];
  }

  // Test if animations are properly disabled with prefers-reduced-motion
  testReducedMotion() {
    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    const testElement = document.createElement('div');
    testElement.className = 'sb-pulse';
    document.body.appendChild(testElement);

    const computedStyle = window.getComputedStyle(testElement);
    const animationDuration = computedStyle.animationDuration;
    
    const isReduced = motionQuery.matches;
    const isDisabled = animationDuration === '0.01s' || animationDuration === '0.01ms';
    
    this.testResults.push({
      test: 'prefers-reduced-motion',
      passed: isReduced ? isDisabled : true,
      details: `Motion preference: ${isReduced}, Animation duration: ${animationDuration}`
    });

    document.body.removeChild(testElement);
    return isReduced ? isDisabled : true;
  }

  // Test GPU acceleration
  testGPUAcceleration() {
    const testElement = document.createElement('div');
    testElement.className = 'sb-gpu-accelerated';
    document.body.appendChild(testElement);

    const computedStyle = window.getComputedStyle(testElement);
    const transform = computedStyle.transform;
    const willChange = computedStyle.willChange;
    
    const hasGPUAcceleration = transform !== 'none' || willChange.includes('transform');
    
    this.testResults.push({
      test: 'gpu-acceleration',
      passed: hasGPUAcceleration,
      details: `Transform: ${transform}, Will-change: ${willChange}`
    });

    document.body.removeChild(testElement);
    return hasGPUAcceleration;
  }

  // Test if CSS variables are properly defined
  testCSSVariables() {
    const testElement = document.createElement('div');
    document.body.appendChild(testElement);

    const computedStyle = window.getComputedStyle(testElement);
    const requiredVariables = [
      '--sb-scale-hover',
      '--sb-scale-active',
      '--sb-translate-hover',
      '--sb-transition-fast',
      '--sb-transition-normal'
    ];

    const missingVars = requiredVariables.filter(varName => {
      const value = computedStyle.getPropertyValue(varName);
      return !value || value.trim() === '';
    });

    this.testResults.push({
      test: 'css-variables',
      passed: missingVars.length === 0,
      details: `Missing variables: ${missingVars.join(', ')}`
    });

    document.body.removeChild(testElement);
    return missingVars.length === 0;
  }

  // Test animation performance
  testAnimationPerformance() {
    const testElement = document.createElement('div');
    testElement.className = 'sb-pulse sb-gpu-accelerated';
    testElement.style.position = 'absolute';
    testElement.style.left = '-9999px';
    document.body.appendChild(testElement);

    const startTime = performance.now();
    
    // Trigger animation
    testElement.classList.add('sb-pulse');
    
    // Measure after animation should start
    setTimeout(() => {
      const endTime = performance.now();
      const duration = endTime - startTime;
      
      this.testResults.push({
        test: 'animation-performance',
        passed: duration < 50, // Should start within 50ms
        details: `Animation start time: ${duration.toFixed(2)}ms`
      });

      document.body.removeChild(testElement);
    }, 10);

    return true;
  }

  // Test focus accessibility
  testFocusAccessibility() {
    const testElement = document.createElement('button');
    testElement.className = 'sb-focus-enhanced';
    testElement.textContent = 'Test Button';
    document.body.appendChild(testElement);

    testElement.focus();
    const computedStyle = window.getComputedStyle(testElement);
    const outline = computedStyle.outline;
    const outlineOffset = computedStyle.outlineOffset;
    
    const hasFocusStyle = outline !== 'none' && outlineOffset !== '0px';
    
    this.testResults.push({
      test: 'focus-accessibility',
      passed: hasFocusStyle,
      details: `Outline: ${outline}, Outline-offset: ${outlineOffset}`
    });

    document.body.removeChild(testElement);
    return hasFocusStyle;
  }

  // Run all tests
  runAllTests() {
    console.log('🧪 Running Micro-interactions Tests...');
    
    this.testReducedMotion();
    this.testGPUAcceleration();
    this.testCSSVariables();
    this.testAnimationPerformance();
    this.testFocusAccessibility();

    const passedTests = this.testResults.filter(result => result.passed).length;
    const totalTests = this.testResults.length;

    console.log(`📊 Test Results: ${passedTests}/${totalTests} tests passed`);
    
    this.testResults.forEach(result => {
      const icon = result.passed ? '✅' : '❌';
      console.log(`${icon} ${result.test}: ${result.details}`);
    });

    return {
      passed: passedTests,
      total: totalTests,
      success: passedTests === totalTests,
      results: this.testResults
    };
  }
}

// Auto-run tests if in development mode
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
  document.addEventListener('DOMContentLoaded', () => {
    const tester = new MicroInteractionsTest();
    setTimeout(() => tester.runAllTests(), 1000);
  });
}

// Export for manual testing
window.MicroInteractionsTest = MicroInteractionsTest;
