/**
 * SwitchBot Dashboard v2 - SPA Light Router
 * Implements lightweight asynchronous dynamic page transitions (AJAX-SPA).
 * Intercepts navigation, updates main #app-content container, manages browser
 * history, and executes page-specific scripts safely.
 *
 * Security: loadScriptDynamic validates same-origin before injection.
 * A11y: Focus is moved to #app-content after transition, route change is
 *       announced via an aria-live region for screen readers.
 */
'use strict';

class SPARouter {
  constructor() {
    this.isTransitioning = false;
    // Global scripts that must never be re-executed during SPA transitions.
    // Checked against the URL pathname (query strings are stripped).
    this.globalScripts = [
      'loaders.js',
      'alerts.js',
      'spa-router.js'
    ];
    this.init();
  }

  init() {
    // Intercept back/forward browser navigation
    globalThis.addEventListener('popstate', () => {
      this.navigate(globalThis.location.href, null, false);
    });
  }

  /**
   * Normalize an href to its pathname, stripping query strings and fragments.
   * @param {string} href Raw href attribute value
   * @returns {string} Resolved pathname (e.g. "/static/css/theme.css")
   */
  static normalizeHref(href) {
    try {
      return new URL(href, globalThis.location.origin).pathname;
    } catch {
      return '';
    }
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
    const targetUrl = new URL(url, globalThis.location.origin);
    if (targetUrl.origin !== globalThis.location.origin) {
      globalThis.location.href = url;
      return;
    }

    this.isTransitioning = true;
    
    // 1. Show global loader overlay (from loaders.js)
    if (globalThis.SwitchBotLoaders) {
      globalThis.SwitchBotLoaders.showGlobal();
      if (linkElement) {
        globalThis.SwitchBotLoaders.show(linkElement);
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
        globalThis.location.href = url;
        return;
      }

      // ── CSS Synchronization (P1.1 fix) ──
      // Build a Set of all CSS pathnames already present in the document
      // to avoid injecting duplicates of global stylesheets.
      const existingCSS = new Set(
        Array.from(document.querySelectorAll('link[rel="stylesheet"]'))
          .map(link => SPARouter.normalizeHref(link.getAttribute('href') || ''))
          .filter(Boolean)
      );

      // Collect CSS stylesheets from the target page
      const newStyleLinks = Array.from(
        newDoc.querySelectorAll('link[rel="stylesheet"], link[rel="preload"][as="style"]')
      );
      const newCSSPaths = new Set(
        newStyleLinks
          .map(link => SPARouter.normalizeHref(link.getAttribute('href') || ''))
          .filter(Boolean)
      );

      const pageSpecificCSSPattern = /\/static\/css\/(index|settings|actions|history|devices)\.css$/;

      // Inject only stylesheets that are not already in the document
      const loadPromises = [];
      newStyleLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (!href) return;
        const normalized = SPARouter.normalizeHref(href);
        if (!normalized || existingCSS.has(normalized)) return; // Skip duplicates

        const newLink = document.createElement('link');
        newLink.rel = 'stylesheet';
        newLink.href = href;
        
        const loadPromise = new Promise(resolve => {
          newLink.onload = resolve;
          newLink.onerror = resolve; // avoid blocking
          setTimeout(resolve, 3000); // failsafe
        });
        loadPromises.push(loadPromise);
        document.head.appendChild(newLink);
        existingCSS.add(normalized);
      });

      // Remove orphaned preload links that are no longer needed
      document.querySelectorAll('link[rel="preload"][as="style"]').forEach(pl => {
        const plPath = SPARouter.normalizeHref(pl.getAttribute('href') || '');
        if (plPath && !newCSSPaths.has(plPath)) {
          pl.remove();
        }
      });
      
      // 4. Perform visual fade-out before replacing content
      currentContent.style.opacity = '0';
      currentContent.style.transition = 'opacity 0.15s ease-in-out';
      
      // Wait for both the fade-out and the new stylesheets to finish loading
      await Promise.all([
        new Promise(resolve => setTimeout(resolve, 150)),
        ...loadPromises
      ]);
      
      // Clean up previous page specific components
      if (globalThis.historyDashboard && typeof globalThis.historyDashboard.destroy === 'function') {
        try {
          globalThis.historyDashboard.destroy();
          globalThis.historyDashboard = null;
        } catch (e) {
          console.error('[SPARouter] Error cleaning up history dashboard:', e);
        }
      }
      
      // 5. Replace page content and update title
      // Note: innerHTML from DOMParser on a same-origin fetch is acceptable here.
      // The content is server-generated HTML from our own Flask templates.
      currentContent.innerHTML = newContent.innerHTML;
      document.title = newDoc.title;

      // ── Double footer cleanup (P1.1 fix) ──
      // _footer_nav.html is {% include %}'d in every template, so the fetched
      // HTML may contain a #footer-bar inside #app-content. The canonical footer
      // lives outside #app-content, so remove any duplicate that appeared inside.
      const duplicateFooter = currentContent.querySelector('#footer-bar');
      if (duplicateFooter) {
        duplicateFooter.remove();
      }

      // Remove page-specific stylesheets from the old page that are not in the new page
      Array.from(document.querySelectorAll('link[rel="stylesheet"]')).forEach(curLink => {
        const href = curLink.getAttribute('href');
        if (!href) return;
        const resolvedUrl = SPARouter.normalizeHref(href);
        
        if (pageSpecificCSSPattern.test(resolvedUrl) && !newCSSPaths.has(resolvedUrl)) {
          curLink.remove();
        }
      });
      
      if (pushState) {
        history.pushState(null, '', url);
      }
      
      // 6. Update active states in bottom navigation bar
      this.updateActiveNavState(url);
      
      // 7. Fade-in new content
      currentContent.style.opacity = '1';

      // ── Focus management for accessibility (P2.26 fix) ──
      // Move focus to the main content container so keyboard and screen-reader
      // users are aware of the page change.
      currentContent.setAttribute('tabindex', '-1');
      currentContent.focus({ preventScroll: true });

      // Announce route change via aria-live region
      this.announceRouteChange(document.title);
      
      // 8. Execute page-specific scripts
      this.executePageScripts(newDoc);
      
    } catch (error) {
      console.error('[SPARouter] Navigation error:', error);
      // Fallback on failure
      globalThis.location.href = url;
    } finally {
      // 9. Hide global loaders
      if (globalThis.SwitchBotLoaders) {
        globalThis.SwitchBotLoaders.hideGlobal();
        if (linkElement) {
          globalThis.SwitchBotLoaders.hide(linkElement);
        }
      }
      this.isTransitioning = false;
    }
  }

  /**
   * Announce a route change to assistive technology via an aria-live region.
   * @param {string} pageTitle The new page title
   */
  announceRouteChange(pageTitle) {
    let announcer = document.getElementById('spa-route-announcer');
    if (!announcer) {
      announcer = document.createElement('div');
      announcer.id = 'spa-route-announcer';
      announcer.setAttribute('aria-live', 'assertive');
      announcer.setAttribute('aria-atomic', 'true');
      announcer.className = 'sr-only';
      document.body.appendChild(announcer);
    }
    announcer.textContent = `Page chargée : ${pageTitle}`;
  }

  /**
   * Update active nav link states in bottom navigation bar
   * @param {string} targetUrl 
   */
  updateActiveNavState(targetUrl) {
    const footer = document.getElementById('footer-bar');
    if (!footer) return;
    
    const links = footer.querySelectorAll('a[data-loader]');
    const parsedTarget = new URL(targetUrl, globalThis.location.origin);
    
    links.forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      
      const linkUrl = new URL(href, globalThis.location.origin);
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
   * Execute scripts of the newly loaded page.
   * Global scripts are identified by matching the URL pathname (ignoring
   * query strings like ?v=123) against the globalScripts list.
   * @param {Document} newDoc Parsed HTML Document
   */
  executePageScripts(newDoc) {
    const scripts = Array.from(newDoc.querySelectorAll('script'));
    
    scripts.forEach(script => {
      const src = script.getAttribute('src');
      
      if (src) {
        // Strip query strings before checking against globalScripts (P1.1 fix)
        const srcPath = SPARouter.normalizeHref(src);
        const isGlobal = this.globalScripts.some(globalScript => srcPath.endsWith(globalScript));
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
   * Dynamically loads and runs a JS script file.
   * Validates same-origin before injection to prevent cross-origin script loading.
   * Uses a safe DOM traversal instead of querySelector with string interpolation
   * to avoid CSS selector injection.
   * @param {string} src Script source URL
   */
  loadScriptDynamic(src) {
    // Validate same-origin (P2.43 security fix)
    try {
      const url = new URL(src, globalThis.location.origin);
      if (url.origin !== globalThis.location.origin) {
        console.warn('[SPARouter] Blocked cross-origin script:', src);
        return;
      }
    } catch {
      console.warn('[SPARouter] Invalid script URL:', src);
      return;
    }

    // Remove existing script with same src using safe comparison
    // instead of querySelector with string interpolation (CSS selector injection)
    document.querySelectorAll('script[src]').forEach(s => {
      if (s.getAttribute('src') === src) {
        s.remove();
      }
    });
    
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
  globalThis.SwitchBotRouter = new SPARouter();
});
