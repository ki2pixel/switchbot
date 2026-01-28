This file is a merged representation of a subset of the codebase, containing specifically included files and files not matching ignore patterns, combined into a single document by Repomix.
The content has been processed where line numbers have been added.

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.
- Pay special attention to the Repository Description. These contain important context and guidelines specific to this project.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: config/**, switchbot_dashboard/**, app.py, Dockerfile, gunicorn.conf.py, requirements.txt, .env.example
- Files matching these patterns are excluded: .git/**, .github/**, memory-bank/**, .windsurf/**, node_modules/**, venv*/**, .venv/**, __pycache__/**, *.pyc, *.pyo, *.log, *.sqlite3, .pytest_cache/**, coverage/**, repomix-output.*, docs/repomix.md, switchbot_dashboard/static/vendor/**
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Line numbers have been added to the beginning of each line
- Long base64 data strings (e.g., data:image/png;base64,...) have been truncated to reduce token count
- Files are sorted by Git change count (files with more changes are at the bottom)

# User Provided Header
Switchbot

# Directory Structure
```
config/
  settings.json
switchbot_dashboard/
  static/
    css/
      actions.css
      critical.css
      devices.css
      history.css
      index.css
      settings.css
      sticky-cards.css
      sticky-footer.css
      theme.css
    js/
      advanced-optimizer.js
      alerts.js
      bottom-nav.js
      devices.js
      history.js
      loaders.js
      performance-optimizer.js
      settings.js
  templates/
    _footer_nav.html
    actions.html
    devices.html
    history.html
    index.html
    quota.html
    settings.html
  __init__.py
  aircon.py
  automation.py
  config_store.py
  history_service.py
  ifttt.py
  postgres_store.py
  quota.py
  routes.py
  scheduler.py
  switchbot_api.py
.env.example
app.py
Dockerfile
gunicorn.conf.py
requirements.txt
```

# Files

## File: switchbot_dashboard/static/css/critical.css
```css
  1: /* Critical CSS - Above the Fold Content */
  2: /* Optimized for LCP - Inline in <head> */
  3: 
  4: /* Critical Reset & Base */
  5: *,
  6: *::before,
  7: *::after {
  8:   box-sizing: border-box;
  9: }
 10: 
 11: html {
 12:   line-height: 1.15;
 13:   -webkit-text-size-adjust: 100%;
 14: }
 15: 
 16: body {
 17:   margin: 0;
 18:   font-family: "Space Grotesk", "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
 19:   font-size: 1rem;
 20:   font-weight: 400;
 21:   line-height: 1.5;
 22:   color: var(--sb-text);
 23:   background-color: var(--sb-bg);
 24:   min-height: 100vh;
 25: }
 26: 
 27: /* Critical Theme Variables */
 28: :root {
 29:   color-scheme: dark;
 30:   --sb-bg: #030712;
 31:   --sb-gradient-start: #030712;
 32:   --sb-gradient-mid: #0a1227;
 33:   --sb-gradient-end: #101c35;
 34:   --sb-card: rgba(9, 14, 30, 0.92);
 35:   --sb-card-border: rgba(138, 180, 255, 0.2);
 36:   --sb-text: #f4f7ff;
 37:   --sb-muted: #aeb8d3;
 38:   --sb-accent: #8ab4ff;
 39:   --sb-accent-contrast: #051434;
 40:   --sb-shadow: 0 25px 60px rgba(2, 7, 20, 0.55);
 41:   --sb-outline: rgba(255, 255, 255, 0.08);
 42: }
 43: 
 44: /* Critical Layout */
 45: .container {
 46:   width: 100%;
 47:   padding-right: 1rem;
 48:   padding-left: 1rem;
 49:   margin-right: auto;
 50:   margin-left: auto;
 51:   max-width: 1200px;
 52: }
 53: 
 54: .py-4 {
 55:   padding-top: 1.5rem;
 56:   padding-bottom: 1.5rem;
 57: }
 58: 
 59: .mb-4 {
 60:   margin-bottom: 1.5rem;
 61: }
 62: 
 63: .mb-3 {
 64:   margin-bottom: 1rem;
 65: }
 66: 
 67: .mb-0 {
 68:   margin-bottom: 0 !important;
 69: }
 70: 
 71: /* Critical Typography */
 72: .h3 {
 73:   font-size: 1.75rem;
 74:   font-weight: 600;
 75:   line-height: 1.25;
 76:   margin-bottom: 0.5rem;
 77: }
 78: 
 79: .text-muted {
 80:   color: var(--sb-muted) !important;
 81: }
 82: 
 83: /* Critical Header */
 84: .page-header {
 85:   display: flex;
 86:   flex-direction: column;
 87:   gap: 1rem;
 88:   margin-bottom: 1.5rem;
 89: }
 90: 
 91: @media (min-width: 768px) {
 92:   .page-header {
 93:     flex-direction: row;
 94:     justify-content: space-between;
 95:     align-items: flex-start;
 96:   }
 97: }
 98: 
 99: .page-header-main h1 {
100:   font-size: 1.75rem;
101:   font-weight: 600;
102:   line-height: 1.25;
103:   margin-bottom: 0;
104:   color: var(--sb-text);
105: }
106: 
107: .page-subtitle {
108:   color: var(--sb-muted);
109:   margin-bottom: 0;
110: }
111: 
112: /* Critical Navigation */
113: .page-header-actions {
114:   display: flex;
115:   flex-wrap: wrap;
116:   gap: 0.5rem;
117: }
118: 
119: .btn {
120:   display: inline-block;
121:   font-weight: 400;
122:   line-height: 1.5;
123:   text-align: center;
124:   text-decoration: none;
125:   vertical-align: middle;
126:   cursor: pointer;
127:   user-select: none;
128:   background-color: transparent;
129:   border: 1px solid transparent;
130:   padding: 0.5rem 1rem;
131:   font-size: 0.875rem;
132:   border-radius: 0.375rem;
133:   transition: all 0.15s ease-in-out;
134: }
135: 
136: .btn-primary {
137:   color: #fff;
138:   background-color: var(--sb-accent);
139:   border-color: var(--sb-accent);
140: }
141: 
142: .btn-outline-primary {
143:   color: var(--sb-accent);
144:   border-color: var(--sb-accent);
145: }
146: 
147: .btn-outline-info {
148:   color: var(--sb-info);
149:   border-color: var(--sb-info);
150: }
151: 
152: .btn-outline-secondary {
153:   color: #6c757d;
154:   border-color: #6c757d;
155: }
156: 
157: /* Critical Alert Banner */
158: .alert {
159:   position: relative;
160:   padding: 0.75rem 1.25rem;
161:   margin-bottom: 1rem;
162:   border: 1px solid transparent;
163:   border-radius: 0.375rem;
164: }
165: 
166: .alert-warning {
167:   color: var(--sb-alert-text);
168:   background-color: var(--sb-warning-bg);
169:   border-color: var(--sb-warning);
170: }
171: 
172: .quota-banner {
173:   display: flex;
174:   align-items: center;
175:   justify-content: space-between;
176:   flex-wrap: wrap;
177:   gap: 0.5rem;
178: }
179: 
180: .quota-banner__main {
181:   display: flex;
182:   flex-direction: column;
183:   gap: 0.25rem;
184: }
185: 
186: /* Critical Status Grid */
187: .status-grid {
188:   display: grid;
189:   grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
190:   gap: 1rem;
191:   margin-bottom: 1.5rem;
192: }
193: 
194: .status-item {
195:   background: var(--sb-card);
196:   border: 1px solid var(--sb-card-border);
197:   border-radius: 0.75rem;
198:   padding: 1.25rem;
199:   backdrop-filter: blur(20px);
200:   box-shadow: var(--sb-shadow);
201:   transition: transform 0.2s ease, box-shadow 0.2s ease;
202: }
203: 
204: .status-item:hover {
205:   transform: translateY(-2px);
206:   box-shadow: 0 30px 70px rgba(2, 7, 20, 0.65);
207: }
208: 
209: .status-item h6 {
210:   font-size: 0.875rem;
211:   font-weight: 500;
212:   color: var(--sb-muted);
213:   margin-bottom: 0.5rem;
214:   text-transform: uppercase;
215:   letter-spacing: 0.05em;
216: }
217: 
218: .status-item .h4 {
219:   font-size: 2rem;
220:   font-weight: 600;
221:   margin-bottom: 0;
222:   color: var(--sb-text);
223: }
224: 
225: /* Critical Scene Actions */
226: .scene-actions-wrapper {
227:   position: sticky;
228:   bottom: 1rem;
229:   background: var(--sb-card);
230:   border: 1px solid var(--sb-card-border);
231:   border-radius: 1.25rem;
232:   padding: 1rem;
233:   margin: 1rem -1rem -1rem;
234:   backdrop-filter: blur(20px);
235:   box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.4);
236:   z-index: 10;
237: }
238: 
239: .scene-actions {
240:   display: grid;
241:   grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
242:   gap: 0.75rem;
243: }
244: 
245: .scene-action {
246:   padding: 1rem;
247:   font-size: 1rem;
248:   font-weight: 500;
249:   border-radius: 0.75rem;
250:   text-align: center;
251:   transition: all 0.2s ease;
252:   min-height: 56px;
253:   display: flex;
254:   align-items: center;
255:   justify-content: center;
256: }
257: 
258: .btn-outline-success {
259:   color: var(--sb-success);
260:   border-color: var(--sb-success);
261: }
262: 
263: .btn-outline-danger {
264:   color: var(--sb-danger);
265:   border-color: var(--sb-danger);
266: }
267: 
268: /* Critical Bottom Navigation */
269: #footer-bar {
270:   position: fixed;
271:   bottom: 0;
272:   left: 0;
273:   right: 0;
274:   height: 60px;
275:   background: var(--sb-card);
276:   border-top: 1px solid var(--sb-bottom-nav-border);
277:   backdrop-filter: blur(20px);
278:   display: flex;
279:   justify-content: space-around;
280:   align-items: center;
281:   z-index: 102;
282:   box-shadow: var(--sb-bottom-nav-shadow);
283:   padding-bottom: env(safe-area-inset-bottom);
284: }
285: 
286: #footer-bar a {
287:   display: flex;
288:   flex-direction: column;
289:   align-items: center;
290:   justify-content: center;
291:   color: var(--sb-muted);
292:   text-decoration: none;
293:   font-size: 0.75rem;
294:   padding: 0.5rem;
295:   min-width: 44px;
296:   min-height: 44px;
297:   transition: color 0.2s ease;
298: }
299: 
300: #footer-bar a.active-nav {
301:   color: var(--sb-accent);
302: }
303: 
304: #footer-bar i {
305:   font-size: 1.25rem;
306:   margin-bottom: 0.25rem;
307: }
308: 
309: /* Critical Body Padding for Bottom Nav */
310: body {
311:   padding-bottom: 80px;
312:   padding-bottom: calc(80px + env(safe-area-inset-bottom));
313: }
314: 
315: /* Critical Font Loading */
316: @font-face {
317:   font-family: 'Space Grotesk';
318:   font-style: normal;
319:   font-weight: 400;
320:   font-display: swap;
321:   src: url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&display=swap');
322: }
323: 
324: /* Critical Accessibility */
325: [role="navigation"] {
326:   outline: none;
327: }
328: 
329: [aria-hidden="true"] {
330:   display: none;
331: }
332: 
333: /* Critical Loading States */
334: .skeleton {
335:   background: linear-gradient(90deg, var(--sb-card) 25%, var(--sb-card-border) 50%, var(--sb-card) 75%);
336:   background-size: 200% 100%;
337:   animation: skeleton-loading 1.5s infinite;
338: }
339: 
340: @keyframes skeleton-loading {
341:   0% { background-position: 200% 0; }
342:   100% { background-position: -200% 0; }
343: }
344: 
345: /* Critical GPU Optimization */
346: .sb-gpu-accelerated {
347:   transform: translateZ(0);
348:   backface-visibility: hidden;
349:   perspective: 1000px;
350: }
351: 
352: /* Critical Responsive */
353: @media (max-width: 768px) {
354:   .container {
355:     padding-right: 0.75rem;
356:     padding-left: 0.75rem;
357:   }
358:   
359:   .page-header-actions {
360:     width: 100%;
361:   }
362:   
363:   .scene-actions {
364:     grid-template-columns: 1fr;
365:   }
366:   
367:   #footer-bar {
368:     display: flex;
369:   }
370: }
371: 
372: @media (min-width: 769px) {
373:   #footer-bar {
374:     display: none;
375:   }
376:   
377:   body {
378:     padding-bottom: 0;
379:   }
380: }
381: 
382: /* Critical Reduced Motion */
383: @media (prefers-reduced-motion: reduce) {
384:   *,
385:   *::before,
386:   *::after {
387:     animation-duration: 0.01ms !important;
388:     animation-iteration-count: 1 !important;
389:     transition-duration: 0.01ms !important;
390:   }
391: }
```

## File: switchbot_dashboard/static/js/performance-optimizer.js
```javascript
  1: /**
  2:  * Performance Optimizations Module
  3:  * Implements lazy loading, code splitting, and performance monitoring
  4:  */
  5: (function() {
  6:   'use strict';
  7:   
  8:   class PerformanceOptimizer {
  9:     constructor() {
 10:       this.observers = new Map();
 11:       this.loadedAssets = new Set();
 12:       this.performanceMetrics = {
 13:         navigationStart: performance.timing.navigationStart,
 14:         domContentLoaded: performance.timing.domContentLoadedEventEnd,
 15:         loadComplete: performance.timing.loadEventEnd
 16:       };
 17:       
 18:       this.init();
 19:     }
 20:     
 21:     init() {
 22:       this.setupLazyLoading();
 23:       this.setupCodeSplitting();
 24:       this.setupPerformanceMonitoring();
 25:       this.optimizeImages();
 26:       this.setupResourceHints();
 27:     }
 28:     
 29:     setupLazyLoading() {
 30:       // Lazy load images and iframes
 31:       if ('IntersectionObserver' in window) {
 32:         const imageObserver = new IntersectionObserver((entries) => {
 33:           entries.forEach(entry => {
 34:             if (entry.isIntersecting) {
 35:               this.loadImage(entry.target);
 36:               imageObserver.unobserve(entry.target);
 37:             }
 38:           });
 39:         }, {
 40:           rootMargin: '50px 0px',
 41:           threshold: 0.01
 42:         });
 43:         
 44:         // Observe all images with data-src
 45:         document.querySelectorAll('img[data-src]').forEach(img => {
 46:           imageObserver.observe(img);
 47:         });
 48:         
 49:         this.observers.set('images', imageObserver);
 50:       }
 51:     }
 52:     
 53:     loadImage(img) {
 54:       const src = img.dataset.src;
 55:       if (src && !this.loadedAssets.has(src)) {
 56:         img.src = src;
 57:         img.classList.remove('lazy-load');
 58:         img.classList.add('loaded');
 59:         this.loadedAssets.add(src);
 60:         
 61:         // Add fade-in effect
 62:         img.style.opacity = '0';
 63:         img.style.transition = 'opacity 0.3s ease';
 64:         setTimeout(() => {
 65:           img.style.opacity = '1';
 66:         }, 10);
 67:       }
 68:     }
 69:     
 70:     setupCodeSplitting() {
 71:       // Dynamic import for non-critical JavaScript modules
 72:       this.loadModuleWhenNeeded = async (moduleName, element) => {
 73:         try {
 74:           const module = await import(`/static/js/modules/${moduleName}.js`);
 75:           if (module.default) {
 76:             module.default(element);
 77:           }
 78:         } catch (error) {
 79:           console.warn(`Failed to load module ${moduleName}:`, error);
 80:         }
 81:       };
 82:       
 83:       // Load history chart module only when history page is visited
 84:       if (window.location.pathname.includes('/history')) {
 85:         this.loadModuleWhenNeeded('history-chart');
 86:       }
 87:       
 88:       // Load device management module only on devices page
 89:       if (window.location.pathname.includes('/devices')) {
 90:         this.loadModuleWhenNeeded('device-manager');
 91:       }
 92:     }
 93:     
 94:     setupPerformanceMonitoring() {
 95:       // Monitor Core Web Vitals
 96:       this.measureCoreWebVitals();
 97:       
 98:       // Monitor memory usage
 99:       if (performance.memory) {
100:         setInterval(() => {
101:           const memoryUsage = {
102:             used: Math.round(performance.memory.usedJSHeapSize / 1048576),
103:             total: Math.round(performance.memory.totalJSHeapSize / 1048576),
104:             limit: Math.round(performance.memory.jsHeapSizeLimit / 1048576)
105:           };
106:           
107:           // Log memory warnings
108:           if (memoryUsage.used / memoryUsage.limit > 0.8) {
109:             console.warn('High memory usage detected:', memoryUsage);
110:           }
111:         }, 30000); // Check every 30 seconds
112:       }
113:       
114:       // Monitor FPS
115:       this.monitorFPS();
116:     }
117:     
118:     measureCoreWebVitals() {
119:       // Largest Contentful Paint (LCP)
120:       if ('PerformanceObserver' in window) {
121:         const lcpObserver = new PerformanceObserver((list) => {
122:           const entries = list.getEntries();
123:           const lastEntry = entries[entries.length - 1];
124:           console.log('LCP:', lastEntry.renderTime || lastEntry.loadTime);
125:         });
126:         lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
127:         
128:         // First Input Delay (FID)
129:         const fidObserver = new PerformanceObserver((list) => {
130:           const entries = list.getEntries();
131:           entries.forEach(entry => {
132:             console.log('FID:', entry.processingStart - entry.startTime);
133:           });
134:         });
135:         fidObserver.observe({ entryTypes: ['first-input'] });
136:         
137:         // Cumulative Layout Shift (CLS)
138:         let clsValue = 0;
139:         const clsObserver = new PerformanceObserver((list) => {
140:           list.getEntries().forEach(entry => {
141:             if (!entry.hadRecentInput) {
142:               clsValue += entry.value;
143:             }
144:           });
145:           console.log('CLS:', clsValue);
146:         });
147:         clsObserver.observe({ entryTypes: ['layout-shift'] });
148:       }
149:     }
150:     
151:     monitorFPS() {
152:       let lastTime = performance.now();
153:       let frameCount = 0;
154:       
155:       const measureFPS = () => {
156:         frameCount++;
157:         const currentTime = performance.now();
158:         
159:         if (currentTime >= lastTime + 1000) {
160:           const fps = Math.round((frameCount * 1000) / (currentTime - lastTime));
161:           
162:           // Log FPS warnings
163:           if (fps < 30) {
164:             console.warn('Low FPS detected:', fps);
165:           }
166:           
167:           frameCount = 0;
168:           lastTime = currentTime;
169:         }
170:         
171:         requestAnimationFrame(measureFPS);
172:       };
173:       
174:       requestAnimationFrame(measureFPS);
175:     }
176:     
177:     optimizeImages() {
178:       // Add loading="lazy" to all images that don't have it
179:       document.querySelectorAll('img:not([loading])').forEach(img => {
180:         img.loading = 'lazy';
181:       });
182:       
183:       // Optimize existing images
184:       document.querySelectorAll('img').forEach(img => {
185:         // Add error handling
186:         img.addEventListener('error', () => {
187:           img.src = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0i...';
188:         });
189:         
190:         // Add CSS for smooth loading
191:         img.style.transition = 'opacity 0.3s ease';
192:       });
193:     }
194:     
195:     setupResourceHints() {
196:       // Add prefetch for critical resources
197:       const criticalResources = [
198:         '/static/css/theme.css',
199:         '/static/js/loaders.js'
200:       ];
201:       
202:       criticalResources.forEach(resource => {
203:         const link = document.createElement('link');
204:         link.rel = 'prefetch';
205:         link.href = resource;
206:         document.head.appendChild(link);
207:       });
208:       
209:       // Add preconnect for external domains
210:       const externalDomains = [
211:         'https://cdn.jsdelivr.net'
212:       ];
213:       
214:       externalDomains.forEach(domain => {
215:         const link = document.createElement('link');
216:         link.rel = 'preconnect';
217:         link.href = domain;
218:         document.head.appendChild(link);
219:       });
220:     }
221:     
222:     // Public API for manual optimization
223:     optimizeElement(element) {
224:       // Add GPU acceleration for animations
225:       element.style.willChange = 'transform, opacity';
226:       element.style.transform = 'translateZ(0)';
227:       
228:       // Remove will-change after animation completes
229:       setTimeout(() => {
230:         element.style.willChange = 'auto';
231:       }, 1000);
232:     }
233:     
234:     // Cleanup method
235:     destroy() {
236:       this.observers.forEach(observer => observer.disconnect());
237:       this.observers.clear();
238:     }
239:   }
240:   
241:   // Initialize performance optimizer
242:   let performanceOptimizer;
243:   
244:   if (document.readyState === 'loading') {
245:     document.addEventListener('DOMContentLoaded', () => {
246:       performanceOptimizer = new PerformanceOptimizer();
247:     });
248:   } else {
249:     performanceOptimizer = new PerformanceOptimizer();
250:   }
251:   
252:   // Expose to global scope for manual usage
253:   window.PerformanceOptimizer = PerformanceOptimizer;
254:   window.performanceOptimizer = performanceOptimizer;
255: })();
```

## File: app.py
```python
 1: import os
 2: 
 3: from dotenv import load_dotenv
 4: 
 5: from switchbot_dashboard import create_app
 6: 
 7: 
 8: load_dotenv()
 9: 
10: app = create_app()
11: 
12: 
13: if __name__ == "__main__":
14:     host = os.environ.get("FLASK_HOST", "127.0.0.1")
15:     port = int(os.environ.get("FLASK_PORT", "5000"))
16:     debug = os.environ.get("FLASK_DEBUG", "0") == "1"
17: 
18:     app.run(host=host, port=port, debug=debug)
```

## File: gunicorn.conf.py
```python
 1: """Gunicorn configuration for SwitchBot Dashboard.
 2: 
 3: Uses a single worker to avoid APScheduler conflicts.
 4: For background job scheduling (APScheduler), multiple workers would
 5: create duplicate scheduled tasks running in parallel.
 6: """
 7: import os
 8: 
 9: 
10: # Single worker to prevent APScheduler conflicts
11: # Can be overridden via WEB_CONCURRENCY env var if scheduler is disabled
12: workers = int(os.environ.get("WEB_CONCURRENCY", "1"))
13: bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
14: timeout = 120
15: accesslog = "-"
16: errorlog = "-"
17: loglevel = os.environ.get("LOG_LEVEL", "info").lower()
18: 
19: # Worker class optimized for I/O bound operations (SwitchBot API calls)
20: worker_class = "sync"
21: threads = 2
```

## File: switchbot_dashboard/static/css/actions.css
```css
  1: .actions-section,
  2: .scenes-section,
  3: .status-info {
  4:   margin-bottom: 2rem;
  5: }
  6: 
  7: .action-btn,
  8: .scene-btn {
  9:   min-height: 80px;
 10:   display: flex;
 11:   align-items: center;
 12:   justify-content: center;
 13:   font-size: 1rem;
 14:   font-weight: 500;
 15:   border-radius: 0.75rem;
 16:   text-align: center;
 17:   transition: all 0.2s ease;
 18:   position: relative;
 19:   overflow: hidden;
 20: }
 21: 
 22: .action-btn:hover,
 23: .scene-btn:hover {
 24:   transform: translateY(-2px);
 25:   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
 26: }
 27: 
 28: .action-btn:active,
 29: .scene-btn:active {
 30:   transform: translateY(0);
 31: }
 32: 
 33: .scene-btn:disabled {
 34:   opacity: 0.6;
 35:   cursor: not-allowed;
 36: }
 37: 
 38: .scene-content {
 39:   display: flex;
 40:   align-items: center;
 41:   gap: 1rem;
 42:   width: 100%;
 43: }
 44: 
 45: .scene-icon {
 46:   width: 40px;
 47:   height: 40px;
 48:   display: flex;
 49:   align-items: center;
 50:   justify-content: center;
 51:   flex-shrink: 0;
 52: }
 53: 
 54: .scene-icon svg {
 55:   width: 100%;
 56:   height: 100%;
 57: }
 58: 
 59: .scene-info {
 60:   flex-grow: 1;
 61:   text-align: left;
 62: }
 63: 
 64: .scene-title {
 65:   font-weight: 600;
 66:   margin-bottom: 0.25rem;
 67: }
 68: 
 69: .scene-status {
 70:   font-size: 0.875rem;
 71: }
 72: 
 73: .status-item {
 74:   background: var(--sb-card);
 75:   border: 1px solid var(--sb-card-border);
 76:   border-radius: 0.5rem;
 77:   padding: 1rem;
 78:   text-align: center;
 79:   backdrop-filter: blur(20px);
 80: }
 81: 
 82: .status-label {
 83:   font-size: 0.875rem;
 84:   color: var(--sb-muted);
 85:   margin-bottom: 0.5rem;
 86:   text-transform: uppercase;
 87:   letter-spacing: 0.05em;
 88: }
 89: 
 90: .status-value {
 91:   font-size: 1.5rem;
 92:   font-weight: 600;
 93:   color: var(--sb-text);
 94: }
 95: 
 96: @media (max-width: 768px) {
 97:   .action-btn,
 98:   .scene-btn {
 99:     min-height: 70px;
100:     font-size: 0.9rem;
101:   }
102:   
103:   .scene-content {
104:     gap: 0.75rem;
105:   }
106:   
107:   .scene-icon {
108:     width: 35px;
109:     height: 35px;
110:   }
111:   
112:   .scene-title {
113:     font-size: 0.95rem;
114:   }
115:   
116:   .scene-status {
117:     font-size: 0.8rem;
118:   }
119: }
120: 
121: .scene-icon--winter {
122:   color: #6ee7b7;
123: }
124: 
125: .scene-icon--summer {
126:   color: #4bc9f0;
127: }
128: 
129: .scene-icon--fan {
130:   color: #f6c343;
131: }
132: 
133: .scene-icon--off {
134:   color: #ff6b81;
135: }
136: 
137: .action-btn,
138: .scene-btn,
139: .status-item {
140:   transform: translateZ(0);
141:   backface-visibility: hidden;
142:   perspective: 1000px;
143: }
144: 
145: @media (prefers-reduced-motion: reduce) {
146:   .action-btn,
147:   .scene-btn {
148:     transition: none;
149:   }
150:   
151:   .action-btn:hover,
152:   .scene-btn:hover {
153:     transform: none;
154:   }
155: }
```

## File: switchbot_dashboard/static/css/sticky-cards.css
```css
  1: .card-style {
  2:   overflow: hidden;
  3:   margin: 0px 16px 30px 16px;
  4:   border-radius: 15px;
  5:   border: none;
  6:   box-shadow: 0 4px 24px 0 rgba(0, 0, 0, 0.08);
  7:   background: var(--sb-card);
  8:   color: var(--sb-text);
  9: }
 10: 
 11: .card-style .card-body {
 12:   padding: 15px;
 13: }
 14: 
 15: .card-style .card-overlay {
 16:   border-radius: 15px;
 17: }
 18: 
 19: .content-box {
 20:   background-color: var(--sb-card);
 21:   border-radius: 15px;
 22:   margin-left: 15px;
 23:   margin-right: 15px;
 24:   box-shadow: 0 2px 14px 0 rgba(0, 0, 0, 0.08);
 25:   border: 1px solid var(--sb-card-border);
 26: }
 27: 
 28: .content {
 29:   margin: 20px 15px 20px 15px;
 30: }
 31: 
 32: .content p:last-child {
 33:   margin-bottom: 0px;
 34: }
 35: 
 36: .content-full {
 37:   margin: 0px;
 38: }
 39: 
 40: .content-boxed {
 41:   padding: 20px 15px 0px 15px;
 42: }
 43: 
 44: .rounded-0 {
 45:   border-radius: 0px !important;
 46: }
 47: 
 48: .rounded-xs {
 49:   border-radius: 5px !important;
 50: }
 51: 
 52: .rounded-s {
 53:   border-radius: 8px !important;
 54: }
 55: 
 56: .rounded-sm {
 57:   border-radius: 10px !important;
 58: }
 59: 
 60: .rounded-m {
 61:   border-radius: 15px !important;
 62: }
 63: 
 64: .rounded-l {
 65:   border-radius: 30px !important;
 66: }
 67: 
 68: .rounded-xl {
 69:   border-radius: 50px !important;
 70: }
 71: 
 72: .shadow-none {
 73:   box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0) !important;
 74: }
 75: 
 76: .shadow-0 {
 77:   box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0) !important;
 78: }
 79: 
 80: .shadow-xs {
 81:   box-shadow: 0px 0px 5px 2px rgba(0, 0, 0, 0.04) !important;
 82: }
 83: 
 84: .shadow-s {
 85:   box-shadow: 0 4px 10px 0 rgba(0, 0, 0, 0.1) !important;
 86: }
 87: 
 88: .shadow-m {
 89:   box-shadow: 0 2px 14px 0 rgba(0, 0, 0, 0.08) !important;
 90: }
 91: 
 92: .shadow-l {
 93:   box-shadow: 0 5px 15px 0 rgba(0, 0, 0, 0.09) !important;
 94: }
 95: 
 96: .shadow-xl {
 97:   box-shadow: 0 5px 30px 0 rgba(0, 0, 0, 0.11), 0 5px 15px 0 rgba(0, 0, 0, 0.08) !important;
 98: }
 99: 
100: /* Dark Mode Integration */
101: @media (prefers-color-scheme: dark) {
102:   .card-style {
103:     box-shadow: 0 4px 24px 0 rgba(0, 0, 0, 0.4);
104:   }
105:   
106:   .content-box {
107:     box-shadow: 0 2px 14px 0 rgba(0, 0, 0, 0.3);
108:   }
109:   
110:   .shadow-l {
111:     box-shadow: 0 5px 15px 0 rgba(0, 0, 0, 0.3) !important;
112:   }
113:   
114:   .shadow-xl {
115:     box-shadow: 0 5px 30px 0 rgba(0, 0, 0, 0.4), 0 5px 15px 0 rgba(0, 0, 0, 0.3) !important;
116:   }
117: }
```

## File: switchbot_dashboard/static/js/advanced-optimizer.js
```javascript
  1: /**
  2:  * Advanced Performance Optimizer - Core Web Vitals Enhancement
  3:  * Implements advanced optimizations for LCP, FID, and CLS
  4:  */
  5: (function() {
  6:   'use strict';
  7:   
  8:   class AdvancedPerformanceOptimizer {
  9:     constructor() {
 10:       this.criticalResources = new Set();
 11:       this.loadedResources = new Map();
 12:       this.layoutShiftElements = new Map();
 13:       this.fontLoadPromise = null;
 14:       this.metrics = {
 15:         lcp: 0,
 16:         fid: 0,
 17:         cls: 0,
 18:         ttfb: 0,
 19:         fcp: 0
 20:       };
 21:       
 22:       this.init();
 23:     }
 24:     
 25:     init() {
 26:       this.setupResourceHints();
 27:       this.optimizeFontLoading();
 28:       this.setupAdvancedCLS();
 29:       this.setupAdvancedFID();
 30:       this.setupAdvancedLCP();
 31:       this.setupIntersectionOptimization();
 32:       this.setupMainThreadScheduling();
 33:       this.monitorAdvancedMetrics();
 34:     }
 35:     
 36:     setupResourceHints() {
 37:       // Preconnect for external domains
 38:       const preconnectDomains = [
 39:         'https://cdn.jsdelivr.net',
 40:         'https://fonts.googleapis.com',
 41:         'https://fonts.gstatic.com'
 42:       ];
 43:       
 44:       preconnectDomains.forEach(domain => {
 45:         const link = document.createElement('link');
 46:         link.rel = 'preconnect';
 47:         link.href = domain;
 48:         link.crossOrigin = 'anonymous';
 49:         document.head.appendChild(link);
 50:       });
 51:       
 52:       // Prefetch critical resources
 53:       const criticalResources = [
 54:         '/static/css/theme.css',
 55:         '/static/css/index.css',
 56:         '/static/js/loaders.js',
 57:         '/static/js/performance-optimizer.js'
 58:       ];
 59:       
 60:       criticalResources.forEach(resource => {
 61:         const link = document.createElement('link');
 62:         link.rel = 'prefetch';
 63:         link.href = resource;
 64:         document.head.appendChild(link);
 65:       });
 66:       
 67:       // Preload most critical resources
 68:       const preloadResources = [
 69:         { href: '/static/css/theme.css', as: 'style' },
 70:         { href: '/static/css/index.css', as: 'style' },
 71:         { href: '/static/js/loaders.js', as: 'script' }
 72:       ];
 73:       
 74:       preloadResources.forEach(resource => {
 75:         const link = document.createElement('link');
 76:         link.rel = 'preload';
 77:         link.href = resource.href;
 78:         link.as = resource.as;
 79:         if (resource.as === 'style') {
 80:           link.onload = function() { this.rel = 'stylesheet'; };
 81:         }
 82:         document.head.appendChild(link);
 83:       });
 84:     }
 85:     
 86:     optimizeFontLoading() {
 87:       // Ensure the Google Fonts stylesheet is promoted to stylesheet quickly
 88:       const fontStylesheet = document.querySelector('link[href*="fonts.googleapis.com"]');
 89:       if (fontStylesheet && fontStylesheet.rel === 'preload') {
 90:         fontStylesheet.onload = function() {
 91:           this.rel = 'stylesheet';
 92:         };
 93:       }
 94:       
 95:       // Create font load promise (swap handled by CSS)
 96:       this.fontLoadPromise = new Promise((resolve) => {
 97:         if (document.fonts && document.fonts.ready) {
 98:           document.fonts.ready.then(() => {
 99:             console.log('✅ Fonts loaded');
100:             resolve();
101:           });
102:         } else {
103:           // Fallback for older browsers
104:           setTimeout(resolve, 1000);
105:         }
106:       });
107:     }
108:     
109:     setupAdvancedCLS() {
110:       // Reserve space for dynamic content
111:       this.reserveSpaceForDynamicContent();
112:       
113:       // Monitor for layout shifts
114:       let clsValue = 0;
115:       let clsEntries = [];
116:       
117:       if ('PerformanceObserver' in window) {
118:         const clsObserver = new PerformanceObserver((list) => {
119:           list.getEntries().forEach(entry => {
120:             if (!entry.hadRecentInput) {
121:               clsValue += entry.value;
122:               clsEntries.push({
123:                 value: entry.value,
124:                 sources: entry.sources,
125:                 timestamp: entry.startTime
126:               });
127:               
128:               // Log significant layout shifts
129:               if (entry.value > 0.1) {
130:                 console.warn('⚠️ Significant layout shift detected:', entry);
131:                 this.debugLayoutShift(entry);
132:               }
133:             }
134:           });
135:           
136:           this.metrics.cls = clsValue;
137:         });
138:         
139:         clsObserver.observe({ entryTypes: ['layout-shift'] });
140:       }
141:       
142:       // Add skeleton screens for async content
143:       this.addSkeletonScreens();
144:     }
145:     
146:     reserveSpaceForDynamicContent() {
147:       // Reserve space for images
148:       document.querySelectorAll('img').forEach(img => {
149:         if (!img.style.width && !img.style.height) {
150:           // Set explicit dimensions if available
151:           if (img.width && img.height) {
152:             img.style.width = img.width + 'px';
153:             img.style.height = img.height + 'px';
154:           } else {
155:             // Add aspect-ratio placeholder
156:             img.style.aspectRatio = '16 / 9';
157:             img.style.width = '100%';
158:             img.style.height = 'auto';
159:           }
160:         }
161:       });
162:       
163:       // Reserve space for iframes
164:       document.querySelectorAll('iframe').forEach(iframe => {
165:         if (!iframe.style.width && !iframe.style.height) {
166:           iframe.style.width = '100%';
167:           iframe.style.height = '400px';
168:         }
169:       });
170:       
171:       // Reserve space for dynamic content areas
172:       document.querySelectorAll('[data-dynamic-content]').forEach(element => {
173:         const minHeight = element.dataset.minHeight || '200px';
174:         element.style.minHeight = minHeight;
175:         element.classList.add('dynamic-content-reserved');
176:       });
177:     }
178:     
179:     addSkeletonScreens() {
180:       // Add skeleton screens for cards that might load asynchronously
181:       document.querySelectorAll('.card[data-skeleton]').forEach(card => {
182:         const skeleton = document.createElement('div');
183:         skeleton.className = 'skeleton skeleton-card';
184:         skeleton.style.cssText = `
185:           height: ${card.dataset.skeletonHeight || '120px'};
186:           border-radius: 0.75rem;
187:           margin-bottom: 1rem;
188:         `;
189:         
190:         // Hide skeleton when content loads
191:         const observer = new MutationObserver((mutations) => {
192:           mutations.forEach((mutation) => {
193:             if (mutation.target.textContent.trim()) {
194:               skeleton.remove();
195:               observer.disconnect();
196:             }
197:           });
198:         });
199:         
200:         observer.observe(card, { childList: true, subtree: true });
201:         card.parentNode.insertBefore(skeleton, card);
202:       });
203:     }
204:     
205:     debugLayoutShift(entry) {
206:       entry.sources.forEach(source => {
207:         const element = source.node;
208:         if (element) {
209:           console.log('Layout shift source:', {
210:             element: element.tagName + (element.className ? '.' + element.className : ''),
211:             previousRect: source.previousRect,
212:             currentRect: source.currentRect,
213:             shift: entry.value
214:           });
215:           
216:           // Add visual indicator for debugging
217:           element.style.outline = '2px solid red';
218:           setTimeout(() => {
219:             element.style.outline = '';
220:           }, 2000);
221:         }
222:       });
223:     }
224:     
225:     setupAdvancedFID() {
226:       // Optimize event listeners
227:       this.optimizeEventListeners();
228:       
229:       // Use passive event listeners where possible
230:       this.addPassiveListeners();
231:       
232:       // Monitor First Input Delay
233:       if ('PerformanceObserver' in window) {
234:         const fidObserver = new PerformanceObserver((list) => {
235:           const entries = list.getEntries();
236:           entries.forEach(entry => {
237:             this.metrics.fid = entry.processingStart - entry.startTime;
238:             console.log('🎯 FID:', this.metrics.fid.toFixed(2), 'ms');
239:             
240:             // Log slow interactions
241:             if (this.metrics.fid > 100) {
242:               console.warn('⚠️ Slow input detected:', this.metrics.fid.toFixed(2), 'ms');
243:             }
244:           });
245:         });
246:         
247:         fidObserver.observe({ entryTypes: ['first-input'] });
248:       }
249:       
250:       // Optimize main thread work
251:       this.optimizeMainThread();
252:     }
253:     
254:     optimizeEventListeners() {
255:       // Debounce scroll events
256:       let scrollTimeout;
257:       const originalScrollHandler = window.onscroll;
258:       
259:       window.addEventListener('scroll', () => {
260:         if (scrollTimeout) {
261:           cancelAnimationFrame(scrollTimeout);
262:         }
263:         
264:         scrollTimeout = requestAnimationFrame(() => {
265:           if (originalScrollHandler) {
266:             originalScrollHandler();
267:           }
268:         });
269:       }, { passive: true });
270:       
271:       // Debounce resize events
272:       let resizeTimeout;
273:       window.addEventListener('resize', () => {
274:         if (resizeTimeout) {
275:           clearTimeout(resizeTimeout);
276:         }
277:         
278:         resizeTimeout = setTimeout(() => {
279:           // Handle resize
280:           this.handleResize();
281:         }, 150);
282:       }, { passive: true });
283:     }
284:     
285:     addPassiveListeners() {
286:       // Make touch and wheel events passive
287:       const events = ['touchstart', 'touchmove', 'wheel', 'mousewheel'];
288:       
289:       events.forEach(eventType => {
290:         document.addEventListener(eventType, () => {}, { passive: true });
291:       });
292:     }
293:     
294:     optimizeMainThread() {
295:       // Use requestIdleCallback for non-critical tasks
296:       if ('requestIdleCallback' in window) {
297:         requestIdleCallback(() => {
298:           this.performNonCriticalTasks();
299:         });
300:       } else {
301:         // Fallback
302:         setTimeout(() => {
303:           this.performNonCriticalTasks();
304:         }, 100);
305:       }
306:     }
307:     
308:     performNonCriticalTasks() {
309:       // Load non-critical CSS
310:       this.loadNonCriticalCSS();
311:       
312:       // Initialize non-critical JavaScript
313:       this.initializeNonCriticalJS();
314:     }
315:     
316:     loadNonCriticalCSS() {
317:       const nonCriticalCSS = [
318:         '/static/css/sticky-cards.css',
319:         '/static/css/sticky-footer.css'
320:       ];
321:       
322:       nonCriticalCSS.forEach(href => {
323:         const link = document.createElement('link');
324:         link.rel = 'stylesheet';
325:         link.href = href;
326:         link.media = 'print';
327:         link.onload = function() {
328:           this.media = 'all';
329:         };
330:         document.head.appendChild(link);
331:       });
332:     }
333:     
334:     initializeNonCriticalJS() {
335:       // Initialize modules that are not critical for first paint
336:       setTimeout(() => {
337:         // Initialize bottom navigation
338:         if (window.BottomNavigation) {
339:           new BottomNavigation();
340:         }
341:         
342:         // Initialize micro-interactions
343:         if (window.MicroInteractions) {
344:           new MicroInteractions();
345:         }
346:       }, 200);
347:     }
348:     
349:     setupAdvancedLCP() {
350:       // Optimize largest contentful paint
351:       this.optimizeLCPElements();
352:       
353:       // Monitor LCP
354:       if ('PerformanceObserver' in window) {
355:         const lcpObserver = new PerformanceObserver((list) => {
356:           const entries = list.getEntries();
357:           const lastEntry = entries[entries.length - 1];
358:           this.metrics.lcp = lastEntry.renderTime || lastEntry.loadTime;
359:           console.log('🎨 LCP:', this.metrics.lcp.toFixed(2), 'ms');
360:           
361:           // Log slow LCP
362:           if (this.metrics.lcp > 2500) {
363:             console.warn('⚠️ Slow LCP detected:', this.metrics.lcp.toFixed(2), 'ms');
364:             this.analyzeLCPElement(lastEntry);
365:           }
366:         });
367:         
368:         lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
369:       }
370:       
371:       // Optimize critical images
372:       this.optimizeCriticalImages();
373:     }
374:     
375:     optimizeLCPElements() {
376:       // Prioritize loading of LCP candidates
377:       const lcpCandidates = [
378:         'img',
379:         'video',
380:         'canvas',
381:         'svg',
382:         '.status-item',
383:         '.scene-action',
384:         'h1', 'h2', 'h3'
385:       ];
386:       
387:       lcpCandidates.forEach(selector => {
388:         const elements = document.querySelectorAll(selector);
389:         elements.forEach(element => {
390:           // Add loading priority hints
391:           if (element.tagName === 'IMG') {
392:             element.loading = 'eager';
393:             element.fetchpriority = 'high';
394:           }
395:           
396:           // Add GPU acceleration
397:           element.classList.add('sb-gpu-accelerated');
398:         });
399:       });
400:     }
401:     
402:     optimizeCriticalImages() {
403:       document.querySelectorAll('img').forEach(img => {
404:         // Add proper loading attributes
405:         if (!img.loading) {
406:           img.loading = 'eager';
407:         }
408:         
409:         // Add error handling
410:         img.addEventListener('error', () => {
411:           img.style.display = 'none';
412:           const placeholder = document.createElement('div');
413:           placeholder.className = 'image-error-placeholder';
414:           placeholder.textContent = 'Image non disponible';
415:           placeholder.style.cssText = `
416:             display: flex;
417:             align-items: center;
418:             justify-content: center;
419:             width: ${img.style.width || '100%'};
420:             height: ${img.style.height || '200px'};
421:             background: var(--sb-card);
422:             border: 1px solid var(--sb-card-border);
423:             border-radius: 0.5rem;
424:             color: var(--sb-muted);
425:             font-size: 0.875rem;
426:           `;
427:           img.parentNode.insertBefore(placeholder, img);
428:         });
429:         
430:         // Add fade-in effect
431:         img.style.opacity = '0';
432:         img.style.transition = 'opacity 0.3s ease';
433:         img.onload = () => {
434:           img.style.opacity = '1';
435:         };
436:       });
437:     }
438:     
439:     analyzeLCPElement(entry) {
440:       console.log('LCP Element Analysis:', {
441:         element: entry.element?.tagName + (entry.element?.className ? '.' + entry.element.className : ''),
442:         size: `${entry.width}x${entry.height}`,
443:         loadTime: entry.loadTime,
444:         renderTime: entry.renderTime,
445:         url: entry.url
446:       });
447:     }
448:     
449:     setupIntersectionOptimization() {
450:       // Use Intersection Observer for lazy loading and visibility-based optimizations
451:       if ('IntersectionObserver' in window) {
452:         const observer = new IntersectionObserver((entries) => {
453:           entries.forEach(entry => {
454:             if (entry.isIntersecting) {
455:               // Element is visible, optimize for performance
456:               this.optimizeVisibleElement(entry.target);
457:             } else {
458:               // Element is not visible, reduce resource usage
459:               this.reduceResourceUsage(entry.target);
460:             }
461:           });
462:         }, {
463:           rootMargin: '50px',
464:           threshold: 0.1
465:         });
466:         
467:         // Observe relevant elements
468:         document.querySelectorAll('.card, .status-item, img').forEach(el => {
469:           observer.observe(el);
470:         });
471:       }
472:     }
473:     
474:     optimizeVisibleElement(element) {
475:       // Enable animations for visible elements
476:       element.style.willChange = 'transform, opacity';
477:       
478:       // Start any paused animations
479:       if (element.dataset.pausedAnimation) {
480:         element.style.animationPlayState = 'running';
481:       }
482:     }
483:     
484:     reduceResourceUsage(element) {
485:       // Disable animations for non-visible elements
486:       element.style.willChange = 'auto';
487:       
488:       // Pause animations
489:       if (element.style.animationPlayState !== 'paused') {
490:         element.style.animationPlayState = 'paused';
491:         element.dataset.pausedAnimation = 'true';
492:       }
493:     }
494:     
495:     setupMainThreadScheduling() {
496:       // Schedule tasks to avoid blocking the main thread
497:       this.scheduleTasks();
498:     }
499:     
500:     scheduleTasks() {
501:       // Break up large tasks into smaller chunks
502:       const tasks = [
503:         () => this.initializeAnalytics(),
504:         () => this.initializeTooltips(),
505:         () => this.initializeModals(),
506:         () => this.preloadSecondaryResources()
507:       ];
508:       
509:       let taskIndex = 0;
510:       
511:       const runNextTask = () => {
512:         if (taskIndex < tasks.length) {
513:           const task = tasks[taskIndex];
514:           
515:           // Use requestAnimationFrame for smooth execution
516:           requestAnimationFrame(() => {
517:             task();
518:             taskIndex++;
519:             
520:             // Schedule next task with a small delay
521:             setTimeout(runNextTask, 50);
522:           });
523:         }
524:       };
525:       
526:       // Start task scheduling after initial paint
527:       if ('requestIdleCallback' in window) {
528:         requestIdleCallback(runNextTask);
529:       } else {
530:         setTimeout(runNextTask, 100);
531:       }
532:     }
533:     
534:     initializeAnalytics() {
535:       // Initialize analytics if present
536:       if (window.gtag) {
537:         // Analytics initialization
538:       }
539:     }
540:     
541:     initializeTooltips() {
542:       // Initialize tooltips
543:       document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
544:         // Initialize tooltip
545:       });
546:     }
547:     
548:     initializeModals() {
549:       // Initialize modals
550:       document.querySelectorAll('.modal').forEach(el => {
551:         // Initialize modal
552:       });
553:     }
554:     
555:     preloadSecondaryResources() {
556:       // Secondary resources are now opt-in via data-secondary-resource attributes
557:       const resources = Array.from(document.querySelectorAll('[data-secondary-resource]'))
558:         .map(el => el.getAttribute('data-secondary-resource'))
559:         .filter(Boolean);
560:       
561:       if (!resources.length) {
562:         return;
563:       }
564:       
565:       resources.forEach(resource => {
566:         const link = document.createElement('link');
567:         link.rel = 'preload';
568:         link.as = 'image';
569:         link.href = resource;
570:         document.head.appendChild(link);
571:       });
572:     }
573:     
574:     monitorAdvancedMetrics() {
575:       // Monitor additional performance metrics
576:       this.monitorTTFB();
577:       this.monitorFCP();
578:       this.setupPerformanceReporting();
579:     }
580:     
581:     monitorTTFB() {
582:       // Time to First Byte
583:       const navigation = performance.getEntriesByType('navigation')[0];
584:       if (navigation) {
585:         this.metrics.ttfb = navigation.responseStart - navigation.requestStart;
586:         console.log('⏱️ TTFB:', this.metrics.ttfb.toFixed(2), 'ms');
587:         
588:         if (this.metrics.ttfb > 800) {
589:           console.warn('⚠️ Slow TTFB detected:', this.metrics.ttfb.toFixed(2), 'ms');
590:         }
591:       }
592:     }
593:     
594:     monitorFCP() {
595:       // First Contentful Paint
596:       if ('PerformanceObserver' in window) {
597:         const fcpObserver = new PerformanceObserver((list) => {
598:           const entries = list.getEntries();
599:           entries.forEach(entry => {
600:             if (entry.name === 'first-contentful-paint') {
601:               this.metrics.fcp = entry.startTime;
602:               console.log('🎨 FCP:', this.metrics.fcp.toFixed(2), 'ms');
603:               
604:               if (this.metrics.fcp > 1800) {
605:                 console.warn('⚠️ Slow FCP detected:', this.metrics.fcp.toFixed(2), 'ms');
606:               }
607:             }
608:           });
609:         });
610:         
611:         fcpObserver.observe({ entryTypes: ['paint'] });
612:       }
613:     }
614:     
615:     setupPerformanceReporting() {
616:       // Report performance metrics periodically
617:       setInterval(() => {
618:         this.reportMetrics();
619:       }, 30000); // Every 30 seconds
620:       
621:       // Report on page unload
622:       window.addEventListener('beforeunload', () => {
623:         this.reportMetrics(true);
624:       });
625:     }
626:     
627:     reportMetrics(isFinal = false) {
628:       const report = {
629:         url: window.location.pathname,
630:         timestamp: Date.now(),
631:         metrics: this.metrics,
632:         userAgent: navigator.userAgent,
633:         viewport: {
634:           width: window.innerWidth,
635:           height: window.innerHeight
636:         },
637:         connection: navigator.connection ? {
638:           effectiveType: navigator.connection.effectiveType,
639:           downlink: navigator.connection.downlink,
640:           rtt: navigator.connection.rtt
641:         } : null,
642:         final: isFinal
643:       };
644:       
645:       console.log('📊 Performance Report:', report);
646:       
647:       // Send to analytics service if available
648:       if (window.gtag && isFinal) {
649:         window.gtag('event', 'performance_metrics', {
650:           custom_map: {
651:             lcp: this.metrics.lcp,
652:             fid: this.metrics.fid,
653:             cls: this.metrics.cls,
654:             ttfb: this.metrics.ttfb,
655:             fcp: this.metrics.fcp
656:           }
657:         });
658:       }
659:     }
660:     
661:     handleResize() {
662:       // Handle responsive layout changes
663:       this.reserveSpaceForDynamicContent();
664:     }
665:     
666:     // Public API
667:     getMetrics() {
668:       return { ...this.metrics };
669:     }
670:     
671:     optimizeElement(element) {
672:       element.classList.add('sb-gpu-accelerated');
673:       element.style.willChange = 'transform, opacity';
674:       
675:       setTimeout(() => {
676:         element.style.willChange = 'auto';
677:       }, 1000);
678:     }
679:     
680:     // Cleanup method
681:     destroy() {
682:       // Clean up observers and event listeners
683:       this.criticalResources.clear();
684:       this.loadedResources.clear();
685:       this.layoutShiftElements.clear();
686:     }
687:   }
688:   
689:   // Initialize advanced performance optimizer
690:   let advancedOptimizer;
691:   
692:   if (document.readyState === 'loading') {
693:     document.addEventListener('DOMContentLoaded', () => {
694:       advancedOptimizer = new AdvancedPerformanceOptimizer();
695:     });
696:   } else {
697:     advancedOptimizer = new AdvancedPerformanceOptimizer();
698:   }
699:   
700:   // Expose to global scope
701:   window.AdvancedPerformanceOptimizer = AdvancedPerformanceOptimizer;
702:   window.advancedOptimizer = advancedOptimizer;
703:   
704:   // Performance mark for initialization
705:   if ('performance' in window && 'mark' in performance) {
706:     performance.mark('advanced-optimizer-initialized');
707:   }
708: })();
```

## File: switchbot_dashboard/static/js/alerts.js
```javascript
 1: (() => {
 2:   const DISMISS_CLASS = "alert-dismissed";
 3: 
 4:   const dismissAlert = (alertElement) => {
 5:     if (!alertElement || alertElement.classList.contains(DISMISS_CLASS)) {
 6:       return;
 7:     }
 8: 
 9:     alertElement.classList.add(DISMISS_CLASS);
10:     const removeAfterTransition = () => {
11:       alertElement.removeEventListener("transitionend", removeAfterTransition);
12:       if (alertElement.parentElement) {
13:         alertElement.parentElement.removeChild(alertElement);
14:       }
15:     };
16: 
17:     alertElement.addEventListener("transitionend", removeAfterTransition);
18:     window.setTimeout(removeAfterTransition, 600);
19:   };
20: 
21:   document.addEventListener("DOMContentLoaded", () => {
22:     document.querySelectorAll("[data-auto-dismiss]").forEach((alertElement) => {
23:       const timeout = Number(alertElement.dataset.autoDismiss) || 0;
24:       if (timeout <= 0) {
25:         return;
26:       }
27: 
28:       window.setTimeout(() => dismissAlert(alertElement), timeout);
29:     });
30:   });
31: })();
```

## File: switchbot_dashboard/static/js/bottom-nav.js
```javascript
  1: (function() {
  2:   'use strict';
  3:   
  4:   class BottomNavigation {
  5:     constructor() {
  6:       this.nav = document.querySelector('.sb-bottom-nav');
  7:       this.lastScrollY = window.scrollY;
  8:       this.scrollThreshold = 100;
  9:       this.isTicking = false;
 10:       
 11:       if (this.nav) {
 12:         this.init();
 13:       }
 14:     }
 15:     
 16:     init() {
 17:       this.bindEvents();
 18:       this.updateActiveState();
 19:       this.setupPerformanceOptimizations();
 20:     }
 21:     
 22:     bindEvents() {
 23:       let scrollTimer;
 24:       window.addEventListener('scroll', () => {
 25:         if (!scrollTimer) {
 26:           scrollTimer = setTimeout(() => {
 27:             this.handleScroll();
 28:             scrollTimer = null;
 29:           }, 16); // ~60fps
 30:         }
 31:       }, { passive: true });
 32:       
 33:       this.nav.addEventListener('click', (e) => {
 34:         const link = e.target.closest('.sb-bottom-nav-item');
 35:         if (link) {
 36:           this.handleNavClick(link, e);
 37:         }
 38:       });
 39:       
 40:       window.addEventListener('resize', this.debounce(() => {
 41:         this.updateActiveState();
 42:       }, 250));
 43:     }
 44:     
 45:     handleScroll() {
 46:       const currentScrollY = window.scrollY;
 47:       const scrollDelta = Math.abs(currentScrollY - this.lastScrollY);
 48:       
 49:       if (scrollDelta > this.scrollThreshold) {
 50:         if (currentScrollY > this.lastScrollY && currentScrollY > 100) {
 51:           // Scrolling down - hide nav
 52:           this.hideNav();
 53:         } else {
 54:           // Scrolling up - show nav
 55:           this.showNav();
 56:         }
 57:         this.lastScrollY = currentScrollY;
 58:       }
 59:     }
 60:     
 61:     handleNavClick(link, event) {
 62:       link.style.transform = 'scale(0.95)';
 63:       setTimeout(() => {
 64:         link.style.transform = '';
 65:       }, 150);
 66:       
 67:       this.updateActiveState(link);
 68:     }
 69:     
 70:     hideNav() {
 71:       if (!this.nav.classList.contains('sb-bottom-nav--hidden')) {
 72:         this.nav.classList.add('sb-bottom-nav--hidden');
 73:       }
 74:     }
 75:     
 76:     showNav() {
 77:       if (this.nav.classList.contains('sb-bottom-nav--hidden')) {
 78:         this.nav.classList.remove('sb-bottom-nav--hidden');
 79:       }
 80:     }
 81:     
 82:     updateActiveState(clickedLink = null) {
 83:       const currentPath = window.location.pathname;
 84:       const links = this.nav.querySelectorAll('.sb-bottom-nav-item');
 85:       
 86:       links.forEach(link => {
 87:         const href = link.getAttribute('href');
 88:         const isActive = clickedLink === link || 
 89:                        (href === currentPath) ||
 90:                        (href === '/' && currentPath === '/');
 91:         
 92:         if (isActive) {
 93:           link.classList.add('sb-bottom-nav-item--active');
 94:           link.setAttribute('aria-current', 'page');
 95:         } else {
 96:           link.classList.remove('sb-bottom-nav-item--active');
 97:           link.removeAttribute('aria-current');
 98:         }
 99:       });
100:     }
101:     
102:     setupPerformanceOptimizations() {
103:       this.nav.style.willChange = 'transform';
104:       
105:       this.nav.style.transform = 'translateZ(0)';
106:       
107:       if ('IntersectionObserver' in window) {
108:         const observer = new IntersectionObserver((entries) => {
109:           entries.forEach(entry => {
110:             if (entry.isIntersecting) {
111:               this.nav.style.opacity = '1';
112:             }
113:           });
114:         }, { threshold: 0.1 });
115:         
116:         observer.observe(this.nav);
117:       }
118:     }
119:     
120:     debounce(func, wait) {
121:       let timeout;
122:       return function executedFunction(...args) {
123:         const later = () => {
124:           clearTimeout(timeout);
125:           func(...args);
126:         };
127:         clearTimeout(timeout);
128:         timeout = setTimeout(later, wait);
129:       };
130:     }
131:   }
132:   
133:   if (document.readyState === 'loading') {
134:     document.addEventListener('DOMContentLoaded', () => {
135:       new BottomNavigation();
136:     });
137:   } else {
138:     new BottomNavigation();
139:   }
140: })();
```

## File: switchbot_dashboard/static/js/settings.js
```javascript
 1: document.addEventListener("DOMContentLoaded", () => {
 2:   const summary = document.getElementById("time_window_days_summary");
 3:   if (!summary) {
 4:     return;
 5:   }
 6: 
 7:   const checkboxes = Array.from(
 8:     document.querySelectorAll('input[name="time_window_days"]')
 9:   );
10: 
11:   const render = () => {
12:     const selectedCount = checkboxes.filter((checkbox) => checkbox.checked).length;
13:     summary.textContent = `${selectedCount} jour(s) sélectionné(s).`;
14:   };
15: 
16:   checkboxes.forEach((checkbox) => {
17:     checkbox.addEventListener("change", render);
18:   });
19: 
20:   render();
21: });
```

## File: switchbot_dashboard/aircon.py
```python
 1: from __future__ import annotations
 2: 
 3: from typing import Any, Dict
 4: 
 5: AIRCON_SCENE_KEYS: tuple[str, ...] = ("winter", "summer", "fan", "off")
 6: AIRCON_SCENE_LABELS: dict[str, str] = {
 7:     "winter": "Aircon ON – Hiver",
 8:     "summer": "Aircon ON – Été",
 9:     "fan": "Aircon ON – Mode neutre",
10:     "off": "Aircon OFF – Scène",
11: }
12: AIRCON_IFTTT_LABELS: dict[str, str] = {
13:     "winter": "IFTTT Webhook – Hiver",
14:     "summer": "IFTTT Webhook – Été",
15:     "fan": "IFTTT Webhook – Ventilateur",
16:     "off": "IFTTT Webhook – Arrêt",
17: }
18: 
19: 
20: def extract_aircon_scenes(settings: dict[str, Any]) -> Dict[str, str]:
21:     """Return a sanitized mapping of configured aircon scenes."""
22: 
23:     raw_scenes = settings.get("aircon_scenes", {})
24:     if not isinstance(raw_scenes, dict):
25:         raw_scenes = {}
26: 
27:     sanitized: dict[str, str] = {}
28:     for key in AIRCON_SCENE_KEYS:
29:         value = raw_scenes.get(key, "")
30:         sanitized[key] = str(value).strip() if isinstance(value, str) else ""
31:     return sanitized
```

## File: switchbot_dashboard/static/css/history.css
```css
  1: .history-filters .card {
  2:   border: 1px solid var(--sb-outline);
  3:   background: var(--sb-card);
  4: }
  5: 
  6: .history-filters .metric-checkboxes {
  7:   display: flex;
  8:   flex-wrap: wrap;
  9:   gap: 0.5rem;
 10: }
 11: 
 12: .history-filters .form-check {
 13:   background: var(--sb-surface-elevated);
 14:   border: 1px solid var(--sb-outline);
 15:   border-radius: 0.375rem;
 16:   padding: 0.5rem 0.75rem;
 17:   margin: 0;
 18: }
 19: 
 20: .history-filters .form-check-input:checked {
 21:   background-color: var(--sb-accent);
 22:   border-color: var(--sb-accent);
 23: }
 24: 
 25: .history-filters .form-check-label {
 26:   color: var(--sb-text-primary);
 27:   font-size: 0.875rem;
 28:   margin-bottom: 0;
 29: }
 30: 
 31: .status-card {
 32:   border: 1px solid var(--sb-border-color);
 33:   background: var(--sb-surface);
 34:   transition: transform 0.2s ease, box-shadow 0.2s ease;
 35: }
 36: 
 37: .status-card:hover {
 38:   transform: translateY(-2px);
 39:   box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
 40: }
 41: 
 42: .status-card .card-body {
 43:   padding: 1.5rem;
 44: }
 45: 
 46: .status-card__value {
 47:   font-size: 2rem;
 48:   font-weight: 700;
 49:   color: var(--sb-primary);
 50:   line-height: 1;
 51:   margin-bottom: 0.5rem;
 52: }
 53: 
 54: .status-card__label {
 55:   font-size: 0.875rem;
 56:   color: var(--sb-text-secondary);
 57:   font-weight: 500;
 58:   margin-bottom: 0.25rem;
 59: }
 60: 
 61: .status-card__unit {
 62:   font-size: 0.75rem;
 63:   color: var(--sb-text-muted);
 64:   text-transform: uppercase;
 65:   letter-spacing: 0.05em;
 66: }
 67: 
 68: .charts-section .card {
 69:   border: 1px solid var(--sb-border-color);
 70:   background: var(--sb-surface);
 71:   margin-bottom: 1rem;
 72: }
 73: 
 74: .charts-section .card-header {
 75:   background: var(--sb-surface-elevated);
 76:   border-bottom: 1px solid var(--sb-border-color);
 77:   padding: 1rem 1.5rem;
 78: }
 79: 
 80: .charts-section .card-title {
 81:   color: var(--sb-text-primary);
 82:   font-weight: 600;
 83:   font-size: 1rem;
 84: }
 85: 
 86: .chart-container {
 87:   position: relative;
 88:   height: 300px;
 89:   padding: 1rem;
 90: }
 91: 
 92: .chart-controls {
 93:   display: flex;
 94:   gap: 0.5rem;
 95: }
 96: 
 97: .chart-controls .btn {
 98:   font-size: 0.75rem;
 99:   padding: 0.25rem 0.5rem;
100:   border: 1px solid var(--sb-border-color);
101:   background: var(--sb-surface-elevated);
102:   color: var(--sb-text-secondary);
103: }
104: 
105: .chart-controls .btn:hover {
106:   background: var(--sb-surface-hover);
107:   color: var(--sb-text-primary);
108: }
109: 
110: @media (max-width: 992px) {
111:   .chart-container {
112:     height: 280px;
113:   }
114: }
115: 
116: @media (max-width: 768px) {
117:   .chart-container {
118:     height: 240px;
119:   }
120:   
121:   .chart-container canvas {
122:     max-height: 220px;
123:   }
124: }
125: 
126: @media (max-width: 576px) {
127:   .chart-container {
128:     height: 200px;
129:     padding: 0.75rem;
130:   }
131:   
132:   .chart-container canvas {
133:     max-height: 180px;
134:   }
135: }
136: 
137: @media (max-width: 480px) {
138:   .chart-container {
139:     height: 180px;
140:     padding: 0.5rem;
141:   }
142:   
143:   .chart-container canvas {
144:     max-height: 160px;
145:   }
146: }
147: 
148: .latest-records .card {
149:   border: 1px solid var(--sb-border-color);
150:   background: var(--sb-surface);
151: }
152: 
153: .latest-records .table {
154:   color: var(--sb-text-primary);
155:   margin-bottom: 0;
156: }
157: 
158: .latest-records .table th {
159:   background: var(--sb-surface-elevated);
160:   border-color: var(--sb-border-color);
161:   color: var(--sb-text-secondary);
162:   font-weight: 600;
163:   font-size: 0.875rem;
164:   text-transform: uppercase;
165:   letter-spacing: 0.05em;
166:   padding: 0.75rem;
167: }
168: 
169: .latest-records .table td {
170:   border-color: var(--sb-border-color);
171:   padding: 0.75rem;
172:   vertical-align: middle;
173: }
174: 
175: .latest-records .table-hover tbody tr:hover {
176:   background: var(--sb-surface-hover);
177: }
178: 
179: .real-time-status .card {
180:   border: 1px solid var(--sb-border-color);
181:   background: var(--sb-surface);
182: }
183: 
184: .status-indicator {
185:   width: 12px;
186:   height: 12px;
187:   border-radius: 50%;
188:   background: var(--sb-text-muted);
189:   transition: background-color 0.3s ease;
190: }
191: 
192: .status-indicator.status-success {
193:   background: var(--sb-success);
194:   box-shadow: 0 0 8px rgba(25, 135, 84, 0.4);
195: }
196: 
197: .status-indicator.status-error {
198:   background: var(--sb-danger);
199:   box-shadow: 0 0 8px rgba(220, 53, 69, 0.4);
200: }
201: 
202: .status-indicator.status-loading {
203:   background: var(--sb-warning);
204:   animation: pulse 1.5s ease-in-out infinite;
205: }
206: 
207: @keyframes pulse {
208:   0%, 100% {
209:     opacity: 1;
210:   }
211:   50% {
212:     opacity: 0.5;
213:   }
214: }
215: 
216: .sb-select,
217: .sb-input {
218:   background: var(--sb-surface-elevated);
219:   border: 1px solid var(--sb-border-color);
220:   color: var(--sb-text-primary);
221: }
222: 
223: .sb-select:focus,
224: .sb-input:focus {
225:   background: var(--sb-surface-elevated);
226:   border-color: var(--sb-primary);
227:   color: var(--sb-text-primary);
228:   box-shadow: 0 0 0 0.2rem rgba(13, 110, 253, 0.25);
229: }
230: 
231: .sb-select option {
232:   background: var(--sb-surface-elevated);
233:   color: var(--sb-text-primary);
234: }
235: 
236: .loading-overlay {
237:   position: absolute;
238:   top: 0;
239:   left: 0;
240:   right: 0;
241:   bottom: 0;
242:   background: rgba(33, 37, 41, 0.8);
243:   display: flex;
244:   align-items: center;
245:   justify-content: center;
246:   border-radius: 0.375rem;
247:   z-index: 10;
248: }
249: 
250: .loading-overlay .spinner-border {
251:   color: var(--sb-primary);
252: }
253: 
254: .chart-container canvas {
255:   border-radius: 0.25rem;
256: }
257: 
258: @media (max-width: 992px) {
259:   .status-cards .col-md-3 {
260:     margin-bottom: 1rem;
261:   }
262:   
263:   .charts-section .col-lg-8,
264:   .charts-section .col-lg-6 {
265:     margin-bottom: 1.5rem;
266:   }
267: }
268: 
269: @media (max-width: 768px) {
270:   .page-header {
271:     flex-direction: column;
272:     align-items: flex-start !important;
273:     gap: 1rem;
274:   }
275:   
276:   .page-header-actions {
277:     width: 100%;
278:     justify-content: flex-start;
279:   }
280:   
281:   .history-filters .row {
282:     gap: 1rem;
283:   }
284:   
285:   .history-filters .metric-checkboxes {
286:     flex-direction: column;
287:   }
288:   
289:   .metric-checkboxes .form-check {
290:     width: 100%;
291:   }
292: }
293: 
294: @media (max-width: 576px) {
295:   .container {
296:     padding-left: 1rem;
297:     padding-right: 1rem;
298:   }
299:   
300:   .status-card__value {
301:     font-size: 1.5rem;
302:   }
303:   
304:   .chart-container {
305:     padding: 0.5rem;
306:   }
307:   
308:   .latest-records .table {
309:     font-size: 0.875rem;
310:   }
311:   
312:   .latest-records .table th,
313:   .latest-records .table td {
314:     padding: 0.5rem;
315:   }
316: }
317: 
318: @media print {
319:   .page-header-actions,
320:   .chart-controls,
321:   .real-time-status {
322:     display: none !important;
323:   }
324:   
325:   .card {
326:     break-inside: avoid;
327:     border: 1px solid #000 !important;
328:   }
329:   
330:   .chart-container {
331:     height: 400px !important;
332:   }
333: }
334: 
335: @media (prefers-reduced-motion: reduce) {
336:   .status-card {
337:     transition: none;
338:   }
339:   
340:   .status-indicator {
341:     transition: none;
342:     animation: none;
343:   }
344:   
345:   .loading-overlay .spinner-border {
346:     animation: none;
347:     border: 2px solid var(--sb-primary);
348:     border-radius: 50%;
349:   }
350: }
351: 
352: @media (prefers-contrast: high) {
353:   .status-card,
354:   .charts-section .card,
355:   .latest-records .card,
356:   .real-time-status .card {
357:     border-width: 2px;
358:   }
359:   
360:   .sb-select,
361:   .sb-input {
362:     border-width: 2px;
363:   }
364: }
```

## File: switchbot_dashboard/static/js/devices.js
```javascript
 1: document.addEventListener("click", async (event) => {
 2:   const button = event.target.closest(".btn-copy");
 3:   if (!button) {
 4:     return;
 5:   }
 6: 
 7:   const value = button.getAttribute("data-copy");
 8:   if (!value) {
 9:     return;
10:   }
11: 
12:   const showFeedback = (message) => {
13:     const original = button.textContent;
14:     button.textContent = message;
15:     button.setAttribute("aria-live", "assertive");
16:     setTimeout(() => {
17:       button.textContent = original;
18:       button.removeAttribute("aria-live");
19:     }, 1800);
20:   };
21: 
22:   try {
23:     if (!navigator.clipboard) {
24:       throw new Error("Clipboard API unavailable");
25:     }
26: 
27:     await navigator.clipboard.writeText(value);
28:     showFeedback("Copié ✓");
29:   } catch (err) {
30:     console.warn("Clipboard API unavailable, using fallback", err);
31:     try {
32:       const textarea = document.createElement("textarea");
33:       textarea.value = value;
34:       textarea.setAttribute("readonly", "");
35:       textarea.style.position = "absolute";
36:       textarea.style.left = "-9999px";
37:       document.body.appendChild(textarea);
38:       textarea.select();
39:       const success = document.execCommand("copy");
40:       document.body.removeChild(textarea);
41:       if (success) {
42:         showFeedback("Copié ✓ (compatibilité)");
43:         return;
44:       }
45:       throw new Error("Fallback copy failed");
46:     } catch (fallbackError) {
47:       console.error("Clipboard copy failed", fallbackError);
48:       showFeedback("Copie impossible");
49:     }
50:   }
51: });
```

## File: switchbot_dashboard/templates/_footer_nav.html
```html
 1: <!-- StickyMobile Bottom Navigation Bar -->
 2: <div id="footer-bar" class="footer-bar-1" role="navigation" aria-label="Navigation mobile">
 3:   <a href="{{ url_for('dashboard.index') }}" class="{% if request.endpoint == 'dashboard.index' %}active-nav{% endif %}" data-loader aria-current="{% if request.endpoint == 'dashboard.index' %}page{% endif %}">
 4:     <i class="fas fa-home"></i>
 5:     <span class="nav-text">Accueil</span>
 6:   </a>
 7:   
 8:   <a href="{{ url_for('dashboard.settings_page') }}" class="{% if request.endpoint == 'dashboard.settings_page' %}active-nav{% endif %}" data-loader aria-current="{% if request.endpoint == 'dashboard.settings_page' %}page{% endif %}">
 9:     <i class="fas fa-cog"></i>
10:     <span class="nav-text">Réglages</span>
11:   </a>
12:   
13:   <a href="{{ url_for('dashboard.actions_page') }}" class="{% if request.endpoint == 'dashboard.actions_page' %}active-nav{% endif %}" data-loader aria-current="{% if request.endpoint == 'dashboard.actions_page' %}page{% endif %}">
14:     <i class="fas fa-bolt"></i>
15:     <span class="nav-text">Actions</span>
16:   </a>
17:   
18:   <a href="{{ url_for('dashboard.quota') }}" class="{% if request.endpoint == 'dashboard.quota' %}active-nav{% endif %}" data-loader aria-current="{% if request.endpoint == 'dashboard.quota' %}page{% endif %}">
19:     <i class="fas fa-chart-pie"></i>
20:     <span class="nav-text">Quota</span>
21:   </a>
22:   
23:   <a href="{{ url_for('dashboard.history_page') }}" class="{% if request.endpoint == 'dashboard.history_page' %}active-nav{% endif %}" data-loader aria-current="{% if request.endpoint == 'dashboard.history_page' %}page{% endif %}">
24:     <i class="fas fa-chart-line"></i>
25:     <span class="nav-text">Historique</span>
26:   </a>
27:   
28:   <a href="{{ url_for('dashboard.devices') }}" class="{% if request.endpoint == 'dashboard.devices' %}active-nav{% endif %}" data-loader aria-current="{% if request.endpoint == 'dashboard.devices' %}page{% endif %}">
29:     <i class="fas fa-microchip"></i>
30:     <span class="nav-text">Appareils</span>
31:   </a>
32: </div>
```

## File: switchbot_dashboard/ifttt.py
```python
  1: from __future__ import annotations
  2: 
  3: import logging
  4: from typing import Any
  5: from urllib.parse import urlparse
  6: 
  7: import requests
  8: 
  9: 
 10: logger = logging.getLogger(__name__)
 11: 
 12: 
 13: class IFTTTWebhookError(Exception):
 14:     pass
 15: 
 16: 
 17: def validate_webhook_url(url: str) -> bool:
 18:     if not url or not isinstance(url, str):
 19:         return False
 20:     url = url.strip()
 21:     if not url:
 22:         return False
 23:     try:
 24:         parsed = urlparse(url)
 25:         return parsed.scheme == "https" and bool(parsed.netloc)
 26:     except Exception:
 27:         return False
 28: 
 29: 
 30: def extract_ifttt_webhooks(settings: dict[str, Any]) -> dict[str, str]:
 31:     """Extract and normalize IFTTT webhook URLs from settings.
 32: 
 33:     Args:
 34:         settings: Configuration dictionary containing 'ifttt_webhooks' mapping
 35: 
 36:     Returns:
 37:         Dictionary with normalized webhook URLs for keys: 'winter', 'summer', 'fan', 'off'
 38:         Empty strings are used for missing or invalid entries
 39: 
 40:     Example:
 41:         >>> settings = {"ifttt_webhooks": {"winter": "https://maker.ifttt.com/trigger/..."}}
 42:         >>> extract_ifttt_webhooks(settings)
 43:         {"winter": "https://maker.ifttt.com/trigger/...", "summer": "", "fan": "", "off": ""}
 44:     """
 45:     raw_webhooks = settings.get("ifttt_webhooks", {})
 46:     if not isinstance(raw_webhooks, dict):
 47:         raw_webhooks = {}
 48: 
 49:     sanitized: dict[str, str] = {}
 50:     for key in ("winter", "summer", "fan", "off"):
 51:         value = raw_webhooks.get(key, "")
 52:         sanitized[key] = str(value).strip() if isinstance(value, str) else ""
 53:     return sanitized
 54: 
 55: 
 56: class IFTTTWebhookClient:
 57:     def __init__(
 58:         self,
 59:         *,
 60:         timeout: float = 10.0,
 61:         logger_instance: logging.Logger | None = None,
 62:     ) -> None:
 63:         self._timeout = timeout
 64:         self._logger = logger_instance or logger
 65: 
 66:     def _log(self, level: int, message: str, **details: Any) -> None:
 67:         payload = f"[ifttt] {message}"
 68:         if details:
 69:             formatted_details = " | ".join(f"{k}={v!r}" for k, v in sorted(details.items()))
 70:             payload = f"{payload} | {formatted_details}"
 71:         self._logger.log(level, payload)
 72: 
 73:     def trigger_webhook(
 74:         self,
 75:         webhook_url: str,
 76:         *,
 77:         event_data: dict[str, Any] | None = None,
 78:     ) -> None:
 79:         webhook_url = webhook_url.strip()
 80:         if not validate_webhook_url(webhook_url):
 81:             raise IFTTTWebhookError(f"Invalid webhook URL: {webhook_url}")
 82: 
 83:         payload = event_data or {}
 84: 
 85:         self._log(
 86:             logging.DEBUG,
 87:             "Triggering IFTTT webhook",
 88:             url=webhook_url[:50] + "..." if len(webhook_url) > 50 else webhook_url,
 89:             payload_keys=list(payload.keys()) if payload else [],
 90:         )
 91: 
 92:         try:
 93:             response = requests.post(
 94:                 webhook_url,
 95:                 json=payload,
 96:                 timeout=self._timeout,
 97:                 headers={"Content-Type": "application/json"},
 98:             )
 99:             response.raise_for_status()
100: 
101:             self._log(
102:                 logging.INFO,
103:                 "IFTTT webhook triggered successfully",
104:                 status_code=response.status_code,
105:             )
106: 
107:         except requests.exceptions.Timeout:
108:             self._log(logging.ERROR, "IFTTT webhook timeout", url=webhook_url[:50])
109:             raise IFTTTWebhookError(f"Webhook request timeout after {self._timeout}s")
110:         except requests.exceptions.RequestException as exc:
111:             self._log(
112:                 logging.ERROR,
113:                 "IFTTT webhook request failed",
114:                 error=str(exc),
115:                 url=webhook_url[:50],
116:             )
117:             raise IFTTTWebhookError(f"Webhook request failed: {exc}")
```

## File: switchbot_dashboard/postgres_store.py
```python
  1: from __future__ import annotations
  2: 
  3: import json
  4: import logging
  5: import threading
  6: from typing import Any
  7: 
  8: import psycopg
  9: from psycopg import sql
 10: from psycopg.rows import dict_row
 11: from psycopg.types.json import Jsonb
 12: from psycopg_pool import ConnectionPool
 13: 
 14: 
 15: class PostgresStoreError(RuntimeError):
 16:     """Raised when PostgreSQL storage backend cannot satisfy an operation."""
 17: 
 18: 
 19: class PostgresStore:
 20:     """PostgreSQL JSON store implementing BaseStore interface for Neon PostgreSQL."""
 21: 
 22:     def __init__(
 23:         self,
 24:         connection_string: str,
 25:         kind: str,
 26:         *,
 27:         logger: logging.Logger,
 28:         ssl_mode: str = "require",
 29:         max_connections: int = 10,
 30:     ) -> None:
 31:         self._kind = kind
 32:         self._logger = logger
 33:         self._lock = threading.Lock()
 34: 
 35:         # Configure connection parameters for Neon
 36:         self._connection_params = {
 37:             "conninfo": connection_string,
 38:             "min_size": 1,
 39:             "max_size": max_connections,
 40:         }
 41: 
 42:         # Initialize connection pool
 43:         self._pool = None
 44:         self._initialize_pool()
 45:         self._ensure_table_exists()
 46: 
 47:     def _initialize_pool(self) -> None:
 48:         """Initialize PostgreSQL connection pool (single attempt)."""
 49:         try:
 50:             self._pool = ConnectionPool(**self._connection_params)
 51:             self._logger.info(
 52:                 "[postgres] Connection pool initialized for %s store", self._kind
 53:             )
 54:         except Exception as exc:
 55:             self._logger.error(
 56:                 "[postgres] Failed to initialize connection pool for %s store (%s)",
 57:                 self._kind,
 58:                 exc,
 59:             )
 60:             raise PostgresStoreError(
 61:                 f"Failed to initialize PostgreSQL connection pool for {self._kind} store"
 62:             ) from exc
 63: 
 64:     def _ensure_table_exists(self) -> None:
 65:         """Create json_store table if it doesn't exist."""
 66:         create_table_query = sql.SQL("""
 67:             CREATE TABLE IF NOT EXISTS json_store (
 68:                 kind VARCHAR(50) PRIMARY KEY,
 69:                 data JSONB NOT NULL,
 70:                 updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
 71:             );
 72:             CREATE INDEX IF NOT EXISTS idx_json_store_kind ON json_store(kind);
 73:             CREATE INDEX IF NOT EXISTS idx_json_store_updated_at ON json_store(updated_at);
 74:         """)
 75: 
 76:         try:
 77:             with self._pool.connection() as conn:
 78:                 with conn.cursor() as cur:
 79:                     cur.execute(create_table_query)
 80:                     conn.commit()
 81:                     self._logger.info(
 82:                         "[postgres] Table ensured for %s store", self._kind
 83:                     )
 84:         except Exception as exc:
 85:             self._logger.error(
 86:                 "[postgres] Failed to ensure table exists for %s store (%s)",
 87:                 self._kind,
 88:                 exc,
 89:             )
 90:             raise PostgresStoreError(
 91:                 f"Failed to ensure table exists for {self._kind} store"
 92:             ) from exc
 93: 
 94:     def read(self) -> dict[str, Any]:
 95:         query = sql.SQL("SELECT data FROM json_store WHERE kind = %s")
 96: 
 97:         try:
 98:             with self._pool.connection() as conn:
 99:                 with conn.cursor(row_factory=dict_row) as cur:
100:                     cur.execute(query, (self._kind,))
101:                     result = cur.fetchone()
102: 
103:                     if result is None:
104:                         self._logger.debug(
105:                             "[postgres] No data found for %s store, returning empty dict",
106:                             self._kind,
107:                         )
108:                         return {}
109: 
110:                     # Parse JSONB data
111:                     data = result["data"]
112:                     if isinstance(data, str):
113:                         return json.loads(data)
114:                     if isinstance(data, dict):
115:                         return data
116:                     raise PostgresStoreError(
117:                         f"Invalid data type in PostgreSQL for {self._kind} store"
118:                     )
119: 
120:         except PostgresStoreError:
121:             raise
122:         except Exception as exc:
123:             self._logger.error(
124:                 "[postgres] Read failed for %s store (%s)", self._kind, exc
125:             )
126:             raise PostgresStoreError(
127:                 f"PostgreSQL read failed for {self._kind} store"
128:             ) from exc
129: 
130:     def write(self, data: dict[str, Any]) -> None:
131:         query = sql.SQL("""
132:             INSERT INTO json_store (kind, data, updated_at)
133:             VALUES (%s, %s, NOW())
134:             ON CONFLICT (kind)
135:             DO UPDATE SET
136:                 data = EXCLUDED.data,
137:                 updated_at = EXCLUDED.updated_at
138:         """)
139: 
140:         try:
141:             with self._pool.connection() as conn:
142:                 with conn.cursor() as cur:
143:                     # Convert data to JSONB
144:                     jsonb_data = Jsonb(data)
145:                     cur.execute(query, (self._kind, jsonb_data))
146:                     conn.commit()
147:                     self._logger.debug(
148:                         "[postgres] Data written successfully for %s store", self._kind
149:                     )
150: 
151:         except Exception as exc:
152:             self._logger.error(
153:                 "[postgres] Write failed for %s store (%s)", self._kind, exc
154:             )
155:             raise PostgresStoreError(
156:                 f"PostgreSQL write failed for {self._kind} store"
157:             ) from exc
158: 
159:     def close(self) -> None:
160:         """Close connection pool and cleanup resources."""
161:         if self._pool:
162:             try:
163:                 self._pool.close()
164:                 self._logger.info("[postgres] Connection pool closed for %s store", self._kind)
165:             except Exception as exc:
166:                 self._logger.warning(
167:                     "[postgres] Error closing connection pool for %s store (%s)",
168:                     self._kind,
169:                     exc,
170:                 )
171:             finally:
172:                 self._pool = None
173: 
174:     def health_check(self) -> bool:
175:         if not self._pool:
176:             return False
177: 
178:         try:
179:             with self._pool.connection() as conn:
180:                 with conn.cursor() as cur:
181:                     cur.execute("SELECT 1")
182:                     cur.fetchone()
183:                     return True
184:         except Exception as exc:
185:             self._logger.warning(
186:                 "[postgres] Health check failed for %s store (%s)", self._kind, exc
187:             )
188:             return False
189: 
190:     def __del__(self) -> None:
191:         """Cleanup on garbage collection."""
192:         self.close()
```

## File: switchbot_dashboard/quota.py
```python
  1: from __future__ import annotations
  2: 
  3: import datetime as dt
  4: import logging
  5: from typing import Any
  6: 
  7: from .config_store import BaseStore
  8: 
  9: logger = logging.getLogger(__name__)
 10: 
 11: 
 12: class ApiQuotaTracker:
 13:     """Persist and expose a daily SwitchBot API quota estimate."""
 14: 
 15:     def __init__(self, state_store: BaseStore, default_daily_limit: int = 10_000) -> None:
 16:         self._state_store = state_store
 17:         self._default_daily_limit = max(int(default_daily_limit), 1)
 18: 
 19:     def record_call(self, *, increment: int = 1) -> None:
 20:         """Fallback path used when the API does not expose quota headers."""
 21:         if increment <= 0:
 22:             return
 23: 
 24:         state = self._normalize_state()
 25:         limit = self._extract_limit(state)
 26:         used = self._safe_int(state.get("api_requests_total"), fallback=0)
 27:         used = max(used, 0) + increment
 28:         remaining = max(limit - used, 0)
 29: 
 30:         state["api_requests_total"] = used
 31:         state["api_requests_remaining"] = remaining
 32:         self._state_store.write(state)
 33:         logger.debug("[quota] fallback increment recorded: used=%s remaining=%s limit=%s", used, remaining, limit)
 34: 
 35:     def record_from_headers(self, *, limit: int | None, remaining: int | None) -> bool:
 36:         """
 37:         Persist authoritative data when SwitchBot exposes X-RateLimit headers.
 38: 
 39:         Returns True when the state was updated, False otherwise (e.g. headers missing).
 40:         """
 41:         if remaining is None:
 42:             return False
 43: 
 44:         state = self._normalize_state()
 45: 
 46:         limit_value: int
 47:         if limit is not None:
 48:             limit_value = max(int(limit), 1)
 49:             state["api_requests_limit"] = limit_value
 50:         else:
 51:             limit_value = self._extract_limit(state)
 52: 
 53:         remaining_value = max(min(int(remaining), limit_value), 0)
 54:         used = max(limit_value - remaining_value, 0)
 55: 
 56:         state["api_requests_total"] = used
 57:         state["api_requests_remaining"] = remaining_value
 58:         self._state_store.write(state)
 59: 
 60:         logger.debug(
 61:             "[quota] headers snapshot recorded: used=%s remaining=%s limit=%s",
 62:             used,
 63:             remaining_value,
 64:             limit_value,
 65:         )
 66:         return True
 67: 
 68:     def refresh_snapshot(self) -> dict[str, Any]:
 69:         """
 70:         Force a normalization of the quota snapshot even if no API call occurred recently.
 71: 
 72:         Returns the refreshed state for callers that want to reuse the values.
 73:         """
 74:         state = self._normalize_state()
 75:         self._state_store.write(state)
 76:         logger.debug("[quota] snapshot refreshed: day=%s remaining=%s", state.get("api_quota_day"), state.get("api_requests_remaining"))
 77:         return state
 78: 
 79:     def _normalize_state(self) -> dict[str, Any]:
 80:         state = self._state_store.read()
 81:         now = dt.datetime.now(dt.timezone.utc)
 82:         today = now.date().isoformat()
 83:         if state.get("api_quota_day") != today:
 84:             state["api_quota_day"] = today
 85:             state["api_requests_total"] = 0
 86:             state["api_requests_limit"] = self._default_daily_limit
 87:             state["api_requests_remaining"] = self._default_daily_limit
 88:             state["api_quota_reset_at"] = now.isoformat()
 89:         else:
 90:             # Ensure limit field is always present for downstream consumers.
 91:             state["api_requests_limit"] = self._extract_limit(state)
 92:             state.setdefault("api_quota_reset_at", now.isoformat())
 93:         return state
 94: 
 95:     def _extract_limit(self, state: dict[str, Any]) -> int:
 96:         limit = self._safe_int(state.get("api_requests_limit"), fallback=self._default_daily_limit)
 97:         return max(limit, 1)
 98: 
 99:     @staticmethod
100:     def _safe_int(value: Any, *, fallback: int) -> int:
101:         try:
102:             return int(value)
103:         except (TypeError, ValueError):
104:             return fallback
```

## File: .env.example
```
 1: # SwitchBot API v1.1 credentials
 2: # Get these from the SwitchBot app (Developer Options)
 3: SWITCHBOT_TOKEN=
 4: SWITCHBOT_SECRET=
 5: 
 6: # Retry settings (network instability)
 7: # Default behavior is 2 attempts total (1 retry) with 10 seconds delay
 8: SWITCHBOT_RETRY_ATTEMPTS=2
 9: SWITCHBOT_RETRY_DELAY_SECONDS=10
10: 
11: # Poll interval override (seconds, >=15)
12: SWITCHBOT_POLL_INTERVAL_SECONDS=60
13: 
14: # APScheduler configuration
15: # Set to "false" to disable internal scheduler (e.g., when using external cron)
16: SCHEDULER_ENABLED=true
17: 
18: # Flask settings
19: FLASK_SECRET_KEY=change-me
20: FLASK_HOST=127.0.0.1
21: FLASK_PORT=5000
22: FLASK_DEBUG=0
23: 
24: # Optional: override config paths
25: # SWITCHBOT_SETTINGS_PATH=/absolute/path/to/settings.json
26: # SWITCHBOT_STATE_PATH=/absolute/path/to/state.json
27: 
28: # Storage backend configuration
29: # STORE_BACKEND=postgres (recommended) or filesystem (fallback)
30: # POSTGRES_URL=postgresql://user:password@host:5432/dbname?sslmode=require
31: # POSTGRES_SSL_MODE=require (default, for Neon PostgreSQL)
32: 
33: # Legacy Redis configuration (deprecated, use PostgreSQL instead)
34: # STORE_BACKEND=redis
35: # REDIS_URL_PRIMARY=rediss://default:password@host:6379/0
36: # REDIS_URL_SECONDARY=rediss://default:password@host2:6380/0
37: # REDIS_URL=rediss://default:password@host:6379/0  # Legacy single-URL (fallback to PRIMARY if unset)
38: # REDIS_PREFIX=switchbot_dashboard
39: # REDIS_TTL_SECONDS=86400
40: 
41: # Timezone configuration (IANA timezone identifiers)
42: # TIMEZONE=Europe/Paris
```

## File: Dockerfile
```dockerfile
 1: FROM python:3.11-slim AS base
 2: 
 3: ENV PYTHONDONTWRITEBYTECODE=1 \
 4:     PYTHONUNBUFFERED=1 \
 5:     FLASK_ENV=production \
 6:     PORT=8000 \
 7:     WEB_CONCURRENCY=1
 8: 
 9: WORKDIR /app
10: 
11: RUN apt-get update \
12:     && apt-get install --no-install-recommends -y build-essential curl \
13:     && rm -rf /var/lib/apt/lists/*
14: 
15: COPY requirements.txt .
16: 
17: RUN pip install --no-cache-dir --upgrade pip \
18:     && pip install --no-cache-dir -r requirements.txt
19: 
20: COPY . .
21: 
22: RUN addgroup --system appuser \
23:     && adduser --system --ingroup appuser appuser \
24:     && chown -R appuser:appuser /app
25: 
26: USER appuser
27: 
28: EXPOSE 8000
29: 
30: CMD ["sh", "-c", "exec gunicorn 'switchbot_dashboard:create_app()' --config gunicorn.conf.py"]
```

## File: switchbot_dashboard/static/css/devices.css
```css
  1: .highlight-card {
  2:   border: 1px solid var(--sb-accent);
  3:   background: linear-gradient(120deg, rgba(138, 180, 255, 0.12), rgba(138, 180, 255, 0.05));
  4: }
  5: 
  6: .section-title {
  7:   display: flex;
  8:   align-items: center;
  9:   justify-content: space-between;
 10:   gap: 1rem;
 11:   margin-bottom: 1.25rem;
 12: }
 13: 
 14: .device-grid {
 15:   display: grid;
 16:   grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
 17:   gap: 1.5rem;
 18: }
 19: 
 20: .device-card {
 21:   border: 1px solid var(--sb-card-border);
 22:   background: rgba(12, 17, 34, 0.85);
 23:   border-radius: 1.25rem;
 24:   padding: 1.25rem;
 25:   box-shadow: 0 25px 60px rgba(0, 0, 0, 0.35);
 26:   display: flex;
 27:   flex-direction: column;
 28:   gap: 1rem;
 29: }
 30: 
 31: .device-card__header {
 32:   display: flex;
 33:   justify-content: space-between;
 34:   gap: 1rem;
 35:   align-items: flex-start;
 36: }
 37: 
 38: .device-name {
 39:   font-size: 1.1rem;
 40:   margin-bottom: 0.1rem;
 41: }
 42: 
 43: .device-type {
 44:   font-size: 0.85rem;
 45: }
 46: 
 47: .device-meta {
 48:   display: grid;
 49:   grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
 50:   gap: 0.75rem;
 51:   margin: 0;
 52: }
 53: 
 54: .device-meta--primary {
 55:   grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
 56: }
 57: 
 58: .device-meta--secondary {
 59:   margin-top: 0.75rem;
 60: }
 61: 
 62: .device-details {
 63:   border: 1px solid var(--sb-outline);
 64:   border-radius: 1rem;
 65:   padding: 0.75rem 1rem;
 66:   background: rgba(255, 255, 255, 0.03);
 67:   transition: all var(--sb-transition-normal) ease;
 68:   position: relative;
 69:   overflow: hidden;
 70: }
 71: 
 72: .device-details::before {
 73:   content: '';
 74:   position: absolute;
 75:   top: 0;
 76:   left: -100%;
 77:   width: 100%;
 78:   height: 100%;
 79:   background: linear-gradient(90deg, transparent, rgba(138, 180, 255, 0.1), transparent);
 80:   transition: left var(--sb-transition-slow) ease;
 81: }
 82: 
 83: .device-details:hover {
 84:   border-color: var(--sb-accent);
 85:   background: rgba(255, 255, 255, 0.06);
 86:   box-shadow: 0 4px 15px rgba(138, 180, 255, 0.2);
 87:   transform: translateY(-1px);
 88: }
 89: 
 90: .device-details:hover::before {
 91:   left: 100%;
 92: }
 93: 
 94: .device-details summary {
 95:   cursor: pointer;
 96:   font-weight: 600;
 97:   color: var(--sb-text);
 98:   display: flex;
 99:   align-items: center;
100:   justify-content: space-between;
101:   padding: 0.25rem 0;
102:   transition: color var(--sb-transition-fast) ease;
103:   position: relative;
104: }
105: 
106: .device-details summary::after {
107:   content: '▶';
108:   font-size: 0.8rem;
109:   transition: transform var(--sb-transition-fast) ease;
110:   color: var(--sb-accent);
111:   margin-left: 0.5rem;
112: }
113: 
114: .device-details[open] summary::after {
115:   transform: rotate(90deg);
116: }
117: 
118: .device-details:hover summary {
119:   color: var(--sb-accent);
120: }
121: 
122: .device-details[open] summary {
123:   margin-bottom: 0.35rem;
124: }
125: 
126: .device-meta dt {
127:   font-size: 0.7rem;
128:   text-transform: uppercase;
129:   letter-spacing: 0.05em;
130:   color: var(--sb-muted);
131:   margin-bottom: 0.1rem;
132: }
133: 
134: .device-meta dd {
135:   margin: 0;
136:   font-size: 0.95rem;
137: }
138: 
139: .device-actions {
140:   display: flex;
141:   flex-wrap: wrap;
142:   gap: 0.5rem;
143:   align-items: center;
144: }
145: 
146: .btn-copy {
147:   border: 1px solid var(--sb-outline);
148:   border-radius: 0.75rem;
149:   padding: 0.35rem 0.85rem;
150:   background: transparent;
151:   color: var(--sb-text);
152:   font-size: 0.9rem;
153:   transition: background 0.2s ease;
154: }
155: 
156: .btn-copy:hover,
157: .btn-copy:focus-visible {
158:   background: rgba(255, 255, 255, 0.08);
159:   color: var(--sb-text);
160: }
161: 
162: .raw-block {
163:   border: 1px solid var(--sb-outline);
164:   border-radius: 1rem;
165:   padding: 1rem;
166:   background: rgba(5, 10, 24, 0.55);
167:   transition: all var(--sb-transition-normal) ease;
168:   position: relative;
169:   overflow: hidden;
170: }
171: 
172: .raw-block::before {
173:   content: '';
174:   position: absolute;
175:   top: 0;
176:   left: -100%;
177:   width: 100%;
178:   height: 100%;
179:   background: linear-gradient(90deg, transparent, rgba(138, 180, 255, 0.08), transparent);
180:   transition: left var(--sb-transition-slow) ease;
181: }
182: 
183: .raw-block:hover {
184:   border-color: var(--sb-accent);
185:   background: rgba(5, 10, 24, 0.65);
186:   box-shadow: 0 4px 15px rgba(138, 180, 255, 0.15);
187:   transform: translateY(-1px);
188: }
189: 
190: .raw-block:hover::before {
191:   left: 100%;
192: }
193: 
194: .raw-block summary {
195:   cursor: pointer;
196:   font-weight: 600;
197:   display: flex;
198:   align-items: center;
199:   justify-content: space-between;
200:   color: var(--sb-text);
201:   transition: color var(--sb-transition-fast) ease;
202: }
203: 
204: .raw-block summary::after {
205:   content: '▶';
206:   font-size: 0.8rem;
207:   transition: transform var(--sb-transition-fast) ease;
208:   color: var(--sb-accent);
209:   margin-left: 0.5rem;
210: }
211: 
212: .raw-block[open] summary::after {
213:   transform: rotate(90deg);
214: }
215: 
216: .raw-block:hover summary {
217:   color: var(--sb-accent);
218: }
219: 
220: .raw-block[open] summary {
221:   margin-bottom: 0.75rem;
222: }
223: 
224: @media (max-width: 576px) {
225:   .device-card {
226:     padding: 1rem;
227:   }
228: 
229:   .device-actions {
230:     flex-direction: column;
231:     align-items: stretch;
232:   }
233: 
234:   .btn-copy {
235:     width: 100%;
236:     padding: 0.6rem 0.85rem;
237:   }
238:   
239:   .device-details,
240:   .raw-block {
241:     padding: 0.6rem 0.8rem;
242:   }
243:   
244:   .device-details summary,
245:   .raw-block summary {
246:     font-size: 0.95rem;
247:     padding: 0.3rem 0;
248:   }
249:   
250:   .device-details summary::after,
251:   .raw-block summary::after {
252:     font-size: 0.75rem;
253:   }
254: }
```

## File: switchbot_dashboard/static/css/settings.css
```css
 1: .settings-form label {
 2:   font-size: 0.92rem;
 3:   font-weight: 600;
 4:   color: var(--sb-muted);
 5: }
 6: 
 7: .settings-form .section-heading {
 8:   display: flex;
 9:   align-items: center;
10:   justify-content: space-between;
11:   gap: 0.5rem;
12: }
13: 
14: .time-window-card {
15:   background: rgba(138, 180, 255, 0.08);
16:   border: 1px dashed rgba(138, 180, 255, 0.3);
17: }
18: 
19: .day-chip .btn {
20:   min-width: 48px;
21:   border-radius: 999px;
22:   border-color: rgba(138, 180, 255, 0.4);
23:   color: var(--sb-text);
24: }
25: 
26: .day-chip .btn-check:checked + .btn {
27:   background: rgba(138, 180, 255, 0.22);
28:   border-color: var(--sb-accent);
29:   color: var(--sb-text);
30: }
31: 
32: .day-chip .btn:focus-visible {
33:   outline: 2px solid var(--sb-accent);
34:   outline-offset: 2px;
35: }
36: 
37: /* Mobile Form Optimization */
38: @media (max-width: 576px) {
39:   .day-chip .btn {
40:     min-width: 56px;
41:   }
42:   
43:   .time-window-card .col-6 {
44:     flex: 0 0 100%;
45:     max-width: 100%;
46:   }
47:   
48:   .form-select {
49:     font-size: 1rem;
50:     padding: 1rem;
51:     min-height: 56px;
52:   }
53:   
54:   .form-control {
55:     font-size: 1rem;
56:     padding: 1rem;
57:     min-height: 56px;
58:   }
59:   
60:   .form-label {
61:     font-size: 1rem;
62:     margin-bottom: 0.75rem;
63:   }
64:   
65:   .time-window-card {
66:     padding: 1rem;
67:   }
68: }
```

## File: switchbot_dashboard/templates/actions.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>Actions · SwitchBot Dashboard</title>
  7:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/bootstrap.min.css') }}" />
  8:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/space-grotesk.css') }}" />
  9:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 10:     <link rel="stylesheet" href="{{ url_for('static', filename='css/actions.css') }}" />
 11:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 12:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/fontawesome/css/all.min.css') }}" />
 13:   </head>
 14:   <body class="sb-dark">
 15:     <div class="container py-4">
 16:       <header class="page-header mb-4">
 17:         <div class="page-header-main">
 18:           <h1 class="h3 mb-0">Actions Rapides</h1>
 19:           <p class="page-subtitle text-muted mb-0">
 20:             Déclenchez manuellement les scènes et commandes de climatisation.
 21:           </p>
 22:         </div>
 23:       </header>
 24: 
 25:       {% with messages = get_flashed_messages(with_categories=true) %}
 26:         {% if messages %}
 27:           <div class="mb-3" aria-live="polite" aria-atomic="true">
 28:             {% for category, message in messages %}
 29:               {% if category == 'error' %}
 30:                 <div class="alert alert-danger" role="alert" data-auto-dismiss="6000">
 31:                   {{ message }}
 32:                 </div>
 33:               {% else %}
 34:                 <div class="alert alert-success" role="alert" data-auto-dismiss="6000">
 35:                   {{ message }}
 36:                 </div>
 37:               {% endif %}
 38:             {% endfor %}
 39:           </div>
 40:         {% endif %}
 41:       {% endwith %}
 42: 
 43:       <!-- Actions principales -->
 44:       <section class="actions-section mb-4">
 45:         <div class="card sb-card">
 46:           <div class="card-header">
 47:             <h5 class="card-title mb-0">Actions principales</h5>
 48:             <small class="text-muted">Déclenchements manuels de l'automatisation</small>
 49:           </div>
 50:           <div class="card-body">
 51:             <div class="row g-3">
 52:               <div class="col-12 col-md-6">
 53:                 <form method="post" action="{{ url_for('dashboard.run_once') }}" data-loader>
 54:                   <button class="btn btn-primary w-100 action-btn rounded-m shadow-l" type="submit">
 55:                     <i class="fas fa-play me-2"></i>
 56:                     Exécuter une fois
 57:                   </button>
 58:                 </form>
 59:               </div>
 60:               <div class="col-12 col-md-6">
 61:                 <form method="post" action="{{ url_for('dashboard.quick_off') }}" data-loader>
 62:                   <button class="btn btn-secondary w-100 action-btn rounded-m shadow-l" type="submit">
 63:                     <i class="fas fa-stop me-2"></i>
 64:                     Arrêt rapide
 65:                   </button>
 66:                 </form>
 67:               </div>
 68:             </div>
 69:           </div>
 70:         </div>
 71:       </section>
 72: 
 73:       <!-- Scènes de climatisation -->
 74:       <section class="scenes-section mb-4">
 75:         <div class="card sb-card">
 76:           <div class="card-header">
 77:             <h5 class="card-title mb-0">Scènes de climatisation</h5>
 78:             <small class="text-muted">Déclenchez les scènes SwitchBot configurées</small>
 79:           </div>
 80:           <div class="card-body">
 81:             <div class="row g-3">
 82:               <div class="col-12 col-md-6">
 83:                 <form method="post" action="{{ url_for('dashboard.aircon_on_winter') }}" data-loader>
 84:                   <button
 85:                     class="btn btn-outline-success w-100 scene-btn rounded-m shadow-l"
 86:                     type="submit"
 87:                     aria-label="Activer la scène hiver SwitchBot"
 88:                     {% if missing_scenes['winter'] %}disabled aria-disabled="true"{% endif %}>
 89:                     <div class="scene-content">
 90:                       <div class="scene-icon scene-icon--winter" aria-hidden="true">
 91:                         <svg viewBox="0 0 24 24" role="img" focusable="false">
 92:                           <circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.6" fill="none" />
 93:                           <line x1="12" y1="3" x2="12" y2="1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
 94:                           <line x1="12" y1="23" x2="12" y2="21" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
 95:                           <line x1="4.22" y1="4.22" x2="2.81" y2="2.81" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
 96:                           <line x1="21.19" y1="21.19" x2="19.78" y2="19.78" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
 97:                           <line x1="3" y1="12" x2="1" y2="12" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
 98:                           <line x1="23" y1="12" x2="21" y2="12" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
 99:                           <line x1="4.22" y1="19.78" x2="2.81" y2="21.19" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
100:                           <line x1="21.19" y1="2.81" x2="19.78" y2="4.22" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
101:                         </svg>
102:                       </div>
103:                       <div class="scene-info">
104:                         <div class="scene-title">Climatisation ON – Hiver</div>
105:                         <div class="scene-status small {% if missing_scenes['winter'] %}text-warning{% else %}text-muted{% endif %}">
106:                           {% if missing_scenes['winter'] %}
107:                             Scène manquante
108:                           {% else %}
109:                             Scène configurée
110:                           {% endif %}
111:                         </div>
112:                       </div>
113:                     </div>
114:                   </button>
115:                 </form>
116:               </div>
117:               
118:               <div class="col-12 col-md-6">
119:                 <form method="post" action="{{ url_for('dashboard.aircon_on_summer') }}" data-loader>
120:                   <button
121:                     class="btn btn-outline-success w-100 scene-btn rounded-m shadow-l"
122:                     type="submit"
123:                     aria-label="Activer la scène été SwitchBot"
124:                     {% if missing_scenes['summer'] %}disabled aria-disabled="true"{% endif %}>
125:                     <div class="scene-content">
126:                       <div class="scene-icon scene-icon--summer" aria-hidden="true">
127:                         <svg viewBox="0 0 24 24" role="img" focusable="false">
128:                           <path
129:                             d="M12 2v20M4.93 4.93l14.14 14.14M2 12h20M4.93 19.07 19.07 4.93"
130:                             stroke="currentColor"
131:                             stroke-width="1.6"
132:                             stroke-linecap="round"
133:                             stroke-linejoin="round"
134:                             fill="none"
135:                           />
136:                           <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.6" fill="none" />
137:                         </svg>
138:                       </div>
139:                       <div class="scene-info">
140:                         <div class="scene-title">Climatisation ON – Été</div>
141:                         <div class="scene-status small {% if missing_scenes['summer'] %}text-warning{% else %}text-muted{% endif %}">
142:                           {% if missing_scenes['summer'] %}
143:                             Scène manquante
144:                           {% else %}
145:                             Scène configurée
146:                           {% endif %}
147:                         </div>
148:                       </div>
149:                     </div>
150:                   </button>
151:                 </form>
152:               </div>
153:               
154:               <div class="col-12 col-md-6">
155:                 <form method="post" action="{{ url_for('dashboard.aircon_on_fan') }}" data-loader>
156:                   <button
157:                     class="btn btn-outline-success w-100 scene-btn rounded-m shadow-l"
158:                     type="submit"
159:                     aria-label="Activer la scène ventilation SwitchBot"
160:                     {% if missing_scenes['fan'] %}disabled aria-disabled="true"{% endif %}>
161:                     <div class="scene-content">
162:                       <div class="scene-icon scene-icon--fan" aria-hidden="true">
163:                         <svg viewBox="0 0 24 24" role="img" focusable="false">
164:                           <path
165:                             d="M12 12c1.2-2.7 3.7-5.5 7.5-4.5 2.2.6 2.5 3.2.6 4.2-1.9 1-4.8.2-8.1.3M12 12c2.7 1.2 5.5 3.7 4.5 7.5-.6 2.2-3.2 2.5-4.2.6-1-1.9-.2-4.8-.3-8.1M12 12c-1.2 2.7-3.7 5.5-7.5 4.5-2.2-.6-2.5-3.2-.6-4.2 1.9-1 4.8-.2 8.1-.3"
166:                             stroke="currentColor"
167:                             stroke-width="1.6"
168:                             stroke-linecap="round"
169:                             stroke-linejoin="round"
170:                             fill="none"
171:                           />
172:                           <circle cx="12" cy="12" r="1.8" fill="currentColor" />
173:                         </svg>
174:                       </div>
175:                       <div class="scene-info">
176:                         <div class="scene-title">Climatisation ON – Mode neutre</div>
177:                         <div class="scene-status small {% if missing_scenes['fan'] %}text-warning{% else %}text-muted{% endif %}">
178:                           {% if missing_scenes['fan'] %}
179:                             Scène manquante
180:                           {% else %}
181:                             Scène configurée
182:                           {% endif %}
183:                         </div>
184:                       </div>
185:                     </div>
186:                   </button>
187:                 </form>
188:               </div>
189:               
190:               <div class="col-12 col-md-6">
191:                 <form method="post" action="{{ url_for('dashboard.aircon_off') }}" data-loader>
192:                   <button
193:                     class="btn btn-outline-danger w-100 scene-btn rounded-m shadow-l"
194:                     type="submit"
195:                     aria-label="Éteindre le climatiseur via la scène SwitchBot"
196:                     {% if missing_scenes['off'] %}disabled aria-disabled="true"{% endif %}>
197:                     <div class="scene-content">
198:                       <div class="scene-icon scene-icon--off" aria-hidden="true">
199:                         <svg viewBox="0 0 24 24" role="img" focusable="false">
200:                           <path
201:                             d="M12 2v10M7 4.5A9 9 0 1 0 17 4.5"
202:                             stroke="currentColor"
203:                             stroke-width="1.6"
204:                             stroke-linecap="round"
205:                             stroke-linejoin="round"
206:                             fill="none"
207:                           />
208:                         </svg>
209:                       </div>
210:                       <div class="scene-info">
211:                         <div class="scene-title">Climatisation OFF</div>
212:                         <div class="scene-status small {% if missing_scenes['off'] %}text-warning{% else %}text-muted{% endif %}">
213:                           {% if missing_scenes['off'] %}
214:                             Scène manquante
215:                           {% else %}
216:                             Scène configurée
217:                           {% endif %}
218:                         </div>
219:                       </div>
220:                     </div>
221:                   </button>
222:                 </form>
223:               </div>
224:             </div>
225:           </div>
226:         </div>
227:       </section>
228: 
229:       <!-- Informations d'état -->
230:       <section class="status-info">
231:         <div class="card sb-card">
232:           <div class="card-header">
233:             <h5 class="card-title mb-0">État actuel</h5>
234:           </div>
235:           <div class="card-body">
236:             <div class="row g-3">
237:               <div class="col-12 col-md-6">
238:                 <div class="status-item">
239:                   <div class="status-label">Température</div>
240:                   <div class="status-value">{{ state.get('last_temperature') }}</div>
241:                 </div>
242:               </div>
243:               <div class="col-12 col-md-6">
244:                 <div class="status-item">
245:                   <div class="status-label">Climatisation</div>
246:                   <div class="status-value">
247:                     {% if state.get('assumed_aircon_power') == 'on' %}
248:                       <span class="text-success">ON</span>
249:                     {% else %}
250:                       <span class="text-secondary">OFF</span>
251:                     {% endif %}
252:                   </div>
253:                 </div>
254:               </div>
255:             </div>
256:           </div>
257:         </div>
258:       </section>
259:     </div>
260:     
261:     {% include '_footer_nav.html' %}
262:     
263:     <script src="{{ url_for('static', filename='js/alerts.js') }}"></script>
264:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
265:     <script src="{{ url_for('static', filename='js/bottom-nav.js') }}"></script>
266:   </body>
267: </html>
```

## File: switchbot_dashboard/config_store.py
```python
  1: from __future__ import annotations
  2: 
  3: import json
  4: import logging
  5: import threading
  6: import time
  7: from collections.abc import Callable
  8: from pathlib import Path
  9: from typing import Any, Protocol, TypeVar, runtime_checkable
 10: 
 11: from redis import Redis
 12: from redis.exceptions import RedisError
 13: 
 14: 
 15: class StoreError(RuntimeError):
 16:     """Raised when a storage backend cannot satisfy a read/write operation."""
 17: 
 18: 
 19: @runtime_checkable
 20: class BaseStore(Protocol):
 21:     def read(self) -> dict[str, Any]:
 22:         ...
 23: 
 24:     def write(self, data: dict[str, Any]) -> None:
 25:         ...
 26: 
 27: 
 28: class JsonStore:
 29:     def __init__(self, path: str) -> None:
 30:         self._path = Path(path)
 31:         self._lock = threading.Lock()
 32: 
 33:     @property
 34:     def path(self) -> Path:
 35:         return self._path
 36: 
 37:     def read(self) -> dict[str, Any]:
 38:         with self._lock:
 39:             if not self._path.exists():
 40:                 return {}
 41: 
 42:             with self._path.open("r", encoding="utf-8") as handle:
 43:                 return json.load(handle)
 44: 
 45:     def write(self, data: dict[str, Any]) -> None:
 46:         self._path.parent.mkdir(parents=True, exist_ok=True)
 47: 
 48:         with self._lock:
 49:             tmp_path = self._path.with_suffix(self._path.suffix + ".tmp")
 50:             with tmp_path.open("w", encoding="utf-8") as handle:
 51:                 json.dump(data, handle, indent=2, ensure_ascii=False)
 52:                 handle.write("\n")
 53: 
 54:             tmp_path.replace(self._path)
 55: 
 56: 
 57: class RedisJsonStore:
 58:     def __init__(
 59:         self,
 60:         client: Redis,
 61:         key: str,
 62:         ttl_seconds: int | None = None,
 63:     ) -> None:
 64:         self._client = client
 65:         self._key = key
 66:         self._ttl_seconds = ttl_seconds
 67: 
 68:     def read(self) -> dict[str, Any]:
 69:         try:
 70:             raw_value = self._client.get(self._key)
 71:         except RedisError as exc:
 72:             raise StoreError(f"Redis read failed for key '{self._key}'") from exc
 73: 
 74:         if raw_value is None:
 75:             return {}
 76: 
 77:         try:
 78:             raw_text = raw_value.decode("utf-8") if isinstance(raw_value, bytes) else str(raw_value)
 79:             return json.loads(raw_text)
 80:         except json.JSONDecodeError as exc:
 81:             raise StoreError(f"Redis payload for '{self._key}' is not valid JSON") from exc
 82: 
 83:     def write(self, data: dict[str, Any]) -> None:
 84:         payload = json.dumps(data, ensure_ascii=False)
 85:         try:
 86:             self._client.set(name=self._key, value=payload, ex=self._ttl_seconds)
 87:         except RedisError as exc:
 88:             raise StoreError(f"Redis write failed for key '{self._key}'") from exc
 89: 
 90: 
 91: _T = TypeVar("_T")
 92: 
 93: 
 94: class FailoverStore:
 95:     def __init__(
 96:         self,
 97:         *,
 98:         kind: str,
 99:         primary: BaseStore,
100:         secondary: BaseStore | None,
101:         logger: logging.Logger,
102:         unhealthy_cooldown_seconds: int = 60,
103:     ) -> None:
104:         self._kind = kind
105:         self._primary = primary
106:         self._secondary = secondary
107:         self._logger = logger
108:         self._unhealthy_cooldown_seconds = max(unhealthy_cooldown_seconds, 1)
109: 
110:         self._lock = threading.Lock()
111:         self._primary_unhealthy_until = 0.0
112:         self._secondary_unhealthy_until = 0.0
113: 
114:     def mark_unhealthy(self, backend_name: str) -> None:
115:         if backend_name not in ("primary", "secondary"):
116:             raise ValueError(f"Unknown backend: {backend_name}")
117:         if backend_name == "secondary" and self._secondary is None:
118:             return
119:         self._mark_unhealthy(backend_name)
120: 
121:     def read(self) -> dict[str, Any]:
122:         return self._execute("read", lambda store: store.read())
123: 
124:     def write(self, data: dict[str, Any]) -> None:
125:         self._execute("write", lambda store: store.write(data))
126:         return None
127: 
128:     def _execute(self, operation: str, func: Callable[[BaseStore], _T]) -> _T:
129:         if self._secondary is None:
130:             return func(self._primary)
131: 
132:         backends = self._get_backend_order()
133:         last_exc: StoreError | None = None
134: 
135:         for backend_name, store in backends:
136:             try:
137:                 result = func(store)
138:             except StoreError as exc:
139:                 last_exc = exc
140:                 self._mark_unhealthy(backend_name)
141:                 self._logger.error(
142:                     "[store] %s store: %s backend failed during %s (%s)",
143:                     self._kind,
144:                     backend_name,
145:                     operation,
146:                     exc,
147:                 )
148:                 continue
149: 
150:             with self._lock:
151:                 if backend_name == "primary":
152:                     self._primary_unhealthy_until = 0.0
153:                 elif backend_name == "secondary":
154:                     self._secondary_unhealthy_until = 0.0
155:             return result
156: 
157:         raise StoreError(
158:             f"All backends failed for {self._kind} store (operation={operation})"
159:         ) from last_exc
160: 
161:     def _get_backend_order(self) -> list[tuple[str, BaseStore]]:
162:         now = time.monotonic()
163:         with self._lock:
164:             primary_healthy = now >= self._primary_unhealthy_until
165:             secondary_healthy = now >= self._secondary_unhealthy_until
166: 
167:         order: list[tuple[str, BaseStore]] = []
168:         if primary_healthy:
169:             order.append(("primary", self._primary))
170:         if secondary_healthy:
171:             order.append(("secondary", self._secondary))
172:         if not order:
173:             order = [("primary", self._primary), ("secondary", self._secondary)]
174: 
175:         return order
176: 
177:     def _mark_unhealthy(self, backend_name: str) -> None:
178:         until = time.monotonic() + self._unhealthy_cooldown_seconds
179:         with self._lock:
180:             if backend_name == "primary":
181:                 self._primary_unhealthy_until = until
182:             elif backend_name == "secondary":
183:                 self._secondary_unhealthy_until = until
```

## File: requirements.txt
```
1: Flask>=2.3,<4
2: APScheduler>=3.10,<4
3: requests>=2.31,<3
4: python-dotenv>=1.0,<2
5: gunicorn>=21.2,<22
6: redis>=5,<6
7: beautifulsoup4>=4.12,<5
8: psycopg[binary]>=3.2,<4
9: psycopg-pool>=3.3,<4
```

## File: switchbot_dashboard/static/css/sticky-footer.css
```css
  1: /* StickyMobile Footer Navigation - Adapted for SwitchBot Dashboard Theme */
  2: /* Extracted from StickyMobile template with dark mode integration */
  3: 
  4: /* Body padding to account for fixed footer */
  5: body.sb-dark {
  6:   padding-bottom: 80px;
  7:   padding-bottom: calc(80px + constant(safe-area-inset-bottom) * 1.1);
  8:   padding-bottom: calc(80px + env(safe-area-inset-bottom) * 1.1);
  9: }
 10: 
 11: /* Show footer on desktop too - with text + icons for complete navigation */
 12: @media (min-width: 769px) {
 13:   body.sb-dark {
 14:     padding-bottom: 80px;
 15:     padding-bottom: calc(80px + constant(safe-area-inset-bottom) * 1.1);
 16:     padding-bottom: calc(80px + env(safe-area-inset-bottom) * 1.1);
 17:   }
 18:   
 19:   #footer-bar {
 20:     display: flex !important; /* Force show on desktop */
 21:   }
 22:   
 23:   #footer-bar .nav-text {
 24:     display: block !important; /* Show text on desktop */
 25:   }
 26:   
 27:   #footer-bar a {
 28:     padding-top: 12px;
 29:   }
 30:   
 31:   #footer-bar i {
 32:     font-size: 18px;
 33:     margin-bottom: 0.25rem;
 34:   }
 35: }
 36: 
 37: /* Footer Bar Main Component */
 38: #footer-bar {
 39:   position: fixed;
 40:   bottom: 0px;
 41:   left: 0px;
 42:   right: 0px;
 43:   z-index: 102; /* Above 100 as requested */
 44:   background-color: var(--sb-bottom-nav-bg);
 45:   box-shadow: 0 -5px 10px 0 rgba(0, 0, 0, 0.06);
 46:   min-height: 60px;
 47:   height: calc(62px + constant(safe-area-inset-bottom) * 1.1);
 48:   height: calc(62px + env(safe-area-inset-bottom) * 1.1);
 49:   display: flex;
 50:   text-align: center;
 51:   backdrop-filter: blur(20px);
 52:   border-top: 1px solid var(--sb-bottom-nav-border);
 53: }
 54: 
 55: /* Footer Navigation Links */
 56: #footer-bar a {
 57:   color: var(--sb-text);
 58:   padding-top: 12px;
 59:   position: relative;
 60:   flex: 1 1 auto;
 61:   text-decoration: none;
 62:   transition: color var(--sb-transition-fast);
 63:   display: flex;
 64:   flex-direction: column;
 65:   align-items: center;
 66:   justify-content: center;
 67:   min-width: 44px;
 68:   min-height: 44px;
 69:   padding: 0.5rem;
 70: }
 71: 
 72: #footer-bar a:hover {
 73:   color: var(--sb-accent);
 74: }
 75: 
 76: #footer-bar .nav-text {
 77:   position: relative;
 78:   z-index: 2;
 79:   display: block;
 80:   font-size: 10px;
 81:   font-weight: 500;
 82:   margin-top: 0.25rem;
 83:   opacity: 0.7;
 84:   font-family: "Roboto", sans-serif !important;
 85: }
 86: 
 87: /* Hide text on mobile - show only icons */
 88: @media (max-width: 480px) {
 89:   #footer-bar .nav-text {
 90:     display: none !important;
 91:   }
 92:   
 93:   #footer-bar a {
 94:     padding-top: 1rem;
 95:     padding-bottom: 1rem;
 96:   }
 97:   
 98:   #footer-bar i {
 99:     font-size: 1.25rem;
100:     margin-bottom: 0;
101:     display: block !important;
102:     visibility: visible !important;
103:     opacity: 1 !important;
104:   }
105: }
106: 
107: /* Hide text on desktop too for icon-only navigation */
108: @media (min-width: 481px) and (max-width: 768px) {
109:   #footer-bar .nav-text {
110:     display: none !important;
111:   }
112:   
113:   #footer-bar a {
114:     padding-top: 1rem;
115:   }
116:   
117:   #footer-bar i {
118:     font-size: 1.1rem;
119:     margin-bottom: 0;
120:   }
121: }
122: 
123: /* For tablets and small desktops, show text + icons */
124: @media (min-width: 769px) {
125:   #footer-bar {
126:     display: flex !important; /* Ensure visible on desktop */
127:   }
128: }
129: 
130: #footer-bar i {
131:   font-size: 18px;
132:   position: relative;
133:   z-index: 2;
134:   margin-bottom: 0.25rem;
135: }
136: 
137: /* Footer Badge Component */
138: #footer-bar .badge {
139:   font-style: normal;
140:   z-index: 5;
141:   top: 0px;
142:   position: absolute;
143:   margin-left: 3px;
144:   color: var(--sb-alert-text) !important;
145:   width: 18px;
146:   text-align: center;
147:   line-height: 18px;
148:   padding: 0px;
149:   padding-left: 0px !important;
150:   border-radius: 18px;
151:   margin-top: 7px;
152:   font-size: 11px;
153:   background: var(--sb-accent);
154: }
155: 
156: /* Footer Bar Variants */
157: .footer-bar-1 {
158:   /* Default footer bar style */
159: }
160: 
161: .footer-bar-2 .active-nav {
162:   color: var(--sb-accent) !important;
163: }
164: 
165: .footer-bar-2 .active-nav strong {
166:   position: absolute;
167:   width: 80px;
168:   left: 50%;
169:   transform: translateX(-50%);
170:   top: 0px;
171:   bottom: 0px;
172:   background: var(--sb-accent);
173:   opacity: 0.1;
174: }
175: 
176: .footer-bar-3 span {
177:   display: none !important;
178: }
179: 
180: .footer-bar-3 .active-nav {
181:   padding-top: 11px !important;
182: }
183: 
184: .footer-bar-3 .active-nav span {
185:   display: block !important;
186: }
187: 
188: .footer-bar-3 a {
189:   padding-top: 18px !important;
190: }
191: 
192: .footer-bar-4 .active-nav {
193:   color: var(--sb-accent) !important;
194: }
195: 
196: .footer-bar-4 .active-nav strong {
197:   position: absolute;
198:   width: 47px;
199:   height: 47px;
200:   border-radius: 60px;
201:   left: 50%;
202:   top: 30px;
203:   transform: translate(-50%, -50%);
204:   bottom: 0px;
205:   background: var(--sb-accent);
206:   opacity: 0.15;
207: }
208: 
209: .footer-bar-4 span {
210:   display: none !important;
211: }
212: 
213: .footer-bar-4 i {
214:   padding-top: 10px;
215: }
216: 
217: .footer-bar-5 .active-nav strong {
218:   position: absolute;
219:   width: 50px;
220:   height: 2px;
221:   border-radius: 60px;
222:   left: 50%;
223:   top: 0px;
224:   transform: translateX(-50%);
225:   background: var(--sb-accent);
226: }
227: 
228: /* Footer Menu States */
229: .footer-menu-hidden {
230:   transition: all 100ms ease;
231:   transform: translateY(100%) !important;
232: }
233: 
234: .footer-bar-white * {
235:   color: var(--sb-text);
236: }
237: 
238: #footer-bar.position-relative {
239:   z-index: 102 !important;
240: }
241: 
242: /* iOS Specific Adjustments */
243: .is-ios #footer-bar {
244:   height: calc(65px + constant(safe-area-inset-bottom) * 1.1);
245:   height: calc(65px + env(safe-area-inset-bottom) * 1.1);
246: }
247: 
248: /* Non-iOS Specific Adjustments */
249: .is-not-ios .footer-menu-clear {
250:   height: 70px;
251:   display: block;
252: }
253: 
254: .is-not-ios .footer {
255:   padding-bottom: 0px;
256: }
257: 
258: .is-not-ios #footer-menu a i {
259:   padding-top: 13px;
260: }
261: 
262: .is-not-ios #footer-menu a span {
263:   opacity: 0.6;
264: }
265: 
266: /* Scrolling Footer Bar for Overflow */
267: .footer-bar-scroll {
268:   display: block !important;
269:   overflow-x: auto;
270:   -webkit-overflow-scrolling: touch;
271:   white-space: nowrap;
272:   margin: 0px;
273:   padding: 0px;
274: }
275: 
276: .footer-bar-scroll a {
277:   display: inline-block;
278:   width: 19.5%;
279: }
280: 
281: .footer-bar-scroll.footer-bar-4 .active-nav strong {
282:   margin-top: 1px;
283: }
284: 
285: .footer-bar-scroll.footer-bar-4 .badge {
286:   margin-left: -8px !important;
287:   margin-top: 14px !important;
288: }
289: 
290: .footer-bar-scroll.footer-bar-3 .badge {
291:   margin-left: -7px !important;
292:   margin-top: 0px !important;
293: }
294: 
295: .footer-bar-scroll.footer-bar-3 i {
296:   transform: translateY(-10px);
297: }
298: 
299: .footer-bar-scroll.footer-bar-3 .active-nav i {
300:   transform: translateY(0px);
301: }
302: 
303: /* Active State Enhancement */
304: #footer-bar .active-nav {
305:   color: var(--sb-accent) !important;
306: }
307: 
308: #footer-bar .active-nav .nav-text {
309:   opacity: 1;
310: }
311: 
312: /* Dark Mode Integration */
313: @media (prefers-color-scheme: dark) {
314:   #footer-bar {
315:     box-shadow: 0 -5px 10px 0 rgba(0, 0, 0, 0.3);
316:   }
317:   
318:   #footer-bar .badge {
319:     background: var(--sb-accent);
320:     color: var(--sb-accent-contrast) !important;
321:   }
322: }
```

## File: switchbot_dashboard/static/js/loaders.js
```javascript
  1: (() => {
  2:     const LOADER_CLASS = 'sb-loader';
  3:     const LOADER_ACTIVE_CLASS = 'sb-loader--active';
  4:     const LOADER_OVERLAY_CLASS = 'sb-loader-overlay';
  5:     const LOADER_SPINNER_CLASS = 'sb-loader-spinner';
  6:     const GLOBAL_LOADER_ID = 'sb-global-loader';
  7:     const GLOBAL_LOADER_ACTIVE_CLASS = 'sb-global-loader--active';
  8:     const FAILSAFE_TIMEOUT_MS = 15000;
  9:     
 10:     const loaderFailsafes = new WeakMap();
 11:     
 12:     const clearLoaderFailsafe = (element) => {
 13:         if (!element) {
 14:             return;
 15:         }
 16:         const timerId = loaderFailsafes.get(element);
 17:         if (timerId) {
 18:             clearTimeout(timerId);
 19:             loaderFailsafes.delete(element);
 20:         }
 21:     };
 22:     
 23:     const scheduleLoaderFailsafe = (element, cleanupCallback) => {
 24:         if (!element || typeof cleanupCallback !== 'function') {
 25:             return;
 26:         }
 27:         clearLoaderFailsafe(element);
 28:         const timerId = window.setTimeout(() => {
 29:             loaderFailsafes.delete(element);
 30:             cleanupCallback();
 31:         }, FAILSAFE_TIMEOUT_MS);
 32:         loaderFailsafes.set(element, timerId);
 33:     };
 34:     
 35:     const createLoaderOverlay = () => {
 36:         const overlay = document.createElement('span');
 37:         overlay.className = LOADER_OVERLAY_CLASS;
 38:         overlay.setAttribute('aria-hidden', 'true');
 39:         overlay.setAttribute('role', 'presentation');
 40:         
 41:         const spinner = document.createElement('span');
 42:         spinner.className = LOADER_SPINNER_CLASS;
 43:         spinner.setAttribute('role', 'img');
 44:         spinner.setAttribute('aria-label', 'Chargement...');
 45:         
 46:         overlay.appendChild(spinner);
 47:         return overlay;
 48:     };
 49: 
 50:     const ensureGlobalLoader = () => {
 51:         let overlay = document.getElementById(GLOBAL_LOADER_ID);
 52:         if (overlay) {
 53:             return overlay;
 54:         }
 55: 
 56:         overlay = document.createElement('div');
 57:         overlay.id = GLOBAL_LOADER_ID;
 58:         overlay.className = 'sb-global-loader';
 59:         overlay.setAttribute('aria-hidden', 'true');
 60:         overlay.setAttribute('role', 'presentation');
 61: 
 62:         const spinner = document.createElement('div');
 63:         spinner.className = 'sb-global-loader__spinner';
 64:         spinner.setAttribute('role', 'img');
 65:         spinner.setAttribute('aria-label', 'Chargement...');
 66: 
 67:         overlay.appendChild(spinner);
 68:         document.body.appendChild(overlay);
 69:         return overlay;
 70:     };
 71: 
 72:     const showGlobalLoader = () => {
 73:         const overlay = ensureGlobalLoader();
 74:         overlay.classList.add(GLOBAL_LOADER_ACTIVE_CLASS);
 75:         document.body.classList.add('sb-loading');
 76:     };
 77: 
 78:     const hideGlobalLoader = () => {
 79:         const overlay = document.getElementById(GLOBAL_LOADER_ID);
 80:         if (!overlay) {
 81:             return;
 82:         }
 83:         overlay.classList.remove(GLOBAL_LOADER_ACTIVE_CLASS);
 84:         document.body.classList.remove('sb-loading');
 85:     };
 86:     
 87:     const resetButtonState = (button, originalText) => {
 88:         if (!button) {
 89:             return;
 90:         }
 91:         if (typeof originalText === 'string') {
 92:             button.textContent = originalText;
 93:         }
 94:         if ('disabled' in button) {
 95:             button.disabled = false;
 96:         }
 97:     };
 98:     
 99:     const showLoader = (element) => {
100:         if (!element || element.classList.contains(LOADER_ACTIVE_CLASS)) {
101:             return;
102:         }
103:         
104:         element.classList.add(LOADER_ACTIVE_CLASS);
105:         element.setAttribute('aria-busy', 'true');
106:         
107:         const overlay = createLoaderOverlay();
108:         element.style.position = 'relative';
109:         element.appendChild(overlay);
110:         
111:         requestAnimationFrame(() => {
112:             overlay.style.opacity = '1';
113:         });
114:     };
115:     
116:     const hideLoader = (element) => {
117:         if (!element || !element.classList.contains(LOADER_ACTIVE_CLASS)) {
118:             return;
119:         }
120:         
121:         clearLoaderFailsafe(element);
122:         element.classList.remove(LOADER_ACTIVE_CLASS);
123:         element.removeAttribute('aria-busy');
124:         
125:         const overlay = element.querySelector(`.${LOADER_OVERLAY_CLASS}`);
126:         if (overlay) {
127:             overlay.style.opacity = '0';
128:             
129:             setTimeout(() => {
130:                 if (overlay.parentElement) {
131:                     overlay.parentElement.removeChild(overlay);
132:                 }
133:             }, 200);
134:         }
135:     };
136:     
137:     const setupFormLoaders = () => {
138:         const forms = document.querySelectorAll('form[data-loader]');
139:         forms.forEach((form) => {
140:             form.addEventListener('submit', (event) => {
141:                 const submitButton = form.querySelector('button[type="submit"], input[type="submit"]');
142:                 if (submitButton && !submitButton.disabled) {
143:                     event.preventDefault();
144:                     showGlobalLoader();
145:                     showLoader(submitButton);
146:                     
147:                     const originalText = submitButton.textContent;
148:                     submitButton.textContent = 'Chargement...';
149:                     submitButton.disabled = true;
150:                     
151:                     setTimeout(() => {
152:                         form.submit();
153:                     }, 1000);
154: 
155:                     const finalizeSubmission = () => {
156:                         hideGlobalLoader();
157:                         hideLoader(submitButton);
158:                         resetButtonState(submitButton, originalText);
159:                     };
160: 
161:                     setTimeout(() => {
162:                         finalizeSubmission();
163:                         clearLoaderFailsafe(submitButton);
164:                     }, 10000);
165: 
166:                     scheduleLoaderFailsafe(submitButton, finalizeSubmission);
167:                 }
168:             });
169:         });
170:     };
171:     
172:     const setupButtonLoaders = () => {
173:         document.querySelectorAll('button[data-loader]').forEach(button => {
174:             button.addEventListener('click', (event) => {
175:                 if (button.disabled) {
176:                     event.preventDefault();
177:                     return;
178:                 }
179:                 
180:                 showLoader(button);
181:                 
182:                 const originalText = button.textContent;
183:                 button.textContent = 'Chargement...';
184:                 button.disabled = true;
185: 
186:                 const finalizeAction = () => {
187:                     hideLoader(button);
188:                     resetButtonState(button, originalText);
189:                 };
190:                 
191:                 setTimeout(() => {
192:                     finalizeAction();
193:                     clearLoaderFailsafe(button);
194:                 }, 3000);
195: 
196:                 scheduleLoaderFailsafe(button, () => {
197:                     hideGlobalLoader();
198:                     finalizeAction();
199:                 });
200:             });
201:         });
202:     };
203:     
204:     const setupNavigationLoaders = () => {
205:         document.querySelectorAll('a[data-loader]').forEach((link) => {
206:             link.addEventListener('click', (event) => {
207:                 if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) {
208:                     return;
209:                 }
210: 
211:                 const href = link.getAttribute('href') || '';
212:                 if (!href || href.startsWith('#') || href.startsWith('javascript:')) {
213:                     return;
214:                 }
215: 
216:                 event.preventDefault();
217:                 showGlobalLoader();
218:                 showLoader(link);
219: 
220:                 scheduleLoaderFailsafe(link, () => {
221:                     hideGlobalLoader();
222:                     hideLoader(link);
223:                 });
224: 
225:                 setTimeout(() => {
226:                     window.location.href = href;
227:                 }, 150);
228:             });
229:         });
230:     };
231:     
232:     document.addEventListener('DOMContentLoaded', () => {
233:         ensureGlobalLoader();
234:         hideGlobalLoader();
235:         setupFormLoaders();
236:         setupButtonLoaders();
237:         setupNavigationLoaders();
238:         
239:         window.SwitchBotLoaders = {
240:             show: showLoader,
241:             hide: hideLoader,
242:             showGlobal: showGlobalLoader,
243:             hideGlobal: hideGlobalLoader,
244:             scheduleFailsafe: scheduleLoaderFailsafe,
245:             clearFailsafe: clearLoaderFailsafe,
246:             failsafeDelayMs: FAILSAFE_TIMEOUT_MS,
247:         };
248:     });
249: })();
```

## File: switchbot_dashboard/scheduler.py
```python
  1: from __future__ import annotations
  2: 
  3: import datetime as dt
  4: import logging
  5: import threading
  6: from typing import Any, Callable
  7: from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
  8: 
  9: from apscheduler.schedulers.background import BackgroundScheduler
 10: 
 11: from .config_store import BaseStore
 12: from .automation import DEFAULT_TIMEZONE, OFF_REPEAT_STATE_KEY, _is_now_in_windows, _parse_hhmm
 13: 
 14: 
 15: class SchedulerService:
 16:     def __init__(
 17:         self,
 18:         settings_store: BaseStore,
 19:         tick_callable: Callable[[], None],
 20:         *,
 21:         state_store: BaseStore | None = None,
 22:         logger: logging.Logger | None = None,
 23:     ) -> None:
 24:         self._settings_store = settings_store
 25:         self._state_store = state_store
 26:         self._tick_callable = tick_callable
 27:         self._scheduler: BackgroundScheduler | None = None
 28:         self._job_id = "automation_tick"
 29:         self._lock = threading.Lock()
 30:         self._logger = logger or logging.getLogger(__name__)
 31:         self._current_interval_seconds: int | None = None
 32: 
 33:     def _run_tick_safe(self) -> None:
 34:         """Execute tick callable while guarding against uncaught exceptions."""
 35:         try:
 36:             self._tick_callable()
 37:         except Exception as exc:  # pragma: no cover - exercised via tests
 38:             self._logger.error(
 39:                 "[scheduler] Automation tick raised exception: %s",
 40:                 exc,
 41:                 exc_info=True,
 42:             )
 43:         finally:
 44:             self._maybe_reschedule_after_tick()
 45: 
 46:     @staticmethod
 47:     def _as_int(value: Any, *, default: int, minimum: int | None = None, maximum: int | None = None) -> int:
 48:         try:
 49:             parsed = int(value)
 50:         except (TypeError, ValueError):
 51:             parsed = default
 52: 
 53:         if minimum is not None and parsed < minimum:
 54:             parsed = minimum
 55:         if maximum is not None and parsed > maximum:
 56:             parsed = maximum
 57:         return parsed
 58: 
 59:     def _has_pending_off_repeat(self) -> bool:
 60:         if self._state_store is None:
 61:             return False
 62: 
 63:         state = self._state_store.read()
 64:         task = state.get(OFF_REPEAT_STATE_KEY)
 65:         if not isinstance(task, dict):
 66:             return False
 67:         remaining = self._as_int(task.get("remaining"), default=0, minimum=0)
 68:         return remaining > 0
 69: 
 70:     def _resolve_timezone(self, settings: dict[str, Any]) -> dt.tzinfo:
 71:         timezone_name = str(settings.get("timezone") or "").strip() or DEFAULT_TIMEZONE
 72:         try:
 73:             return ZoneInfo(timezone_name)
 74:         except ZoneInfoNotFoundError:
 75:             return dt.timezone.utc
 76: 
 77:     def _next_window_start(self, time_windows: list[dict[str, Any]], now: dt.datetime) -> dt.datetime | None:
 78:         if not time_windows:
 79:             return None
 80: 
 81:         candidates: list[dt.datetime] = []
 82:         tzinfo = now.tzinfo or dt.timezone.utc
 83:         base_date = now.date()
 84:         base_weekday = now.weekday()
 85: 
 86:         for window in time_windows:
 87:             days = window.get("days")
 88:             if not isinstance(days, list):
 89:                 continue
 90:             start_raw = window.get("start")
 91:             end_raw = window.get("end")
 92:             if not isinstance(start_raw, str) or not isinstance(end_raw, str):
 93:                 continue
 94: 
 95:             try:
 96:                 start_time = _parse_hhmm(start_raw)
 97:             except ValueError:
 98:                 continue
 99: 
100:             for day_offset in range(0, 8):
101:                 candidate_weekday = (base_weekday + day_offset) % 7
102:                 if candidate_weekday not in days:
103:                     continue
104:                 candidate_date = base_date + dt.timedelta(days=day_offset)
105:                 candidate_start = dt.datetime.combine(candidate_date, start_time, tzinfo=tzinfo)
106:                 if candidate_start > now:
107:                     candidates.append(candidate_start)
108: 
109:         if not candidates:
110:             return None
111:         return min(candidates)
112: 
113:     def _get_effective_interval_seconds(self, *, now_utc: dt.datetime | None = None) -> tuple[int, str]:
114:         settings = self._settings_store.read()
115: 
116:         base_interval = self._as_int(
117:             settings.get("poll_interval_seconds", 120),
118:             default=120,
119:             minimum=15,
120:             maximum=3600,
121:         )
122: 
123:         adaptive_enabled = bool(settings.get("adaptive_polling_enabled", True))
124:         if not adaptive_enabled:
125:             return base_interval, "fixed"
126: 
127:         automation_enabled = bool(settings.get("automation_enabled", False))
128:         if not automation_enabled:
129:             return base_interval, "automation_disabled"
130: 
131:         time_windows = settings.get("time_windows", [])
132:         if not isinstance(time_windows, list) or not time_windows:
133:             return base_interval, "no_windows"
134: 
135:         if self._has_pending_off_repeat():
136:             return base_interval, "pending_off_repeat"
137: 
138:         tzinfo = self._resolve_timezone(settings)
139:         now = (now_utc or dt.datetime.now(dt.timezone.utc)).astimezone(tzinfo)
140:         in_window = _is_now_in_windows(time_windows, now)
141:         if in_window:
142:             return base_interval, "in_window"
143: 
144:         idle_interval = self._as_int(
145:             settings.get("idle_poll_interval_seconds", 600),
146:             default=600,
147:             minimum=15,
148:             maximum=86_400,
149:         )
150:         warmup_minutes = self._as_int(
151:             settings.get("poll_warmup_minutes", 15),
152:             default=15,
153:             minimum=0,
154:             maximum=24 * 60,
155:         )
156:         if warmup_minutes <= 0:
157:             return idle_interval, "idle"
158: 
159:         next_start = self._next_window_start(time_windows, now)
160:         if next_start is None:
161:             return idle_interval, "idle"
162: 
163:         warmup_delta = dt.timedelta(minutes=warmup_minutes)
164:         if next_start - now <= warmup_delta:
165:             return base_interval, "warmup"
166: 
167:         seconds_until_warmup_start = int((next_start - warmup_delta - now).total_seconds())
168:         if seconds_until_warmup_start <= 0:
169:             return base_interval, "warmup"
170: 
171:         clamped_idle = min(idle_interval, max(15, seconds_until_warmup_start))
172:         return clamped_idle, "idle"
173: 
174:     def _get_interval_seconds(self) -> int:
175:         interval, _ = self._get_effective_interval_seconds()
176:         return interval
177: 
178:     def _maybe_reschedule_after_tick(self) -> None:
179:         with self._lock:
180:             if self._scheduler is None:
181:                 return
182: 
183:             desired_interval, mode = self._get_effective_interval_seconds()
184:             if self._current_interval_seconds == desired_interval:
185:                 return
186: 
187:             previous = self._current_interval_seconds
188:             self._logger.info(
189:                 "[scheduler] Adaptive polling reschedule: %s -> %s seconds (mode=%s)",
190:                 previous,
191:                 desired_interval,
192:                 mode,
193:             )
194:             self._schedule_or_reschedule_locked()
195: 
196:     def start(self) -> None:
197:         with self._lock:
198:             if self._scheduler is not None:
199:                 self._logger.warning("[scheduler] Scheduler already started, ignoring duplicate start() call")
200:                 return
201: 
202:             self._scheduler = BackgroundScheduler(daemon=True)
203:             self._scheduler.start()
204:             self._logger.info("[scheduler] BackgroundScheduler started successfully")
205:             self._schedule_or_reschedule_locked()
206: 
207:         self._logger.info("[scheduler] Triggering immediate first tick")
208:         self._run_tick_safe()
209: 
210:     def _schedule_or_reschedule_locked(self) -> None:
211:         if self._scheduler is None:
212:             self._logger.warning("[scheduler] Cannot schedule job: scheduler is None")
213:             return
214: 
215:         interval = self._get_interval_seconds()
216: 
217:         existing_job = self._scheduler.get_job(self._job_id)
218:         if existing_job is not None:
219:             self._logger.debug("[scheduler] Removing existing job before rescheduling")
220:             existing_job.remove()
221: 
222:         self._scheduler.add_job(
223:             func=self._run_tick_safe,
224:             trigger="interval",
225:             seconds=interval,
226:             id=self._job_id,
227:             replace_existing=True,
228:             max_instances=1,
229:             coalesce=True,
230:         )
231:         self._current_interval_seconds = interval
232:         self._logger.info("[scheduler] Job scheduled with interval=%d seconds", interval)
233: 
234:     def reschedule(self) -> None:
235:         with self._lock:
236:             if self._scheduler is None:
237:                 self._logger.debug("[scheduler] Reschedule called but scheduler not started (normal if SCHEDULER_ENABLED=false)")
238:                 return
239:             
240:             self._logger.info("[scheduler] Rescheduling automation job")
241:             self._schedule_or_reschedule_locked()
242: 
243:     def stop(self) -> None:
244:         with self._lock:
245:             if self._scheduler is None:
246:                 self._logger.debug("[scheduler] Stop called but scheduler already stopped")
247:                 return
248: 
249:             self._logger.info("[scheduler] Shutting down scheduler")
250:             self._scheduler.shutdown(wait=False)
251:             self._scheduler = None
252: 
253:     def is_running(self) -> bool:
254:         with self._lock:
255:             if self._scheduler is None:
256:                 return False
257: 
258:             return getattr(self._scheduler, "running", False)
```

## File: switchbot_dashboard/switchbot_api.py
```python
  1: from __future__ import annotations
  2: 
  3: import base64
  4: import hashlib
  5: import hmac
  6: import time
  7: import uuid
  8: import logging
  9: from dataclasses import dataclass
 10: from typing import Any, Protocol
 11: 
 12: import requests
 13: from requests import Response
 14: 
 15: 
 16: logger = logging.getLogger(__name__)
 17: 
 18: 
 19: @dataclass(frozen=True)
 20: class SwitchBotResponse:
 21:     status_code: int
 22:     message: str
 23:     body: Any
 24: 
 25: 
 26: class SwitchBotApiError(RuntimeError):
 27:     pass
 28: 
 29: 
 30: class QuotaTracker(Protocol):
 31:     def record_call(self, *, increment: int = 1) -> None:
 32:         ...
 33: 
 34:     def record_from_headers(self, *, limit: int | None, remaining: int | None) -> bool:
 35:         ...
 36: 
 37: 
 38: class SwitchBotClient:
 39:     def __init__(
 40:         self,
 41:         token: str,
 42:         secret: str,
 43:         base_url: str | None = None,
 44:         retry_attempts: int = 2,
 45:         retry_delay_seconds: int = 10,
 46:         quota_tracker: QuotaTracker | None = None,
 47:     ) -> None:
 48:         self._token = token.strip()
 49:         self._secret = secret.strip()
 50:         self._base_url = (base_url or "https://api.switch-bot.com").rstrip("/")
 51:         self._retry_attempts = max(int(retry_attempts), 1)
 52:         self._retry_delay_seconds = max(int(retry_delay_seconds), 0)
 53:         self._last_quota: dict[str, int] | None = None
 54:         self._quota_tracker = quota_tracker
 55: 
 56:     def _build_headers(self) -> dict[str, str]:
 57:         if not self._token or not self._secret:
 58:             raise SwitchBotApiError(
 59:                 "Missing SwitchBot credentials. Set SWITCHBOT_TOKEN and SWITCHBOT_SECRET."
 60:             )
 61: 
 62:         t = int(round(time.time() * 1000))
 63:         nonce = str(uuid.uuid4())
 64:         string_to_sign = f"{self._token}{t}{nonce}".encode("utf-8")
 65:         secret_bytes = self._secret.encode("utf-8")
 66:         sign = base64.b64encode(
 67:             hmac.new(secret_bytes, msg=string_to_sign, digestmod=hashlib.sha256).digest()
 68:         ).decode("utf-8")
 69: 
 70:         return {
 71:             "Authorization": self._token,
 72:             "Content-Type": "application/json; charset=utf-8",
 73:             "t": str(t),
 74:             "sign": sign,
 75:             "nonce": nonce,
 76:         }
 77: 
 78:     def _request(self, method: str, path: str, json_body: dict[str, Any] | None = None) -> Any:
 79:         url = f"{self._base_url}{path}"
 80:         last_error: Exception | None = None
 81: 
 82:         for attempt_index in range(self._retry_attempts):
 83:             headers = self._build_headers()
 84:             try:
 85:                 response = requests.request(
 86:                     method=method,
 87:                     url=url,
 88:                     headers=headers,
 89:                     json=json_body,
 90:                     timeout=15,
 91:                 )
 92:             except requests.RequestException as exc:
 93:                 last_error = exc
 94:                 if attempt_index < (self._retry_attempts - 1) and self._retry_delay_seconds > 0:
 95:                     time.sleep(self._retry_delay_seconds)
 96:                     continue
 97: 
 98:                 raise SwitchBotApiError(f"SwitchBot request failed: {exc}") from exc
 99: 
100:             logger.debug(
101:                 "SwitchBot %s %s → HTTP %s headers=%s",
102:                 method,
103:                 path,
104:                 response.status_code,
105:                 dict(response.headers),
106:             )
107: 
108:             retryable_http = response.status_code == 429 or 500 <= response.status_code <= 599
109:             if retryable_http and attempt_index < (self._retry_attempts - 1):
110:                 if self._retry_delay_seconds > 0:
111:                     time.sleep(self._retry_delay_seconds)
112:                 continue
113: 
114:             tracker_updated = self._capture_quota_metadata(response)
115: 
116:             if response.status_code >= 400:
117:                 try:
118:                     data = response.json()
119:                 except ValueError as exc:
120:                     raise SwitchBotApiError(
121:                         f"SwitchBot HTTP {response.status_code}: invalid JSON error payload."
122:                     ) from exc
123:                 raise SwitchBotApiError(f"SwitchBot HTTP {response.status_code}: {data!r}")
124: 
125:             try:
126:                 data = response.json()
127:             except ValueError as exc:
128:                 raise SwitchBotApiError(
129:                     f"Invalid JSON response from SwitchBot ({response.status_code})."
130:                 ) from exc
131: 
132:             if not isinstance(data, dict) or "statusCode" not in data:
133:                 raise SwitchBotApiError(f"Unexpected SwitchBot response: {data!r}")
134: 
135:             status_code = data.get("statusCode")
136:             logger.debug(
137:                 "SwitchBot API payload parsed: statusCode=%s message=%s path=%s",
138:                 status_code,
139:                 data.get("message"),
140:                 path,
141:             )
142:             if status_code == 100:
143:                 if self._quota_tracker and not tracker_updated:
144:                     self._quota_tracker.record_call()
145:                 return data
146: 
147:             if status_code == 190 and attempt_index < (self._retry_attempts - 1):
148:                 if self._retry_delay_seconds > 0:
149:                     time.sleep(self._retry_delay_seconds)
150:                 continue
151: 
152:             raise SwitchBotApiError(f"SwitchBot API error: {data!r}")
153: 
154:         if last_error is not None:
155:             raise SwitchBotApiError(f"SwitchBot request failed: {last_error}") from last_error
156: 
157:         raise SwitchBotApiError("SwitchBot request failed")
158: 
159:     def get_devices(self) -> Any:
160:         return self._request("GET", "/v1.1/devices")
161: 
162:     def get_scenes(self) -> Any:
163:         return self._request("GET", "/v1.1/scenes")
164: 
165:     def get_device_status(self, device_id: str) -> Any:
166:         device_id = device_id.strip()
167:         if not device_id:
168:             raise SwitchBotApiError("Missing device_id")
169: 
170:         return self._request("GET", f"/v1.1/devices/{device_id}/status")
171: 
172:     def send_command(
173:         self,
174:         device_id: str,
175:         command: str,
176:         parameter: str = "default",
177:         command_type: str = "command",
178:     ) -> Any:
179:         device_id = device_id.strip()
180:         if not device_id:
181:             raise SwitchBotApiError("Missing device_id")
182: 
183:         body = {
184:             "command": command,
185:             "parameter": parameter,
186:             "commandType": command_type,
187:         }
188:         return self._request("POST", f"/v1.1/devices/{device_id}/commands", json_body=body)
189: 
190:     def run_scene(self, scene_id: str) -> Any:
191:         scene_id = scene_id.strip()
192:         if not scene_id:
193:             raise SwitchBotApiError("Missing scene_id")
194: 
195:         return self._request("POST", f"/v1.1/scenes/{scene_id}/execute", json_body={})
196: 
197:     def _capture_quota_metadata(self, response: Response) -> bool:
198:         header_map = {key.lower(): value for key, value in response.headers.items()}
199:         limit_raw = (
200:             header_map.get("x-ratelimit-limit")
201:             or header_map.get("x-rate-limit-limit")
202:             or header_map.get("ratelimit-limit")
203:         )
204:         remaining_raw = (
205:             header_map.get("x-ratelimit-remaining")
206:             or header_map.get("x-rate-limit-remaining")
207:             or header_map.get("ratelimit-remaining")
208:         )
209: 
210:         limit = self._safe_int(limit_raw)
211:         remaining = self._safe_int(remaining_raw)
212: 
213:         tracker_updated = False
214:         if limit is None and remaining is None:
215:             if self._quota_tracker:
216:                 self._quota_tracker.record_call()
217:                 tracker_updated = True
218:             logger.debug("SwitchBot quota headers absent on latest response.")
219:             return tracker_updated
220: 
221:         self._last_quota = {}
222:         if limit is not None:
223:             self._last_quota["limit"] = limit
224:         if remaining is not None:
225:             self._last_quota["remaining"] = remaining
226: 
227:         logger.info(
228:             "SwitchBot quota snapshot captured: remaining=%s limit=%s",
229:             remaining if remaining is not None else "unknown",
230:             limit if limit is not None else "unknown",
231:         )
232: 
233:         if self._quota_tracker:
234:             tracker_updated = self._quota_tracker.record_from_headers(limit=limit, remaining=remaining)
235: 
236:         return tracker_updated
237: 
238:     @staticmethod
239:     def _safe_int(value: str | None) -> int | None:
240:         if value is None:
241:             return None
242:         try:
243:             return int(value)
244:         except (TypeError, ValueError):
245:             return None
246: 
247:     def get_last_quota_snapshot(self) -> dict[str, int] | None:
248:         if self._last_quota is None:
249:             return None
250:         return dict(self._last_quota)
```

## File: switchbot_dashboard/static/js/history.js
```javascript
  1: /**
  2:  * History Dashboard JavaScript
  3:  * Handles real-time monitoring charts and data visualization
  4:  */
  5: 
  6: class HistoryDashboard {
  7:     constructor() {
  8:         this.charts = {};
  9:         this.updateInterval = null;
 10:         this.isSmallMobile = window.innerWidth <= 480;
 11:         this.defaultGranularity = this.isSmallMobile ? '5min' : 'minute';
 12:         this.currentFilters = {
 13:             timeRange: '6h',
 14:             granularity: this.defaultGranularity,
 15:             metrics: ['temperature', 'humidity', 'assumed_aircon_power']
 16:         };
 17:         
 18:         this.init();
 19:     }
 20: 
 21:     init() {
 22:         this.applyResponsiveDefaults();
 23:         this.initCharts();
 24:         this.bindEvents();
 25:         this.loadInitialData();
 26:         this.startRealTimeUpdates();
 27:     }
 28: 
 29:     applyResponsiveDefaults() {
 30:         if (!this.isSmallMobile) {
 31:             return;
 32:         }
 33: 
 34:         const granularitySelect = document.getElementById('granularity');
 35:         if (granularitySelect) {
 36:             granularitySelect.value = '5min';
 37:         }
 38:     }
 39: 
 40:     initCharts() {
 41:         // Viewport-based responsive configuration
 42:         const isMobile = window.innerWidth <= 768;
 43:         const isSmallMobile = window.innerWidth <= 480;
 44:         
 45:         const chartOptions = {
 46:             responsive: true,
 47:             maintainAspectRatio: false,
 48:             parsing: false,
 49:             normalized: true,
 50:             animation: false,
 51:             interaction: {
 52:                 mode: 'index',
 53:                 intersect: false,
 54:             },
 55:             plugins: {
 56:                 legend: {
 57:                     position: isMobile ? 'bottom' : 'top',
 58:                     labels: {
 59:                         color: '#e9ecef',
 60:                         font: {
 61:                             size: isSmallMobile ? 10 : (isMobile ? 11 : 12)
 62:                         },
 63:                         padding: isSmallMobile ? 10 : 20,
 64:                         boxWidth: isSmallMobile ? 12 : 15
 65:                     }
 66:                 },
 67:                 tooltip: {
 68:                     backgroundColor: 'rgba(33, 37, 41, 0.9)',
 69:                     titleColor: '#ffffff',
 70:                     bodyColor: '#e9ecef',
 71:                     borderColor: '#495057',
 72:                     borderWidth: 1,
 73:                     titleFont: {
 74:                         size: isSmallMobile ? 11 : 12
 75:                     },
 76:                     bodyFont: {
 77:                         size: isSmallMobile ? 10 : 11
 78:                     },
 79:                     padding: isSmallMobile ? 6 : 10
 80:                 },
 81:                 decimation: {
 82:                     enabled: true,
 83:                     algorithm: 'lttb',
 84:                     samples: 100
 85:                 }
 86:             },
 87:             scales: {
 88:                 x: {
 89:                     type: 'time',
 90:                     time: {
 91:                         displayFormats: {
 92:                             minute: isSmallMobile ? 'H:mm' : 'HH:mm',
 93:                             hour: isSmallMobile ? 'H:mm' : 'HH:mm'
 94:                         }
 95:                     },
 96:                     ticks: {
 97:                         color: '#6c757d',
 98:                         font: {
 99:                             size: isSmallMobile ? 9 : 10
100:                         },
101:                         maxTicksLimit: isSmallMobile ? 6 : 8
102:                     },
103:                     grid: {
104:                         color: 'rgba(108, 117, 125, 0.2)'
105:                     }
106:                 }
107:             }
108:         };
109: 
110:         // Temperature & Humidity Chart
111:         this.charts.tempHumidity = new Chart(document.getElementById('tempHumidityChart'), {
112:             type: 'line',
113:             data: {
114:                 datasets: [
115:                     {
116:                         label: 'Température (°C)',
117:                         data: [],
118:                         borderColor: '#dc3545',
119:                         backgroundColor: 'rgba(220, 53, 69, 0.1)',
120:                         tension: 0.4,
121:                         yAxisID: 'y'
122:                     },
123:                     {
124:                         label: 'Humidité (%)',
125:                         data: [],
126:                         borderColor: '#0d6efd',
127:                         backgroundColor: 'rgba(13, 110, 253, 0.1)',
128:                         tension: 0.4,
129:                         yAxisID: 'y1'
130:                     }
131:                 ]
132:             },
133:             options: {
134:                 ...chartOptions,
135:                 scales: {
136:                     ...chartOptions.scales,
137:                     y: {
138:                         type: 'linear',
139:                         display: true,
140:                         position: 'left',
141:                         title: {
142:                             display: !isMobile,
143:                             text: 'Température (°C)',
144:                             color: '#dc3545',
145:                             font: {
146:                                 size: isSmallMobile ? 9 : 10
147:                             }
148:                         },
149:                         ticks: {
150:                             color: '#6c757d',
151:                             font: {
152:                                 size: isSmallMobile ? 9 : 10
153:                             },
154:                             maxTicksLimit: isSmallMobile ? 4 : 6
155:                         },
156:                         grid: {
157:                             color: 'rgba(108, 117, 125, 0.2)'
158:                         }
159:                     },
160:                     y1: {
161:                         type: 'linear',
162:                         display: true,
163:                         position: 'right',
164:                         title: {
165:                             display: !isMobile,
166:                             text: 'Humidité (%)',
167:                             color: '#0d6efd',
168:                             font: {
169:                                 size: isSmallMobile ? 9 : 10
170:                             }
171:                         },
172:                         ticks: {
173:                             color: '#6c757d',
174:                             font: {
175:                                 size: isSmallMobile ? 9 : 10
176:                             },
177:                             maxTicksLimit: isSmallMobile ? 4 : 6
178:                         },
179:                         grid: {
180:                             drawOnChartArea: false
181:                         }
182:                     }
183:                 }
184:             }
185:         });
186: 
187:         // Aircon State Chart
188:         this.charts.airconState = new Chart(document.getElementById('airconStateChart'), {
189:             type: 'doughnut',
190:             data: {
191:                 labels: ['ON', 'OFF', 'Unknown'],
192:                 datasets: [{
193:                     data: [0, 0, 0],
194:                     backgroundColor: [
195:                         '#198754',
196:                         '#dc3545',
197:                         '#6c757d'
198:                     ],
199:                     borderWidth: 0
200:                 }]
201:             },
202:             options: {
203:                 responsive: true,
204:                 maintainAspectRatio: false,
205:                 plugins: {
206:                     legend: {
207:                         position: 'bottom',
208:                         labels: {
209:                             color: '#e9ecef',
210:                             padding: isSmallMobile ? 10 : 20,
211:                             font: {
212:                                 size: isSmallMobile ? 10 : 11
213:                             },
214:                             boxWidth: isSmallMobile ? 12 : 15
215:                         }
216:                     },
217:                     tooltip: {
218:                         backgroundColor: 'rgba(33, 37, 41, 0.9)',
219:                         titleColor: '#ffffff',
220:                         bodyColor: '#e9ecef',
221:                         borderColor: '#495057',
222:                         borderWidth: 1,
223:                         titleFont: {
224:                             size: isSmallMobile ? 11 : 12
225:                         },
226:                         bodyFont: {
227:                             size: isSmallMobile ? 10 : 11
228:                         },
229:                         padding: isSmallMobile ? 6 : 10
230:                     }
231:                 }
232:             }
233:         });
234:     }
235: 
236:     bindEvents() {
237:         // Filter form submission
238:         document.getElementById('filtersForm').addEventListener('submit', (e) => {
239:             e.preventDefault();
240:             this.applyFilters();
241:         });
242: 
243:         // Time range change
244:         document.getElementById('timeRange').addEventListener('change', (e) => {
245:             const customGroups = ['customStartGroup', 'customEndGroup'];
246:             customGroups.forEach(id => {
247:                 document.getElementById(id).style.display = 
248:                     e.target.value === 'custom' ? 'block' : 'none';
249:             });
250:         });
251: 
252:         // Reset zoom button
253:         document.getElementById('resetZoomTemp').addEventListener('click', () => {
254:             this.charts.tempHumidity.resetZoom();
255:         });
256: 
257:         // Refresh latest records
258:         document.getElementById('refreshLatest').addEventListener('click', () => {
259:             this.loadLatestRecords();
260:         });
261: 
262:         // Metric checkboxes
263:         document.querySelectorAll('.metric-checkboxes input').forEach(checkbox => {
264:             checkbox.addEventListener('change', () => {
265:                 this.updateMetrics();
266:             });
267:         });
268:     }
269: 
270:     async loadInitialData() {
271:         try {
272:             const [historyData, aggregates, latestRecords] = await Promise.all([
273:                 this.loadHistoryData(),
274:                 this.loadAggregates(),
275:                 this.loadLatestRecords()
276:             ]);
277:             
278:             // Check if data is mocked (handle undefined safely)
279:             const isMockData = (historyData && historyData.mock) || 
280:                               (aggregates && aggregates.mock) || 
281:                               (latestRecords && latestRecords.mock);
282:             if (isMockData) {
283:                 this.showMockDataWarning();
284:             }
285:             
286:             this.updateStatus('success', 'Données chargées');
287:         } catch (error) {
288:             console.error('Error loading initial data:', error);
289:             this.updateStatus('error', 'Erreur de chargement');
290:         }
291:     }
292: 
293:     showMockDataWarning() {
294:         // Add a warning banner for mock data
295:         const banner = document.createElement('div');
296:         banner.className = 'alert alert-warning alert-dismissible fade show mb-3';
297:         banner.innerHTML = `
298:             <strong>⚠️ Mode démonstration</strong><br>
299:             Le service d'historique n'est pas disponible. Données simulées affichées.
300:             <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
301:         `;
302:         
303:         const container = document.querySelector('.container');
304:         container.insertBefore(banner, container.firstChild);
305:     }
306: 
307:     async loadHistoryData() {
308:         const params = new URLSearchParams({
309:             start: this.getTimeRangeStart(),
310:             end: new Date().toISOString(),
311:             granularity: this.currentFilters.granularity,
312:             metrics: this.currentFilters.metrics
313:         });
314: 
315:         try {
316:             const response = await fetch(`/history/api/data?${params}`);
317:             if (!response.ok) {
318:                 throw new Error(`HTTP ${response.status}: ${response.statusText}`);
319:             }
320: 
321:             const data = await response.json();
322:             this.updateCharts(data.data || []);
323:             return data; // Return the full response for mock checking
324:         } catch (error) {
325:             console.error('Failed to load history data:', error);
326:             this.updateStatus('error', 'Erreur de chargement des données');
327:             this.renderChartErrorState(error);
328:             throw error;
329:         }
330:     }
331: 
332:     renderChartErrorState(error) {
333:         document.querySelectorAll('.chart-container').forEach((container) => {
334:             container.innerHTML = `
335:                 <div class="d-flex flex-column align-items-center justify-content-center text-muted py-4">
336:                     <div class="fs-3 mb-2">⚠️</div>
337:                     <div class="text-center">Impossible de charger les données</div>
338:                     <small class="d-block mt-2">${error.message}</small>
339:                 </div>
340:             `;
341:         });
342:     }
343: 
344:     async loadAggregates() {
345:         const response = await fetch('/history/api/aggregates?period_hours=6');
346:         if (!response.ok) throw new Error('Failed to load aggregates');
347:         
348:         const data = await response.json();
349:         this.updateStatusCards(data.aggregates || {});
350:         return data; // Return the full response for mock checking
351:     }
352: 
353:     async loadLatestRecords() {
354:         const response = await fetch('/history/api/latest?limit=10');
355:         if (!response.ok) throw new Error('Failed to load latest records');
356:         
357:         const data = await response.json();
358:         this.updateLatestTable(data.latest || []);
359:         return data; // Return the full response for mock checking
360:     }
361: 
362:     updateCharts(historyData) {
363:         if (!historyData || historyData.length === 0) return;
364: 
365:         // Update temperature & humidity chart
366:         const tempData = historyData.map(d => ({
367:             x: d.timestamp,
368:             y: d.temperature
369:         })).filter(d => d.y !== null);
370: 
371:         const humidityData = historyData.map(d => ({
372:             x: d.timestamp,
373:             y: d.humidity
374:         })).filter(d => d.y !== null);
375: 
376:         this.charts.tempHumidity.data.datasets[0].data = tempData;
377:         this.charts.tempHumidity.data.datasets[1].data = humidityData;
378:         this.charts.tempHumidity.update('none');
379: 
380:         // Update aircon state chart
381:         const airconStates = historyData.reduce((acc, d) => {
382:             const state = d.assumed_aircon_power || 'unknown';
383:             acc[state] = (acc[state] || 0) + 1;
384:             return acc;
385:         }, {});
386: 
387:         this.charts.airconState.data.datasets[0].data = [
388:             airconStates['on'] || 0,
389:             airconStates['off'] || 0,
390:             airconStates['unknown'] || 0
391:         ];
392:         this.charts.airconState.update('none');
393:     }
394: 
395:     updateStatusCards(aggregates) {
396:         console.log('updateStatusCards called with:', aggregates);
397:         
398:         const avgTemp = aggregates.avg_temperature ? parseFloat(aggregates.avg_temperature).toFixed(1) : '--';
399:         const avgHumidity = aggregates.avg_humidity ? parseFloat(aggregates.avg_humidity).toFixed(1) : '--';
400:         
401:         console.log('Processed values - Temp:', avgTemp, 'Humidity:', avgHumidity);
402:         
403:         const tempElement = document.getElementById('avgTemp');
404:         const humidityElement = document.getElementById('avgHumidity');
405:         
406:         console.log('Elements found:', !!tempElement, !!humidityElement);
407:         
408:         if (tempElement) tempElement.textContent = avgTemp;
409:         if (humidityElement) humidityElement.textContent = avgHumidity;
410:     }
411: 
412:     updateLatestTable(latestRecords) {
413:         const tbody = document.getElementById('latestTableBody');
414:         
415:         if (!latestRecords || latestRecords.length === 0) {
416:             tbody.innerHTML = `
417:                 <tr>
418:                     <td colspan="5" class="text-center text-muted">
419:                         Aucun enregistrement trouvé
420:                     </td>
421:                 </tr>
422:             `;
423:             return;
424:         }
425: 
426:         tbody.innerHTML = latestRecords.map(record => {
427:             const timestamp = new Date(record.timestamp).toLocaleString('fr-FR');
428:             const temp = record.temperature ? `${record.temperature}°C` : '--';
429:             const humidity = record.humidity ? `${record.humidity}%` : '--';
430:             const airconState = this.formatAirconState(record.assumed_aircon_power);
431:             const action = record.last_action || '--';
432:             
433:             return `
434:                 <tr>
435:                     <td>${timestamp}</td>
436:                     <td>${temp}</td>
437:                     <td>${humidity}</td>
438:                     <td>${airconState}</td>
439:                     <td>${action}</td>
440:                 </tr>
441:             `;
442:         }).join('');
443:     }
444: 
445:     formatAirconState(state) {
446:         const stateMap = {
447:             'on': '<span class="badge bg-success">ON</span>',
448:             'off': '<span class="badge bg-danger">OFF</span>',
449:             'unknown': '<span class="badge bg-secondary">?</span>'
450:         };
451:         return stateMap[state] || stateMap['unknown'];
452:     }
453: 
454:     getTimeRangeStart() {
455:         const now = new Date();
456:         const range = this.currentFilters.timeRange;
457:         
458:         switch (range) {
459:             case '1h':
460:                 return new Date(now.getTime() - 60 * 60 * 1000).toISOString();
461:             case '6h':
462:                 return new Date(now.getTime() - 6 * 60 * 60 * 1000).toISOString();
463:             case '24h':
464:                 return new Date(now.getTime() - 24 * 60 * 60 * 1000).toISOString();
465:             case 'custom':
466:                 const customStart = document.getElementById('customStart').value;
467:                 return customStart ? new Date(customStart).toISOString() : this.getTimeRangeStart();
468:             default:
469:                 return this.getTimeRangeStart();
470:         }
471:     }
472: 
473:     applyFilters() {
474:         const timeRange = document.getElementById('timeRange').value;
475:         const granularity = document.getElementById('granularity').value;
476:         const metrics = Array.from(document.querySelectorAll('.metric-checkboxes input:checked'))
477:             .map(cb => cb.value);
478: 
479:         this.currentFilters = { timeRange, granularity, metrics };
480:         this.loadHistoryData();
481:         this.updateStatus('loading', 'Application des filtres...');
482:     }
483: 
484:     updateMetrics() {
485:         const checkedMetrics = Array.from(document.querySelectorAll('.metric-checkboxes input:checked'))
486:             .map(cb => cb.value);
487:         this.currentFilters.metrics = checkedMetrics;
488:         this.loadHistoryData();
489:     }
490: 
491:     updateStatus(type, message) {
492:         const indicator = document.getElementById('statusIndicator');
493:         const text = document.getElementById('statusText');
494:         const lastUpdate = document.getElementById('lastUpdate');
495: 
496:         // Update indicator
497:         indicator.className = 'status-indicator';
498:         if (type === 'success') {
499:             indicator.classList.add('status-success');
500:         } else if (type === 'error') {
501:             indicator.classList.add('status-error');
502:         } else if (type === 'loading') {
503:             indicator.classList.add('status-loading');
504:         }
505: 
506:         // Update text
507:         text.textContent = message;
508:         lastUpdate.textContent = new Date().toLocaleTimeString('fr-FR');
509:     }
510: 
511:     startRealTimeUpdates() {
512:         // Update every 30 seconds
513:         this.updateInterval = setInterval(() => {
514:             this.loadHistoryData();
515:             this.loadAggregates();
516:             this.loadLatestRecords();
517:         }, 30000);
518:     }
519: 
520:     destroy() {
521:         if (this.updateInterval) {
522:             clearInterval(this.updateInterval);
523:         }
524:         
525:         // Destroy charts
526:         Object.values(this.charts).forEach(chart => {
527:             if (chart) chart.destroy();
528:         });
529:     }
530: }
531: 
532: // Initialize dashboard when DOM is ready
533: document.addEventListener('DOMContentLoaded', () => {
534:     window.historyDashboard = new HistoryDashboard();
535: });
536: 
537: // Cleanup on page unload
538: window.addEventListener('beforeunload', () => {
539:     if (window.historyDashboard) {
540:         window.historyDashboard.destroy();
541:     }
542: });
```

## File: switchbot_dashboard/history_service.py
```python
  1: from __future__ import annotations
  2: 
  3: import datetime as dt
  4: import json
  5: import logging
  6: import threading
  7: from typing import Any, Optional
  8: 
  9: import psycopg
 10: from psycopg import sql
 11: from psycopg.rows import dict_row
 12: from psycopg.types.json import Jsonb
 13: from psycopg_pool import ConnectionPool
 14: 
 15: from .postgres_store import PostgresStoreError
 16: 
 17: 
 18: class HistoryServiceError(RuntimeError):
 19:     """Raised when history service operations fail."""
 20: 
 21: 
 22: class HistoryService:
 23:     """Service for collecting and retrieving historical monitoring data."""
 24: 
 25:     def __init__(
 26:         self,
 27:         connection_pool: ConnectionPool,
 28:         *,
 29:         logger: logging.Logger,
 30:         retention_hours: int = 6,
 31:         batch_size: int = 4,
 32:         flush_interval_seconds: int = 60,
 33:     ) -> None:
 34:         """
 35:         Initialize history service with PostgreSQL connection pool.
 36: 
 37:         Args:
 38:             connection_pool: PostgreSQL connection pool from PostgresStore
 39:             logger: Logger instance for error reporting
 40:             retention_hours: Data retention period (default: 6 hours for Neon PITR)
 41:             batch_size: Number of records to buffer before flushing (default: 4)
 42:             flush_interval_seconds: Maximum seconds to keep buffered data before flushing
 43:         """
 44:         self._pool = connection_pool
 45:         self._logger = logger
 46:         self._retention_hours = retention_hours
 47:         self._batch_size = max(1, batch_size)
 48:         self._flush_interval_seconds = max(0, flush_interval_seconds)
 49:         self._pending_records: list[tuple[Any, ...]] = []
 50:         self._pending_lock = threading.Lock()
 51:         self._flush_timer: threading.Timer | None = None
 52:         self._ensure_table_exists()
 53: 
 54:     def _ensure_table_exists(self) -> None:
 55:         """Create state_history table if it doesn't exist."""
 56:         create_table_query = sql.SQL("""
 57:             CREATE TABLE IF NOT EXISTS state_history (
 58:                 id SERIAL PRIMARY KEY,
 59:                 timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
 60:                 temperature DECIMAL(4,1),
 61:                 humidity DECIMAL(4,1),
 62:                 assumed_aircon_power VARCHAR(10),
 63:                 last_action VARCHAR(50),
 64:                 api_requests_today INTEGER DEFAULT 0,
 65:                 error_count INTEGER DEFAULT 0,
 66:                 last_temperature_stale BOOLEAN DEFAULT FALSE,
 67:                 timezone VARCHAR(50) DEFAULT 'UTC',
 68:                 metadata JSONB DEFAULT '{}'
 69:             );
 70:             CREATE INDEX IF NOT EXISTS idx_state_history_timestamp ON state_history(timestamp DESC);
 71:             CREATE INDEX IF NOT EXISTS idx_state_history_aircon_power ON state_history(assumed_aircon_power);
 72:             CREATE INDEX IF NOT EXISTS idx_state_history_metadata ON state_history USING GIN(metadata);
 73:         """)
 74: 
 75:         try:
 76:             with self._pool.connection() as conn:
 77:                 with conn.cursor() as cur:
 78:                     cur.execute(create_table_query)
 79:                     conn.commit()
 80:                     self._logger.info("[history] Table state_history ensured")
 81:         except Exception as exc:
 82:             self._logger.error("[history] Failed to create table (%s)", exc)
 83:             raise HistoryServiceError("Failed to ensure history table exists") from exc
 84: 
 85:     def record_state(
 86:         self,
 87:         state_data: dict[str, Any],
 88:         timezone: str = "UTC",
 89:         *,
 90:         force_flush: bool = False,
 91:     ) -> None:
 92:         record_tuple = self._build_record_tuple(state_data, timezone)
 93: 
 94:         with self._pending_lock:
 95:             self._pending_records.append(record_tuple)
 96: 
 97:             if len(self._pending_records) >= self._batch_size:
 98:                 self._flush_pending_records_locked()
 99:             else:
100:                 self._schedule_flush_timer_locked()
101: 
102:         if force_flush:
103:             self.flush_pending_records(force=True)
104: 
105:     def get_history(
106:         self,
107:         start: dt.datetime,
108:         end: dt.datetime,
109:         metrics: Optional[list[str]] = None,
110:         granularity: str = "minute",
111:         limit: int = 1000,
112:     ) -> list[dict[str, Any]]:
113:         if metrics is None:
114:             metrics = [
115:                 "timestamp",
116:                 "temperature",
117:                 "humidity",
118:                 "assumed_aircon_power",
119:                 "last_action",
120:                 "api_requests_today",
121:                 "error_count",
122:                 "last_temperature_stale",
123:             ]
124: 
125:         # Build time bucket expression based on granularity
126:         time_bucket = self._get_time_bucket_expression(granularity)
127: 
128:         # Build SELECT clause
129:         select_fields = []
130:         timestamp_included = False
131:         
132:         for metric in metrics:
133:             if metric == "timestamp":
134:                 select_fields.append(sql.SQL("date_trunc(%s, timestamp) as timestamp"))
135:                 timestamp_included = True
136:             elif metric in ["temperature", "humidity"]:
137:                 select_fields.append(sql.SQL("AVG({}) as {}").format(
138:                     sql.Identifier(metric), sql.Identifier(metric)
139:                 ))
140:             elif metric == "assumed_aircon_power":
141:                 select_fields.append(sql.SQL("MODE() WITHIN GROUP (ORDER BY assumed_aircon_power) as assumed_aircon_power"))
142:             elif metric == "last_action":
143:                 select_fields.append(sql.SQL("MODE() WITHIN GROUP (ORDER BY last_action) as last_action"))
144:             elif metric == "api_requests_today":
145:                 select_fields.append(sql.SQL("MAX(api_requests_today) as api_requests_today"))
146:             elif metric == "error_count":
147:                 select_fields.append(sql.SQL("SUM(error_count) as error_count"))
148:             elif metric == "last_temperature_stale":
149:                 select_fields.append(sql.SQL("BOOL_OR(last_temperature_stale) as last_temperature_stale"))
150: 
151:         # Always include timestamp for ordering
152:         if not timestamp_included:
153:             select_fields.insert(0, sql.SQL("date_trunc(%s, timestamp) as timestamp"))
154: 
155:         # If no metrics specified, return empty result
156:         if not select_fields:
157:             self._logger.warning("[history] No valid metrics specified: %s", metrics)
158:             return []
159: 
160:         # Build query using subqueries for each metric to avoid GROUP BY issues
161:         if not metrics:
162:             self._logger.warning("[history] No valid metrics specified: %s", metrics)
163:             return []
164: 
165:         # For now, implement a simple approach without aggregation
166:         # Get raw data and let frontend handle the aggregation
167:         select_fields_raw = []
168:         
169:         # Always include timestamp
170:         select_fields_raw.append(sql.SQL("timestamp"))
171:         
172:         for metric in metrics:
173:             if metric in ["temperature", "humidity", "assumed_aircon_power", "last_action", "api_requests_today", "error_count", "last_temperature_stale"]:
174:                 select_fields_raw.append(sql.Identifier(metric))
175: 
176:         query = sql.SQL("""
177:             SELECT {}
178:             FROM state_history
179:             WHERE timestamp >= %s AND timestamp < %s
180:             ORDER BY timestamp DESC
181:             LIMIT %s
182:         """).format(
183:             sql.SQL(", ").join(select_fields_raw)
184:         )
185: 
186:         try:
187:             with self._pool.connection() as conn:
188:                 with conn.cursor(row_factory=dict_row) as cur:
189:                     # Simple parameters: start + end + limit
190:                     params = [start, end, limit]
191:                     cur.execute(query, params)
192:                     results = cur.fetchall()
193: 
194:                     # Convert datetime objects to ISO strings for JSON serialization
195:                     for result in results:
196:                         if "timestamp" in result and result["timestamp"]:
197:                             result["timestamp"] = result["timestamp"].isoformat()
198: 
199:                     self._logger.debug("[history] Retrieved %d records", len(results))
200:                     return results
201: 
202:         except Exception as exc:
203:             self._logger.error("[history] Failed to retrieve history (%s)", exc)
204:             raise HistoryServiceError("Failed to retrieve historical data") from exc
205: 
206:     def get_aggregates(self, period_hours: int = 1) -> dict[str, Any]:
207:         """
208:         Get aggregated statistics for a recent period.
209: 
210:         Args:
211:             period_hours: Number of hours to aggregate (default: 1)
212: 
213:         Returns:
214:             Dictionary with aggregated metrics
215: 
216:         Raises:
217:             HistoryServiceError: If aggregation fails
218:         """
219:         query = sql.SQL("""
220:             SELECT 
221:                 COUNT(*) as total_records,
222:                 AVG(temperature) as avg_temperature,
223:                 MIN(temperature) as min_temperature,
224:                 MAX(temperature) as max_temperature,
225:                 AVG(humidity) as avg_humidity,
226:                 MIN(humidity) as min_humidity,
227:                 MAX(humidity) as max_humidity,
228:                 MODE() WITHIN GROUP (ORDER BY assumed_aircon_power) as common_aircon_state,
229:                 COUNT(DISTINCT last_action) as distinct_actions,
230:                 SUM(error_count) as total_errors,
231:                 MAX(api_requests_today) as max_api_requests
232:             FROM state_history
233:             WHERE timestamp >= NOW() - make_interval(hours => %s)
234:         """)
235: 
236:         try:
237:             with self._pool.connection() as conn:
238:                 with conn.cursor(row_factory=dict_row) as cur:
239:                     cur.execute(query, (period_hours,))
240:                     result = cur.fetchone()
241:                     return result or {}
242: 
243:         except Exception as exc:
244:             self._logger.error("[history] Failed to get aggregates (%s)", exc)
245:             raise HistoryServiceError("Failed to get aggregated statistics") from exc
246: 
247:     def cleanup_old_records(self) -> int:
248:         delete_query = sql.SQL("""
249:             DELETE FROM state_history
250:             WHERE timestamp < NOW() - make_interval(hours => %s)
251:         """)
252: 
253:         try:
254:             with self._pool.connection() as conn:
255:                 with conn.cursor() as cur:
256:                     cur.execute(delete_query, (self._retention_hours,))
257:                     deleted_count = cur.rowcount
258:                     conn.commit()
259:                     self._logger.info("[history] Cleaned up %d old records", deleted_count)
260:                     return deleted_count
261: 
262:         except Exception as exc:
263:             self._logger.error("[history] Failed to cleanup old records (%s)", exc)
264:             raise HistoryServiceError("Failed to cleanup old records") from exc
265: 
266:     def flush_pending_records(self, *, force: bool = False) -> int:
267:         """Flush buffered records to PostgreSQL."""
268:         with self._pending_lock:
269:             if not self._pending_records:
270:                 return 0
271: 
272:             if not force and len(self._pending_records) < self._batch_size:
273:                 return 0
274: 
275:             return self._flush_pending_records_locked()
276: 
277:     def _build_record_tuple(
278:         self,
279:         state_data: dict[str, Any],
280:         timezone: str,
281:     ) -> tuple[Any, ...]:
282:         temperature = state_data.get("last_temperature")
283:         humidity = state_data.get("last_humidity")
284:         aircon_power = state_data.get("assumed_aircon_power", "unknown")
285:         last_action = state_data.get("last_action")
286:         api_requests = state_data.get("api_requests_today", 0)
287:         error_count = state_data.get("error_count", 0)
288:         temp_stale = state_data.get("last_temperature_stale", False)
289: 
290:         metadata = {
291:             "last_read_at": state_data.get("last_read_at"),
292:             "last_tick": state_data.get("last_tick"),
293:             "automation_active": state_data.get("automation_active"),
294:             "pending_off_repeat": state_data.get("pending_off_repeat"),
295:         }
296: 
297:         return (
298:             temperature,
299:             humidity,
300:             aircon_power,
301:             last_action,
302:             api_requests,
303:             error_count,
304:             temp_stale,
305:             timezone,
306:             Jsonb(metadata),
307:         )
308: 
309:     def _schedule_flush_timer_locked(self) -> None:
310:         """Schedule a timer-based flush if needed (lock must be held)."""
311:         if self._flush_interval_seconds <= 0:
312:             return
313: 
314:         if self._flush_timer is not None:
315:             return
316: 
317:         timer = threading.Timer(self._flush_interval_seconds, self._flush_due)
318:         timer.daemon = True
319:         timer.start()
320:         self._flush_timer = timer
321: 
322:     def _flush_due(self) -> None:
323:         """Flush callback triggered by the timer."""
324:         with self._pending_lock:
325:             self._flush_timer = None
326:             if not self._pending_records:
327:                 return
328: 
329:             try:
330:                 self._flush_pending_records_locked()
331:             except HistoryServiceError as exc:
332:                 self._logger.error("[history] Timed flush failed (%s)", exc)
333: 
334:     def _cancel_flush_timer_locked(self) -> None:
335:         """Cancel the scheduled flush timer if it exists."""
336:         if self._flush_timer is not None:
337:             self._flush_timer.cancel()
338:             self._flush_timer = None
339: 
340:     def _flush_pending_records_locked(self) -> int:
341:         """Flush pending records to PostgreSQL (lock must be held)."""
342:         if not self._pending_records:
343:             return 0
344: 
345:         records = list(self._pending_records)
346:         self._pending_records.clear()
347:         self._cancel_flush_timer_locked()
348: 
349:         column_count = len(records[0])
350:         placeholders = "(" + ", ".join(["%s"] * column_count) + ")"
351:         values_segment = ", ".join([placeholders] * len(records))
352:         insert_query = sql.SQL(
353:             """
354:             INSERT INTO state_history (
355:                 temperature, humidity, assumed_aircon_power, last_action,
356:                 api_requests_today, error_count, last_temperature_stale,
357:                 timezone, metadata
358:             ) VALUES {}
359:             """
360:         ).format(sql.SQL(values_segment))
361:         flat_params: list[Any] = []
362:         for record in records:
363:             flat_params.extend(record)
364: 
365:         try:
366:             with self._pool.connection() as conn:
367:                 with conn.cursor() as cur:
368:                     cur.execute(insert_query, flat_params)
369:                     conn.commit()
370:                     self._logger.debug(
371:                         "[history] Flushed %d buffered records", len(records)
372:                     )
373:         except Exception as exc:
374:             self._logger.error("[history] Failed to flush records (%s)", exc)
375:             raise HistoryServiceError("Failed to flush buffered records") from exc
376: 
377:         return len(records)
378: 
379:     def _get_time_bucket_expression(self, granularity: str) -> sql.SQL:
380:         """Get PostgreSQL time bucket expression for given granularity."""
381:         granularity_map = {
382:             "minute": "minute",
383:             "5min": "5 minutes",
384:             "15min": "15 minutes",
385:             "hour": "hour",
386:         }
387:         bucket = granularity_map.get(granularity, "minute")
388:         return sql.SQL("date_trunc(%s, timestamp)").format(sql.Literal(bucket))
389: 
390:     def get_latest_records(self, limit: int = 10) -> list[dict[str, Any]]:
391:         """
392:         Get the most recent records.
393: 
394:         Args:
395:             limit: Maximum number of records to return
396: 
397:         Returns:
398:             List of recent records
399: 
400:         Raises:
401:             HistoryServiceError: If retrieval fails
402:         """
403:         query = sql.SQL("""
404:             SELECT *
405:             FROM state_history
406:             ORDER BY timestamp DESC
407:             LIMIT %s
408:         """)
409: 
410:         try:
411:             with self._pool.connection() as conn:
412:                 with conn.cursor(row_factory=dict_row) as cur:
413:                     cur.execute(query, (limit,))
414:                     results = cur.fetchall()
415: 
416:                     # Convert datetime objects to ISO strings
417:                     for result in results:
418:                         if "timestamp" in result and result["timestamp"]:
419:                             result["timestamp"] = result["timestamp"].isoformat()
420:                         if "metadata" in result and result["metadata"]:
421:                             result["metadata"] = dict(result["metadata"])
422: 
423:                     return results
424: 
425:         except Exception as exc:
426:             self._logger.error("[history] Failed to get latest records (%s)", exc)
427:             raise HistoryServiceError("Failed to get latest records") from exc
```

## File: switchbot_dashboard/static/css/index.css
```css
  1: .scene-action {
  2:   text-align: left;
  3:   padding: 1rem 1.15rem;
  4:   display: flex;
  5:   flex-direction: column;
  6:   gap: 0.45rem;
  7:   border-color: rgba(255, 255, 255, 0.25);
  8:   transition: transform var(--sb-transition-fast), 
  9:               box-shadow var(--sb-transition-fast),
 10:               background var(--sb-transition-normal);
 11:   position: relative;
 12:   overflow: hidden;
 13: }
 14: 
 15: .scene-action:hover {
 16:   transform: translateY(var(--sb-translate-hover)) scale(var(--sb-scale-hover));
 17:   box-shadow: var(--sb-glass-shadow-hover);
 18:   background: var(--sb-glass-bg-hover);
 19: }
 20: 
 21: .scene-action:active {
 22:   transform: scale(var(--sb-scale-active));
 23:   transition: transform var(--sb-transition-fast);
 24: }
 25: 
 26: .scene-action:focus-visible {
 27:   outline: 2px solid var(--sb-accent);
 28:   outline-offset: 2px;
 29: }
 30: 
 31: /* Success state animation */
 32: .scene-action.sb-success-flash {
 33:   animation: sb-success-flash 0.8s ease-out;
 34: }
 35: 
 36: /* Cooldown state */
 37: .scene-action.sb-cooldown {
 38:   pointer-events: none;
 39:   opacity: 0.7;
 40: }
 41: 
 42: .scene-action.sb-cooldown::after {
 43:   content: '';
 44:   position: absolute;
 45:   top: 50%;
 46:   left: 50%;
 47:   width: 100%;
 48:   height: 100%;
 49:   border: 2px solid var(--sb-muted);
 50:   border-radius: inherit;
 51:   transform: translate(-50%, -50%);
 52:   animation: sb-cooldown-ring 2s linear infinite;
 53: }
 54: 
 55: /* Loading state */
 56: .scene-action.sb-loading {
 57:   background: rgba(255, 255, 255, 0.08);
 58: }
 59: 
 60: .scene-action.sb-loading::before {
 61:   content: '';
 62:   position: absolute;
 63:   top: 0;
 64:   left: -100%;
 65:   width: 100%;
 66:   height: 100%;
 67:   background: linear-gradient(
 68:     90deg,
 69:     transparent,
 70:     rgba(255, 255, 255, 0.1),
 71:     transparent
 72:   );
 73:   animation: sb-shimmer 1.5s infinite;
 74: }
 75: 
 76: .scene-action[disabled],
 77: .scene-action[aria-disabled="true"] {
 78:   opacity: 0.65;
 79: }
 80: 
 81: .scene-header {
 82:   display: flex;
 83:   align-items: center;
 84:   gap: 0.75rem;
 85: }
 86: 
 87: .scene-icon {
 88:   width: 2.5rem;
 89:   height: 2.5rem;
 90:   border-radius: 0.95rem;
 91:   background: rgba(255, 255, 255, 0.08);
 92:   display: inline-flex;
 93:   align-items: center;
 94:   justify-content: center;
 95:   color: var(--sb-text);
 96:   transition: transform var(--sb-transition-fast), 
 97:               background var(--sb-transition-normal);
 98: }
 99: 
100: .scene-icon:hover {
101:   transform: scale(1.1);
102: }
103: 
104: .scene-icon svg {
105:   width: 1.6rem;
106:   height: 1.6rem;
107:   transition: transform var(--sb-transition-fast);
108: }
109: 
110: .scene-action:hover .scene-icon svg {
111:   transform: scale(1.05);
112: }
113: 
114: .scene-icon--winter {
115:   background: rgba(110, 231, 183, 0.15);
116:   color: var(--sb-success);
117: }
118: 
119: .scene-icon--summer {
120:   background: rgba(246, 195, 67, 0.15);
121:   color: var(--sb-warning);
122: }
123: 
124: .scene-icon--fan {
125:   background: rgba(75, 201, 240, 0.15);
126:   color: var(--sb-info);
127: }
128: 
129: .scene-icon--off {
130:   background: rgba(255, 107, 129, 0.15);
131:   color: var(--sb-danger);
132: }
133: 
134: /* Pulse animation for active scene icons */
135: .scene-icon.sb-pulse {
136:   animation: sb-pulse 0.6s ease-in-out;
137: }
138: 
139: .scene-title {
140:   font-weight: 600;
141: }
142: 
143: .scene-status {
144:   display: inline-flex;
145:   align-items: center;
146:   gap: 0.3rem;
147: }
148: 
149: .scene-status::before {
150:   content: "";
151:   width: 0.4rem;
152:   height: 0.4rem;
153:   border-radius: 50%;
154:   background: currentColor;
155:   opacity: 0.7;
156: }
157: 
158: /* Thumb Zone Optimization */
159: .scene-actions-wrapper {
160:   display: none;
161: }
162: 
163: @media (max-width: 767px) {
164:   .scene-actions-wrapper {
165:     display: block;
166:     position: sticky;
167:     bottom: 1rem;
168:     background: var(--sb-glass-bg);
169:     backdrop-filter: blur(20px);
170:     border: 1px solid var(--sb-glass-border);
171:     border-radius: 1.25rem;
172:     padding: 1rem;
173:     margin: 1rem -1rem -1rem;
174:     box-shadow: var(--sb-glass-shadow);
175:     z-index: 10;
176:   }
177:   
178:   .scene-actions-container {
179:     display: flex;
180:     flex-direction: column;
181:     gap: var(--spacing-md);
182:   }
183:   
184:   .scene-action {
185:     min-height: 56px;
186:     padding: 1rem;
187:   }
188:   
189:   .scene-icon {
190:     width: 2.75rem;
191:     height: 2.75rem;
192:   }
193: }
194: 
195: .status-grid {
196:   display: grid;
197:   grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
198:   gap: 1rem;
199: }
200: 
201: .status-item {
202:   border: 1px solid var(--sb-outline);
203:   border-radius: 1rem;
204:   padding: 0.85rem 1rem;
205:   background: rgba(255, 255, 255, 0.03);
206:   display: flex;
207:   flex-direction: column;
208:   gap: 0.25rem;
209:   transition: transform var(--sb-transition-fast), 
210:               box-shadow var(--sb-transition-fast),
211:               background var(--sb-transition-normal);
212: }
213: 
214: .status-item:hover {
215:   transform: translateY(var(--sb-translate-hover)) scale(var(--sb-scale-hover));
216:   box-shadow: var(--sb-glass-shadow-hover);
217:   background: var(--sb-glass-bg-hover);
218: }
219: 
220: .status-item:focus-visible {
221:   outline: 2px solid var(--sb-accent);
222:   outline-offset: 2px;
223: }
224: 
225: /* Loading state for status items */
226: .status-item.sb-loading {
227:   background: rgba(255, 255, 255, 0.05);
228: }
229: 
230: /* Data update animation for values */
231: .status-value.sb-data-update {
232:   animation: sb-data-update 0.4s ease-out;
233: }
234: 
235: .status-label {
236:   font-size: 0.75rem;
237:   text-transform: uppercase;
238:   letter-spacing: 0.08em;
239:   color: var(--sb-muted);
240: }
241: 
242: .status-value {
243:   font-size: 1.05rem;
244:   font-weight: 600;
245:   color: var(--sb-text);
246:   transition: color var(--sb-transition-normal), 
247:               transform var(--sb-transition-fast);
248: }
249: 
250: /* Temperature change animation */
251: .status-value.sb-temp-change {
252:   animation: sb-temp-change 1s ease-in-out;
253: }
254: 
255: /* Status indicator with pulse */
256: .scene-status.sb-status-indicator {
257:   position: relative;
258: }
259: 
260: .scene-status.sb-status-indicator::before {
261:   content: '';
262:   position: absolute;
263:   top: 50%;
264:   left: -12px;
265:   width: 6px;
266:   height: 6px;
267:   border-radius: 50%;
268:   background: currentColor;
269:   transform: translate(-50%, -50%);
270:   animation: sb-status-pulse 2s infinite;
271: }
272: 
273: /* Data value update animation */
274: .status-value.sb-data-update {
275:   animation: sb-data-update 0.4s ease-out;
276: }
277: 
278: /* Temperature specific styles */
279: .temperature-value {
280:   position: relative;
281:   display: inline-flex;
282:   align-items: baseline;
283:   gap: 0.2rem;
284: }
285: 
286: .temperature-value::after {
287:   content: '°C';
288:   font-size: 0.8em;
289:   opacity: 0.7;
290: }
291: 
292: .temperature-value.sb-temp-change::after {
293:   animation: sb-temp-change 1s ease-in-out;
294: }
295: 
296: /* Humidity specific styles */
297: .humidity-value::after {
298:   content: '%';
299:   font-size: 0.8em;
300:   opacity: 0.7;
301: }
302: 
303: /* API quota animations */
304: .quota-value {
305:   position: relative;
306:   display: inline-flex;
307:   align-items: center;
308:   gap: 0.3rem;
309: }
310: 
311: .quota-value.sb-warning {
312:   color: var(--sb-warning);
313:   animation: sb-pulse 1s ease-in-out infinite;
314: }
315: 
316: .quota-value.sb-danger {
317:   color: var(--sb-danger);
318:   animation: sb-pulse 0.8s ease-in-out infinite;
319: }
320: 
321: .status-value--muted {
322:   color: var(--sb-muted);
323:   font-weight: 500;
324: }
325: 
326: .status-badge {
327:   align-self: flex-start;
328: }
329: 
330: /* Status Grid Mobile Fix */
331: @media (max-width: 480px) {
332:   .status-grid {
333:     grid-template-columns: 1fr;
334:     gap: 0.75rem;
335:   }
336:   .status-item {
337:     padding: 1rem;
338:   }
339: }
```

## File: switchbot_dashboard/static/css/theme.css
```css
  1: :root {
  2:   color-scheme: dark;
  3:   --sb-bg: #030712;
  4:   --sb-gradient-start: #030712;
  5:   --sb-gradient-mid: #0a1227;
  6:   --sb-gradient-end: #101c35;
  7:   --sb-card: rgba(9, 14, 30, 0.92);
  8:   --sb-card-border: rgba(138, 180, 255, 0.2);
  9:   --sb-text: #f4f7ff;
 10:   --sb-muted: #aeb8d3;
 11:   --sb-accent: #8ab4ff;
 12:   --sb-accent-contrast: #051434;
 13:   --sb-shadow: 0 25px 60px rgba(2, 7, 20, 0.55);
 14:   --sb-outline: rgba(255, 255, 255, 0.08);
 15:   --sb-warning: #f6c343;
 16:   --sb-info: #4bc9f0;
 17:   --sb-danger: #ff6b81;
 18:   --sb-success: #6ee7b7;
 19:   --sb-success-bg: #0d4b39;
 20:   --sb-warning-bg: #5f370e;
 21:   --sb-danger-bg: #611527;
 22:   --sb-info-bg: #0b3a57;
 23:   --sb-alert-text: #f8fafc;
 24:   
 25:   /* Design System Tokens */
 26:   --sb-spacing-xs: 0.25rem;
 27:   --sb-spacing-sm: 0.5rem;
 28:   --sb-spacing-md: 1rem;
 29:   --sb-spacing-lg: 1.5rem;
 30:   --sb-spacing-xl: 2rem;
 31:   --sb-spacing-2xl: 3rem;
 32:   
 33:   --sb-transition-fast: 0.15s ease;
 34:   --sb-transition-normal: 0.3s ease;
 35:   --sb-transition-slow: 0.5s ease;
 36:   
 37:   --sb-breakpoint-sm: 576px;
 38:   --sb-breakpoint-md: 768px;
 39:   --sb-breakpoint-lg: 992px;
 40:   
 41:   /* Enhanced Glassmorphism Tokens */
 42:   --sb-glass-bg: rgba(255, 255, 255, 0.05);
 43:   --sb-glass-border: rgba(255, 255, 255, 0.1);
 44:   --sb-glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
 45:   --sb-glass-bg-hover: rgba(255, 255, 255, 0.08);
 46:   --sb-glass-border-hover: rgba(255, 255, 255, 0.15);
 47:   --sb-glass-shadow-hover: 0 12px 40px rgba(0, 0, 0, 0.4);
 48:   
 49:   /* Micro-interaction Tokens */
 50:   --sb-scale-hover: 1.02;
 51:   --sb-scale-active: 0.98;
 52:   --sb-scale-loading: 1.01;
 53:   --sb-translate-hover: -2px;
 54:   --sb-translate-active: 0px;
 55:   
 56:   /* Bottom Navigation Tokens */
 57:   --sb-bottom-nav-height: 60px;
 58:   --sb-bottom-nav-bg: rgba(9, 14, 30, 0.95);
 59:   --sb-bottom-nav-border: rgba(255, 255, 255, 0.1);
 60:   --sb-bottom-nav-shadow: 0 -4px 20px rgba(0, 0, 0, 0.3);
 61:   
 62:   /* Performance Tokens */
 63:   --sb-will-change-transform: will-change: transform;
 64:   --sb-will-change-opacity: will-change: opacity;
 65:   --sb-transform-gpu: transform: translateZ(0);
 66: }
 67: 
 68: body.sb-dark {
 69:   min-height: 100vh;
 70:   background: radial-gradient(circle at top, var(--sb-gradient-mid), var(--sb-gradient-end) 45%, var(--sb-gradient-start));
 71:   color: var(--sb-text);
 72:   letter-spacing: 0.01em;
 73:   font-family: "Space Grotesk", "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
 74: }
 75: 
 76: .sb-dark .text-muted {
 77:   color: var(--sb-muted) !important;
 78: }
 79: 
 80: .sb-dark .text-muted strong {
 81:   color: var(--sb-text);
 82: }
 83: 
 84: .sb-dark .text-muted code {
 85:   color: var(--sb-accent);
 86: }
 87: 
 88: .sb-loader-overlay {
 89:   position: absolute;
 90:   top: 0;
 91:   left: 0;
 92:   right: 0;
 93:   bottom: 0;
 94:   background: rgba(3, 7, 18, 0.8);
 95:   backdrop-filter: blur(2px);
 96:   border-radius: inherit;
 97:   display: flex;
 98:   align-items: center;
 99:   justify-content: center;
100:   opacity: 0;
101:   transition: opacity 0.2s ease-in-out;
102:   z-index: 10;
103: }
104: 
105: .sb-loader-spinner {
106:   width: 2rem;
107:   height: 2rem;
108:   border: 2px solid var(--sb-outline);
109:   border-top: 2px solid var(--sb-accent);
110:   border-radius: 50%;
111:   animation: sb-spin 1s linear infinite;
112: }
113: 
114: @keyframes sb-spin {
115:   0% { transform: rotate(0deg); }
116:   100% { transform: rotate(360deg); }
117: }
118: 
119: .sb-loader--active {
120:   pointer-events: none;
121: }
122: 
123: .sb-loader--active .btn,
124: .sb-loader--active button {
125:   opacity: 0.7;
126: }
127: 
128:  .sb-global-loader {
129:    position: fixed;
130:    top: 0;
131:    left: 0;
132:    right: 0;
133:    bottom: 0;
134:    display: flex;
135:    align-items: center;
136:    justify-content: center;
137:    background: rgba(3, 7, 18, 0.72);
138:    backdrop-filter: blur(3px);
139:    opacity: 0;
140:    visibility: hidden;
141:    pointer-events: none;
142:    transition: opacity 0.18s ease-in-out, visibility 0s linear 0.18s;
143:    z-index: 10000;
144:  }
145: 
146:  .sb-global-loader--active {
147:    opacity: 1;
148:    visibility: visible;
149:    pointer-events: auto;
150:    transition: opacity 0.18s ease-in-out;
151:  }
152: 
153:  .sb-global-loader__spinner {
154:    width: 2.75rem;
155:    height: 2.75rem;
156:    border: 3px solid rgba(255, 255, 255, 0.12);
157:    border-top-color: var(--sb-accent);
158:    border-radius: 50%;
159:    animation: sb-spin 0.9s linear infinite;
160:  }
161: 
162:  body.sb-dark.sb-loading {
163:    cursor: progress;
164:  }
165: 
166: .container {
167:   max-width: 1200px;
168: }
169: 
170: .page-header {
171:   display: flex;
172:   justify-content: space-between;
173:   align-items: center;
174:   gap: 1rem;
175: }
176: 
177: .page-header-main {
178:   display: flex;
179:   align-items: center;
180:   gap: 1.25rem;
181: }
182: 
183: .page-header-actions {
184:   display: flex;
185:   gap: 0.75rem;
186:   flex-wrap: wrap;
187:   justify-content: flex-end;
188: }
189: 
190: .page-header-actions .btn {
191:   white-space: nowrap;
192: }
193: 
194: .quota-banner {
195:   display: flex;
196:   align-items: flex-start;
197:   justify-content: space-between;
198:   gap: 1rem;
199:   border-left: 4px solid var(--sb-warning);
200:   background: linear-gradient(135deg, var(--sb-warning-bg), rgba(95, 55, 14, 0.8));
201:   box-shadow: 0 8px 25px rgba(246, 195, 67, 0.25), 0 4px 12px rgba(0, 0, 0, 0.3);
202:   border-radius: 0.75rem;
203:   backdrop-filter: blur(8px);
204:   position: relative;
205:   overflow: hidden;
206: }
207: 
208: .quota-banner::before {
209:   content: '';
210:   position: absolute;
211:   top: 0;
212:   left: 0;
213:   right: 0;
214:   height: 2px;
215:   background: linear-gradient(90deg, var(--sb-warning), var(--sb-accent), var(--sb-warning));
216:   animation: quota-pulse 2s ease-in-out infinite;
217: }
218: 
219: @keyframes quota-pulse {
220:   0%, 100% { opacity: 0.6; }
221:   50% { opacity: 1; }
222: }
223: 
224: .quota-banner__main {
225:   display: flex;
226:   flex-direction: column;
227:   gap: 0.15rem;
228: }
229: 
230: .page-subtitle {
231:   color: var(--sb-muted);
232:   font-size: 0.95rem;
233: }
234: 
235: @media (max-width: 768px) {
236:   .page-header {
237:     flex-direction: column;
238:     align-items: flex-start;
239:   }
240: 
241:   .page-header-main {
242:     width: 100%;
243:     flex-direction: column;
244:     align-items: flex-start;
245:   }
246: 
247:   .page-header-actions {
248:     width: 100%;
249:     justify-content: flex-start;
250:     flex-wrap: nowrap;
251:     overflow-x: auto;
252:     -webkit-overflow-scrolling: touch;
253:     padding-bottom: 0.25rem;
254:   }
255: 
256:   .quota-banner {
257:     position: sticky;
258:     top: 0.75rem;
259:     z-index: 20;
260:     margin: 0 0.5rem;
261:     border-left-width: 6px;
262:     box-shadow: 0 12px 35px rgba(246, 195, 67, 0.35), 0 6px 18px rgba(0, 0, 0, 0.4);
263:   }
264:   
265:   .quota-banner::before {
266:     height: 3px;
267:     animation-duration: 1.5s;
268:   }
269: }
270: 
271: .card {
272:   border: 1px solid var(--sb-glass-border);
273:   background: var(--sb-glass-bg);
274:   border-radius: 1.25rem;
275:   box-shadow: var(--sb-glass-shadow);
276:   backdrop-filter: blur(20px);
277:   color: var(--sb-text);
278:   transition: background var(--sb-transition-normal), border-color var(--sb-transition-normal), box-shadow var(--sb-transition-normal);
279: }
280: 
281: .card:hover {
282:   background: var(--sb-glass-bg-hover);
283:   border-color: var(--sb-glass-border-hover);
284:   box-shadow: var(--sb-glass-shadow-hover);
285: }
286: 
287: .card-header {
288:   background: transparent;
289:   border-bottom: 1px solid var(--sb-outline);
290:   font-weight: 600;
291:   color: var(--sb-muted);
292: }
293: 
294: dl dt {
295:   color: var(--sb-muted);
296:   text-transform: uppercase;
297:   letter-spacing: 0.06em;
298:   font-size: 0.72rem;
299: }
300: 
301: dl dd {
302:   color: var(--sb-text);
303:   font-weight: 600;
304: }
305: 
306: .btn,
307: .form-check-input,
308: .form-control,
309: .form-select {
310:   border-radius: 0.85rem;
311: }
312: 
313: .btn {
314:   border: 1px solid transparent;
315:   font-weight: 600;
316:   letter-spacing: 0.02em;
317: }
318: 
319: .btn-primary {
320:   background: linear-gradient(120deg, var(--sb-accent), #9fd0ff);
321:   color: var(--sb-accent-contrast);
322:   border-color: transparent;
323: }
324: 
325: .btn-outline-secondary,
326: .btn-outline-success,
327: .btn-outline-danger,
328: .btn-outline-primary,
329: .btn-outline-light {
330:   border-color: rgba(255, 255, 255, 0.35);
331:   color: var(--sb-text);
332: }
333: 
334: .btn-outline-secondary:hover,
335: .btn-outline-success:hover,
336: .btn-outline-danger:hover,
337: .btn-outline-primary:hover,
338: .btn-outline-light:hover,
339: .btn-outline-light:focus-visible {
340:   background: rgba(255, 255, 255, 0.08);
341:   color: var(--sb-text);
342: }
343: 
344: .btn-warning {
345:   background: var(--sb-warning);
346:   color: #332400;
347:   border: none;
348: }
349: 
350: .btn-info {
351:   background: var(--sb-info);
352:   color: #02131b;
353:   border: none;
354: }
355: 
356: .btn-secondary {
357:   background: rgba(255, 255, 255, 0.15);
358:   border: none;
359:   color: var(--sb-text);
360: }
361: 
362: .form-control,
363: .form-select {
364:   background: var(--sb-glass-bg);
365:   border: 1px solid var(--sb-glass-border);
366:   color: var(--sb-text);
367:   padding: 0.85rem 1rem;
368:   backdrop-filter: blur(10px);
369:   transition: background var(--sb-transition-normal), border-color var(--sb-transition-normal), box-shadow var(--sb-transition-normal);
370: }
371: 
372: .form-control:focus,
373: .form-select:focus {
374:   background: var(--sb-glass-bg-hover);
375:   border-color: var(--sb-accent);
376:   box-shadow: 0 0 0 0.15rem rgba(138, 180, 255, 0.25);
377: }
378: 
379: .form-text,
380: .small,
381: .text-muted {
382:   color: var(--sb-muted) !important;
383: }
384: 
385: .form-check-input {
386:   background-color: rgba(255, 255, 255, 0.08);
387:   border-color: var(--sb-outline);
388: }
389: 
390: .form-check-input:checked {
391:   background-color: var(--sb-accent);
392:   border-color: var(--sb-accent);
393: }
394: 
395: .badge.bg-secondary-subtle {
396:   background: rgba(138, 180, 255, 0.15) !important;
397:   color: var(--sb-accent) !important;
398: }
399: 
400: .badge.bg-glass {
401:   background: rgba(255, 255, 255, 0.08);
402:   color: var(--sb-text);
403: }
404: 
405: .badge.bg-accent {
406:   background: rgba(138, 180, 255, 0.2);
407:   color: var(--sb-accent);
408: }
409: 
410: .badge.bg-outline {
411:   border: 1px solid var(--sb-outline);
412:   color: var(--sb-text);
413: }
414: 
415: .api-quota {
416:   background: rgba(255, 255, 255, 0.04);
417:   border: 1px solid var(--sb-outline);
418:   border-radius: 1rem;
419:   padding: 0.75rem 1rem;
420:   min-width: 260px;
421: }
422: 
423: .api-quota-meta {
424:   margin-top: 0.35rem;
425:   font-size: 0.85rem;
426:   color: var(--sb-muted);
427:   display: flex;
428:   align-items: center;
429:   gap: 0.35rem;
430: }
431: 
432: .api-quota-meta .separator {
433:   opacity: 0.6;
434: }
435: 
436: .api-quota-label {
437:   font-size: 0.78rem;
438:   text-transform: uppercase;
439:   letter-spacing: 0.08em;
440:   color: var(--sb-muted);
441: }
442: 
443: .api-quota-values {
444:   display: flex;
445:   align-items: center;
446:   gap: 0.75rem;
447:   margin-top: 0.35rem;
448: }
449: 
450: .api-quota-metric {
451:   display: flex;
452:   flex-direction: column;
453:   gap: 0.1rem;
454: }
455: 
456: .metric-label {
457:   font-size: 0.75rem;
458:   color: var(--sb-muted);
459: }
460: 
461: .metric-value {
462:   font-size: 1.1rem;
463:   font-weight: 600;
464:   color: var(--sb-text);
465: }
466: 
467: .metric-cap {
468:   font-size: 0.75rem;
469:   color: var(--sb-muted);
470: }
471: 
472: .api-quota-separator {
473:   width: 1px;
474:   height: 30px;
475:   background: var(--sb-outline);
476: }
477: 
478: .quota-alert {
479:   border-color: rgba(246, 195, 67, 0.5);
480:   background: rgba(246, 195, 67, 0.08);
481:   color: var(--sb-warning);
482: }
483: 
484: .alert {
485:   border-radius: 1rem;
486:   border: 1px solid var(--sb-glass-border);
487:   padding: 1rem 1.25rem;
488:   color: var(--sb-alert-text);
489:   background: var(--sb-glass-bg);
490:   box-shadow: var(--sb-glass-shadow);
491:   backdrop-filter: blur(15px);
492:   transition: opacity var(--sb-transition-normal), transform var(--sb-transition-normal), background var(--sb-transition-normal);
493: }
494: 
495: .alert p:last-child {
496:   margin-bottom: 0;
497: }
498: 
499: .alert-success {
500:   background: var(--sb-success-bg);
501:   border-color: rgba(110, 231, 183, 0.35);
502: }
503: 
504: .alert-danger {
505:   background: var(--sb-danger-bg);
506:   border-color: rgba(255, 107, 129, 0.35);
507: }
508: 
509: .alert-warning {
510:   background: var(--sb-warning-bg);
511:   border-color: rgba(246, 195, 67, 0.35);
512: }
513: 
514: .alert-info {
515:   background: var(--sb-info-bg);
516:   border-color: rgba(75, 201, 240, 0.45);
517: }
518: 
519: .alert-dismissed {
520:   opacity: 0;
521:   transform: translateY(-6px);
522: }
523: 
524: pre {
525:   color: var(--sb-text);
526:   background: rgba(5, 10, 24, 0.8);
527:   border: 1px solid var(--sb-outline);
528:   border-radius: 1rem;
529:   padding: 1rem;
530:   max-height: 420px;
531:   overflow: auto;
532:   font-size: 0.85rem;
533: }
534: 
535: /* Bottom Navigation Bar */
536: .sb-bottom-nav {
537:   position: fixed;
538:   bottom: 0;
539:   left: 0;
540:   right: 0;
541:   height: var(--sb-bottom-nav-height);
542:   background: var(--sb-bottom-nav-bg);
543:   border-top: 1px solid var(--sb-bottom-nav-border);
544:   box-shadow: var(--sb-bottom-nav-shadow);
545:   backdrop-filter: blur(20px);
546:   z-index: 1000;
547:   display: flex;
548:   justify-content: space-around;
549:   align-items: center;
550:   padding: 0 var(--sb-spacing-md);
551:   transform: translateY(0);
552:   transition: transform var(--sb-transition-normal);
553: }
554: 
555: .sb-bottom-nav--hidden {
556:   transform: translateY(100%);
557: }
558: 
559: .sb-bottom-nav-item {
560:   display: flex;
561:   flex-direction: column;
562:   align-items: center;
563:   gap: var(--sb-spacing-xs);
564:   padding: var(--sb-spacing-sm);
565:   border-radius: var(--sb-spacing-sm);
566:   text-decoration: none;
567:   color: var(--sb-muted);
568:   transition: color var(--sb-transition-fast), 
569:               background var(--sb-transition-fast),
570:               transform var(--sb-transition-fast);
571:   min-width: 44px;
572:   min-height: 44px;
573:   justify-content: center;
574:   position: relative;
575:   overflow: hidden;
576: }
577: 
578: .sb-bottom-nav-item:hover {
579:   color: var(--sb-accent);
580:   background: var(--sb-glass-bg);
581:   transform: translateY(-1px);
582: }
583: 
584: .sb-bottom-nav-item:active {
585:   transform: scale(var(--sb-scale-active));
586: }
587: 
588: .sb-bottom-nav-item--active {
589:   color: var(--sb-accent);
590:   background: var(--sb-glass-bg-hover);
591: }
592: 
593: .sb-bottom-nav-item--active::before {
594:   content: '';
595:   position: absolute;
596:   top: 2px;
597:   left: 50%;
598:   transform: translateX(-50%);
599:   width: 4px;
600:   height: 4px;
601:   border-radius: 50%;
602:   background: var(--sb-accent);
603:   animation: sb-nav-dot-pulse 2s infinite;
604: }
605: 
606: @keyframes sb-nav-dot-pulse {
607:   0%, 100% { 
608:     opacity: 0.8;
609:     transform: translateX(-50%) scale(1);
610:   }
611:   50% { 
612:     opacity: 1;
613:     transform: translateX(-50%) scale(1.2);
614:   }
615: }
616: 
617: .sb-bottom-nav-icon {
618:   width: 20px;
619:   height: 20px;
620:   display: flex;
621:   align-items: center;
622:   justify-content: center;
623:   transition: transform var(--sb-transition-fast);
624: }
625: 
626: .sb-bottom-nav-item:hover .sb-bottom-nav-icon {
627:   transform: scale(1.1);
628: }
629: 
630: .sb-bottom-nav-label {
631:   font-size: 0.7rem;
632:   font-weight: 500;
633:   text-align: center;
634:   transition: transform var(--sb-transition-fast);
635: }
636: 
637: /* Ripple effect for navigation items */
638: .sb-bottom-nav-item.sb-ripple::before {
639:   content: '';
640:   position: absolute;
641:   top: 50%;
642:   left: 50%;
643:   width: 0;
644:   height: 0;
645:   border-radius: 50%;
646:   background: rgba(255, 255, 255, 0.2);
647:   transform: translate(-50%, -50%);
648:   transition: width 0.6s, height 0.6s;
649: }
650: 
651: .sb-bottom-nav-item.sb-ripple:active::before {
652:   width: 80px;
653:   height: 80px;
654: }
655: 
656: /* Add bottom padding to body to account for fixed nav */
657: body.sb-dark {
658:   padding-bottom: var(--sb-bottom-nav-height);
659: }
660: 
661: @media (max-width: 768px) {
662:   .sb-bottom-nav {
663:     padding: 0 var(--sb-spacing-sm);
664:   }
665:   
666:   .sb-bottom-nav-label {
667:     font-size: 0.65rem;
668:   }
669: }
670: 
671: @media (min-width: 769px) {
672:   .sb-bottom-nav {
673:     display: none;
674:   }
675:   
676:   body.sb-dark {
677:     padding-bottom: 0;
678:   }
679: }
680: 
681: /* Micro-interactions & Animations CSS Pures */
682: 
683: /*
684:  * DESIGN SYSTEM - MICRO-INTERACTIONS
685:  * 
686:  * Ce fichier contient toutes les animations CSS pures et micro-interactions
687:  * pour améliorer l'expérience utilisateur sans impacter les performances.
688:  * 
689:  * PRINCIPES:
690:  * - GPU-optimisé: Utilisation de transform/opacity uniquement
691:  * - Accessibilité: Respect de prefers-reduced-motion
692:  * - Performance: Animations légères avec timing approprié
693:  * - Cohérence: Variables CSS pour maintenance facile
694:  * 
695:  * CLASSES DISPONIBLES:
696:  * 
697:  * États de chargement:
698:  * - .sb-loading : Shimmer effect pour les données en chargement
699:  * 
700:  * Animations de données:
701:  * - .sb-pulse : Pulse subtile pour les mises à jour
702:  * - .sb-data-update : Fade-in pour les nouvelles valeurs
703:  * - .sb-temp-change : Animation couleur pour changements température
704:  * 
705:  * États de succès/erreur:
706:  * - .sb-success-flash : Flash vert pour actions réussies
707:  * - .sb-cooldown : Animation d'attente pour cooldowns
708:  * 
709: * Interactions utilisateur:
710:  * - .sb-card-hover : Hover amélioré pour les cartes
711:  * - .sb-button-active : Press effect pour boutons
712:  * - .sb-focus-enhanced : Focus visible amélioré
713:  * - .sb-ripple : Ripple effect pour navigation
714:  * 
715: * Optimisations:
716:  * - .sb-gpu-accelerated : Accélération matérielle
717:  * - .sb-will-change-transform : Hint pour transform animations
718:  * - .sb-will-change-opacity : Hint pour opacity animations
719:  * 
720: * UTILISATION:
721:  * Ajouter les classes directement aux éléments HTML ou via JavaScript
722:  * pour déclencher les animations au bon moment.
723:  * 
724: * EXEMPLE:
725:  * <div class="status-item sb-loading">...</div>
726:  * <button class="scene-action sb-success-flash">...</button>
727:  * <div class="temperature-value sb-temp-change">25.5°C</div>
728:  */
729: 
730: /* Respect for prefers-reduced-motion */
731: @media (prefers-reduced-motion: reduce) {
732:   *,
733:   *::before,
734:   *::after {
735:     animation-duration: 0.01ms !important;
736:     animation-iteration-count: 1 !important;
737:     transition-duration: 0.01ms !important;
738:   }
739: }
740: 
741: /* Loading States */
742: .sb-loading {
743:   position: relative;
744:   overflow: hidden;
745: }
746: 
747: .sb-loading::before {
748:   content: '';
749:   position: absolute;
750:   top: 0;
751:   left: -100%;
752:   width: 100%;
753:   height: 100%;
754:   background: linear-gradient(
755:     90deg,
756:     transparent,
757:     rgba(255, 255, 255, 0.1),
758:     transparent
759:   );
760:   animation: sb-shimmer 1.5s infinite;
761: }
762: 
763: @keyframes sb-shimmer {
764:   0% { transform: translateX(-100%); }
765:   100% { transform: translateX(100%); }
766: }
767: 
768: /* Pulse Animation for Data Updates */
769: .sb-pulse {
770:   animation: sb-pulse 0.6s ease-in-out;
771: }
772: 
773: @keyframes sb-pulse {
774:   0%, 100% { 
775:     opacity: 1; 
776:     transform: scale(1);
777:   }
778:   50% { 
779:     opacity: 0.8; 
780:     transform: scale(var(--sb-scale-loading));
781:   }
782: }
783: 
784: /* Success Flash Animation */
785: .sb-success-flash {
786:   animation: sb-success-flash 0.8s ease-out;
787: }
788: 
789: @keyframes sb-success-flash {
790:   0% { 
791:     background-color: var(--sb-success-bg);
792:     box-shadow: 0 0 0 0 rgba(110, 231, 183, 0.4);
793:   }
794:   50% { 
795:     background-color: var(--sb-success-bg);
796:     box-shadow: 0 0 0 8px rgba(110, 231, 183, 0);
797:   }
798:   100% { 
799:     background-color: transparent;
800:     box-shadow: 0 0 0 0 rgba(110, 231, 183, 0);
801:   }
802: }
803: 
804: /* Temperature Change Animation */
805: .sb-temp-change {
806:   animation: sb-temp-change 1s ease-in-out;
807: }
808: 
809: @keyframes sb-temp-change {
810:   0%, 100% { color: var(--sb-text); }
811:   25% { color: var(--sb-info); }
812:   50% { color: var(--sb-warning); }
813:   75% { color: var(--sb-danger); }
814: }
815: 
816: /* Cooldown State Animation */
817: .sb-cooldown {
818:   position: relative;
819:   pointer-events: none;
820: }
821: 
822: .sb-cooldown::after {
823:   content: '';
824:   position: absolute;
825:   top: 50%;
826:   left: 50%;
827:   width: 100%;
828:   height: 100%;
829:   border: 2px solid var(--sb-muted);
830:   border-radius: inherit;
831:   transform: translate(-50%, -50%);
832:   animation: sb-cooldown-ring 2s linear infinite;
833: }
834: 
835: @keyframes sb-cooldown-ring {
836:   0% { 
837:     transform: translate(-50%, -50%) scale(0.8);
838:     opacity: 1;
839:   }
840:   100% { 
841:     transform: translate(-50%, -50%) scale(1.2);
842:     opacity: 0;
843:   }
844: }
845: 
846: /* Focus States Enhancement */
847: .sb-focus-enhanced:focus-visible {
848:   outline: 2px solid var(--sb-accent);
849:   outline-offset: 2px;
850:   transform: scale(var(--sb-scale-hover));
851: }
852: 
853: /* Ripple Effect for Navigation */
854: .sb-ripple {
855:   position: relative;
856:   overflow: hidden;
857: }
858: 
859: .sb-ripple::before {
860:   content: '';
861:   position: absolute;
862:   top: 50%;
863:   left: 50%;
864:   width: 0;
865:   height: 0;
866:   border-radius: 50%;
867:   background: rgba(255, 255, 255, 0.3);
868:   transform: translate(-50%, -50%);
869:   transition: width 0.6s, height 0.6s;
870: }
871: 
872: .sb-ripple:active::before {
873:   width: 100px;
874:   height: 100px;
875: }
876: 
877: /* Data Value Animation */
878: .sb-data-update {
879:   animation: sb-data-update 0.4s ease-out;
880: }
881: 
882: @keyframes sb-data-update {
883:   0% { 
884:     opacity: 0.3;
885:     transform: translateY(4px);
886:   }
887:   100% { 
888:     opacity: 1;
889:     transform: translateY(0);
890:   }
891: }
892: 
893: /* Hover Enhancement for Cards */
894: .sb-card-hover {
895:   transition: transform var(--sb-transition-fast), 
896:               box-shadow var(--sb-transition-fast),
897:               background var(--sb-transition-normal);
898: }
899: 
900: .sb-card-hover:hover {
901:   transform: translateY(var(--sb-translate-hover)) scale(var(--sb-scale-hover));
902:   box-shadow: var(--sb-glass-shadow-hover);
903: }
904: 
905: /* Active State for Buttons */
906: .sb-button-active {
907:   transition: transform var(--sb-transition-fast);
908: }
909: 
910: .sb-button-active:active {
911:   transform: scale(var(--sb-scale-active));
912: }
913: 
914: /* Status Indicator Animation */
915: .sb-status-indicator {
916:   position: relative;
917: }
918: 
919: .sb-status-indicator::before {
920:   content: '';
921:   position: absolute;
922:   top: 50%;
923:   left: 50%;
924:   width: 8px;
925:   height: 8px;
926:   border-radius: 50%;
927:   background: currentColor;
928:   transform: translate(-50%, -50%);
929:   animation: sb-status-pulse 2s infinite;
930: }
931: 
932: @keyframes sb-status-pulse {
933:   0%, 100% { 
934:     opacity: 0.8;
935:     transform: translate(-50%, -50%) scale(1);
936:   }
937:   50% { 
938:     opacity: 1;
939:     transform: translate(-50%, -50%) scale(1.2);
940:   }
941: }
942: 
943: /* GPU Optimization Classes */
944: .sb-gpu-accelerated {
945:   transform: translateZ(0);
946:   backface-visibility: hidden;
947:   perspective: 1000px;
948: }
949: 
950: .sb-will-change-transform {
951:   will-change: transform;
952: }
953: 
954: .sb-will-change-opacity {
955:   will-change: opacity;
956: }
```

## File: switchbot_dashboard/templates/devices.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>Appareils - SwitchBot Dashboard</title>
  7:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/bootstrap.min.css') }}" />
  8:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/space-grotesk.css') }}" />
  9:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 10:     <link rel="stylesheet" href="{{ url_for('static', filename='css/devices.css') }}" />
 11:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 12:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/fontawesome/css/all.min.css') }}" />
 13:   </head>
 14:   <body class="sb-dark">
 15:     <div class="container py-4">
 16:       <h1 class="h3 mb-4">Appareils</h1>
 17: 
 18:       {% if error %}
 19:         <div class="alert alert-danger">{{ error }}</div>
 20:       {% endif %}
 21: 
 22:       {% if data %}
 23:         {% set body = data.get("body", {}) or {} %}
 24:         {% set device_list = body.get("deviceList") or [] %}
 25:         {% set remote_list = body.get("infraredRemoteList") or [] %}
 26: 
 27:         <div class="card highlight-card mb-4" aria-live="polite">
 28:           <div class="card-body d-flex flex-column flex-lg-row align-items-lg-center gap-3">
 29:             <div>
 30:               <p class="text-uppercase small text-muted fw-semibold mb-1">Instantané d'inventaire</p>
 31:               <h2 class="h4 mb-0">{{ device_list | length }} physiques · {{ remote_list | length }} infrarouges</h2>
 32:             </div>
 33:             <div class="ms-lg-auto">
 34:               <p class="mb-0 text-muted">
 35:                 Utilise ces listes pour retrouver rapidement <code>meter_device_id</code> et <code>aircon_device_id</code>
 36:                 avant de mettre à jour <strong>config/settings.json</strong> (cf. docs/README.md).
 37:               </p>
 38:             </div>
 39:           </div>
 40:         </div>
 41: 
 42:         <section aria-labelledby="devices-heading" class="mb-5">
 43:           <div class="section-title">
 44:             <div>
 45:               <p class="text-uppercase small text-muted fw-semibold mb-1">Appareils physiques</p>
 46:               <h2 id="devices-heading" class="h4 mb-0">Liste des appareils</h2>
 47:             </div>
 48:             {% if device_list %}
 49:               <span class="badge rounded-pill bg-glass">{{ device_list | length }} trouvés</span>
 50:             {% endif %}
 51:           </div>
 52: 
 53:           {% if device_list %}
 54:             <div class="device-grid">
 55:               {% for device in device_list %}
 56:                 <article class="device-card" aria-label="{{ device.get('deviceName') or 'Appareil SwitchBot' }}">
 57:                   <div class="device-card__header">
 58:                     <div>
 59:                       <h3 class="device-name">{{ device.get("deviceName") or "Appareil sans nom" }}</h3>
 60:                       <p class="device-type text-muted mb-0">{{ device.get("deviceType") or "Type inconnu" }}</p>
 61:                     </div>
 62:                     <span class="badge rounded-pill bg-accent">
 63:                       {{ "Hub" if device.get("hubDeviceId") else "Autonome" }}
 64:                     </span>
 65:                   </div>
 66: 
 67:                   <dl class="device-meta device-meta--primary">
 68:                     <div>
 69:                       <dt>ID</dt>
 70:                       <dd class="device-id">{{ device.get("deviceId") or "—" }}</dd>
 71:                     </div>
 72:                     <div>
 73:                       <dt>Statut</dt>
 74:                       <dd class="{{ 'text-success' if device.get('status') == 'online' else 'text-warning' }}">
 75:                         {{ device.get("status") or "n/d" }}
 76:                       </dd>
 77:                     </div>
 78:                   </dl>
 79: 
 80:                   <details class="device-details">
 81:                     <summary>Voir les détails</summary>
 82:                     <dl class="device-meta device-meta--secondary">
 83:                       <div>
 84:                         <dt>Hub</dt>
 85:                         <dd>{{ device.get("hubDeviceId") or "Aucun" }}</dd>
 86:                       </div>
 87:                       <div>
 88:                         <dt>Firmware</dt>
 89:                         <dd>{{ device.get("firmwareVersion") or "Inconnu" }}</dd>
 90:                       </div>
 91:                       <div>
 92:                         <dt>Cloud</dt>
 93:                         <dd>{{ "Activé" if device.get("enableCloudService") else "Désactivé" }}</dd>
 94:                       </div>
 95:                       <div>
 96:                         <dt>Batterie</dt>
 97:                         <dd>{{ device.get("battery") or "—" }}</dd>
 98:                       </div>
 99:                     </dl>
100:                   </details>
101: 
102:                   <div class="device-actions">
103:                     <button
104:                       type="button"
105:                       class="btn btn-copy"
106:                       data-copy="{{ device.get('deviceId') }}"
107:                       aria-label="Copier l'identifiant {{ device.get('deviceName') }}"
108:                     >
109:                       Copier l'ID
110:                     </button>
111:                     {% if device.get("virtualModel") %}
112:                       <span class="badge rounded-pill bg-outline">{{ device.get("virtualModel") }}</span>
113:                     {% endif %}
114:                   </div>
115:                 </article>
116:               {% endfor %}
117:             </div>
118:           {% else %}
119:             <p class="text-muted fst-italic">Aucun appareil physique n'a été renvoyé.</p>
120:           {% endif %}
121: 
122:           <!-- Collapsible raw JSON retained for troubleshooting without overwhelming the main UI -->
123:           <details class="raw-block mt-3">
124:             <summary>Afficher le JSON brut deviceList</summary>
125:             <pre>{{ device_list | tojson(indent=2) }}</pre>
126:           </details>
127:         </section>
128: 
129:         <section aria-labelledby="remotes-heading">
130:           <div class="section-title">
131:             <div>
132:               <p class="text-uppercase small text-muted fw-semibold mb-1">Télécommandes infrarouges</p>
133:               <h2 id="remotes-heading" class="h4 mb-0">Liste des télécommandes</h2>
134:             </div>
135:             {% if remote_list %}
136:               <span class="badge rounded-pill bg-glass">{{ remote_list | length }} trouvées</span>
137:             {% endif %}
138:           </div>
139: 
140:           {% if remote_list %}
141:             <div class="device-grid">
142:               {% for remote in remote_list %}
143:                 <article class="device-card" aria-label="{{ remote.get('remoteName') or 'Télécommande infrarouge' }}">
144:                   <div class="device-card__header">
145:                     <div>
146:                       <h3 class="device-name">{{ remote.get("remoteName") or "Télécommande sans nom" }}</h3>
147:                       <p class="device-type text-muted mb-0">{{ remote.get("remoteType") or "Type inconnu" }}</p>
148:                     </div>
149:                     <span class="badge rounded-pill bg-accent">
150:                       {{ remote.get("hubDeviceId") or "Hub n/d" }}
151:                     </span>
152:                   </div>
153: 
154:                   <dl class="device-meta device-meta--primary">
155:                     <div>
156:                       <dt>ID</dt>
157:                       <dd class="device-id">{{ remote.get("deviceId") or "—" }}</dd>
158:                     </div>
159:                     <div>
160:                       <dt>Marque</dt>
161:                       <dd>{{ remote.get("remoteBrand") or "Inconnue" }}</dd>
162:                     </div>
163:                   </dl>
164: 
165:                   <details class="device-details">
166:                     <summary>Voir les détails</summary>
167:                     <dl class="device-meta device-meta--secondary">
168:                       <div>
169:                         <dt>Modèle</dt>
170:                         <dd>{{ remote.get("remoteModel") or "Inconnu" }}</dd>
171:                       </div>
172:                       <div>
173:                         <dt>Catégorie</dt>
174:                         <dd>{{ remote.get("remoteDeviceType") or "n/d" }}</dd>
175:                       </div>
176:                       <div>
177:                         <dt>Cloud</dt>
178:                         <dd>{{ "Activé" if remote.get("enableCloudService") else "Désactivé" }}</dd>
179:                       </div>
180:                     </dl>
181:                   </details>
182: 
183:                   <div class="device-actions">
184:                     <button
185:                       type="button"
186:                       class="btn btn-copy"
187:                       data-copy="{{ remote.get('deviceId') }}"
188:                       aria-label="Copier l'identifiant {{ remote.get('remoteName') }}"
189:                     >
190:                       Copier l'ID
191:                     </button>
192:                     {% if remote.get("hubDeviceId") %}
193:                       <span class="badge rounded-pill bg-outline">Hub {{ remote.get("hubDeviceId") }}</span>
194:                     {% endif %}
195:                   </div>
196:                 </article>
197:               {% endfor %}
198:             </div>
199:           {% else %}
200:             <p class="text-muted fst-italic">Aucune télécommande IR n'a été renvoyée.</p>
201:           {% endif %}
202: 
203:           <details class="raw-block mt-3">
204:             <summary>Afficher le JSON brut infraredRemoteList</summary>
205:             <pre>{{ remote_list | tojson(indent=2) }}</pre>
206:           </details>
207:         </section>
208:       {% else %}
209:         <div class="alert alert-warning">Aucune donnée.</div>
210:       {% endif %}
211:     </div>
212:     
213:     {% include '_footer_nav.html' %}
214:     
215:     <script src="{{ url_for('static', filename='js/devices.js') }}"></script>
216:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
217:   </body>
218: </html>
```

## File: switchbot_dashboard/templates/history.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>Historique Monitoring - SwitchBot Dashboard</title>
  7:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/bootstrap.min.css') }}" />
  8:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/space-grotesk.css') }}" />
  9:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 10:     <link rel="stylesheet" href="{{ url_for('static', filename='css/history.css') }}" />
 11:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 12:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/fontawesome/css/all.min.css') }}" />
 13:     <style>
 14:       /* Centrage et blocs des checkboxes de métriques */
 15:       .metric-checkboxes {
 16:         display: flex;
 17:         justify-content: center;
 18:         align-items: stretch;
 19:         gap: 1rem;
 20:         flex-wrap: wrap;
 21:       }
 22:       
 23:       .metric-checkboxes .metric-option {
 24:         flex: 1 1 140px;
 25:         min-width: 140px;
 26:         background: var(--sb-card);
 27:         border: 1px solid var(--sb-card-border);
 28:         border-radius: 0.75rem;
 29:         padding: 0.75rem 1rem;
 30:         display: flex;
 31:         align-items: center;
 32:         gap: 0.75rem;
 33:         margin: 0;
 34:         box-shadow: var(--sb-shadow);
 35:       }
 36:       
 37:       .metric-checkboxes .metric-option:hover {
 38:         border-color: var(--sb-accent);
 39:       }
 40:       
 41:       .metric-checkboxes .metric-option .form-check-input {
 42:         margin: 0;
 43:         width: 1.1rem;
 44:         height: 1.1rem;
 45:       }
 46:       
 47:       .metric-checkboxes .metric-option .form-check-label {
 48:         margin: 0;
 49:         font-weight: 600;
 50:         color: var(--sb-text);
 51:         display: flex;
 52:         align-items: center;
 53:       }
 54:       
 55:       @media (max-width: 768px) {
 56:         .metric-checkboxes {
 57:           flex-direction: column;
 58:           gap: 0.75rem;
 59:         }
 60:       }
 61:     </style>
 62:   </head>
 63:   <body class="sb-dark">
 64:     <div class="container py-4">
 65:       <header class="page-header mb-4">
 66:         <div class="page-header-main">
 67:           <h1 class="h3 mb-0">Historique Monitoring</h1>
 68:           <p class="page-subtitle text-muted mb-0">
 69:             Visualisez les tendances et analysez les données historiques.
 70:           </p>
 71:         </div>
 72:       </header>
 73: 
 74:       <!-- Filters Section -->
 75:       <section class="history-filters mb-4">
 76:         <div class="card sb-card">
 77:           <div class="card-body">
 78:             <form id="filtersForm" class="row g-3 align-items-end">
 79:               <div class="col-md-3">
 80:                 <label for="timeRange" class="form-label">Période</label>
 81:                 <select class="form-select sb-select" id="timeRange" name="timeRange">
 82:                   <option value="1h">Dernière heure</option>
 83:                   <option value="6h" selected>Dernières 6 heures</option>
 84:                   <option value="24h">Dernières 24 heures</option>
 85:                   <option value="custom">Personnalisé</option>
 86:                 </select>
 87:               </div>
 88:               <div class="col-md-3" id="customStartGroup" style="display: none;">
 89:                 <label for="customStart" class="form-label">Début</label>
 90:                 <input type="datetime-local" class="form-control sb-input" id="customStart" name="customStart">
 91:               </div>
 92:               <div class="col-md-3" id="customEndGroup" style="display: none;">
 93:                 <label for="customEnd" class="form-label">Fin</label>
 94:                 <input type="datetime-local" class="form-control sb-input" id="customEnd" name="customEnd">
 95:               </div>
 96:               <div class="col-md-2">
 97:                 <label for="granularity" class="form-label">Granularité</label>
 98:                 <select class="form-select sb-select" id="granularity" name="granularity">
 99:                   <option value="minute">Par minute</option>
100:                   <option value="5min">Par 5 minutes</option>
101:                   <option value="15min">Par 15 minutes</option>
102:                   <option value="hour">Par heure</option>
103:                 </select>
104:               </div>
105:               <div class="col-md-4">
106:                 <label class="form-label">Métriques</label>
107:                 <div class="metric-checkboxes">
108:                   <div class="form-check metric-option">
109:                     <input class="form-check-input" type="checkbox" id="metricTemp" value="temperature" checked>
110:                     <label class="form-check-label" for="metricTemp">
111:                       <span>Température</span>
112:                     </label>
113:                   </div>
114:                   <div class="form-check metric-option">
115:                     <input class="form-check-input" type="checkbox" id="metricHumidity" value="humidity" checked>
116:                     <label class="form-check-label" for="metricHumidity">
117:                       <span>Humidité</span>
118:                     </label>
119:                   </div>
120:                   <div class="form-check metric-option">
121:                     <input class="form-check-input" type="checkbox" id="metricAircon" value="assumed_aircon_power" checked>
122:                     <label class="form-check-label" for="metricAircon">
123:                       <span>Climatisation</span>
124:                     </label>
125:                   </div>
126:                 </div>
127:               </div>
128:               <div class="col-md-2">
129:                 <button type="submit" class="btn btn-primary w-100" data-loader>
130:                   Appliquer
131:                 </button>
132:               </div>
133:             </form>
134:           </div>
135:         </div>
136:       </section>
137: 
138:       <!-- Status Cards -->
139:       <section class="status-cards mb-4">
140:         <div class="row g-3">
141:           <div class="col-md-6">
142:             <div class="card sb-card status-card">
143:               <div class="card-body text-center">
144:                 <div class="status-card__value" id="avgTemp">--</div>
145:                 <div class="status-card__label">Température moyenne</div>
146:                 <div class="status-card__unit">°C</div>
147:               </div>
148:             </div>
149:           </div>
150:           <div class="col-md-6">
151:             <div class="card sb-card status-card">
152:               <div class="card-body text-center">
153:                 <div class="status-card__value" id="avgHumidity">--</div>
154:                 <div class="status-card__label">Humidité moyenne</div>
155:                 <div class="status-card__unit">%</div>
156:               </div>
157:             </div>
158:           </div>
159:         </div>
160:       </section>
161: 
162:       <!-- Charts Section -->
163:       <section class="charts-section mb-4">
164:         <div class="row g-4">
165:           <!-- Temperature & Humidity Chart -->
166:           <div class="col-12">
167:             <div class="card sb-card">
168:               <div class="card-header d-flex justify-content-between align-items-center">
169:                 <h5 class="card-title mb-0">Température & Humidité</h5>
170:                 <div class="chart-controls">
171:                   <button class="btn btn-sm btn-outline-secondary" id="resetZoomTemp">
172:                     Réinitialiser zoom
173:                   </button>
174:                 </div>
175:               </div>
176:               <div class="card-body">
177:                 <div class="chart-container">
178:                   <canvas id="tempHumidityChart"></canvas>
179:                 </div>
180:               </div>
181:             </div>
182:           </div>
183: 
184:           <!-- Aircon State Chart -->
185:           <div class="col-12">
186:             <div class="card sb-card">
187:               <div class="card-header">
188:                 <h5 class="card-title mb-0">État Climatisation</h5>
189:               </div>
190:               <div class="card-body">
191:                 <div class="chart-container" style="max-height: 300px;">
192:                   <canvas id="airconStateChart"></canvas>
193:                 </div>
194:               </div>
195:             </div>
196:           </div>
197:         </div>
198:       </section>
199: 
200:       <!-- Latest Records Table -->
201:       <section class="latest-records mb-4">
202:         <div class="card sb-card">
203:           <div class="card-header d-flex justify-content-between align-items-center">
204:             <h5 class="card-title mb-0">Derniers enregistrements</h5>
205:             <button class="btn btn-sm btn-outline-secondary" id="refreshLatest">
206:               Actualiser
207:             </button>
208:           </div>
209:           <div class="card-body">
210:             <div class="table-responsive">
211:               <table class="table table-dark table-hover" id="latestTable">
212:                 <thead>
213:                   <tr>
214:                     <th>Timestamp</th>
215:                     <th>Température</th>
216:                     <th>Humidité</th>
217:                     <th>Climatisation</th>
218:                     <th>Action</th>
219:                   </tr>
220:                 </thead>
221:                 <tbody id="latestTableBody">
222:                   <tr>
223:                     <td colspan="5" class="text-center text-muted">
224:                       <div class="spinner-border spinner-border-sm me-2" role="status"></div>
225:                       Chargement...
226:                     </td>
227:                   </tr>
228:                 </tbody>
229:               </table>
230:             </div>
231:           </div>
232:         </div>
233:       </section>
234: 
235:       <!-- Real-time Status -->
236:       <section class="real-time-status">
237:         <div class="card sb-card">
238:           <div class="card-body">
239:             <div class="d-flex justify-content-between align-items-center">
240:               <div>
241:                 <small class="text-muted">Dernière mise à jour</small>
242:                 <div class="fw-bold" id="lastUpdate">--</div>
243:               </div>
244:               <div class="d-flex align-items-center">
245:                 <div class="status-indicator me-2" id="statusIndicator"></div>
246:                 <span id="statusText">En attente</span>
247:               </div>
248:             </div>
249:           </div>
250:         </div>
251:       </section>
252:     </div>
253: 
254:     {% include '_footer_nav.html' %}
255: 
256:     <!-- Scripts -->
257:     <script src="{{ url_for('static', filename='vendor/js/chart.umd.min.js') }}"></script>
258:     <script src="{{ url_for('static', filename='vendor/js/chartjs-adapter-date-fns.bundle.min.js') }}"></script>
259:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
260:     <script src="{{ url_for('static', filename='js/history.js') }}"></script>
261:   </body>
262: </html>
```

## File: switchbot_dashboard/templates/quota.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>Quota API SwitchBot</title>
  7:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/bootstrap.min.css') }}" />
  8:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/space-grotesk.css') }}" />
  9:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 10:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 11:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/fontawesome/css/all.min.css') }}" />
 12:   </head>
 13:   <body class="sb-dark">
 14:     <div class="container py-4">
 15:       <header class="page-header mb-4">
 16:         <div class="page-header-main">
 17:           <h1 class="h3 mb-0">Quota API quotidien</h1>
 18:           <p class="page-subtitle text-muted mb-0">
 19:             Surveillez votre consommation SwitchBot et anticipez les coupures.
 20:           </p>
 21:         </div>
 22:       </header>
 23: 
 24:       <section class="mb-4">
 25:         <form method="post" action="{{ url_for('dashboard.quota_refresh') }}" data-loader class="d-flex flex-column flex-md-row align-items-md-center gap-3">
 26:           {{ csrf_field() if csrf_field is defined }}
 27:           <div class="flex-grow-1">
 28:             <p class="mb-1 text-muted">Forcez un rafraîchissement pour re-normaliser les compteurs locaux si nécessaire.</p>
 29:           </div>
 30:           <button type="submit" class="btn btn-outline-light">
 31:             <i class="fas fa-rotate me-2"></i>
 32:             Rafraîchir les compteurs
 33:           </button>
 34:         </form>
 35:       </section>
 36: 
 37:       {% with messages = get_flashed_messages(with_categories=true) %}
 38:         {% if messages %}
 39:           <div class="mb-3" aria-live="polite" aria-atomic="true">
 40:             {% for category, message in messages %}
 41:               {% if category == 'error' %}
 42:                 <div class="alert alert-danger" role="alert" data-auto-dismiss="6000">
 43:                   {{ message }}
 44:                 </div>
 45:               {% elif category == 'success' %}
 46:                 <div class="alert alert-success" role="alert" data-auto-dismiss="6000">
 47:                   {{ message }}
 48:                 </div>
 49:               {% else %}
 50:                 <div class="alert alert-info" role="alert" data-auto-dismiss="6000">
 51:                   {{ message }}
 52:                 </div>
 53:               {% endif %}
 54:             {% endfor %}
 55:           </div>
 56:         {% endif %}
 57:       {% endwith %}
 58: 
 59:       <article class="card">
 60:         <div class="card-body">
 61:           <div class="d-flex flex-column flex-lg-row align-items-lg-center gap-4">
 62:             <div class="api-quota flex-grow-1">
 63:               <span class="api-quota-label">Suivi journalier</span>
 64:               {% if api_quota_day %}
 65:                 <div class="api-quota-meta">
 66:                   Jour suivi : <strong>{{ api_quota_day }}</strong>
 67:                   {% if api_quota_reset_at %}
 68:                     <span class="separator">•</span>
 69:                     Reset prévu : <strong>{{ api_quota_reset_at }}</strong>
 70:                   {% else %}
 71:                     <span class="separator">•</span>
 72:                     Reset automatique à 00:00 UTC
 73:                   {% endif %}
 74:                 </div>
 75:               {% endif %}
 76: 
 77:               <div class="api-quota-values">
 78:                 <div class="api-quota-metric">
 79:                   <span class="metric-label">Restantes</span>
 80:                   <span class="metric-value">
 81:                     {{ api_requests_remaining if api_requests_remaining is not none else "N/A" }}
 82:                   </span>
 83:                 </div>
 84:                 <span class="api-quota-separator" aria-hidden="true"></span>
 85:                 <div class="api-quota-metric">
 86:                   <span class="metric-label">Utilisées</span>
 87:                   <span class="metric-value">
 88:                     {{ api_requests_total if api_requests_total is not none else "N/A" }}
 89:                   </span>
 90:                   <span class="metric-cap">
 91:                     / {{ api_requests_limit if api_requests_limit is not none else "10,000" }}
 92:                   </span>
 93:                 </div>
 94:               </div>
 95: 
 96:               {% if show_quota_warning %}
 97:                 <div class="quota-alert alert alert-warning mt-3" role="status">
 98:                   <strong>Attention : quota critique.</strong>
 99:                   <span>
100:                     Il ne reste que {{ api_requests_remaining }} appels (seuil fixé à {{ quota_warning_threshold }}).
101:                   </span>
102:                 </div>
103:               {% endif %}
104:             </div>
105: 
106:             <div class="text-muted small flex-grow-1">
107:               <p class="mb-2">
108:                 Le compteur s'appuie sur <strong>ApiQuotaTracker</strong> :
109:               </p>
110:               <ul class="mb-3 ps-4">
111:                 <li>Réinitialisation automatique à minuit (UTC)</li>
112:                 <li>Fallback local si les en-têtes SwitchBot sont absents</li>
113:                 <li>Inclut les appels manuels, scènes et boucles d'automatisation</li>
114:               </ul>
115:               <p class="mb-0">
116:                 Ajustez le seuil d'alerte dans les réglages de l'accueil pour être prévenu suffisamment tôt.
117:               </p>
118:             </div>
119:           </div>
120:         </div>
121:       </article>
122:     </div>
123:     
124:     {% include '_footer_nav.html' %}
125:     
126:     <script src="{{ url_for('static', filename='js/alerts.js') }}"></script>
127:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
128:   </body>
129: </html>
```

## File: config/settings.json
```json
 1: {
 2:   "automation_enabled": true,
 3:   "mode": "winter",
 4:   "poll_interval_seconds": 30,
 5:   "hysteresis_celsius": 0.3,
 6:   "command_cooldown_seconds": 60,
 7:   "action_on_cooldown_seconds": 420,
 8:   "action_off_cooldown_seconds": 60,
 9:   "off_repeat_count": 2,
10:   "off_repeat_interval_seconds": 10,
11:   "turn_off_outside_windows": true,
12:   "timezone": "Europe/Paris",
13:   "api_quota_warning_threshold": 250,
14:   "meter_device_id": "FCE61F1FD04C",
15:   "aircon_device_id": "01-202401301615-24010246",
16:   "winter": {
17:     "min_temp": 24.0,
18:     "max_temp": 27.0,
19:     "target_temp": 26.0,
20:     "fan_speed": 3,
21:     "ac_mode": 5
22:   },
23:   "summer": {
24:     "min_temp": 23.0,
25:     "max_temp": 26.0,
26:     "target_temp": 24.0,
27:     "fan_speed": 3,
28:     "ac_mode": 2
29:   },
30:   "aircon_scenes": {
31:     "winter": "c8e87fd2-2b9f-4a2d-8f81-c82e7f230e94",
32:     "summer": "f621a00e-5979-4372-888b-4e18e4017945",
33:     "fan": "2988f98c-ed4a-437c-9faa-fa62ccc38bc8",
34:     "off": "bd52478c-37a0-4607-9ab9-3e9749ecf0df"
35:   },
36:   "ifttt_webhooks": {
37:     "winter": "https://maker.ifttt.com/trigger/switchbot_winter/with/key/k6QOrDiDeXrNxOhN94s3b",
38:     "summer": "https://maker.ifttt.com/trigger/switchbot_summer/with/key/k6QOrDiDeXrNxOhN94s3b",
39:     "fan": "https://maker.ifttt.com/trigger/switchbot_fan/with/key/k6QOrDiDeXrNxOhN94s3b",
40:     "off": "https://maker.ifttt.com/trigger/switchbot_off/with/key/k6QOrDiDeXrNxOhN94s3b"
41:   },
42:   "time_windows": [
43:     {
44:       "days": [0, 1, 2, 3, 4, 5, 6],
45:       "start": "10:00",
46:       "end": "01:00"
47:     }
48:   ]
49: }
```

## File: switchbot_dashboard/templates/settings.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>Réglages · SwitchBot Dashboard</title>
  7:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/bootstrap.min.css') }}" />
  8:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/space-grotesk.css') }}" />
  9:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 10:     <link rel="stylesheet" href="{{ url_for('static', filename='css/settings.css') }}" />
 11:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 12:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/fontawesome/css/all.min.css') }}" />
 13:   </head>
 14:   <body class="sb-dark">
 15:     <div class="container py-4">
 16:       <header class="page-header mb-4">
 17:         <div class="page-header-main">
 18:           <h1 class="h3 mb-0">Réglages SwitchBot</h1>
 19:           <p class="page-subtitle text-muted mb-0">
 20:             Configurez les fenêtres horaires, profils hiver/été, scènes et seuils avancés.
 21:           </p>
 22:         </div>
 23:       </header>
 24: 
 25:       {% with messages = get_flashed_messages(with_categories=true) %}
 26:         {% if messages %}
 27:           <div class="mb-3" aria-live="polite" aria-atomic="true">
 28:             {% for category, message in messages %}
 29:               {% if category == 'error' %}
 30:                 <div class="alert alert-danger" role="alert" data-auto-dismiss="6000">
 31:                   {{ message }}
 32:                 </div>
 33:               {% else %}
 34:                 <div class="alert alert-success" role="alert" data-auto-dismiss="6000">
 35:                   {{ message }}
 36:                 </div>
 37:               {% endif %}
 38:             {% endfor %}
 39:           </div>
 40:         {% endif %}
 41:       {% endwith %}
 42: 
 43:       <div class="row g-3">
 44:         <div class="col-12 col-xl-9">
 45:           <div class="card">
 46:             <div class="card-header">Paramètres d'automatisation</div>
 47:             <div class="card-body">
 48:               <form method="post" action="{{ url_for('dashboard.update_settings') }}" class="settings-form" data-loader>
 49:                 <div class="form-check form-switch mb-3">
 50:                   <input
 51:                     class="form-check-input"
 52:                     type="checkbox"
 53:                     role="switch"
 54:                     id="automation_enabled"
 55:                     name="automation_enabled"
 56:                     {% if settings.get('automation_enabled') %}checked{% endif %}
 57:                   />
 58:                   <label class="form-check-label" for="automation_enabled">Automatisation activée</label>
 59:                 </div>
 60: 
 61:                 <div class="row g-3">
 62:                   <div class="col-12 col-md-4">
 63:                     <label class="form-label" for="mode">Mode</label>
 64:                     <select class="form-select" id="mode" name="mode">
 65:                       <option value="winter" {% if settings.get('mode') == 'winter' %}selected{% endif %}>hiver</option>
 66:                       <option value="summer" {% if settings.get('mode') == 'summer' %}selected{% endif %}>été</option>
 67:                     </select>
 68:                   </div>
 69: 
 70:                   <div class="col-12 col-md-4">
 71:                     <label class="form-label" for="poll_interval_seconds">Intervalle de sondage (s)</label>
 72:                     <input
 73:                       class="form-control"
 74:                       id="poll_interval_seconds"
 75:                       name="poll_interval_seconds"
 76:                       value="{{ settings.get('poll_interval_seconds') }}"
 77:                       inputmode="numeric"
 78:                     />
 79:                   </div>
 80: 
 81:                   <div class="col-12 col-md-4">
 82:                     <label class="form-label" for="command_cooldown_seconds">Cooldown par défaut (s)</label>
 83:                     <input
 84:                       class="form-control"
 85:                       id="command_cooldown_seconds"
 86:                       name="command_cooldown_seconds"
 87:                       value="{{ settings.get('command_cooldown_seconds') }}"
 88:                       inputmode="numeric"
 89:                     />
 90:                     <div class="form-text">Utilisé si les champs ci-dessous sont vides.</div>
 91:                   </div>
 92: 
 93:                   <div class="col-12 col-md-4">
 94:                     <label class="form-label" for="action_on_cooldown_seconds">Cooldown après démarrage (s)</label>
 95:                     <input
 96:                       class="form-control"
 97:                       id="action_on_cooldown_seconds"
 98:                       name="action_on_cooldown_seconds"
 99:                       value="{{ settings.get('action_on_cooldown_seconds') }}"
100:                       inputmode="numeric"
101:                     />
102:                     <div class="form-text">Recommandé : 300 s (5 min) pour laisser la pompe chauffer.</div>
103:                   </div>
104: 
105:                   <div class="col-12 col-md-4">
106:                     <label class="form-label" for="action_off_cooldown_seconds">Cooldown après arrêt (s)</label>
107:                     <input
108:                       class="form-control"
109:                       id="action_off_cooldown_seconds"
110:                       name="action_off_cooldown_seconds"
111:                       value="{{ settings.get('action_off_cooldown_seconds') }}"
112:                       inputmode="numeric"
113:                     />
114:                     <div class="form-text">Recommandé : 60 s pour garder un arrêt réactif.</div>
115:                   </div>
116:                 </div>
117: 
118:                 <div class="row g-3">
119:                   <div class="col-12">
120:                     <div class="form-check form-switch">
121:                       <input
122:                         class="form-check-input"
123:                         type="checkbox"
124:                         role="switch"
125:                         id="adaptive_polling_enabled"
126:                         name="adaptive_polling_enabled"
127:                         {% if settings.get('adaptive_polling_enabled', true) %}checked{% endif %}
128:                       />
129:                       <label class="form-check-label" for="adaptive_polling_enabled">Polling adaptatif activé</label>
130:                     </div>
131:                     <div class="form-text">Réduit la fréquence hors fenêtres horaires et relance avant les créneaux actifs.</div>
132:                   </div>
133: 
134:                   <div class="col-12 col-md-6">
135:                     <label class="form-label" for="idle_poll_interval_seconds">Intervalle hors fenêtre (s)</label>
136:                     <input
137:                       class="form-control"
138:                       id="idle_poll_interval_seconds"
139:                       name="idle_poll_interval_seconds"
140:                       value="{{ settings.get('idle_poll_interval_seconds', 600) }}"
141:                       inputmode="numeric"
142:                       min="15"
143:                       max="86400"
144:                     />
145:                     <div class="form-text">Recommandé : 600 s (10 min) lorsque l'automatisation est inactive.</div>
146:                   </div>
147: 
148:                   <div class="col-12 col-md-6">
149:                     <label class="form-label" for="poll_warmup_minutes">Warmup avant fenêtre (min)</label>
150:                     <input
151:                       class="form-control"
152:                       id="poll_warmup_minutes"
153:                       name="poll_warmup_minutes"
154:                       value="{{ settings.get('poll_warmup_minutes', 15) }}"
155:                       inputmode="numeric"
156:                       min="0"
157:                       max="1440"
158:                     />
159:                     <div class="form-text">Repasse à l'intervalle normal N minutes avant la prochaine fenêtre.</div>
160:                   </div>
161:                 </div>
162: 
163:                 <div class="row g-3">
164:                   <div class="col-12 col-md-4">
165:                     <label class="form-label" for="off_repeat_count">Répétitions arrêt OFF</label>
166:                     <input
167:                       class="form-control"
168:                       id="off_repeat_count"
169:                       name="off_repeat_count"
170:                       value="{{ settings.get('off_repeat_count', 1) }}"
171:                       inputmode="numeric"
172:                       min="1"
173:                       max="10"
174:                     />
175:                     <div class="form-text">Nombre total d'ordres OFF envoyés (1 = aucune répétition).</div>
176:                   </div>
177: 
178:                   <div class="col-12 col-md-4">
179:                     <label class="form-label" for="off_repeat_interval_seconds">Intervalle entre OFF (s)</label>
180:                     <input
181:                       class="form-control"
182:                       id="off_repeat_interval_seconds"
183:                       name="off_repeat_interval_seconds"
184:                       value="{{ settings.get('off_repeat_interval_seconds', 10) }}"
185:                       inputmode="numeric"
186:                       min="1"
187:                     />
188:                     <div class="form-text">Délai entre deux OFF successifs (ex. 10 s).</div>
189:                   </div>
190:                 </div>
191: 
192:                 <div class="row g-3">
193:                   <div class="col-12 col-md-6">
194:                     <label class="form-label" for="hysteresis_celsius">Hystérésis (°C)</label>
195:                     <input
196:                       class="form-control"
197:                       id="hysteresis_celsius"
198:                       name="hysteresis_celsius"
199:                       value="{{ settings.get('hysteresis_celsius') }}"
200:                     />
201:                   </div>
202: 
203:                   <div class="col-12 col-md-6">
204:                     <label class="form-label" for="api_quota_warning_threshold">Seuil d'alerte quota</label>
205:                     <input
206:                       class="form-control"
207:                       id="api_quota_warning_threshold"
208:                       name="api_quota_warning_threshold"
209:                       type="number"
210:                       min="0"
211:                       max="10000"
212:                       value="{{ settings.get('api_quota_warning_threshold', quota_warning_threshold) }}"
213:                     />
214:                     <div class="form-text">Bannière d'alerte lorsque les appels restants passent sous cette valeur.</div>
215:                   </div>
216: 
217:                   <div class="col-12 col-md-6">
218:                     <label class="form-label" for="timezone">Fuseau horaire</label>
219:                     <input
220:                       class="form-control"
221:                       id="timezone"
222:                       name="timezone"
223:                       value="{{ settings.get('timezone', 'Europe/Paris') }}"
224:                       placeholder="Europe/Paris"
225:                       autocapitalize="none"
226:                       autocomplete="off"
227:                       spellcheck="false"
228:                     />
229:                     <div class="form-text">Utilisé pour interpréter les fenêtres horaires (identifiant IANA, ex: Europe/Paris, UTC).</div>
230:                   </div>
231: 
232:                   <div class="col-12">
233:                     <div class="form-check mb-2">
234:                       <input
235:                         class="form-check-input"
236:                         type="checkbox"
237:                         id="turn_off_outside_windows"
238:                         name="turn_off_outside_windows"
239:                         {% if settings.get('turn_off_outside_windows') %}checked{% endif %}
240:                       />
241:                       <label class="form-check-label" for="turn_off_outside_windows">Éteindre en dehors des fenêtres horaires</label>
242:                     </div>
243:                   </div>
244: 
245:                   <div class="col-12 col-md-6">
246:                     <label class="form-label" for="meter_device_id">ID du capteur Meter</label>
247:                     <input class="form-control" id="meter_device_id" name="meter_device_id" value="{{ settings.get('meter_device_id') }}" />
248:                   </div>
249: 
250:                   <div class="col-12 col-md-6">
251:                     <label class="form-label" for="aircon_device_id">ID de la télécommande IR</label>
252:                     <input class="form-control" id="aircon_device_id" name="aircon_device_id" value="{{ settings.get('aircon_device_id') }}" />
253:                     <div class="form-text">Identifiant de la télécommande infrarouge (remoteType: Air Conditioner).</div>
254:                   </div>
255:                 </div>
256: 
257:                 <hr />
258: 
259:                 <div class="section-heading mb-2">
260:                   <label class="form-label mb-0">Fenêtre horaire</label>
261:                   <span class="badge rounded-pill bg-secondary-subtle text-secondary-emphasis">optimisé mobile</span>
262:                 </div>
263:                 <div class="small text-muted mb-2">Sélectionnez les jours puis choisissez l'heure de début et de fin (format 24h).</div>
264:                 <div class="border rounded-3 p-3 mb-3 time-window-card">
265:                   <div class="row g-3">
266:                     <div class="col-12">
267:                       <label class="form-label d-block">Jours</label>
268:                       <div class="d-flex flex-wrap gap-2">
269:                         {% for day in day_choices %}
270:                           <div class="form-check form-check-inline day-chip">
271:                             <input
272:                               class="btn-check"
273:                               type="checkbox"
274:                               id="day_{{ day.value }}"
275:                               name="time_window_days"
276:                               value="{{ day.value }}"
277:                               aria-describedby="time_window_days_summary"
278:                               {% if day.value in time_window_form['days'] %}checked{% endif %}
279:                             />
280:                             <label class="btn btn-outline-primary btn-sm" for="day_{{ day.value }}">{{ day.label }}</label>
281:                           </div>
282:                         {% endfor %}
283:                       </div>
284:                       <div id="time_window_days_summary" class="form-text" aria-live="polite">
285:                         {{ time_window_form['days'] | length }} jour(s) sélectionné(s).
286:                       </div>
287:                     </div>
288:                     <div class="col-6">
289:                       <label class="form-label" for="time_window_start">Début</label>
290:                       <select class="form-select" id="time_window_start" name="time_window_start" aria-describedby="time_window_help">
291:                         <option value="">Choisir…</option>
292:                         {% for choice in time_choices %}
293:                           <option value="{{ choice }}" {% if time_window_form['start'] == choice %}selected{% endif %}>{{ choice }}</option>
294:                         {% endfor %}
295:                       </select>
296:                     </div>
297:                     <div class="col-6">
298:                       <label class="form-label" for="time_window_end">Fin</label>
299:                       <select class="form-select" id="time_window_end" name="time_window_end" aria-describedby="time_window_help">
300:                         <option value="">Choisir…</option>
301:                         {% for choice in time_choices %}
302:                           <option value="{{ choice }}" {% if time_window_form['end'] == choice %}selected{% endif %}>{{ choice }}</option>
303:                         {% endfor %}
304:                       </select>
305:                     </div>
306:                     <div class="col-12">
307:                       <div id="time_window_help" class="form-text">
308:                         Astuce : si aucun jour n'est sélectionné, la fenêtre horaire est considérée comme inactive.
309:                       </div>
310:                     </div>
311:                   </div>
312:                 </div>
313: 
314:                 <hr />
315: 
316:                 {% set winter_profile = settings.get('winter', {}) %}
317:                 <h2 class="h6">Profil hiver</h2>
318:                 <div class="row g-2 mb-3">
319:                   <div class="col-4">
320:                     <label class="form-label" for="winter_min_temp">Min.</label>
321:                     <select class="form-select" id="winter_min_temp" name="winter_min_temp">
322:                       {% for choice in temp_choices %}
323:                         <option value="{{ choice.value }}" {% if (winter_profile.get('min_temp') | float) == choice.value %}selected{% endif %}>
324:                           {{ choice.label }}°C
325:                         </option>
326:                       {% endfor %}
327:                     </select>
328:                   </div>
329:                   <div class="col-4">
330:                     <label class="form-label" for="winter_max_temp">Max.</label>
331:                     <select class="form-select" id="winter_max_temp" name="winter_max_temp">
332:                       {% for choice in temp_choices %}
333:                         <option value="{{ choice.value }}" {% if (winter_profile.get('max_temp') | float) == choice.value %}selected{% endif %}>
334:                           {{ choice.label }}°C
335:                         </option>
336:                       {% endfor %}
337:                     </select>
338:                   </div>
339:                   <div class="col-4">
340:                     <label class="form-label" for="winter_target_temp">Cible</label>
341:                     <select class="form-select" id="winter_target_temp" name="winter_target_temp">
342:                       {% for choice in temp_choices %}
343:                         <option value="{{ choice.value }}" {% if (winter_profile.get('target_temp') | float) == choice.value %}selected{% endif %}>
344:                           {{ choice.label }}°C
345:                         </option>
346:                       {% endfor %}
347:                     </select>
348:                   </div>
349:                   <div class="col-6">
350:                     <label class="form-label" for="winter_ac_mode">Mode clim</label>
351:                     <select class="form-select" id="winter_ac_mode" name="winter_ac_mode">
352:                       {% for choice in ac_mode_choices %}
353:                         <option value="{{ choice.value }}" {% if (winter_profile.get('ac_mode') | int) == choice.value %}selected{% endif %}>
354:                           {{ choice.label }}
355:                         </option>
356:                       {% endfor %}
357:                     </select>
358:                   </div>
359:                   <div class="col-6">
360:                     <label class="form-label" for="winter_fan_speed">Vitesse ventilateur</label>
361:                     <select class="form-select" id="winter_fan_speed" name="winter_fan_speed">
362:                       {% for choice in fan_speed_choices %}
363:                         <option value="{{ choice.value }}" {% if (winter_profile.get('fan_speed') | int) == choice.value %}selected{% endif %}>
364:                           {{ choice.label }}
365:                         </option>
366:                       {% endfor %}
367:                     </select>
368:                   </div>
369:                 </div>
370: 
371:                 {% set summer_profile = settings.get('summer', {}) %}
372:                 <h2 class="h6">Profil été</h2>
373:                 <div class="row g-2">
374:                   <div class="col-4">
375:                     <label class="form-label" for="summer_min_temp">Min.</label>
376:                     <select class="form-select" id="summer_min_temp" name="summer_min_temp">
377:                       {% for choice in temp_choices %}
378:                         <option value="{{ choice.value }}" {% if (summer_profile.get('min_temp') | float) == choice.value %}selected{% endif %}>
379:                           {{ choice.label }}°C
380:                         </option>
381:                       {% endfor %}
382:                     </select>
383:                   </div>
384:                   <div class="col-4">
385:                     <label class="form-label" for="summer_max_temp">Max.</label>
386:                     <select class="form-select" id="summer_max_temp" name="summer_max_temp">
387:                       {% for choice in temp_choices %}
388:                         <option value="{{ choice.value }}" {% if (summer_profile.get('max_temp') | float) == choice.value %}selected{% endif %}>
389:                           {{ choice.label }}°C
390:                         </option>
391:                       {% endfor %}
392:                     </select>
393:                   </div>
394:                   <div class="col-4">
395:                     <label class="form-label" for="summer_target_temp">Cible</label>
396:                     <select class="form-select" id="summer_target_temp" name="summer_target_temp">
397:                       {% for choice in temp_choices %}
398:                         <option value="{{ choice.value }}" {% if (summer_profile.get('target_temp') | float) == choice.value %}selected{% endif %}>
399:                           {{ choice.label }}°C
400:                         </option>
401:                       {% endfor %}
402:                     </select>
403:                   </div>
404:                   <div class="col-6">
405:                     <label class="form-label" for="summer_ac_mode">Mode clim</label>
406:                     <select class="form-select" id="summer_ac_mode" name="summer_ac_mode">
407:                       {% for choice in ac_mode_choices %}
408:                         <option value="{{ choice.value }}" {% if (summer_profile.get('ac_mode') | int) == choice.value %}selected{% endif %}>
409:                           {{ choice.label }}
410:                         </option>
411:                       {% endfor %}
412:                     </select>
413:                   </div>
414:                   <div class="col-6">
415:                     <label class="form-label" for="summer_fan_speed">Vitesse ventilateur</label>
416:                     <select class="form-select" id="summer_fan_speed" name="summer_fan_speed">
417:                       {% for choice in fan_speed_choices %}
418:                         <option value="{{ choice.value }}" {% if (summer_profile.get('fan_speed') | int) == choice.value %}selected{% endif %}>
419:                           {{ choice.label }}
420:                         </option>
421:                       {% endfor %}
422:                     </select>
423:                   </div>
424:                 </div>
425: 
426:                 <div class="mt-4">
427:                   <button class="btn btn-primary w-100 w-md-auto" type="submit">Enregistrer les réglages</button>
428:                 </div>
429: 
430:                 <hr class="my-4" />
431: 
432:                 <h2 class="h6">Webhooks IFTTT (Priorité)</h2>
433:                 <p class="small text-muted">
434:                   Renseignez les URLs des webhooks IFTTT pour déclencher vos scènes via le cloud. Les webhooks sont prioritaires sur les scènes SwitchBot natives.
435:                 </p>
436:                 <div class="row g-3 mb-4">
437:                   {% for key in aircon_scene_keys %}
438:                     <div class="col-12 col-md-6">
439:                       <label class="form-label" for="webhook_{{ key }}_url">{{ aircon_scene_labels[key] }}</label>
440:                       <input
441:                         class="form-control"
442:                         id="webhook_{{ key }}_url"
443:                         name="webhook_{{ key }}_url"
444:                         value="{{ ifttt_webhooks[key] }}"
445:                         placeholder="https://maker.ifttt.com/trigger/..."
446:                         type="url"
447:                       />
448:                       {% if missing_webhooks[key] %}
449:                         <div class="form-text text-warning">Non configuré (fallback vers scène SwitchBot)</div>
450:                       {% else %}
451:                         <div class="form-text text-success">Prêt</div>
452:                       {% endif %}
453:                     </div>
454:                   {% endfor %}
455:                 </div>
456: 
457:                 <h2 class="h6">Scènes favorites SwitchBot (Fallback)</h2>
458:                 <p class="small text-muted">
459:                   Renseignez les IDs des scènes favorites (SwitchBot → Scenes). Elles servent de fallback si les webhooks IFTTT échouent ou ne sont pas configurés.
460:                 </p>
461:                 <div class="row g-3">
462:                   {% for key in aircon_scene_keys %}
463:                     <div class="col-12 col-md-6 col-lg-3">
464:                       <label class="form-label" for="scene_{{ key }}_id">{{ aircon_scene_labels[key] }}</label>
465:                       <input
466:                         class="form-control"
467:                         id="scene_{{ key }}_id"
468:                         name="scene_{{ key }}_id"
469:                         value="{{ aircon_scenes[key] }}"
470:                         placeholder="UUID scène"
471:                       />
472:                       {% if missing_scenes[key] %}
473:                         <div class="form-text text-warning">Non configuré</div>
474:                       {% else %}
475:                         <div class="form-text text-success">Prêt</div>
476:                       {% endif %}
477:                     </div>
478:                   {% endfor %}
479:                 </div>
480:               </form>
481:             </div>
482:           </div>
483:         </div>
484: 
485:         <div class="col-12 col-xl-3">
486:           <div class="card h-100">
487:             <div class="card-header">Résumé rapide</div>
488:             <div class="card-body">
489:               <dl class="row mb-0 small">
490:                 <dt class="col-7">Mode actuel</dt>
491:                 <dd class="col-5 text-end text-capitalize">{{ settings.get('mode', 'winter') }}</dd>
492: 
493:                 <dt class="col-7">Seuil alerte quota</dt>
494:                 <dd class="col-5 text-end">{{ quota_warning_threshold }}</dd>
495: 
496:                 <dt class="col-7">Fenêtre horaire</dt>
497:                 <dd class="col-5 text-end">
498:                   {% if time_window_form['days'] %}
499:                     {{ time_window_form['start'] or '--:--' }} → {{ time_window_form['end'] or '--:--' }}
500:                   {% else %}
501:                     Aucune
502:                   {% endif %}
503:                 </dd>
504: 
505:                 <dt class="col-7">Webhooks IFTTT</dt>
506:                 <dd class="col-5 text-end">
507:                   {{ configured_webhooks_count }} / {{ aircon_scene_keys | length }}
508:                 </dd>
509: 
510:                 <dt class="col-7">Scènes configurées</dt>
511:                 <dd class="col-5 text-end">
512:                   {{ configured_scenes_count }} / {{ aircon_scene_keys | length }}
513:                 </dd>
514:               </dl>
515:               <div class="mt-3">
516:                 <p class="small text-muted mb-2">Besoin d'un rafraîchissement ?</p>
517:                 <a class="btn btn-outline-light w-100" href="{{ url_for('dashboard.index') }}">Voir l'état en temps réel</a>
518:               </div>
519:             </div>
520:           </div>
521:         </div>
522:       </div>
523:     </div>
524:     
525:     {% include '_footer_nav.html' %}
526:     
527:     <script src="{{ url_for('static', filename='js/alerts.js') }}"></script>
528:     <script src="{{ url_for('static', filename='js/settings.js') }}"></script>
529:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
530:     <script src="{{ url_for('static', filename='js/bottom-nav.js') }}"></script>
531:     <script src="{{ url_for('static', filename='js/performance-optimizer.js') }}"></script>
532:   </body>
533: </html>
```

## File: switchbot_dashboard/__init__.py
```python
  1: from __future__ import annotations
  2: 
  3: import logging
  4: import os
  5: from pathlib import Path
  6: 
  7: from dotenv import load_dotenv
  8: 
  9: from flask import Flask
 10: 
 11: from .automation import AutomationService
 12: from .config_store import BaseStore, JsonStore, StoreError
 13: from .postgres_store import PostgresStore, PostgresStoreError
 14: from .history_service import HistoryService
 15: from .ifttt import IFTTTWebhookClient
 16: from .routes import dashboard_bp
 17: from .scheduler import SchedulerService
 18: from .quota import ApiQuotaTracker
 19: from .switchbot_api import SwitchBotClient
 20: 
 21: load_dotenv()
 22: 
 23: 
 24: def _build_store(
 25:     app: Flask,
 26:     *,
 27:     kind: str,
 28:     default_path: str,
 29:     path_env: str,
 30: ) -> BaseStore:
 31:     backend = os.environ.get("STORE_BACKEND", "postgres").strip().lower()
 32:     selected_backend = backend or "postgres"
 33: 
 34:     def _make_json_store() -> BaseStore:
 35:         path = os.environ.get(path_env, default_path)
 36:         app.logger.info("Using filesystem backend for %s store at %s", kind, path)
 37:         return JsonStore(path)
 38: 
 39:     # PostgreSQL backend (preferred)
 40:     if selected_backend == "postgres":
 41:         postgres_url = os.environ.get("POSTGRES_URL", "").strip()
 42:         if not postgres_url:
 43:             app.logger.error(
 44:                 "[store] STORE_BACKEND=postgres but no POSTGRES_URL configured. Falling back to filesystem for %s store.",
 45:                 kind,
 46:             )
 47:             return _make_json_store()
 48: 
 49:         try:
 50:             ssl_mode = os.environ.get("POSTGRES_SSL_MODE", "require").strip()
 51:             store = PostgresStore(
 52:                 connection_string=postgres_url,
 53:                 kind=kind,
 54:                 logger=app.logger,
 55:                 ssl_mode=ssl_mode,
 56:             )
 57:             
 58:             # Health check
 59:             if store.health_check():
 60:                 app.logger.info("[store] Using PostgreSQL backend for %s store", kind)
 61:                 return store
 62:             else:
 63:                 app.logger.error(
 64:                     "[store] PostgreSQL health check failed for %s store. Falling back to filesystem.",
 65:                     kind,
 66:                 )
 67:                 store.close()
 68:                 return _make_json_store()
 69:                 
 70:         except PostgresStoreError as exc:
 71:             app.logger.error(
 72:                 "[store] PostgreSQL backend unavailable for %s store (%s). Falling back to filesystem.",
 73:                 kind,
 74:                 exc,
 75:             )
 76:             return _make_json_store()
 77: 
 78:     # Legacy Redis support (deprecated)
 79:     elif selected_backend == "redis":
 80:         app.logger.warning(
 81:             "[store] Redis backend is deprecated. Consider migrating to PostgreSQL. Using filesystem fallback for %s store.",
 82:             kind,
 83:         )
 84:         return _make_json_store()
 85: 
 86:     # Filesystem fallback
 87:     return _make_json_store()
 88: 
 89: 
 90: def _mark_temperature_stale(app: Flask, state_store: BaseStore, *, reason: str) -> None:
 91:     try:
 92:         state = state_store.read()
 93:     except StoreError as exc:
 94:         app.logger.warning("Unable to read state to mark temperature stale: %s", exc)
 95:         return
 96: 
 97:     state["last_temperature_stale"] = True
 98:     state["last_temperature_stale_reason"] = reason
 99: 
100:     try:
101:         state_store.write(state)
102:     except StoreError as exc:
103:         app.logger.warning("Unable to persist temperature stale flag: %s", exc)
104: 
105: 
106: def create_app() -> Flask:
107:     app = Flask(__name__)
108:     app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev")
109:     app.config["STATE_DEBUG_TOKEN"] = os.environ.get("STATE_DEBUG_TOKEN", "").strip()
110: 
111:     log_level_raw = os.environ.get("LOG_LEVEL", "info").strip().upper()
112:     log_level = getattr(logging, log_level_raw, logging.INFO)
113:     logging.getLogger().setLevel(log_level)
114:     app.logger.setLevel(log_level)
115: 
116:     project_root = Path(__file__).resolve().parents[1]
117:     default_settings_path = str(project_root / "config" / "settings.json")
118:     default_state_path = str(project_root / "config" / "state.json")
119: 
120:     settings_store = _build_store(
121:         app,
122:         kind="settings",
123:         default_path=default_settings_path,
124:         path_env="SWITCHBOT_SETTINGS_PATH",
125:     )
126:     state_store = _build_store(
127:         app,
128:         kind="state",
129:         default_path=default_state_path,
130:         path_env="SWITCHBOT_STATE_PATH",
131:     )
132: 
133:     poll_interval_env = os.environ.get("SWITCHBOT_POLL_INTERVAL_SECONDS")
134:     if poll_interval_env:
135:         try:
136:             poll_interval_seconds = max(15, int(poll_interval_env))
137:         except ValueError:
138:             poll_interval_seconds = None
139:         else:
140:             settings = settings_store.read()
141:             if settings.get("poll_interval_seconds") != poll_interval_seconds:
142:                 settings["poll_interval_seconds"] = poll_interval_seconds
143:                 settings_store.write(settings)
144: 
145:     token = os.environ.get("SWITCHBOT_TOKEN", "")
146:     secret = os.environ.get("SWITCHBOT_SECRET", "")
147: 
148:     retry_attempts_raw = os.environ.get("SWITCHBOT_RETRY_ATTEMPTS", "2")
149:     retry_delay_raw = os.environ.get("SWITCHBOT_RETRY_DELAY_SECONDS", "10")
150:     try:
151:         retry_attempts = int(retry_attempts_raw)
152:     except ValueError:
153:         retry_attempts = 2
154: 
155:     try:
156:         retry_delay_seconds = int(retry_delay_raw)
157:     except ValueError:
158:         retry_delay_seconds = 10
159: 
160:     quota_tracker = ApiQuotaTracker(state_store=state_store)
161: 
162:     client = SwitchBotClient(
163:         token=token,
164:         secret=secret,
165:         retry_attempts=retry_attempts,
166:         retry_delay_seconds=retry_delay_seconds,
167:         quota_tracker=quota_tracker,
168:     )
169: 
170:     ifttt_client = IFTTTWebhookClient(timeout=10.0, logger_instance=app.logger)
171: 
172:     # Initialize HistoryService if PostgreSQL is available
173:     history_service = None
174:     app.logger.info(f"[history] Settings store type: {type(settings_store)}")
175:     app.logger.info(f"[history] Is PostgresStore: {isinstance(settings_store, PostgresStore)}")
176:     
177:     if isinstance(settings_store, PostgresStore):
178:         try:
179:             history_service = HistoryService(
180:                 connection_pool=settings_store._pool,
181:                 logger=app.logger,
182:                 retention_hours=6,
183:             )
184:             app.logger.info("[history] HistoryService initialized with PostgreSQL backend")
185:         except Exception as exc:
186:             app.logger.error("[history] Failed to initialize HistoryService: %s", exc)
187:             import traceback
188:             app.logger.error(f"[history] Traceback: {traceback.format_exc()}")
189:     else:
190:         app.logger.warning("[history] HistoryService disabled: PostgreSQL backend not available")
191: 
192:     automation_service = AutomationService(
193:         settings_store=settings_store,
194:         state_store=state_store,
195:         switchbot_client=client,
196:         ifttt_client=ifttt_client,
197:         history_service=history_service,
198:     )
199: 
200:     scheduler_service = SchedulerService(
201:         settings_store=settings_store,
202:         tick_callable=automation_service.run_once,
203:         state_store=state_store,
204:         logger=app.logger,
205:     )
206: 
207:     app.extensions["settings_store"] = settings_store
208:     app.extensions["state_store"] = state_store
209:     app.extensions["switchbot_client"] = client
210:     app.extensions["ifttt_client"] = ifttt_client
211:     app.extensions["automation_service"] = automation_service
212:     app.extensions["scheduler_service"] = scheduler_service
213:     app.extensions["quota_tracker"] = quota_tracker
214:     if history_service:
215:         app.extensions["history_service"] = history_service
216: 
217:     app.register_blueprint(dashboard_bp)
218: 
219:     _mark_temperature_stale(app, state_store, reason="app_start")
220:     try:
221:         automation_service.poll_meter()
222:     except Exception as exc:  # pragma: no cover - defensive safeguard
223:         app.logger.warning("Initial meter poll failed: %s", exc)
224: 
225:     scheduler_enabled = os.environ.get("SCHEDULER_ENABLED", "true").strip().lower()
226: 
227:     if scheduler_enabled == "true":
228:         is_flask_dev_reloader_parent = (
229:             os.environ.get("FLASK_DEBUG", "").strip().lower() not in ("", "0", "false")
230:             and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
231:             and not os.environ.get("SERVER_SOFTWARE")
232:         )
233: 
234:         if is_flask_dev_reloader_parent:
235:             app.logger.info("[scheduler] Skipping start in Flask development reloader parent process")
236:         else:
237:             scheduler_service.start()
238:             app.logger.info("[scheduler] APScheduler enabled and started")
239:     else:
240:         app.logger.info("[scheduler] APScheduler disabled via SCHEDULER_ENABLED=false")
241: 
242:     return app
```

## File: switchbot_dashboard/automation.py
```python
  1: from __future__ import annotations
  2: 
  3: import datetime as dt
  4: import logging
  5: from typing import Any, Optional
  6: from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
  7: 
  8: from flask import has_request_context, request
  9: 
 10: from .aircon import AIRCON_IFTTT_LABELS, AIRCON_SCENE_LABELS, extract_aircon_scenes
 11: from .config_store import BaseStore
 12: from .ifttt import IFTTTWebhookClient, IFTTTWebhookError, extract_ifttt_webhooks
 13: from .switchbot_api import SwitchBotApiError, SwitchBotClient
 14: 
 15: 
 16: def _parse_hhmm(value: str) -> dt.time:
 17:     parts = value.strip().split(":")
 18:     if len(parts) != 2:
 19:         raise ValueError("Invalid HH:MM")
 20: 
 21:     hour = int(parts[0])
 22:     minute = int(parts[1])
 23:     return dt.time(hour=hour, minute=minute)
 24: 
 25: 
 26: def _is_now_in_windows(time_windows: list[dict[str, Any]], now: dt.datetime) -> bool:
 27:     for window in time_windows:
 28:         days = window.get("days")
 29:         if not isinstance(days, list):
 30:             continue
 31: 
 32:         start_raw = window.get("start")
 33:         end_raw = window.get("end")
 34:         if not isinstance(start_raw, str) or not isinstance(end_raw, str):
 35:             continue
 36: 
 37:         try:
 38:             start = _parse_hhmm(start_raw)
 39:             end = _parse_hhmm(end_raw)
 40:         except ValueError:
 41:             continue
 42:         now_time = now.time().replace(tzinfo=None)
 43: 
 44:         if start <= end:
 45:             if now.weekday() in days and start <= now_time <= end:
 46:                 return True
 47:         else:
 48:             if now.weekday() in days and now_time >= start:
 49:                 return True
 50: 
 51:             previous_weekday = (now - dt.timedelta(days=1)).weekday()
 52:             if previous_weekday in days and now_time <= end:
 53:                 return True
 54: 
 55:     return False
 56: 
 57: 
 58: def _utc_now_iso() -> str:
 59:     return dt.datetime.now(dt.timezone.utc).isoformat()
 60: 
 61: 
 62: def _ensure_utc(value: dt.datetime) -> dt.datetime:
 63:     if value.tzinfo is None:
 64:         return value.replace(tzinfo=dt.timezone.utc)
 65:     return value.astimezone(dt.timezone.utc)
 66: 
 67: 
 68: logger = logging.getLogger(__name__)
 69: OFF_REPEAT_STATE_KEY = "pending_off_repeat"
 70: DEFAULT_TIMEZONE = "Europe/Paris"
 71: 
 72: 
 73: def _format_details(details: dict[str, Any]) -> str:
 74:     if not details:
 75:         return ""
 76:     serialized = []
 77:     for key in sorted(details):
 78:         value = details[key]
 79:         serialized.append(f"{key}={value!r}")
 80:     return " | ".join(serialized)
 81: 
 82: 
 83: def _summarize_time_windows(time_windows: list[dict[str, Any]]) -> str:
 84:     if not time_windows:
 85:         return "none"
 86:     segments: list[str] = []
 87:     for window in time_windows:
 88:         days = window.get("days")
 89:         if isinstance(days, list):
 90:             day_tokens = ",".join(str(day) for day in days)
 91:         else:
 92:             day_tokens = "?"
 93:         start = window.get("start", "?")
 94:         end = window.get("end", "?")
 95:         segments.append(f"[{day_tokens}] {start}-{end}")
 96:     return "; ".join(segments)
 97: 
 98: 
 99: class AutomationService:
100:     """Core automation service for SwitchBot device control.
101: 
102:     Manages temperature monitoring, scene execution, and device automation
103:     with timezone-aware scheduling and IFTTT webhook integration.
104: 
105:     Attributes:
106:         _settings_store: Persistent storage for configuration settings
107:         _state_store: Persistent storage for runtime state
108:         _client: SwitchBot API client with quota tracking
109:         _ifttt_client: IFTTT webhook client for scene triggers
110:         _logger: Logger instance for structured logging
111: 
112:     Example:
113:         >>> service = AutomationService(settings_store, state_store, client, ifttt_client)
114:         >>> service.run_once()  # Execute one automation cycle
115:     """
116:     def __init__(
117:         self,
118:         settings_store: BaseStore,
119:         state_store: BaseStore,
120:         switchbot_client: SwitchBotClient,
121:         ifttt_client: IFTTTWebhookClient,
122:         *,
123:         history_service: Optional[Any] = None,  # HistoryService to avoid circular import
124:         logger: logging.Logger | None = None,
125:     ) -> None:
126:         self._settings_store = settings_store
127:         self._state_store = state_store
128:         self._client = switchbot_client
129:         self._ifttt_client = ifttt_client
130:         self._history_service = history_service
131:         self._logger = logger or logging.getLogger(__name__)
132:         self._cached_timezone_key: str | None = None
133:         self._cached_timezone_value: tuple[dt.tzinfo, str] | None = None
134: 
135:     def _update_state(self, **updates: Any) -> None:
136:         state = self._state_store.read()
137:         state.update(updates)
138:         self._state_store.write(state)
139: 
140:     def _log(self, level: int, message: str, **details: Any) -> None:
141:         payload = "[automation] " + message
142:         formatted_details = _format_details(details)
143:         if formatted_details:
144:             payload = f"{payload} | {formatted_details}"
145:         self._logger.log(level, payload)
146: 
147:     def _debug(self, message: str, **details: Any) -> None:
148:         self._log(logging.DEBUG, message, **details)
149: 
150:     def _info(self, message: str, **details: Any) -> None:
151:         self._log(logging.INFO, message, **details)
152: 
153:     def _warning(self, message: str, **details: Any) -> None:
154:         self._log(logging.WARNING, message, **details)
155: 
156:     def _error(self, message: str, **details: Any) -> None:
157:         self._log(logging.ERROR, message, **details)
158: 
159:     def _detect_trigger_source(self) -> str:
160:         if has_request_context():
161:             endpoint = request.endpoint or "http_request"
162:             return f"http:{endpoint}"
163:         return "scheduler"
164: 
165:     def _get_timezone(self, settings: dict[str, Any], *, trigger: str) -> tuple[dt.tzinfo, str]:
166:         raw_timezone = settings.get("timezone")
167:         timezone_name = str(raw_timezone or "").strip() or DEFAULT_TIMEZONE
168:         cache_key = timezone_name
169:         if (
170:             self._cached_timezone_key == cache_key
171:             and self._cached_timezone_value is not None
172:         ):
173:             return self._cached_timezone_value
174: 
175:         try:
176:             timezone_obj = ZoneInfo(timezone_name)
177:             resolved_name = timezone_name
178:         except ZoneInfoNotFoundError:
179:             self._warning(
180:                 "Invalid timezone; falling back to UTC",
181:                 trigger=trigger,
182:                 timezone=timezone_name,
183:             )
184:             timezone_obj = dt.timezone.utc
185:             resolved_name = "UTC"
186: 
187:         self._cached_timezone_key = cache_key
188:         self._cached_timezone_value = (timezone_obj, resolved_name)
189:         return timezone_obj, resolved_name
190: 
191:     def _log_quota_snapshot(self, context: str) -> None:
192:         state = self._state_store.read()
193:         self._debug(
194:             "Quota snapshot updated",
195:             context=context,
196:             api_requests_total=state.get("api_requests_total"),
197:             api_requests_remaining=state.get("api_requests_remaining"),
198:             api_requests_limit=state.get("api_requests_limit"),
199:             api_quota_day=state.get("api_quota_day"),
200:         )
201: 
202:     def _log_tick_completion(self, trigger: str, outcome: str, **details: Any) -> None:
203:         self._debug("Automation tick finished", trigger=trigger, outcome=outcome, **details)
204: 
205:     def poll_meter(self) -> dict[str, Any] | None:
206:         settings = self._settings_store.read()
207:         meter_id = str(settings.get("meter_device_id", "")).strip()
208:         trigger = self._detect_trigger_source()
209:         if not meter_id:
210:             self._warning(
211:                 "Meter polling skipped: missing meter_device_id",
212:                 trigger=trigger,
213:             )
214:             self._update_state(last_error="Missing meter_device_id", last_read_at=_utc_now_iso())
215:             return None
216: 
217:         self._debug("Polling SwitchBot meter", trigger=trigger, meter_device_id=meter_id)
218: 
219:         try:
220:             response = self._client.get_device_status(meter_id)
221:         except SwitchBotApiError as exc:
222:             self._update_state(
223:                 last_error=str(exc),
224:                 last_read_at=_utc_now_iso(),
225:                 last_temperature_stale=True,
226:                 last_temperature_stale_reason="api_error",
227:             )
228:             self._error(
229:                 "Meter polling failed",
230:                 trigger=trigger,
231:                 meter_device_id=meter_id,
232:                 error=str(exc),
233:             )
234:             self._log_quota_snapshot(context="meter_status_error")
235:             return None
236: 
237:         self._log_quota_snapshot(context="meter_status")
238: 
239:         body = response.get("body", {})
240:         temperature = body.get("temperature")
241:         humidity = body.get("humidity")
242: 
243:         self._update_state(
244:             last_temperature=temperature,
245:             last_humidity=humidity,
246:             last_read_at=_utc_now_iso(),
247:             last_error=None,
248:             last_temperature_stale=False,
249:             last_temperature_stale_reason=None,
250:         )
251:         self._debug(
252:             "Meter reading stored",
253:             trigger=trigger,
254:             temperature=temperature,
255:             humidity=humidity,
256:         )
257:         return {"temperature": temperature, "humidity": humidity}
258: 
259:     def _cooldown_active(self, now: dt.datetime) -> bool:
260:         state = self._state_store.read()
261:         settings = self._settings_store.read()
262:         
263:         assumed_power = state.get("assumed_aircon_power", "")
264:         
265:         if assumed_power == "on":
266:             cooldown_seconds = int(settings.get("action_on_cooldown_seconds", 0) or 0)
267:             cooldown_type = "ON"
268:         else:
269:             cooldown_seconds = int(settings.get("action_off_cooldown_seconds", 0) or 0)
270:             cooldown_type = "OFF"
271:         
272:         if cooldown_seconds <= 0:
273:             default_cooldown = int(settings.get("command_cooldown_seconds", 0) or 0)
274:             if default_cooldown <= 0:
275:                 return False
276:             cooldown_seconds = default_cooldown
277:             cooldown_type = "default"
278: 
279:         last_action_at = state.get("last_action_at")
280:         if not isinstance(last_action_at, str) or not last_action_at:
281:             return False
282: 
283:         try:
284:             last = dt.datetime.fromisoformat(last_action_at.replace("Z", "+00:00"))
285:         except ValueError:
286:             return False
287: 
288:         if last.tzinfo is None:
289:             last = last.replace(tzinfo=dt.timezone.utc)
290: 
291:         now_utc = now.astimezone(dt.timezone.utc)
292:         elapsed = now_utc - last
293:         remaining = dt.timedelta(seconds=cooldown_seconds) - elapsed
294:         
295:         if remaining > dt.timedelta(0):
296:             remaining_minutes = int(remaining.total_seconds() / 60)
297:             remaining_seconds = int(remaining.total_seconds() % 60)
298:             self._debug(
299:                 f"Cooldown active ({cooldown_type} action)",
300:                 remaining_time=f"{remaining_minutes}m{remaining_seconds}s",
301:                 cooldown_seconds=cooldown_seconds,
302:             )
303:             return True
304:         
305:         return False
306: 
307:     def _send_aircon_off(self, aircon_device_id: str, *, trigger: str, reason: str, force: bool = False) -> bool:
308:         aircon_device_id = aircon_device_id.strip()
309:         if not aircon_device_id:
310:             self._warning("Cannot send turnOff: missing aircon_device_id", trigger=trigger, reason=reason)
311:             self._update_state(last_error="Missing aircon_device_id for turnOff command")
312:             return False
313: 
314:         state = self._state_store.read()
315:         if not force and state.get("assumed_aircon_power") == "off":
316:             self._debug("Skipping turnOff: already assumed off", trigger=trigger, reason=reason)
317:             return False
318: 
319:         self._debug("Requesting aircon turnOff", trigger=trigger, aircon_device_id=aircon_device_id, reason=reason)
320:         self._client.send_command(aircon_device_id, command="turnOff", parameter="default")
321:         self._log_quota_snapshot(context="turn_off")
322:         self._update_state(
323:             assumed_aircon_power="off",
324:             last_action="turnOff",
325:             last_action_at=_utc_now_iso(),
326:             last_error=None,
327:         )
328:         return True
329: 
330:     def _send_aircon_setall(
331:         self,
332:         aircon_device_id: str,
333:         temperature: float,
334:         mode: int,
335:         fan_speed: int,
336:         power_state: str,
337:         *,
338:         trigger: str,
339:         reason: str,
340:     ) -> None:
341:         aircon_device_id = aircon_device_id.strip()
342:         if not aircon_device_id:
343:             self._warning("Cannot send setAll: missing aircon_device_id", trigger=trigger, reason=reason)
344:             self._update_state(last_error="Missing aircon_device_id for setAll command")
345:             return
346: 
347:         state = self._state_store.read()
348:         parameter = f"{temperature},{mode},{fan_speed},{power_state}"
349:         if (
350:             state.get("assumed_aircon_power") == power_state
351:             and state.get("assumed_aircon_mode") == mode
352:             and state.get("assumed_aircon_parameter") == parameter
353:         ):
354:             self._debug(
355:                 "Skipping setAll: desired state already assumed",
356:                 trigger=trigger,
357:                 aircon_device_id=aircon_device_id,
358:                 reason=reason,
359:                 parameter=parameter,
360:             )
361:             return
362: 
363:         self._debug(
364:             "Requesting aircon setAll",
365:             trigger=trigger,
366:             aircon_device_id=aircon_device_id,
367:             reason=reason,
368:             temperature=temperature,
369:             mode=mode,
370:             fan_speed=fan_speed,
371:             power_state=power_state,
372:         )
373:         self._client.send_command(
374:             aircon_device_id,
375:             command="setAll",
376:             parameter=parameter,
377:             command_type="command",
378:         )
379:         self._log_quota_snapshot(context="set_all")
380:         self._update_state(
381:             assumed_aircon_power=power_state,
382:             assumed_aircon_mode=mode,
383:             assumed_aircon_parameter=parameter,
384:             last_action=f"setAll({parameter})",
385:             last_action_at=_utc_now_iso(),
386:             last_error=None,
387:         )
388: 
389:     def _clear_off_repeat_task(self) -> None:
390:         state = self._state_store.read()
391:         if state.pop(OFF_REPEAT_STATE_KEY, None) is not None:
392:             self._state_store.write(state)
393:             self._debug("Cleared pending off repeat task")
394: 
395:     def _has_pending_off_repeat(self) -> bool:
396:         state = self._state_store.read()
397:         task = state.get(OFF_REPEAT_STATE_KEY)
398:         if not isinstance(task, dict):
399:             return False
400:         remaining = int(task.get("remaining", 0) or 0)
401:         return remaining > 0
402: 
403:     def _schedule_off_repeat_task(self, now: dt.datetime, *, state_reason: str) -> None:
404:         settings = self._settings_store.read()
405:         repeat_count = int(settings.get("off_repeat_count", 1) or 1)
406:         if repeat_count <= 1:
407:             self._clear_off_repeat_task()
408:             return
409: 
410:         interval_seconds = int(settings.get("off_repeat_interval_seconds", 10) or 10)
411:         if interval_seconds < 1:
412:             interval_seconds = 1
413: 
414:         remaining = repeat_count - 1
415:         next_run_at = (_ensure_utc(now) + dt.timedelta(seconds=interval_seconds)).isoformat()
416: 
417:         state = self._state_store.read()
418:         state[OFF_REPEAT_STATE_KEY] = {
419:             "remaining": remaining,
420:             "interval_seconds": interval_seconds,
421:             "next_run_at": next_run_at,
422:             "state_reason": state_reason,
423:         }
424:         self._state_store.write(state)
425:         self._debug(
426:             "Scheduled repeated off action",
427:             pending_repeats=remaining,
428:             interval_seconds=interval_seconds,
429:             state_reason=state_reason,
430:         )
431: 
432:     def _process_off_repeat_task(
433:         self,
434:         now: dt.datetime,
435:         *,
436:         trigger: str,
437:         webhooks: dict[str, str],
438:         scenes: dict[str, str],
439:         aircon_device_id: str,
440:     ) -> None:
441:         state = self._state_store.read()
442:         task = state.get(OFF_REPEAT_STATE_KEY)
443:         if not isinstance(task, dict):
444:             return
445: 
446:         remaining = int(task.get("remaining", 0) or 0)
447:         if remaining <= 0:
448:             self._clear_off_repeat_task()
449:             return
450: 
451:         next_run_raw = task.get("next_run_at")
452:         if not isinstance(next_run_raw, str):
453:             self._clear_off_repeat_task()
454:             return
455: 
456:         try:
457:             next_run_at = dt.datetime.fromisoformat(next_run_raw.replace("Z", "+00:00"))
458:         except ValueError:
459:             self._clear_off_repeat_task()
460:             return
461: 
462:         now_utc = _ensure_utc(now)
463:         if now_utc < _ensure_utc(next_run_at):
464:             return
465: 
466:         state_reason = str(task.get("state_reason", "automation_off_repeat")).strip() or "automation_off_repeat"
467:         interval_seconds = int(task.get("interval_seconds", 10) or 10)
468:         if interval_seconds < 1:
469:             interval_seconds = 1
470: 
471:         self._debug(
472:             "Executing scheduled off repeat",
473:             trigger=trigger,
474:             state_reason=state_reason,
475:             remaining_before=remaining,
476:         )
477: 
478:         success = self._perform_off_action(
479:             trigger=trigger,
480:             webhooks=webhooks,
481:             scenes=scenes,
482:             aircon_device_id=aircon_device_id,
483:             state_reason=state_reason,
484:             force_direct=True,
485:         )
486: 
487:         if not success:
488:             self._warning("Off repeat action failed; clearing schedule", trigger=trigger, state_reason=state_reason)
489:             self._clear_off_repeat_task()
490:             return
491: 
492:         remaining -= 1
493:         if remaining <= 0:
494:             self._clear_off_repeat_task()
495:             return
496: 
497:         next_run_at = (now_utc + dt.timedelta(seconds=interval_seconds)).isoformat()
498:         state = self._state_store.read()
499:         state[OFF_REPEAT_STATE_KEY] = {
500:             "remaining": remaining,
501:             "interval_seconds": interval_seconds,
502:             "next_run_at": next_run_at,
503:             "state_reason": state_reason,
504:         }
505:         self._state_store.write(state)
506:         self._debug(
507:             "Off repeat rescheduled",
508:             trigger=trigger,
509:             remaining=remaining,
510:             next_run_at=next_run_at,
511:         )
512: 
513:     def _perform_off_action(
514:         self,
515:         *,
516:         trigger: str,
517:         webhooks: dict[str, str],
518:         scenes: dict[str, str],
519:         aircon_device_id: str,
520:         state_reason: str,
521:         force_direct: bool = False,
522:     ) -> bool:
523:         if not force_direct:
524:             state = self._state_store.read()
525:             if state.get("assumed_aircon_power") == "off":
526:                 self._debug(
527:                     "Skipping off action: already assumed off",
528:                     trigger=trigger,
529:                     state_reason=state_reason,
530:                 )
531:                 return False
532: 
533:         handled = self._trigger_aircon_action(
534:             action_key="off",
535:             state_reason=state_reason,
536:             assumed_power="off",
537:             trigger=trigger,
538:             webhooks=webhooks,
539:             scenes=scenes,
540:             aircon_device_id=aircon_device_id,
541:         )
542:         if handled:
543:             return True
544: 
545:         if not aircon_device_id:
546:             return False
547: 
548:         try:
549:             return self._send_aircon_off(
550:                 aircon_device_id,
551:                 trigger=trigger,
552:                 reason=state_reason,
553:                 force=force_direct,
554:             )
555:         except SwitchBotApiError as exc:
556:             self._update_state(last_error=str(exc))
557:             self._error(
558:                 "SwitchBot API error during direct turnOff",
559:                 trigger=trigger,
560:                 error=str(exc),
561:                 state_reason=state_reason,
562:             )
563:             return False
564: 
565:     def _trigger_aircon_action(
566:         self,
567:         *,
568:         action_key: str,
569:         state_reason: str,
570:         assumed_power: str,
571:         trigger: str,
572:         webhooks: dict[str, str],
573:         scenes: dict[str, str],
574:         aircon_device_id: str = "",
575:     ) -> bool:
576:         webhook_url = webhooks.get(action_key, "").strip()
577:         scene_id = scenes.get(action_key, "").strip()
578:         aircon_device_id = aircon_device_id.strip()
579:         
580:         friendly_webhook = AIRCON_IFTTT_LABELS.get(action_key, action_key)
581:         friendly_scene = AIRCON_SCENE_LABELS.get(action_key, action_key)
582: 
583:         if webhook_url:
584:             self._debug(
585:                 "Triggering IFTTT webhook",
586:                 trigger=trigger,
587:                 action_key=action_key,
588:                 state_reason=state_reason,
589:             )
590:             try:
591:                 self._ifttt_client.trigger_webhook(webhook_url)
592:                 self._update_state(
593:                     assumed_aircon_power=assumed_power,
594:                     assumed_aircon_mode=None,
595:                     assumed_aircon_parameter=None,
596:                     last_action=f"ifttt_webhook({action_key}) ({state_reason})",
597:                     last_action_at=_utc_now_iso(),
598:                     last_error=None,
599:                 )
600:                 return True
601:             except IFTTTWebhookError as exc:
602:                 self._error(
603:                     "IFTTT webhook failed",
604:                     trigger=trigger,
605:                     action_key=action_key,
606:                     error=str(exc),
607:                 )
608:                 self._warning("Falling back to SwitchBot scene", trigger=trigger, action_key=action_key)
609: 
610:         if scene_id:
611:             self._debug(
612:                 "Using SwitchBot scene (webhook unavailable)",
613:                 trigger=trigger,
614:                 action_key=action_key,
615:                 scene_id=scene_id,
616:                 state_reason=state_reason,
617:             )
618:             try:
619:                 self._client.run_scene(scene_id)
620:                 self._log_quota_snapshot(context=f"scene_{action_key}")
621:                 self._update_state(
622:                     assumed_aircon_power=assumed_power,
623:                     assumed_aircon_mode=None,
624:                     assumed_aircon_parameter=None,
625:                     last_action=f"scene({scene_id}) ({state_reason})",
626:                     last_action_at=_utc_now_iso(),
627:                     last_error=None,
628:                 )
629:                 return True
630:             except SwitchBotApiError as exc:
631:                 self._error(
632:                     "Scene execution failed",
633:                     trigger=trigger,
634:                     action_key=action_key,
635:                     scene_id=scene_id,
636:                     error=str(exc),
637:                 )
638:                 if aircon_device_id:
639:                     self._warning(
640:                         "Falling back to direct command",
641:                         trigger=trigger,
642:                         action_key=action_key,
643:                     )
644:                 else:
645:                     self._update_state(last_error=str(exc))
646:                     return False
647: 
648:         if not webhook_url and not scene_id:
649:             self._update_state(last_error=f"Missing webhook and scene for {friendly_webhook}")
650:             self._warning(
651:                 "Skipping automation: no webhook or scene configured",
652:                 trigger=trigger,
653:                 action_key=action_key,
654:             )
655: 
656:         return False
657: 
658:     def run_once(self) -> None:
659:         trigger = self._detect_trigger_source()
660:         self._update_state(last_tick=_utc_now_iso())
661:         settings = self._settings_store.read()
662:         timezone_info, timezone_name = self._get_timezone(settings, trigger=trigger)
663:         now = dt.datetime.now(dt.timezone.utc).astimezone(timezone_info)
664:         poll_interval = int(settings.get("poll_interval_seconds", 0) or 0)
665:         automation_enabled = bool(settings.get("automation_enabled", False))
666:         outcome = "noop"
667: 
668:         scenes = extract_aircon_scenes(settings)
669:         webhooks = extract_ifttt_webhooks(settings)
670:         aircon_id = str(settings.get("aircon_device_id", "")).strip()
671: 
672:         self._debug(
673:             "Automation tick started",
674:             trigger=trigger,
675:             poll_interval_seconds=poll_interval,
676:             automation_enabled=automation_enabled,
677:             timezone=timezone_name,
678:             now_local=now.isoformat(),
679:         )
680: 
681:         self._process_off_repeat_task(
682:             now,
683:             trigger=trigger,
684:             webhooks=webhooks,
685:             scenes=scenes,
686:             aircon_device_id=aircon_id,
687:         )
688: 
689:         if not automation_enabled:
690:             self._debug("Automation disabled — polling meter only", trigger=trigger)
691:             self.poll_meter()
692:             self._log_tick_completion(trigger, outcome="disabled")
693:             return
694: 
695:         time_windows = settings.get("time_windows", [])
696:         if not isinstance(time_windows, list):
697:             time_windows = []
698: 
699:         in_window = _is_now_in_windows(time_windows, now)
700: 
701:         self._debug(
702:             "Time window evaluation",
703:             trigger=trigger,
704:             in_window=in_window,
705:             time_windows=_summarize_time_windows(time_windows),
706:             turn_off_outside_windows=bool(settings.get("turn_off_outside_windows", False)),
707:             timezone=timezone_name,
708:             now_local=now.isoformat(),
709:         )
710: 
711:         if not in_window:
712:             self._debug("Outside configured window — polling meter", trigger=trigger)
713:             self.poll_meter()
714:             if settings.get("turn_off_outside_windows", False):
715:                 state = self._state_store.read()
716:                 if state.get("assumed_aircon_power") == "off":
717:                     self._debug(
718:                         "Skipping off automation outside window: already assumed off",
719:                         trigger=trigger,
720:                     )
721:                     outcome = "already_off"
722:                 elif self._cooldown_active(now):
723:                     self._debug("Cooldown active, skipping off automation outside window", trigger=trigger)
724:                 else:
725:                     handled = self._perform_off_action(
726:                         trigger=trigger,
727:                         webhooks=webhooks,
728:                         scenes=scenes,
729:                         aircon_device_id=aircon_id,
730:                         state_reason="automation_off_outside_window",
731:                     )
732:                     if handled:
733:                         self._schedule_off_repeat_task(now, state_reason="automation_off_outside_window")
734:                         outcome = "turned_off_outside_window"
735:             else:
736:                 outcome = "outside_window"
737:             self._log_tick_completion(trigger, outcome=outcome)
738:             return
739: 
740:         reading = self.poll_meter()
741:         if not reading or reading.get("temperature") is None:
742:             self._debug("Meter reading unavailable; aborting automation tick", trigger=trigger)
743:             self._log_tick_completion(trigger, outcome="missing_meter")
744:             return
745: 
746:         try:
747:             current_temp = float(reading["temperature"])
748:         except (TypeError, ValueError):
749:             self._update_state(last_error="Invalid temperature reading")
750:             self._error("Invalid temperature reading returned by meter", trigger=trigger, value=reading.get("temperature"))
751:             self._log_tick_completion(trigger, outcome="invalid_temperature")
752:             return
753: 
754:         mode = str(settings.get("mode", "winter")).strip().lower()
755:         profile = settings.get(mode, {})
756:         if not isinstance(profile, dict):
757:             profile = {}
758: 
759:         hysteresis = float(settings.get("hysteresis_celsius", 0.0) or 0.0)
760: 
761:         try:
762:             min_temp = float(profile.get("min_temp"))
763:             max_temp = float(profile.get("max_temp"))
764:             target_temp = float(profile.get("target_temp"))
765:             ac_mode = int(profile.get("ac_mode"))
766:             fan_speed = int(profile.get("fan_speed"))
767:         except (TypeError, ValueError):
768:             self._update_state(last_error=f"Invalid profile configuration for mode: {mode}")
769:             self._error("Invalid automation profile configuration", trigger=trigger, mode=mode)
770:             self._log_tick_completion(trigger, outcome="invalid_profile")
771:             return
772: 
773:         if min_temp > max_temp:
774:             self._update_state(last_error=f"Invalid thresholds: min_temp > max_temp ({mode})")
775:             self._error("Invalid temperature thresholds", trigger=trigger, mode=mode, min_temp=min_temp, max_temp=max_temp)
776:             self._log_tick_completion(trigger, outcome="invalid_thresholds")
777:             return
778: 
779:         self._debug(
780:             "Temperature evaluation",
781:             trigger=trigger,
782:             mode=mode,
783:             current_temp=current_temp,
784:             min_temp=min_temp,
785:             max_temp=max_temp,
786:             hysteresis=hysteresis,
787:             target_temp=target_temp,
788:         )
789: 
790:         if self._cooldown_active(now):
791:             self._debug("Cooldown active — skipping automation", trigger=trigger)
792:             self._log_tick_completion(trigger, outcome="cooldown")
793:             return
794: 
795:         decision_taken = False
796: 
797:         try:
798:             if mode == "winter":
799:                 if current_temp <= (min_temp - hysteresis):
800:                     self._debug("Winter mode: below min threshold", trigger=trigger, threshold=min_temp - hysteresis)
801:                     self._clear_off_repeat_task()
802:                     executed = self._trigger_aircon_action(
803:                         action_key="winter",
804:                         state_reason="automation_winter_on",
805:                         assumed_power="on",
806:                         trigger=trigger,
807:                         webhooks=webhooks,
808:                         scenes=scenes,
809:                         aircon_device_id=aircon_id,
810:                     )
811:                     if not executed and aircon_id:
812:                         self._send_aircon_setall(
813:                             aircon_id,
814:                             temperature=target_temp,
815:                             mode=ac_mode,
816:                             fan_speed=fan_speed,
817:                             power_state="on",
818:                             trigger=trigger,
819:                             reason="automation_winter_on",
820:                         )
821:                     decision_taken = True
822:                     outcome = "winter_on"
823:                 elif current_temp >= (max_temp + hysteresis):
824:                     self._debug("Winter mode: above max threshold", trigger=trigger, threshold=max_temp + hysteresis)
825:                     state = self._state_store.read()
826:                     if state.get("assumed_aircon_power") == "off":
827:                         self._debug(
828:                             "Skipping winter_off: already assumed off",
829:                             trigger=trigger,
830:                         )
831:                         outcome = "already_off"
832:                     elif self._has_pending_off_repeat():
833:                         self._debug(
834:                             "Skipping winter_off: off repeat already pending",
835:                             trigger=trigger,
836:                         )
837:                         outcome = "off_repeat_pending"
838:                     else:
839:                         turned_off = self._perform_off_action(
840:                             trigger=trigger,
841:                             webhooks=webhooks,
842:                             scenes=scenes,
843:                             aircon_device_id=aircon_id,
844:                             state_reason="automation_winter_off",
845:                         )
846:                         if turned_off:
847:                             self._schedule_off_repeat_task(now, state_reason="automation_winter_off")
848:                             decision_taken = True
849:                             outcome = "winter_off"
850:             elif mode == "summer":
851:                 if current_temp >= (max_temp + hysteresis):
852:                     self._debug("Summer mode: above max threshold", trigger=trigger, threshold=max_temp + hysteresis)
853:                     self._clear_off_repeat_task()
854:                     executed = self._trigger_aircon_action(
855:                         action_key="summer",
856:                         state_reason="automation_summer_on",
857:                         assumed_power="on",
858:                         trigger=trigger,
859:                         webhooks=webhooks,
860:                         scenes=scenes,
861:                         aircon_device_id=aircon_id,
862:                     )
863:                     if not executed and aircon_id:
864:                         self._send_aircon_setall(
865:                             aircon_id,
866:                             temperature=target_temp,
867:                             mode=ac_mode,
868:                             fan_speed=fan_speed,
869:                             power_state="on",
870:                             trigger=trigger,
871:                             reason="automation_summer_on",
872:                         )
873:                     decision_taken = True
874:                     outcome = "summer_on"
875:                 elif current_temp <= (min_temp - hysteresis):
876:                     self._debug("Summer mode: below min threshold", trigger=trigger, threshold=min_temp - hysteresis)
877:                     state = self._state_store.read()
878:                     if state.get("assumed_aircon_power") == "off":
879:                         self._debug(
880:                             "Skipping summer_off: already assumed off",
881:                             trigger=trigger,
882:                         )
883:                         outcome = "already_off"
884:                     elif self._has_pending_off_repeat():
885:                         self._debug(
886:                             "Skipping summer_off: off repeat already pending",
887:                             trigger=trigger,
888:                         )
889:                         outcome = "off_repeat_pending"
890:                     else:
891:                         turned_off = self._perform_off_action(
892:                             trigger=trigger,
893:                             webhooks=webhooks,
894:                             scenes=scenes,
895:                             aircon_device_id=aircon_id,
896:                             state_reason="automation_summer_off",
897:                         )
898:                         if turned_off:
899:                             self._schedule_off_repeat_task(now, state_reason="automation_summer_off")
900:                             decision_taken = True
901:                             outcome = "summer_off"
902:             else:
903:                 self._update_state(last_error=f"Unknown mode: {mode}")
904:                 self._error("Unknown automation mode", trigger=trigger, mode=mode)
905:                 outcome = "invalid_mode"
906:         except SwitchBotApiError as exc:
907:             self._update_state(last_error=str(exc))
908:             self._error("SwitchBot API error during automation", trigger=trigger, error=str(exc))
909:             self._log_tick_completion(trigger, outcome="api_error")
910:             return
911: 
912:         if not decision_taken:
913:             self._debug("No automation action needed — thresholds not crossed", trigger=trigger)
914:             outcome = "no_action"
915: 
916:         self._log_tick_completion(trigger, outcome=outcome)
917:         
918:         if self._history_service:
919:             try:
920:                 current_state = self._state_store.read()
921:                 self._history_service.record_state(current_state, timezone_name)
922:             except Exception as exc:
923:                 self._warning("Failed to record state in history", trigger=trigger, error=str(exc))
924:             else:
925:                 try:
926:                     deleted = self._history_service.cleanup_old_records()
927:                     if deleted:
928:                         self._debug(
929:                             "Cleaned up old history records",
930:                             trigger=trigger,
931:                             deleted=deleted,
932:                         )
933:                 except Exception as exc:
934:                     self._warning("Failed to cleanup history records", trigger=trigger, error=str(exc))
```

## File: switchbot_dashboard/templates/index.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>SwitchBot Dashboard</title>
  7:     
  8:     <!-- Critical Theme Bootstrapping -->
  9:     <script>
 10:       (function() {
 11:         const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
 12:         const root = document.documentElement;
 13:         root.dataset.theme = 'dark';
 14:         root.style.setProperty('color-scheme', prefersDark ? 'dark' : 'light');
 15:       })();
 16:     </script>
 17:     
 18:     <!-- Critical CSS Inlined for LCP Optimization -->
 19:     <style>
 20:       /* Critical CSS - Above the Fold Content */
 21:       /* Optimized for LCP - Inline in <head> */
 22: 
 23:       /* Critical Reset & Base */
 24:       *,
 25:       *::before,
 26:       *::after {
 27:         box-sizing: border-box;
 28:       }
 29: 
 30:       html {
 31:         line-height: 1.15;
 32:         -webkit-text-size-adjust: 100%;
 33:       }
 34: 
 35:       body {
 36:         margin: 0;
 37:         font-family: "Space Grotesk", "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
 38:         font-size: 1rem;
 39:         font-weight: 400;
 40:         line-height: 1.5;
 41:         color: var(--sb-text);
 42:         background-color: var(--sb-bg);
 43:         min-height: 100vh;
 44:         padding-bottom: 80px;
 45:         padding-bottom: calc(80px + env(safe-area-inset-bottom));
 46:       }
 47: 
 48:       /* Override any possible light theme */
 49:       * {
 50:         background-color: inherit !important;
 51:       }
 52: 
 53: 
 54:       /* Critical Theme Variables */
 55:       :root {
 56:         color-scheme: dark;
 57:         --sb-bg: #030712;
 58:         --sb-gradient-start: #030712;
 59:         --sb-gradient-mid: #0a1227;
 60:         --sb-gradient-end: #101c35;
 61:         --sb-card: rgba(9, 14, 30, 0.92);
 62:         --sb-card-border: rgba(138, 180, 255, 0.2);
 63:         --sb-text: #f4f7ff;
 64:         --sb-muted: #aeb8d3;
 65:         --sb-accent: #8ab4ff;
 66:         --sb-accent-contrast: #051434;
 67:         --sb-shadow: 0 25px 60px rgba(2, 7, 20, 0.55);
 68:         --sb-outline: rgba(255, 255, 255, 0.08);
 69:         --sb-success: #6ee7b7;
 70:         --sb-danger: #ff6b81;
 71:         --sb-info: #4bc9f0;
 72:         --sb-warning: #f6c343;
 73:         --sb-success-bg: #0d4b39;
 74:         --sb-danger-bg: #611527;
 75:         --sb-info-bg: #0b3a57;
 76:         --sb-warning-bg: #5f370e;
 77:         --sb-alert-text: #f8fafc;
 78:       }
 79: 
 80:       /* Critical Layout */
 81:       .container {
 82:         width: 100%;
 83:         padding-right: 1rem;
 84:         padding-left: 1rem;
 85:         margin-right: auto;
 86:         margin-left: auto;
 87:         max-width: 1200px;
 88:       }
 89: 
 90:       .py-4 {
 91:         padding-top: 1.5rem;
 92:         padding-bottom: 1.5rem;
 93:       }
 94: 
 95:       .mb-4 {
 96:         margin-bottom: 1.5rem;
 97:       }
 98: 
 99:       .mb-3 {
100:         margin-bottom: 1rem;
101:       }
102: 
103:       .mb-0 {
104:         margin-bottom: 0 !important;
105:       }
106: 
107:       /* Critical Typography */
108:       .h3 {
109:         font-size: 1.75rem;
110:         font-weight: 600;
111:         line-height: 1.25;
112:         margin-bottom: 0.5rem;
113:       }
114: 
115:       .text-muted {
116:         color: var(--sb-muted) !important;
117:       }
118: 
119:       /* Critical Header */
120:       .page-header {
121:         display: flex;
122:         flex-direction: column;
123:         gap: 1rem;
124:         margin-bottom: 1.5rem;
125:       }
126: 
127:       @media (min-width: 768px) {
128:         .page-header {
129:           flex-direction: row;
130:           justify-content: space-between;
131:           align-items: flex-start;
132:         }
133:       }
134: 
135:       .page-header-main h1 {
136:         font-size: 1.75rem;
137:         font-weight: 600;
138:         line-height: 1.25;
139:         margin-bottom: 0;
140:         color: var(--sb-text);
141:       }
142: 
143:       .page-subtitle {
144:         color: var(--sb-muted);
145:         margin-bottom: 0;
146:       }
147: 
148:       /* Critical Navigation */
149:       .page-header-actions {
150:         display: flex;
151:         flex-wrap: wrap;
152:         gap: 0.5rem;
153:       }
154: 
155:       .btn {
156:         display: inline-block;
157:         font-weight: 400;
158:         line-height: 1.5;
159:         text-align: center;
160:         text-decoration: none;
161:         vertical-align: middle;
162:         cursor: pointer;
163:         user-select: none;
164:         background-color: transparent;
165:         border: 1px solid transparent;
166:         padding: 0.5rem 1rem;
167:         font-size: 0.875rem;
168:         border-radius: 0.375rem;
169:         transition: all 0.15s ease-in-out;
170:       }
171: 
172:       .btn-primary {
173:         color: #fff;
174:         background-color: var(--sb-accent);
175:         border-color: var(--sb-accent);
176:       }
177: 
178:       .btn-outline-primary {
179:         color: var(--sb-accent);
180:         border-color: var(--sb-accent);
181:       }
182: 
183:       .btn-outline-info {
184:         color: var(--sb-info);
185:         border-color: var(--sb-info);
186:       }
187: 
188:       .btn-outline-secondary {
189:         color: #6c757d;
190:         border-color: #6c757d;
191:       }
192: 
193:       /* Critical Alert Banner */
194:       .alert {
195:         position: relative;
196:         padding: 0.75rem 1.25rem;
197:         margin-bottom: 1rem;
198:         border: 1px solid transparent;
199:         border-radius: 0.375rem;
200:       }
201: 
202:       .alert-warning {
203:         color: var(--sb-alert-text);
204:         background-color: var(--sb-warning-bg);
205:         border-color: var(--sb-warning);
206:       }
207: 
208:       .quota-banner {
209:         display: flex;
210:         align-items: center;
211:         justify-content: space-between;
212:         flex-wrap: wrap;
213:         gap: 0.5rem;
214:       }
215: 
216:       .quota-banner__main {
217:         display: flex;
218:         flex-direction: column;
219:         gap: 0.25rem;
220:       }
221: 
222:       /* Critical Status Grid */
223:       .status-grid {
224:         display: grid;
225:         grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
226:         gap: 1rem;
227:         margin-bottom: 1.5rem;
228:       }
229: 
230:       .status-item {
231:         background: var(--sb-card);
232:         border: 1px solid var(--sb-card-border);
233:         border-radius: 0.75rem;
234:         padding: 1.25rem;
235:         backdrop-filter: blur(20px);
236:         box-shadow: var(--sb-shadow);
237:         transition: transform 0.2s ease, box-shadow 0.2s ease;
238:       }
239: 
240:       .status-item:hover {
241:         transform: translateY(-2px);
242:         box-shadow: 0 30px 70px rgba(2, 7, 20, 0.65);
243:       }
244: 
245:       .status-item h6 {
246:         font-size: 0.875rem;
247:         font-weight: 500;
248:         color: var(--sb-muted);
249:         margin-bottom: 0.5rem;
250:         text-transform: uppercase;
251:         letter-spacing: 0.05em;
252:       }
253: 
254:       .status-item .h4 {
255:         font-size: 2rem;
256:         font-weight: 600;
257:         margin-bottom: 0;
258:         color: var(--sb-text);
259:       }
260: 
261:       /* Critical Scene Actions */
262:       .scene-actions-wrapper {
263:         position: sticky;
264:         bottom: 1rem;
265:         background: var(--sb-card);
266:         border: 1px solid var(--sb-card-border);
267:         border-radius: 1.25rem;
268:         padding: 1rem;
269:         margin: 1rem -1rem -1rem;
270:         backdrop-filter: blur(20px);
271:         box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.4);
272:         z-index: 10;
273:       }
274: 
275:       .scene-actions {
276:         display: grid;
277:         grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
278:         gap: 0.75rem;
279:       }
280: 
281:       .scene-action {
282:         padding: 1rem;
283:         font-size: 1rem;
284:         font-weight: 500;
285:         border-radius: 0.75rem;
286:         text-align: center;
287:         transition: all 0.2s ease;
288:         min-height: 56px;
289:         display: flex;
290:         align-items: center;
291:         justify-content: center;
292:       }
293: 
294:       .btn-outline-success {
295:         color: var(--sb-success);
296:         border-color: var(--sb-success);
297:       }
298: 
299:       .btn-outline-danger {
300:         color: var(--sb-danger);
301:         border-color: var(--sb-danger);
302:       }
303: 
304:       /* Bottom Navigation - Let sticky-footer.css handle responsive behavior */
305:       #footer-bar {
306:         position: fixed;
307:         bottom: 0;
308:         left: 0;
309:         right: 0;
310:         height: 60px;
311:         background: var(--sb-card);
312:         border-top: 1px solid var(--sb-card-border);
313:         backdrop-filter: blur(20px);
314:         display: flex;
315:         justify-content: space-around;
316:         align-items: center;
317:         z-index: 102;
318:         box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.3);
319:         padding-bottom: env(safe-area-inset-bottom);
320:       }
321: 
322:       #footer-bar a {
323:         display: flex;
324:         flex-direction: column;
325:         align-items: center;
326:         justify-content: center;
327:         color: var(--sb-muted);
328:         text-decoration: none;
329:         font-size: 0.75rem;
330:         padding: 0.5rem;
331:         min-width: 44px;
332:         min-height: 44px;
333:         transition: color 0.2s ease;
334:       }
335: 
336:       #footer-bar a.active-nav {
337:         color: var(--sb-accent);
338:       }
339: 
340:       #footer-bar i {
341:         font-size: 1.25rem;
342:         margin-bottom: 0.25rem;
343:       }
344: 
345:       /* Critical GPU Optimization */
346:       .sb-gpu-accelerated {
347:         transform: translateZ(0);
348:         backface-visibility: hidden;
349:         perspective: 1000px;
350:       }
351: 
352:       /* Responsive - Let sticky-footer.css handle footer visibility */
353:       @media (max-width: 768px) {
354:         .container {
355:           padding-right: 0.75rem;
356:           padding-left: 0.75rem;
357:         }
358:         
359:         .page-header-actions {
360:           width: 100%;
361:         }
362:         
363:         .scene-actions {
364:           grid-template-columns: 1fr;
365:         }
366:       }
367: 
368:       /* Critical Reduced Motion */
369:       @media (prefers-reduced-motion: reduce) {
370:         *,
371:         *::before,
372:         *::after {
373:           animation-duration: 0.01ms !important;
374:           animation-iteration-count: 1 !important;
375:           transition-duration: 0.01ms !important;
376:         }
377:       }
378:       
379:       /* Prevent flash of unstyled content - Enhanced anti-flash */
380:       html, body {
381:         background-color: #030712 !important;
382:         color: #f4f7ff !important;
383:       }
384:       
385:       /* Allow transitions for smooth UX */
386:       .btn {
387:         transition: all 0.15s ease-in-out, transform 0.1s ease-out;
388:       }
389:       
390:       .btn:active {
391:         transform: scale(0.98);
392:       }
393:     </style>
394:     
395:     <!-- Preload Critical Resources -->
396:     <link rel="preload" href="{{ url_for('static', filename='css/theme.css') }}" as="style" onload="this.onload=null;this.rel='stylesheet'" />
397:     <link rel="preload" href="{{ url_for('static', filename='css/index.css') }}" as="style" onload="this.onload=null;this.rel='stylesheet'" />
398:     <link rel="preload" href="{{ url_for('static', filename='js/loaders.js') }}" as="script" />
399:     <link rel="preload" href="{{ url_for('static', filename='js/advanced-optimizer.js') }}" as="script" />
400:     <link rel="preload" href="{{ url_for('static', filename='vendor/css/bootstrap.min.css') }}" as="style" onload="this.onload=null;this.rel='stylesheet'" />
401:     <link rel="preload" href="{{ url_for('static', filename='vendor/css/space-grotesk.css') }}" as="style" onload="this.onload=null;this.rel='stylesheet'" />
402:     
403:     <!-- Vendor CSS -->
404:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/bootstrap.min.css') }}" />
405:     
406:     <!-- Non-Critical CSS (loaded after critical) -->
407:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-cards.css') }}" media="print" onload="this.media='all'" />
408:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" media="print" onload="this.media='all'" />
409:     
410:     <!-- Local Fonts & Icons -->
411:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/space-grotesk.css') }}" />
412:     <link rel="stylesheet" href="{{ url_for('static', filename='vendor/fontawesome/css/all.min.css') }}" />
413:     
414:     <!-- Critical JS for Performance -->
415:     <script>
416:       // Performance mark for critical resources start
417:       if ('performance' in window && 'mark' in performance) {
418:         performance.mark('critical-css-start');
419:       }
420:     </script>
421:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
422:     <link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}" />
423:   </head>
424:   <body class="sb-dark sb-page sb-dashboard">
425: 
426: <!-- Enhanced anti-flash script for body -->
427: <script>
428:   // Ensure dark theme is applied immediately when body loads
429:   document.body.style.backgroundColor = '#030712';
430:   document.body.style.color = '#f4f7ff';
431:   
432:   // Add dark theme class immediately
433:   document.body.classList.add('sb-dark');
434: </script>
435:     <div class="sb-page__gradient"></div>
436:     <main class="sb-page__content">
437:       <div class="container py-5 py-lg-6">
438:         <section class="sb-card sb-card-hero sb-card-hover mb-4" role="region" aria-label="Présentation SwitchBot">
439:           <div class="sb-card-hero__content">
440:             <div class="sb-card-hero__text">
441:               <p class="sb-card__eyebrow">Tableau de bord</p>
442:               <h1 class="sb-hero__title">SwitchBot Dashboard</h1>
443:               <p class="sb-hero__subtitle">
444:                 Surveillez l'état actuel, vos quotas et déclenchez les actions clés sans quitter cette page.
445:               </p>
446:             </div>
447:             <div class="sb-hero__cta">
448:               <a class="btn btn-outline-light sb-button-active" href="{{ url_for('dashboard.settings_page') }}" data-loader>
449:                 <i class="fas fa-sliders-h me-2"></i>
450:                 Voir les réglages
451:               </a>
452:               <a class="btn btn-primary sb-button-active" href="{{ url_for('dashboard.actions_page') }}" data-loader>
453:                 <i class="fas fa-bolt me-2"></i>
454:                 Actions rapides
455:               </a>
456:             </div>
457:           </div>
458:         </section>
459: 
460:         {% if show_quota_warning %}
461:           <section class="sb-card sb-card--warning sb-card-hover mb-3 quota-panel quota-banner" role="status">
462:             <div class="quota-panel__icon">
463:               <i class="fas fa-triangle-exclamation"></i>
464:             </div>
465:             <div class="quota-panel__content">
466:               <p class="quota-panel__title">Attention : quota API faible</p>
467:               <p class="quota-panel__subtitle">
468:                 Il ne reste que {{ api_requests_remaining }} appels (seuil {{ quota_warning_threshold }}).
469:               </p>
470:             </div>
471:             <div class="quota-panel__action">
472:               <a class="btn btn-outline-light btn-sm" href="{{ url_for('dashboard.quota') }}" data-loader>
473:                 Voir le quota
474:               </a>
475:             </div>
476:           </section>
477:         {% endif %}
478: 
479:         {% with messages = get_flashed_messages(with_categories=true) %}
480:           {% if messages %}
481:             <section class="mb-3" aria-live="polite" aria-atomic="true">
482:               {% for category, message in messages %}
483:                 <article class="alert {{ 'alert-danger' if category == 'error' else 'alert-success' }}" role="alert" data-auto-dismiss="6000">
484:                   {{ message }}
485:                 </article>
486:               {% endfor %}
487:             </section>
488:           {% endif %}
489:         {% endwith %}
490: 
491:         <section class="sb-card sb-card-hover mb-4">
492:           <form method="post" action="{{ url_for('dashboard.run_once') }}" class="run-once-form" data-loader>
493:             {{ csrf_field() if csrf_field is defined }}
494:             <div class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-3">
495:               <div>
496:                 <p class="sb-card__eyebrow mb-1">Automatisation</p>
497:                 <h2 class="sb-card__title mb-0">Lancer un cycle manuel</h2>
498:                 <p class="text-muted mb-0">Déclenche un tick immédiat pour rafraîchir les données et appliquer les règles.</p>
499:               </div>
500:               <button type="submit" class="btn btn-outline-light btn-lg">
501:                 <i class="fas fa-sync-alt me-2"></i>
502:                 Exécuter maintenant
503:               </button>
504:             </div>
505:           </form>
506:         </section>
507: 
508:         <section class="sb-card sb-card-hover mb-4">
509:           <div class="sb-card__header">
510:             <div>
511:               <p class="sb-card__eyebrow">Statut actuel</p>
512:               <h2 class="sb-card__title">Données en temps réel</h2>
513:             </div>
514:             <div class="sb-card__meta text-muted">Dernière mise à jour {{ state.get('last_read_at') }}</div>
515:           </div>
516:           <div class="sb-card__body">
517:             <div class="status-grid">
518:               <article class="status-item sb-card-hover">
519:                 <div class="status-label">Température</div>
520:                 <div class="status-value temperature-value">
521:                   {{ state.get('last_temperature') }}
522:                 </div>
523:                 {% if state.get('last_temperature_stale') %}
524:                   <span class="badge bg-secondary-subtle text-secondary-emphasis status-badge">
525:                     Donnée potentiellement obsolète
526:                   </span>
527:                 {% endif %}
528:               </article>
529: 
530:               <article class="status-item sb-card-hover">
531:                 <div class="status-label">Humidité</div>
532:                 <div class="status-value humidity-value">
533:                   {{ state.get('last_humidity') }}
534:                 </div>
535:               </article>
536: 
537:               <article class="status-item sb-card-hover">
538:                 <div class="status-label">Climatisation supposée</div>
539:                 <div class="status-value">
540:                   {% if state.get('assumed_aircon_power') == 'on' %}
541:                     <span class="text-success">ON</span>
542:                   {% else %}
543:                     <span class="text-secondary">OFF</span>
544:                   {% endif %}
545:                 </div>
546:                 <p class="status-value--muted mb-0">
547:                   {{ state.get('last_action') or 'Aucune action' }}
548:                 </p>
549:               </article>
550: 
551:               <article class="status-item sb-card-hover">
552:                 <div class="status-label">Dernière erreur</div>
553:                 <div class="status-value status-value--muted">
554:                   {{ state.get('last_error') or 'Aucune erreur' }}
555:                 </div>
556:               </article>
557: 
558:               <article class="status-item sb-card-hover">
559:                 <div class="status-label">Dernière lecture</div>
560:                 <div class="status-value">
561:                   {{ state.get('last_read_at') or 'N/A' }}
562:                 </div>
563:               </article>
564:             </div>
565:           </div>
566:         </section>
567: 
568:         <section class="scene-actions-wrapper sb-card sb-card-hover">
569:           <div class="scene-actions-container text-center">
570:             <p class="text-muted mb-0 scene-actions__subtitle">
571:               <i class="fas fa-bolt me-2"></i>
572:               Accédez à toutes les actions manuelles via la page <strong>Actions</strong>
573:             </p>
574:             <a href="{{ url_for('dashboard.actions_page') }}" class="btn btn-primary rounded-m shadow-l" data-loader>
575:               <i class="fas fa-arrow-right me-2"></i>
576:               Voir les actions
577:             </a>
578:           </div>
579:         </section>
580:       </div>
581:     </main>
582:     
583:     {% include '_footer_nav.html' %}
584:     
585:     <script src="{{ url_for('static', filename='js/alerts.js') }}"></script>
586:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
587:     <script src="{{ url_for('static', filename='js/bottom-nav.js') }}"></script>
588:     <script src="{{ url_for('static', filename='js/performance-optimizer.js') }}"></script>
589:     <script src="{{ url_for('static', filename='js/advanced-optimizer.js') }}"></script>
590:     
591:     <!-- Enhanced Performance Optimization Script -->
592:     <script>
593:       // Mark critical CSS loading complete
594:       if ('performance' in window && 'mark' in performance) {
595:         performance.mark('critical-css-loaded');
596:         performance.measure('critical-css-load-time', 'critical-css-start', 'critical-css-loaded');
597:       }
598:       
599:       // Initialize advanced performance optimizations
600:       if ('requestIdleCallback' in window) {
601:         requestIdleCallback(() => {
602:           console.log('🚀 Advanced Performance Optimizer initialized');
603:         });
604:       }
605:       
606:       // Ensure dark theme is maintained after load
607:       window.addEventListener('load', function() {
608:         document.body.style.backgroundColor = '#030712';
609:         document.body.style.color = '#f4f7ff';
610:       });
611:     </script>
612:   </body>
613: </html>
```

## File: switchbot_dashboard/routes.py
```python
   1: from __future__ import annotations
   2: 
   3: import datetime as dt
   4: import json
   5: from typing import Any
   6: from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
   7: 
   8: from flask import (
   9:     Blueprint,
  10:     current_app,
  11:     flash,
  12:     redirect,
  13:     render_template,
  14:     request,
  15:     url_for,
  16:     abort,
  17: )
  18: 
  19: from .config_store import StoreError
  20: from .ifttt import IFTTTWebhookError, extract_ifttt_webhooks
  21: from .switchbot_api import SwitchBotApiError
  22: 
  23: 
  24: dashboard_bp = Blueprint("dashboard", __name__)
  25: 
  26: 
  27: DAY_CHOICES: list[dict[str, Any]] = [
  28:     {"value": 0, "label": "Mon"},
  29:     {"value": 1, "label": "Tue"},
  30:     {"value": 2, "label": "Wed"},
  31:     {"value": 3, "label": "Thu"},
  32:     {"value": 4, "label": "Fri"},
  33:     {"value": 5, "label": "Sat"},
  34:     {"value": 6, "label": "Sun"},
  35: ]
  36: 
  37: 
  38: def _build_time_choices(step_minutes: int = 30) -> list[str]:
  39:     """Generate 24h slot labels spaced by ``step_minutes`` for the time-window dropdowns rendered in index.html."""
  40:     values: list[str] = []
  41:     total_minutes = 24 * 60
  42:     for minutes in range(0, total_minutes, step_minutes):
  43:         hour = minutes // 60
  44:         minute = minutes % 60
  45:         values.append(f"{hour:02d}:{minute:02d}")
  46:     return values
  47: 
  48: 
  49: TIME_CHOICES = _build_time_choices()
  50: 
  51: 
  52: def _build_temp_choices(start: float = 14.0, end: float = 32.0, step: float = 0.5) -> list[dict[str, Any]]:
  53:     """Produce half-degree temperature options shared by the Winter/Summer dropdowns to keep the UI and validators aligned."""
  54:     values: list[dict[str, Any]] = []
  55:     scaled_start = int(start * 2)
  56:     scaled_end = int(end * 2)
  57:     scaled_step = max(1, int(step * 2))
  58:     for scaled in range(scaled_start, scaled_end + 1, scaled_step):
  59:         numeric_value = scaled / 2
  60:         label = f"{numeric_value:.1f}".rstrip("0").rstrip(".")
  61:         if label == "":
  62:             label = "0"
  63:         values.append({"value": numeric_value, "label": label})
  64:     return values
  65: 
  66: 
  67: TEMP_CHOICES = _build_temp_choices()
  68: 
  69: FAN_SPEED_CHOICES: list[dict[str, Any]] = [
  70:     {"value": 1, "label": "Auto"},
  71:     {"value": 2, "label": "Low"},
  72:     {"value": 3, "label": "Medium"},
  73:     {"value": 4, "label": "High"},
  74: ]
  75: 
  76: AC_MODE_CHOICES: list[dict[str, Any]] = [
  77:     {"value": 1, "label": "Auto"},
  78:     {"value": 2, "label": "Cool"},
  79:     {"value": 3, "label": "Dry"},
  80:     {"value": 4, "label": "Fan"},
  81:     {"value": 5, "label": "Heat"},
  82: ]
  83: 
  84: AIRCON_SCENE_KEYS: tuple[str, ...] = ("winter", "summer", "fan", "off")
  85: AIRCON_SCENE_LABELS: dict[str, str] = {
  86:     "winter": "Aircon ON – Hiver",
  87:     "summer": "Aircon ON – Été",
  88:     "fan": "Aircon ON – Mode neutre",
  89:     "off": "Aircon OFF – Scène",
  90: }
  91: DEFAULT_QUOTA_WARNING_THRESHOLD = 250
  92: DEFAULT_TIMEZONE = "Europe/Paris"
  93: 
  94: 
  95: def _utc_now_iso() -> str:
  96:     return dt.datetime.now(dt.timezone.utc).isoformat()
  97: 
  98: 
  99: def _parse_iso_datetime(value: str) -> dt.datetime | None:
 100:     raw = value.strip()
 101:     if not raw:
 102:         return None
 103:     if raw.endswith("Z"):
 104:         raw = raw[:-1] + "+00:00"
 105:     try:
 106:         parsed = dt.datetime.fromisoformat(raw)
 107:     except ValueError:
 108:         return None
 109:     if parsed.tzinfo is None:
 110:         return parsed.replace(tzinfo=dt.timezone.utc)
 111:     return parsed
 112: 
 113: 
 114: def _resolve_timezone(settings: dict[str, Any]) -> dt.tzinfo:
 115:     raw_timezone = settings.get("timezone")
 116:     timezone_name = str(raw_timezone or "").strip() or DEFAULT_TIMEZONE
 117:     try:
 118:         return ZoneInfo(timezone_name)
 119:     except ZoneInfoNotFoundError:
 120:         return dt.timezone.utc
 121: 
 122: 
 123: def _localize_iso_timestamp(value: Any, timezone: dt.tzinfo) -> str | None:
 124:     if not isinstance(value, str):
 125:         return None
 126:     parsed = _parse_iso_datetime(value)
 127:     if parsed is None:
 128:         return None
 129:     return parsed.astimezone(timezone).isoformat()
 130: 
 131: 
 132: def _as_bool(value: Any) -> bool:
 133:     if value is None:
 134:         return False
 135: 
 136:     if isinstance(value, bool):
 137:         return value
 138: 
 139:     return str(value).strip().lower() in {"1", "true", "yes", "on"}
 140: 
 141: 
 142: def _as_int(value: Any, default: int, minimum: int | None = None, maximum: int | None = None) -> int:
 143:     try:
 144:         parsed = int(value)
 145:     except (TypeError, ValueError):
 146:         return default
 147: 
 148:     if minimum is not None and parsed < minimum:
 149:         return minimum
 150: 
 151:     if maximum is not None and parsed > maximum:
 152:         return maximum
 153: 
 154:     return parsed
 155: 
 156: 
 157: def _as_float(
 158:     value: Any,
 159:     default: float,
 160:     minimum: float | None = None,
 161:     maximum: float | None = None,
 162: ) -> float:
 163:     try:
 164:         parsed = float(value)
 165:     except (TypeError, ValueError):
 166:         return default
 167: 
 168:     if minimum is not None and parsed < minimum:
 169:         return minimum
 170: 
 171:     if maximum is not None and parsed > maximum:
 172:         return maximum
 173: 
 174:     return parsed
 175: 
 176: 
 177: def _get_time_window_form(settings: dict[str, Any]) -> dict[str, Any]:
 178:     windows = settings.get("time_windows", [])
 179:     window = windows[0] if windows else {}
 180:     raw_days = window.get("days", [])
 181:     days: list[int] = []
 182:     if isinstance(raw_days, list):
 183:         for token in raw_days:
 184:             try:
 185:                 day = int(token)
 186:             except (TypeError, ValueError):
 187:                 continue
 188:             if 0 <= day <= 6:
 189:                 days.append(day)
 190: 
 191:     return {
 192:         "days": days,
 193:         "start": window.get("start", ""),
 194:         "end": window.get("end", ""),
 195:     }
 196: 
 197: 
 198: def _extract_aircon_scenes(settings: dict[str, Any]) -> dict[str, str]:
 199:     raw_scenes = settings.get("aircon_scenes", {})
 200:     if not isinstance(raw_scenes, dict):
 201:         raw_scenes = {}
 202: 
 203:     sanitized: dict[str, str] = {}
 204:     for key in AIRCON_SCENE_KEYS:
 205:         value = raw_scenes.get(key, "")
 206:         sanitized[key] = str(value).strip() if isinstance(value, str) else ""
 207:     return sanitized
 208: 
 209: 
 210: def _extract_ifttt_webhooks(settings: dict[str, Any]) -> dict[str, str]:
 211:     return extract_ifttt_webhooks(settings)
 212: 
 213: 
 214: def _build_quota_context(settings: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
 215:     api_requests_remaining = state.get("api_requests_remaining")
 216:     api_requests_total = state.get("api_requests_total")
 217:     api_requests_limit = state.get("api_requests_limit")
 218:     api_quota_reset_at = state.get("api_quota_reset_at")
 219: 
 220:     raw_threshold = settings.get("api_quota_warning_threshold", DEFAULT_QUOTA_WARNING_THRESHOLD)
 221:     try:
 222:         quota_warning_threshold = int(raw_threshold)
 223:     except (TypeError, ValueError):
 224:         quota_warning_threshold = DEFAULT_QUOTA_WARNING_THRESHOLD
 225:     if quota_warning_threshold < 0:
 226:         quota_warning_threshold = 0
 227: 
 228:     show_quota_warning = (
 229:         quota_warning_threshold > 0
 230:         and isinstance(api_requests_remaining, (int, float))
 231:         and api_requests_remaining is not None
 232:         and api_requests_remaining <= quota_warning_threshold
 233:     )
 234: 
 235:     return {
 236:         "api_requests_remaining": api_requests_remaining,
 237:         "api_requests_total": api_requests_total,
 238:         "api_requests_limit": api_requests_limit,
 239:         "api_quota_day": state.get("api_quota_day"),
 240:         "api_quota_reset_at": api_quota_reset_at,
 241:         "quota_warning_threshold": quota_warning_threshold,
 242:         "show_quota_warning": show_quota_warning,
 243:     }
 244: 
 245: 
 246: def _build_scenes_context(settings: dict[str, Any]) -> tuple[dict[str, str], dict[str, bool]]:
 247:     aircon_scenes = _extract_aircon_scenes(settings)
 248:     missing_scenes = {key: not aircon_scenes[key] for key in AIRCON_SCENE_KEYS}
 249:     return aircon_scenes, missing_scenes
 250: 
 251: 
 252: @dashboard_bp.get("/")
 253: def index() -> str:
 254:     settings_store = current_app.extensions["settings_store"]
 255:     state_store = current_app.extensions["state_store"]
 256: 
 257:     settings = settings_store.read()
 258:     state = state_store.read()
 259:     timezone = _resolve_timezone(settings)
 260:     state_for_view = dict(state)
 261:     localized_last_read_at = _localize_iso_timestamp(state.get("last_read_at"), timezone)
 262:     if localized_last_read_at is not None:
 263:         state_for_view["last_read_at"] = localized_last_read_at
 264:     quota_context = _build_quota_context(settings, state)
 265:     aircon_scenes, missing_scenes = _build_scenes_context(settings)
 266:     ifttt_webhooks = _extract_ifttt_webhooks(settings)
 267:     missing_webhooks = {key: not ifttt_webhooks[key] for key in AIRCON_SCENE_KEYS}
 268: 
 269:     return render_template(
 270:         "index.html",
 271:         state=state_for_view,
 272:         settings=settings,
 273:         **quota_context,
 274:         aircon_scenes=aircon_scenes,
 275:         missing_scenes=missing_scenes,
 276:         ifttt_webhooks=ifttt_webhooks,
 277:         missing_webhooks=missing_webhooks,
 278:         aircon_scene_labels=AIRCON_SCENE_LABELS,
 279:         aircon_scene_keys=AIRCON_SCENE_KEYS,
 280:     )
 281: 
 282: 
 283: @dashboard_bp.get("/reglages")
 284: def settings_page() -> str:
 285:     settings_store = current_app.extensions["settings_store"]
 286:     state_store = current_app.extensions["state_store"]
 287: 
 288:     settings = settings_store.read()
 289:     state = state_store.read()
 290:     time_window_form = _get_time_window_form(settings)
 291:     quota_context = _build_quota_context(settings, state)
 292:     aircon_scenes, missing_scenes = _build_scenes_context(settings)
 293:     ifttt_webhooks = _extract_ifttt_webhooks(settings)
 294:     missing_webhooks = {key: not ifttt_webhooks[key] for key in AIRCON_SCENE_KEYS}
 295: 
 296:     configured_scenes_count = sum(1 for value in aircon_scenes.values() if value)
 297:     configured_webhooks_count = sum(1 for value in ifttt_webhooks.values() if value)
 298: 
 299:     return render_template(
 300:         "settings.html",
 301:         settings=settings,
 302:         aircon_scenes=aircon_scenes,
 303:         missing_scenes=missing_scenes,
 304:         ifttt_webhooks=ifttt_webhooks,
 305:         missing_webhooks=missing_webhooks,
 306:         aircon_scene_labels=AIRCON_SCENE_LABELS,
 307:         time_window_form=time_window_form,
 308:         day_choices=DAY_CHOICES,
 309:         time_choices=TIME_CHOICES,
 310:         temp_choices=TEMP_CHOICES,
 311:         fan_speed_choices=FAN_SPEED_CHOICES,
 312:         ac_mode_choices=AC_MODE_CHOICES,
 313:         aircon_scene_keys=AIRCON_SCENE_KEYS,
 314:         quota_warning_threshold=quota_context["quota_warning_threshold"],
 315:         configured_scenes_count=configured_scenes_count,
 316:         configured_webhooks_count=configured_webhooks_count,
 317:     )
 318: 
 319: 
 320: @dashboard_bp.get("/quota")
 321: def quota() -> str:
 322:     settings_store = current_app.extensions["settings_store"]
 323:     state_store = current_app.extensions["state_store"]
 324: 
 325:     settings = settings_store.read()
 326:     state = state_store.read()
 327:     quota_context = _build_quota_context(settings, state)
 328: 
 329:     return render_template("quota.html", **quota_context)
 330: 
 331: 
 332: @dashboard_bp.post("/quota/refresh")
 333: def quota_refresh() -> Any:
 334:     quota_tracker = current_app.extensions.get("quota_tracker")
 335:     if quota_tracker is None:
 336:         flash("Suivi de quota indisponible.", "error")
 337:         return redirect(url_for("dashboard.quota"))
 338: 
 339:     quota_tracker.record_call()
 340:     quota_tracker.refresh_snapshot()
 341:     flash("Quota mis à jour.", "success")
 342:     return redirect(url_for("dashboard.quota"))
 343: 
 344: 
 345: @dashboard_bp.get("/debug/state")
 346: def debug_state() -> Any:
 347:     expected_token = current_app.config.get("STATE_DEBUG_TOKEN")
 348:     provided_token = request.args.get("token")
 349: 
 350:     if not expected_token or provided_token != expected_token:
 351:         abort(404)
 352: 
 353:     state_store = current_app.extensions["state_store"]
 354:     state = state_store.read()
 355: 
 356:     return current_app.response_class(
 357:         json.dumps(state, indent=2, ensure_ascii=False) + "\n",
 358:         mimetype="application/json",
 359:     )
 360: 
 361: 
 362: @dashboard_bp.get("/healthz")
 363: def healthz() -> Any:
 364:     app = current_app
 365:     settings_store = app.extensions["settings_store"]
 366:     state_store = app.extensions["state_store"]
 367:     scheduler_service = app.extensions["scheduler_service"]
 368: 
 369:     timestamp = _utc_now_iso()
 370: 
 371:     try:
 372:         settings = settings_store.read()
 373:         state = state_store.read()
 374:         scheduler_running = bool(scheduler_service.is_running())
 375:         automation_enabled = bool(settings.get("automation_enabled", False))
 376:         last_tick = state.get("last_tick")
 377:     except StoreError as exc:
 378:         app.logger.error("[health] store error: %s", exc)
 379:         payload = {
 380:             "status": "error",
 381:             "details": "store_unavailable",
 382:             "timestamp_utc": timestamp,
 383:         }
 384:         return app.response_class(
 385:             json.dumps(payload) + "\n", mimetype="application/json", status=503
 386:         )
 387:     except Exception as exc:  # pragma: no cover - defensive fallback
 388:         app.logger.exception("[health] unexpected failure")
 389:         payload = {
 390:             "status": "error",
 391:             "details": "unexpected_failure",
 392:             "timestamp_utc": timestamp,
 393:         }
 394:         return app.response_class(
 395:             json.dumps(payload) + "\n", mimetype="application/json", status=503
 396:         )
 397: 
 398:     payload = {
 399:         "status": "ok",
 400:         "scheduler_running": scheduler_running,
 401:         "automation_enabled": automation_enabled,
 402:         "last_tick": last_tick,
 403:         "timestamp_utc": timestamp,
 404:     }
 405:     return app.response_class(
 406:         json.dumps(payload) + "\n", mimetype="application/json", status=200
 407:     )
 408: 
 409: 
 410: @dashboard_bp.post("/settings")
 411: def update_settings() -> Any:
 412:     """Handle settings form submission and validation.
 413: 
 414:     Processes form data from the settings page, validates all inputs,
 415:     and persists changes to the settings store.
 416: 
 417:     Returns:
 418:         Redirect to settings page with success or error flash messages
 419: 
 420:     Raises:
 421:         StoreError: If settings cannot be read or written
 422:     """
 423:     settings_store = current_app.extensions["settings_store"]
 424:     scheduler_service = current_app.extensions["scheduler_service"]
 425: 
 426:     settings = settings_store.read()
 427:     current_aircon_scenes = _extract_aircon_scenes(settings)
 428: 
 429:     settings["automation_enabled"] = _as_bool(request.form.get("automation_enabled"))
 430:     settings["mode"] = str(request.form.get("mode", settings.get("mode", "winter"))).strip().lower()
 431: 
 432:     settings["poll_interval_seconds"] = _as_int(
 433:         request.form.get("poll_interval_seconds"),
 434:         default=int(settings.get("poll_interval_seconds", 120) or 120),
 435:         minimum=15,
 436:         maximum=3600,
 437:     )
 438: 
 439:     settings["adaptive_polling_enabled"] = _as_bool(
 440:         request.form.get("adaptive_polling_enabled", settings.get("adaptive_polling_enabled", True))
 441:     )
 442:     settings["idle_poll_interval_seconds"] = _as_int(
 443:         request.form.get("idle_poll_interval_seconds"),
 444:         default=int(settings.get("idle_poll_interval_seconds", 600) or 600),
 445:         minimum=15,
 446:         maximum=86_400,
 447:     )
 448:     settings["poll_warmup_minutes"] = _as_int(
 449:         request.form.get("poll_warmup_minutes"),
 450:         default=int(settings.get("poll_warmup_minutes", 15) or 15),
 451:         minimum=0,
 452:         maximum=24 * 60,
 453:     )
 454: 
 455:     settings["hysteresis_celsius"] = _as_float(
 456:         request.form.get("hysteresis_celsius"),
 457:         default=float(settings.get("hysteresis_celsius", 0.3) or 0.3),
 458:         minimum=0.0,
 459:         maximum=5.0,
 460:     )
 461: 
 462:     settings["command_cooldown_seconds"] = _as_int(
 463:         request.form.get("command_cooldown_seconds"),
 464:         default=int(settings.get("command_cooldown_seconds", 180) or 180),
 465:         minimum=0,
 466:         maximum=3600,
 467:     )
 468:     settings["action_on_cooldown_seconds"] = _as_int(
 469:         request.form.get("action_on_cooldown_seconds"),
 470:         default=int(settings.get("action_on_cooldown_seconds", 0) or 0),
 471:         minimum=0,
 472:         maximum=3600,
 473:     )
 474:     settings["action_off_cooldown_seconds"] = _as_int(
 475:         request.form.get("action_off_cooldown_seconds"),
 476:         default=int(settings.get("action_off_cooldown_seconds", 0) or 0),
 477:         minimum=0,
 478:         maximum=3600,
 479:     )
 480:     settings["off_repeat_count"] = _as_int(
 481:         request.form.get("off_repeat_count"),
 482:         default=int(settings.get("off_repeat_count", 1) or 1),
 483:         minimum=1,
 484:         maximum=10,
 485:     )
 486:     settings["off_repeat_interval_seconds"] = _as_int(
 487:         request.form.get("off_repeat_interval_seconds"),
 488:         default=int(settings.get("off_repeat_interval_seconds", 10) or 10),
 489:         minimum=1,
 490:         maximum=600,
 491:     )
 492: 
 493:     settings["turn_off_outside_windows"] = _as_bool(request.form.get("turn_off_outside_windows"))
 494: 
 495:     timezone_raw = request.form.get("timezone")
 496:     if timezone_raw is None:
 497:         settings.setdefault("timezone", DEFAULT_TIMEZONE)
 498:     else:
 499:         requested_timezone = str(timezone_raw).strip() or DEFAULT_TIMEZONE
 500:         try:
 501:             ZoneInfo(requested_timezone)
 502:         except ZoneInfoNotFoundError:
 503:             flash(
 504:                 "Fuseau horaire invalide : utilisez un identifiant IANA (ex: Europe/Paris, UTC).",
 505:                 "error",
 506:             )
 507:         else:
 508:             settings["timezone"] = requested_timezone
 509: 
 510:     settings["api_quota_warning_threshold"] = _as_int(
 511:         request.form.get("api_quota_warning_threshold"),
 512:         default=int(settings.get("api_quota_warning_threshold", DEFAULT_QUOTA_WARNING_THRESHOLD) or DEFAULT_QUOTA_WARNING_THRESHOLD),
 513:         minimum=0,
 514:         maximum=10_000,
 515:     )
 516: 
 517:     settings["meter_device_id"] = str(request.form.get("meter_device_id", "")).strip()
 518:     settings["aircon_device_id"] = str(request.form.get("aircon_device_id", "")).strip()
 519: 
 520:     time_window_days_raw = request.form.getlist("time_window_days")
 521:     time_window_start = request.form.get("time_window_start", "").strip()
 522:     time_window_end = request.form.get("time_window_end", "").strip()
 523: 
 524:     if time_window_days_raw or time_window_start or time_window_end:
 525:         try:
 526:             parsed_days = [
 527:                 int(token.strip())
 528:                 for token in time_window_days_raw
 529:                 if token.strip() != ""
 530:             ]
 531:         except ValueError:
 532:             parsed_days = []
 533: 
 534:         parsed_days = sorted({day for day in parsed_days if 0 <= day <= 6})
 535: 
 536:         if parsed_days and time_window_start and time_window_end:
 537:             settings["time_windows"] = [
 538:                 {
 539:                     "days": parsed_days,
 540:                     "start": time_window_start,
 541:                     "end": time_window_end,
 542:                 }
 543:             ]
 544:         else:
 545:             flash(
 546:                 "Fenêtre horaire invalide : les jours doivent être compris entre 0 et 6 et les heures de début/fin sont obligatoires.",
 547:                 "error",
 548:             )
 549:     else:
 550:         settings["time_windows"] = []
 551: 
 552:     for key in ("winter", "summer"):
 553:         profile = settings.get(key, {})
 554:         if not isinstance(profile, dict):
 555:             profile = {}
 556: 
 557:         profile["min_temp"] = _as_float(request.form.get(f"{key}_min_temp"), default=float(profile.get("min_temp", 0.0) or 0.0))
 558:         profile["max_temp"] = _as_float(request.form.get(f"{key}_max_temp"), default=float(profile.get("max_temp", 0.0) or 0.0))
 559:         profile["target_temp"] = _as_float(request.form.get(f"{key}_target_temp"), default=float(profile.get("target_temp", 0.0) or 0.0))
 560:         profile["fan_speed"] = _as_int(request.form.get(f"{key}_fan_speed"), default=int(profile.get("fan_speed", 3) or 3), minimum=1, maximum=4)
 561:         profile["ac_mode"] = _as_int(request.form.get(f"{key}_ac_mode"), default=int(profile.get("ac_mode", 5 if key == "winter" else 2) or 0), minimum=0, maximum=5)
 562: 
 563:         settings[key] = profile
 564: 
 565:     updated_aircon_scenes: dict[str, str] = {}
 566:     for key in AIRCON_SCENE_KEYS:
 567:         updated_aircon_scenes[key] = str(
 568:             request.form.get(f"scene_{key}_id", current_aircon_scenes.get(key, ""))
 569:         ).strip()
 570: 
 571:     settings["aircon_scenes"] = updated_aircon_scenes
 572: 
 573:     current_webhooks = _extract_ifttt_webhooks(settings)
 574:     updated_webhooks: dict[str, str] = {}
 575:     for key in AIRCON_SCENE_KEYS:
 576:         updated_webhooks[key] = str(
 577:             request.form.get(f"webhook_{key}_url", current_webhooks.get(key, ""))
 578:         ).strip()
 579: 
 580:     settings["ifttt_webhooks"] = updated_webhooks
 581: 
 582:     settings_store.write(settings)
 583:     scheduler_service.reschedule()
 584: 
 585:     flash("Paramètres enregistrés.")
 586:     return redirect(url_for("dashboard.index"))
 587: 
 588: 
 589: @dashboard_bp.route("/actions/run_once", methods=["GET", "POST"])
 590: def run_once() -> Any:
 591:     """Execute a single automation cycle manually.
 592: 
 593:     Triggers the automation service to run one complete cycle
 594:     of temperature monitoring and device control.
 595: 
 596:     Returns:
 597:         Redirect to home page with success flash message
 598:     """
 599:     automation_service = current_app.extensions["automation_service"]
 600: 
 601:     automation_service.run_once()
 602:     flash("Cycle d'automatisation exécuté.")
 603:     return redirect(url_for("dashboard.index"))
 604: 
 605: 
 606: @dashboard_bp.post("/actions/aircon_off")
 607: def aircon_off() -> Any:
 608:     return _execute_aircon_action(
 609:         "off",
 610:         state_reason="manual_off",
 611:         flash_label="Climatisation arrêtée.",
 612:         assumed_power="off",
 613:     )
 614: 
 615: 
 616: def _execute_aircon_action(
 617:     action_key: str,
 618:     *,
 619:     state_reason: str,
 620:     flash_label: str,
 621:     assumed_power: str = "unknown",
 622: ) -> Any:
 623:     settings_store = current_app.extensions["settings_store"]
 624:     state_store = current_app.extensions["state_store"]
 625:     client = current_app.extensions["switchbot_client"]
 626:     ifttt_client = current_app.extensions["ifttt_client"]
 627: 
 628:     settings = settings_store.read()
 629:     webhooks = _extract_ifttt_webhooks(settings)
 630:     scenes = _extract_aircon_scenes(settings)
 631:     aircon_id = str(settings.get("aircon_device_id", "")).strip()
 632: 
 633:     webhook_url = webhooks.get(action_key, "").strip()
 634:     scene_id = scenes.get(action_key, "").strip()
 635: 
 636:     if webhook_url:
 637:         try:
 638:             ifttt_client.trigger_webhook(webhook_url)
 639:             state = state_store.read()
 640:             state["assumed_aircon_power"] = assumed_power
 641:             state["assumed_aircon_mode"] = None
 642:             state["assumed_aircon_parameter"] = None
 643:             state["last_action"] = f"ifttt_webhook({action_key}) ({state_reason})"
 644:             state["last_action_at"] = _utc_now_iso()
 645:             state["last_error"] = None
 646:             state_store.write(state)
 647:             flash(flash_label)
 648:             return redirect(url_for("dashboard.index"))
 649:         except IFTTTWebhookError as exc:
 650:             current_app.logger.warning(f"IFTTT webhook failed for {action_key}: {exc}. Falling back to scene.")
 651: 
 652:     if scene_id:
 653:         try:
 654:             client.run_scene(scene_id)
 655:             state = state_store.read()
 656:             state["assumed_aircon_power"] = assumed_power
 657:             state["assumed_aircon_mode"] = None
 658:             state["assumed_aircon_parameter"] = None
 659:             state["last_action"] = f"scene({scene_id}) ({state_reason})"
 660:             state["last_action_at"] = _utc_now_iso()
 661:             state["last_error"] = None
 662:             state_store.write(state)
 663:             flash(flash_label)
 664:             return redirect(url_for("dashboard.index"))
 665:         except SwitchBotApiError as exc:
 666:             if not aircon_id:
 667:                 state = state_store.read()
 668:                 state["last_error"] = str(exc)
 669:                 state_store.write(state)
 670:                 flash(str(exc), "error")
 671:                 return redirect(url_for("dashboard.index"))
 672:             current_app.logger.warning(f"Scene execution failed for {action_key}: {exc}. Falling back to direct command.")
 673: 
 674:     if not webhook_url and not scene_id:
 675:         action_label = AIRCON_SCENE_LABELS.get(action_key, action_key)
 676:         flash(f"Aucun webhook ou scène configuré pour {action_label}", "error")
 677:         return redirect(url_for("dashboard.index"))
 678: 
 679:     if action_key == "off":
 680:         if not aircon_id:
 681:             flash("aircon_device_id manquant", "error")
 682:             return redirect(url_for("dashboard.index"))
 683:         try:
 684:             client.send_command(aircon_id, command="turnOff", parameter="default", command_type="command")
 685:             state = state_store.read()
 686:             state["assumed_aircon_power"] = "off"
 687:             state["assumed_aircon_mode"] = None
 688:             state["assumed_aircon_parameter"] = None
 689:             state["last_action"] = f"turnOff ({state_reason})"
 690:             state["last_action_at"] = _utc_now_iso()
 691:             state["last_error"] = None
 692:             state_store.write(state)
 693:             flash(flash_label)
 694:             return redirect(url_for("dashboard.index"))
 695:         except SwitchBotApiError as exc:
 696:             state = state_store.read()
 697:             state["last_error"] = str(exc)
 698:             state_store.write(state)
 699:             flash(str(exc), "error")
 700:             return redirect(url_for("dashboard.index"))
 701:     else:
 702:         flash(f"Impossible d'exécuter l'action {action_key} : aucune méthode disponible", "error")
 703:         return redirect(url_for("dashboard.index"))
 704: 
 705: 
 706: @dashboard_bp.post("/actions/aircon_on")
 707: def aircon_on() -> Any:
 708:     """Route to the current mode scene for backward compatibility."""
 709:     settings_store = current_app.extensions["settings_store"]
 710:     settings = settings_store.read()
 711:     mode = str(settings.get("mode", "winter")).strip().lower()
 712:     scene_key = mode if mode in AIRCON_SCENE_KEYS else "winter"
 713:     return _execute_aircon_action(
 714:         scene_key,
 715:         state_reason=f"manual_{scene_key}",
 716:         flash_label=f"Action {scene_key} exécutée.",
 717:     )
 718: 
 719: 
 720: @dashboard_bp.post("/actions/aircon_on_winter")
 721: def aircon_on_winter() -> Any:
 722:     return _execute_aircon_action(
 723:         "winter",
 724:         state_reason="manual_winter",
 725:         flash_label="Mode hiver activé.",
 726:         assumed_power="on",
 727:     )
 728: 
 729: 
 730: @dashboard_bp.post("/actions/aircon_on_summer")
 731: def aircon_on_summer() -> Any:
 732:     return _execute_aircon_action(
 733:         "summer",
 734:         state_reason="manual_summer",
 735:         flash_label="Mode été activé.",
 736:         assumed_power="on",
 737:     )
 738: 
 739: 
 740: @dashboard_bp.post("/actions/aircon_on_fan")
 741: def aircon_on_fan() -> Any:
 742:     return _execute_aircon_action(
 743:         "fan",
 744:         state_reason="manual_fan",
 745:         flash_label="Mode ventilateur activé.",
 746:         assumed_power="on",
 747:     )
 748: 
 749: 
 750: @dashboard_bp.get("/devices")
 751: def devices() -> str:
 752:     client = current_app.extensions["switchbot_client"]
 753: 
 754:     data = None
 755:     error = None
 756: 
 757:     try:
 758:         data = client.get_devices()
 759:     except SwitchBotApiError as exc:
 760:         error = str(exc)
 761: 
 762:     return render_template("devices.html", data=data, error=error)
 763: 
 764: 
 765: @dashboard_bp.post("/actions/quick_off")
 766: def quick_off() -> Any:
 767:     settings_store = current_app.extensions["settings_store"]
 768:     
 769:     settings = settings_store.read()
 770:     settings["automation_enabled"] = False
 771:     settings_store.write(settings)
 772:     
 773:     return _execute_aircon_action(
 774:         "off",
 775:         state_reason="quick_off",
 776:         flash_label="Automatisation désactivée et climatisation éteinte.",
 777:         assumed_power="off",
 778:     )
 779: 
 780: 
 781: @dashboard_bp.get("/history")
 782: def history_page() -> str:
 783:     return render_template("history.html")
 784: 
 785: 
 786: @dashboard_bp.get("/actions")
 787: def actions_page() -> str:
 788:     settings_store = current_app.extensions["settings_store"]
 789:     state_store = current_app.extensions["state_store"]
 790:     
 791:     try:
 792:         settings = settings_store.read()
 793:     except StoreError:
 794:         settings = {}
 795:     
 796:     try:
 797:         state = state_store.read()
 798:     except StoreError:
 799:         state = {}
 800:     
 801:     # Get scene configuration for status display
 802:     aircon_scenes = settings.get("aircon_scenes", {})
 803:     missing_scenes = {
 804:         key: not aircon_scenes.get(key)
 805:         for key in ["winter", "summer", "fan", "off"]
 806:     }
 807:     
 808:     return render_template(
 809:         "actions.html",
 810:         settings=settings,
 811:         state=state,
 812:         missing_scenes=missing_scenes,
 813:     )
 814: 
 815: 
 816: @dashboard_bp.get("/history/api/data")
 817: def history_api_data() -> Any:
 818:     history_service = current_app.extensions.get("history_service")
 819:     if not history_service:
 820:         # Return mock data when service is not available
 821:         import random
 822:         
 823:         end = dt.datetime.now(dt.timezone.utc)
 824:         start = end - dt.timedelta(hours=6)
 825:         mock_data = []
 826:         
 827:         current = start
 828:         while current <= end:
 829:             mock_data.append({
 830:                 "timestamp": current.isoformat() + "Z",
 831:                 "temperature": round(20 + random.random() * 10, 1),
 832:                 "humidity": round(40 + random.random() * 20, 1),
 833:                 "assumed_aircon_power": random.choice(["on", "off", "unknown"]),
 834:                 "last_action": random.choice(["automation_winter_on", "automation_summer_on", "automation_winter_off", None]),
 835:                 "api_requests_today": random.randint(100, 200),
 836:                 "error_count": random.randint(0, 2)
 837:             })
 838:             current += timedelta(minutes=5)
 839:         
 840:         return {
 841:             "data": mock_data,
 842:             "start": start.isoformat() + "Z",
 843:             "end": end.isoformat() + "Z",
 844:             "granularity": "minute",
 845:             "metrics": ["temperature", "humidity", "assumed_aircon_power"],
 846:             "count": len(mock_data),
 847:             "mock": True
 848:         }
 849: 
 850:     try:
 851:         # Parse query parameters
 852:         start_str = request.args.get("start")
 853:         end_str = request.args.get("end")
 854:         metrics_param = request.args.get("metrics")
 855:         granularity = request.args.get("granularity", "minute")
 856:         limit = int(request.args.get("limit", 1000))
 857: 
 858:         # Parse metrics parameter (can be comma-separated string or list)
 859:         metrics = []
 860:         if metrics_param:
 861:             if isinstance(metrics_param, str):
 862:                 metrics = [m.strip() for m in metrics_param.split(",") if m.strip()]
 863:             else:
 864:                 metrics = metrics_param
 865: 
 866:         # Default to last 6 hours if no time range specified
 867:         if not start_str or not end_str:
 868:             end = dt.datetime.now(dt.timezone.utc)
 869:             start = end - dt.timedelta(hours=6)
 870:         else:
 871:             start = dt.datetime.fromisoformat(start_str.replace("Z", "+00:00"))
 872:             end = dt.datetime.fromisoformat(end_str.replace("Z", "+00:00"))
 873: 
 874:         # Validate granularity
 875:         valid_granularities = ["minute", "5min", "15min", "hour"]
 876:         if granularity not in valid_granularities:
 877:             granularity = "minute"
 878: 
 879:         # Get historical data
 880:         data = history_service.get_history(start, end, metrics, granularity, limit)
 881:         
 882:         # Return empty data structure if no data found
 883:         if not data:
 884:             return {
 885:                 "data": [],
 886:                 "start": start.isoformat(),
 887:                 "end": end.isoformat(),
 888:                 "granularity": granularity,
 889:                 "metrics": metrics or ["timestamp", "temperature", "humidity", "assumed_aircon_power"],
 890:                 "count": 0,
 891:                 "message": "No historical data available yet"
 892:             }
 893:         
 894:         return {
 895:             "data": data,
 896:             "start": start.isoformat(),
 897:             "end": end.isoformat(),
 898:             "granularity": granularity,
 899:             "metrics": metrics or ["timestamp", "temperature", "humidity", "assumed_aircon_power"],
 900:             "count": len(data),
 901:         }
 902: 
 903:     except ValueError as exc:
 904:         return {"error": f"Invalid parameters: {exc}"}, 400
 905:     except Exception as exc:
 906:         current_app.logger.error(f"[history] API error: {exc}")
 907:         # Return empty data structure on error to avoid breaking the frontend
 908:         return {
 909:             "data": [],
 910:             "start": start.isoformat() if 'start' in locals() else dt.datetime.now(dt.timezone.utc).isoformat(),
 911:             "end": end.isoformat() if 'end' in locals() else dt.datetime.now(dt.timezone.utc).isoformat(),
 912:             "granularity": "minute",
 913:             "metrics": ["timestamp", "temperature", "humidity", "assumed_aircon_power"],
 914:             "count": 0,
 915:             "message": "Error retrieving data"
 916:         }
 917: 
 918: 
 919: @dashboard_bp.get("/history/api/aggregates")
 920: def history_api_aggregates() -> Any:
 921:     """API endpoint for aggregated statistics."""
 922:     history_service = current_app.extensions.get("history_service")
 923:     if not history_service:
 924:         # Return mock aggregates when service is not available
 925:         import random
 926:         
 927:         return {
 928:             "period_hours": 6,
 929:             "aggregates": {
 930:                 "total_records": random.randint(50, 100),
 931:                 "avg_temperature": round(20 + random.random() * 10, 1),
 932:                 "min_temperature": round(18 + random.random() * 2, 1),
 933:                 "max_temperature": round(28 + random.random() * 2, 1),
 934:                 "avg_humidity": round(40 + random.random() * 20, 1),
 935:                 "min_humidity": round(35 + random.random() * 5, 1),
 936:                 "max_humidity": round(60 + random.random() * 5, 1),
 937:                 "common_aircon_state": random.choice(["on", "off"]),
 938:                 "distinct_actions": random.randint(2, 4),
 939:                 "total_errors": random.randint(0, 5),
 940:                 "max_api_requests": random.randint(150, 250)
 941:             },
 942:             "mock": True
 943:         }
 944: 
 945:     try:
 946:         period_hours = int(request.args.get("period_hours", 1))
 947:         if period_hours < 1 or period_hours > 24:
 948:             period_hours = 1
 949: 
 950:         aggregates = history_service.get_aggregates(period_hours)
 951:         
 952:         # Return empty aggregates if no data
 953:         if not aggregates:
 954:             return {
 955:                 "period_hours": period_hours,
 956:                 "aggregates": {
 957:                     "total_records": 0,
 958:                     "avg_temperature": 0,
 959:                     "min_temperature": 0,
 960:                     "max_temperature": 0,
 961:                     "avg_humidity": 0,
 962:                     "min_humidity": 0,
 963:                     "max_humidity": 0,
 964:                     "common_aircon_state": "unknown",
 965:                     "distinct_actions": 0,
 966:                     "total_errors": 0,
 967:                     "max_api_requests": 0
 968:                 },
 969:                 "message": "No historical data available yet"
 970:             }
 971:         
 972:         return {
 973:             "period_hours": period_hours,
 974:             "aggregates": aggregates,
 975:         }
 976: 
 977:     except Exception as exc:
 978:         current_app.logger.error(f"[history] Aggregates API error: {exc}")
 979:         # Return empty aggregates on error to avoid breaking the frontend
 980:         return {
 981:             "period_hours": 1,
 982:             "aggregates": {
 983:                 "total_records": 0,
 984:                 "avg_temperature": 0,
 985:                 "min_temperature": 0,
 986:                 "max_temperature": 0,
 987:                 "avg_humidity": 0,
 988:                 "min_humidity": 0,
 989:                 "max_humidity": 0,
 990:                 "common_aircon_state": "unknown",
 991:                 "distinct_actions": 0,
 992:                 "total_errors": 0,
 993:                 "max_api_requests": 0
 994:             },
 995:             "message": "Error retrieving data"
 996:         }
 997: 
 998: 
 999: @dashboard_bp.get("/history/api/latest")
1000: def history_api_latest() -> Any:
1001:     history_service = current_app.extensions.get("history_service")
1002:     if not history_service:
1003:         # Return mock latest records when service is not available
1004:         import random
1005:         
1006:         mock_latest = []
1007:         for i in range(10):
1008:             timestamp = dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=i * 5)
1009:             mock_latest.append({
1010:                 "id": i + 1,
1011:                 "timestamp": timestamp.isoformat() + "Z",
1012:                 "temperature": round(20 + random.random() * 10, 1),
1013:                 "humidity": round(40 + random.random() * 20, 1),
1014:                 "assumed_aircon_power": random.choice(["on", "off", "unknown"]),
1015:                 "last_action": random.choice(["automation_winter_on", "automation_summer_on", "automation_winter_off", None]),
1016:                 "error_count": random.randint(0, 2),
1017:                 "metadata": {
1018:                     "last_read_at": timestamp.isoformat() + "Z",
1019:                     "automation_active": random.choice([True, False])
1020:                 }
1021:             })
1022:         
1023:         return {
1024:             "latest": mock_latest,
1025:             "count": len(mock_latest),
1026:             "mock": True
1027:         }
1028: 
1029:     try:
1030:         limit = int(request.args.get("limit", 10))
1031:         if limit < 1 or limit > 100:
1032:             limit = 10
1033: 
1034:         latest = history_service.get_latest_records(limit)
1035:         
1036:         # Return empty latest if no data
1037:         if not latest:
1038:             return {
1039:                 "latest": [],
1040:                 "count": 0,
1041:                 "message": "No historical data available yet"
1042:             }
1043:         
1044:         return {
1045:             "latest": latest,
1046:             "count": len(latest),
1047:         }
1048: 
1049:     except Exception as exc:
1050:         current_app.logger.error(f"[history] Latest API error: {exc}")
1051:         # Return empty latest on error to avoid breaking the frontend
1052:         return {
1053:             "latest": [],
1054:             "count": 0,
1055:             "message": "Error retrieving data"
1056:         }
```
