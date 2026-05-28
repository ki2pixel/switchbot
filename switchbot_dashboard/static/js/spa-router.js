/**
 * SwitchBot Dashboard v2 - SPA Light Router
 * Implements lightweight asynchronous dynamic page transitions (AJAX-SPA).
 * Intercepts navigation, updates main #app-content container, manages browser
 * history, and executes page-specific scripts safely.
 */
'use strict';

class SPARouter {
  constructor() {
    this.isTransitioning = false;
    this.globalScripts = [
      'loaders.js',
      'alerts.js',
      'bottom-nav.js',
      'performance-optimizer.js',
      'advanced-optimizer.js',
      'spa-router.js'
    ];
    this.init();
  }

  init() {
    // Intercept back/forward browser navigation
    window.addEventListener('popstate', () => {
      this.navigate(window.location.href, null, false);
    });
    console.log('🚀 SPA Light Router initialized');
  }

  /**
   * Navigate to a new page dynamically
   * @param {string} url Destination URL
   * @param {HTMLElement|null} linkElement Anchor element that triggered navigation
   * @param {boolean} pushState Whether to push state to history
   */
  async navigate(url, linkElement = null, pushState = true) {
    if (this.isTransitioning) return;
    
    // Safety check to ensure it's a local page in same origin
    const targetUrl = new URL(url, window.location.origin);
    if (targetUrl.origin !== window.location.origin) {
      window.location.href = url;
      return;
    }

    this.isTransitioning = true;
    
    // 1. Show global loader overlay (from loaders.js)
    if (window.SwitchBotLoaders) {
      window.SwitchBotLoaders.showGlobal();
      if (linkElement) {
        window.SwitchBotLoaders.show(linkElement);
      }
    }

    try {
      // 2. Fetch page HTML
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: Failed to fetch page`);
      }
      
      const htmlText = await response.text();
      
      // 3. Parse fetched HTML
      const parser = new DOMParser();
      const newDoc = parser.parseFromString(htmlText, 'text/html');
      
      const newContent = newDoc.getElementById('app-content');
      const currentContent = document.getElementById('app-content');
      
      if (!newContent || !currentContent) {
        // Fallback to standard page load if elements are missing
        window.location.href = url;
        return;
      }
      
      // 4. Perform visual fade-out before replacing content
      currentContent.style.opacity = '0';
      currentContent.style.transition = 'opacity 0.15s ease-in-out';
      
      await new Promise(resolve => setTimeout(resolve, 150));
      
      // Clean up previous page specific components
      if (window.historyDashboard && typeof window.historyDashboard.destroy === 'function') {
        try {
          window.historyDashboard.destroy();
          window.historyDashboard = null;
        } catch (e) {
          console.error('[SPARouter] Error cleaning up history dashboard:', e);
        }
      }
      
      // 5. Replace page content and update title
      currentContent.innerHTML = newContent.innerHTML;
      document.title = newDoc.title;
      
      if (pushState) {
        history.pushState(null, '', url);
      }
      
      // 6. Update active states in bottom navigation bar
      this.updateActiveNavState(url);
      
      // 7. Fade-in new content
      currentContent.style.opacity = '1';
      
      // 8. Execute page-specific scripts
      this.executePageScripts(newDoc);
      
    } catch (error) {
      console.error('[SPARouter] Navigation error:', error);
      // Fallback on failure
      window.location.href = url;
    } finally {
      // 9. Hide global loaders
      if (window.SwitchBotLoaders) {
        window.SwitchBotLoaders.hideGlobal();
        if (linkElement) {
          window.SwitchBotLoaders.hide(linkElement);
        }
      }
      this.isTransitioning = false;
    }
  }

  /**
   * Update active nav link states in bottom navigation bar
   * @param {string} targetUrl 
   */
  updateActiveNavState(targetUrl) {
    const footer = document.getElementById('footer-bar');
    if (!footer) return;
    
    const links = footer.querySelectorAll('a[data-loader]');
    const parsedTarget = new URL(targetUrl, window.location.origin);
    
    links.forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      
      const linkUrl = new URL(href, window.location.origin);
      const isActive = linkUrl.pathname === parsedTarget.pathname;
      
      if (isActive) {
        link.classList.add('active-nav');
        link.setAttribute('aria-current', 'page');
      } else {
        link.classList.remove('active-nav');
        link.removeAttribute('aria-current');
      }
    });
  }

  /**
   * Execute scripts of the newly loaded page
   * @param {Document} newDoc Parsed HTML Document
   */
  executePageScripts(newDoc) {
    const scripts = Array.from(newDoc.querySelectorAll('script'));
    
    scripts.forEach(script => {
      const src = script.getAttribute('src');
      
      if (src) {
        // Skip global scripts that are already running on the window level
        const isGlobal = this.globalScripts.some(globalScript => src.endsWith(globalScript));
        if (isGlobal) {
          return;
        }
        
        // Re-execute page-specific script (e.g. settings.js, history.js)
        this.loadScriptDynamic(src);
      } else {
        // Execute inline script
        this.executeInlineScript(script.textContent);
      }
    });
  }

  /**
   * Dynamically loads and runs a JS script file
   * @param {string} src Script source URL
   */
  loadScriptDynamic(src) {
    // Remove existing script element with same src to avoid cluttering DOM
    const existing = document.querySelector(`script[src="${src}"]`);
    if (existing) {
      existing.remove();
    }
    
    const newScript = document.createElement('script');
    newScript.src = src;
    newScript.async = false; // Maintain execution order
    document.body.appendChild(newScript);
  }

  /**
   * Dynamically runs inline script content
   * @param {string} code JS code
   */
  executeInlineScript(code) {
    const newScript = document.createElement('script');
    newScript.textContent = code;
    document.body.appendChild(newScript);
    // Remove inline scripts immediately after execution to keep DOM clean
    newScript.remove();
  }
}

// Instantiate router globally
document.addEventListener('DOMContentLoaded', () => {
  window.SwitchBotRouter = new SPARouter();
});
