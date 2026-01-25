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
- Files matching these patterns are excluded: .git/**, .github/**, memory-bank/**, .windsurf/**, node_modules/**, venv*/**, .venv/**, __pycache__/**, *.pyc, *.pyo, *.log, *.sqlite3, .pytest_cache/**, coverage/**, repomix-output.*, docs/repomix.md
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
    vendor/
      css/
        bootstrap.min.css
        space-grotesk.css
      fontawesome/
        css/
          all.min.css
        webfonts/
          fa-brands-400.ttf
          fa-brands-400.woff2
          fa-solid-900.ttf
          fa-solid-900.woff2
      fonts/
        SpaceGrotesk-Medium.ttf
        SpaceGrotesk-Regular.ttf
        SpaceGrotesk-SemiBold.ttf
      js/
        chart.umd.min.js
        chartjs-adapter-date-fns.bundle.min.js
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

## File: switchbot_dashboard/static/vendor/css/bootstrap.min.css
```css
1: @charset "UTF-8";/*!
2:  * Bootstrap  v5.3.2 (https://getbootstrap.com/)
3:  * Copyright 2011-2023 The Bootstrap Authors
4:  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
5:  */:root,[data-bs-theme=light]{--bs-blue:#0d6efd;--bs-indigo:#6610f2;--bs-purple:#6f42c1;--bs-pink:#d63384;--bs-red:#dc3545;--bs-orange:#fd7e14;--bs-yellow:#ffc107;--bs-green:#198754;--bs-teal:#20c997;--bs-cyan:#0dcaf0;--bs-black:#000;--bs-white:#fff;--bs-gray:#6c757d;--bs-gray-dark:#343a40;--bs-gray-100:#f8f9fa;--bs-gray-200:#e9ecef;--bs-gray-300:#dee2e6;--bs-gray-400:#ced4da;--bs-gray-500:#adb5bd;--bs-gray-600:#6c757d;--bs-gray-700:#495057;--bs-gray-800:#343a40;--bs-gray-900:#212529;--bs-primary:#0d6efd;--bs-secondary:#6c757d;--bs-success:#198754;--bs-info:#0dcaf0;--bs-warning:#ffc107;--bs-danger:#dc3545;--bs-light:#f8f9fa;--bs-dark:#212529;--bs-primary-rgb:13,110,253;--bs-secondary-rgb:108,117,125;--bs-success-rgb:25,135,84;--bs-info-rgb:13,202,240;--bs-warning-rgb:255,193,7;--bs-danger-rgb:220,53,69;--bs-light-rgb:248,249,250;--bs-dark-rgb:33,37,41;--bs-primary-text-emphasis:#052c65;--bs-secondary-text-emphasis:#2b2f32;--bs-success-text-emphasis:#0a3622;--bs-info-text-emphasis:#055160;--bs-warning-text-emphasis:#664d03;--bs-danger-text-emphasis:#58151c;--bs-light-text-emphasis:#495057;--bs-dark-text-emphasis:#495057;--bs-primary-bg-subtle:#cfe2ff;--bs-secondary-bg-subtle:#e2e3e5;--bs-success-bg-subtle:#d1e7dd;--bs-info-bg-subtle:#cff4fc;--bs-warning-bg-subtle:#fff3cd;--bs-danger-bg-subtle:#f8d7da;--bs-light-bg-subtle:#fcfcfd;--bs-dark-bg-subtle:#ced4da;--bs-primary-border-subtle:#9ec5fe;--bs-secondary-border-subtle:#c4c8cb;--bs-success-border-subtle:#a3cfbb;--bs-info-border-subtle:#9eeaf9;--bs-warning-border-subtle:#ffe69c;--bs-danger-border-subtle:#f1aeb5;--bs-light-border-subtle:#e9ecef;--bs-dark-border-subtle:#adb5bd;--bs-white-rgb:255,255,255;--bs-black-rgb:0,0,0;--bs-font-sans-serif:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans","Liberation Sans",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";--bs-font-monospace:SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;--bs-gradient:linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));--bs-body-font-family:var(--bs-font-sans-serif);--bs-body-font-size:1rem;--bs-body-font-weight:400;--bs-body-line-height:1.5;--bs-body-color:#212529;--bs-body-color-rgb:33,37,41;--bs-body-bg:#fff;--bs-body-bg-rgb:255,255,255;--bs-emphasis-color:#000;--bs-emphasis-color-rgb:0,0,0;--bs-secondary-color:rgba(33, 37, 41, 0.75);--bs-secondary-color-rgb:33,37,41;--bs-secondary-bg:#e9ecef;--bs-secondary-bg-rgb:233,236,239;--bs-tertiary-color:rgba(33, 37, 41, 0.5);--bs-tertiary-color-rgb:33,37,41;--bs-tertiary-bg:#f8f9fa;--bs-tertiary-bg-rgb:248,249,250;--bs-heading-color:inherit;--bs-link-color:#0d6efd;--bs-link-color-rgb:13,110,253;--bs-link-decoration:underline;--bs-link-hover-color:#0a58ca;--bs-link-hover-color-rgb:10,88,202;--bs-code-color:#d63384;--bs-highlight-color:#212529;--bs-highlight-bg:#fff3cd;--bs-border-width:1px;--bs-border-style:solid;--bs-border-color:#dee2e6;--bs-border-color-translucent:rgba(0, 0, 0, 0.175);--bs-border-radius:0.375rem;--bs-border-radius-sm:0.25rem;--bs-border-radius-lg:0.5rem;--bs-border-radius-xl:1rem;--bs-border-radius-xxl:2rem;--bs-border-radius-2xl:var(--bs-border-radius-xxl);--bs-border-radius-pill:50rem;--bs-box-shadow:0 0.5rem 1rem rgba(0, 0, 0, 0.15);--bs-box-shadow-sm:0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);--bs-box-shadow-lg:0 1rem 3rem rgba(0, 0, 0, 0.175);--bs-box-shadow-inset:inset 0 1px 2px rgba(0, 0, 0, 0.075);--bs-focus-ring-width:0.25rem;--bs-focus-ring-opacity:0.25;--bs-focus-ring-color:rgba(13, 110, 253, 0.25);--bs-form-valid-color:#198754;--bs-form-valid-border-color:#198754;--bs-form-invalid-color:#dc3545;--bs-form-invalid-border-color:#dc3545}[data-bs-theme=dark]{color-scheme:dark;--bs-body-color:#dee2e6;--bs-body-color-rgb:222,226,230;--bs-body-bg:#212529;--bs-body-bg-rgb:33,37,41;--bs-emphasis-color:#fff;--bs-emphasis-color-rgb:255,255,255;--bs-secondary-color:rgba(222, 226, 230, 0.75);--bs-secondary-color-rgb:222,226,230;--bs-secondary-bg:#343a40;--bs-secondary-bg-rgb:52,58,64;--bs-tertiary-color:rgba(222, 226, 230, 0.5);--bs-tertiary-color-rgb:222,226,230;--bs-tertiary-bg:#2b3035;--bs-tertiary-bg-rgb:43,48,53;--bs-primary-text-emphasis:#6ea8fe;--bs-secondary-text-emphasis:#a7acb1;--bs-success-text-emphasis:#75b798;--bs-info-text-emphasis:#6edff6;--bs-warning-text-emphasis:#ffda6a;--bs-danger-text-emphasis:#ea868f;--bs-light-text-emphasis:#f8f9fa;--bs-dark-text-emphasis:#dee2e6;--bs-primary-bg-subtle:#031633;--bs-secondary-bg-subtle:#161719;--bs-success-bg-subtle:#051b11;--bs-info-bg-subtle:#032830;--bs-warning-bg-subtle:#332701;--bs-danger-bg-subtle:#2c0b0e;--bs-light-bg-subtle:#343a40;--bs-dark-bg-subtle:#1a1d20;--bs-primary-border-subtle:#084298;--bs-secondary-border-subtle:#41464b;--bs-success-border-subtle:#0f5132;--bs-info-border-subtle:#087990;--bs-warning-border-subtle:#997404;--bs-danger-border-subtle:#842029;--bs-light-border-subtle:#495057;--bs-dark-border-subtle:#343a40;--bs-heading-color:inherit;--bs-link-color:#6ea8fe;--bs-link-hover-color:#8bb9fe;--bs-link-color-rgb:110,168,254;--bs-link-hover-color-rgb:139,185,254;--bs-code-color:#e685b5;--bs-highlight-color:#dee2e6;--bs-highlight-bg:#664d03;--bs-border-color:#495057;--bs-border-color-translucent:rgba(255, 255, 255, 0.15);--bs-form-valid-color:#75b798;--bs-form-valid-border-color:#75b798;--bs-form-invalid-color:#ea868f;--bs-form-invalid-border-color:#ea868f}*,::after,::before{box-sizing:border-box}@media (prefers-reduced-motion:no-preference){:root{scroll-behavior:smooth}}body{margin:0;font-family:var(--bs-body-font-family);font-size:var(--bs-body-font-size);font-weight:var(--bs-body-font-weight);line-height:var(--bs-body-line-height);color:var(--bs-body-color);text-align:var(--bs-body-text-align);background-color:var(--bs-body-bg);-webkit-text-size-adjust:100%;-webkit-tap-highlight-color:transparent}hr{margin:1rem 0;color:inherit;border:0;border-top:var(--bs-border-width) solid;opacity:.25}.h1,.h2,.h3,.h4,.h5,.h6,h1,h2,h3,h4,h5,h6{margin-top:0;margin-bottom:.5rem;font-weight:500;line-height:1.2;color:var(--bs-heading-color)}.h1,h1{font-size:calc(1.375rem + 1.5vw)}@media (min-width:1200px){.h1,h1{font-size:2.5rem}}.h2,h2{font-size:calc(1.325rem + .9vw)}@media (min-width:1200px){.h2,h2{font-size:2rem}}.h3,h3{font-size:calc(1.3rem + .6vw)}@media (min-width:1200px){.h3,h3{font-size:1.75rem}}.h4,h4{font-size:calc(1.275rem + .3vw)}@media (min-width:1200px){.h4,h4{font-size:1.5rem}}.h5,h5{font-size:1.25rem}.h6,h6{font-size:1rem}p{margin-top:0;margin-bottom:1rem}abbr[title]{-webkit-text-decoration:underline dotted;text-decoration:underline dotted;cursor:help;-webkit-text-decoration-skip-ink:none;text-decoration-skip-ink:none}address{margin-bottom:1rem;font-style:normal;line-height:inherit}ol,ul{padding-left:2rem}dl,ol,ul{margin-top:0;margin-bottom:1rem}ol ol,ol ul,ul ol,ul ul{margin-bottom:0}dt{font-weight:700}dd{margin-bottom:.5rem;margin-left:0}blockquote{margin:0 0 1rem}b,strong{font-weight:bolder}.small,small{font-size:.875em}.mark,mark{padding:.1875em;color:var(--bs-highlight-color);background-color:var(--bs-highlight-bg)}sub,sup{position:relative;font-size:.75em;line-height:0;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}a{color:rgba(var(--bs-link-color-rgb),var(--bs-link-opacity,1));text-decoration:underline}a:hover{--bs-link-color-rgb:var(--bs-link-hover-color-rgb)}a:not([href]):not([class]),a:not([href]):not([class]):hover{color:inherit;text-decoration:none}code,kbd,pre,samp{font-family:var(--bs-font-monospace);font-size:1em}pre{display:block;margin-top:0;margin-bottom:1rem;overflow:auto;font-size:.875em}pre code{font-size:inherit;color:inherit;word-break:normal}code{font-size:.875em;color:var(--bs-code-color);word-wrap:break-word}a>code{color:inherit}kbd{padding:.1875rem .375rem;font-size:.875em;color:var(--bs-body-bg);background-color:var(--bs-body-color);border-radius:.25rem}kbd kbd{padding:0;font-size:1em}figure{margin:0 0 1rem}img,svg{vertical-align:middle}table{caption-side:bottom;border-collapse:collapse}caption{padding-top:.5rem;padding-bottom:.5rem;color:var(--bs-secondary-color);text-align:left}th{text-align:inherit;text-align:-webkit-match-parent}tbody,td,tfoot,th,thead,tr{border-color:inherit;border-style:solid;border-width:0}label{display:inline-block}button{border-radius:0}button:focus:not(:focus-visible){outline:0}button,input,optgroup,select,textarea{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button,select{text-transform:none}[role=button]{cursor:pointer}select{word-wrap:normal}select:disabled{opacity:1}[list]:not([type=date]):not([type=datetime-local]):not([type=month]):not([type=week]):not([type=time])::-webkit-calendar-picker-indicator{display:none!important}[type=button],[type=reset],[type=submit],button{-webkit-appearance:button}[type=button]:not(:disabled),[type=reset]:not(:disabled),[type=submit]:not(:disabled),button:not(:disabled){cursor:pointer}::-moz-focus-inner{padding:0;border-style:none}textarea{resize:vertical}fieldset{min-width:0;padding:0;margin:0;border:0}legend{float:left;width:100%;padding:0;margin-bottom:.5rem;font-size:calc(1.275rem + .3vw);line-height:inherit}@media (min-width:1200px){legend{font-size:1.5rem}}legend+*{clear:left}::-webkit-datetime-edit-day-field,::-webkit-datetime-edit-fields-wrapper,::-webkit-datetime-edit-hour-field,::-webkit-datetime-edit-minute,::-webkit-datetime-edit-month-field,::-webkit-datetime-edit-text,::-webkit-datetime-edit-year-field{padding:0}::-webkit-inner-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}::-webkit-search-decoration{-webkit-appearance:none}::-webkit-color-swatch-wrapper{padding:0}::-webkit-file-upload-button{font:inherit;-webkit-appearance:button}::file-selector-button{font:inherit;-webkit-appearance:button}output{display:inline-block}iframe{border:0}summary{display:list-item;cursor:pointer}progress{vertical-align:baseline}[hidden]{display:none!important}.lead{font-size:1.25rem;font-weight:300}.display-1{font-size:calc(1.625rem + 4.5vw);font-weight:300;line-height:1.2}@media (min-width:1200px){.display-1{font-size:5rem}}.display-2{font-size:calc(1.575rem + 3.9vw);font-weight:300;line-height:1.2}@media (min-width:1200px){.display-2{font-size:4.5rem}}.display-3{font-size:calc(1.525rem + 3.3vw);font-weight:300;line-height:1.2}@media (min-width:1200px){.display-3{font-size:4rem}}.display-4{font-size:calc(1.475rem + 2.7vw);font-weight:300;line-height:1.2}@media (min-width:1200px){.display-4{font-size:3.5rem}}.display-5{font-size:calc(1.425rem + 2.1vw);font-weight:300;line-height:1.2}@media (min-width:1200px){.display-5{font-size:3rem}}.display-6{font-size:calc(1.375rem + 1.5vw);font-weight:300;line-height:1.2}@media (min-width:1200px){.display-6{font-size:2.5rem}}.list-unstyled{padding-left:0;list-style:none}.list-inline{padding-left:0;list-style:none}.list-inline-item{display:inline-block}.list-inline-item:not(:last-child){margin-right:.5rem}.initialism{font-size:.875em;text-transform:uppercase}.blockquote{margin-bottom:1rem;font-size:1.25rem}.blockquote>:last-child{margin-bottom:0}.blockquote-footer{margin-top:-1rem;margin-bottom:1rem;font-size:.875em;color:#6c757d}.blockquote-footer::before{content:"— "}.img-fluid{max-width:100%;height:auto}.img-thumbnail{padding:.25rem;background-color:var(--bs-body-bg);border:var(--bs-border-width) solid var(--bs-border-color);border-radius:var(--bs-border-radius);max-width:100%;height:auto}.figure{display:inline-block}.figure-img{margin-bottom:.5rem;line-height:1}.figure-caption{font-size:.875em;color:var(--bs-secondary-color)}.container,.container-fluid,.container-lg,.container-md,.container-sm,.container-xl,.container-xxl{--bs-gutter-x:1.5rem;--bs-gutter-y:0;width:100%;padding-right:calc(var(--bs-gutter-x) * .5);padding-left:calc(var(--bs-gutter-x) * .5);margin-right:auto;margin-left:auto}@media (min-width:576px){.container,.container-sm{max-width:540px}}@media (min-width:768px){.container,.container-md,.container-sm{max-width:720px}}@media (min-width:992px){.container,.container-lg,.container-md,.container-sm{max-width:960px}}@media (min-width:1200px){.container,.container-lg,.container-md,.container-sm,.container-xl{max-width:1140px}}@media (min-width:1400px){.container,.container-lg,.container-md,.container-sm,.container-xl,.container-xxl{max-width:1320px}}:root{--bs-breakpoint-xs:0;--bs-breakpoint-sm:576px;--bs-breakpoint-md:768px;--bs-breakpoint-lg:992px;--bs-breakpoint-xl:1200px;--bs-breakpoint-xxl:1400px}.row{--bs-gutter-x:1.5rem;--bs-gutter-y:0;display:flex;flex-wrap:wrap;margin-top:calc(-1 * var(--bs-gutter-y));margin-right:calc(-.5 * var(--bs-gutter-x));margin-left:calc(-.5 * var(--bs-gutter-x))}.row>*{flex-shrink:0;width:100%;max-width:100%;padding-right:calc(var(--bs-gutter-x) * .5);padding-left:calc(var(--bs-gutter-x) * .5);margin-top:var(--bs-gutter-y)}.col{flex:1 0 0%}.row-cols-auto>*{flex:0 0 auto;width:auto}.row-cols-1>*{flex:0 0 auto;width:100%}.row-cols-2>*{flex:0 0 auto;width:50%}.row-cols-3>*{flex:0 0 auto;width:33.33333333%}.row-cols-4>*{flex:0 0 auto;width:25%}.row-cols-5>*{flex:0 0 auto;width:20%}.row-cols-6>*{flex:0 0 auto;width:16.66666667%}.col-auto{flex:0 0 auto;width:auto}.col-1{flex:0 0 auto;width:8.33333333%}.col-2{flex:0 0 auto;width:16.66666667%}.col-3{flex:0 0 auto;width:25%}.col-4{flex:0 0 auto;width:33.33333333%}.col-5{flex:0 0 auto;width:41.66666667%}.col-6{flex:0 0 auto;width:50%}.col-7{flex:0 0 auto;width:58.33333333%}.col-8{flex:0 0 auto;width:66.66666667%}.col-9{flex:0 0 auto;width:75%}.col-10{flex:0 0 auto;width:83.33333333%}.col-11{flex:0 0 auto;width:91.66666667%}.col-12{flex:0 0 auto;width:100%}.offset-1{margin-left:8.33333333%}.offset-2{margin-left:16.66666667%}.offset-3{margin-left:25%}.offset-4{margin-left:33.33333333%}.offset-5{margin-left:41.66666667%}.offset-6{margin-left:50%}.offset-7{margin-left:58.33333333%}.offset-8{margin-left:66.66666667%}.offset-9{margin-left:75%}.offset-10{margin-left:83.33333333%}.offset-11{margin-left:91.66666667%}.g-0,.gx-0{--bs-gutter-x:0}.g-0,.gy-0{--bs-gutter-y:0}.g-1,.gx-1{--bs-gutter-x:0.25rem}.g-1,.gy-1{--bs-gutter-y:0.25rem}.g-2,.gx-2{--bs-gutter-x:0.5rem}.g-2,.gy-2{--bs-gutter-y:0.5rem}.g-3,.gx-3{--bs-gutter-x:1rem}.g-3,.gy-3{--bs-gutter-y:1rem}.g-4,.gx-4{--bs-gutter-x:1.5rem}.g-4,.gy-4{--bs-gutter-y:1.5rem}.g-5,.gx-5{--bs-gutter-x:3rem}.g-5,.gy-5{--bs-gutter-y:3rem}@media (min-width:576px){.col-sm{flex:1 0 0%}.row-cols-sm-auto>*{flex:0 0 auto;width:auto}.row-cols-sm-1>*{flex:0 0 auto;width:100%}.row-cols-sm-2>*{flex:0 0 auto;width:50%}.row-cols-sm-3>*{flex:0 0 auto;width:33.33333333%}.row-cols-sm-4>*{flex:0 0 auto;width:25%}.row-cols-sm-5>*{flex:0 0 auto;width:20%}.row-cols-sm-6>*{flex:0 0 auto;width:16.66666667%}.col-sm-auto{flex:0 0 auto;width:auto}.col-sm-1{flex:0 0 auto;width:8.33333333%}.col-sm-2{flex:0 0 auto;width:16.66666667%}.col-sm-3{flex:0 0 auto;width:25%}.col-sm-4{flex:0 0 auto;width:33.33333333%}.col-sm-5{flex:0 0 auto;width:41.66666667%}.col-sm-6{flex:0 0 auto;width:50%}.col-sm-7{flex:0 0 auto;width:58.33333333%}.col-sm-8{flex:0 0 auto;width:66.66666667%}.col-sm-9{flex:0 0 auto;width:75%}.col-sm-10{flex:0 0 auto;width:83.33333333%}.col-sm-11{flex:0 0 auto;width:91.66666667%}.col-sm-12{flex:0 0 auto;width:100%}.offset-sm-0{margin-left:0}.offset-sm-1{margin-left:8.33333333%}.offset-sm-2{margin-left:16.66666667%}.offset-sm-3{margin-left:25%}.offset-sm-4{margin-left:33.33333333%}.offset-sm-5{margin-left:41.66666667%}.offset-sm-6{margin-left:50%}.offset-sm-7{margin-left:58.33333333%}.offset-sm-8{margin-left:66.66666667%}.offset-sm-9{margin-left:75%}.offset-sm-10{margin-left:83.33333333%}.offset-sm-11{margin-left:91.66666667%}.g-sm-0,.gx-sm-0{--bs-gutter-x:0}.g-sm-0,.gy-sm-0{--bs-gutter-y:0}.g-sm-1,.gx-sm-1{--bs-gutter-x:0.25rem}.g-sm-1,.gy-sm-1{--bs-gutter-y:0.25rem}.g-sm-2,.gx-sm-2{--bs-gutter-x:0.5rem}.g-sm-2,.gy-sm-2{--bs-gutter-y:0.5rem}.g-sm-3,.gx-sm-3{--bs-gutter-x:1rem}.g-sm-3,.gy-sm-3{--bs-gutter-y:1rem}.g-sm-4,.gx-sm-4{--bs-gutter-x:1.5rem}.g-sm-4,.gy-sm-4{--bs-gutter-y:1.5rem}.g-sm-5,.gx-sm-5{--bs-gutter-x:3rem}.g-sm-5,.gy-sm-5{--bs-gutter-y:3rem}}@media (min-width:768px){.col-md{flex:1 0 0%}.row-cols-md-auto>*{flex:0 0 auto;width:auto}.row-cols-md-1>*{flex:0 0 auto;width:100%}.row-cols-md-2>*{flex:0 0 auto;width:50%}.row-cols-md-3>*{flex:0 0 auto;width:33.33333333%}.row-cols-md-4>*{flex:0 0 auto;width:25%}.row-cols-md-5>*{flex:0 0 auto;width:20%}.row-cols-md-6>*{flex:0 0 auto;width:16.66666667%}.col-md-auto{flex:0 0 auto;width:auto}.col-md-1{flex:0 0 auto;width:8.33333333%}.col-md-2{flex:0 0 auto;width:16.66666667%}.col-md-3{flex:0 0 auto;width:25%}.col-md-4{flex:0 0 auto;width:33.33333333%}.col-md-5{flex:0 0 auto;width:41.66666667%}.col-md-6{flex:0 0 auto;width:50%}.col-md-7{flex:0 0 auto;width:58.33333333%}.col-md-8{flex:0 0 auto;width:66.66666667%}.col-md-9{flex:0 0 auto;width:75%}.col-md-10{flex:0 0 auto;width:83.33333333%}.col-md-11{flex:0 0 auto;width:91.66666667%}.col-md-12{flex:0 0 auto;width:100%}.offset-md-0{margin-left:0}.offset-md-1{margin-left:8.33333333%}.offset-md-2{margin-left:16.66666667%}.offset-md-3{margin-left:25%}.offset-md-4{margin-left:33.33333333%}.offset-md-5{margin-left:41.66666667%}.offset-md-6{margin-left:50%}.offset-md-7{margin-left:58.33333333%}.offset-md-8{margin-left:66.66666667%}.offset-md-9{margin-left:75%}.offset-md-10{margin-left:83.33333333%}.offset-md-11{margin-left:91.66666667%}.g-md-0,.gx-md-0{--bs-gutter-x:0}.g-md-0,.gy-md-0{--bs-gutter-y:0}.g-md-1,.gx-md-1{--bs-gutter-x:0.25rem}.g-md-1,.gy-md-1{--bs-gutter-y:0.25rem}.g-md-2,.gx-md-2{--bs-gutter-x:0.5rem}.g-md-2,.gy-md-2{--bs-gutter-y:0.5rem}.g-md-3,.gx-md-3{--bs-gutter-x:1rem}.g-md-3,.gy-md-3{--bs-gutter-y:1rem}.g-md-4,.gx-md-4{--bs-gutter-x:1.5rem}.g-md-4,.gy-md-4{--bs-gutter-y:1.5rem}.g-md-5,.gx-md-5{--bs-gutter-x:3rem}.g-md-5,.gy-md-5{--bs-gutter-y:3rem}}@media (min-width:992px){.col-lg{flex:1 0 0%}.row-cols-lg-auto>*{flex:0 0 auto;width:auto}.row-cols-lg-1>*{flex:0 0 auto;width:100%}.row-cols-lg-2>*{flex:0 0 auto;width:50%}.row-cols-lg-3>*{flex:0 0 auto;width:33.33333333%}.row-cols-lg-4>*{flex:0 0 auto;width:25%}.row-cols-lg-5>*{flex:0 0 auto;width:20%}.row-cols-lg-6>*{flex:0 0 auto;width:16.66666667%}.col-lg-auto{flex:0 0 auto;width:auto}.col-lg-1{flex:0 0 auto;width:8.33333333%}.col-lg-2{flex:0 0 auto;width:16.66666667%}.col-lg-3{flex:0 0 auto;width:25%}.col-lg-4{flex:0 0 auto;width:33.33333333%}.col-lg-5{flex:0 0 auto;width:41.66666667%}.col-lg-6{flex:0 0 auto;width:50%}.col-lg-7{flex:0 0 auto;width:58.33333333%}.col-lg-8{flex:0 0 auto;width:66.66666667%}.col-lg-9{flex:0 0 auto;width:75%}.col-lg-10{flex:0 0 auto;width:83.33333333%}.col-lg-11{flex:0 0 auto;width:91.66666667%}.col-lg-12{flex:0 0 auto;width:100%}.offset-lg-0{margin-left:0}.offset-lg-1{margin-left:8.33333333%}.offset-lg-2{margin-left:16.66666667%}.offset-lg-3{margin-left:25%}.offset-lg-4{margin-left:33.33333333%}.offset-lg-5{margin-left:41.66666667%}.offset-lg-6{margin-left:50%}.offset-lg-7{margin-left:58.33333333%}.offset-lg-8{margin-left:66.66666667%}.offset-lg-9{margin-left:75%}.offset-lg-10{margin-left:83.33333333%}.offset-lg-11{margin-left:91.66666667%}.g-lg-0,.gx-lg-0{--bs-gutter-x:0}.g-lg-0,.gy-lg-0{--bs-gutter-y:0}.g-lg-1,.gx-lg-1{--bs-gutter-x:0.25rem}.g-lg-1,.gy-lg-1{--bs-gutter-y:0.25rem}.g-lg-2,.gx-lg-2{--bs-gutter-x:0.5rem}.g-lg-2,.gy-lg-2{--bs-gutter-y:0.5rem}.g-lg-3,.gx-lg-3{--bs-gutter-x:1rem}.g-lg-3,.gy-lg-3{--bs-gutter-y:1rem}.g-lg-4,.gx-lg-4{--bs-gutter-x:1.5rem}.g-lg-4,.gy-lg-4{--bs-gutter-y:1.5rem}.g-lg-5,.gx-lg-5{--bs-gutter-x:3rem}.g-lg-5,.gy-lg-5{--bs-gutter-y:3rem}}@media (min-width:1200px){.col-xl{flex:1 0 0%}.row-cols-xl-auto>*{flex:0 0 auto;width:auto}.row-cols-xl-1>*{flex:0 0 auto;width:100%}.row-cols-xl-2>*{flex:0 0 auto;width:50%}.row-cols-xl-3>*{flex:0 0 auto;width:33.33333333%}.row-cols-xl-4>*{flex:0 0 auto;width:25%}.row-cols-xl-5>*{flex:0 0 auto;width:20%}.row-cols-xl-6>*{flex:0 0 auto;width:16.66666667%}.col-xl-auto{flex:0 0 auto;width:auto}.col-xl-1{flex:0 0 auto;width:8.33333333%}.col-xl-2{flex:0 0 auto;width:16.66666667%}.col-xl-3{flex:0 0 auto;width:25%}.col-xl-4{flex:0 0 auto;width:33.33333333%}.col-xl-5{flex:0 0 auto;width:41.66666667%}.col-xl-6{flex:0 0 auto;width:50%}.col-xl-7{flex:0 0 auto;width:58.33333333%}.col-xl-8{flex:0 0 auto;width:66.66666667%}.col-xl-9{flex:0 0 auto;width:75%}.col-xl-10{flex:0 0 auto;width:83.33333333%}.col-xl-11{flex:0 0 auto;width:91.66666667%}.col-xl-12{flex:0 0 auto;width:100%}.offset-xl-0{margin-left:0}.offset-xl-1{margin-left:8.33333333%}.offset-xl-2{margin-left:16.66666667%}.offset-xl-3{margin-left:25%}.offset-xl-4{margin-left:33.33333333%}.offset-xl-5{margin-left:41.66666667%}.offset-xl-6{margin-left:50%}.offset-xl-7{margin-left:58.33333333%}.offset-xl-8{margin-left:66.66666667%}.offset-xl-9{margin-left:75%}.offset-xl-10{margin-left:83.33333333%}.offset-xl-11{margin-left:91.66666667%}.g-xl-0,.gx-xl-0{--bs-gutter-x:0}.g-xl-0,.gy-xl-0{--bs-gutter-y:0}.g-xl-1,.gx-xl-1{--bs-gutter-x:0.25rem}.g-xl-1,.gy-xl-1{--bs-gutter-y:0.25rem}.g-xl-2,.gx-xl-2{--bs-gutter-x:0.5rem}.g-xl-2,.gy-xl-2{--bs-gutter-y:0.5rem}.g-xl-3,.gx-xl-3{--bs-gutter-x:1rem}.g-xl-3,.gy-xl-3{--bs-gutter-y:1rem}.g-xl-4,.gx-xl-4{--bs-gutter-x:1.5rem}.g-xl-4,.gy-xl-4{--bs-gutter-y:1.5rem}.g-xl-5,.gx-xl-5{--bs-gutter-x:3rem}.g-xl-5,.gy-xl-5{--bs-gutter-y:3rem}}@media (min-width:1400px){.col-xxl{flex:1 0 0%}.row-cols-xxl-auto>*{flex:0 0 auto;width:auto}.row-cols-xxl-1>*{flex:0 0 auto;width:100%}.row-cols-xxl-2>*{flex:0 0 auto;width:50%}.row-cols-xxl-3>*{flex:0 0 auto;width:33.33333333%}.row-cols-xxl-4>*{flex:0 0 auto;width:25%}.row-cols-xxl-5>*{flex:0 0 auto;width:20%}.row-cols-xxl-6>*{flex:0 0 auto;width:16.66666667%}.col-xxl-auto{flex:0 0 auto;width:auto}.col-xxl-1{flex:0 0 auto;width:8.33333333%}.col-xxl-2{flex:0 0 auto;width:16.66666667%}.col-xxl-3{flex:0 0 auto;width:25%}.col-xxl-4{flex:0 0 auto;width:33.33333333%}.col-xxl-5{flex:0 0 auto;width:41.66666667%}.col-xxl-6{flex:0 0 auto;width:50%}.col-xxl-7{flex:0 0 auto;width:58.33333333%}.col-xxl-8{flex:0 0 auto;width:66.66666667%}.col-xxl-9{flex:0 0 auto;width:75%}.col-xxl-10{flex:0 0 auto;width:83.33333333%}.col-xxl-11{flex:0 0 auto;width:91.66666667%}.col-xxl-12{flex:0 0 auto;width:100%}.offset-xxl-0{margin-left:0}.offset-xxl-1{margin-left:8.33333333%}.offset-xxl-2{margin-left:16.66666667%}.offset-xxl-3{margin-left:25%}.offset-xxl-4{margin-left:33.33333333%}.offset-xxl-5{margin-left:41.66666667%}.offset-xxl-6{margin-left:50%}.offset-xxl-7{margin-left:58.33333333%}.offset-xxl-8{margin-left:66.66666667%}.offset-xxl-9{margin-left:75%}.offset-xxl-10{margin-left:83.33333333%}.offset-xxl-11{margin-left:91.66666667%}.g-xxl-0,.gx-xxl-0{--bs-gutter-x:0}.g-xxl-0,.gy-xxl-0{--bs-gutter-y:0}.g-xxl-1,.gx-xxl-1{--bs-gutter-x:0.25rem}.g-xxl-1,.gy-xxl-1{--bs-gutter-y:0.25rem}.g-xxl-2,.gx-xxl-2{--bs-gutter-x:0.5rem}.g-xxl-2,.gy-xxl-2{--bs-gutter-y:0.5rem}.g-xxl-3,.gx-xxl-3{--bs-gutter-x:1rem}.g-xxl-3,.gy-xxl-3{--bs-gutter-y:1rem}.g-xxl-4,.gx-xxl-4{--bs-gutter-x:1.5rem}.g-xxl-4,.gy-xxl-4{--bs-gutter-y:1.5rem}.g-xxl-5,.gx-xxl-5{--bs-gutter-x:3rem}.g-xxl-5,.gy-xxl-5{--bs-gutter-y:3rem}}.table{--bs-table-color-type:initial;--bs-table-bg-type:initial;--bs-table-color-state:initial;--bs-table-bg-state:initial;--bs-table-color:var(--bs-emphasis-color);--bs-table-bg:var(--bs-body-bg);--bs-table-border-color:var(--bs-border-color);--bs-table-accent-bg:transparent;--bs-table-striped-color:var(--bs-emphasis-color);--bs-table-striped-bg:rgba(var(--bs-emphasis-color-rgb), 0.05);--bs-table-active-color:var(--bs-emphasis-color);--bs-table-active-bg:rgba(var(--bs-emphasis-color-rgb), 0.1);--bs-table-hover-color:var(--bs-emphasis-color);--bs-table-hover-bg:rgba(var(--bs-emphasis-color-rgb), 0.075);width:100%;margin-bottom:1rem;vertical-align:top;border-color:var(--bs-table-border-color)}.table>:not(caption)>*>*{padding:.5rem .5rem;color:var(--bs-table-color-state,var(--bs-table-color-type,var(--bs-table-color)));background-color:var(--bs-table-bg);border-bottom-width:var(--bs-border-width);box-shadow:inset 0 0 0 9999px var(--bs-table-bg-state,var(--bs-table-bg-type,var(--bs-table-accent-bg)))}.table>tbody{vertical-align:inherit}.table>thead{vertical-align:bottom}.table-group-divider{border-top:calc(var(--bs-border-width) * 2) solid currentcolor}.caption-top{caption-side:top}.table-sm>:not(caption)>*>*{padding:.25rem .25rem}.table-bordered>:not(caption)>*{border-width:var(--bs-border-width) 0}.table-bordered>:not(caption)>*>*{border-width:0 var(--bs-border-width)}.table-borderless>:not(caption)>*>*{border-bottom-width:0}.table-borderless>:not(:first-child){border-top-width:0}.table-striped>tbody>tr:nth-of-type(odd)>*{--bs-table-color-type:var(--bs-table-striped-color);--bs-table-bg-type:var(--bs-table-striped-bg)}.table-striped-columns>:not(caption)>tr>:nth-child(2n){--bs-table-color-type:var(--bs-table-striped-color);--bs-table-bg-type:var(--bs-table-striped-bg)}.table-active{--bs-table-color-state:var(--bs-table-active-color);--bs-table-bg-state:var(--bs-table-active-bg)}.table-hover>tbody>tr:hover>*{--bs-table-color-state:var(--bs-table-hover-color);--bs-table-bg-state:var(--bs-table-hover-bg)}.table-primary{--bs-table-color:#000;--bs-table-bg:#cfe2ff;--bs-table-border-color:#a6b5cc;--bs-table-striped-bg:#c5d7f2;--bs-table-striped-color:#000;--bs-table-active-bg:#bacbe6;--bs-table-active-color:#000;--bs-table-hover-bg:#bfd1ec;--bs-table-hover-color:#000;color:var(--bs-table-color);border-color:var(--bs-table-border-color)}.table-secondary{--bs-table-color:#000;--bs-table-bg:#e2e3e5;--bs-table-border-color:#b5b6b7;--bs-table-striped-bg:#d7d8da;--bs-table-striped-color:#000;--bs-table-active-bg:#cbccce;--bs-table-active-color:#000;--bs-table-hover-bg:#d1d2d4;--bs-table-hover-color:#000;color:var(--bs-table-color);border-color:var(--bs-table-border-color)}.table-success{--bs-table-color:#000;--bs-table-bg:#d1e7dd;--bs-table-border-color:#a7b9b1;--bs-table-striped-bg:#c7dbd2;--bs-table-striped-color:#000;--bs-table-active-bg:#bcd0c7;--bs-table-active-color:#000;--bs-table-hover-bg:#c1d6cc;--bs-table-hover-color:#000;color:var(--bs-table-color);border-color:var(--bs-table-border-color)}.table-info{--bs-table-color:#000;--bs-table-bg:#cff4fc;--bs-table-border-color:#a6c3ca;--bs-table-striped-bg:#c5e8ef;--bs-table-striped-color:#000;--bs-table-active-bg:#badce3;--bs-table-active-color:#000;--bs-table-hover-bg:#bfe2e9;--bs-table-hover-color:#000;color:var(--bs-table-color);border-color:var(--bs-table-border-color)}.table-warning{--bs-table-color:#000;--bs-table-bg:#fff3cd;--bs-table-border-color:#ccc2a4;--bs-table-striped-bg:#f2e7c3;--bs-table-striped-color:#000;--bs-table-active-bg:#e6dbb9;--bs-table-active-color:#000;--bs-table-hover-bg:#ece1be;--bs-table-hover-color:#000;color:var(--bs-table-color);border-color:var(--bs-table-border-color)}.table-danger{--bs-table-color:#000;--bs-table-bg:#f8d7da;--bs-table-border-color:#c6acae;--bs-table-striped-bg:#eccccf;--bs-table-striped-color:#000;--bs-table-active-bg:#dfc2c4;--bs-table-active-color:#000;--bs-table-hover-bg:#e5c7ca;--bs-table-hover-color:#000;color:var(--bs-table-color);border-color:var(--bs-table-border-color)}.table-light{--bs-table-color:#000;--bs-table-bg:#f8f9fa;--bs-table-border-color:#c6c7c8;--bs-table-striped-bg:#ecedee;--bs-table-striped-color:#000;--bs-table-active-bg:#dfe0e1;--bs-table-active-color:#000;--bs-table-hover-bg:#e5e6e7;--bs-table-hover-color:#000;color:var(--bs-table-color);border-color:var(--bs-table-border-color)}.table-dark{--bs-table-color:#fff;--bs-table-bg:#212529;--bs-table-border-color:#4d5154;--bs-table-striped-bg:#2c3034;--bs-table-striped-color:#fff;--bs-table-active-bg:#373b3e;--bs-table-active-color:#fff;--bs-table-hover-bg:#323539;--bs-table-hover-color:#fff;color:var(--bs-table-color);border-color:var(--bs-table-border-color)}.table-responsive{overflow-x:auto;-webkit-overflow-scrolling:touch}@media (max-width:575.98px){.table-responsive-sm{overflow-x:auto;-webkit-overflow-scrolling:touch}}@media (max-width:767.98px){.table-responsive-md{overflow-x:auto;-webkit-overflow-scrolling:touch}}@media (max-width:991.98px){.table-responsive-lg{overflow-x:auto;-webkit-overflow-scrolling:touch}}@media (max-width:1199.98px){.table-responsive-xl{overflow-x:auto;-webkit-overflow-scrolling:touch}}@media (max-width:1399.98px){.table-responsive-xxl{overflow-x:auto;-webkit-overflow-scrolling:touch}}.form-label{margin-bottom:.5rem}.col-form-label{padding-top:calc(.375rem + var(--bs-border-width));padding-bottom:calc(.375rem + var(--bs-border-width));margin-bottom:0;font-size:inherit;line-height:1.5}.col-form-label-lg{padding-top:calc(.5rem + var(--bs-border-width));padding-bottom:calc(.5rem + var(--bs-border-width));font-size:1.25rem}.col-form-label-sm{padding-top:calc(.25rem + var(--bs-border-width));padding-bottom:calc(.25rem + var(--bs-border-width));font-size:.875rem}.form-text{margin-top:.25rem;font-size:.875em;color:var(--bs-secondary-color)}.form-control{display:block;width:100%;padding:.375rem .75rem;font-size:1rem;font-weight:400;line-height:1.5;color:var(--bs-body-color);-webkit-appearance:none;-moz-appearance:none;appearance:none;background-color:var(--bs-body-bg);background-clip:padding-box;border:var(--bs-border-width) solid var(--bs-border-color);border-radius:var(--bs-border-radius);transition:border-color .15s ease-in-out,box-shadow .15s ease-in-out}@media (prefers-reduced-motion:reduce){.form-control{transition:none}}.form-control[type=file]{overflow:hidden}.form-control[type=file]:not(:disabled):not([readonly]){cursor:pointer}.form-control:focus{color:var(--bs-body-color);background-color:var(--bs-body-bg);border-color:#86b7fe;outline:0;box-shadow:0 0 0 .25rem rgba(13,110,253,.25)}.form-control::-webkit-date-and-time-value{min-width:85px;height:1.5em;margin:0}.form-control::-webkit-datetime-edit{display:block;padding:0}.form-control::-moz-placeholder{color:var(--bs-secondary-color);opacity:1}.form-control::placeholder{color:var(--bs-secondary-color);opacity:1}.form-control:disabled{background-color:var(--bs-secondary-bg);opacity:1}.form-control::-webkit-file-upload-button{padding:.375rem .75rem;margin:-.375rem -.75rem;-webkit-margin-end:.75rem;margin-inline-end:.75rem;color:var(--bs-body-color);background-color:var(--bs-tertiary-bg);pointer-events:none;border-color:inherit;border-style:solid;border-width:0;border-inline-end-width:var(--bs-border-width);border-radius:0;-webkit-transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out}.form-control::file-selector-button{padding:.375rem .75rem;margin:-.375rem -.75rem;-webkit-margin-end:.75rem;margin-inline-end:.75rem;color:var(--bs-body-color);background-color:var(--bs-tertiary-bg);pointer-events:none;border-color:inherit;border-style:solid;border-width:0;border-inline-end-width:var(--bs-border-width);border-radius:0;transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out}@media (prefers-reduced-motion:reduce){.form-control::-webkit-file-upload-button{-webkit-transition:none;transition:none}.form-control::file-selector-button{transition:none}}.form-control:hover:not(:disabled):not([readonly])::-webkit-file-upload-button{background-color:var(--bs-secondary-bg)}.form-control:hover:not(:disabled):not([readonly])::file-selector-button{background-color:var(--bs-secondary-bg)}.form-control-plaintext{display:block;width:100%;padding:.375rem 0;margin-bottom:0;line-height:1.5;color:var(--bs-body-color);background-color:transparent;border:solid transparent;border-width:var(--bs-border-width) 0}.form-control-plaintext:focus{outline:0}.form-control-plaintext.form-control-lg,.form-control-plaintext.form-control-sm{padding-right:0;padding-left:0}.form-control-sm{min-height:calc(1.5em + .5rem + calc(var(--bs-border-width) * 2));padding:.25rem .5rem;font-size:.875rem;border-radius:var(--bs-border-radius-sm)}.form-control-sm::-webkit-file-upload-button{padding:.25rem .5rem;margin:-.25rem -.5rem;-webkit-margin-end:.5rem;margin-inline-end:.5rem}.form-control-sm::file-selector-button{padding:.25rem .5rem;margin:-.25rem -.5rem;-webkit-margin-end:.5rem;margin-inline-end:.5rem}.form-control-lg{min-height:calc(1.5em + 1rem + calc(var(--bs-border-width) * 2));padding:.5rem 1rem;font-size:1.25rem;border-radius:var(--bs-border-radius-lg)}.form-control-lg::-webkit-file-upload-button{padding:.5rem 1rem;margin:-.5rem -1rem;-webkit-margin-end:1rem;margin-inline-end:1rem}.form-control-lg::file-selector-button{padding:.5rem 1rem;margin:-.5rem -1rem;-webkit-margin-end:1rem;margin-inline-end:1rem}textarea.form-control{min-height:calc(1.5em + .75rem + calc(var(--bs-border-width) * 2))}textarea.form-control-sm{min-height:calc(1.5em + .5rem + calc(var(--bs-border-width) * 2))}textarea.form-control-lg{min-height:calc(1.5em + 1rem + calc(var(--bs-border-width) * 2))}.form-control-color{width:3rem;height:calc(1.5em + .75rem + calc(var(--bs-border-width) * 2));padding:.375rem}.form-control-color:not(:disabled):not([readonly]){cursor:pointer}.form-control-color::-moz-color-swatch{border:0!important;border-radius:var(--bs-border-radius)}.form-control-color::-webkit-color-swatch{border:0!important;border-radius:var(--bs-border-radius)}.form-control-color.form-control-sm{height:calc(1.5em + .5rem + calc(var(--bs-border-width) * 2))}.form-control-color.form-control-lg{height:calc(1.5em + 1rem + calc(var(--bs-border-width) * 2))}.form-select{--bs-form-select-bg-img:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23343a40' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/%3e%3c/svg%3e");display:block;width:100%;padding:.375rem 2.25rem .375rem .75rem;font-size:1rem;font-weight:400;line-height:1.5;color:var(--bs-body-color);-webkit-appearance:none;-moz-appearance:none;appearance:none;background-color:var(--bs-body-bg);background-image:var(--bs-form-select-bg-img),var(--bs-form-select-bg-icon,none);background-repeat:no-repeat;background-position:right .75rem center;background-size:16px 12px;border:var(--bs-border-width) solid var(--bs-border-color);border-radius:var(--bs-border-radius);transition:border-color .15s ease-in-out,box-shadow .15s ease-in-out}@media (prefers-reduced-motion:reduce){.form-select{transition:none}}.form-select:focus{border-color:#86b7fe;outline:0;box-shadow:0 0 0 .25rem rgba(13,110,253,.25)}.form-select[multiple],.form-select[size]:not([size="1"]){padding-right:.75rem;background-image:none}.form-select:disabled{background-color:var(--bs-secondary-bg)}.form-select:-moz-focusring{color:transparent;text-shadow:0 0 0 var(--bs-body-color)}.form-select-sm{padding-top:.25rem;padding-bottom:.25rem;padding-left:.5rem;font-size:.875rem;border-radius:var(--bs-border-radius-sm)}.form-select-lg{padding-top:.5rem;padding-bottom:.5rem;padding-left:1rem;font-size:1.25rem;border-radius:var(--bs-border-radius-lg)}[data-bs-theme=dark] .form-select{--bs-form-select-bg-img:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23dee2e6' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/%3e%3c/svg%3e")}.form-check{display:block;min-height:1.5rem;padding-left:1.5em;margin-bottom:.125rem}.form-check .form-check-input{float:left;margin-left:-1.5em}.form-check-reverse{padding-right:1.5em;padding-left:0;text-align:right}.form-check-reverse .form-check-input{float:right;margin-right:-1.5em;margin-left:0}.form-check-input{--bs-form-check-bg:var(--bs-body-bg);flex-shrink:0;width:1em;height:1em;margin-top:.25em;vertical-align:top;-webkit-appearance:none;-moz-appearance:none;appearance:none;background-color:var(--bs-form-check-bg);background-image:var(--bs-form-check-bg-image);background-repeat:no-repeat;background-position:center;background-size:contain;border:var(--bs-border-width) solid var(--bs-border-color);-webkit-print-color-adjust:exact;color-adjust:exact;print-color-adjust:exact}.form-check-input[type=checkbox]{border-radius:.25em}.form-check-input[type=radio]{border-radius:50%}.form-check-input:active{filter:brightness(90%)}.form-check-input:focus{border-color:#86b7fe;outline:0;box-shadow:0 0 0 .25rem rgba(13,110,253,.25)}.form-check-input:checked{background-color:#0d6efd;border-color:#0d6efd}.form-check-input:checked[type=checkbox]{--bs-form-check-bg-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='m6 10 3 3 6-6'/%3e%3c/svg%3e")}.form-check-input:checked[type=radio]{--bs-form-check-bg-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='2' fill='%23fff'/%3e%3c/svg%3e")}.form-check-input[type=checkbox]:indeterminate{background-color:#0d6efd;border-color:#0d6efd;--bs-form-check-bg-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10h8'/%3e%3c/svg%3e")}.form-check-input:disabled{pointer-events:none;filter:none;opacity:.5}.form-check-input:disabled~.form-check-label,.form-check-input[disabled]~.form-check-label{cursor:default;opacity:.5}.form-switch{padding-left:2.5em}.form-switch .form-check-input{--bs-form-switch-bg:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='rgba%280, 0, 0, 0.25%29'/%3e%3c/svg%3e");width:2em;margin-left:-2.5em;background-image:var(--bs-form-switch-bg);background-position:left center;border-radius:2em;transition:background-position .15s ease-in-out}@media (prefers-reduced-motion:reduce){.form-switch .form-check-input{transition:none}}.form-switch .form-check-input:focus{--bs-form-switch-bg:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%2386b7fe'/%3e%3c/svg%3e")}.form-switch .form-check-input:checked{background-position:right center;--bs-form-switch-bg:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23fff'/%3e%3c/svg%3e")}.form-switch.form-check-reverse{padding-right:2.5em;padding-left:0}.form-switch.form-check-reverse .form-check-input{margin-right:-2.5em;margin-left:0}.form-check-inline{display:inline-block;margin-right:1rem}.btn-check{position:absolute;clip:rect(0,0,0,0);pointer-events:none}.btn-check:disabled+.btn,.btn-check[disabled]+.btn{pointer-events:none;filter:none;opacity:.65}[data-bs-theme=dark] .form-switch .form-check-input:not(:checked):not(:focus){--bs-form-switch-bg:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='rgba%28255, 255, 255, 0.25%29'/%3e%3c/svg%3e")}.form-range{width:100%;height:1.5rem;padding:0;-webkit-appearance:none;-moz-appearance:none;appearance:none;background-color:transparent}.form-range:focus{outline:0}.form-range:focus::-webkit-slider-thumb{box-shadow:0 0 0 1px #fff,0 0 0 .25rem rgba(13,110,253,.25)}.form-range:focus::-moz-range-thumb{box-shadow:0 0 0 1px #fff,0 0 0 .25rem rgba(13,110,253,.25)}.form-range::-moz-focus-outer{border:0}.form-range::-webkit-slider-thumb{width:1rem;height:1rem;margin-top:-.25rem;-webkit-appearance:none;appearance:none;background-color:#0d6efd;border:0;border-radius:1rem;-webkit-transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out}@media (prefers-reduced-motion:reduce){.form-range::-webkit-slider-thumb{-webkit-transition:none;transition:none}}.form-range::-webkit-slider-thumb:active{background-color:#b6d4fe}.form-range::-webkit-slider-runnable-track{width:100%;height:.5rem;color:transparent;cursor:pointer;background-color:var(--bs-secondary-bg);border-color:transparent;border-radius:1rem}.form-range::-moz-range-thumb{width:1rem;height:1rem;-moz-appearance:none;appearance:none;background-color:#0d6efd;border:0;border-radius:1rem;-moz-transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out}@media (prefers-reduced-motion:reduce){.form-range::-moz-range-thumb{-moz-transition:none;transition:none}}.form-range::-moz-range-thumb:active{background-color:#b6d4fe}.form-range::-moz-range-track{width:100%;height:.5rem;color:transparent;cursor:pointer;background-color:var(--bs-secondary-bg);border-color:transparent;border-radius:1rem}.form-range:disabled{pointer-events:none}.form-range:disabled::-webkit-slider-thumb{background-color:var(--bs-secondary-color)}.form-range:disabled::-moz-range-thumb{background-color:var(--bs-secondary-color)}.form-floating{position:relative}.form-floating>.form-control,.form-floating>.form-control-plaintext,.form-floating>.form-select{height:calc(3.5rem + calc(var(--bs-border-width) * 2));min-height:calc(3.5rem + calc(var(--bs-border-width) * 2));line-height:1.25}.form-floating>label{position:absolute;top:0;left:0;z-index:2;height:100%;padding:1rem .75rem;overflow:hidden;text-align:start;text-overflow:ellipsis;white-space:nowrap;pointer-events:none;border:var(--bs-border-width) solid transparent;transform-origin:0 0;transition:opacity .1s ease-in-out,transform .1s ease-in-out}@media (prefers-reduced-motion:reduce){.form-floating>label{transition:none}}.form-floating>.form-control,.form-floating>.form-control-plaintext{padding:1rem .75rem}.form-floating>.form-control-plaintext::-moz-placeholder,.form-floating>.form-control::-moz-placeholder{color:transparent}.form-floating>.form-control-plaintext::placeholder,.form-floating>.form-control::placeholder{color:transparent}.form-floating>.form-control-plaintext:not(:-moz-placeholder-shown),.form-floating>.form-control:not(:-moz-placeholder-shown){padding-top:1.625rem;padding-bottom:.625rem}.form-floating>.form-control-plaintext:focus,.form-floating>.form-control-plaintext:not(:placeholder-shown),.form-floating>.form-control:focus,.form-floating>.form-control:not(:placeholder-shown){padding-top:1.625rem;padding-bottom:.625rem}.form-floating>.form-control-plaintext:-webkit-autofill,.form-floating>.form-control:-webkit-autofill{padding-top:1.625rem;padding-bottom:.625rem}.form-floating>.form-select{padding-top:1.625rem;padding-bottom:.625rem}.form-floating>.form-control:not(:-moz-placeholder-shown)~label{color:rgba(var(--bs-body-color-rgb),.65);transform:scale(.85) translateY(-.5rem) translateX(.15rem)}.form-floating>.form-control-plaintext~label,.form-floating>.form-control:focus~label,.form-floating>.form-control:not(:placeholder-shown)~label,.form-floating>.form-select~label{color:rgba(var(--bs-body-color-rgb),.65);transform:scale(.85) translateY(-.5rem) translateX(.15rem)}.form-floating>.form-control:not(:-moz-placeholder-shown)~label::after{position:absolute;inset:1rem 0.375rem;z-index:-1;height:1.5em;content:"";background-color:var(--bs-body-bg);border-radius:var(--bs-border-radius)}.form-floating>.form-control-plaintext~label::after,.form-floating>.form-control:focus~label::after,.form-floating>.form-control:not(:placeholder-shown)~label::after,.form-floating>.form-select~label::after{position:absolute;inset:1rem 0.375rem;z-index:-1;height:1.5em;content:"";background-color:var(--bs-body-bg);border-radius:var(--bs-border-radius)}.form-floating>.form-control:-webkit-autofill~label{color:rgba(var(--bs-body-color-rgb),.65);transform:scale(.85) translateY(-.5rem) translateX(.15rem)}.form-floating>.form-control-plaintext~label{border-width:var(--bs-border-width) 0}.form-floating>.form-control:disabled~label,.form-floating>:disabled~label{color:#6c757d}.form-floating>.form-control:disabled~label::after,.form-floating>:disabled~label::after{background-color:var(--bs-secondary-bg)}.input-group{position:relative;display:flex;flex-wrap:wrap;align-items:stretch;width:100%}.input-group>.form-control,.input-group>.form-floating,.input-group>.form-select{position:relative;flex:1 1 auto;width:1%;min-width:0}.input-group>.form-control:focus,.input-group>.form-floating:focus-within,.input-group>.form-select:focus{z-index:5}.input-group .btn{position:relative;z-index:2}.input-group .btn:focus{z-index:5}.input-group-text{display:flex;align-items:center;padding:.375rem .75rem;font-size:1rem;font-weight:400;line-height:1.5;color:var(--bs-body-color);text-align:center;white-space:nowrap;background-color:var(--bs-tertiary-bg);border:var(--bs-border-width) solid var(--bs-border-color);border-radius:var(--bs-border-radius)}.input-group-lg>.btn,.input-group-lg>.form-control,.input-group-lg>.form-select,.input-group-lg>.input-group-text{padding:.5rem 1rem;font-size:1.25rem;border-radius:var(--bs-border-radius-lg)}.input-group-sm>.btn,.input-group-sm>.form-control,.input-group-sm>.form-select,.input-group-sm>.input-group-text{padding:.25rem .5rem;font-size:.875rem;border-radius:var(--bs-border-radius-sm)}.input-group-lg>.form-select,.input-group-sm>.form-select{padding-right:3rem}.input-group:not(.has-validation)>.dropdown-toggle:nth-last-child(n+3),.input-group:not(.has-validation)>.form-floating:not(:last-child)>.form-control,.input-group:not(.has-validation)>.form-floating:not(:last-child)>.form-select,.input-group:not(.has-validation)>:not(:last-child):not(.dropdown-toggle):not(.dropdown-menu):not(.form-floating){border-top-right-radius:0;border-bottom-right-radius:0}.input-group.has-validation>.dropdown-toggle:nth-last-child(n+4),.input-group.has-validation>.form-floating:nth-last-child(n+3)>.form-control,.input-group.has-validation>.form-floating:nth-last-child(n+3)>.form-select,.input-group.has-validation>:nth-last-child(n+3):not(.dropdown-toggle):not(.dropdown-menu):not(.form-floating){border-top-right-radius:0;border-bottom-right-radius:0}.input-group>:not(:first-child):not(.dropdown-menu):not(.valid-tooltip):not(.valid-feedback):not(.invalid-tooltip):not(.invalid-feedback){margin-left:calc(var(--bs-border-width) * -1);border-top-left-radius:0;border-bottom-left-radius:0}.input-group>.form-floating:not(:first-child)>.form-control,.input-group>.form-floating:not(:first-child)>.form-select{border-top-left-radius:0;border-bottom-left-radius:0}.valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:.875em;color:var(--bs-form-valid-color)}.valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.25rem .5rem;margin-top:.1rem;font-size:.875rem;color:#fff;background-color:var(--bs-success);border-radius:var(--bs-border-radius)}.is-valid~.valid-feedback,.is-valid~.valid-tooltip,.was-validated :valid~.valid-feedback,.was-validated :valid~.valid-tooltip{display:block}.form-control.is-valid,.was-validated .form-control:valid{border-color:var(--bs-form-valid-border-color);padding-right:calc(1.5em + .75rem);background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");background-repeat:no-repeat;background-position:right calc(.375em + .1875rem) center;background-size:calc(.75em + .375rem) calc(.75em + .375rem)}.form-control.is-valid:focus,.was-validated .form-control:valid:focus{border-color:var(--bs-form-valid-border-color);box-shadow:0 0 0 .25rem rgba(var(--bs-success-rgb),.25)}.was-validated textarea.form-control:valid,textarea.form-control.is-valid{padding-right:calc(1.5em + .75rem);background-position:top calc(.375em + .1875rem) right calc(.375em + .1875rem)}.form-select.is-valid,.was-validated .form-select:valid{border-color:var(--bs-form-valid-border-color)}.form-select.is-valid:not([multiple]):not([size]),.form-select.is-valid:not([multiple])[size="1"],.was-validated .form-select:valid:not([multiple]):not([size]),.was-validated .form-select:valid:not([multiple])[size="1"]{--bs-form-select-bg-icon:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");padding-right:4.125rem;background-position:right .75rem center,center right 2.25rem;background-size:16px 12px,calc(.75em + .375rem) calc(.75em + .375rem)}.form-select.is-valid:focus,.was-validated .form-select:valid:focus{border-color:var(--bs-form-valid-border-color);box-shadow:0 0 0 .25rem rgba(var(--bs-success-rgb),.25)}.form-control-color.is-valid,.was-validated .form-control-color:valid{width:calc(3rem + calc(1.5em + .75rem))}.form-check-input.is-valid,.was-validated .form-check-input:valid{border-color:var(--bs-form-valid-border-color)}.form-check-input.is-valid:checked,.was-validated .form-check-input:valid:checked{background-color:var(--bs-form-valid-color)}.form-check-input.is-valid:focus,.was-validated .form-check-input:valid:focus{box-shadow:0 0 0 .25rem rgba(var(--bs-success-rgb),.25)}.form-check-input.is-valid~.form-check-label,.was-validated .form-check-input:valid~.form-check-label{color:var(--bs-form-valid-color)}.form-check-inline .form-check-input~.valid-feedback{margin-left:.5em}.input-group>.form-control:not(:focus).is-valid,.input-group>.form-floating:not(:focus-within).is-valid,.input-group>.form-select:not(:focus).is-valid,.was-validated .input-group>.form-control:not(:focus):valid,.was-validated .input-group>.form-floating:not(:focus-within):valid,.was-validated .input-group>.form-select:not(:focus):valid{z-index:3}.invalid-feedback{display:none;width:100%;margin-top:.25rem;font-size:.875em;color:var(--bs-form-invalid-color)}.invalid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.25rem .5rem;margin-top:.1rem;font-size:.875rem;color:#fff;background-color:var(--bs-danger);border-radius:var(--bs-border-radius)}.is-invalid~.invalid-feedback,.is-invalid~.invalid-tooltip,.was-validated :invalid~.invalid-feedback,.was-validated :invalid~.invalid-tooltip{display:block}.form-control.is-invalid,.was-validated .form-control:invalid{border-color:var(--bs-form-invalid-border-color);padding-right:calc(1.5em + .75rem);background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");background-repeat:no-repeat;background-position:right calc(.375em + .1875rem) center;background-size:calc(.75em + .375rem) calc(.75em + .375rem)}.form-control.is-invalid:focus,.was-validated .form-control:invalid:focus{border-color:var(--bs-form-invalid-border-color);box-shadow:0 0 0 .25rem rgba(var(--bs-danger-rgb),.25)}.was-validated textarea.form-control:invalid,textarea.form-control.is-invalid{padding-right:calc(1.5em + .75rem);background-position:top calc(.375em + .1875rem) right calc(.375em + .1875rem)}.form-select.is-invalid,.was-validated .form-select:invalid{border-color:var(--bs-form-invalid-border-color)}.form-select.is-invalid:not([multiple]):not([size]),.form-select.is-invalid:not([multiple])[size="1"],.was-validated .form-select:invalid:not([multiple]):not([size]),.was-validated .form-select:invalid:not([multiple])[size="1"]{--bs-form-select-bg-icon:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");padding-right:4.125rem;background-position:right .75rem center,center right 2.25rem;background-size:16px 12px,calc(.75em + .375rem) calc(.75em + .375rem)}.form-select.is-invalid:focus,.was-validated .form-select:invalid:focus{border-color:var(--bs-form-invalid-border-color);box-shadow:0 0 0 .25rem rgba(var(--bs-danger-rgb),.25)}.form-control-color.is-invalid,.was-validated .form-control-color:invalid{width:calc(3rem + calc(1.5em + .75rem))}.form-check-input.is-invalid,.was-validated .form-check-input:invalid{border-color:var(--bs-form-invalid-border-color)}.form-check-input.is-invalid:checked,.was-validated .form-check-input:invalid:checked{background-color:var(--bs-form-invalid-color)}.form-check-input.is-invalid:focus,.was-validated .form-check-input:invalid:focus{box-shadow:0 0 0 .25rem rgba(var(--bs-danger-rgb),.25)}.form-check-input.is-invalid~.form-check-label,.was-validated .form-check-input:invalid~.form-check-label{color:var(--bs-form-invalid-color)}.form-check-inline .form-check-input~.invalid-feedback{margin-left:.5em}.input-group>.form-control:not(:focus).is-invalid,.input-group>.form-floating:not(:focus-within).is-invalid,.input-group>.form-select:not(:focus).is-invalid,.was-validated .input-group>.form-control:not(:focus):invalid,.was-validated .input-group>.form-floating:not(:focus-within):invalid,.was-validated .input-group>.form-select:not(:focus):invalid{z-index:4}.btn{--bs-btn-padding-x:0.75rem;--bs-btn-padding-y:0.375rem;--bs-btn-font-family: ;--bs-btn-font-size:1rem;--bs-btn-font-weight:400;--bs-btn-line-height:1.5;--bs-btn-color:var(--bs-body-color);--bs-btn-bg:transparent;--bs-btn-border-width:var(--bs-border-width);--bs-btn-border-color:transparent;--bs-btn-border-radius:var(--bs-border-radius);--bs-btn-hover-border-color:transparent;--bs-btn-box-shadow:inset 0 1px 0 rgba(255, 255, 255, 0.15),0 1px 1px rgba(0, 0, 0, 0.075);--bs-btn-disabled-opacity:0.65;--bs-btn-focus-box-shadow:0 0 0 0.25rem rgba(var(--bs-btn-focus-shadow-rgb), .5);display:inline-block;padding:var(--bs-btn-padding-y) var(--bs-btn-padding-x);font-family:var(--bs-btn-font-family);font-size:var(--bs-btn-font-size);font-weight:var(--bs-btn-font-weight);line-height:var(--bs-btn-line-height);color:var(--bs-btn-color);text-align:center;text-decoration:none;vertical-align:middle;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;user-select:none;border:var(--bs-btn-border-width) solid var(--bs-btn-border-color);border-radius:var(--bs-btn-border-radius);background-color:var(--bs-btn-bg);transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out}@media (prefers-reduced-motion:reduce){.btn{transition:none}}.btn:hover{color:var(--bs-btn-hover-color);background-color:var(--bs-btn-hover-bg);border-color:var(--bs-btn-hover-border-color)}.btn-check+.btn:hover{color:var(--bs-btn-color);background-color:var(--bs-btn-bg);border-color:var(--bs-btn-border-color)}.btn:focus-visible{color:var(--bs-btn-hover-color);background-color:var(--bs-btn-hover-bg);border-color:var(--bs-btn-hover-border-color);outline:0;box-shadow:var(--bs-btn-focus-box-shadow)}.btn-check:focus-visible+.btn{border-color:var(--bs-btn-hover-border-color);outline:0;box-shadow:var(--bs-btn-focus-box-shadow)}.btn-check:checked+.btn,.btn.active,.btn.show,.btn:first-child:active,:not(.btn-check)+.btn:active{color:var(--bs-btn-active-color);background-color:var(--bs-btn-active-bg);border-color:var(--bs-btn-active-border-color)}.btn-check:checked+.btn:focus-visible,.btn.active:focus-visible,.btn.show:focus-visible,.btn:first-child:active:focus-visible,:not(.btn-check)+.btn:active:focus-visible{box-shadow:var(--bs-btn-focus-box-shadow)}.btn.disabled,.btn:disabled,fieldset:disabled .btn{color:var(--bs-btn-disabled-color);pointer-events:none;background-color:var(--bs-btn-disabled-bg);border-color:var(--bs-btn-disabled-border-color);opacity:var(--bs-btn-disabled-opacity)}.btn-primary{--bs-btn-color:#fff;--bs-btn-bg:#0d6efd;--bs-btn-border-color:#0d6efd;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#0b5ed7;--bs-btn-hover-border-color:#0a58ca;--bs-btn-focus-shadow-rgb:49,132,253;--bs-btn-active-color:#fff;--bs-btn-active-bg:#0a58ca;--bs-btn-active-border-color:#0a53be;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#fff;--bs-btn-disabled-bg:#0d6efd;--bs-btn-disabled-border-color:#0d6efd}.btn-secondary{--bs-btn-color:#fff;--bs-btn-bg:#6c757d;--bs-btn-border-color:#6c757d;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#5c636a;--bs-btn-hover-border-color:#565e64;--bs-btn-focus-shadow-rgb:130,138,145;--bs-btn-active-color:#fff;--bs-btn-active-bg:#565e64;--bs-btn-active-border-color:#51585e;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#fff;--bs-btn-disabled-bg:#6c757d;--bs-btn-disabled-border-color:#6c757d}.btn-success{--bs-btn-color:#fff;--bs-btn-bg:#198754;--bs-btn-border-color:#198754;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#157347;--bs-btn-hover-border-color:#146c43;--bs-btn-focus-shadow-rgb:60,153,110;--bs-btn-active-color:#fff;--bs-btn-active-bg:#146c43;--bs-btn-active-border-color:#13653f;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#fff;--bs-btn-disabled-bg:#198754;--bs-btn-disabled-border-color:#198754}.btn-info{--bs-btn-color:#000;--bs-btn-bg:#0dcaf0;--bs-btn-border-color:#0dcaf0;--bs-btn-hover-color:#000;--bs-btn-hover-bg:#31d2f2;--bs-btn-hover-border-color:#25cff2;--bs-btn-focus-shadow-rgb:11,172,204;--bs-btn-active-color:#000;--bs-btn-active-bg:#3dd5f3;--bs-btn-active-border-color:#25cff2;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#000;--bs-btn-disabled-bg:#0dcaf0;--bs-btn-disabled-border-color:#0dcaf0}.btn-warning{--bs-btn-color:#000;--bs-btn-bg:#ffc107;--bs-btn-border-color:#ffc107;--bs-btn-hover-color:#000;--bs-btn-hover-bg:#ffca2c;--bs-btn-hover-border-color:#ffc720;--bs-btn-focus-shadow-rgb:217,164,6;--bs-btn-active-color:#000;--bs-btn-active-bg:#ffcd39;--bs-btn-active-border-color:#ffc720;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#000;--bs-btn-disabled-bg:#ffc107;--bs-btn-disabled-border-color:#ffc107}.btn-danger{--bs-btn-color:#fff;--bs-btn-bg:#dc3545;--bs-btn-border-color:#dc3545;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#bb2d3b;--bs-btn-hover-border-color:#b02a37;--bs-btn-focus-shadow-rgb:225,83,97;--bs-btn-active-color:#fff;--bs-btn-active-bg:#b02a37;--bs-btn-active-border-color:#a52834;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#fff;--bs-btn-disabled-bg:#dc3545;--bs-btn-disabled-border-color:#dc3545}.btn-light{--bs-btn-color:#000;--bs-btn-bg:#f8f9fa;--bs-btn-border-color:#f8f9fa;--bs-btn-hover-color:#000;--bs-btn-hover-bg:#d3d4d5;--bs-btn-hover-border-color:#c6c7c8;--bs-btn-focus-shadow-rgb:211,212,213;--bs-btn-active-color:#000;--bs-btn-active-bg:#c6c7c8;--bs-btn-active-border-color:#babbbc;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#000;--bs-btn-disabled-bg:#f8f9fa;--bs-btn-disabled-border-color:#f8f9fa}.btn-dark{--bs-btn-color:#fff;--bs-btn-bg:#212529;--bs-btn-border-color:#212529;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#424649;--bs-btn-hover-border-color:#373b3e;--bs-btn-focus-shadow-rgb:66,70,73;--bs-btn-active-color:#fff;--bs-btn-active-bg:#4d5154;--bs-btn-active-border-color:#373b3e;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#fff;--bs-btn-disabled-bg:#212529;--bs-btn-disabled-border-color:#212529}.btn-outline-primary{--bs-btn-color:#0d6efd;--bs-btn-border-color:#0d6efd;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#0d6efd;--bs-btn-hover-border-color:#0d6efd;--bs-btn-focus-shadow-rgb:13,110,253;--bs-btn-active-color:#fff;--bs-btn-active-bg:#0d6efd;--bs-btn-active-border-color:#0d6efd;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#0d6efd;--bs-btn-disabled-bg:transparent;--bs-btn-disabled-border-color:#0d6efd;--bs-gradient:none}.btn-outline-secondary{--bs-btn-color:#6c757d;--bs-btn-border-color:#6c757d;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#6c757d;--bs-btn-hover-border-color:#6c757d;--bs-btn-focus-shadow-rgb:108,117,125;--bs-btn-active-color:#fff;--bs-btn-active-bg:#6c757d;--bs-btn-active-border-color:#6c757d;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#6c757d;--bs-btn-disabled-bg:transparent;--bs-btn-disabled-border-color:#6c757d;--bs-gradient:none}.btn-outline-success{--bs-btn-color:#198754;--bs-btn-border-color:#198754;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#198754;--bs-btn-hover-border-color:#198754;--bs-btn-focus-shadow-rgb:25,135,84;--bs-btn-active-color:#fff;--bs-btn-active-bg:#198754;--bs-btn-active-border-color:#198754;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#198754;--bs-btn-disabled-bg:transparent;--bs-btn-disabled-border-color:#198754;--bs-gradient:none}.btn-outline-info{--bs-btn-color:#0dcaf0;--bs-btn-border-color:#0dcaf0;--bs-btn-hover-color:#000;--bs-btn-hover-bg:#0dcaf0;--bs-btn-hover-border-color:#0dcaf0;--bs-btn-focus-shadow-rgb:13,202,240;--bs-btn-active-color:#000;--bs-btn-active-bg:#0dcaf0;--bs-btn-active-border-color:#0dcaf0;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#0dcaf0;--bs-btn-disabled-bg:transparent;--bs-btn-disabled-border-color:#0dcaf0;--bs-gradient:none}.btn-outline-warning{--bs-btn-color:#ffc107;--bs-btn-border-color:#ffc107;--bs-btn-hover-color:#000;--bs-btn-hover-bg:#ffc107;--bs-btn-hover-border-color:#ffc107;--bs-btn-focus-shadow-rgb:255,193,7;--bs-btn-active-color:#000;--bs-btn-active-bg:#ffc107;--bs-btn-active-border-color:#ffc107;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#ffc107;--bs-btn-disabled-bg:transparent;--bs-btn-disabled-border-color:#ffc107;--bs-gradient:none}.btn-outline-danger{--bs-btn-color:#dc3545;--bs-btn-border-color:#dc3545;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#dc3545;--bs-btn-hover-border-color:#dc3545;--bs-btn-focus-shadow-rgb:220,53,69;--bs-btn-active-color:#fff;--bs-btn-active-bg:#dc3545;--bs-btn-active-border-color:#dc3545;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#dc3545;--bs-btn-disabled-bg:transparent;--bs-btn-disabled-border-color:#dc3545;--bs-gradient:none}.btn-outline-light{--bs-btn-color:#f8f9fa;--bs-btn-border-color:#f8f9fa;--bs-btn-hover-color:#000;--bs-btn-hover-bg:#f8f9fa;--bs-btn-hover-border-color:#f8f9fa;--bs-btn-focus-shadow-rgb:248,249,250;--bs-btn-active-color:#000;--bs-btn-active-bg:#f8f9fa;--bs-btn-active-border-color:#f8f9fa;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#f8f9fa;--bs-btn-disabled-bg:transparent;--bs-btn-disabled-border-color:#f8f9fa;--bs-gradient:none}.btn-outline-dark{--bs-btn-color:#212529;--bs-btn-border-color:#212529;--bs-btn-hover-color:#fff;--bs-btn-hover-bg:#212529;--bs-btn-hover-border-color:#212529;--bs-btn-focus-shadow-rgb:33,37,41;--bs-btn-active-color:#fff;--bs-btn-active-bg:#212529;--bs-btn-active-border-color:#212529;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#212529;--bs-btn-disabled-bg:transparent;--bs-btn-disabled-border-color:#212529;--bs-gradient:none}.btn-link{--bs-btn-font-weight:400;--bs-btn-color:var(--bs-link-color);--bs-btn-bg:transparent;--bs-btn-border-color:transparent;--bs-btn-hover-color:var(--bs-link-hover-color);--bs-btn-hover-border-color:transparent;--bs-btn-active-color:var(--bs-link-hover-color);--bs-btn-active-border-color:transparent;--bs-btn-disabled-color:#6c757d;--bs-btn-disabled-border-color:transparent;--bs-btn-box-shadow:0 0 0 #000;--bs-btn-focus-shadow-rgb:49,132,253;text-decoration:underline}.btn-link:focus-visible{color:var(--bs-btn-color)}.btn-link:hover{color:var(--bs-btn-hover-color)}.btn-group-lg>.btn,.btn-lg{--bs-btn-padding-y:0.5rem;--bs-btn-padding-x:1rem;--bs-btn-font-size:1.25rem;--bs-btn-border-radius:var(--bs-border-radius-lg)}.btn-group-sm>.btn,.btn-sm{--bs-btn-padding-y:0.25rem;--bs-btn-padding-x:0.5rem;--bs-btn-font-size:0.875rem;--bs-btn-border-radius:var(--bs-border-radius-sm)}.fade{transition:opacity .15s linear}@media (prefers-reduced-motion:reduce){.fade{transition:none}}.fade:not(.show){opacity:0}.collapse:not(.show){display:none}.collapsing{height:0;overflow:hidden;transition:height .35s ease}@media (prefers-reduced-motion:reduce){.collapsing{transition:none}}.collapsing.collapse-horizontal{width:0;height:auto;transition:width .35s ease}@media (prefers-reduced-motion:reduce){.collapsing.collapse-horizontal{transition:none}}.dropdown,.dropdown-center,.dropend,.dropstart,.dropup,.dropup-center{position:relative}.dropdown-toggle{white-space:nowrap}.dropdown-toggle::after{display:inline-block;margin-left:.255em;vertical-align:.255em;content:"";border-top:.3em solid;border-right:.3em solid transparent;border-bottom:0;border-left:.3em solid transparent}.dropdown-toggle:empty::after{margin-left:0}.dropdown-menu{--bs-dropdown-zindex:1000;--bs-dropdown-min-width:10rem;--bs-dropdown-padding-x:0;--bs-dropdown-padding-y:0.5rem;--bs-dropdown-spacer:0.125rem;--bs-dropdown-font-size:1rem;--bs-dropdown-color:var(--bs-body-color);--bs-dropdown-bg:var(--bs-body-bg);--bs-dropdown-border-color:var(--bs-border-color-translucent);--bs-dropdown-border-radius:var(--bs-border-radius);--bs-dropdown-border-width:var(--bs-border-width);--bs-dropdown-inner-border-radius:calc(var(--bs-border-radius) - var(--bs-border-width));--bs-dropdown-divider-bg:var(--bs-border-color-translucent);--bs-dropdown-divider-margin-y:0.5rem;--bs-dropdown-box-shadow:var(--bs-box-shadow);--bs-dropdown-link-color:var(--bs-body-color);--bs-dropdown-link-hover-color:var(--bs-body-color);--bs-dropdown-link-hover-bg:var(--bs-tertiary-bg);--bs-dropdown-link-active-color:#fff;--bs-dropdown-link-active-bg:#0d6efd;--bs-dropdown-link-disabled-color:var(--bs-tertiary-color);--bs-dropdown-item-padding-x:1rem;--bs-dropdown-item-padding-y:0.25rem;--bs-dropdown-header-color:#6c757d;--bs-dropdown-header-padding-x:1rem;--bs-dropdown-header-padding-y:0.5rem;position:absolute;z-index:var(--bs-dropdown-zindex);display:none;min-width:var(--bs-dropdown-min-width);padding:var(--bs-dropdown-padding-y) var(--bs-dropdown-padding-x);margin:0;font-size:var(--bs-dropdown-font-size);color:var(--bs-dropdown-color);text-align:left;list-style:none;background-color:var(--bs-dropdown-bg);background-clip:padding-box;border:var(--bs-dropdown-border-width) solid var(--bs-dropdown-border-color);border-radius:var(--bs-dropdown-border-radius)}.dropdown-menu[data-bs-popper]{top:100%;left:0;margin-top:var(--bs-dropdown-spacer)}.dropdown-menu-start{--bs-position:start}.dropdown-menu-start[data-bs-popper]{right:auto;left:0}.dropdown-menu-end{--bs-position:end}.dropdown-menu-end[data-bs-popper]{right:0;left:auto}@media (min-width:576px){.dropdown-menu-sm-start{--bs-position:start}.dropdown-menu-sm-start[data-bs-popper]{right:auto;left:0}.dropdown-menu-sm-end{--bs-position:end}.dropdown-menu-sm-end[data-bs-popper]{right:0;left:auto}}@media (min-width:768px){.dropdown-menu-md-start{--bs-position:start}.dropdown-menu-md-start[data-bs-popper]{right:auto;left:0}.dropdown-menu-md-end{--bs-position:end}.dropdown-menu-md-end[data-bs-popper]{right:0;left:auto}}@media (min-width:992px){.dropdown-menu-lg-start{--bs-position:start}.dropdown-menu-lg-start[data-bs-popper]{right:auto;left:0}.dropdown-menu-lg-end{--bs-position:end}.dropdown-menu-lg-end[data-bs-popper]{right:0;left:auto}}@media (min-width:1200px){.dropdown-menu-xl-start{--bs-position:start}.dropdown-menu-xl-start[data-bs-popper]{right:auto;left:0}.dropdown-menu-xl-end{--bs-position:end}.dropdown-menu-xl-end[data-bs-popper]{right:0;left:auto}}@media (min-width:1400px){.dropdown-menu-xxl-start{--bs-position:start}.dropdown-menu-xxl-start[data-bs-popper]{right:auto;left:0}.dropdown-menu-xxl-end{--bs-position:end}.dropdown-menu-xxl-end[data-bs-popper]{right:0;left:auto}}.dropup .dropdown-menu[data-bs-popper]{top:auto;bottom:100%;margin-top:0;margin-bottom:var(--bs-dropdown-spacer)}.dropup .dropdown-toggle::after{display:inline-block;margin-left:.255em;vertical-align:.255em;content:"";border-top:0;border-right:.3em solid transparent;border-bottom:.3em solid;border-left:.3em solid transparent}.dropup .dropdown-toggle:empty::after{margin-left:0}.dropend .dropdown-menu[data-bs-popper]{top:0;right:auto;left:100%;margin-top:0;margin-left:var(--bs-dropdown-spacer)}.dropend .dropdown-toggle::after{display:inline-block;margin-left:.255em;vertical-align:.255em;content:"";border-top:.3em solid transparent;border-right:0;border-bottom:.3em solid transparent;border-left:.3em solid}.dropend .dropdown-toggle:empty::after{margin-left:0}.dropend .dropdown-toggle::after{vertical-align:0}.dropstart .dropdown-menu[data-bs-popper]{top:0;right:100%;left:auto;margin-top:0;margin-right:var(--bs-dropdown-spacer)}.dropstart .dropdown-toggle::after{display:inline-block;margin-left:.255em;vertical-align:.255em;content:""}.dropstart .dropdown-toggle::after{display:none}.dropstart .dropdown-toggle::before{display:inline-block;margin-right:.255em;vertical-align:.255em;content:"";border-top:.3em solid transparent;border-right:.3em solid;border-bottom:.3em solid transparent}.dropstart .dropdown-toggle:empty::after{margin-left:0}.dropstart .dropdown-toggle::before{vertical-align:0}.dropdown-divider{height:0;margin:var(--bs-dropdown-divider-margin-y) 0;overflow:hidden;border-top:1px solid var(--bs-dropdown-divider-bg);opacity:1}.dropdown-item{display:block;width:100%;padding:var(--bs-dropdown-item-padding-y) var(--bs-dropdown-item-padding-x);clear:both;font-weight:400;color:var(--bs-dropdown-link-color);text-align:inherit;text-decoration:none;white-space:nowrap;background-color:transparent;border:0;border-radius:var(--bs-dropdown-item-border-radius,0)}.dropdown-item:focus,.dropdown-item:hover{color:var(--bs-dropdown-link-hover-color);background-color:var(--bs-dropdown-link-hover-bg)}.dropdown-item.active,.dropdown-item:active{color:var(--bs-dropdown-link-active-color);text-decoration:none;background-color:var(--bs-dropdown-link-active-bg)}.dropdown-item.disabled,.dropdown-item:disabled{color:var(--bs-dropdown-link-disabled-color);pointer-events:none;background-color:transparent}.dropdown-menu.show{display:block}.dropdown-header{display:block;padding:var(--bs-dropdown-header-padding-y) var(--bs-dropdown-header-padding-x);margin-bottom:0;font-size:.875rem;color:var(--bs-dropdown-header-color);white-space:nowrap}.dropdown-item-text{display:block;padding:var(--bs-dropdown-item-padding-y) var(--bs-dropdown-item-padding-x);color:var(--bs-dropdown-link-color)}.dropdown-menu-dark{--bs-dropdown-color:#dee2e6;--bs-dropdown-bg:#343a40;--bs-dropdown-border-color:var(--bs-border-color-translucent);--bs-dropdown-box-shadow: ;--bs-dropdown-link-color:#dee2e6;--bs-dropdown-link-hover-color:#fff;--bs-dropdown-divider-bg:var(--bs-border-color-translucent);--bs-dropdown-link-hover-bg:rgba(255, 255, 255, 0.15);--bs-dropdown-link-active-color:#fff;--bs-dropdown-link-active-bg:#0d6efd;--bs-dropdown-link-disabled-color:#adb5bd;--bs-dropdown-header-color:#adb5bd}.btn-group,.btn-group-vertical{position:relative;display:inline-flex;vertical-align:middle}.btn-group-vertical>.btn,.btn-group>.btn{position:relative;flex:1 1 auto}.btn-group-vertical>.btn-check:checked+.btn,.btn-group-vertical>.btn-check:focus+.btn,.btn-group-vertical>.btn.active,.btn-group-vertical>.btn:active,.btn-group-vertical>.btn:focus,.btn-group-vertical>.btn:hover,.btn-group>.btn-check:checked+.btn,.btn-group>.btn-check:focus+.btn,.btn-group>.btn.active,.btn-group>.btn:active,.btn-group>.btn:focus,.btn-group>.btn:hover{z-index:1}.btn-toolbar{display:flex;flex-wrap:wrap;justify-content:flex-start}.btn-toolbar .input-group{width:auto}.btn-group{border-radius:var(--bs-border-radius)}.btn-group>.btn-group:not(:first-child),.btn-group>:not(.btn-check:first-child)+.btn{margin-left:calc(var(--bs-border-width) * -1)}.btn-group>.btn-group:not(:last-child)>.btn,.btn-group>.btn.dropdown-toggle-split:first-child,.btn-group>.btn:not(:last-child):not(.dropdown-toggle){border-top-right-radius:0;border-bottom-right-radius:0}.btn-group>.btn-group:not(:first-child)>.btn,.btn-group>.btn:nth-child(n+3),.btn-group>:not(.btn-check)+.btn{border-top-left-radius:0;border-bottom-left-radius:0}.dropdown-toggle-split{padding-right:.5625rem;padding-left:.5625rem}.dropdown-toggle-split::after,.dropend .dropdown-toggle-split::after,.dropup .dropdown-toggle-split::after{margin-left:0}.dropstart .dropdown-toggle-split::before{margin-right:0}.btn-group-sm>.btn+.dropdown-toggle-split,.btn-sm+.dropdown-toggle-split{padding-right:.375rem;padding-left:.375rem}.btn-group-lg>.btn+.dropdown-toggle-split,.btn-lg+.dropdown-toggle-split{padding-right:.75rem;padding-left:.75rem}.btn-group-vertical{flex-direction:column;align-items:flex-start;justify-content:center}.btn-group-vertical>.btn,.btn-group-vertical>.btn-group{width:100%}.btn-group-vertical>.btn-group:not(:first-child),.btn-group-vertical>.btn:not(:first-child){margin-top:calc(var(--bs-border-width) * -1)}.btn-group-vertical>.btn-group:not(:last-child)>.btn,.btn-group-vertical>.btn:not(:last-child):not(.dropdown-toggle){border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical>.btn-group:not(:first-child)>.btn,.btn-group-vertical>.btn~.btn{border-top-left-radius:0;border-top-right-radius:0}.nav{--bs-nav-link-padding-x:1rem;--bs-nav-link-padding-y:0.5rem;--bs-nav-link-font-weight: ;--bs-nav-link-color:var(--bs-link-color);--bs-nav-link-hover-color:var(--bs-link-hover-color);--bs-nav-link-disabled-color:var(--bs-secondary-color);display:flex;flex-wrap:wrap;padding-left:0;margin-bottom:0;list-style:none}.nav-link{display:block;padding:var(--bs-nav-link-padding-y) var(--bs-nav-link-padding-x);font-size:var(--bs-nav-link-font-size);font-weight:var(--bs-nav-link-font-weight);color:var(--bs-nav-link-color);text-decoration:none;background:0 0;border:0;transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out}@media (prefers-reduced-motion:reduce){.nav-link{transition:none}}.nav-link:focus,.nav-link:hover{color:var(--bs-nav-link-hover-color)}.nav-link:focus-visible{outline:0;box-shadow:0 0 0 .25rem rgba(13,110,253,.25)}.nav-link.disabled,.nav-link:disabled{color:var(--bs-nav-link-disabled-color);pointer-events:none;cursor:default}.nav-tabs{--bs-nav-tabs-border-width:var(--bs-border-width);--bs-nav-tabs-border-color:var(--bs-border-color);--bs-nav-tabs-border-radius:var(--bs-border-radius);--bs-nav-tabs-link-hover-border-color:var(--bs-secondary-bg) var(--bs-secondary-bg) var(--bs-border-color);--bs-nav-tabs-link-active-color:var(--bs-emphasis-color);--bs-nav-tabs-link-active-bg:var(--bs-body-bg);--bs-nav-tabs-link-active-border-color:var(--bs-border-color) var(--bs-border-color) var(--bs-body-bg);border-bottom:var(--bs-nav-tabs-border-width) solid var(--bs-nav-tabs-border-color)}.nav-tabs .nav-link{margin-bottom:calc(-1 * var(--bs-nav-tabs-border-width));border:var(--bs-nav-tabs-border-width) solid transparent;border-top-left-radius:var(--bs-nav-tabs-border-radius);border-top-right-radius:var(--bs-nav-tabs-border-radius)}.nav-tabs .nav-link:focus,.nav-tabs .nav-link:hover{isolation:isolate;border-color:var(--bs-nav-tabs-link-hover-border-color)}.nav-tabs .nav-item.show .nav-link,.nav-tabs .nav-link.active{color:var(--bs-nav-tabs-link-active-color);background-color:var(--bs-nav-tabs-link-active-bg);border-color:var(--bs-nav-tabs-link-active-border-color)}.nav-tabs .dropdown-menu{margin-top:calc(-1 * var(--bs-nav-tabs-border-width));border-top-left-radius:0;border-top-right-radius:0}.nav-pills{--bs-nav-pills-border-radius:var(--bs-border-radius);--bs-nav-pills-link-active-color:#fff;--bs-nav-pills-link-active-bg:#0d6efd}.nav-pills .nav-link{border-radius:var(--bs-nav-pills-border-radius)}.nav-pills .nav-link.active,.nav-pills .show>.nav-link{color:var(--bs-nav-pills-link-active-color);background-color:var(--bs-nav-pills-link-active-bg)}.nav-underline{--bs-nav-underline-gap:1rem;--bs-nav-underline-border-width:0.125rem;--bs-nav-underline-link-active-color:var(--bs-emphasis-color);gap:var(--bs-nav-underline-gap)}.nav-underline .nav-link{padding-right:0;padding-left:0;border-bottom:var(--bs-nav-underline-border-width) solid transparent}.nav-underline .nav-link:focus,.nav-underline .nav-link:hover{border-bottom-color:currentcolor}.nav-underline .nav-link.active,.nav-underline .show>.nav-link{font-weight:700;color:var(--bs-nav-underline-link-active-color);border-bottom-color:currentcolor}.nav-fill .nav-item,.nav-fill>.nav-link{flex:1 1 auto;text-align:center}.nav-justified .nav-item,.nav-justified>.nav-link{flex-basis:0;flex-grow:1;text-align:center}.nav-fill .nav-item .nav-link,.nav-justified .nav-item .nav-link{width:100%}.tab-content>.tab-pane{display:none}.tab-content>.active{display:block}.navbar{--bs-navbar-padding-x:0;--bs-navbar-padding-y:0.5rem;--bs-navbar-color:rgba(var(--bs-emphasis-color-rgb), 0.65);--bs-navbar-hover-color:rgba(var(--bs-emphasis-color-rgb), 0.8);--bs-navbar-disabled-color:rgba(var(--bs-emphasis-color-rgb), 0.3);--bs-navbar-active-color:rgba(var(--bs-emphasis-color-rgb), 1);--bs-navbar-brand-padding-y:0.3125rem;--bs-navbar-brand-margin-end:1rem;--bs-navbar-brand-font-size:1.25rem;--bs-navbar-brand-color:rgba(var(--bs-emphasis-color-rgb), 1);--bs-navbar-brand-hover-color:rgba(var(--bs-emphasis-color-rgb), 1);--bs-navbar-nav-link-padding-x:0.5rem;--bs-navbar-toggler-padding-y:0.25rem;--bs-navbar-toggler-padding-x:0.75rem;--bs-navbar-toggler-font-size:1.25rem;--bs-navbar-toggler-icon-bg:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%2833, 37, 41, 0.75%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");--bs-navbar-toggler-border-color:rgba(var(--bs-emphasis-color-rgb), 0.15);--bs-navbar-toggler-border-radius:var(--bs-border-radius);--bs-navbar-toggler-focus-width:0.25rem;--bs-navbar-toggler-transition:box-shadow 0.15s ease-in-out;position:relative;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:var(--bs-navbar-padding-y) var(--bs-navbar-padding-x)}.navbar>.container,.navbar>.container-fluid,.navbar>.container-lg,.navbar>.container-md,.navbar>.container-sm,.navbar>.container-xl,.navbar>.container-xxl{display:flex;flex-wrap:inherit;align-items:center;justify-content:space-between}.navbar-brand{padding-top:var(--bs-navbar-brand-padding-y);padding-bottom:var(--bs-navbar-brand-padding-y);margin-right:var(--bs-navbar-brand-margin-end);font-size:var(--bs-navbar-brand-font-size);color:var(--bs-navbar-brand-color);text-decoration:none;white-space:nowrap}.navbar-brand:focus,.navbar-brand:hover{color:var(--bs-navbar-brand-hover-color)}.navbar-nav{--bs-nav-link-padding-x:0;--bs-nav-link-padding-y:0.5rem;--bs-nav-link-font-weight: ;--bs-nav-link-color:var(--bs-navbar-color);--bs-nav-link-hover-color:var(--bs-navbar-hover-color);--bs-nav-link-disabled-color:var(--bs-navbar-disabled-color);display:flex;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}.navbar-nav .nav-link.active,.navbar-nav .nav-link.show{color:var(--bs-navbar-active-color)}.navbar-nav .dropdown-menu{position:static}.navbar-text{padding-top:.5rem;padding-bottom:.5rem;color:var(--bs-navbar-color)}.navbar-text a,.navbar-text a:focus,.navbar-text a:hover{color:var(--bs-navbar-active-color)}.navbar-collapse{flex-basis:100%;flex-grow:1;align-items:center}.navbar-toggler{padding:var(--bs-navbar-toggler-padding-y) var(--bs-navbar-toggler-padding-x);font-size:var(--bs-navbar-toggler-font-size);line-height:1;color:var(--bs-navbar-color);background-color:transparent;border:var(--bs-border-width) solid var(--bs-navbar-toggler-border-color);border-radius:var(--bs-navbar-toggler-border-radius);transition:var(--bs-navbar-toggler-transition)}@media (prefers-reduced-motion:reduce){.navbar-toggler{transition:none}}.navbar-toggler:hover{text-decoration:none}.navbar-toggler:focus{text-decoration:none;outline:0;box-shadow:0 0 0 var(--bs-navbar-toggler-focus-width)}.navbar-toggler-icon{display:inline-block;width:1.5em;height:1.5em;vertical-align:middle;background-image:var(--bs-navbar-toggler-icon-bg);background-repeat:no-repeat;background-position:center;background-size:100%}.navbar-nav-scroll{max-height:var(--bs-scroll-height,75vh);overflow-y:auto}@media (min-width:576px){.navbar-expand-sm{flex-wrap:nowrap;justify-content:flex-start}.navbar-expand-sm .navbar-nav{flex-direction:row}.navbar-expand-sm .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-sm .navbar-nav .nav-link{padding-right:var(--bs-navbar-nav-link-padding-x);padding-left:var(--bs-navbar-nav-link-padding-x)}.navbar-expand-sm .navbar-nav-scroll{overflow:visible}.navbar-expand-sm .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-sm .navbar-toggler{display:none}.navbar-expand-sm .offcanvas{position:static;z-index:auto;flex-grow:1;width:auto!important;height:auto!important;visibility:visible!important;background-color:transparent!important;border:0!important;transform:none!important;transition:none}.navbar-expand-sm .offcanvas .offcanvas-header{display:none}.navbar-expand-sm .offcanvas .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible}}@media (min-width:768px){.navbar-expand-md{flex-wrap:nowrap;justify-content:flex-start}.navbar-expand-md .navbar-nav{flex-direction:row}.navbar-expand-md .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-md .navbar-nav .nav-link{padding-right:var(--bs-navbar-nav-link-padding-x);padding-left:var(--bs-navbar-nav-link-padding-x)}.navbar-expand-md .navbar-nav-scroll{overflow:visible}.navbar-expand-md .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-md .navbar-toggler{display:none}.navbar-expand-md .offcanvas{position:static;z-index:auto;flex-grow:1;width:auto!important;height:auto!important;visibility:visible!important;background-color:transparent!important;border:0!important;transform:none!important;transition:none}.navbar-expand-md .offcanvas .offcanvas-header{display:none}.navbar-expand-md .offcanvas .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible}}@media (min-width:992px){.navbar-expand-lg{flex-wrap:nowrap;justify-content:flex-start}.navbar-expand-lg .navbar-nav{flex-direction:row}.navbar-expand-lg .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-lg .navbar-nav .nav-link{padding-right:var(--bs-navbar-nav-link-padding-x);padding-left:var(--bs-navbar-nav-link-padding-x)}.navbar-expand-lg .navbar-nav-scroll{overflow:visible}.navbar-expand-lg .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-lg .navbar-toggler{display:none}.navbar-expand-lg .offcanvas{position:static;z-index:auto;flex-grow:1;width:auto!important;height:auto!important;visibility:visible!important;background-color:transparent!important;border:0!important;transform:none!important;transition:none}.navbar-expand-lg .offcanvas .offcanvas-header{display:none}.navbar-expand-lg .offcanvas .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible}}@media (min-width:1200px){.navbar-expand-xl{flex-wrap:nowrap;justify-content:flex-start}.navbar-expand-xl .navbar-nav{flex-direction:row}.navbar-expand-xl .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-xl .navbar-nav .nav-link{padding-right:var(--bs-navbar-nav-link-padding-x);padding-left:var(--bs-navbar-nav-link-padding-x)}.navbar-expand-xl .navbar-nav-scroll{overflow:visible}.navbar-expand-xl .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-xl .navbar-toggler{display:none}.navbar-expand-xl .offcanvas{position:static;z-index:auto;flex-grow:1;width:auto!important;height:auto!important;visibility:visible!important;background-color:transparent!important;border:0!important;transform:none!important;transition:none}.navbar-expand-xl .offcanvas .offcanvas-header{display:none}.navbar-expand-xl .offcanvas .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible}}@media (min-width:1400px){.navbar-expand-xxl{flex-wrap:nowrap;justify-content:flex-start}.navbar-expand-xxl .navbar-nav{flex-direction:row}.navbar-expand-xxl .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-xxl .navbar-nav .nav-link{padding-right:var(--bs-navbar-nav-link-padding-x);padding-left:var(--bs-navbar-nav-link-padding-x)}.navbar-expand-xxl .navbar-nav-scroll{overflow:visible}.navbar-expand-xxl .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-xxl .navbar-toggler{display:none}.navbar-expand-xxl .offcanvas{position:static;z-index:auto;flex-grow:1;width:auto!important;height:auto!important;visibility:visible!important;background-color:transparent!important;border:0!important;transform:none!important;transition:none}.navbar-expand-xxl .offcanvas .offcanvas-header{display:none}.navbar-expand-xxl .offcanvas .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible}}.navbar-expand{flex-wrap:nowrap;justify-content:flex-start}.navbar-expand .navbar-nav{flex-direction:row}.navbar-expand .navbar-nav .dropdown-menu{position:absolute}.navbar-expand .navbar-nav .nav-link{padding-right:var(--bs-navbar-nav-link-padding-x);padding-left:var(--bs-navbar-nav-link-padding-x)}.navbar-expand .navbar-nav-scroll{overflow:visible}.navbar-expand .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand .navbar-toggler{display:none}.navbar-expand .offcanvas{position:static;z-index:auto;flex-grow:1;width:auto!important;height:auto!important;visibility:visible!important;background-color:transparent!important;border:0!important;transform:none!important;transition:none}.navbar-expand .offcanvas .offcanvas-header{display:none}.navbar-expand .offcanvas .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible}.navbar-dark,.navbar[data-bs-theme=dark]{--bs-navbar-color:rgba(255, 255, 255, 0.55);--bs-navbar-hover-color:rgba(255, 255, 255, 0.75);--bs-navbar-disabled-color:rgba(255, 255, 255, 0.25);--bs-navbar-active-color:#fff;--bs-navbar-brand-color:#fff;--bs-navbar-brand-hover-color:#fff;--bs-navbar-toggler-border-color:rgba(255, 255, 255, 0.1);--bs-navbar-toggler-icon-bg:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e")}[data-bs-theme=dark] .navbar-toggler-icon{--bs-navbar-toggler-icon-bg:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e")}.card{--bs-card-spacer-y:1rem;--bs-card-spacer-x:1rem;--bs-card-title-spacer-y:0.5rem;--bs-card-title-color: ;--bs-card-subtitle-color: ;--bs-card-border-width:var(--bs-border-width);--bs-card-border-color:var(--bs-border-color-translucent);--bs-card-border-radius:var(--bs-border-radius);--bs-card-box-shadow: ;--bs-card-inner-border-radius:calc(var(--bs-border-radius) - (var(--bs-border-width)));--bs-card-cap-padding-y:0.5rem;--bs-card-cap-padding-x:1rem;--bs-card-cap-bg:rgba(var(--bs-body-color-rgb), 0.03);--bs-card-cap-color: ;--bs-card-height: ;--bs-card-color: ;--bs-card-bg:var(--bs-body-bg);--bs-card-img-overlay-padding:1rem;--bs-card-group-margin:0.75rem;position:relative;display:flex;flex-direction:column;min-width:0;height:var(--bs-card-height);color:var(--bs-body-color);word-wrap:break-word;background-color:var(--bs-card-bg);background-clip:border-box;border:var(--bs-card-border-width) solid var(--bs-card-border-color);border-radius:var(--bs-card-border-radius)}.card>hr{margin-right:0;margin-left:0}.card>.list-group{border-top:inherit;border-bottom:inherit}.card>.list-group:first-child{border-top-width:0;border-top-left-radius:var(--bs-card-inner-border-radius);border-top-right-radius:var(--bs-card-inner-border-radius)}.card>.list-group:last-child{border-bottom-width:0;border-bottom-right-radius:var(--bs-card-inner-border-radius);border-bottom-left-radius:var(--bs-card-inner-border-radius)}.card>.card-header+.list-group,.card>.list-group+.card-footer{border-top:0}.card-body{flex:1 1 auto;padding:var(--bs-card-spacer-y) var(--bs-card-spacer-x);color:var(--bs-card-color)}.card-title{margin-bottom:var(--bs-card-title-spacer-y);color:var(--bs-card-title-color)}.card-subtitle{margin-top:calc(-.5 * var(--bs-card-title-spacer-y));margin-bottom:0;color:var(--bs-card-subtitle-color)}.card-text:last-child{margin-bottom:0}.card-link+.card-link{margin-left:var(--bs-card-spacer-x)}.card-header{padding:var(--bs-card-cap-padding-y) var(--bs-card-cap-padding-x);margin-bottom:0;color:var(--bs-card-cap-color);background-color:var(--bs-card-cap-bg);border-bottom:var(--bs-card-border-width) solid var(--bs-card-border-color)}.card-header:first-child{border-radius:var(--bs-card-inner-border-radius) var(--bs-card-inner-border-radius) 0 0}.card-footer{padding:var(--bs-card-cap-padding-y) var(--bs-card-cap-padding-x);color:var(--bs-card-cap-color);background-color:var(--bs-card-cap-bg);border-top:var(--bs-card-border-width) solid var(--bs-card-border-color)}.card-footer:last-child{border-radius:0 0 var(--bs-card-inner-border-radius) var(--bs-card-inner-border-radius)}.card-header-tabs{margin-right:calc(-.5 * var(--bs-card-cap-padding-x));margin-bottom:calc(-1 * var(--bs-card-cap-padding-y));margin-left:calc(-.5 * var(--bs-card-cap-padding-x));border-bottom:0}.card-header-tabs .nav-link.active{background-color:var(--bs-card-bg);border-bottom-color:var(--bs-card-bg)}.card-header-pills{margin-right:calc(-.5 * var(--bs-card-cap-padding-x));margin-left:calc(-.5 * var(--bs-card-cap-padding-x))}.card-img-overlay{position:absolute;top:0;right:0;bottom:0;left:0;padding:var(--bs-card-img-overlay-padding);border-radius:var(--bs-card-inner-border-radius)}.card-img,.card-img-bottom,.card-img-top{width:100%}.card-img,.card-img-top{border-top-left-radius:var(--bs-card-inner-border-radius);border-top-right-radius:var(--bs-card-inner-border-radius)}.card-img,.card-img-bottom{border-bottom-right-radius:var(--bs-card-inner-border-radius);border-bottom-left-radius:var(--bs-card-inner-border-radius)}.card-group>.card{margin-bottom:var(--bs-card-group-margin)}@media (min-width:576px){.card-group{display:flex;flex-flow:row wrap}.card-group>.card{flex:1 0 0%;margin-bottom:0}.card-group>.card+.card{margin-left:0;border-left:0}.card-group>.card:not(:last-child){border-top-right-radius:0;border-bottom-right-radius:0}.card-group>.card:not(:last-child) .card-header,.card-group>.card:not(:last-child) .card-img-top{border-top-right-radius:0}.card-group>.card:not(:last-child) .card-footer,.card-group>.card:not(:last-child) .card-img-bottom{border-bottom-right-radius:0}.card-group>.card:not(:first-child){border-top-left-radius:0;border-bottom-left-radius:0}.card-group>.card:not(:first-child) .card-header,.card-group>.card:not(:first-child) .card-img-top{border-top-left-radius:0}.card-group>.card:not(:first-child) .card-footer,.card-group>.card:not(:first-child) .card-img-bottom{border-bottom-left-radius:0}}.accordion{--bs-accordion-color:var(--bs-body-color);--bs-accordion-bg:var(--bs-body-bg);--bs-accordion-transition:color 0.15s ease-in-out,background-color 0.15s ease-in-out,border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out,border-radius 0.15s ease;--bs-accordion-border-color:var(--bs-border-color);--bs-accordion-border-width:var(--bs-border-width);--bs-accordion-border-radius:var(--bs-border-radius);--bs-accordion-inner-border-radius:calc(var(--bs-border-radius) - (var(--bs-border-width)));--bs-accordion-btn-padding-x:1.25rem;--bs-accordion-btn-padding-y:1rem;--bs-accordion-btn-color:var(--bs-body-color);--bs-accordion-btn-bg:var(--bs-accordion-bg);--bs-accordion-btn-icon:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23212529'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");--bs-accordion-btn-icon-width:1.25rem;--bs-accordion-btn-icon-transform:rotate(-180deg);--bs-accordion-btn-icon-transition:transform 0.2s ease-in-out;--bs-accordion-btn-active-icon:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23052c65'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");--bs-accordion-btn-focus-border-color:#86b7fe;--bs-accordion-btn-focus-box-shadow:0 0 0 0.25rem rgba(13, 110, 253, 0.25);--bs-accordion-body-padding-x:1.25rem;--bs-accordion-body-padding-y:1rem;--bs-accordion-active-color:var(--bs-primary-text-emphasis);--bs-accordion-active-bg:var(--bs-primary-bg-subtle)}.accordion-button{position:relative;display:flex;align-items:center;width:100%;padding:var(--bs-accordion-btn-padding-y) var(--bs-accordion-btn-padding-x);font-size:1rem;color:var(--bs-accordion-btn-color);text-align:left;background-color:var(--bs-accordion-btn-bg);border:0;border-radius:0;overflow-anchor:none;transition:var(--bs-accordion-transition)}@media (prefers-reduced-motion:reduce){.accordion-button{transition:none}}.accordion-button:not(.collapsed){color:var(--bs-accordion-active-color);background-color:var(--bs-accordion-active-bg);box-shadow:inset 0 calc(-1 * var(--bs-accordion-border-width)) 0 var(--bs-accordion-border-color)}.accordion-button:not(.collapsed)::after{background-image:var(--bs-accordion-btn-active-icon);transform:var(--bs-accordion-btn-icon-transform)}.accordion-button::after{flex-shrink:0;width:var(--bs-accordion-btn-icon-width);height:var(--bs-accordion-btn-icon-width);margin-left:auto;content:"";background-image:var(--bs-accordion-btn-icon);background-repeat:no-repeat;background-size:var(--bs-accordion-btn-icon-width);transition:var(--bs-accordion-btn-icon-transition)}@media (prefers-reduced-motion:reduce){.accordion-button::after{transition:none}}.accordion-button:hover{z-index:2}.accordion-button:focus{z-index:3;border-color:var(--bs-accordion-btn-focus-border-color);outline:0;box-shadow:var(--bs-accordion-btn-focus-box-shadow)}.accordion-header{margin-bottom:0}.accordion-item{color:var(--bs-accordion-color);background-color:var(--bs-accordion-bg);border:var(--bs-accordion-border-width) solid var(--bs-accordion-border-color)}.accordion-item:first-of-type{border-top-left-radius:var(--bs-accordion-border-radius);border-top-right-radius:var(--bs-accordion-border-radius)}.accordion-item:first-of-type .accordion-button{border-top-left-radius:var(--bs-accordion-inner-border-radius);border-top-right-radius:var(--bs-accordion-inner-border-radius)}.accordion-item:not(:first-of-type){border-top:0}.accordion-item:last-of-type{border-bottom-right-radius:var(--bs-accordion-border-radius);border-bottom-left-radius:var(--bs-accordion-border-radius)}.accordion-item:last-of-type .accordion-button.collapsed{border-bottom-right-radius:var(--bs-accordion-inner-border-radius);border-bottom-left-radius:var(--bs-accordion-inner-border-radius)}.accordion-item:last-of-type .accordion-collapse{border-bottom-right-radius:var(--bs-accordion-border-radius);border-bottom-left-radius:var(--bs-accordion-border-radius)}.accordion-body{padding:var(--bs-accordion-body-padding-y) var(--bs-accordion-body-padding-x)}.accordion-flush .accordion-collapse{border-width:0}.accordion-flush .accordion-item{border-right:0;border-left:0;border-radius:0}.accordion-flush .accordion-item:first-child{border-top:0}.accordion-flush .accordion-item:last-child{border-bottom:0}.accordion-flush .accordion-item .accordion-button,.accordion-flush .accordion-item .accordion-button.collapsed{border-radius:0}[data-bs-theme=dark] .accordion-button::after{--bs-accordion-btn-icon:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%236ea8fe'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");--bs-accordion-btn-active-icon:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%236ea8fe'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e")}.breadcrumb{--bs-breadcrumb-padding-x:0;--bs-breadcrumb-padding-y:0;--bs-breadcrumb-margin-bottom:1rem;--bs-breadcrumb-bg: ;--bs-breadcrumb-border-radius: ;--bs-breadcrumb-divider-color:var(--bs-secondary-color);--bs-breadcrumb-item-padding-x:0.5rem;--bs-breadcrumb-item-active-color:var(--bs-secondary-color);display:flex;flex-wrap:wrap;padding:var(--bs-breadcrumb-padding-y) var(--bs-breadcrumb-padding-x);margin-bottom:var(--bs-breadcrumb-margin-bottom);font-size:var(--bs-breadcrumb-font-size);list-style:none;background-color:var(--bs-breadcrumb-bg);border-radius:var(--bs-breadcrumb-border-radius)}.breadcrumb-item+.breadcrumb-item{padding-left:var(--bs-breadcrumb-item-padding-x)}.breadcrumb-item+.breadcrumb-item::before{float:left;padding-right:var(--bs-breadcrumb-item-padding-x);color:var(--bs-breadcrumb-divider-color);content:var(--bs-breadcrumb-divider, "/")}.breadcrumb-item.active{color:var(--bs-breadcrumb-item-active-color)}.pagination{--bs-pagination-padding-x:0.75rem;--bs-pagination-padding-y:0.375rem;--bs-pagination-font-size:1rem;--bs-pagination-color:var(--bs-link-color);--bs-pagination-bg:var(--bs-body-bg);--bs-pagination-border-width:var(--bs-border-width);--bs-pagination-border-color:var(--bs-border-color);--bs-pagination-border-radius:var(--bs-border-radius);--bs-pagination-hover-color:var(--bs-link-hover-color);--bs-pagination-hover-bg:var(--bs-tertiary-bg);--bs-pagination-hover-border-color:var(--bs-border-color);--bs-pagination-focus-color:var(--bs-link-hover-color);--bs-pagination-focus-bg:var(--bs-secondary-bg);--bs-pagination-focus-box-shadow:0 0 0 0.25rem rgba(13, 110, 253, 0.25);--bs-pagination-active-color:#fff;--bs-pagination-active-bg:#0d6efd;--bs-pagination-active-border-color:#0d6efd;--bs-pagination-disabled-color:var(--bs-secondary-color);--bs-pagination-disabled-bg:var(--bs-secondary-bg);--bs-pagination-disabled-border-color:var(--bs-border-color);display:flex;padding-left:0;list-style:none}.page-link{position:relative;display:block;padding:var(--bs-pagination-padding-y) var(--bs-pagination-padding-x);font-size:var(--bs-pagination-font-size);color:var(--bs-pagination-color);text-decoration:none;background-color:var(--bs-pagination-bg);border:var(--bs-pagination-border-width) solid var(--bs-pagination-border-color);transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out}@media (prefers-reduced-motion:reduce){.page-link{transition:none}}.page-link:hover{z-index:2;color:var(--bs-pagination-hover-color);background-color:var(--bs-pagination-hover-bg);border-color:var(--bs-pagination-hover-border-color)}.page-link:focus{z-index:3;color:var(--bs-pagination-focus-color);background-color:var(--bs-pagination-focus-bg);outline:0;box-shadow:var(--bs-pagination-focus-box-shadow)}.active>.page-link,.page-link.active{z-index:3;color:var(--bs-pagination-active-color);background-color:var(--bs-pagination-active-bg);border-color:var(--bs-pagination-active-border-color)}.disabled>.page-link,.page-link.disabled{color:var(--bs-pagination-disabled-color);pointer-events:none;background-color:var(--bs-pagination-disabled-bg);border-color:var(--bs-pagination-disabled-border-color)}.page-item:not(:first-child) .page-link{margin-left:calc(var(--bs-border-width) * -1)}.page-item:first-child .page-link{border-top-left-radius:var(--bs-pagination-border-radius);border-bottom-left-radius:var(--bs-pagination-border-radius)}.page-item:last-child .page-link{border-top-right-radius:var(--bs-pagination-border-radius);border-bottom-right-radius:var(--bs-pagination-border-radius)}.pagination-lg{--bs-pagination-padding-x:1.5rem;--bs-pagination-padding-y:0.75rem;--bs-pagination-font-size:1.25rem;--bs-pagination-border-radius:var(--bs-border-radius-lg)}.pagination-sm{--bs-pagination-padding-x:0.5rem;--bs-pagination-padding-y:0.25rem;--bs-pagination-font-size:0.875rem;--bs-pagination-border-radius:var(--bs-border-radius-sm)}.badge{--bs-badge-padding-x:0.65em;--bs-badge-padding-y:0.35em;--bs-badge-font-size:0.75em;--bs-badge-font-weight:700;--bs-badge-color:#fff;--bs-badge-border-radius:var(--bs-border-radius);display:inline-block;padding:var(--bs-badge-padding-y) var(--bs-badge-padding-x);font-size:var(--bs-badge-font-size);font-weight:var(--bs-badge-font-weight);line-height:1;color:var(--bs-badge-color);text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:var(--bs-badge-border-radius)}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.alert{--bs-alert-bg:transparent;--bs-alert-padding-x:1rem;--bs-alert-padding-y:1rem;--bs-alert-margin-bottom:1rem;--bs-alert-color:inherit;--bs-alert-border-color:transparent;--bs-alert-border:var(--bs-border-width) solid var(--bs-alert-border-color);--bs-alert-border-radius:var(--bs-border-radius);--bs-alert-link-color:inherit;position:relative;padding:var(--bs-alert-padding-y) var(--bs-alert-padding-x);margin-bottom:var(--bs-alert-margin-bottom);color:var(--bs-alert-color);background-color:var(--bs-alert-bg);border:var(--bs-alert-border);border-radius:var(--bs-alert-border-radius)}.alert-heading{color:inherit}.alert-link{font-weight:700;color:var(--bs-alert-link-color)}.alert-dismissible{padding-right:3rem}.alert-dismissible .btn-close{position:absolute;top:0;right:0;z-index:2;padding:1.25rem 1rem}.alert-primary{--bs-alert-color:var(--bs-primary-text-emphasis);--bs-alert-bg:var(--bs-primary-bg-subtle);--bs-alert-border-color:var(--bs-primary-border-subtle);--bs-alert-link-color:var(--bs-primary-text-emphasis)}.alert-secondary{--bs-alert-color:var(--bs-secondary-text-emphasis);--bs-alert-bg:var(--bs-secondary-bg-subtle);--bs-alert-border-color:var(--bs-secondary-border-subtle);--bs-alert-link-color:var(--bs-secondary-text-emphasis)}.alert-success{--bs-alert-color:var(--bs-success-text-emphasis);--bs-alert-bg:var(--bs-success-bg-subtle);--bs-alert-border-color:var(--bs-success-border-subtle);--bs-alert-link-color:var(--bs-success-text-emphasis)}.alert-info{--bs-alert-color:var(--bs-info-text-emphasis);--bs-alert-bg:var(--bs-info-bg-subtle);--bs-alert-border-color:var(--bs-info-border-subtle);--bs-alert-link-color:var(--bs-info-text-emphasis)}.alert-warning{--bs-alert-color:var(--bs-warning-text-emphasis);--bs-alert-bg:var(--bs-warning-bg-subtle);--bs-alert-border-color:var(--bs-warning-border-subtle);--bs-alert-link-color:var(--bs-warning-text-emphasis)}.alert-danger{--bs-alert-color:var(--bs-danger-text-emphasis);--bs-alert-bg:var(--bs-danger-bg-subtle);--bs-alert-border-color:var(--bs-danger-border-subtle);--bs-alert-link-color:var(--bs-danger-text-emphasis)}.alert-light{--bs-alert-color:var(--bs-light-text-emphasis);--bs-alert-bg:var(--bs-light-bg-subtle);--bs-alert-border-color:var(--bs-light-border-subtle);--bs-alert-link-color:var(--bs-light-text-emphasis)}.alert-dark{--bs-alert-color:var(--bs-dark-text-emphasis);--bs-alert-bg:var(--bs-dark-bg-subtle);--bs-alert-border-color:var(--bs-dark-border-subtle);--bs-alert-link-color:var(--bs-dark-text-emphasis)}@keyframes progress-bar-stripes{0%{background-position-x:1rem}}.progress,.progress-stacked{--bs-progress-height:1rem;--bs-progress-font-size:0.75rem;--bs-progress-bg:var(--bs-secondary-bg);--bs-progress-border-radius:var(--bs-border-radius);--bs-progress-box-shadow:var(--bs-box-shadow-inset);--bs-progress-bar-color:#fff;--bs-progress-bar-bg:#0d6efd;--bs-progress-bar-transition:width 0.6s ease;display:flex;height:var(--bs-progress-height);overflow:hidden;font-size:var(--bs-progress-font-size);background-color:var(--bs-progress-bg);border-radius:var(--bs-progress-border-radius)}.progress-bar{display:flex;flex-direction:column;justify-content:center;overflow:hidden;color:var(--bs-progress-bar-color);text-align:center;white-space:nowrap;background-color:var(--bs-progress-bar-bg);transition:var(--bs-progress-bar-transition)}@media (prefers-reduced-motion:reduce){.progress-bar{transition:none}}.progress-bar-striped{background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-size:var(--bs-progress-height) var(--bs-progress-height)}.progress-stacked>.progress{overflow:visible}.progress-stacked>.progress>.progress-bar{width:100%}.progress-bar-animated{animation:1s linear infinite progress-bar-stripes}@media (prefers-reduced-motion:reduce){.progress-bar-animated{animation:none}}.list-group{--bs-list-group-color:var(--bs-body-color);--bs-list-group-bg:var(--bs-body-bg);--bs-list-group-border-color:var(--bs-border-color);--bs-list-group-border-width:var(--bs-border-width);--bs-list-group-border-radius:var(--bs-border-radius);--bs-list-group-item-padding-x:1rem;--bs-list-group-item-padding-y:0.5rem;--bs-list-group-action-color:var(--bs-secondary-color);--bs-list-group-action-hover-color:var(--bs-emphasis-color);--bs-list-group-action-hover-bg:var(--bs-tertiary-bg);--bs-list-group-action-active-color:var(--bs-body-color);--bs-list-group-action-active-bg:var(--bs-secondary-bg);--bs-list-group-disabled-color:var(--bs-secondary-color);--bs-list-group-disabled-bg:var(--bs-body-bg);--bs-list-group-active-color:#fff;--bs-list-group-active-bg:#0d6efd;--bs-list-group-active-border-color:#0d6efd;display:flex;flex-direction:column;padding-left:0;margin-bottom:0;border-radius:var(--bs-list-group-border-radius)}.list-group-numbered{list-style-type:none;counter-reset:section}.list-group-numbered>.list-group-item::before{content:counters(section, ".") ". ";counter-increment:section}.list-group-item-action{width:100%;color:var(--bs-list-group-action-color);text-align:inherit}.list-group-item-action:focus,.list-group-item-action:hover{z-index:1;color:var(--bs-list-group-action-hover-color);text-decoration:none;background-color:var(--bs-list-group-action-hover-bg)}.list-group-item-action:active{color:var(--bs-list-group-action-active-color);background-color:var(--bs-list-group-action-active-bg)}.list-group-item{position:relative;display:block;padding:var(--bs-list-group-item-padding-y) var(--bs-list-group-item-padding-x);color:var(--bs-list-group-color);text-decoration:none;background-color:var(--bs-list-group-bg);border:var(--bs-list-group-border-width) solid var(--bs-list-group-border-color)}.list-group-item:first-child{border-top-left-radius:inherit;border-top-right-radius:inherit}.list-group-item:last-child{border-bottom-right-radius:inherit;border-bottom-left-radius:inherit}.list-group-item.disabled,.list-group-item:disabled{color:var(--bs-list-group-disabled-color);pointer-events:none;background-color:var(--bs-list-group-disabled-bg)}.list-group-item.active{z-index:2;color:var(--bs-list-group-active-color);background-color:var(--bs-list-group-active-bg);border-color:var(--bs-list-group-active-border-color)}.list-group-item+.list-group-item{border-top-width:0}.list-group-item+.list-group-item.active{margin-top:calc(-1 * var(--bs-list-group-border-width));border-top-width:var(--bs-list-group-border-width)}.list-group-horizontal{flex-direction:row}.list-group-horizontal>.list-group-item:first-child:not(:last-child){border-bottom-left-radius:var(--bs-list-group-border-radius);border-top-right-radius:0}.list-group-horizontal>.list-group-item:last-child:not(:first-child){border-top-right-radius:var(--bs-list-group-border-radius);border-bottom-left-radius:0}.list-group-horizontal>.list-group-item.active{margin-top:0}.list-group-horizontal>.list-group-item+.list-group-item{border-top-width:var(--bs-list-group-border-width);border-left-width:0}.list-group-horizontal>.list-group-item+.list-group-item.active{margin-left:calc(-1 * var(--bs-list-group-border-width));border-left-width:var(--bs-list-group-border-width)}@media (min-width:576px){.list-group-horizontal-sm{flex-direction:row}.list-group-horizontal-sm>.list-group-item:first-child:not(:last-child){border-bottom-left-radius:var(--bs-list-group-border-radius);border-top-right-radius:0}.list-group-horizontal-sm>.list-group-item:last-child:not(:first-child){border-top-right-radius:var(--bs-list-group-border-radius);border-bottom-left-radius:0}.list-group-horizontal-sm>.list-group-item.active{margin-top:0}.list-group-horizontal-sm>.list-group-item+.list-group-item{border-top-width:var(--bs-list-group-border-width);border-left-width:0}.list-group-horizontal-sm>.list-group-item+.list-group-item.active{margin-left:calc(-1 * var(--bs-list-group-border-width));border-left-width:var(--bs-list-group-border-width)}}@media (min-width:768px){.list-group-horizontal-md{flex-direction:row}.list-group-horizontal-md>.list-group-item:first-child:not(:last-child){border-bottom-left-radius:var(--bs-list-group-border-radius);border-top-right-radius:0}.list-group-horizontal-md>.list-group-item:last-child:not(:first-child){border-top-right-radius:var(--bs-list-group-border-radius);border-bottom-left-radius:0}.list-group-horizontal-md>.list-group-item.active{margin-top:0}.list-group-horizontal-md>.list-group-item+.list-group-item{border-top-width:var(--bs-list-group-border-width);border-left-width:0}.list-group-horizontal-md>.list-group-item+.list-group-item.active{margin-left:calc(-1 * var(--bs-list-group-border-width));border-left-width:var(--bs-list-group-border-width)}}@media (min-width:992px){.list-group-horizontal-lg{flex-direction:row}.list-group-horizontal-lg>.list-group-item:first-child:not(:last-child){border-bottom-left-radius:var(--bs-list-group-border-radius);border-top-right-radius:0}.list-group-horizontal-lg>.list-group-item:last-child:not(:first-child){border-top-right-radius:var(--bs-list-group-border-radius);border-bottom-left-radius:0}.list-group-horizontal-lg>.list-group-item.active{margin-top:0}.list-group-horizontal-lg>.list-group-item+.list-group-item{border-top-width:var(--bs-list-group-border-width);border-left-width:0}.list-group-horizontal-lg>.list-group-item+.list-group-item.active{margin-left:calc(-1 * var(--bs-list-group-border-width));border-left-width:var(--bs-list-group-border-width)}}@media (min-width:1200px){.list-group-horizontal-xl{flex-direction:row}.list-group-horizontal-xl>.list-group-item:first-child:not(:last-child){border-bottom-left-radius:var(--bs-list-group-border-radius);border-top-right-radius:0}.list-group-horizontal-xl>.list-group-item:last-child:not(:first-child){border-top-right-radius:var(--bs-list-group-border-radius);border-bottom-left-radius:0}.list-group-horizontal-xl>.list-group-item.active{margin-top:0}.list-group-horizontal-xl>.list-group-item+.list-group-item{border-top-width:var(--bs-list-group-border-width);border-left-width:0}.list-group-horizontal-xl>.list-group-item+.list-group-item.active{margin-left:calc(-1 * var(--bs-list-group-border-width));border-left-width:var(--bs-list-group-border-width)}}@media (min-width:1400px){.list-group-horizontal-xxl{flex-direction:row}.list-group-horizontal-xxl>.list-group-item:first-child:not(:last-child){border-bottom-left-radius:var(--bs-list-group-border-radius);border-top-right-radius:0}.list-group-horizontal-xxl>.list-group-item:last-child:not(:first-child){border-top-right-radius:var(--bs-list-group-border-radius);border-bottom-left-radius:0}.list-group-horizontal-xxl>.list-group-item.active{margin-top:0}.list-group-horizontal-xxl>.list-group-item+.list-group-item{border-top-width:var(--bs-list-group-border-width);border-left-width:0}.list-group-horizontal-xxl>.list-group-item+.list-group-item.active{margin-left:calc(-1 * var(--bs-list-group-border-width));border-left-width:var(--bs-list-group-border-width)}}.list-group-flush{border-radius:0}.list-group-flush>.list-group-item{border-width:0 0 var(--bs-list-group-border-width)}.list-group-flush>.list-group-item:last-child{border-bottom-width:0}.list-group-item-primary{--bs-list-group-color:var(--bs-primary-text-emphasis);--bs-list-group-bg:var(--bs-primary-bg-subtle);--bs-list-group-border-color:var(--bs-primary-border-subtle);--bs-list-group-action-hover-color:var(--bs-emphasis-color);--bs-list-group-action-hover-bg:var(--bs-primary-border-subtle);--bs-list-group-action-active-color:var(--bs-emphasis-color);--bs-list-group-action-active-bg:var(--bs-primary-border-subtle);--bs-list-group-active-color:var(--bs-primary-bg-subtle);--bs-list-group-active-bg:var(--bs-primary-text-emphasis);--bs-list-group-active-border-color:var(--bs-primary-text-emphasis)}.list-group-item-secondary{--bs-list-group-color:var(--bs-secondary-text-emphasis);--bs-list-group-bg:var(--bs-secondary-bg-subtle);--bs-list-group-border-color:var(--bs-secondary-border-subtle);--bs-list-group-action-hover-color:var(--bs-emphasis-color);--bs-list-group-action-hover-bg:var(--bs-secondary-border-subtle);--bs-list-group-action-active-color:var(--bs-emphasis-color);--bs-list-group-action-active-bg:var(--bs-secondary-border-subtle);--bs-list-group-active-color:var(--bs-secondary-bg-subtle);--bs-list-group-active-bg:var(--bs-secondary-text-emphasis);--bs-list-group-active-border-color:var(--bs-secondary-text-emphasis)}.list-group-item-success{--bs-list-group-color:var(--bs-success-text-emphasis);--bs-list-group-bg:var(--bs-success-bg-subtle);--bs-list-group-border-color:var(--bs-success-border-subtle);--bs-list-group-action-hover-color:var(--bs-emphasis-color);--bs-list-group-action-hover-bg:var(--bs-success-border-subtle);--bs-list-group-action-active-color:var(--bs-emphasis-color);--bs-list-group-action-active-bg:var(--bs-success-border-subtle);--bs-list-group-active-color:var(--bs-success-bg-subtle);--bs-list-group-active-bg:var(--bs-success-text-emphasis);--bs-list-group-active-border-color:var(--bs-success-text-emphasis)}.list-group-item-info{--bs-list-group-color:var(--bs-info-text-emphasis);--bs-list-group-bg:var(--bs-info-bg-subtle);--bs-list-group-border-color:var(--bs-info-border-subtle);--bs-list-group-action-hover-color:var(--bs-emphasis-color);--bs-list-group-action-hover-bg:var(--bs-info-border-subtle);--bs-list-group-action-active-color:var(--bs-emphasis-color);--bs-list-group-action-active-bg:var(--bs-info-border-subtle);--bs-list-group-active-color:var(--bs-info-bg-subtle);--bs-list-group-active-bg:var(--bs-info-text-emphasis);--bs-list-group-active-border-color:var(--bs-info-text-emphasis)}.list-group-item-warning{--bs-list-group-color:var(--bs-warning-text-emphasis);--bs-list-group-bg:var(--bs-warning-bg-subtle);--bs-list-group-border-color:var(--bs-warning-border-subtle);--bs-list-group-action-hover-color:var(--bs-emphasis-color);--bs-list-group-action-hover-bg:var(--bs-warning-border-subtle);--bs-list-group-action-active-color:var(--bs-emphasis-color);--bs-list-group-action-active-bg:var(--bs-warning-border-subtle);--bs-list-group-active-color:var(--bs-warning-bg-subtle);--bs-list-group-active-bg:var(--bs-warning-text-emphasis);--bs-list-group-active-border-color:var(--bs-warning-text-emphasis)}.list-group-item-danger{--bs-list-group-color:var(--bs-danger-text-emphasis);--bs-list-group-bg:var(--bs-danger-bg-subtle);--bs-list-group-border-color:var(--bs-danger-border-subtle);--bs-list-group-action-hover-color:var(--bs-emphasis-color);--bs-list-group-action-hover-bg:var(--bs-danger-border-subtle);--bs-list-group-action-active-color:var(--bs-emphasis-color);--bs-list-group-action-active-bg:var(--bs-danger-border-subtle);--bs-list-group-active-color:var(--bs-danger-bg-subtle);--bs-list-group-active-bg:var(--bs-danger-text-emphasis);--bs-list-group-active-border-color:var(--bs-danger-text-emphasis)}.list-group-item-light{--bs-list-group-color:var(--bs-light-text-emphasis);--bs-list-group-bg:var(--bs-light-bg-subtle);--bs-list-group-border-color:var(--bs-light-border-subtle);--bs-list-group-action-hover-color:var(--bs-emphasis-color);--bs-list-group-action-hover-bg:var(--bs-light-border-subtle);--bs-list-group-action-active-color:var(--bs-emphasis-color);--bs-list-group-action-active-bg:var(--bs-light-border-subtle);--bs-list-group-active-color:var(--bs-light-bg-subtle);--bs-list-group-active-bg:var(--bs-light-text-emphasis);--bs-list-group-active-border-color:var(--bs-light-text-emphasis)}.list-group-item-dark{--bs-list-group-color:var(--bs-dark-text-emphasis);--bs-list-group-bg:var(--bs-dark-bg-subtle);--bs-list-group-border-color:var(--bs-dark-border-subtle);--bs-list-group-action-hover-color:var(--bs-emphasis-color);--bs-list-group-action-hover-bg:var(--bs-dark-border-subtle);--bs-list-group-action-active-color:var(--bs-emphasis-color);--bs-list-group-action-active-bg:var(--bs-dark-border-subtle);--bs-list-group-active-color:var(--bs-dark-bg-subtle);--bs-list-group-active-bg:var(--bs-dark-text-emphasis);--bs-list-group-active-border-color:var(--bs-dark-text-emphasis)}.btn-close{--bs-btn-close-color:#000;--bs-btn-close-bg:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='M.293.293a1 1 0 0 1 1.414 0L8 6.586 14.293.293a1 1 0 1 1 1.414 1.414L9.414 8l6.293 6.293a1 1 0 0 1-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 0 1-1.414-1.414L6.586 8 .293 1.707a1 1 0 0 1 0-1.414z'/%3e%3c/svg%3e");--bs-btn-close-opacity:0.5;--bs-btn-close-hover-opacity:0.75;--bs-btn-close-focus-shadow:0 0 0 0.25rem rgba(13, 110, 253, 0.25);--bs-btn-close-focus-opacity:1;--bs-btn-close-disabled-opacity:0.25;--bs-btn-close-white-filter:invert(1) grayscale(100%) brightness(200%);box-sizing:content-box;width:1em;height:1em;padding:.25em .25em;color:var(--bs-btn-close-color);background:transparent var(--bs-btn-close-bg) center/1em auto no-repeat;border:0;border-radius:.375rem;opacity:var(--bs-btn-close-opacity)}.btn-close:hover{color:var(--bs-btn-close-color);text-decoration:none;opacity:var(--bs-btn-close-hover-opacity)}.btn-close:focus{outline:0;box-shadow:var(--bs-btn-close-focus-shadow);opacity:var(--bs-btn-close-focus-opacity)}.btn-close.disabled,.btn-close:disabled{pointer-events:none;-webkit-user-select:none;-moz-user-select:none;user-select:none;opacity:var(--bs-btn-close-disabled-opacity)}.btn-close-white{filter:var(--bs-btn-close-white-filter)}[data-bs-theme=dark] .btn-close{filter:var(--bs-btn-close-white-filter)}.toast{--bs-toast-zindex:1090;--bs-toast-padding-x:0.75rem;--bs-toast-padding-y:0.5rem;--bs-toast-spacing:1.5rem;--bs-toast-max-width:350px;--bs-toast-font-size:0.875rem;--bs-toast-color: ;--bs-toast-bg:rgba(var(--bs-body-bg-rgb), 0.85);--bs-toast-border-width:var(--bs-border-width);--bs-toast-border-color:var(--bs-border-color-translucent);--bs-toast-border-radius:var(--bs-border-radius);--bs-toast-box-shadow:var(--bs-box-shadow);--bs-toast-header-color:var(--bs-secondary-color);--bs-toast-header-bg:rgba(var(--bs-body-bg-rgb), 0.85);--bs-toast-header-border-color:var(--bs-border-color-translucent);width:var(--bs-toast-max-width);max-width:100%;font-size:var(--bs-toast-font-size);color:var(--bs-toast-color);pointer-events:auto;background-color:var(--bs-toast-bg);background-clip:padding-box;border:var(--bs-toast-border-width) solid var(--bs-toast-border-color);box-shadow:var(--bs-toast-box-shadow);border-radius:var(--bs-toast-border-radius)}.toast.showing{opacity:0}.toast:not(.show){display:none}.toast-container{--bs-toast-zindex:1090;position:absolute;z-index:var(--bs-toast-zindex);width:-webkit-max-content;width:-moz-max-content;width:max-content;max-width:100%;pointer-events:none}.toast-container>:not(:last-child){margin-bottom:var(--bs-toast-spacing)}.toast-header{display:flex;align-items:center;padding:var(--bs-toast-padding-y) var(--bs-toast-padding-x);color:var(--bs-toast-header-color);background-color:var(--bs-toast-header-bg);background-clip:padding-box;border-bottom:var(--bs-toast-border-width) solid var(--bs-toast-header-border-color);border-top-left-radius:calc(var(--bs-toast-border-radius) - var(--bs-toast-border-width));border-top-right-radius:calc(var(--bs-toast-border-radius) - var(--bs-toast-border-width))}.toast-header .btn-close{margin-right:calc(-.5 * var(--bs-toast-padding-x));margin-left:var(--bs-toast-padding-x)}.toast-body{padding:var(--bs-toast-padding-x);word-wrap:break-word}.modal{--bs-modal-zindex:1055;--bs-modal-width:500px;--bs-modal-padding:1rem;--bs-modal-margin:0.5rem;--bs-modal-color: ;--bs-modal-bg:var(--bs-body-bg);--bs-modal-border-color:var(--bs-border-color-translucent);--bs-modal-border-width:var(--bs-border-width);--bs-modal-border-radius:var(--bs-border-radius-lg);--bs-modal-box-shadow:var(--bs-box-shadow-sm);--bs-modal-inner-border-radius:calc(var(--bs-border-radius-lg) - (var(--bs-border-width)));--bs-modal-header-padding-x:1rem;--bs-modal-header-padding-y:1rem;--bs-modal-header-padding:1rem 1rem;--bs-modal-header-border-color:var(--bs-border-color);--bs-modal-header-border-width:var(--bs-border-width);--bs-modal-title-line-height:1.5;--bs-modal-footer-gap:0.5rem;--bs-modal-footer-bg: ;--bs-modal-footer-border-color:var(--bs-border-color);--bs-modal-footer-border-width:var(--bs-border-width);position:fixed;top:0;left:0;z-index:var(--bs-modal-zindex);display:none;width:100%;height:100%;overflow-x:hidden;overflow-y:auto;outline:0}.modal-dialog{position:relative;width:auto;margin:var(--bs-modal-margin);pointer-events:none}.modal.fade .modal-dialog{transition:transform .3s ease-out;transform:translate(0,-50px)}@media (prefers-reduced-motion:reduce){.modal.fade .modal-dialog{transition:none}}.modal.show .modal-dialog{transform:none}.modal.modal-static .modal-dialog{transform:scale(1.02)}.modal-dialog-scrollable{height:calc(100% - var(--bs-modal-margin) * 2)}.modal-dialog-scrollable .modal-content{max-height:100%;overflow:hidden}.modal-dialog-scrollable .modal-body{overflow-y:auto}.modal-dialog-centered{display:flex;align-items:center;min-height:calc(100% - var(--bs-modal-margin) * 2)}.modal-content{position:relative;display:flex;flex-direction:column;width:100%;color:var(--bs-modal-color);pointer-events:auto;background-color:var(--bs-modal-bg);background-clip:padding-box;border:var(--bs-modal-border-width) solid var(--bs-modal-border-color);border-radius:var(--bs-modal-border-radius);outline:0}.modal-backdrop{--bs-backdrop-zindex:1050;--bs-backdrop-bg:#000;--bs-backdrop-opacity:0.5;position:fixed;top:0;left:0;z-index:var(--bs-backdrop-zindex);width:100vw;height:100vh;background-color:var(--bs-backdrop-bg)}.modal-backdrop.fade{opacity:0}.modal-backdrop.show{opacity:var(--bs-backdrop-opacity)}.modal-header{display:flex;flex-shrink:0;align-items:center;justify-content:space-between;padding:var(--bs-modal-header-padding);border-bottom:var(--bs-modal-header-border-width) solid var(--bs-modal-header-border-color);border-top-left-radius:var(--bs-modal-inner-border-radius);border-top-right-radius:var(--bs-modal-inner-border-radius)}.modal-header .btn-close{padding:calc(var(--bs-modal-header-padding-y) * .5) calc(var(--bs-modal-header-padding-x) * .5);margin:calc(-.5 * var(--bs-modal-header-padding-y)) calc(-.5 * var(--bs-modal-header-padding-x)) calc(-.5 * var(--bs-modal-header-padding-y)) auto}.modal-title{margin-bottom:0;line-height:var(--bs-modal-title-line-height)}.modal-body{position:relative;flex:1 1 auto;padding:var(--bs-modal-padding)}.modal-footer{display:flex;flex-shrink:0;flex-wrap:wrap;align-items:center;justify-content:flex-end;padding:calc(var(--bs-modal-padding) - var(--bs-modal-footer-gap) * .5);background-color:var(--bs-modal-footer-bg);border-top:var(--bs-modal-footer-border-width) solid var(--bs-modal-footer-border-color);border-bottom-right-radius:var(--bs-modal-inner-border-radius);border-bottom-left-radius:var(--bs-modal-inner-border-radius)}.modal-footer>*{margin:calc(var(--bs-modal-footer-gap) * .5)}@media (min-width:576px){.modal{--bs-modal-margin:1.75rem;--bs-modal-box-shadow:var(--bs-box-shadow)}.modal-dialog{max-width:var(--bs-modal-width);margin-right:auto;margin-left:auto}.modal-sm{--bs-modal-width:300px}}@media (min-width:992px){.modal-lg,.modal-xl{--bs-modal-width:800px}}@media (min-width:1200px){.modal-xl{--bs-modal-width:1140px}}.modal-fullscreen{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen .modal-content{height:100%;border:0;border-radius:0}.modal-fullscreen .modal-footer,.modal-fullscreen .modal-header{border-radius:0}.modal-fullscreen .modal-body{overflow-y:auto}@media (max-width:575.98px){.modal-fullscreen-sm-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-sm-down .modal-content{height:100%;border:0;border-radius:0}.modal-fullscreen-sm-down .modal-footer,.modal-fullscreen-sm-down .modal-header{border-radius:0}.modal-fullscreen-sm-down .modal-body{overflow-y:auto}}@media (max-width:767.98px){.modal-fullscreen-md-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-md-down .modal-content{height:100%;border:0;border-radius:0}.modal-fullscreen-md-down .modal-footer,.modal-fullscreen-md-down .modal-header{border-radius:0}.modal-fullscreen-md-down .modal-body{overflow-y:auto}}@media (max-width:991.98px){.modal-fullscreen-lg-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-lg-down .modal-content{height:100%;border:0;border-radius:0}.modal-fullscreen-lg-down .modal-footer,.modal-fullscreen-lg-down .modal-header{border-radius:0}.modal-fullscreen-lg-down .modal-body{overflow-y:auto}}@media (max-width:1199.98px){.modal-fullscreen-xl-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-xl-down .modal-content{height:100%;border:0;border-radius:0}.modal-fullscreen-xl-down .modal-footer,.modal-fullscreen-xl-down .modal-header{border-radius:0}.modal-fullscreen-xl-down .modal-body{overflow-y:auto}}@media (max-width:1399.98px){.modal-fullscreen-xxl-down{width:100vw;max-width:none;height:100%;margin:0}.modal-fullscreen-xxl-down .modal-content{height:100%;border:0;border-radius:0}.modal-fullscreen-xxl-down .modal-footer,.modal-fullscreen-xxl-down .modal-header{border-radius:0}.modal-fullscreen-xxl-down .modal-body{overflow-y:auto}}.tooltip{--bs-tooltip-zindex:1080;--bs-tooltip-max-width:200px;--bs-tooltip-padding-x:0.5rem;--bs-tooltip-padding-y:0.25rem;--bs-tooltip-margin: ;--bs-tooltip-font-size:0.875rem;--bs-tooltip-color:var(--bs-body-bg);--bs-tooltip-bg:var(--bs-emphasis-color);--bs-tooltip-border-radius:var(--bs-border-radius);--bs-tooltip-opacity:0.9;--bs-tooltip-arrow-width:0.8rem;--bs-tooltip-arrow-height:0.4rem;z-index:var(--bs-tooltip-zindex);display:block;margin:var(--bs-tooltip-margin);font-family:var(--bs-font-sans-serif);font-style:normal;font-weight:400;line-height:1.5;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;white-space:normal;word-spacing:normal;line-break:auto;font-size:var(--bs-tooltip-font-size);word-wrap:break-word;opacity:0}.tooltip.show{opacity:var(--bs-tooltip-opacity)}.tooltip .tooltip-arrow{display:block;width:var(--bs-tooltip-arrow-width);height:var(--bs-tooltip-arrow-height)}.tooltip .tooltip-arrow::before{position:absolute;content:"";border-color:transparent;border-style:solid}.bs-tooltip-auto[data-popper-placement^=top] .tooltip-arrow,.bs-tooltip-top .tooltip-arrow{bottom:calc(-1 * var(--bs-tooltip-arrow-height))}.bs-tooltip-auto[data-popper-placement^=top] .tooltip-arrow::before,.bs-tooltip-top .tooltip-arrow::before{top:-1px;border-width:var(--bs-tooltip-arrow-height) calc(var(--bs-tooltip-arrow-width) * .5) 0;border-top-color:var(--bs-tooltip-bg)}.bs-tooltip-auto[data-popper-placement^=right] .tooltip-arrow,.bs-tooltip-end .tooltip-arrow{left:calc(-1 * var(--bs-tooltip-arrow-height));width:var(--bs-tooltip-arrow-height);height:var(--bs-tooltip-arrow-width)}.bs-tooltip-auto[data-popper-placement^=right] .tooltip-arrow::before,.bs-tooltip-end .tooltip-arrow::before{right:-1px;border-width:calc(var(--bs-tooltip-arrow-width) * .5) var(--bs-tooltip-arrow-height) calc(var(--bs-tooltip-arrow-width) * .5) 0;border-right-color:var(--bs-tooltip-bg)}.bs-tooltip-auto[data-popper-placement^=bottom] .tooltip-arrow,.bs-tooltip-bottom .tooltip-arrow{top:calc(-1 * var(--bs-tooltip-arrow-height))}.bs-tooltip-auto[data-popper-placement^=bottom] .tooltip-arrow::before,.bs-tooltip-bottom .tooltip-arrow::before{bottom:-1px;border-width:0 calc(var(--bs-tooltip-arrow-width) * .5) var(--bs-tooltip-arrow-height);border-bottom-color:var(--bs-tooltip-bg)}.bs-tooltip-auto[data-popper-placement^=left] .tooltip-arrow,.bs-tooltip-start .tooltip-arrow{right:calc(-1 * var(--bs-tooltip-arrow-height));width:var(--bs-tooltip-arrow-height);height:var(--bs-tooltip-arrow-width)}.bs-tooltip-auto[data-popper-placement^=left] .tooltip-arrow::before,.bs-tooltip-start .tooltip-arrow::before{left:-1px;border-width:calc(var(--bs-tooltip-arrow-width) * .5) 0 calc(var(--bs-tooltip-arrow-width) * .5) var(--bs-tooltip-arrow-height);border-left-color:var(--bs-tooltip-bg)}.tooltip-inner{max-width:var(--bs-tooltip-max-width);padding:var(--bs-tooltip-padding-y) var(--bs-tooltip-padding-x);color:var(--bs-tooltip-color);text-align:center;background-color:var(--bs-tooltip-bg);border-radius:var(--bs-tooltip-border-radius)}.popover{--bs-popover-zindex:1070;--bs-popover-max-width:276px;--bs-popover-font-size:0.875rem;--bs-popover-bg:var(--bs-body-bg);--bs-popover-border-width:var(--bs-border-width);--bs-popover-border-color:var(--bs-border-color-translucent);--bs-popover-border-radius:var(--bs-border-radius-lg);--bs-popover-inner-border-radius:calc(var(--bs-border-radius-lg) - var(--bs-border-width));--bs-popover-box-shadow:var(--bs-box-shadow);--bs-popover-header-padding-x:1rem;--bs-popover-header-padding-y:0.5rem;--bs-popover-header-font-size:1rem;--bs-popover-header-color:inherit;--bs-popover-header-bg:var(--bs-secondary-bg);--bs-popover-body-padding-x:1rem;--bs-popover-body-padding-y:1rem;--bs-popover-body-color:var(--bs-body-color);--bs-popover-arrow-width:1rem;--bs-popover-arrow-height:0.5rem;--bs-popover-arrow-border:var(--bs-popover-border-color);z-index:var(--bs-popover-zindex);display:block;max-width:var(--bs-popover-max-width);font-family:var(--bs-font-sans-serif);font-style:normal;font-weight:400;line-height:1.5;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;white-space:normal;word-spacing:normal;line-break:auto;font-size:var(--bs-popover-font-size);word-wrap:break-word;background-color:var(--bs-popover-bg);background-clip:padding-box;border:var(--bs-popover-border-width) solid var(--bs-popover-border-color);border-radius:var(--bs-popover-border-radius)}.popover .popover-arrow{display:block;width:var(--bs-popover-arrow-width);height:var(--bs-popover-arrow-height)}.popover .popover-arrow::after,.popover .popover-arrow::before{position:absolute;display:block;content:"";border-color:transparent;border-style:solid;border-width:0}.bs-popover-auto[data-popper-placement^=top]>.popover-arrow,.bs-popover-top>.popover-arrow{bottom:calc(-1 * (var(--bs-popover-arrow-height)) - var(--bs-popover-border-width))}.bs-popover-auto[data-popper-placement^=top]>.popover-arrow::after,.bs-popover-auto[data-popper-placement^=top]>.popover-arrow::before,.bs-popover-top>.popover-arrow::after,.bs-popover-top>.popover-arrow::before{border-width:var(--bs-popover-arrow-height) calc(var(--bs-popover-arrow-width) * .5) 0}.bs-popover-auto[data-popper-placement^=top]>.popover-arrow::before,.bs-popover-top>.popover-arrow::before{bottom:0;border-top-color:var(--bs-popover-arrow-border)}.bs-popover-auto[data-popper-placement^=top]>.popover-arrow::after,.bs-popover-top>.popover-arrow::after{bottom:var(--bs-popover-border-width);border-top-color:var(--bs-popover-bg)}.bs-popover-auto[data-popper-placement^=right]>.popover-arrow,.bs-popover-end>.popover-arrow{left:calc(-1 * (var(--bs-popover-arrow-height)) - var(--bs-popover-border-width));width:var(--bs-popover-arrow-height);height:var(--bs-popover-arrow-width)}.bs-popover-auto[data-popper-placement^=right]>.popover-arrow::after,.bs-popover-auto[data-popper-placement^=right]>.popover-arrow::before,.bs-popover-end>.popover-arrow::after,.bs-popover-end>.popover-arrow::before{border-width:calc(var(--bs-popover-arrow-width) * .5) var(--bs-popover-arrow-height) calc(var(--bs-popover-arrow-width) * .5) 0}.bs-popover-auto[data-popper-placement^=right]>.popover-arrow::before,.bs-popover-end>.popover-arrow::before{left:0;border-right-color:var(--bs-popover-arrow-border)}.bs-popover-auto[data-popper-placement^=right]>.popover-arrow::after,.bs-popover-end>.popover-arrow::after{left:var(--bs-popover-border-width);border-right-color:var(--bs-popover-bg)}.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow,.bs-popover-bottom>.popover-arrow{top:calc(-1 * (var(--bs-popover-arrow-height)) - var(--bs-popover-border-width))}.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow::after,.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow::before,.bs-popover-bottom>.popover-arrow::after,.bs-popover-bottom>.popover-arrow::before{border-width:0 calc(var(--bs-popover-arrow-width) * .5) var(--bs-popover-arrow-height)}.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow::before,.bs-popover-bottom>.popover-arrow::before{top:0;border-bottom-color:var(--bs-popover-arrow-border)}.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow::after,.bs-popover-bottom>.popover-arrow::after{top:var(--bs-popover-border-width);border-bottom-color:var(--bs-popover-bg)}.bs-popover-auto[data-popper-placement^=bottom] .popover-header::before,.bs-popover-bottom .popover-header::before{position:absolute;top:0;left:50%;display:block;width:var(--bs-popover-arrow-width);margin-left:calc(-.5 * var(--bs-popover-arrow-width));content:"";border-bottom:var(--bs-popover-border-width) solid var(--bs-popover-header-bg)}.bs-popover-auto[data-popper-placement^=left]>.popover-arrow,.bs-popover-start>.popover-arrow{right:calc(-1 * (var(--bs-popover-arrow-height)) - var(--bs-popover-border-width));width:var(--bs-popover-arrow-height);height:var(--bs-popover-arrow-width)}.bs-popover-auto[data-popper-placement^=left]>.popover-arrow::after,.bs-popover-auto[data-popper-placement^=left]>.popover-arrow::before,.bs-popover-start>.popover-arrow::after,.bs-popover-start>.popover-arrow::before{border-width:calc(var(--bs-popover-arrow-width) * .5) 0 calc(var(--bs-popover-arrow-width) * .5) var(--bs-popover-arrow-height)}.bs-popover-auto[data-popper-placement^=left]>.popover-arrow::before,.bs-popover-start>.popover-arrow::before{right:0;border-left-color:var(--bs-popover-arrow-border)}.bs-popover-auto[data-popper-placement^=left]>.popover-arrow::after,.bs-popover-start>.popover-arrow::after{right:var(--bs-popover-border-width);border-left-color:var(--bs-popover-bg)}.popover-header{padding:var(--bs-popover-header-padding-y) var(--bs-popover-header-padding-x);margin-bottom:0;font-size:var(--bs-popover-header-font-size);color:var(--bs-popover-header-color);background-color:var(--bs-popover-header-bg);border-bottom:var(--bs-popover-border-width) solid var(--bs-popover-border-color);border-top-left-radius:var(--bs-popover-inner-border-radius);border-top-right-radius:var(--bs-popover-inner-border-radius)}.popover-header:empty{display:none}.popover-body{padding:var(--bs-popover-body-padding-y) var(--bs-popover-body-padding-x);color:var(--bs-popover-body-color)}.carousel{position:relative}.carousel.pointer-event{touch-action:pan-y}.carousel-inner{position:relative;width:100%;overflow:hidden}.carousel-inner::after{display:block;clear:both;content:""}.carousel-item{position:relative;display:none;float:left;width:100%;margin-right:-100%;-webkit-backface-visibility:hidden;backface-visibility:hidden;transition:transform .6s ease-in-out}@media (prefers-reduced-motion:reduce){.carousel-item{transition:none}}.carousel-item-next,.carousel-item-prev,.carousel-item.active{display:block}.active.carousel-item-end,.carousel-item-next:not(.carousel-item-start){transform:translateX(100%)}.active.carousel-item-start,.carousel-item-prev:not(.carousel-item-end){transform:translateX(-100%)}.carousel-fade .carousel-item{opacity:0;transition-property:opacity;transform:none}.carousel-fade .carousel-item-next.carousel-item-start,.carousel-fade .carousel-item-prev.carousel-item-end,.carousel-fade .carousel-item.active{z-index:1;opacity:1}.carousel-fade .active.carousel-item-end,.carousel-fade .active.carousel-item-start{z-index:0;opacity:0;transition:opacity 0s .6s}@media (prefers-reduced-motion:reduce){.carousel-fade .active.carousel-item-end,.carousel-fade .active.carousel-item-start{transition:none}}.carousel-control-next,.carousel-control-prev{position:absolute;top:0;bottom:0;z-index:1;display:flex;align-items:center;justify-content:center;width:15%;padding:0;color:#fff;text-align:center;background:0 0;border:0;opacity:.5;transition:opacity .15s ease}@media (prefers-reduced-motion:reduce){.carousel-control-next,.carousel-control-prev{transition:none}}.carousel-control-next:focus,.carousel-control-next:hover,.carousel-control-prev:focus,.carousel-control-prev:hover{color:#fff;text-decoration:none;outline:0;opacity:.9}.carousel-control-prev{left:0}.carousel-control-next{right:0}.carousel-control-next-icon,.carousel-control-prev-icon{display:inline-block;width:2rem;height:2rem;background-repeat:no-repeat;background-position:50%;background-size:100% 100%}.carousel-control-prev-icon{background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z'/%3e%3c/svg%3e")}.carousel-control-next-icon{background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e")}.carousel-indicators{position:absolute;right:0;bottom:0;left:0;z-index:2;display:flex;justify-content:center;padding:0;margin-right:15%;margin-bottom:1rem;margin-left:15%}.carousel-indicators [data-bs-target]{box-sizing:content-box;flex:0 1 auto;width:30px;height:3px;padding:0;margin-right:3px;margin-left:3px;text-indent:-999px;cursor:pointer;background-color:#fff;background-clip:padding-box;border:0;border-top:10px solid transparent;border-bottom:10px solid transparent;opacity:.5;transition:opacity .6s ease}@media (prefers-reduced-motion:reduce){.carousel-indicators [data-bs-target]{transition:none}}.carousel-indicators .active{opacity:1}.carousel-caption{position:absolute;right:15%;bottom:1.25rem;left:15%;padding-top:1.25rem;padding-bottom:1.25rem;color:#fff;text-align:center}.carousel-dark .carousel-control-next-icon,.carousel-dark .carousel-control-prev-icon{filter:invert(1) grayscale(100)}.carousel-dark .carousel-indicators [data-bs-target]{background-color:#000}.carousel-dark .carousel-caption{color:#000}[data-bs-theme=dark] .carousel .carousel-control-next-icon,[data-bs-theme=dark] .carousel .carousel-control-prev-icon,[data-bs-theme=dark].carousel .carousel-control-next-icon,[data-bs-theme=dark].carousel .carousel-control-prev-icon{filter:invert(1) grayscale(100)}[data-bs-theme=dark] .carousel .carousel-indicators [data-bs-target],[data-bs-theme=dark].carousel .carousel-indicators [data-bs-target]{background-color:#000}[data-bs-theme=dark] .carousel .carousel-caption,[data-bs-theme=dark].carousel .carousel-caption{color:#000}.spinner-border,.spinner-grow{display:inline-block;width:var(--bs-spinner-width);height:var(--bs-spinner-height);vertical-align:var(--bs-spinner-vertical-align);border-radius:50%;animation:var(--bs-spinner-animation-speed) linear infinite var(--bs-spinner-animation-name)}@keyframes spinner-border{to{transform:rotate(360deg)}}.spinner-border{--bs-spinner-width:2rem;--bs-spinner-height:2rem;--bs-spinner-vertical-align:-0.125em;--bs-spinner-border-width:0.25em;--bs-spinner-animation-speed:0.75s;--bs-spinner-animation-name:spinner-border;border:var(--bs-spinner-border-width) solid currentcolor;border-right-color:transparent}.spinner-border-sm{--bs-spinner-width:1rem;--bs-spinner-height:1rem;--bs-spinner-border-width:0.2em}@keyframes spinner-grow{0%{transform:scale(0)}50%{opacity:1;transform:none}}.spinner-grow{--bs-spinner-width:2rem;--bs-spinner-height:2rem;--bs-spinner-vertical-align:-0.125em;--bs-spinner-animation-speed:0.75s;--bs-spinner-animation-name:spinner-grow;background-color:currentcolor;opacity:0}.spinner-grow-sm{--bs-spinner-width:1rem;--bs-spinner-height:1rem}@media (prefers-reduced-motion:reduce){.spinner-border,.spinner-grow{--bs-spinner-animation-speed:1.5s}}.offcanvas,.offcanvas-lg,.offcanvas-md,.offcanvas-sm,.offcanvas-xl,.offcanvas-xxl{--bs-offcanvas-zindex:1045;--bs-offcanvas-width:400px;--bs-offcanvas-height:30vh;--bs-offcanvas-padding-x:1rem;--bs-offcanvas-padding-y:1rem;--bs-offcanvas-color:var(--bs-body-color);--bs-offcanvas-bg:var(--bs-body-bg);--bs-offcanvas-border-width:var(--bs-border-width);--bs-offcanvas-border-color:var(--bs-border-color-translucent);--bs-offcanvas-box-shadow:var(--bs-box-shadow-sm);--bs-offcanvas-transition:transform 0.3s ease-in-out;--bs-offcanvas-title-line-height:1.5}@media (max-width:575.98px){.offcanvas-sm{position:fixed;bottom:0;z-index:var(--bs-offcanvas-zindex);display:flex;flex-direction:column;max-width:100%;color:var(--bs-offcanvas-color);visibility:hidden;background-color:var(--bs-offcanvas-bg);background-clip:padding-box;outline:0;transition:var(--bs-offcanvas-transition)}}@media (max-width:575.98px) and (prefers-reduced-motion:reduce){.offcanvas-sm{transition:none}}@media (max-width:575.98px){.offcanvas-sm.offcanvas-start{top:0;left:0;width:var(--bs-offcanvas-width);border-right:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(-100%)}.offcanvas-sm.offcanvas-end{top:0;right:0;width:var(--bs-offcanvas-width);border-left:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(100%)}.offcanvas-sm.offcanvas-top{top:0;right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-bottom:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(-100%)}.offcanvas-sm.offcanvas-bottom{right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-top:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(100%)}.offcanvas-sm.show:not(.hiding),.offcanvas-sm.showing{transform:none}.offcanvas-sm.hiding,.offcanvas-sm.show,.offcanvas-sm.showing{visibility:visible}}@media (min-width:576px){.offcanvas-sm{--bs-offcanvas-height:auto;--bs-offcanvas-border-width:0;background-color:transparent!important}.offcanvas-sm .offcanvas-header{display:none}.offcanvas-sm .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible;background-color:transparent!important}}@media (max-width:767.98px){.offcanvas-md{position:fixed;bottom:0;z-index:var(--bs-offcanvas-zindex);display:flex;flex-direction:column;max-width:100%;color:var(--bs-offcanvas-color);visibility:hidden;background-color:var(--bs-offcanvas-bg);background-clip:padding-box;outline:0;transition:var(--bs-offcanvas-transition)}}@media (max-width:767.98px) and (prefers-reduced-motion:reduce){.offcanvas-md{transition:none}}@media (max-width:767.98px){.offcanvas-md.offcanvas-start{top:0;left:0;width:var(--bs-offcanvas-width);border-right:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(-100%)}.offcanvas-md.offcanvas-end{top:0;right:0;width:var(--bs-offcanvas-width);border-left:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(100%)}.offcanvas-md.offcanvas-top{top:0;right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-bottom:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(-100%)}.offcanvas-md.offcanvas-bottom{right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-top:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(100%)}.offcanvas-md.show:not(.hiding),.offcanvas-md.showing{transform:none}.offcanvas-md.hiding,.offcanvas-md.show,.offcanvas-md.showing{visibility:visible}}@media (min-width:768px){.offcanvas-md{--bs-offcanvas-height:auto;--bs-offcanvas-border-width:0;background-color:transparent!important}.offcanvas-md .offcanvas-header{display:none}.offcanvas-md .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible;background-color:transparent!important}}@media (max-width:991.98px){.offcanvas-lg{position:fixed;bottom:0;z-index:var(--bs-offcanvas-zindex);display:flex;flex-direction:column;max-width:100%;color:var(--bs-offcanvas-color);visibility:hidden;background-color:var(--bs-offcanvas-bg);background-clip:padding-box;outline:0;transition:var(--bs-offcanvas-transition)}}@media (max-width:991.98px) and (prefers-reduced-motion:reduce){.offcanvas-lg{transition:none}}@media (max-width:991.98px){.offcanvas-lg.offcanvas-start{top:0;left:0;width:var(--bs-offcanvas-width);border-right:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(-100%)}.offcanvas-lg.offcanvas-end{top:0;right:0;width:var(--bs-offcanvas-width);border-left:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(100%)}.offcanvas-lg.offcanvas-top{top:0;right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-bottom:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(-100%)}.offcanvas-lg.offcanvas-bottom{right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-top:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(100%)}.offcanvas-lg.show:not(.hiding),.offcanvas-lg.showing{transform:none}.offcanvas-lg.hiding,.offcanvas-lg.show,.offcanvas-lg.showing{visibility:visible}}@media (min-width:992px){.offcanvas-lg{--bs-offcanvas-height:auto;--bs-offcanvas-border-width:0;background-color:transparent!important}.offcanvas-lg .offcanvas-header{display:none}.offcanvas-lg .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible;background-color:transparent!important}}@media (max-width:1199.98px){.offcanvas-xl{position:fixed;bottom:0;z-index:var(--bs-offcanvas-zindex);display:flex;flex-direction:column;max-width:100%;color:var(--bs-offcanvas-color);visibility:hidden;background-color:var(--bs-offcanvas-bg);background-clip:padding-box;outline:0;transition:var(--bs-offcanvas-transition)}}@media (max-width:1199.98px) and (prefers-reduced-motion:reduce){.offcanvas-xl{transition:none}}@media (max-width:1199.98px){.offcanvas-xl.offcanvas-start{top:0;left:0;width:var(--bs-offcanvas-width);border-right:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(-100%)}.offcanvas-xl.offcanvas-end{top:0;right:0;width:var(--bs-offcanvas-width);border-left:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(100%)}.offcanvas-xl.offcanvas-top{top:0;right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-bottom:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(-100%)}.offcanvas-xl.offcanvas-bottom{right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-top:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(100%)}.offcanvas-xl.show:not(.hiding),.offcanvas-xl.showing{transform:none}.offcanvas-xl.hiding,.offcanvas-xl.show,.offcanvas-xl.showing{visibility:visible}}@media (min-width:1200px){.offcanvas-xl{--bs-offcanvas-height:auto;--bs-offcanvas-border-width:0;background-color:transparent!important}.offcanvas-xl .offcanvas-header{display:none}.offcanvas-xl .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible;background-color:transparent!important}}@media (max-width:1399.98px){.offcanvas-xxl{position:fixed;bottom:0;z-index:var(--bs-offcanvas-zindex);display:flex;flex-direction:column;max-width:100%;color:var(--bs-offcanvas-color);visibility:hidden;background-color:var(--bs-offcanvas-bg);background-clip:padding-box;outline:0;transition:var(--bs-offcanvas-transition)}}@media (max-width:1399.98px) and (prefers-reduced-motion:reduce){.offcanvas-xxl{transition:none}}@media (max-width:1399.98px){.offcanvas-xxl.offcanvas-start{top:0;left:0;width:var(--bs-offcanvas-width);border-right:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(-100%)}.offcanvas-xxl.offcanvas-end{top:0;right:0;width:var(--bs-offcanvas-width);border-left:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(100%)}.offcanvas-xxl.offcanvas-top{top:0;right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-bottom:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(-100%)}.offcanvas-xxl.offcanvas-bottom{right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-top:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(100%)}.offcanvas-xxl.show:not(.hiding),.offcanvas-xxl.showing{transform:none}.offcanvas-xxl.hiding,.offcanvas-xxl.show,.offcanvas-xxl.showing{visibility:visible}}@media (min-width:1400px){.offcanvas-xxl{--bs-offcanvas-height:auto;--bs-offcanvas-border-width:0;background-color:transparent!important}.offcanvas-xxl .offcanvas-header{display:none}.offcanvas-xxl .offcanvas-body{display:flex;flex-grow:0;padding:0;overflow-y:visible;background-color:transparent!important}}.offcanvas{position:fixed;bottom:0;z-index:var(--bs-offcanvas-zindex);display:flex;flex-direction:column;max-width:100%;color:var(--bs-offcanvas-color);visibility:hidden;background-color:var(--bs-offcanvas-bg);background-clip:padding-box;outline:0;transition:var(--bs-offcanvas-transition)}@media (prefers-reduced-motion:reduce){.offcanvas{transition:none}}.offcanvas.offcanvas-start{top:0;left:0;width:var(--bs-offcanvas-width);border-right:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(-100%)}.offcanvas.offcanvas-end{top:0;right:0;width:var(--bs-offcanvas-width);border-left:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateX(100%)}.offcanvas.offcanvas-top{top:0;right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-bottom:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(-100%)}.offcanvas.offcanvas-bottom{right:0;left:0;height:var(--bs-offcanvas-height);max-height:100%;border-top:var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);transform:translateY(100%)}.offcanvas.show:not(.hiding),.offcanvas.showing{transform:none}.offcanvas.hiding,.offcanvas.show,.offcanvas.showing{visibility:visible}.offcanvas-backdrop{position:fixed;top:0;left:0;z-index:1040;width:100vw;height:100vh;background-color:#000}.offcanvas-backdrop.fade{opacity:0}.offcanvas-backdrop.show{opacity:.5}.offcanvas-header{display:flex;align-items:center;justify-content:space-between;padding:var(--bs-offcanvas-padding-y) var(--bs-offcanvas-padding-x)}.offcanvas-header .btn-close{padding:calc(var(--bs-offcanvas-padding-y) * .5) calc(var(--bs-offcanvas-padding-x) * .5);margin-top:calc(-.5 * var(--bs-offcanvas-padding-y));margin-right:calc(-.5 * var(--bs-offcanvas-padding-x));margin-bottom:calc(-.5 * var(--bs-offcanvas-padding-y))}.offcanvas-title{margin-bottom:0;line-height:var(--bs-offcanvas-title-line-height)}.offcanvas-body{flex-grow:1;padding:var(--bs-offcanvas-padding-y) var(--bs-offcanvas-padding-x);overflow-y:auto}.placeholder{display:inline-block;min-height:1em;vertical-align:middle;cursor:wait;background-color:currentcolor;opacity:.5}.placeholder.btn::before{display:inline-block;content:""}.placeholder-xs{min-height:.6em}.placeholder-sm{min-height:.8em}.placeholder-lg{min-height:1.2em}.placeholder-glow .placeholder{animation:placeholder-glow 2s ease-in-out infinite}@keyframes placeholder-glow{50%{opacity:.2}}.placeholder-wave{-webkit-mask-image:linear-gradient(130deg,#000 55%,rgba(0,0,0,0.8) 75%,#000 95%);mask-image:linear-gradient(130deg,#000 55%,rgba(0,0,0,0.8) 75%,#000 95%);-webkit-mask-size:200% 100%;mask-size:200% 100%;animation:placeholder-wave 2s linear infinite}@keyframes placeholder-wave{100%{-webkit-mask-position:-200% 0%;mask-position:-200% 0%}}.clearfix::after{display:block;clear:both;content:""}.text-bg-primary{color:#fff!important;background-color:RGBA(var(--bs-primary-rgb),var(--bs-bg-opacity,1))!important}.text-bg-secondary{color:#fff!important;background-color:RGBA(var(--bs-secondary-rgb),var(--bs-bg-opacity,1))!important}.text-bg-success{color:#fff!important;background-color:RGBA(var(--bs-success-rgb),var(--bs-bg-opacity,1))!important}.text-bg-info{color:#000!important;background-color:RGBA(var(--bs-info-rgb),var(--bs-bg-opacity,1))!important}.text-bg-warning{color:#000!important;background-color:RGBA(var(--bs-warning-rgb),var(--bs-bg-opacity,1))!important}.text-bg-danger{color:#fff!important;background-color:RGBA(var(--bs-danger-rgb),var(--bs-bg-opacity,1))!important}.text-bg-light{color:#000!important;background-color:RGBA(var(--bs-light-rgb),var(--bs-bg-opacity,1))!important}.text-bg-dark{color:#fff!important;background-color:RGBA(var(--bs-dark-rgb),var(--bs-bg-opacity,1))!important}.link-primary{color:RGBA(var(--bs-primary-rgb),var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(var(--bs-primary-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(var(--bs-primary-rgb),var(--bs-link-underline-opacity,1))!important}.link-primary:focus,.link-primary:hover{color:RGBA(10,88,202,var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(10,88,202,var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(10,88,202,var(--bs-link-underline-opacity,1))!important}.link-secondary{color:RGBA(var(--bs-secondary-rgb),var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(var(--bs-secondary-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(var(--bs-secondary-rgb),var(--bs-link-underline-opacity,1))!important}.link-secondary:focus,.link-secondary:hover{color:RGBA(86,94,100,var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(86,94,100,var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(86,94,100,var(--bs-link-underline-opacity,1))!important}.link-success{color:RGBA(var(--bs-success-rgb),var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(var(--bs-success-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(var(--bs-success-rgb),var(--bs-link-underline-opacity,1))!important}.link-success:focus,.link-success:hover{color:RGBA(20,108,67,var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(20,108,67,var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(20,108,67,var(--bs-link-underline-opacity,1))!important}.link-info{color:RGBA(var(--bs-info-rgb),var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(var(--bs-info-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(var(--bs-info-rgb),var(--bs-link-underline-opacity,1))!important}.link-info:focus,.link-info:hover{color:RGBA(61,213,243,var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(61,213,243,var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(61,213,243,var(--bs-link-underline-opacity,1))!important}.link-warning{color:RGBA(var(--bs-warning-rgb),var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(var(--bs-warning-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(var(--bs-warning-rgb),var(--bs-link-underline-opacity,1))!important}.link-warning:focus,.link-warning:hover{color:RGBA(255,205,57,var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(255,205,57,var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(255,205,57,var(--bs-link-underline-opacity,1))!important}.link-danger{color:RGBA(var(--bs-danger-rgb),var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(var(--bs-danger-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(var(--bs-danger-rgb),var(--bs-link-underline-opacity,1))!important}.link-danger:focus,.link-danger:hover{color:RGBA(176,42,55,var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(176,42,55,var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(176,42,55,var(--bs-link-underline-opacity,1))!important}.link-light{color:RGBA(var(--bs-light-rgb),var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(var(--bs-light-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(var(--bs-light-rgb),var(--bs-link-underline-opacity,1))!important}.link-light:focus,.link-light:hover{color:RGBA(249,250,251,var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(249,250,251,var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(249,250,251,var(--bs-link-underline-opacity,1))!important}.link-dark{color:RGBA(var(--bs-dark-rgb),var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(var(--bs-dark-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(var(--bs-dark-rgb),var(--bs-link-underline-opacity,1))!important}.link-dark:focus,.link-dark:hover{color:RGBA(26,30,33,var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(26,30,33,var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(26,30,33,var(--bs-link-underline-opacity,1))!important}.link-body-emphasis{color:RGBA(var(--bs-emphasis-color-rgb),var(--bs-link-opacity,1))!important;-webkit-text-decoration-color:RGBA(var(--bs-emphasis-color-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:RGBA(var(--bs-emphasis-color-rgb),var(--bs-link-underline-opacity,1))!important}.link-body-emphasis:focus,.link-body-emphasis:hover{color:RGBA(var(--bs-emphasis-color-rgb),var(--bs-link-opacity,.75))!important;-webkit-text-decoration-color:RGBA(var(--bs-emphasis-color-rgb),var(--bs-link-underline-opacity,0.75))!important;text-decoration-color:RGBA(var(--bs-emphasis-color-rgb),var(--bs-link-underline-opacity,0.75))!important}.focus-ring:focus{outline:0;box-shadow:var(--bs-focus-ring-x,0) var(--bs-focus-ring-y,0) var(--bs-focus-ring-blur,0) var(--bs-focus-ring-width) var(--bs-focus-ring-color)}.icon-link{display:inline-flex;gap:.375rem;align-items:center;-webkit-text-decoration-color:rgba(var(--bs-link-color-rgb),var(--bs-link-opacity,0.5));text-decoration-color:rgba(var(--bs-link-color-rgb),var(--bs-link-opacity,0.5));text-underline-offset:0.25em;-webkit-backface-visibility:hidden;backface-visibility:hidden}.icon-link>.bi{flex-shrink:0;width:1em;height:1em;fill:currentcolor;transition:.2s ease-in-out transform}@media (prefers-reduced-motion:reduce){.icon-link>.bi{transition:none}}.icon-link-hover:focus-visible>.bi,.icon-link-hover:hover>.bi{transform:var(--bs-icon-link-transform,translate3d(.25em,0,0))}.ratio{position:relative;width:100%}.ratio::before{display:block;padding-top:var(--bs-aspect-ratio);content:""}.ratio>*{position:absolute;top:0;left:0;width:100%;height:100%}.ratio-1x1{--bs-aspect-ratio:100%}.ratio-4x3{--bs-aspect-ratio:75%}.ratio-16x9{--bs-aspect-ratio:56.25%}.ratio-21x9{--bs-aspect-ratio:42.8571428571%}.fixed-top{position:fixed;top:0;right:0;left:0;z-index:1030}.fixed-bottom{position:fixed;right:0;bottom:0;left:0;z-index:1030}.sticky-top{position:-webkit-sticky;position:sticky;top:0;z-index:1020}.sticky-bottom{position:-webkit-sticky;position:sticky;bottom:0;z-index:1020}@media (min-width:576px){.sticky-sm-top{position:-webkit-sticky;position:sticky;top:0;z-index:1020}.sticky-sm-bottom{position:-webkit-sticky;position:sticky;bottom:0;z-index:1020}}@media (min-width:768px){.sticky-md-top{position:-webkit-sticky;position:sticky;top:0;z-index:1020}.sticky-md-bottom{position:-webkit-sticky;position:sticky;bottom:0;z-index:1020}}@media (min-width:992px){.sticky-lg-top{position:-webkit-sticky;position:sticky;top:0;z-index:1020}.sticky-lg-bottom{position:-webkit-sticky;position:sticky;bottom:0;z-index:1020}}@media (min-width:1200px){.sticky-xl-top{position:-webkit-sticky;position:sticky;top:0;z-index:1020}.sticky-xl-bottom{position:-webkit-sticky;position:sticky;bottom:0;z-index:1020}}@media (min-width:1400px){.sticky-xxl-top{position:-webkit-sticky;position:sticky;top:0;z-index:1020}.sticky-xxl-bottom{position:-webkit-sticky;position:sticky;bottom:0;z-index:1020}}.hstack{display:flex;flex-direction:row;align-items:center;align-self:stretch}.vstack{display:flex;flex:1 1 auto;flex-direction:column;align-self:stretch}.visually-hidden,.visually-hidden-focusable:not(:focus):not(:focus-within){width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}.visually-hidden-focusable:not(:focus):not(:focus-within):not(caption),.visually-hidden:not(caption){position:absolute!important}.stretched-link::after{position:absolute;top:0;right:0;bottom:0;left:0;z-index:1;content:""}.text-truncate{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.vr{display:inline-block;align-self:stretch;width:var(--bs-border-width);min-height:1em;background-color:currentcolor;opacity:.25}.align-baseline{vertical-align:baseline!important}.align-top{vertical-align:top!important}.align-middle{vertical-align:middle!important}.align-bottom{vertical-align:bottom!important}.align-text-bottom{vertical-align:text-bottom!important}.align-text-top{vertical-align:text-top!important}.float-start{float:left!important}.float-end{float:right!important}.float-none{float:none!important}.object-fit-contain{-o-object-fit:contain!important;object-fit:contain!important}.object-fit-cover{-o-object-fit:cover!important;object-fit:cover!important}.object-fit-fill{-o-object-fit:fill!important;object-fit:fill!important}.object-fit-scale{-o-object-fit:scale-down!important;object-fit:scale-down!important}.object-fit-none{-o-object-fit:none!important;object-fit:none!important}.opacity-0{opacity:0!important}.opacity-25{opacity:.25!important}.opacity-50{opacity:.5!important}.opacity-75{opacity:.75!important}.opacity-100{opacity:1!important}.overflow-auto{overflow:auto!important}.overflow-hidden{overflow:hidden!important}.overflow-visible{overflow:visible!important}.overflow-scroll{overflow:scroll!important}.overflow-x-auto{overflow-x:auto!important}.overflow-x-hidden{overflow-x:hidden!important}.overflow-x-visible{overflow-x:visible!important}.overflow-x-scroll{overflow-x:scroll!important}.overflow-y-auto{overflow-y:auto!important}.overflow-y-hidden{overflow-y:hidden!important}.overflow-y-visible{overflow-y:visible!important}.overflow-y-scroll{overflow-y:scroll!important}.d-inline{display:inline!important}.d-inline-block{display:inline-block!important}.d-block{display:block!important}.d-grid{display:grid!important}.d-inline-grid{display:inline-grid!important}.d-table{display:table!important}.d-table-row{display:table-row!important}.d-table-cell{display:table-cell!important}.d-flex{display:flex!important}.d-inline-flex{display:inline-flex!important}.d-none{display:none!important}.shadow{box-shadow:var(--bs-box-shadow)!important}.shadow-sm{box-shadow:var(--bs-box-shadow-sm)!important}.shadow-lg{box-shadow:var(--bs-box-shadow-lg)!important}.shadow-none{box-shadow:none!important}.focus-ring-primary{--bs-focus-ring-color:rgba(var(--bs-primary-rgb), var(--bs-focus-ring-opacity))}.focus-ring-secondary{--bs-focus-ring-color:rgba(var(--bs-secondary-rgb), var(--bs-focus-ring-opacity))}.focus-ring-success{--bs-focus-ring-color:rgba(var(--bs-success-rgb), var(--bs-focus-ring-opacity))}.focus-ring-info{--bs-focus-ring-color:rgba(var(--bs-info-rgb), var(--bs-focus-ring-opacity))}.focus-ring-warning{--bs-focus-ring-color:rgba(var(--bs-warning-rgb), var(--bs-focus-ring-opacity))}.focus-ring-danger{--bs-focus-ring-color:rgba(var(--bs-danger-rgb), var(--bs-focus-ring-opacity))}.focus-ring-light{--bs-focus-ring-color:rgba(var(--bs-light-rgb), var(--bs-focus-ring-opacity))}.focus-ring-dark{--bs-focus-ring-color:rgba(var(--bs-dark-rgb), var(--bs-focus-ring-opacity))}.position-static{position:static!important}.position-relative{position:relative!important}.position-absolute{position:absolute!important}.position-fixed{position:fixed!important}.position-sticky{position:-webkit-sticky!important;position:sticky!important}.top-0{top:0!important}.top-50{top:50%!important}.top-100{top:100%!important}.bottom-0{bottom:0!important}.bottom-50{bottom:50%!important}.bottom-100{bottom:100%!important}.start-0{left:0!important}.start-50{left:50%!important}.start-100{left:100%!important}.end-0{right:0!important}.end-50{right:50%!important}.end-100{right:100%!important}.translate-middle{transform:translate(-50%,-50%)!important}.translate-middle-x{transform:translateX(-50%)!important}.translate-middle-y{transform:translateY(-50%)!important}.border{border:var(--bs-border-width) var(--bs-border-style) var(--bs-border-color)!important}.border-0{border:0!important}.border-top{border-top:var(--bs-border-width) var(--bs-border-style) var(--bs-border-color)!important}.border-top-0{border-top:0!important}.border-end{border-right:var(--bs-border-width) var(--bs-border-style) var(--bs-border-color)!important}.border-end-0{border-right:0!important}.border-bottom{border-bottom:var(--bs-border-width) var(--bs-border-style) var(--bs-border-color)!important}.border-bottom-0{border-bottom:0!important}.border-start{border-left:var(--bs-border-width) var(--bs-border-style) var(--bs-border-color)!important}.border-start-0{border-left:0!important}.border-primary{--bs-border-opacity:1;border-color:rgba(var(--bs-primary-rgb),var(--bs-border-opacity))!important}.border-secondary{--bs-border-opacity:1;border-color:rgba(var(--bs-secondary-rgb),var(--bs-border-opacity))!important}.border-success{--bs-border-opacity:1;border-color:rgba(var(--bs-success-rgb),var(--bs-border-opacity))!important}.border-info{--bs-border-opacity:1;border-color:rgba(var(--bs-info-rgb),var(--bs-border-opacity))!important}.border-warning{--bs-border-opacity:1;border-color:rgba(var(--bs-warning-rgb),var(--bs-border-opacity))!important}.border-danger{--bs-border-opacity:1;border-color:rgba(var(--bs-danger-rgb),var(--bs-border-opacity))!important}.border-light{--bs-border-opacity:1;border-color:rgba(var(--bs-light-rgb),var(--bs-border-opacity))!important}.border-dark{--bs-border-opacity:1;border-color:rgba(var(--bs-dark-rgb),var(--bs-border-opacity))!important}.border-black{--bs-border-opacity:1;border-color:rgba(var(--bs-black-rgb),var(--bs-border-opacity))!important}.border-white{--bs-border-opacity:1;border-color:rgba(var(--bs-white-rgb),var(--bs-border-opacity))!important}.border-primary-subtle{border-color:var(--bs-primary-border-subtle)!important}.border-secondary-subtle{border-color:var(--bs-secondary-border-subtle)!important}.border-success-subtle{border-color:var(--bs-success-border-subtle)!important}.border-info-subtle{border-color:var(--bs-info-border-subtle)!important}.border-warning-subtle{border-color:var(--bs-warning-border-subtle)!important}.border-danger-subtle{border-color:var(--bs-danger-border-subtle)!important}.border-light-subtle{border-color:var(--bs-light-border-subtle)!important}.border-dark-subtle{border-color:var(--bs-dark-border-subtle)!important}.border-1{border-width:1px!important}.border-2{border-width:2px!important}.border-3{border-width:3px!important}.border-4{border-width:4px!important}.border-5{border-width:5px!important}.border-opacity-10{--bs-border-opacity:0.1}.border-opacity-25{--bs-border-opacity:0.25}.border-opacity-50{--bs-border-opacity:0.5}.border-opacity-75{--bs-border-opacity:0.75}.border-opacity-100{--bs-border-opacity:1}.w-25{width:25%!important}.w-50{width:50%!important}.w-75{width:75%!important}.w-100{width:100%!important}.w-auto{width:auto!important}.mw-100{max-width:100%!important}.vw-100{width:100vw!important}.min-vw-100{min-width:100vw!important}.h-25{height:25%!important}.h-50{height:50%!important}.h-75{height:75%!important}.h-100{height:100%!important}.h-auto{height:auto!important}.mh-100{max-height:100%!important}.vh-100{height:100vh!important}.min-vh-100{min-height:100vh!important}.flex-fill{flex:1 1 auto!important}.flex-row{flex-direction:row!important}.flex-column{flex-direction:column!important}.flex-row-reverse{flex-direction:row-reverse!important}.flex-column-reverse{flex-direction:column-reverse!important}.flex-grow-0{flex-grow:0!important}.flex-grow-1{flex-grow:1!important}.flex-shrink-0{flex-shrink:0!important}.flex-shrink-1{flex-shrink:1!important}.flex-wrap{flex-wrap:wrap!important}.flex-nowrap{flex-wrap:nowrap!important}.flex-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-start{justify-content:flex-start!important}.justify-content-end{justify-content:flex-end!important}.justify-content-center{justify-content:center!important}.justify-content-between{justify-content:space-between!important}.justify-content-around{justify-content:space-around!important}.justify-content-evenly{justify-content:space-evenly!important}.align-items-start{align-items:flex-start!important}.align-items-end{align-items:flex-end!important}.align-items-center{align-items:center!important}.align-items-baseline{align-items:baseline!important}.align-items-stretch{align-items:stretch!important}.align-content-start{align-content:flex-start!important}.align-content-end{align-content:flex-end!important}.align-content-center{align-content:center!important}.align-content-between{align-content:space-between!important}.align-content-around{align-content:space-around!important}.align-content-stretch{align-content:stretch!important}.align-self-auto{align-self:auto!important}.align-self-start{align-self:flex-start!important}.align-self-end{align-self:flex-end!important}.align-self-center{align-self:center!important}.align-self-baseline{align-self:baseline!important}.align-self-stretch{align-self:stretch!important}.order-first{order:-1!important}.order-0{order:0!important}.order-1{order:1!important}.order-2{order:2!important}.order-3{order:3!important}.order-4{order:4!important}.order-5{order:5!important}.order-last{order:6!important}.m-0{margin:0!important}.m-1{margin:.25rem!important}.m-2{margin:.5rem!important}.m-3{margin:1rem!important}.m-4{margin:1.5rem!important}.m-5{margin:3rem!important}.m-auto{margin:auto!important}.mx-0{margin-right:0!important;margin-left:0!important}.mx-1{margin-right:.25rem!important;margin-left:.25rem!important}.mx-2{margin-right:.5rem!important;margin-left:.5rem!important}.mx-3{margin-right:1rem!important;margin-left:1rem!important}.mx-4{margin-right:1.5rem!important;margin-left:1.5rem!important}.mx-5{margin-right:3rem!important;margin-left:3rem!important}.mx-auto{margin-right:auto!important;margin-left:auto!important}.my-0{margin-top:0!important;margin-bottom:0!important}.my-1{margin-top:.25rem!important;margin-bottom:.25rem!important}.my-2{margin-top:.5rem!important;margin-bottom:.5rem!important}.my-3{margin-top:1rem!important;margin-bottom:1rem!important}.my-4{margin-top:1.5rem!important;margin-bottom:1.5rem!important}.my-5{margin-top:3rem!important;margin-bottom:3rem!important}.my-auto{margin-top:auto!important;margin-bottom:auto!important}.mt-0{margin-top:0!important}.mt-1{margin-top:.25rem!important}.mt-2{margin-top:.5rem!important}.mt-3{margin-top:1rem!important}.mt-4{margin-top:1.5rem!important}.mt-5{margin-top:3rem!important}.mt-auto{margin-top:auto!important}.me-0{margin-right:0!important}.me-1{margin-right:.25rem!important}.me-2{margin-right:.5rem!important}.me-3{margin-right:1rem!important}.me-4{margin-right:1.5rem!important}.me-5{margin-right:3rem!important}.me-auto{margin-right:auto!important}.mb-0{margin-bottom:0!important}.mb-1{margin-bottom:.25rem!important}.mb-2{margin-bottom:.5rem!important}.mb-3{margin-bottom:1rem!important}.mb-4{margin-bottom:1.5rem!important}.mb-5{margin-bottom:3rem!important}.mb-auto{margin-bottom:auto!important}.ms-0{margin-left:0!important}.ms-1{margin-left:.25rem!important}.ms-2{margin-left:.5rem!important}.ms-3{margin-left:1rem!important}.ms-4{margin-left:1.5rem!important}.ms-5{margin-left:3rem!important}.ms-auto{margin-left:auto!important}.p-0{padding:0!important}.p-1{padding:.25rem!important}.p-2{padding:.5rem!important}.p-3{padding:1rem!important}.p-4{padding:1.5rem!important}.p-5{padding:3rem!important}.px-0{padding-right:0!important;padding-left:0!important}.px-1{padding-right:.25rem!important;padding-left:.25rem!important}.px-2{padding-right:.5rem!important;padding-left:.5rem!important}.px-3{padding-right:1rem!important;padding-left:1rem!important}.px-4{padding-right:1.5rem!important;padding-left:1.5rem!important}.px-5{padding-right:3rem!important;padding-left:3rem!important}.py-0{padding-top:0!important;padding-bottom:0!important}.py-1{padding-top:.25rem!important;padding-bottom:.25rem!important}.py-2{padding-top:.5rem!important;padding-bottom:.5rem!important}.py-3{padding-top:1rem!important;padding-bottom:1rem!important}.py-4{padding-top:1.5rem!important;padding-bottom:1.5rem!important}.py-5{padding-top:3rem!important;padding-bottom:3rem!important}.pt-0{padding-top:0!important}.pt-1{padding-top:.25rem!important}.pt-2{padding-top:.5rem!important}.pt-3{padding-top:1rem!important}.pt-4{padding-top:1.5rem!important}.pt-5{padding-top:3rem!important}.pe-0{padding-right:0!important}.pe-1{padding-right:.25rem!important}.pe-2{padding-right:.5rem!important}.pe-3{padding-right:1rem!important}.pe-4{padding-right:1.5rem!important}.pe-5{padding-right:3rem!important}.pb-0{padding-bottom:0!important}.pb-1{padding-bottom:.25rem!important}.pb-2{padding-bottom:.5rem!important}.pb-3{padding-bottom:1rem!important}.pb-4{padding-bottom:1.5rem!important}.pb-5{padding-bottom:3rem!important}.ps-0{padding-left:0!important}.ps-1{padding-left:.25rem!important}.ps-2{padding-left:.5rem!important}.ps-3{padding-left:1rem!important}.ps-4{padding-left:1.5rem!important}.ps-5{padding-left:3rem!important}.gap-0{gap:0!important}.gap-1{gap:.25rem!important}.gap-2{gap:.5rem!important}.gap-3{gap:1rem!important}.gap-4{gap:1.5rem!important}.gap-5{gap:3rem!important}.row-gap-0{row-gap:0!important}.row-gap-1{row-gap:.25rem!important}.row-gap-2{row-gap:.5rem!important}.row-gap-3{row-gap:1rem!important}.row-gap-4{row-gap:1.5rem!important}.row-gap-5{row-gap:3rem!important}.column-gap-0{-moz-column-gap:0!important;column-gap:0!important}.column-gap-1{-moz-column-gap:0.25rem!important;column-gap:.25rem!important}.column-gap-2{-moz-column-gap:0.5rem!important;column-gap:.5rem!important}.column-gap-3{-moz-column-gap:1rem!important;column-gap:1rem!important}.column-gap-4{-moz-column-gap:1.5rem!important;column-gap:1.5rem!important}.column-gap-5{-moz-column-gap:3rem!important;column-gap:3rem!important}.font-monospace{font-family:var(--bs-font-monospace)!important}.fs-1{font-size:calc(1.375rem + 1.5vw)!important}.fs-2{font-size:calc(1.325rem + .9vw)!important}.fs-3{font-size:calc(1.3rem + .6vw)!important}.fs-4{font-size:calc(1.275rem + .3vw)!important}.fs-5{font-size:1.25rem!important}.fs-6{font-size:1rem!important}.fst-italic{font-style:italic!important}.fst-normal{font-style:normal!important}.fw-lighter{font-weight:lighter!important}.fw-light{font-weight:300!important}.fw-normal{font-weight:400!important}.fw-medium{font-weight:500!important}.fw-semibold{font-weight:600!important}.fw-bold{font-weight:700!important}.fw-bolder{font-weight:bolder!important}.lh-1{line-height:1!important}.lh-sm{line-height:1.25!important}.lh-base{line-height:1.5!important}.lh-lg{line-height:2!important}.text-start{text-align:left!important}.text-end{text-align:right!important}.text-center{text-align:center!important}.text-decoration-none{text-decoration:none!important}.text-decoration-underline{text-decoration:underline!important}.text-decoration-line-through{text-decoration:line-through!important}.text-lowercase{text-transform:lowercase!important}.text-uppercase{text-transform:uppercase!important}.text-capitalize{text-transform:capitalize!important}.text-wrap{white-space:normal!important}.text-nowrap{white-space:nowrap!important}.text-break{word-wrap:break-word!important;word-break:break-word!important}.text-primary{--bs-text-opacity:1;color:rgba(var(--bs-primary-rgb),var(--bs-text-opacity))!important}.text-secondary{--bs-text-opacity:1;color:rgba(var(--bs-secondary-rgb),var(--bs-text-opacity))!important}.text-success{--bs-text-opacity:1;color:rgba(var(--bs-success-rgb),var(--bs-text-opacity))!important}.text-info{--bs-text-opacity:1;color:rgba(var(--bs-info-rgb),var(--bs-text-opacity))!important}.text-warning{--bs-text-opacity:1;color:rgba(var(--bs-warning-rgb),var(--bs-text-opacity))!important}.text-danger{--bs-text-opacity:1;color:rgba(var(--bs-danger-rgb),var(--bs-text-opacity))!important}.text-light{--bs-text-opacity:1;color:rgba(var(--bs-light-rgb),var(--bs-text-opacity))!important}.text-dark{--bs-text-opacity:1;color:rgba(var(--bs-dark-rgb),var(--bs-text-opacity))!important}.text-black{--bs-text-opacity:1;color:rgba(var(--bs-black-rgb),var(--bs-text-opacity))!important}.text-white{--bs-text-opacity:1;color:rgba(var(--bs-white-rgb),var(--bs-text-opacity))!important}.text-body{--bs-text-opacity:1;color:rgba(var(--bs-body-color-rgb),var(--bs-text-opacity))!important}.text-muted{--bs-text-opacity:1;color:var(--bs-secondary-color)!important}.text-black-50{--bs-text-opacity:1;color:rgba(0,0,0,.5)!important}.text-white-50{--bs-text-opacity:1;color:rgba(255,255,255,.5)!important}.text-body-secondary{--bs-text-opacity:1;color:var(--bs-secondary-color)!important}.text-body-tertiary{--bs-text-opacity:1;color:var(--bs-tertiary-color)!important}.text-body-emphasis{--bs-text-opacity:1;color:var(--bs-emphasis-color)!important}.text-reset{--bs-text-opacity:1;color:inherit!important}.text-opacity-25{--bs-text-opacity:0.25}.text-opacity-50{--bs-text-opacity:0.5}.text-opacity-75{--bs-text-opacity:0.75}.text-opacity-100{--bs-text-opacity:1}.text-primary-emphasis{color:var(--bs-primary-text-emphasis)!important}.text-secondary-emphasis{color:var(--bs-secondary-text-emphasis)!important}.text-success-emphasis{color:var(--bs-success-text-emphasis)!important}.text-info-emphasis{color:var(--bs-info-text-emphasis)!important}.text-warning-emphasis{color:var(--bs-warning-text-emphasis)!important}.text-danger-emphasis{color:var(--bs-danger-text-emphasis)!important}.text-light-emphasis{color:var(--bs-light-text-emphasis)!important}.text-dark-emphasis{color:var(--bs-dark-text-emphasis)!important}.link-opacity-10{--bs-link-opacity:0.1}.link-opacity-10-hover:hover{--bs-link-opacity:0.1}.link-opacity-25{--bs-link-opacity:0.25}.link-opacity-25-hover:hover{--bs-link-opacity:0.25}.link-opacity-50{--bs-link-opacity:0.5}.link-opacity-50-hover:hover{--bs-link-opacity:0.5}.link-opacity-75{--bs-link-opacity:0.75}.link-opacity-75-hover:hover{--bs-link-opacity:0.75}.link-opacity-100{--bs-link-opacity:1}.link-opacity-100-hover:hover{--bs-link-opacity:1}.link-offset-1{text-underline-offset:0.125em!important}.link-offset-1-hover:hover{text-underline-offset:0.125em!important}.link-offset-2{text-underline-offset:0.25em!important}.link-offset-2-hover:hover{text-underline-offset:0.25em!important}.link-offset-3{text-underline-offset:0.375em!important}.link-offset-3-hover:hover{text-underline-offset:0.375em!important}.link-underline-primary{--bs-link-underline-opacity:1;-webkit-text-decoration-color:rgba(var(--bs-primary-rgb),var(--bs-link-underline-opacity))!important;text-decoration-color:rgba(var(--bs-primary-rgb),var(--bs-link-underline-opacity))!important}.link-underline-secondary{--bs-link-underline-opacity:1;-webkit-text-decoration-color:rgba(var(--bs-secondary-rgb),var(--bs-link-underline-opacity))!important;text-decoration-color:rgba(var(--bs-secondary-rgb),var(--bs-link-underline-opacity))!important}.link-underline-success{--bs-link-underline-opacity:1;-webkit-text-decoration-color:rgba(var(--bs-success-rgb),var(--bs-link-underline-opacity))!important;text-decoration-color:rgba(var(--bs-success-rgb),var(--bs-link-underline-opacity))!important}.link-underline-info{--bs-link-underline-opacity:1;-webkit-text-decoration-color:rgba(var(--bs-info-rgb),var(--bs-link-underline-opacity))!important;text-decoration-color:rgba(var(--bs-info-rgb),var(--bs-link-underline-opacity))!important}.link-underline-warning{--bs-link-underline-opacity:1;-webkit-text-decoration-color:rgba(var(--bs-warning-rgb),var(--bs-link-underline-opacity))!important;text-decoration-color:rgba(var(--bs-warning-rgb),var(--bs-link-underline-opacity))!important}.link-underline-danger{--bs-link-underline-opacity:1;-webkit-text-decoration-color:rgba(var(--bs-danger-rgb),var(--bs-link-underline-opacity))!important;text-decoration-color:rgba(var(--bs-danger-rgb),var(--bs-link-underline-opacity))!important}.link-underline-light{--bs-link-underline-opacity:1;-webkit-text-decoration-color:rgba(var(--bs-light-rgb),var(--bs-link-underline-opacity))!important;text-decoration-color:rgba(var(--bs-light-rgb),var(--bs-link-underline-opacity))!important}.link-underline-dark{--bs-link-underline-opacity:1;-webkit-text-decoration-color:rgba(var(--bs-dark-rgb),var(--bs-link-underline-opacity))!important;text-decoration-color:rgba(var(--bs-dark-rgb),var(--bs-link-underline-opacity))!important}.link-underline{--bs-link-underline-opacity:1;-webkit-text-decoration-color:rgba(var(--bs-link-color-rgb),var(--bs-link-underline-opacity,1))!important;text-decoration-color:rgba(var(--bs-link-color-rgb),var(--bs-link-underline-opacity,1))!important}.link-underline-opacity-0{--bs-link-underline-opacity:0}.link-underline-opacity-0-hover:hover{--bs-link-underline-opacity:0}.link-underline-opacity-10{--bs-link-underline-opacity:0.1}.link-underline-opacity-10-hover:hover{--bs-link-underline-opacity:0.1}.link-underline-opacity-25{--bs-link-underline-opacity:0.25}.link-underline-opacity-25-hover:hover{--bs-link-underline-opacity:0.25}.link-underline-opacity-50{--bs-link-underline-opacity:0.5}.link-underline-opacity-50-hover:hover{--bs-link-underline-opacity:0.5}.link-underline-opacity-75{--bs-link-underline-opacity:0.75}.link-underline-opacity-75-hover:hover{--bs-link-underline-opacity:0.75}.link-underline-opacity-100{--bs-link-underline-opacity:1}.link-underline-opacity-100-hover:hover{--bs-link-underline-opacity:1}.bg-primary{--bs-bg-opacity:1;background-color:rgba(var(--bs-primary-rgb),var(--bs-bg-opacity))!important}.bg-secondary{--bs-bg-opacity:1;background-color:rgba(var(--bs-secondary-rgb),var(--bs-bg-opacity))!important}.bg-success{--bs-bg-opacity:1;background-color:rgba(var(--bs-success-rgb),var(--bs-bg-opacity))!important}.bg-info{--bs-bg-opacity:1;background-color:rgba(var(--bs-info-rgb),var(--bs-bg-opacity))!important}.bg-warning{--bs-bg-opacity:1;background-color:rgba(var(--bs-warning-rgb),var(--bs-bg-opacity))!important}.bg-danger{--bs-bg-opacity:1;background-color:rgba(var(--bs-danger-rgb),var(--bs-bg-opacity))!important}.bg-light{--bs-bg-opacity:1;background-color:rgba(var(--bs-light-rgb),var(--bs-bg-opacity))!important}.bg-dark{--bs-bg-opacity:1;background-color:rgba(var(--bs-dark-rgb),var(--bs-bg-opacity))!important}.bg-black{--bs-bg-opacity:1;background-color:rgba(var(--bs-black-rgb),var(--bs-bg-opacity))!important}.bg-white{--bs-bg-opacity:1;background-color:rgba(var(--bs-white-rgb),var(--bs-bg-opacity))!important}.bg-body{--bs-bg-opacity:1;background-color:rgba(var(--bs-body-bg-rgb),var(--bs-bg-opacity))!important}.bg-transparent{--bs-bg-opacity:1;background-color:transparent!important}.bg-body-secondary{--bs-bg-opacity:1;background-color:rgba(var(--bs-secondary-bg-rgb),var(--bs-bg-opacity))!important}.bg-body-tertiary{--bs-bg-opacity:1;background-color:rgba(var(--bs-tertiary-bg-rgb),var(--bs-bg-opacity))!important}.bg-opacity-10{--bs-bg-opacity:0.1}.bg-opacity-25{--bs-bg-opacity:0.25}.bg-opacity-50{--bs-bg-opacity:0.5}.bg-opacity-75{--bs-bg-opacity:0.75}.bg-opacity-100{--bs-bg-opacity:1}.bg-primary-subtle{background-color:var(--bs-primary-bg-subtle)!important}.bg-secondary-subtle{background-color:var(--bs-secondary-bg-subtle)!important}.bg-success-subtle{background-color:var(--bs-success-bg-subtle)!important}.bg-info-subtle{background-color:var(--bs-info-bg-subtle)!important}.bg-warning-subtle{background-color:var(--bs-warning-bg-subtle)!important}.bg-danger-subtle{background-color:var(--bs-danger-bg-subtle)!important}.bg-light-subtle{background-color:var(--bs-light-bg-subtle)!important}.bg-dark-subtle{background-color:var(--bs-dark-bg-subtle)!important}.bg-gradient{background-image:var(--bs-gradient)!important}.user-select-all{-webkit-user-select:all!important;-moz-user-select:all!important;user-select:all!important}.user-select-auto{-webkit-user-select:auto!important;-moz-user-select:auto!important;user-select:auto!important}.user-select-none{-webkit-user-select:none!important;-moz-user-select:none!important;user-select:none!important}.pe-none{pointer-events:none!important}.pe-auto{pointer-events:auto!important}.rounded{border-radius:var(--bs-border-radius)!important}.rounded-0{border-radius:0!important}.rounded-1{border-radius:var(--bs-border-radius-sm)!important}.rounded-2{border-radius:var(--bs-border-radius)!important}.rounded-3{border-radius:var(--bs-border-radius-lg)!important}.rounded-4{border-radius:var(--bs-border-radius-xl)!important}.rounded-5{border-radius:var(--bs-border-radius-xxl)!important}.rounded-circle{border-radius:50%!important}.rounded-pill{border-radius:var(--bs-border-radius-pill)!important}.rounded-top{border-top-left-radius:var(--bs-border-radius)!important;border-top-right-radius:var(--bs-border-radius)!important}.rounded-top-0{border-top-left-radius:0!important;border-top-right-radius:0!important}.rounded-top-1{border-top-left-radius:var(--bs-border-radius-sm)!important;border-top-right-radius:var(--bs-border-radius-sm)!important}.rounded-top-2{border-top-left-radius:var(--bs-border-radius)!important;border-top-right-radius:var(--bs-border-radius)!important}.rounded-top-3{border-top-left-radius:var(--bs-border-radius-lg)!important;border-top-right-radius:var(--bs-border-radius-lg)!important}.rounded-top-4{border-top-left-radius:var(--bs-border-radius-xl)!important;border-top-right-radius:var(--bs-border-radius-xl)!important}.rounded-top-5{border-top-left-radius:var(--bs-border-radius-xxl)!important;border-top-right-radius:var(--bs-border-radius-xxl)!important}.rounded-top-circle{border-top-left-radius:50%!important;border-top-right-radius:50%!important}.rounded-top-pill{border-top-left-radius:var(--bs-border-radius-pill)!important;border-top-right-radius:var(--bs-border-radius-pill)!important}.rounded-end{border-top-right-radius:var(--bs-border-radius)!important;border-bottom-right-radius:var(--bs-border-radius)!important}.rounded-end-0{border-top-right-radius:0!important;border-bottom-right-radius:0!important}.rounded-end-1{border-top-right-radius:var(--bs-border-radius-sm)!important;border-bottom-right-radius:var(--bs-border-radius-sm)!important}.rounded-end-2{border-top-right-radius:var(--bs-border-radius)!important;border-bottom-right-radius:var(--bs-border-radius)!important}.rounded-end-3{border-top-right-radius:var(--bs-border-radius-lg)!important;border-bottom-right-radius:var(--bs-border-radius-lg)!important}.rounded-end-4{border-top-right-radius:var(--bs-border-radius-xl)!important;border-bottom-right-radius:var(--bs-border-radius-xl)!important}.rounded-end-5{border-top-right-radius:var(--bs-border-radius-xxl)!important;border-bottom-right-radius:var(--bs-border-radius-xxl)!important}.rounded-end-circle{border-top-right-radius:50%!important;border-bottom-right-radius:50%!important}.rounded-end-pill{border-top-right-radius:var(--bs-border-radius-pill)!important;border-bottom-right-radius:var(--bs-border-radius-pill)!important}.rounded-bottom{border-bottom-right-radius:var(--bs-border-radius)!important;border-bottom-left-radius:var(--bs-border-radius)!important}.rounded-bottom-0{border-bottom-right-radius:0!important;border-bottom-left-radius:0!important}.rounded-bottom-1{border-bottom-right-radius:var(--bs-border-radius-sm)!important;border-bottom-left-radius:var(--bs-border-radius-sm)!important}.rounded-bottom-2{border-bottom-right-radius:var(--bs-border-radius)!important;border-bottom-left-radius:var(--bs-border-radius)!important}.rounded-bottom-3{border-bottom-right-radius:var(--bs-border-radius-lg)!important;border-bottom-left-radius:var(--bs-border-radius-lg)!important}.rounded-bottom-4{border-bottom-right-radius:var(--bs-border-radius-xl)!important;border-bottom-left-radius:var(--bs-border-radius-xl)!important}.rounded-bottom-5{border-bottom-right-radius:var(--bs-border-radius-xxl)!important;border-bottom-left-radius:var(--bs-border-radius-xxl)!important}.rounded-bottom-circle{border-bottom-right-radius:50%!important;border-bottom-left-radius:50%!important}.rounded-bottom-pill{border-bottom-right-radius:var(--bs-border-radius-pill)!important;border-bottom-left-radius:var(--bs-border-radius-pill)!important}.rounded-start{border-bottom-left-radius:var(--bs-border-radius)!important;border-top-left-radius:var(--bs-border-radius)!important}.rounded-start-0{border-bottom-left-radius:0!important;border-top-left-radius:0!important}.rounded-start-1{border-bottom-left-radius:var(--bs-border-radius-sm)!important;border-top-left-radius:var(--bs-border-radius-sm)!important}.rounded-start-2{border-bottom-left-radius:var(--bs-border-radius)!important;border-top-left-radius:var(--bs-border-radius)!important}.rounded-start-3{border-bottom-left-radius:var(--bs-border-radius-lg)!important;border-top-left-radius:var(--bs-border-radius-lg)!important}.rounded-start-4{border-bottom-left-radius:var(--bs-border-radius-xl)!important;border-top-left-radius:var(--bs-border-radius-xl)!important}.rounded-start-5{border-bottom-left-radius:var(--bs-border-radius-xxl)!important;border-top-left-radius:var(--bs-border-radius-xxl)!important}.rounded-start-circle{border-bottom-left-radius:50%!important;border-top-left-radius:50%!important}.rounded-start-pill{border-bottom-left-radius:var(--bs-border-radius-pill)!important;border-top-left-radius:var(--bs-border-radius-pill)!important}.visible{visibility:visible!important}.invisible{visibility:hidden!important}.z-n1{z-index:-1!important}.z-0{z-index:0!important}.z-1{z-index:1!important}.z-2{z-index:2!important}.z-3{z-index:3!important}@media (min-width:576px){.float-sm-start{float:left!important}.float-sm-end{float:right!important}.float-sm-none{float:none!important}.object-fit-sm-contain{-o-object-fit:contain!important;object-fit:contain!important}.object-fit-sm-cover{-o-object-fit:cover!important;object-fit:cover!important}.object-fit-sm-fill{-o-object-fit:fill!important;object-fit:fill!important}.object-fit-sm-scale{-o-object-fit:scale-down!important;object-fit:scale-down!important}.object-fit-sm-none{-o-object-fit:none!important;object-fit:none!important}.d-sm-inline{display:inline!important}.d-sm-inline-block{display:inline-block!important}.d-sm-block{display:block!important}.d-sm-grid{display:grid!important}.d-sm-inline-grid{display:inline-grid!important}.d-sm-table{display:table!important}.d-sm-table-row{display:table-row!important}.d-sm-table-cell{display:table-cell!important}.d-sm-flex{display:flex!important}.d-sm-inline-flex{display:inline-flex!important}.d-sm-none{display:none!important}.flex-sm-fill{flex:1 1 auto!important}.flex-sm-row{flex-direction:row!important}.flex-sm-column{flex-direction:column!important}.flex-sm-row-reverse{flex-direction:row-reverse!important}.flex-sm-column-reverse{flex-direction:column-reverse!important}.flex-sm-grow-0{flex-grow:0!important}.flex-sm-grow-1{flex-grow:1!important}.flex-sm-shrink-0{flex-shrink:0!important}.flex-sm-shrink-1{flex-shrink:1!important}.flex-sm-wrap{flex-wrap:wrap!important}.flex-sm-nowrap{flex-wrap:nowrap!important}.flex-sm-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-sm-start{justify-content:flex-start!important}.justify-content-sm-end{justify-content:flex-end!important}.justify-content-sm-center{justify-content:center!important}.justify-content-sm-between{justify-content:space-between!important}.justify-content-sm-around{justify-content:space-around!important}.justify-content-sm-evenly{justify-content:space-evenly!important}.align-items-sm-start{align-items:flex-start!important}.align-items-sm-end{align-items:flex-end!important}.align-items-sm-center{align-items:center!important}.align-items-sm-baseline{align-items:baseline!important}.align-items-sm-stretch{align-items:stretch!important}.align-content-sm-start{align-content:flex-start!important}.align-content-sm-end{align-content:flex-end!important}.align-content-sm-center{align-content:center!important}.align-content-sm-between{align-content:space-between!important}.align-content-sm-around{align-content:space-around!important}.align-content-sm-stretch{align-content:stretch!important}.align-self-sm-auto{align-self:auto!important}.align-self-sm-start{align-self:flex-start!important}.align-self-sm-end{align-self:flex-end!important}.align-self-sm-center{align-self:center!important}.align-self-sm-baseline{align-self:baseline!important}.align-self-sm-stretch{align-self:stretch!important}.order-sm-first{order:-1!important}.order-sm-0{order:0!important}.order-sm-1{order:1!important}.order-sm-2{order:2!important}.order-sm-3{order:3!important}.order-sm-4{order:4!important}.order-sm-5{order:5!important}.order-sm-last{order:6!important}.m-sm-0{margin:0!important}.m-sm-1{margin:.25rem!important}.m-sm-2{margin:.5rem!important}.m-sm-3{margin:1rem!important}.m-sm-4{margin:1.5rem!important}.m-sm-5{margin:3rem!important}.m-sm-auto{margin:auto!important}.mx-sm-0{margin-right:0!important;margin-left:0!important}.mx-sm-1{margin-right:.25rem!important;margin-left:.25rem!important}.mx-sm-2{margin-right:.5rem!important;margin-left:.5rem!important}.mx-sm-3{margin-right:1rem!important;margin-left:1rem!important}.mx-sm-4{margin-right:1.5rem!important;margin-left:1.5rem!important}.mx-sm-5{margin-right:3rem!important;margin-left:3rem!important}.mx-sm-auto{margin-right:auto!important;margin-left:auto!important}.my-sm-0{margin-top:0!important;margin-bottom:0!important}.my-sm-1{margin-top:.25rem!important;margin-bottom:.25rem!important}.my-sm-2{margin-top:.5rem!important;margin-bottom:.5rem!important}.my-sm-3{margin-top:1rem!important;margin-bottom:1rem!important}.my-sm-4{margin-top:1.5rem!important;margin-bottom:1.5rem!important}.my-sm-5{margin-top:3rem!important;margin-bottom:3rem!important}.my-sm-auto{margin-top:auto!important;margin-bottom:auto!important}.mt-sm-0{margin-top:0!important}.mt-sm-1{margin-top:.25rem!important}.mt-sm-2{margin-top:.5rem!important}.mt-sm-3{margin-top:1rem!important}.mt-sm-4{margin-top:1.5rem!important}.mt-sm-5{margin-top:3rem!important}.mt-sm-auto{margin-top:auto!important}.me-sm-0{margin-right:0!important}.me-sm-1{margin-right:.25rem!important}.me-sm-2{margin-right:.5rem!important}.me-sm-3{margin-right:1rem!important}.me-sm-4{margin-right:1.5rem!important}.me-sm-5{margin-right:3rem!important}.me-sm-auto{margin-right:auto!important}.mb-sm-0{margin-bottom:0!important}.mb-sm-1{margin-bottom:.25rem!important}.mb-sm-2{margin-bottom:.5rem!important}.mb-sm-3{margin-bottom:1rem!important}.mb-sm-4{margin-bottom:1.5rem!important}.mb-sm-5{margin-bottom:3rem!important}.mb-sm-auto{margin-bottom:auto!important}.ms-sm-0{margin-left:0!important}.ms-sm-1{margin-left:.25rem!important}.ms-sm-2{margin-left:.5rem!important}.ms-sm-3{margin-left:1rem!important}.ms-sm-4{margin-left:1.5rem!important}.ms-sm-5{margin-left:3rem!important}.ms-sm-auto{margin-left:auto!important}.p-sm-0{padding:0!important}.p-sm-1{padding:.25rem!important}.p-sm-2{padding:.5rem!important}.p-sm-3{padding:1rem!important}.p-sm-4{padding:1.5rem!important}.p-sm-5{padding:3rem!important}.px-sm-0{padding-right:0!important;padding-left:0!important}.px-sm-1{padding-right:.25rem!important;padding-left:.25rem!important}.px-sm-2{padding-right:.5rem!important;padding-left:.5rem!important}.px-sm-3{padding-right:1rem!important;padding-left:1rem!important}.px-sm-4{padding-right:1.5rem!important;padding-left:1.5rem!important}.px-sm-5{padding-right:3rem!important;padding-left:3rem!important}.py-sm-0{padding-top:0!important;padding-bottom:0!important}.py-sm-1{padding-top:.25rem!important;padding-bottom:.25rem!important}.py-sm-2{padding-top:.5rem!important;padding-bottom:.5rem!important}.py-sm-3{padding-top:1rem!important;padding-bottom:1rem!important}.py-sm-4{padding-top:1.5rem!important;padding-bottom:1.5rem!important}.py-sm-5{padding-top:3rem!important;padding-bottom:3rem!important}.pt-sm-0{padding-top:0!important}.pt-sm-1{padding-top:.25rem!important}.pt-sm-2{padding-top:.5rem!important}.pt-sm-3{padding-top:1rem!important}.pt-sm-4{padding-top:1.5rem!important}.pt-sm-5{padding-top:3rem!important}.pe-sm-0{padding-right:0!important}.pe-sm-1{padding-right:.25rem!important}.pe-sm-2{padding-right:.5rem!important}.pe-sm-3{padding-right:1rem!important}.pe-sm-4{padding-right:1.5rem!important}.pe-sm-5{padding-right:3rem!important}.pb-sm-0{padding-bottom:0!important}.pb-sm-1{padding-bottom:.25rem!important}.pb-sm-2{padding-bottom:.5rem!important}.pb-sm-3{padding-bottom:1rem!important}.pb-sm-4{padding-bottom:1.5rem!important}.pb-sm-5{padding-bottom:3rem!important}.ps-sm-0{padding-left:0!important}.ps-sm-1{padding-left:.25rem!important}.ps-sm-2{padding-left:.5rem!important}.ps-sm-3{padding-left:1rem!important}.ps-sm-4{padding-left:1.5rem!important}.ps-sm-5{padding-left:3rem!important}.gap-sm-0{gap:0!important}.gap-sm-1{gap:.25rem!important}.gap-sm-2{gap:.5rem!important}.gap-sm-3{gap:1rem!important}.gap-sm-4{gap:1.5rem!important}.gap-sm-5{gap:3rem!important}.row-gap-sm-0{row-gap:0!important}.row-gap-sm-1{row-gap:.25rem!important}.row-gap-sm-2{row-gap:.5rem!important}.row-gap-sm-3{row-gap:1rem!important}.row-gap-sm-4{row-gap:1.5rem!important}.row-gap-sm-5{row-gap:3rem!important}.column-gap-sm-0{-moz-column-gap:0!important;column-gap:0!important}.column-gap-sm-1{-moz-column-gap:0.25rem!important;column-gap:.25rem!important}.column-gap-sm-2{-moz-column-gap:0.5rem!important;column-gap:.5rem!important}.column-gap-sm-3{-moz-column-gap:1rem!important;column-gap:1rem!important}.column-gap-sm-4{-moz-column-gap:1.5rem!important;column-gap:1.5rem!important}.column-gap-sm-5{-moz-column-gap:3rem!important;column-gap:3rem!important}.text-sm-start{text-align:left!important}.text-sm-end{text-align:right!important}.text-sm-center{text-align:center!important}}@media (min-width:768px){.float-md-start{float:left!important}.float-md-end{float:right!important}.float-md-none{float:none!important}.object-fit-md-contain{-o-object-fit:contain!important;object-fit:contain!important}.object-fit-md-cover{-o-object-fit:cover!important;object-fit:cover!important}.object-fit-md-fill{-o-object-fit:fill!important;object-fit:fill!important}.object-fit-md-scale{-o-object-fit:scale-down!important;object-fit:scale-down!important}.object-fit-md-none{-o-object-fit:none!important;object-fit:none!important}.d-md-inline{display:inline!important}.d-md-inline-block{display:inline-block!important}.d-md-block{display:block!important}.d-md-grid{display:grid!important}.d-md-inline-grid{display:inline-grid!important}.d-md-table{display:table!important}.d-md-table-row{display:table-row!important}.d-md-table-cell{display:table-cell!important}.d-md-flex{display:flex!important}.d-md-inline-flex{display:inline-flex!important}.d-md-none{display:none!important}.flex-md-fill{flex:1 1 auto!important}.flex-md-row{flex-direction:row!important}.flex-md-column{flex-direction:column!important}.flex-md-row-reverse{flex-direction:row-reverse!important}.flex-md-column-reverse{flex-direction:column-reverse!important}.flex-md-grow-0{flex-grow:0!important}.flex-md-grow-1{flex-grow:1!important}.flex-md-shrink-0{flex-shrink:0!important}.flex-md-shrink-1{flex-shrink:1!important}.flex-md-wrap{flex-wrap:wrap!important}.flex-md-nowrap{flex-wrap:nowrap!important}.flex-md-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-md-start{justify-content:flex-start!important}.justify-content-md-end{justify-content:flex-end!important}.justify-content-md-center{justify-content:center!important}.justify-content-md-between{justify-content:space-between!important}.justify-content-md-around{justify-content:space-around!important}.justify-content-md-evenly{justify-content:space-evenly!important}.align-items-md-start{align-items:flex-start!important}.align-items-md-end{align-items:flex-end!important}.align-items-md-center{align-items:center!important}.align-items-md-baseline{align-items:baseline!important}.align-items-md-stretch{align-items:stretch!important}.align-content-md-start{align-content:flex-start!important}.align-content-md-end{align-content:flex-end!important}.align-content-md-center{align-content:center!important}.align-content-md-between{align-content:space-between!important}.align-content-md-around{align-content:space-around!important}.align-content-md-stretch{align-content:stretch!important}.align-self-md-auto{align-self:auto!important}.align-self-md-start{align-self:flex-start!important}.align-self-md-end{align-self:flex-end!important}.align-self-md-center{align-self:center!important}.align-self-md-baseline{align-self:baseline!important}.align-self-md-stretch{align-self:stretch!important}.order-md-first{order:-1!important}.order-md-0{order:0!important}.order-md-1{order:1!important}.order-md-2{order:2!important}.order-md-3{order:3!important}.order-md-4{order:4!important}.order-md-5{order:5!important}.order-md-last{order:6!important}.m-md-0{margin:0!important}.m-md-1{margin:.25rem!important}.m-md-2{margin:.5rem!important}.m-md-3{margin:1rem!important}.m-md-4{margin:1.5rem!important}.m-md-5{margin:3rem!important}.m-md-auto{margin:auto!important}.mx-md-0{margin-right:0!important;margin-left:0!important}.mx-md-1{margin-right:.25rem!important;margin-left:.25rem!important}.mx-md-2{margin-right:.5rem!important;margin-left:.5rem!important}.mx-md-3{margin-right:1rem!important;margin-left:1rem!important}.mx-md-4{margin-right:1.5rem!important;margin-left:1.5rem!important}.mx-md-5{margin-right:3rem!important;margin-left:3rem!important}.mx-md-auto{margin-right:auto!important;margin-left:auto!important}.my-md-0{margin-top:0!important;margin-bottom:0!important}.my-md-1{margin-top:.25rem!important;margin-bottom:.25rem!important}.my-md-2{margin-top:.5rem!important;margin-bottom:.5rem!important}.my-md-3{margin-top:1rem!important;margin-bottom:1rem!important}.my-md-4{margin-top:1.5rem!important;margin-bottom:1.5rem!important}.my-md-5{margin-top:3rem!important;margin-bottom:3rem!important}.my-md-auto{margin-top:auto!important;margin-bottom:auto!important}.mt-md-0{margin-top:0!important}.mt-md-1{margin-top:.25rem!important}.mt-md-2{margin-top:.5rem!important}.mt-md-3{margin-top:1rem!important}.mt-md-4{margin-top:1.5rem!important}.mt-md-5{margin-top:3rem!important}.mt-md-auto{margin-top:auto!important}.me-md-0{margin-right:0!important}.me-md-1{margin-right:.25rem!important}.me-md-2{margin-right:.5rem!important}.me-md-3{margin-right:1rem!important}.me-md-4{margin-right:1.5rem!important}.me-md-5{margin-right:3rem!important}.me-md-auto{margin-right:auto!important}.mb-md-0{margin-bottom:0!important}.mb-md-1{margin-bottom:.25rem!important}.mb-md-2{margin-bottom:.5rem!important}.mb-md-3{margin-bottom:1rem!important}.mb-md-4{margin-bottom:1.5rem!important}.mb-md-5{margin-bottom:3rem!important}.mb-md-auto{margin-bottom:auto!important}.ms-md-0{margin-left:0!important}.ms-md-1{margin-left:.25rem!important}.ms-md-2{margin-left:.5rem!important}.ms-md-3{margin-left:1rem!important}.ms-md-4{margin-left:1.5rem!important}.ms-md-5{margin-left:3rem!important}.ms-md-auto{margin-left:auto!important}.p-md-0{padding:0!important}.p-md-1{padding:.25rem!important}.p-md-2{padding:.5rem!important}.p-md-3{padding:1rem!important}.p-md-4{padding:1.5rem!important}.p-md-5{padding:3rem!important}.px-md-0{padding-right:0!important;padding-left:0!important}.px-md-1{padding-right:.25rem!important;padding-left:.25rem!important}.px-md-2{padding-right:.5rem!important;padding-left:.5rem!important}.px-md-3{padding-right:1rem!important;padding-left:1rem!important}.px-md-4{padding-right:1.5rem!important;padding-left:1.5rem!important}.px-md-5{padding-right:3rem!important;padding-left:3rem!important}.py-md-0{padding-top:0!important;padding-bottom:0!important}.py-md-1{padding-top:.25rem!important;padding-bottom:.25rem!important}.py-md-2{padding-top:.5rem!important;padding-bottom:.5rem!important}.py-md-3{padding-top:1rem!important;padding-bottom:1rem!important}.py-md-4{padding-top:1.5rem!important;padding-bottom:1.5rem!important}.py-md-5{padding-top:3rem!important;padding-bottom:3rem!important}.pt-md-0{padding-top:0!important}.pt-md-1{padding-top:.25rem!important}.pt-md-2{padding-top:.5rem!important}.pt-md-3{padding-top:1rem!important}.pt-md-4{padding-top:1.5rem!important}.pt-md-5{padding-top:3rem!important}.pe-md-0{padding-right:0!important}.pe-md-1{padding-right:.25rem!important}.pe-md-2{padding-right:.5rem!important}.pe-md-3{padding-right:1rem!important}.pe-md-4{padding-right:1.5rem!important}.pe-md-5{padding-right:3rem!important}.pb-md-0{padding-bottom:0!important}.pb-md-1{padding-bottom:.25rem!important}.pb-md-2{padding-bottom:.5rem!important}.pb-md-3{padding-bottom:1rem!important}.pb-md-4{padding-bottom:1.5rem!important}.pb-md-5{padding-bottom:3rem!important}.ps-md-0{padding-left:0!important}.ps-md-1{padding-left:.25rem!important}.ps-md-2{padding-left:.5rem!important}.ps-md-3{padding-left:1rem!important}.ps-md-4{padding-left:1.5rem!important}.ps-md-5{padding-left:3rem!important}.gap-md-0{gap:0!important}.gap-md-1{gap:.25rem!important}.gap-md-2{gap:.5rem!important}.gap-md-3{gap:1rem!important}.gap-md-4{gap:1.5rem!important}.gap-md-5{gap:3rem!important}.row-gap-md-0{row-gap:0!important}.row-gap-md-1{row-gap:.25rem!important}.row-gap-md-2{row-gap:.5rem!important}.row-gap-md-3{row-gap:1rem!important}.row-gap-md-4{row-gap:1.5rem!important}.row-gap-md-5{row-gap:3rem!important}.column-gap-md-0{-moz-column-gap:0!important;column-gap:0!important}.column-gap-md-1{-moz-column-gap:0.25rem!important;column-gap:.25rem!important}.column-gap-md-2{-moz-column-gap:0.5rem!important;column-gap:.5rem!important}.column-gap-md-3{-moz-column-gap:1rem!important;column-gap:1rem!important}.column-gap-md-4{-moz-column-gap:1.5rem!important;column-gap:1.5rem!important}.column-gap-md-5{-moz-column-gap:3rem!important;column-gap:3rem!important}.text-md-start{text-align:left!important}.text-md-end{text-align:right!important}.text-md-center{text-align:center!important}}@media (min-width:992px){.float-lg-start{float:left!important}.float-lg-end{float:right!important}.float-lg-none{float:none!important}.object-fit-lg-contain{-o-object-fit:contain!important;object-fit:contain!important}.object-fit-lg-cover{-o-object-fit:cover!important;object-fit:cover!important}.object-fit-lg-fill{-o-object-fit:fill!important;object-fit:fill!important}.object-fit-lg-scale{-o-object-fit:scale-down!important;object-fit:scale-down!important}.object-fit-lg-none{-o-object-fit:none!important;object-fit:none!important}.d-lg-inline{display:inline!important}.d-lg-inline-block{display:inline-block!important}.d-lg-block{display:block!important}.d-lg-grid{display:grid!important}.d-lg-inline-grid{display:inline-grid!important}.d-lg-table{display:table!important}.d-lg-table-row{display:table-row!important}.d-lg-table-cell{display:table-cell!important}.d-lg-flex{display:flex!important}.d-lg-inline-flex{display:inline-flex!important}.d-lg-none{display:none!important}.flex-lg-fill{flex:1 1 auto!important}.flex-lg-row{flex-direction:row!important}.flex-lg-column{flex-direction:column!important}.flex-lg-row-reverse{flex-direction:row-reverse!important}.flex-lg-column-reverse{flex-direction:column-reverse!important}.flex-lg-grow-0{flex-grow:0!important}.flex-lg-grow-1{flex-grow:1!important}.flex-lg-shrink-0{flex-shrink:0!important}.flex-lg-shrink-1{flex-shrink:1!important}.flex-lg-wrap{flex-wrap:wrap!important}.flex-lg-nowrap{flex-wrap:nowrap!important}.flex-lg-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-lg-start{justify-content:flex-start!important}.justify-content-lg-end{justify-content:flex-end!important}.justify-content-lg-center{justify-content:center!important}.justify-content-lg-between{justify-content:space-between!important}.justify-content-lg-around{justify-content:space-around!important}.justify-content-lg-evenly{justify-content:space-evenly!important}.align-items-lg-start{align-items:flex-start!important}.align-items-lg-end{align-items:flex-end!important}.align-items-lg-center{align-items:center!important}.align-items-lg-baseline{align-items:baseline!important}.align-items-lg-stretch{align-items:stretch!important}.align-content-lg-start{align-content:flex-start!important}.align-content-lg-end{align-content:flex-end!important}.align-content-lg-center{align-content:center!important}.align-content-lg-between{align-content:space-between!important}.align-content-lg-around{align-content:space-around!important}.align-content-lg-stretch{align-content:stretch!important}.align-self-lg-auto{align-self:auto!important}.align-self-lg-start{align-self:flex-start!important}.align-self-lg-end{align-self:flex-end!important}.align-self-lg-center{align-self:center!important}.align-self-lg-baseline{align-self:baseline!important}.align-self-lg-stretch{align-self:stretch!important}.order-lg-first{order:-1!important}.order-lg-0{order:0!important}.order-lg-1{order:1!important}.order-lg-2{order:2!important}.order-lg-3{order:3!important}.order-lg-4{order:4!important}.order-lg-5{order:5!important}.order-lg-last{order:6!important}.m-lg-0{margin:0!important}.m-lg-1{margin:.25rem!important}.m-lg-2{margin:.5rem!important}.m-lg-3{margin:1rem!important}.m-lg-4{margin:1.5rem!important}.m-lg-5{margin:3rem!important}.m-lg-auto{margin:auto!important}.mx-lg-0{margin-right:0!important;margin-left:0!important}.mx-lg-1{margin-right:.25rem!important;margin-left:.25rem!important}.mx-lg-2{margin-right:.5rem!important;margin-left:.5rem!important}.mx-lg-3{margin-right:1rem!important;margin-left:1rem!important}.mx-lg-4{margin-right:1.5rem!important;margin-left:1.5rem!important}.mx-lg-5{margin-right:3rem!important;margin-left:3rem!important}.mx-lg-auto{margin-right:auto!important;margin-left:auto!important}.my-lg-0{margin-top:0!important;margin-bottom:0!important}.my-lg-1{margin-top:.25rem!important;margin-bottom:.25rem!important}.my-lg-2{margin-top:.5rem!important;margin-bottom:.5rem!important}.my-lg-3{margin-top:1rem!important;margin-bottom:1rem!important}.my-lg-4{margin-top:1.5rem!important;margin-bottom:1.5rem!important}.my-lg-5{margin-top:3rem!important;margin-bottom:3rem!important}.my-lg-auto{margin-top:auto!important;margin-bottom:auto!important}.mt-lg-0{margin-top:0!important}.mt-lg-1{margin-top:.25rem!important}.mt-lg-2{margin-top:.5rem!important}.mt-lg-3{margin-top:1rem!important}.mt-lg-4{margin-top:1.5rem!important}.mt-lg-5{margin-top:3rem!important}.mt-lg-auto{margin-top:auto!important}.me-lg-0{margin-right:0!important}.me-lg-1{margin-right:.25rem!important}.me-lg-2{margin-right:.5rem!important}.me-lg-3{margin-right:1rem!important}.me-lg-4{margin-right:1.5rem!important}.me-lg-5{margin-right:3rem!important}.me-lg-auto{margin-right:auto!important}.mb-lg-0{margin-bottom:0!important}.mb-lg-1{margin-bottom:.25rem!important}.mb-lg-2{margin-bottom:.5rem!important}.mb-lg-3{margin-bottom:1rem!important}.mb-lg-4{margin-bottom:1.5rem!important}.mb-lg-5{margin-bottom:3rem!important}.mb-lg-auto{margin-bottom:auto!important}.ms-lg-0{margin-left:0!important}.ms-lg-1{margin-left:.25rem!important}.ms-lg-2{margin-left:.5rem!important}.ms-lg-3{margin-left:1rem!important}.ms-lg-4{margin-left:1.5rem!important}.ms-lg-5{margin-left:3rem!important}.ms-lg-auto{margin-left:auto!important}.p-lg-0{padding:0!important}.p-lg-1{padding:.25rem!important}.p-lg-2{padding:.5rem!important}.p-lg-3{padding:1rem!important}.p-lg-4{padding:1.5rem!important}.p-lg-5{padding:3rem!important}.px-lg-0{padding-right:0!important;padding-left:0!important}.px-lg-1{padding-right:.25rem!important;padding-left:.25rem!important}.px-lg-2{padding-right:.5rem!important;padding-left:.5rem!important}.px-lg-3{padding-right:1rem!important;padding-left:1rem!important}.px-lg-4{padding-right:1.5rem!important;padding-left:1.5rem!important}.px-lg-5{padding-right:3rem!important;padding-left:3rem!important}.py-lg-0{padding-top:0!important;padding-bottom:0!important}.py-lg-1{padding-top:.25rem!important;padding-bottom:.25rem!important}.py-lg-2{padding-top:.5rem!important;padding-bottom:.5rem!important}.py-lg-3{padding-top:1rem!important;padding-bottom:1rem!important}.py-lg-4{padding-top:1.5rem!important;padding-bottom:1.5rem!important}.py-lg-5{padding-top:3rem!important;padding-bottom:3rem!important}.pt-lg-0{padding-top:0!important}.pt-lg-1{padding-top:.25rem!important}.pt-lg-2{padding-top:.5rem!important}.pt-lg-3{padding-top:1rem!important}.pt-lg-4{padding-top:1.5rem!important}.pt-lg-5{padding-top:3rem!important}.pe-lg-0{padding-right:0!important}.pe-lg-1{padding-right:.25rem!important}.pe-lg-2{padding-right:.5rem!important}.pe-lg-3{padding-right:1rem!important}.pe-lg-4{padding-right:1.5rem!important}.pe-lg-5{padding-right:3rem!important}.pb-lg-0{padding-bottom:0!important}.pb-lg-1{padding-bottom:.25rem!important}.pb-lg-2{padding-bottom:.5rem!important}.pb-lg-3{padding-bottom:1rem!important}.pb-lg-4{padding-bottom:1.5rem!important}.pb-lg-5{padding-bottom:3rem!important}.ps-lg-0{padding-left:0!important}.ps-lg-1{padding-left:.25rem!important}.ps-lg-2{padding-left:.5rem!important}.ps-lg-3{padding-left:1rem!important}.ps-lg-4{padding-left:1.5rem!important}.ps-lg-5{padding-left:3rem!important}.gap-lg-0{gap:0!important}.gap-lg-1{gap:.25rem!important}.gap-lg-2{gap:.5rem!important}.gap-lg-3{gap:1rem!important}.gap-lg-4{gap:1.5rem!important}.gap-lg-5{gap:3rem!important}.row-gap-lg-0{row-gap:0!important}.row-gap-lg-1{row-gap:.25rem!important}.row-gap-lg-2{row-gap:.5rem!important}.row-gap-lg-3{row-gap:1rem!important}.row-gap-lg-4{row-gap:1.5rem!important}.row-gap-lg-5{row-gap:3rem!important}.column-gap-lg-0{-moz-column-gap:0!important;column-gap:0!important}.column-gap-lg-1{-moz-column-gap:0.25rem!important;column-gap:.25rem!important}.column-gap-lg-2{-moz-column-gap:0.5rem!important;column-gap:.5rem!important}.column-gap-lg-3{-moz-column-gap:1rem!important;column-gap:1rem!important}.column-gap-lg-4{-moz-column-gap:1.5rem!important;column-gap:1.5rem!important}.column-gap-lg-5{-moz-column-gap:3rem!important;column-gap:3rem!important}.text-lg-start{text-align:left!important}.text-lg-end{text-align:right!important}.text-lg-center{text-align:center!important}}@media (min-width:1200px){.float-xl-start{float:left!important}.float-xl-end{float:right!important}.float-xl-none{float:none!important}.object-fit-xl-contain{-o-object-fit:contain!important;object-fit:contain!important}.object-fit-xl-cover{-o-object-fit:cover!important;object-fit:cover!important}.object-fit-xl-fill{-o-object-fit:fill!important;object-fit:fill!important}.object-fit-xl-scale{-o-object-fit:scale-down!important;object-fit:scale-down!important}.object-fit-xl-none{-o-object-fit:none!important;object-fit:none!important}.d-xl-inline{display:inline!important}.d-xl-inline-block{display:inline-block!important}.d-xl-block{display:block!important}.d-xl-grid{display:grid!important}.d-xl-inline-grid{display:inline-grid!important}.d-xl-table{display:table!important}.d-xl-table-row{display:table-row!important}.d-xl-table-cell{display:table-cell!important}.d-xl-flex{display:flex!important}.d-xl-inline-flex{display:inline-flex!important}.d-xl-none{display:none!important}.flex-xl-fill{flex:1 1 auto!important}.flex-xl-row{flex-direction:row!important}.flex-xl-column{flex-direction:column!important}.flex-xl-row-reverse{flex-direction:row-reverse!important}.flex-xl-column-reverse{flex-direction:column-reverse!important}.flex-xl-grow-0{flex-grow:0!important}.flex-xl-grow-1{flex-grow:1!important}.flex-xl-shrink-0{flex-shrink:0!important}.flex-xl-shrink-1{flex-shrink:1!important}.flex-xl-wrap{flex-wrap:wrap!important}.flex-xl-nowrap{flex-wrap:nowrap!important}.flex-xl-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-xl-start{justify-content:flex-start!important}.justify-content-xl-end{justify-content:flex-end!important}.justify-content-xl-center{justify-content:center!important}.justify-content-xl-between{justify-content:space-between!important}.justify-content-xl-around{justify-content:space-around!important}.justify-content-xl-evenly{justify-content:space-evenly!important}.align-items-xl-start{align-items:flex-start!important}.align-items-xl-end{align-items:flex-end!important}.align-items-xl-center{align-items:center!important}.align-items-xl-baseline{align-items:baseline!important}.align-items-xl-stretch{align-items:stretch!important}.align-content-xl-start{align-content:flex-start!important}.align-content-xl-end{align-content:flex-end!important}.align-content-xl-center{align-content:center!important}.align-content-xl-between{align-content:space-between!important}.align-content-xl-around{align-content:space-around!important}.align-content-xl-stretch{align-content:stretch!important}.align-self-xl-auto{align-self:auto!important}.align-self-xl-start{align-self:flex-start!important}.align-self-xl-end{align-self:flex-end!important}.align-self-xl-center{align-self:center!important}.align-self-xl-baseline{align-self:baseline!important}.align-self-xl-stretch{align-self:stretch!important}.order-xl-first{order:-1!important}.order-xl-0{order:0!important}.order-xl-1{order:1!important}.order-xl-2{order:2!important}.order-xl-3{order:3!important}.order-xl-4{order:4!important}.order-xl-5{order:5!important}.order-xl-last{order:6!important}.m-xl-0{margin:0!important}.m-xl-1{margin:.25rem!important}.m-xl-2{margin:.5rem!important}.m-xl-3{margin:1rem!important}.m-xl-4{margin:1.5rem!important}.m-xl-5{margin:3rem!important}.m-xl-auto{margin:auto!important}.mx-xl-0{margin-right:0!important;margin-left:0!important}.mx-xl-1{margin-right:.25rem!important;margin-left:.25rem!important}.mx-xl-2{margin-right:.5rem!important;margin-left:.5rem!important}.mx-xl-3{margin-right:1rem!important;margin-left:1rem!important}.mx-xl-4{margin-right:1.5rem!important;margin-left:1.5rem!important}.mx-xl-5{margin-right:3rem!important;margin-left:3rem!important}.mx-xl-auto{margin-right:auto!important;margin-left:auto!important}.my-xl-0{margin-top:0!important;margin-bottom:0!important}.my-xl-1{margin-top:.25rem!important;margin-bottom:.25rem!important}.my-xl-2{margin-top:.5rem!important;margin-bottom:.5rem!important}.my-xl-3{margin-top:1rem!important;margin-bottom:1rem!important}.my-xl-4{margin-top:1.5rem!important;margin-bottom:1.5rem!important}.my-xl-5{margin-top:3rem!important;margin-bottom:3rem!important}.my-xl-auto{margin-top:auto!important;margin-bottom:auto!important}.mt-xl-0{margin-top:0!important}.mt-xl-1{margin-top:.25rem!important}.mt-xl-2{margin-top:.5rem!important}.mt-xl-3{margin-top:1rem!important}.mt-xl-4{margin-top:1.5rem!important}.mt-xl-5{margin-top:3rem!important}.mt-xl-auto{margin-top:auto!important}.me-xl-0{margin-right:0!important}.me-xl-1{margin-right:.25rem!important}.me-xl-2{margin-right:.5rem!important}.me-xl-3{margin-right:1rem!important}.me-xl-4{margin-right:1.5rem!important}.me-xl-5{margin-right:3rem!important}.me-xl-auto{margin-right:auto!important}.mb-xl-0{margin-bottom:0!important}.mb-xl-1{margin-bottom:.25rem!important}.mb-xl-2{margin-bottom:.5rem!important}.mb-xl-3{margin-bottom:1rem!important}.mb-xl-4{margin-bottom:1.5rem!important}.mb-xl-5{margin-bottom:3rem!important}.mb-xl-auto{margin-bottom:auto!important}.ms-xl-0{margin-left:0!important}.ms-xl-1{margin-left:.25rem!important}.ms-xl-2{margin-left:.5rem!important}.ms-xl-3{margin-left:1rem!important}.ms-xl-4{margin-left:1.5rem!important}.ms-xl-5{margin-left:3rem!important}.ms-xl-auto{margin-left:auto!important}.p-xl-0{padding:0!important}.p-xl-1{padding:.25rem!important}.p-xl-2{padding:.5rem!important}.p-xl-3{padding:1rem!important}.p-xl-4{padding:1.5rem!important}.p-xl-5{padding:3rem!important}.px-xl-0{padding-right:0!important;padding-left:0!important}.px-xl-1{padding-right:.25rem!important;padding-left:.25rem!important}.px-xl-2{padding-right:.5rem!important;padding-left:.5rem!important}.px-xl-3{padding-right:1rem!important;padding-left:1rem!important}.px-xl-4{padding-right:1.5rem!important;padding-left:1.5rem!important}.px-xl-5{padding-right:3rem!important;padding-left:3rem!important}.py-xl-0{padding-top:0!important;padding-bottom:0!important}.py-xl-1{padding-top:.25rem!important;padding-bottom:.25rem!important}.py-xl-2{padding-top:.5rem!important;padding-bottom:.5rem!important}.py-xl-3{padding-top:1rem!important;padding-bottom:1rem!important}.py-xl-4{padding-top:1.5rem!important;padding-bottom:1.5rem!important}.py-xl-5{padding-top:3rem!important;padding-bottom:3rem!important}.pt-xl-0{padding-top:0!important}.pt-xl-1{padding-top:.25rem!important}.pt-xl-2{padding-top:.5rem!important}.pt-xl-3{padding-top:1rem!important}.pt-xl-4{padding-top:1.5rem!important}.pt-xl-5{padding-top:3rem!important}.pe-xl-0{padding-right:0!important}.pe-xl-1{padding-right:.25rem!important}.pe-xl-2{padding-right:.5rem!important}.pe-xl-3{padding-right:1rem!important}.pe-xl-4{padding-right:1.5rem!important}.pe-xl-5{padding-right:3rem!important}.pb-xl-0{padding-bottom:0!important}.pb-xl-1{padding-bottom:.25rem!important}.pb-xl-2{padding-bottom:.5rem!important}.pb-xl-3{padding-bottom:1rem!important}.pb-xl-4{padding-bottom:1.5rem!important}.pb-xl-5{padding-bottom:3rem!important}.ps-xl-0{padding-left:0!important}.ps-xl-1{padding-left:.25rem!important}.ps-xl-2{padding-left:.5rem!important}.ps-xl-3{padding-left:1rem!important}.ps-xl-4{padding-left:1.5rem!important}.ps-xl-5{padding-left:3rem!important}.gap-xl-0{gap:0!important}.gap-xl-1{gap:.25rem!important}.gap-xl-2{gap:.5rem!important}.gap-xl-3{gap:1rem!important}.gap-xl-4{gap:1.5rem!important}.gap-xl-5{gap:3rem!important}.row-gap-xl-0{row-gap:0!important}.row-gap-xl-1{row-gap:.25rem!important}.row-gap-xl-2{row-gap:.5rem!important}.row-gap-xl-3{row-gap:1rem!important}.row-gap-xl-4{row-gap:1.5rem!important}.row-gap-xl-5{row-gap:3rem!important}.column-gap-xl-0{-moz-column-gap:0!important;column-gap:0!important}.column-gap-xl-1{-moz-column-gap:0.25rem!important;column-gap:.25rem!important}.column-gap-xl-2{-moz-column-gap:0.5rem!important;column-gap:.5rem!important}.column-gap-xl-3{-moz-column-gap:1rem!important;column-gap:1rem!important}.column-gap-xl-4{-moz-column-gap:1.5rem!important;column-gap:1.5rem!important}.column-gap-xl-5{-moz-column-gap:3rem!important;column-gap:3rem!important}.text-xl-start{text-align:left!important}.text-xl-end{text-align:right!important}.text-xl-center{text-align:center!important}}@media (min-width:1400px){.float-xxl-start{float:left!important}.float-xxl-end{float:right!important}.float-xxl-none{float:none!important}.object-fit-xxl-contain{-o-object-fit:contain!important;object-fit:contain!important}.object-fit-xxl-cover{-o-object-fit:cover!important;object-fit:cover!important}.object-fit-xxl-fill{-o-object-fit:fill!important;object-fit:fill!important}.object-fit-xxl-scale{-o-object-fit:scale-down!important;object-fit:scale-down!important}.object-fit-xxl-none{-o-object-fit:none!important;object-fit:none!important}.d-xxl-inline{display:inline!important}.d-xxl-inline-block{display:inline-block!important}.d-xxl-block{display:block!important}.d-xxl-grid{display:grid!important}.d-xxl-inline-grid{display:inline-grid!important}.d-xxl-table{display:table!important}.d-xxl-table-row{display:table-row!important}.d-xxl-table-cell{display:table-cell!important}.d-xxl-flex{display:flex!important}.d-xxl-inline-flex{display:inline-flex!important}.d-xxl-none{display:none!important}.flex-xxl-fill{flex:1 1 auto!important}.flex-xxl-row{flex-direction:row!important}.flex-xxl-column{flex-direction:column!important}.flex-xxl-row-reverse{flex-direction:row-reverse!important}.flex-xxl-column-reverse{flex-direction:column-reverse!important}.flex-xxl-grow-0{flex-grow:0!important}.flex-xxl-grow-1{flex-grow:1!important}.flex-xxl-shrink-0{flex-shrink:0!important}.flex-xxl-shrink-1{flex-shrink:1!important}.flex-xxl-wrap{flex-wrap:wrap!important}.flex-xxl-nowrap{flex-wrap:nowrap!important}.flex-xxl-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-xxl-start{justify-content:flex-start!important}.justify-content-xxl-end{justify-content:flex-end!important}.justify-content-xxl-center{justify-content:center!important}.justify-content-xxl-between{justify-content:space-between!important}.justify-content-xxl-around{justify-content:space-around!important}.justify-content-xxl-evenly{justify-content:space-evenly!important}.align-items-xxl-start{align-items:flex-start!important}.align-items-xxl-end{align-items:flex-end!important}.align-items-xxl-center{align-items:center!important}.align-items-xxl-baseline{align-items:baseline!important}.align-items-xxl-stretch{align-items:stretch!important}.align-content-xxl-start{align-content:flex-start!important}.align-content-xxl-end{align-content:flex-end!important}.align-content-xxl-center{align-content:center!important}.align-content-xxl-between{align-content:space-between!important}.align-content-xxl-around{align-content:space-around!important}.align-content-xxl-stretch{align-content:stretch!important}.align-self-xxl-auto{align-self:auto!important}.align-self-xxl-start{align-self:flex-start!important}.align-self-xxl-end{align-self:flex-end!important}.align-self-xxl-center{align-self:center!important}.align-self-xxl-baseline{align-self:baseline!important}.align-self-xxl-stretch{align-self:stretch!important}.order-xxl-first{order:-1!important}.order-xxl-0{order:0!important}.order-xxl-1{order:1!important}.order-xxl-2{order:2!important}.order-xxl-3{order:3!important}.order-xxl-4{order:4!important}.order-xxl-5{order:5!important}.order-xxl-last{order:6!important}.m-xxl-0{margin:0!important}.m-xxl-1{margin:.25rem!important}.m-xxl-2{margin:.5rem!important}.m-xxl-3{margin:1rem!important}.m-xxl-4{margin:1.5rem!important}.m-xxl-5{margin:3rem!important}.m-xxl-auto{margin:auto!important}.mx-xxl-0{margin-right:0!important;margin-left:0!important}.mx-xxl-1{margin-right:.25rem!important;margin-left:.25rem!important}.mx-xxl-2{margin-right:.5rem!important;margin-left:.5rem!important}.mx-xxl-3{margin-right:1rem!important;margin-left:1rem!important}.mx-xxl-4{margin-right:1.5rem!important;margin-left:1.5rem!important}.mx-xxl-5{margin-right:3rem!important;margin-left:3rem!important}.mx-xxl-auto{margin-right:auto!important;margin-left:auto!important}.my-xxl-0{margin-top:0!important;margin-bottom:0!important}.my-xxl-1{margin-top:.25rem!important;margin-bottom:.25rem!important}.my-xxl-2{margin-top:.5rem!important;margin-bottom:.5rem!important}.my-xxl-3{margin-top:1rem!important;margin-bottom:1rem!important}.my-xxl-4{margin-top:1.5rem!important;margin-bottom:1.5rem!important}.my-xxl-5{margin-top:3rem!important;margin-bottom:3rem!important}.my-xxl-auto{margin-top:auto!important;margin-bottom:auto!important}.mt-xxl-0{margin-top:0!important}.mt-xxl-1{margin-top:.25rem!important}.mt-xxl-2{margin-top:.5rem!important}.mt-xxl-3{margin-top:1rem!important}.mt-xxl-4{margin-top:1.5rem!important}.mt-xxl-5{margin-top:3rem!important}.mt-xxl-auto{margin-top:auto!important}.me-xxl-0{margin-right:0!important}.me-xxl-1{margin-right:.25rem!important}.me-xxl-2{margin-right:.5rem!important}.me-xxl-3{margin-right:1rem!important}.me-xxl-4{margin-right:1.5rem!important}.me-xxl-5{margin-right:3rem!important}.me-xxl-auto{margin-right:auto!important}.mb-xxl-0{margin-bottom:0!important}.mb-xxl-1{margin-bottom:.25rem!important}.mb-xxl-2{margin-bottom:.5rem!important}.mb-xxl-3{margin-bottom:1rem!important}.mb-xxl-4{margin-bottom:1.5rem!important}.mb-xxl-5{margin-bottom:3rem!important}.mb-xxl-auto{margin-bottom:auto!important}.ms-xxl-0{margin-left:0!important}.ms-xxl-1{margin-left:.25rem!important}.ms-xxl-2{margin-left:.5rem!important}.ms-xxl-3{margin-left:1rem!important}.ms-xxl-4{margin-left:1.5rem!important}.ms-xxl-5{margin-left:3rem!important}.ms-xxl-auto{margin-left:auto!important}.p-xxl-0{padding:0!important}.p-xxl-1{padding:.25rem!important}.p-xxl-2{padding:.5rem!important}.p-xxl-3{padding:1rem!important}.p-xxl-4{padding:1.5rem!important}.p-xxl-5{padding:3rem!important}.px-xxl-0{padding-right:0!important;padding-left:0!important}.px-xxl-1{padding-right:.25rem!important;padding-left:.25rem!important}.px-xxl-2{padding-right:.5rem!important;padding-left:.5rem!important}.px-xxl-3{padding-right:1rem!important;padding-left:1rem!important}.px-xxl-4{padding-right:1.5rem!important;padding-left:1.5rem!important}.px-xxl-5{padding-right:3rem!important;padding-left:3rem!important}.py-xxl-0{padding-top:0!important;padding-bottom:0!important}.py-xxl-1{padding-top:.25rem!important;padding-bottom:.25rem!important}.py-xxl-2{padding-top:.5rem!important;padding-bottom:.5rem!important}.py-xxl-3{padding-top:1rem!important;padding-bottom:1rem!important}.py-xxl-4{padding-top:1.5rem!important;padding-bottom:1.5rem!important}.py-xxl-5{padding-top:3rem!important;padding-bottom:3rem!important}.pt-xxl-0{padding-top:0!important}.pt-xxl-1{padding-top:.25rem!important}.pt-xxl-2{padding-top:.5rem!important}.pt-xxl-3{padding-top:1rem!important}.pt-xxl-4{padding-top:1.5rem!important}.pt-xxl-5{padding-top:3rem!important}.pe-xxl-0{padding-right:0!important}.pe-xxl-1{padding-right:.25rem!important}.pe-xxl-2{padding-right:.5rem!important}.pe-xxl-3{padding-right:1rem!important}.pe-xxl-4{padding-right:1.5rem!important}.pe-xxl-5{padding-right:3rem!important}.pb-xxl-0{padding-bottom:0!important}.pb-xxl-1{padding-bottom:.25rem!important}.pb-xxl-2{padding-bottom:.5rem!important}.pb-xxl-3{padding-bottom:1rem!important}.pb-xxl-4{padding-bottom:1.5rem!important}.pb-xxl-5{padding-bottom:3rem!important}.ps-xxl-0{padding-left:0!important}.ps-xxl-1{padding-left:.25rem!important}.ps-xxl-2{padding-left:.5rem!important}.ps-xxl-3{padding-left:1rem!important}.ps-xxl-4{padding-left:1.5rem!important}.ps-xxl-5{padding-left:3rem!important}.gap-xxl-0{gap:0!important}.gap-xxl-1{gap:.25rem!important}.gap-xxl-2{gap:.5rem!important}.gap-xxl-3{gap:1rem!important}.gap-xxl-4{gap:1.5rem!important}.gap-xxl-5{gap:3rem!important}.row-gap-xxl-0{row-gap:0!important}.row-gap-xxl-1{row-gap:.25rem!important}.row-gap-xxl-2{row-gap:.5rem!important}.row-gap-xxl-3{row-gap:1rem!important}.row-gap-xxl-4{row-gap:1.5rem!important}.row-gap-xxl-5{row-gap:3rem!important}.column-gap-xxl-0{-moz-column-gap:0!important;column-gap:0!important}.column-gap-xxl-1{-moz-column-gap:0.25rem!important;column-gap:.25rem!important}.column-gap-xxl-2{-moz-column-gap:0.5rem!important;column-gap:.5rem!important}.column-gap-xxl-3{-moz-column-gap:1rem!important;column-gap:1rem!important}.column-gap-xxl-4{-moz-column-gap:1.5rem!important;column-gap:1.5rem!important}.column-gap-xxl-5{-moz-column-gap:3rem!important;column-gap:3rem!important}.text-xxl-start{text-align:left!important}.text-xxl-end{text-align:right!important}.text-xxl-center{text-align:center!important}}@media (min-width:1200px){.fs-1{font-size:2.5rem!important}.fs-2{font-size:2rem!important}.fs-3{font-size:1.75rem!important}.fs-4{font-size:1.5rem!important}}@media print{.d-print-inline{display:inline!important}.d-print-inline-block{display:inline-block!important}.d-print-block{display:block!important}.d-print-grid{display:grid!important}.d-print-inline-grid{display:inline-grid!important}.d-print-table{display:table!important}.d-print-table-row{display:table-row!important}.d-print-table-cell{display:table-cell!important}.d-print-flex{display:flex!important}.d-print-inline-flex{display:inline-flex!important}.d-print-none{display:none!important}}
6: /*# sourceMappingURL=bootstrap.min.css.map */
```

## File: switchbot_dashboard/static/vendor/css/space-grotesk.css
```css
 1: @font-face {
 2:   font-family: 'Space Grotesk';
 3:   font-style: normal;
 4:   font-weight: 400;
 5:   font-display: swap;
 6:   src: url('../fonts/SpaceGrotesk-Regular.ttf') format('truetype');
 7: }
 8: 
 9: @font-face {
10:   font-family: 'Space Grotesk';
11:   font-style: normal;
12:   font-weight: 500;
13:   font-display: swap;
14:   src: url('../fonts/SpaceGrotesk-Medium.ttf') format('truetype');
15: }
16: 
17: @font-face {
18:   font-family: 'Space Grotesk';
19:   font-style: normal;
20:   font-weight: 600;
21:   font-display: swap;
22:   src: url('../fonts/SpaceGrotesk-SemiBold.ttf') format('truetype');
23: }
```

## File: switchbot_dashboard/static/vendor/fontawesome/css/all.min.css
```css
1: /*!
2:  * Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com
3:  * License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License)
4:  * Copyright 2023 Fonticons, Inc.
5:  */
6: .fa{font-family:var(--fa-style-family,"Font Awesome 6 Free");font-weight:var(--fa-style,900)}.fa,.fa-brands,.fa-classic,.fa-regular,.fa-sharp,.fa-solid,.fab,.far,.fas{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;display:var(--fa-display,inline-block);font-style:normal;font-variant:normal;line-height:1;text-rendering:auto}.fa-classic,.fa-regular,.fa-solid,.far,.fas{font-family:"Font Awesome 6 Free"}.fa-brands,.fab{font-family:"Font Awesome 6 Brands"}.fa-1x{font-size:1em}.fa-2x{font-size:2em}.fa-3x{font-size:3em}.fa-4x{font-size:4em}.fa-5x{font-size:5em}.fa-6x{font-size:6em}.fa-7x{font-size:7em}.fa-8x{font-size:8em}.fa-9x{font-size:9em}.fa-10x{font-size:10em}.fa-2xs{font-size:.625em;line-height:.1em;vertical-align:.225em}.fa-xs{font-size:.75em;line-height:.08333em;vertical-align:.125em}.fa-sm{font-size:.875em;line-height:.07143em;vertical-align:.05357em}.fa-lg{font-size:1.25em;line-height:.05em;vertical-align:-.075em}.fa-xl{font-size:1.5em;line-height:.04167em;vertical-align:-.125em}.fa-2xl{font-size:2em;line-height:.03125em;vertical-align:-.1875em}.fa-fw{text-align:center;width:1.25em}.fa-ul{list-style-type:none;margin-left:var(--fa-li-margin,2.5em);padding-left:0}.fa-ul>li{position:relative}.fa-li{left:calc(var(--fa-li-width, 2em)*-1);position:absolute;text-align:center;width:var(--fa-li-width,2em);line-height:inherit}.fa-border{border-radius:var(--fa-border-radius,.1em);border:var(--fa-border-width,.08em) var(--fa-border-style,solid) var(--fa-border-color,#eee);padding:var(--fa-border-padding,.2em .25em .15em)}.fa-pull-left{float:left;margin-right:var(--fa-pull-margin,.3em)}.fa-pull-right{float:right;margin-left:var(--fa-pull-margin,.3em)}.fa-beat{-webkit-animation-name:fa-beat;animation-name:fa-beat;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,ease-in-out);animation-timing-function:var(--fa-animation-timing,ease-in-out)}.fa-bounce{-webkit-animation-name:fa-bounce;animation-name:fa-bounce;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,cubic-bezier(.28,.84,.42,1));animation-timing-function:var(--fa-animation-timing,cubic-bezier(.28,.84,.42,1))}.fa-fade{-webkit-animation-name:fa-fade;animation-name:fa-fade;-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1));animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))}.fa-beat-fade,.fa-fade{-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s)}.fa-beat-fade{-webkit-animation-name:fa-beat-fade;animation-name:fa-beat-fade;-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1));animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))}.fa-flip{-webkit-animation-name:fa-flip;animation-name:fa-flip;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,ease-in-out);animation-timing-function:var(--fa-animation-timing,ease-in-out)}.fa-shake{-webkit-animation-name:fa-shake;animation-name:fa-shake;-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,linear);animation-timing-function:var(--fa-animation-timing,linear)}.fa-shake,.fa-spin{-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal)}.fa-spin{-webkit-animation-name:fa-spin;animation-name:fa-spin;-webkit-animation-duration:var(--fa-animation-duration,2s);animation-duration:var(--fa-animation-duration,2s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,linear);animation-timing-function:var(--fa-animation-timing,linear)}.fa-spin-reverse{--fa-animation-direction:reverse}.fa-pulse,.fa-spin-pulse{-webkit-animation-name:fa-spin;animation-name:fa-spin;-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,steps(8));animation-timing-function:var(--fa-animation-timing,steps(8))}@media (prefers-reduced-motion:reduce){.fa-beat,.fa-beat-fade,.fa-bounce,.fa-fade,.fa-flip,.fa-pulse,.fa-shake,.fa-spin,.fa-spin-pulse{-webkit-animation-delay:-1ms;animation-delay:-1ms;-webkit-animation-duration:1ms;animation-duration:1ms;-webkit-animation-iteration-count:1;animation-iteration-count:1;-webkit-transition-delay:0s;transition-delay:0s;-webkit-transition-duration:0s;transition-duration:0s}}@-webkit-keyframes fa-beat{0%,90%{-webkit-transform:scale(1);transform:scale(1)}45%{-webkit-transform:scale(var(--fa-beat-scale,1.25));transform:scale(var(--fa-beat-scale,1.25))}}@keyframes fa-beat{0%,90%{-webkit-transform:scale(1);transform:scale(1)}45%{-webkit-transform:scale(var(--fa-beat-scale,1.25));transform:scale(var(--fa-beat-scale,1.25))}}@-webkit-keyframes fa-bounce{0%{-webkit-transform:scale(1) translateY(0);transform:scale(1) translateY(0)}10%{-webkit-transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0);transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0)}30%{-webkit-transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,-.5em));transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,-.5em))}50%{-webkit-transform:scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95)) translateY(0);transform:scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95)) translateY(0)}57%{-webkit-transform:scale(1) translateY(var(--fa-bounce-rebound,-.125em));transform:scale(1) translateY(var(--fa-bounce-rebound,-.125em))}64%{-webkit-transform:scale(1) translateY(0);transform:scale(1) translateY(0)}to{-webkit-transform:scale(1) translateY(0);transform:scale(1) translateY(0)}}@keyframes fa-bounce{0%{-webkit-transform:scale(1) translateY(0);transform:scale(1) translateY(0)}10%{-webkit-transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0);transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0)}30%{-webkit-transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,-.5em));transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,-.5em))}50%{-webkit-transform:scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95)) translateY(0);transform:scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95)) translateY(0)}57%{-webkit-transform:scale(1) translateY(var(--fa-bounce-rebound,-.125em));transform:scale(1) translateY(var(--fa-bounce-rebound,-.125em))}64%{-webkit-transform:scale(1) translateY(0);transform:scale(1) translateY(0)}to{-webkit-transform:scale(1) translateY(0);transform:scale(1) translateY(0)}}@-webkit-keyframes fa-fade{50%{opacity:var(--fa-fade-opacity,.4)}}@keyframes fa-fade{50%{opacity:var(--fa-fade-opacity,.4)}}@-webkit-keyframes fa-beat-fade{0%,to{opacity:var(--fa-beat-fade-opacity,.4);-webkit-transform:scale(1);transform:scale(1)}50%{opacity:1;-webkit-transform:scale(var(--fa-beat-fade-scale,1.125));transform:scale(var(--fa-beat-fade-scale,1.125))}}@keyframes fa-beat-fade{0%,to{opacity:var(--fa-beat-fade-opacity,.4);-webkit-transform:scale(1);transform:scale(1)}50%{opacity:1;-webkit-transform:scale(var(--fa-beat-fade-scale,1.125));transform:scale(var(--fa-beat-fade-scale,1.125))}}@-webkit-keyframes fa-flip{50%{-webkit-transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg))}}@keyframes fa-flip{50%{-webkit-transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg))}}@-webkit-keyframes fa-shake{0%{-webkit-transform:rotate(-15deg);transform:rotate(-15deg)}4%{-webkit-transform:rotate(15deg);transform:rotate(15deg)}8%,24%{-webkit-transform:rotate(-18deg);transform:rotate(-18deg)}12%,28%{-webkit-transform:rotate(18deg);transform:rotate(18deg)}16%{-webkit-transform:rotate(-22deg);transform:rotate(-22deg)}20%{-webkit-transform:rotate(22deg);transform:rotate(22deg)}32%{-webkit-transform:rotate(-12deg);transform:rotate(-12deg)}36%{-webkit-transform:rotate(12deg);transform:rotate(12deg)}40%,to{-webkit-transform:rotate(0deg);transform:rotate(0deg)}}@keyframes fa-shake{0%{-webkit-transform:rotate(-15deg);transform:rotate(-15deg)}4%{-webkit-transform:rotate(15deg);transform:rotate(15deg)}8%,24%{-webkit-transform:rotate(-18deg);transform:rotate(-18deg)}12%,28%{-webkit-transform:rotate(18deg);transform:rotate(18deg)}16%{-webkit-transform:rotate(-22deg);transform:rotate(-22deg)}20%{-webkit-transform:rotate(22deg);transform:rotate(22deg)}32%{-webkit-transform:rotate(-12deg);transform:rotate(-12deg)}36%{-webkit-transform:rotate(12deg);transform:rotate(12deg)}40%,to{-webkit-transform:rotate(0deg);transform:rotate(0deg)}}@-webkit-keyframes fa-spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}@keyframes fa-spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}.fa-rotate-90{-webkit-transform:rotate(90deg);transform:rotate(90deg)}.fa-rotate-180{-webkit-transform:rotate(180deg);transform:rotate(180deg)}.fa-rotate-270{-webkit-transform:rotate(270deg);transform:rotate(270deg)}.fa-flip-horizontal{-webkit-transform:scaleX(-1);transform:scaleX(-1)}.fa-flip-vertical{-webkit-transform:scaleY(-1);transform:scaleY(-1)}.fa-flip-both,.fa-flip-horizontal.fa-flip-vertical{-webkit-transform:scale(-1);transform:scale(-1)}.fa-rotate-by{-webkit-transform:rotate(var(--fa-rotate-angle,none));transform:rotate(var(--fa-rotate-angle,none))}.fa-stack{display:inline-block;height:2em;line-height:2em;position:relative;vertical-align:middle;width:2.5em}.fa-stack-1x,.fa-stack-2x{left:0;position:absolute;text-align:center;width:100%;z-index:var(--fa-stack-z-index,auto)}.fa-stack-1x{line-height:inherit}.fa-stack-2x{font-size:2em}.fa-inverse{color:var(--fa-inverse,#fff)}
7: 
8: .fa-0:before{content:"\30"}.fa-1:before{content:"\31"}.fa-2:before{content:"\32"}.fa-3:before{content:"\33"}.fa-4:before{content:"\34"}.fa-5:before{content:"\35"}.fa-6:before{content:"\36"}.fa-7:before{content:"\37"}.fa-8:before{content:"\38"}.fa-9:before{content:"\39"}.fa-fill-drip:before{content:"\f576"}.fa-arrows-to-circle:before{content:"\e4bd"}.fa-chevron-circle-right:before,.fa-circle-chevron-right:before{content:"\f138"}.fa-at:before{content:"\40"}.fa-trash-alt:before,.fa-trash-can:before{content:"\f2ed"}.fa-text-height:before{content:"\f034"}.fa-user-times:before,.fa-user-xmark:before{content:"\f235"}.fa-stethoscope:before{content:"\f0f1"}.fa-comment-alt:before,.fa-message:before{content:"\f27a"}.fa-info:before{content:"\f129"}.fa-compress-alt:before,.fa-down-left-and-up-right-to-center:before{content:"\f422"}.fa-explosion:before{content:"\e4e9"}.fa-file-alt:before,.fa-file-lines:before,.fa-file-text:before{content:"\f15c"}.fa-wave-square:before{content:"\f83e"}.fa-ring:before{content:"\f70b"}.fa-building-un:before{content:"\e4d9"}.fa-dice-three:before{content:"\f527"}.fa-calendar-alt:before,.fa-calendar-days:before{content:"\f073"}.fa-anchor-circle-check:before{content:"\e4aa"}.fa-building-circle-arrow-right:before{content:"\e4d1"}.fa-volleyball-ball:before,.fa-volleyball:before{content:"\f45f"}.fa-arrows-up-to-line:before{content:"\e4c2"}.fa-sort-desc:before,.fa-sort-down:before{content:"\f0dd"}.fa-circle-minus:before,.fa-minus-circle:before{content:"\f056"}.fa-door-open:before{content:"\f52b"}.fa-right-from-bracket:before,.fa-sign-out-alt:before{content:"\f2f5"}.fa-atom:before{content:"\f5d2"}.fa-soap:before{content:"\e06e"}.fa-heart-music-camera-bolt:before,.fa-icons:before{content:"\f86d"}.fa-microphone-alt-slash:before,.fa-microphone-lines-slash:before{content:"\f539"}.fa-bridge-circle-check:before{content:"\e4c9"}.fa-pump-medical:before{content:"\e06a"}.fa-fingerprint:before{content:"\f577"}.fa-hand-point-right:before{content:"\f0a4"}.fa-magnifying-glass-location:before,.fa-search-location:before{content:"\f689"}.fa-forward-step:before,.fa-step-forward:before{content:"\f051"}.fa-face-smile-beam:before,.fa-smile-beam:before{content:"\f5b8"}.fa-flag-checkered:before{content:"\f11e"}.fa-football-ball:before,.fa-football:before{content:"\f44e"}.fa-school-circle-exclamation:before{content:"\e56c"}.fa-crop:before{content:"\f125"}.fa-angle-double-down:before,.fa-angles-down:before{content:"\f103"}.fa-users-rectangle:before{content:"\e594"}.fa-people-roof:before{content:"\e537"}.fa-people-line:before{content:"\e534"}.fa-beer-mug-empty:before,.fa-beer:before{content:"\f0fc"}.fa-diagram-predecessor:before{content:"\e477"}.fa-arrow-up-long:before,.fa-long-arrow-up:before{content:"\f176"}.fa-burn:before,.fa-fire-flame-simple:before{content:"\f46a"}.fa-male:before,.fa-person:before{content:"\f183"}.fa-laptop:before{content:"\f109"}.fa-file-csv:before{content:"\f6dd"}.fa-menorah:before{content:"\f676"}.fa-truck-plane:before{content:"\e58f"}.fa-record-vinyl:before{content:"\f8d9"}.fa-face-grin-stars:before,.fa-grin-stars:before{content:"\f587"}.fa-bong:before{content:"\f55c"}.fa-pastafarianism:before,.fa-spaghetti-monster-flying:before{content:"\f67b"}.fa-arrow-down-up-across-line:before{content:"\e4af"}.fa-spoon:before,.fa-utensil-spoon:before{content:"\f2e5"}.fa-jar-wheat:before{content:"\e517"}.fa-envelopes-bulk:before,.fa-mail-bulk:before{content:"\f674"}.fa-file-circle-exclamation:before{content:"\e4eb"}.fa-circle-h:before,.fa-hospital-symbol:before{content:"\f47e"}.fa-pager:before{content:"\f815"}.fa-address-book:before,.fa-contact-book:before{content:"\f2b9"}.fa-strikethrough:before{content:"\f0cc"}.fa-k:before{content:"\4b"}.fa-landmark-flag:before{content:"\e51c"}.fa-pencil-alt:before,.fa-pencil:before{content:"\f303"}.fa-backward:before{content:"\f04a"}.fa-caret-right:before{content:"\f0da"}.fa-comments:before{content:"\f086"}.fa-file-clipboard:before,.fa-paste:before{content:"\f0ea"}.fa-code-pull-request:before{content:"\e13c"}.fa-clipboard-list:before{content:"\f46d"}.fa-truck-loading:before,.fa-truck-ramp-box:before{content:"\f4de"}.fa-user-check:before{content:"\f4fc"}.fa-vial-virus:before{content:"\e597"}.fa-sheet-plastic:before{content:"\e571"}.fa-blog:before{content:"\f781"}.fa-user-ninja:before{content:"\f504"}.fa-person-arrow-up-from-line:before{content:"\e539"}.fa-scroll-torah:before,.fa-torah:before{content:"\f6a0"}.fa-broom-ball:before,.fa-quidditch-broom-ball:before,.fa-quidditch:before{content:"\f458"}.fa-toggle-off:before{content:"\f204"}.fa-archive:before,.fa-box-archive:before{content:"\f187"}.fa-person-drowning:before{content:"\e545"}.fa-arrow-down-9-1:before,.fa-sort-numeric-desc:before,.fa-sort-numeric-down-alt:before{content:"\f886"}.fa-face-grin-tongue-squint:before,.fa-grin-tongue-squint:before{content:"\f58a"}.fa-spray-can:before{content:"\f5bd"}.fa-truck-monster:before{content:"\f63b"}.fa-w:before{content:"\57"}.fa-earth-africa:before,.fa-globe-africa:before{content:"\f57c"}.fa-rainbow:before{content:"\f75b"}.fa-circle-notch:before{content:"\f1ce"}.fa-tablet-alt:before,.fa-tablet-screen-button:before{content:"\f3fa"}.fa-paw:before{content:"\f1b0"}.fa-cloud:before{content:"\f0c2"}.fa-trowel-bricks:before{content:"\e58a"}.fa-face-flushed:before,.fa-flushed:before{content:"\f579"}.fa-hospital-user:before{content:"\f80d"}.fa-tent-arrow-left-right:before{content:"\e57f"}.fa-gavel:before,.fa-legal:before{content:"\f0e3"}.fa-binoculars:before{content:"\f1e5"}.fa-microphone-slash:before{content:"\f131"}.fa-box-tissue:before{content:"\e05b"}.fa-motorcycle:before{content:"\f21c"}.fa-bell-concierge:before,.fa-concierge-bell:before{content:"\f562"}.fa-pen-ruler:before,.fa-pencil-ruler:before{content:"\f5ae"}.fa-people-arrows-left-right:before,.fa-people-arrows:before{content:"\e068"}.fa-mars-and-venus-burst:before{content:"\e523"}.fa-caret-square-right:before,.fa-square-caret-right:before{content:"\f152"}.fa-cut:before,.fa-scissors:before{content:"\f0c4"}.fa-sun-plant-wilt:before{content:"\e57a"}.fa-toilets-portable:before{content:"\e584"}.fa-hockey-puck:before{content:"\f453"}.fa-table:before{content:"\f0ce"}.fa-magnifying-glass-arrow-right:before{content:"\e521"}.fa-digital-tachograph:before,.fa-tachograph-digital:before{content:"\f566"}.fa-users-slash:before{content:"\e073"}.fa-clover:before{content:"\e139"}.fa-mail-reply:before,.fa-reply:before{content:"\f3e5"}.fa-star-and-crescent:before{content:"\f699"}.fa-house-fire:before{content:"\e50c"}.fa-minus-square:before,.fa-square-minus:before{content:"\f146"}.fa-helicopter:before{content:"\f533"}.fa-compass:before{content:"\f14e"}.fa-caret-square-down:before,.fa-square-caret-down:before{content:"\f150"}.fa-file-circle-question:before{content:"\e4ef"}.fa-laptop-code:before{content:"\f5fc"}.fa-swatchbook:before{content:"\f5c3"}.fa-prescription-bottle:before{content:"\f485"}.fa-bars:before,.fa-navicon:before{content:"\f0c9"}.fa-people-group:before{content:"\e533"}.fa-hourglass-3:before,.fa-hourglass-end:before{content:"\f253"}.fa-heart-broken:before,.fa-heart-crack:before{content:"\f7a9"}.fa-external-link-square-alt:before,.fa-square-up-right:before{content:"\f360"}.fa-face-kiss-beam:before,.fa-kiss-beam:before{content:"\f597"}.fa-film:before{content:"\f008"}.fa-ruler-horizontal:before{content:"\f547"}.fa-people-robbery:before{content:"\e536"}.fa-lightbulb:before{content:"\f0eb"}.fa-caret-left:before{content:"\f0d9"}.fa-circle-exclamation:before,.fa-exclamation-circle:before{content:"\f06a"}.fa-school-circle-xmark:before{content:"\e56d"}.fa-arrow-right-from-bracket:before,.fa-sign-out:before{content:"\f08b"}.fa-chevron-circle-down:before,.fa-circle-chevron-down:before{content:"\f13a"}.fa-unlock-alt:before,.fa-unlock-keyhole:before{content:"\f13e"}.fa-cloud-showers-heavy:before{content:"\f740"}.fa-headphones-alt:before,.fa-headphones-simple:before{content:"\f58f"}.fa-sitemap:before{content:"\f0e8"}.fa-circle-dollar-to-slot:before,.fa-donate:before{content:"\f4b9"}.fa-memory:before{content:"\f538"}.fa-road-spikes:before{content:"\e568"}.fa-fire-burner:before{content:"\e4f1"}.fa-flag:before{content:"\f024"}.fa-hanukiah:before{content:"\f6e6"}.fa-feather:before{content:"\f52d"}.fa-volume-down:before,.fa-volume-low:before{content:"\f027"}.fa-comment-slash:before{content:"\f4b3"}.fa-cloud-sun-rain:before{content:"\f743"}.fa-compress:before{content:"\f066"}.fa-wheat-alt:before,.fa-wheat-awn:before{content:"\e2cd"}.fa-ankh:before{content:"\f644"}.fa-hands-holding-child:before{content:"\e4fa"}.fa-asterisk:before{content:"\2a"}.fa-check-square:before,.fa-square-check:before{content:"\f14a"}.fa-peseta-sign:before{content:"\e221"}.fa-header:before,.fa-heading:before{content:"\f1dc"}.fa-ghost:before{content:"\f6e2"}.fa-list-squares:before,.fa-list:before{content:"\f03a"}.fa-phone-square-alt:before,.fa-square-phone-flip:before{content:"\f87b"}.fa-cart-plus:before{content:"\f217"}.fa-gamepad:before{content:"\f11b"}.fa-circle-dot:before,.fa-dot-circle:before{content:"\f192"}.fa-dizzy:before,.fa-face-dizzy:before{content:"\f567"}.fa-egg:before{content:"\f7fb"}.fa-house-medical-circle-xmark:before{content:"\e513"}.fa-campground:before{content:"\f6bb"}.fa-folder-plus:before{content:"\f65e"}.fa-futbol-ball:before,.fa-futbol:before,.fa-soccer-ball:before{content:"\f1e3"}.fa-paint-brush:before,.fa-paintbrush:before{content:"\f1fc"}.fa-lock:before{content:"\f023"}.fa-gas-pump:before{content:"\f52f"}.fa-hot-tub-person:before,.fa-hot-tub:before{content:"\f593"}.fa-map-location:before,.fa-map-marked:before{content:"\f59f"}.fa-house-flood-water:before{content:"\e50e"}.fa-tree:before{content:"\f1bb"}.fa-bridge-lock:before{content:"\e4cc"}.fa-sack-dollar:before{content:"\f81d"}.fa-edit:before,.fa-pen-to-square:before{content:"\f044"}.fa-car-side:before{content:"\f5e4"}.fa-share-alt:before,.fa-share-nodes:before{content:"\f1e0"}.fa-heart-circle-minus:before{content:"\e4ff"}.fa-hourglass-2:before,.fa-hourglass-half:before{content:"\f252"}.fa-microscope:before{content:"\f610"}.fa-sink:before{content:"\e06d"}.fa-bag-shopping:before,.fa-shopping-bag:before{content:"\f290"}.fa-arrow-down-z-a:before,.fa-sort-alpha-desc:before,.fa-sort-alpha-down-alt:before{content:"\f881"}.fa-mitten:before{content:"\f7b5"}.fa-person-rays:before{content:"\e54d"}.fa-users:before{content:"\f0c0"}.fa-eye-slash:before{content:"\f070"}.fa-flask-vial:before{content:"\e4f3"}.fa-hand-paper:before,.fa-hand:before{content:"\f256"}.fa-om:before{content:"\f679"}.fa-worm:before{content:"\e599"}.fa-house-circle-xmark:before{content:"\e50b"}.fa-plug:before{content:"\f1e6"}.fa-chevron-up:before{content:"\f077"}.fa-hand-spock:before{content:"\f259"}.fa-stopwatch:before{content:"\f2f2"}.fa-face-kiss:before,.fa-kiss:before{content:"\f596"}.fa-bridge-circle-xmark:before{content:"\e4cb"}.fa-face-grin-tongue:before,.fa-grin-tongue:before{content:"\f589"}.fa-chess-bishop:before{content:"\f43a"}.fa-face-grin-wink:before,.fa-grin-wink:before{content:"\f58c"}.fa-deaf:before,.fa-deafness:before,.fa-ear-deaf:before,.fa-hard-of-hearing:before{content:"\f2a4"}.fa-road-circle-check:before{content:"\e564"}.fa-dice-five:before{content:"\f523"}.fa-rss-square:before,.fa-square-rss:before{content:"\f143"}.fa-land-mine-on:before{content:"\e51b"}.fa-i-cursor:before{content:"\f246"}.fa-stamp:before{content:"\f5bf"}.fa-stairs:before{content:"\e289"}.fa-i:before{content:"\49"}.fa-hryvnia-sign:before,.fa-hryvnia:before{content:"\f6f2"}.fa-pills:before{content:"\f484"}.fa-face-grin-wide:before,.fa-grin-alt:before{content:"\f581"}.fa-tooth:before{content:"\f5c9"}.fa-v:before{content:"\56"}.fa-bangladeshi-taka-sign:before{content:"\e2e6"}.fa-bicycle:before{content:"\f206"}.fa-rod-asclepius:before,.fa-rod-snake:before,.fa-staff-aesculapius:before,.fa-staff-snake:before{content:"\e579"}.fa-head-side-cough-slash:before{content:"\e062"}.fa-ambulance:before,.fa-truck-medical:before{content:"\f0f9"}.fa-wheat-awn-circle-exclamation:before{content:"\e598"}.fa-snowman:before{content:"\f7d0"}.fa-mortar-pestle:before{content:"\f5a7"}.fa-road-barrier:before{content:"\e562"}.fa-school:before{content:"\f549"}.fa-igloo:before{content:"\f7ae"}.fa-joint:before{content:"\f595"}.fa-angle-right:before{content:"\f105"}.fa-horse:before{content:"\f6f0"}.fa-q:before{content:"\51"}.fa-g:before{content:"\47"}.fa-notes-medical:before{content:"\f481"}.fa-temperature-2:before,.fa-temperature-half:before,.fa-thermometer-2:before,.fa-thermometer-half:before{content:"\f2c9"}.fa-dong-sign:before{content:"\e169"}.fa-capsules:before{content:"\f46b"}.fa-poo-bolt:before,.fa-poo-storm:before{content:"\f75a"}.fa-face-frown-open:before,.fa-frown-open:before{content:"\f57a"}.fa-hand-point-up:before{content:"\f0a6"}.fa-money-bill:before{content:"\f0d6"}.fa-bookmark:before{content:"\f02e"}.fa-align-justify:before{content:"\f039"}.fa-umbrella-beach:before{content:"\f5ca"}.fa-helmet-un:before{content:"\e503"}.fa-bullseye:before{content:"\f140"}.fa-bacon:before{content:"\f7e5"}.fa-hand-point-down:before{content:"\f0a7"}.fa-arrow-up-from-bracket:before{content:"\e09a"}.fa-folder-blank:before,.fa-folder:before{content:"\f07b"}.fa-file-medical-alt:before,.fa-file-waveform:before{content:"\f478"}.fa-radiation:before{content:"\f7b9"}.fa-chart-simple:before{content:"\e473"}.fa-mars-stroke:before{content:"\f229"}.fa-vial:before{content:"\f492"}.fa-dashboard:before,.fa-gauge-med:before,.fa-gauge:before,.fa-tachometer-alt-average:before{content:"\f624"}.fa-magic-wand-sparkles:before,.fa-wand-magic-sparkles:before{content:"\e2ca"}.fa-e:before{content:"\45"}.fa-pen-alt:before,.fa-pen-clip:before{content:"\f305"}.fa-bridge-circle-exclamation:before{content:"\e4ca"}.fa-user:before{content:"\f007"}.fa-school-circle-check:before{content:"\e56b"}.fa-dumpster:before{content:"\f793"}.fa-shuttle-van:before,.fa-van-shuttle:before{content:"\f5b6"}.fa-building-user:before{content:"\e4da"}.fa-caret-square-left:before,.fa-square-caret-left:before{content:"\f191"}.fa-highlighter:before{content:"\f591"}.fa-key:before{content:"\f084"}.fa-bullhorn:before{content:"\f0a1"}.fa-globe:before{content:"\f0ac"}.fa-synagogue:before{content:"\f69b"}.fa-person-half-dress:before{content:"\e548"}.fa-road-bridge:before{content:"\e563"}.fa-location-arrow:before{content:"\f124"}.fa-c:before{content:"\43"}.fa-tablet-button:before{content:"\f10a"}.fa-building-lock:before{content:"\e4d6"}.fa-pizza-slice:before{content:"\f818"}.fa-money-bill-wave:before{content:"\f53a"}.fa-area-chart:before,.fa-chart-area:before{content:"\f1fe"}.fa-house-flag:before{content:"\e50d"}.fa-person-circle-minus:before{content:"\e540"}.fa-ban:before,.fa-cancel:before{content:"\f05e"}.fa-camera-rotate:before{content:"\e0d8"}.fa-air-freshener:before,.fa-spray-can-sparkles:before{content:"\f5d0"}.fa-star:before{content:"\f005"}.fa-repeat:before{content:"\f363"}.fa-cross:before{content:"\f654"}.fa-box:before{content:"\f466"}.fa-venus-mars:before{content:"\f228"}.fa-arrow-pointer:before,.fa-mouse-pointer:before{content:"\f245"}.fa-expand-arrows-alt:before,.fa-maximize:before{content:"\f31e"}.fa-charging-station:before{content:"\f5e7"}.fa-shapes:before,.fa-triangle-circle-square:before{content:"\f61f"}.fa-random:before,.fa-shuffle:before{content:"\f074"}.fa-person-running:before,.fa-running:before{content:"\f70c"}.fa-mobile-retro:before{content:"\e527"}.fa-grip-lines-vertical:before{content:"\f7a5"}.fa-spider:before{content:"\f717"}.fa-hands-bound:before{content:"\e4f9"}.fa-file-invoice-dollar:before{content:"\f571"}.fa-plane-circle-exclamation:before{content:"\e556"}.fa-x-ray:before{content:"\f497"}.fa-spell-check:before{content:"\f891"}.fa-slash:before{content:"\f715"}.fa-computer-mouse:before,.fa-mouse:before{content:"\f8cc"}.fa-arrow-right-to-bracket:before,.fa-sign-in:before{content:"\f090"}.fa-shop-slash:before,.fa-store-alt-slash:before{content:"\e070"}.fa-server:before{content:"\f233"}.fa-virus-covid-slash:before{content:"\e4a9"}.fa-shop-lock:before{content:"\e4a5"}.fa-hourglass-1:before,.fa-hourglass-start:before{content:"\f251"}.fa-blender-phone:before{content:"\f6b6"}.fa-building-wheat:before{content:"\e4db"}.fa-person-breastfeeding:before{content:"\e53a"}.fa-right-to-bracket:before,.fa-sign-in-alt:before{content:"\f2f6"}.fa-venus:before{content:"\f221"}.fa-passport:before{content:"\f5ab"}.fa-heart-pulse:before,.fa-heartbeat:before{content:"\f21e"}.fa-people-carry-box:before,.fa-people-carry:before{content:"\f4ce"}.fa-temperature-high:before{content:"\f769"}.fa-microchip:before{content:"\f2db"}.fa-crown:before{content:"\f521"}.fa-weight-hanging:before{content:"\f5cd"}.fa-xmarks-lines:before{content:"\e59a"}.fa-file-prescription:before{content:"\f572"}.fa-weight-scale:before,.fa-weight:before{content:"\f496"}.fa-user-friends:before,.fa-user-group:before{content:"\f500"}.fa-arrow-up-a-z:before,.fa-sort-alpha-up:before{content:"\f15e"}.fa-chess-knight:before{content:"\f441"}.fa-face-laugh-squint:before,.fa-laugh-squint:before{content:"\f59b"}.fa-wheelchair:before{content:"\f193"}.fa-arrow-circle-up:before,.fa-circle-arrow-up:before{content:"\f0aa"}.fa-toggle-on:before{content:"\f205"}.fa-person-walking:before,.fa-walking:before{content:"\f554"}.fa-l:before{content:"\4c"}.fa-fire:before{content:"\f06d"}.fa-bed-pulse:before,.fa-procedures:before{content:"\f487"}.fa-shuttle-space:before,.fa-space-shuttle:before{content:"\f197"}.fa-face-laugh:before,.fa-laugh:before{content:"\f599"}.fa-folder-open:before{content:"\f07c"}.fa-heart-circle-plus:before{content:"\e500"}.fa-code-fork:before{content:"\e13b"}.fa-city:before{content:"\f64f"}.fa-microphone-alt:before,.fa-microphone-lines:before{content:"\f3c9"}.fa-pepper-hot:before{content:"\f816"}.fa-unlock:before{content:"\f09c"}.fa-colon-sign:before{content:"\e140"}.fa-headset:before{content:"\f590"}.fa-store-slash:before{content:"\e071"}.fa-road-circle-xmark:before{content:"\e566"}.fa-user-minus:before{content:"\f503"}.fa-mars-stroke-up:before,.fa-mars-stroke-v:before{content:"\f22a"}.fa-champagne-glasses:before,.fa-glass-cheers:before{content:"\f79f"}.fa-clipboard:before{content:"\f328"}.fa-house-circle-exclamation:before{content:"\e50a"}.fa-file-arrow-up:before,.fa-file-upload:before{content:"\f574"}.fa-wifi-3:before,.fa-wifi-strong:before,.fa-wifi:before{content:"\f1eb"}.fa-bath:before,.fa-bathtub:before{content:"\f2cd"}.fa-underline:before{content:"\f0cd"}.fa-user-edit:before,.fa-user-pen:before{content:"\f4ff"}.fa-signature:before{content:"\f5b7"}.fa-stroopwafel:before{content:"\f551"}.fa-bold:before{content:"\f032"}.fa-anchor-lock:before{content:"\e4ad"}.fa-building-ngo:before{content:"\e4d7"}.fa-manat-sign:before{content:"\e1d5"}.fa-not-equal:before{content:"\f53e"}.fa-border-style:before,.fa-border-top-left:before{content:"\f853"}.fa-map-location-dot:before,.fa-map-marked-alt:before{content:"\f5a0"}.fa-jedi:before{content:"\f669"}.fa-poll:before,.fa-square-poll-vertical:before{content:"\f681"}.fa-mug-hot:before{content:"\f7b6"}.fa-battery-car:before,.fa-car-battery:before{content:"\f5df"}.fa-gift:before{content:"\f06b"}.fa-dice-two:before{content:"\f528"}.fa-chess-queen:before{content:"\f445"}.fa-glasses:before{content:"\f530"}.fa-chess-board:before{content:"\f43c"}.fa-building-circle-check:before{content:"\e4d2"}.fa-person-chalkboard:before{content:"\e53d"}.fa-mars-stroke-h:before,.fa-mars-stroke-right:before{content:"\f22b"}.fa-hand-back-fist:before,.fa-hand-rock:before{content:"\f255"}.fa-caret-square-up:before,.fa-square-caret-up:before{content:"\f151"}.fa-cloud-showers-water:before{content:"\e4e4"}.fa-bar-chart:before,.fa-chart-bar:before{content:"\f080"}.fa-hands-bubbles:before,.fa-hands-wash:before{content:"\e05e"}.fa-less-than-equal:before{content:"\f537"}.fa-train:before{content:"\f238"}.fa-eye-low-vision:before,.fa-low-vision:before{content:"\f2a8"}.fa-crow:before{content:"\f520"}.fa-sailboat:before{content:"\e445"}.fa-window-restore:before{content:"\f2d2"}.fa-plus-square:before,.fa-square-plus:before{content:"\f0fe"}.fa-torii-gate:before{content:"\f6a1"}.fa-frog:before{content:"\f52e"}.fa-bucket:before{content:"\e4cf"}.fa-image:before{content:"\f03e"}.fa-microphone:before{content:"\f130"}.fa-cow:before{content:"\f6c8"}.fa-caret-up:before{content:"\f0d8"}.fa-screwdriver:before{content:"\f54a"}.fa-folder-closed:before{content:"\e185"}.fa-house-tsunami:before{content:"\e515"}.fa-square-nfi:before{content:"\e576"}.fa-arrow-up-from-ground-water:before{content:"\e4b5"}.fa-glass-martini-alt:before,.fa-martini-glass:before{content:"\f57b"}.fa-rotate-back:before,.fa-rotate-backward:before,.fa-rotate-left:before,.fa-undo-alt:before{content:"\f2ea"}.fa-columns:before,.fa-table-columns:before{content:"\f0db"}.fa-lemon:before{content:"\f094"}.fa-head-side-mask:before{content:"\e063"}.fa-handshake:before{content:"\f2b5"}.fa-gem:before{content:"\f3a5"}.fa-dolly-box:before,.fa-dolly:before{content:"\f472"}.fa-smoking:before{content:"\f48d"}.fa-compress-arrows-alt:before,.fa-minimize:before{content:"\f78c"}.fa-monument:before{content:"\f5a6"}.fa-snowplow:before{content:"\f7d2"}.fa-angle-double-right:before,.fa-angles-right:before{content:"\f101"}.fa-cannabis:before{content:"\f55f"}.fa-circle-play:before,.fa-play-circle:before{content:"\f144"}.fa-tablets:before{content:"\f490"}.fa-ethernet:before{content:"\f796"}.fa-eur:before,.fa-euro-sign:before,.fa-euro:before{content:"\f153"}.fa-chair:before{content:"\f6c0"}.fa-check-circle:before,.fa-circle-check:before{content:"\f058"}.fa-circle-stop:before,.fa-stop-circle:before{content:"\f28d"}.fa-compass-drafting:before,.fa-drafting-compass:before{content:"\f568"}.fa-plate-wheat:before{content:"\e55a"}.fa-icicles:before{content:"\f7ad"}.fa-person-shelter:before{content:"\e54f"}.fa-neuter:before{content:"\f22c"}.fa-id-badge:before{content:"\f2c1"}.fa-marker:before{content:"\f5a1"}.fa-face-laugh-beam:before,.fa-laugh-beam:before{content:"\f59a"}.fa-helicopter-symbol:before{content:"\e502"}.fa-universal-access:before{content:"\f29a"}.fa-chevron-circle-up:before,.fa-circle-chevron-up:before{content:"\f139"}.fa-lari-sign:before{content:"\e1c8"}.fa-volcano:before{content:"\f770"}.fa-person-walking-dashed-line-arrow-right:before{content:"\e553"}.fa-gbp:before,.fa-pound-sign:before,.fa-sterling-sign:before{content:"\f154"}.fa-viruses:before{content:"\e076"}.fa-square-person-confined:before{content:"\e577"}.fa-user-tie:before{content:"\f508"}.fa-arrow-down-long:before,.fa-long-arrow-down:before{content:"\f175"}.fa-tent-arrow-down-to-line:before{content:"\e57e"}.fa-certificate:before{content:"\f0a3"}.fa-mail-reply-all:before,.fa-reply-all:before{content:"\f122"}.fa-suitcase:before{content:"\f0f2"}.fa-person-skating:before,.fa-skating:before{content:"\f7c5"}.fa-filter-circle-dollar:before,.fa-funnel-dollar:before{content:"\f662"}.fa-camera-retro:before{content:"\f083"}.fa-arrow-circle-down:before,.fa-circle-arrow-down:before{content:"\f0ab"}.fa-arrow-right-to-file:before,.fa-file-import:before{content:"\f56f"}.fa-external-link-square:before,.fa-square-arrow-up-right:before{content:"\f14c"}.fa-box-open:before{content:"\f49e"}.fa-scroll:before{content:"\f70e"}.fa-spa:before{content:"\f5bb"}.fa-location-pin-lock:before{content:"\e51f"}.fa-pause:before{content:"\f04c"}.fa-hill-avalanche:before{content:"\e507"}.fa-temperature-0:before,.fa-temperature-empty:before,.fa-thermometer-0:before,.fa-thermometer-empty:before{content:"\f2cb"}.fa-bomb:before{content:"\f1e2"}.fa-registered:before{content:"\f25d"}.fa-address-card:before,.fa-contact-card:before,.fa-vcard:before{content:"\f2bb"}.fa-balance-scale-right:before,.fa-scale-unbalanced-flip:before{content:"\f516"}.fa-subscript:before{content:"\f12c"}.fa-diamond-turn-right:before,.fa-directions:before{content:"\f5eb"}.fa-burst:before{content:"\e4dc"}.fa-house-laptop:before,.fa-laptop-house:before{content:"\e066"}.fa-face-tired:before,.fa-tired:before{content:"\f5c8"}.fa-money-bills:before{content:"\e1f3"}.fa-smog:before{content:"\f75f"}.fa-crutch:before{content:"\f7f7"}.fa-cloud-arrow-up:before,.fa-cloud-upload-alt:before,.fa-cloud-upload:before{content:"\f0ee"}.fa-palette:before{content:"\f53f"}.fa-arrows-turn-right:before{content:"\e4c0"}.fa-vest:before{content:"\e085"}.fa-ferry:before{content:"\e4ea"}.fa-arrows-down-to-people:before{content:"\e4b9"}.fa-seedling:before,.fa-sprout:before{content:"\f4d8"}.fa-arrows-alt-h:before,.fa-left-right:before{content:"\f337"}.fa-boxes-packing:before{content:"\e4c7"}.fa-arrow-circle-left:before,.fa-circle-arrow-left:before{content:"\f0a8"}.fa-group-arrows-rotate:before{content:"\e4f6"}.fa-bowl-food:before{content:"\e4c6"}.fa-candy-cane:before{content:"\f786"}.fa-arrow-down-wide-short:before,.fa-sort-amount-asc:before,.fa-sort-amount-down:before{content:"\f160"}.fa-cloud-bolt:before,.fa-thunderstorm:before{content:"\f76c"}.fa-remove-format:before,.fa-text-slash:before{content:"\f87d"}.fa-face-smile-wink:before,.fa-smile-wink:before{content:"\f4da"}.fa-file-word:before{content:"\f1c2"}.fa-file-powerpoint:before{content:"\f1c4"}.fa-arrows-h:before,.fa-arrows-left-right:before{content:"\f07e"}.fa-house-lock:before{content:"\e510"}.fa-cloud-arrow-down:before,.fa-cloud-download-alt:before,.fa-cloud-download:before{content:"\f0ed"}.fa-children:before{content:"\e4e1"}.fa-blackboard:before,.fa-chalkboard:before{content:"\f51b"}.fa-user-alt-slash:before,.fa-user-large-slash:before{content:"\f4fa"}.fa-envelope-open:before{content:"\f2b6"}.fa-handshake-alt-slash:before,.fa-handshake-simple-slash:before{content:"\e05f"}.fa-mattress-pillow:before{content:"\e525"}.fa-guarani-sign:before{content:"\e19a"}.fa-arrows-rotate:before,.fa-refresh:before,.fa-sync:before{content:"\f021"}.fa-fire-extinguisher:before{content:"\f134"}.fa-cruzeiro-sign:before{content:"\e152"}.fa-greater-than-equal:before{content:"\f532"}.fa-shield-alt:before,.fa-shield-halved:before{content:"\f3ed"}.fa-atlas:before,.fa-book-atlas:before{content:"\f558"}.fa-virus:before{content:"\e074"}.fa-envelope-circle-check:before{content:"\e4e8"}.fa-layer-group:before{content:"\f5fd"}.fa-arrows-to-dot:before{content:"\e4be"}.fa-archway:before{content:"\f557"}.fa-heart-circle-check:before{content:"\e4fd"}.fa-house-chimney-crack:before,.fa-house-damage:before{content:"\f6f1"}.fa-file-archive:before,.fa-file-zipper:before{content:"\f1c6"}.fa-square:before{content:"\f0c8"}.fa-glass-martini:before,.fa-martini-glass-empty:before{content:"\f000"}.fa-couch:before{content:"\f4b8"}.fa-cedi-sign:before{content:"\e0df"}.fa-italic:before{content:"\f033"}.fa-church:before{content:"\f51d"}.fa-comments-dollar:before{content:"\f653"}.fa-democrat:before{content:"\f747"}.fa-z:before{content:"\5a"}.fa-person-skiing:before,.fa-skiing:before{content:"\f7c9"}.fa-road-lock:before{content:"\e567"}.fa-a:before{content:"\41"}.fa-temperature-arrow-down:before,.fa-temperature-down:before{content:"\e03f"}.fa-feather-alt:before,.fa-feather-pointed:before{content:"\f56b"}.fa-p:before{content:"\50"}.fa-snowflake:before{content:"\f2dc"}.fa-newspaper:before{content:"\f1ea"}.fa-ad:before,.fa-rectangle-ad:before{content:"\f641"}.fa-arrow-circle-right:before,.fa-circle-arrow-right:before{content:"\f0a9"}.fa-filter-circle-xmark:before{content:"\e17b"}.fa-locust:before{content:"\e520"}.fa-sort:before,.fa-unsorted:before{content:"\f0dc"}.fa-list-1-2:before,.fa-list-numeric:before,.fa-list-ol:before{content:"\f0cb"}.fa-person-dress-burst:before{content:"\e544"}.fa-money-check-alt:before,.fa-money-check-dollar:before{content:"\f53d"}.fa-vector-square:before{content:"\f5cb"}.fa-bread-slice:before{content:"\f7ec"}.fa-language:before{content:"\f1ab"}.fa-face-kiss-wink-heart:before,.fa-kiss-wink-heart:before{content:"\f598"}.fa-filter:before{content:"\f0b0"}.fa-question:before{content:"\3f"}.fa-file-signature:before{content:"\f573"}.fa-arrows-alt:before,.fa-up-down-left-right:before{content:"\f0b2"}.fa-house-chimney-user:before{content:"\e065"}.fa-hand-holding-heart:before{content:"\f4be"}.fa-puzzle-piece:before{content:"\f12e"}.fa-money-check:before{content:"\f53c"}.fa-star-half-alt:before,.fa-star-half-stroke:before{content:"\f5c0"}.fa-code:before{content:"\f121"}.fa-glass-whiskey:before,.fa-whiskey-glass:before{content:"\f7a0"}.fa-building-circle-exclamation:before{content:"\e4d3"}.fa-magnifying-glass-chart:before{content:"\e522"}.fa-arrow-up-right-from-square:before,.fa-external-link:before{content:"\f08e"}.fa-cubes-stacked:before{content:"\e4e6"}.fa-krw:before,.fa-won-sign:before,.fa-won:before{content:"\f159"}.fa-virus-covid:before{content:"\e4a8"}.fa-austral-sign:before{content:"\e0a9"}.fa-f:before{content:"\46"}.fa-leaf:before{content:"\f06c"}.fa-road:before{content:"\f018"}.fa-cab:before,.fa-taxi:before{content:"\f1ba"}.fa-person-circle-plus:before{content:"\e541"}.fa-chart-pie:before,.fa-pie-chart:before{content:"\f200"}.fa-bolt-lightning:before{content:"\e0b7"}.fa-sack-xmark:before{content:"\e56a"}.fa-file-excel:before{content:"\f1c3"}.fa-file-contract:before{content:"\f56c"}.fa-fish-fins:before{content:"\e4f2"}.fa-building-flag:before{content:"\e4d5"}.fa-face-grin-beam:before,.fa-grin-beam:before{content:"\f582"}.fa-object-ungroup:before{content:"\f248"}.fa-poop:before{content:"\f619"}.fa-location-pin:before,.fa-map-marker:before{content:"\f041"}.fa-kaaba:before{content:"\f66b"}.fa-toilet-paper:before{content:"\f71e"}.fa-hard-hat:before,.fa-hat-hard:before,.fa-helmet-safety:before{content:"\f807"}.fa-eject:before{content:"\f052"}.fa-arrow-alt-circle-right:before,.fa-circle-right:before{content:"\f35a"}.fa-plane-circle-check:before{content:"\e555"}.fa-face-rolling-eyes:before,.fa-meh-rolling-eyes:before{content:"\f5a5"}.fa-object-group:before{content:"\f247"}.fa-chart-line:before,.fa-line-chart:before{content:"\f201"}.fa-mask-ventilator:before{content:"\e524"}.fa-arrow-right:before{content:"\f061"}.fa-map-signs:before,.fa-signs-post:before{content:"\f277"}.fa-cash-register:before{content:"\f788"}.fa-person-circle-question:before{content:"\e542"}.fa-h:before{content:"\48"}.fa-tarp:before{content:"\e57b"}.fa-screwdriver-wrench:before,.fa-tools:before{content:"\f7d9"}.fa-arrows-to-eye:before{content:"\e4bf"}.fa-plug-circle-bolt:before{content:"\e55b"}.fa-heart:before{content:"\f004"}.fa-mars-and-venus:before{content:"\f224"}.fa-home-user:before,.fa-house-user:before{content:"\e1b0"}.fa-dumpster-fire:before{content:"\f794"}.fa-house-crack:before{content:"\e3b1"}.fa-cocktail:before,.fa-martini-glass-citrus:before{content:"\f561"}.fa-face-surprise:before,.fa-surprise:before{content:"\f5c2"}.fa-bottle-water:before{content:"\e4c5"}.fa-circle-pause:before,.fa-pause-circle:before{content:"\f28b"}.fa-toilet-paper-slash:before{content:"\e072"}.fa-apple-alt:before,.fa-apple-whole:before{content:"\f5d1"}.fa-kitchen-set:before{content:"\e51a"}.fa-r:before{content:"\52"}.fa-temperature-1:before,.fa-temperature-quarter:before,.fa-thermometer-1:before,.fa-thermometer-quarter:before{content:"\f2ca"}.fa-cube:before{content:"\f1b2"}.fa-bitcoin-sign:before{content:"\e0b4"}.fa-shield-dog:before{content:"\e573"}.fa-solar-panel:before{content:"\f5ba"}.fa-lock-open:before{content:"\f3c1"}.fa-elevator:before{content:"\e16d"}.fa-money-bill-transfer:before{content:"\e528"}.fa-money-bill-trend-up:before{content:"\e529"}.fa-house-flood-water-circle-arrow-right:before{content:"\e50f"}.fa-poll-h:before,.fa-square-poll-horizontal:before{content:"\f682"}.fa-circle:before{content:"\f111"}.fa-backward-fast:before,.fa-fast-backward:before{content:"\f049"}.fa-recycle:before{content:"\f1b8"}.fa-user-astronaut:before{content:"\f4fb"}.fa-plane-slash:before{content:"\e069"}.fa-trademark:before{content:"\f25c"}.fa-basketball-ball:before,.fa-basketball:before{content:"\f434"}.fa-satellite-dish:before{content:"\f7c0"}.fa-arrow-alt-circle-up:before,.fa-circle-up:before{content:"\f35b"}.fa-mobile-alt:before,.fa-mobile-screen-button:before{content:"\f3cd"}.fa-volume-high:before,.fa-volume-up:before{content:"\f028"}.fa-users-rays:before{content:"\e593"}.fa-wallet:before{content:"\f555"}.fa-clipboard-check:before{content:"\f46c"}.fa-file-audio:before{content:"\f1c7"}.fa-burger:before,.fa-hamburger:before{content:"\f805"}.fa-wrench:before{content:"\f0ad"}.fa-bugs:before{content:"\e4d0"}.fa-rupee-sign:before,.fa-rupee:before{content:"\f156"}.fa-file-image:before{content:"\f1c5"}.fa-circle-question:before,.fa-question-circle:before{content:"\f059"}.fa-plane-departure:before{content:"\f5b0"}.fa-handshake-slash:before{content:"\e060"}.fa-book-bookmark:before{content:"\e0bb"}.fa-code-branch:before{content:"\f126"}.fa-hat-cowboy:before{content:"\f8c0"}.fa-bridge:before{content:"\e4c8"}.fa-phone-alt:before,.fa-phone-flip:before{content:"\f879"}.fa-truck-front:before{content:"\e2b7"}.fa-cat:before{content:"\f6be"}.fa-anchor-circle-exclamation:before{content:"\e4ab"}.fa-truck-field:before{content:"\e58d"}.fa-route:before{content:"\f4d7"}.fa-clipboard-question:before{content:"\e4e3"}.fa-panorama:before{content:"\e209"}.fa-comment-medical:before{content:"\f7f5"}.fa-teeth-open:before{content:"\f62f"}.fa-file-circle-minus:before{content:"\e4ed"}.fa-tags:before{content:"\f02c"}.fa-wine-glass:before{content:"\f4e3"}.fa-fast-forward:before,.fa-forward-fast:before{content:"\f050"}.fa-face-meh-blank:before,.fa-meh-blank:before{content:"\f5a4"}.fa-parking:before,.fa-square-parking:before{content:"\f540"}.fa-house-signal:before{content:"\e012"}.fa-bars-progress:before,.fa-tasks-alt:before{content:"\f828"}.fa-faucet-drip:before{content:"\e006"}.fa-cart-flatbed:before,.fa-dolly-flatbed:before{content:"\f474"}.fa-ban-smoking:before,.fa-smoking-ban:before{content:"\f54d"}.fa-terminal:before{content:"\f120"}.fa-mobile-button:before{content:"\f10b"}.fa-house-medical-flag:before{content:"\e514"}.fa-basket-shopping:before,.fa-shopping-basket:before{content:"\f291"}.fa-tape:before{content:"\f4db"}.fa-bus-alt:before,.fa-bus-simple:before{content:"\f55e"}.fa-eye:before{content:"\f06e"}.fa-face-sad-cry:before,.fa-sad-cry:before{content:"\f5b3"}.fa-audio-description:before{content:"\f29e"}.fa-person-military-to-person:before{content:"\e54c"}.fa-file-shield:before{content:"\e4f0"}.fa-user-slash:before{content:"\f506"}.fa-pen:before{content:"\f304"}.fa-tower-observation:before{content:"\e586"}.fa-file-code:before{content:"\f1c9"}.fa-signal-5:before,.fa-signal-perfect:before,.fa-signal:before{content:"\f012"}.fa-bus:before{content:"\f207"}.fa-heart-circle-xmark:before{content:"\e501"}.fa-home-lg:before,.fa-house-chimney:before{content:"\e3af"}.fa-window-maximize:before{content:"\f2d0"}.fa-face-frown:before,.fa-frown:before{content:"\f119"}.fa-prescription:before{content:"\f5b1"}.fa-shop:before,.fa-store-alt:before{content:"\f54f"}.fa-floppy-disk:before,.fa-save:before{content:"\f0c7"}.fa-vihara:before{content:"\f6a7"}.fa-balance-scale-left:before,.fa-scale-unbalanced:before{content:"\f515"}.fa-sort-asc:before,.fa-sort-up:before{content:"\f0de"}.fa-comment-dots:before,.fa-commenting:before{content:"\f4ad"}.fa-plant-wilt:before{content:"\e5aa"}.fa-diamond:before{content:"\f219"}.fa-face-grin-squint:before,.fa-grin-squint:before{content:"\f585"}.fa-hand-holding-dollar:before,.fa-hand-holding-usd:before{content:"\f4c0"}.fa-bacterium:before{content:"\e05a"}.fa-hand-pointer:before{content:"\f25a"}.fa-drum-steelpan:before{content:"\f56a"}.fa-hand-scissors:before{content:"\f257"}.fa-hands-praying:before,.fa-praying-hands:before{content:"\f684"}.fa-arrow-right-rotate:before,.fa-arrow-rotate-forward:before,.fa-arrow-rotate-right:before,.fa-redo:before{content:"\f01e"}.fa-biohazard:before{content:"\f780"}.fa-location-crosshairs:before,.fa-location:before{content:"\f601"}.fa-mars-double:before{content:"\f227"}.fa-child-dress:before{content:"\e59c"}.fa-users-between-lines:before{content:"\e591"}.fa-lungs-virus:before{content:"\e067"}.fa-face-grin-tears:before,.fa-grin-tears:before{content:"\f588"}.fa-phone:before{content:"\f095"}.fa-calendar-times:before,.fa-calendar-xmark:before{content:"\f273"}.fa-child-reaching:before{content:"\e59d"}.fa-head-side-virus:before{content:"\e064"}.fa-user-cog:before,.fa-user-gear:before{content:"\f4fe"}.fa-arrow-up-1-9:before,.fa-sort-numeric-up:before{content:"\f163"}.fa-door-closed:before{content:"\f52a"}.fa-shield-virus:before{content:"\e06c"}.fa-dice-six:before{content:"\f526"}.fa-mosquito-net:before{content:"\e52c"}.fa-bridge-water:before{content:"\e4ce"}.fa-person-booth:before{content:"\f756"}.fa-text-width:before{content:"\f035"}.fa-hat-wizard:before{content:"\f6e8"}.fa-pen-fancy:before{content:"\f5ac"}.fa-digging:before,.fa-person-digging:before{content:"\f85e"}.fa-trash:before{content:"\f1f8"}.fa-gauge-simple-med:before,.fa-gauge-simple:before,.fa-tachometer-average:before{content:"\f629"}.fa-book-medical:before{content:"\f7e6"}.fa-poo:before{content:"\f2fe"}.fa-quote-right-alt:before,.fa-quote-right:before{content:"\f10e"}.fa-shirt:before,.fa-t-shirt:before,.fa-tshirt:before{content:"\f553"}.fa-cubes:before{content:"\f1b3"}.fa-divide:before{content:"\f529"}.fa-tenge-sign:before,.fa-tenge:before{content:"\f7d7"}.fa-headphones:before{content:"\f025"}.fa-hands-holding:before{content:"\f4c2"}.fa-hands-clapping:before{content:"\e1a8"}.fa-republican:before{content:"\f75e"}.fa-arrow-left:before{content:"\f060"}.fa-person-circle-xmark:before{content:"\e543"}.fa-ruler:before{content:"\f545"}.fa-align-left:before{content:"\f036"}.fa-dice-d6:before{content:"\f6d1"}.fa-restroom:before{content:"\f7bd"}.fa-j:before{content:"\4a"}.fa-users-viewfinder:before{content:"\e595"}.fa-file-video:before{content:"\f1c8"}.fa-external-link-alt:before,.fa-up-right-from-square:before{content:"\f35d"}.fa-table-cells:before,.fa-th:before{content:"\f00a"}.fa-file-pdf:before{content:"\f1c1"}.fa-bible:before,.fa-book-bible:before{content:"\f647"}.fa-o:before{content:"\4f"}.fa-medkit:before,.fa-suitcase-medical:before{content:"\f0fa"}.fa-user-secret:before{content:"\f21b"}.fa-otter:before{content:"\f700"}.fa-female:before,.fa-person-dress:before{content:"\f182"}.fa-comment-dollar:before{content:"\f651"}.fa-briefcase-clock:before,.fa-business-time:before{content:"\f64a"}.fa-table-cells-large:before,.fa-th-large:before{content:"\f009"}.fa-book-tanakh:before,.fa-tanakh:before{content:"\f827"}.fa-phone-volume:before,.fa-volume-control-phone:before{content:"\f2a0"}.fa-hat-cowboy-side:before{content:"\f8c1"}.fa-clipboard-user:before{content:"\f7f3"}.fa-child:before{content:"\f1ae"}.fa-lira-sign:before{content:"\f195"}.fa-satellite:before{content:"\f7bf"}.fa-plane-lock:before{content:"\e558"}.fa-tag:before{content:"\f02b"}.fa-comment:before{content:"\f075"}.fa-birthday-cake:before,.fa-cake-candles:before,.fa-cake:before{content:"\f1fd"}.fa-envelope:before{content:"\f0e0"}.fa-angle-double-up:before,.fa-angles-up:before{content:"\f102"}.fa-paperclip:before{content:"\f0c6"}.fa-arrow-right-to-city:before{content:"\e4b3"}.fa-ribbon:before{content:"\f4d6"}.fa-lungs:before{content:"\f604"}.fa-arrow-up-9-1:before,.fa-sort-numeric-up-alt:before{content:"\f887"}.fa-litecoin-sign:before{content:"\e1d3"}.fa-border-none:before{content:"\f850"}.fa-circle-nodes:before{content:"\e4e2"}.fa-parachute-box:before{content:"\f4cd"}.fa-indent:before{content:"\f03c"}.fa-truck-field-un:before{content:"\e58e"}.fa-hourglass-empty:before,.fa-hourglass:before{content:"\f254"}.fa-mountain:before{content:"\f6fc"}.fa-user-doctor:before,.fa-user-md:before{content:"\f0f0"}.fa-circle-info:before,.fa-info-circle:before{content:"\f05a"}.fa-cloud-meatball:before{content:"\f73b"}.fa-camera-alt:before,.fa-camera:before{content:"\f030"}.fa-square-virus:before{content:"\e578"}.fa-meteor:before{content:"\f753"}.fa-car-on:before{content:"\e4dd"}.fa-sleigh:before{content:"\f7cc"}.fa-arrow-down-1-9:before,.fa-sort-numeric-asc:before,.fa-sort-numeric-down:before{content:"\f162"}.fa-hand-holding-droplet:before,.fa-hand-holding-water:before{content:"\f4c1"}.fa-water:before{content:"\f773"}.fa-calendar-check:before{content:"\f274"}.fa-braille:before{content:"\f2a1"}.fa-prescription-bottle-alt:before,.fa-prescription-bottle-medical:before{content:"\f486"}.fa-landmark:before{content:"\f66f"}.fa-truck:before{content:"\f0d1"}.fa-crosshairs:before{content:"\f05b"}.fa-person-cane:before{content:"\e53c"}.fa-tent:before{content:"\e57d"}.fa-vest-patches:before{content:"\e086"}.fa-check-double:before{content:"\f560"}.fa-arrow-down-a-z:before,.fa-sort-alpha-asc:before,.fa-sort-alpha-down:before{content:"\f15d"}.fa-money-bill-wheat:before{content:"\e52a"}.fa-cookie:before{content:"\f563"}.fa-arrow-left-rotate:before,.fa-arrow-rotate-back:before,.fa-arrow-rotate-backward:before,.fa-arrow-rotate-left:before,.fa-undo:before{content:"\f0e2"}.fa-hard-drive:before,.fa-hdd:before{content:"\f0a0"}.fa-face-grin-squint-tears:before,.fa-grin-squint-tears:before{content:"\f586"}.fa-dumbbell:before{content:"\f44b"}.fa-list-alt:before,.fa-rectangle-list:before{content:"\f022"}.fa-tarp-droplet:before{content:"\e57c"}.fa-house-medical-circle-check:before{content:"\e511"}.fa-person-skiing-nordic:before,.fa-skiing-nordic:before{content:"\f7ca"}.fa-calendar-plus:before{content:"\f271"}.fa-plane-arrival:before{content:"\f5af"}.fa-arrow-alt-circle-left:before,.fa-circle-left:before{content:"\f359"}.fa-subway:before,.fa-train-subway:before{content:"\f239"}.fa-chart-gantt:before{content:"\e0e4"}.fa-indian-rupee-sign:before,.fa-indian-rupee:before,.fa-inr:before{content:"\e1bc"}.fa-crop-alt:before,.fa-crop-simple:before{content:"\f565"}.fa-money-bill-1:before,.fa-money-bill-alt:before{content:"\f3d1"}.fa-left-long:before,.fa-long-arrow-alt-left:before{content:"\f30a"}.fa-dna:before{content:"\f471"}.fa-virus-slash:before{content:"\e075"}.fa-minus:before,.fa-subtract:before{content:"\f068"}.fa-chess:before{content:"\f439"}.fa-arrow-left-long:before,.fa-long-arrow-left:before{content:"\f177"}.fa-plug-circle-check:before{content:"\e55c"}.fa-street-view:before{content:"\f21d"}.fa-franc-sign:before{content:"\e18f"}.fa-volume-off:before{content:"\f026"}.fa-american-sign-language-interpreting:before,.fa-asl-interpreting:before,.fa-hands-american-sign-language-interpreting:before,.fa-hands-asl-interpreting:before{content:"\f2a3"}.fa-cog:before,.fa-gear:before{content:"\f013"}.fa-droplet-slash:before,.fa-tint-slash:before{content:"\f5c7"}.fa-mosque:before{content:"\f678"}.fa-mosquito:before{content:"\e52b"}.fa-star-of-david:before{content:"\f69a"}.fa-person-military-rifle:before{content:"\e54b"}.fa-cart-shopping:before,.fa-shopping-cart:before{content:"\f07a"}.fa-vials:before{content:"\f493"}.fa-plug-circle-plus:before{content:"\e55f"}.fa-place-of-worship:before{content:"\f67f"}.fa-grip-vertical:before{content:"\f58e"}.fa-arrow-turn-up:before,.fa-level-up:before{content:"\f148"}.fa-u:before{content:"\55"}.fa-square-root-alt:before,.fa-square-root-variable:before{content:"\f698"}.fa-clock-four:before,.fa-clock:before{content:"\f017"}.fa-backward-step:before,.fa-step-backward:before{content:"\f048"}.fa-pallet:before{content:"\f482"}.fa-faucet:before{content:"\e005"}.fa-baseball-bat-ball:before{content:"\f432"}.fa-s:before{content:"\53"}.fa-timeline:before{content:"\e29c"}.fa-keyboard:before{content:"\f11c"}.fa-caret-down:before{content:"\f0d7"}.fa-clinic-medical:before,.fa-house-chimney-medical:before{content:"\f7f2"}.fa-temperature-3:before,.fa-temperature-three-quarters:before,.fa-thermometer-3:before,.fa-thermometer-three-quarters:before{content:"\f2c8"}.fa-mobile-android-alt:before,.fa-mobile-screen:before{content:"\f3cf"}.fa-plane-up:before{content:"\e22d"}.fa-piggy-bank:before{content:"\f4d3"}.fa-battery-3:before,.fa-battery-half:before{content:"\f242"}.fa-mountain-city:before{content:"\e52e"}.fa-coins:before{content:"\f51e"}.fa-khanda:before{content:"\f66d"}.fa-sliders-h:before,.fa-sliders:before{content:"\f1de"}.fa-folder-tree:before{content:"\f802"}.fa-network-wired:before{content:"\f6ff"}.fa-map-pin:before{content:"\f276"}.fa-hamsa:before{content:"\f665"}.fa-cent-sign:before{content:"\e3f5"}.fa-flask:before{content:"\f0c3"}.fa-person-pregnant:before{content:"\e31e"}.fa-wand-sparkles:before{content:"\f72b"}.fa-ellipsis-v:before,.fa-ellipsis-vertical:before{content:"\f142"}.fa-ticket:before{content:"\f145"}.fa-power-off:before{content:"\f011"}.fa-long-arrow-alt-right:before,.fa-right-long:before{content:"\f30b"}.fa-flag-usa:before{content:"\f74d"}.fa-laptop-file:before{content:"\e51d"}.fa-teletype:before,.fa-tty:before{content:"\f1e4"}.fa-diagram-next:before{content:"\e476"}.fa-person-rifle:before{content:"\e54e"}.fa-house-medical-circle-exclamation:before{content:"\e512"}.fa-closed-captioning:before{content:"\f20a"}.fa-hiking:before,.fa-person-hiking:before{content:"\f6ec"}.fa-venus-double:before{content:"\f226"}.fa-images:before{content:"\f302"}.fa-calculator:before{content:"\f1ec"}.fa-people-pulling:before{content:"\e535"}.fa-n:before{content:"\4e"}.fa-cable-car:before,.fa-tram:before{content:"\f7da"}.fa-cloud-rain:before{content:"\f73d"}.fa-building-circle-xmark:before{content:"\e4d4"}.fa-ship:before{content:"\f21a"}.fa-arrows-down-to-line:before{content:"\e4b8"}.fa-download:before{content:"\f019"}.fa-face-grin:before,.fa-grin:before{content:"\f580"}.fa-backspace:before,.fa-delete-left:before{content:"\f55a"}.fa-eye-dropper-empty:before,.fa-eye-dropper:before,.fa-eyedropper:before{content:"\f1fb"}.fa-file-circle-check:before{content:"\e5a0"}.fa-forward:before{content:"\f04e"}.fa-mobile-android:before,.fa-mobile-phone:before,.fa-mobile:before{content:"\f3ce"}.fa-face-meh:before,.fa-meh:before{content:"\f11a"}.fa-align-center:before{content:"\f037"}.fa-book-dead:before,.fa-book-skull:before{content:"\f6b7"}.fa-drivers-license:before,.fa-id-card:before{content:"\f2c2"}.fa-dedent:before,.fa-outdent:before{content:"\f03b"}.fa-heart-circle-exclamation:before{content:"\e4fe"}.fa-home-alt:before,.fa-home-lg-alt:before,.fa-home:before,.fa-house:before{content:"\f015"}.fa-calendar-week:before{content:"\f784"}.fa-laptop-medical:before{content:"\f812"}.fa-b:before{content:"\42"}.fa-file-medical:before{content:"\f477"}.fa-dice-one:before{content:"\f525"}.fa-kiwi-bird:before{content:"\f535"}.fa-arrow-right-arrow-left:before,.fa-exchange:before{content:"\f0ec"}.fa-redo-alt:before,.fa-rotate-forward:before,.fa-rotate-right:before{content:"\f2f9"}.fa-cutlery:before,.fa-utensils:before{content:"\f2e7"}.fa-arrow-up-wide-short:before,.fa-sort-amount-up:before{content:"\f161"}.fa-mill-sign:before{content:"\e1ed"}.fa-bowl-rice:before{content:"\e2eb"}.fa-skull:before{content:"\f54c"}.fa-broadcast-tower:before,.fa-tower-broadcast:before{content:"\f519"}.fa-truck-pickup:before{content:"\f63c"}.fa-long-arrow-alt-up:before,.fa-up-long:before{content:"\f30c"}.fa-stop:before{content:"\f04d"}.fa-code-merge:before{content:"\f387"}.fa-upload:before{content:"\f093"}.fa-hurricane:before{content:"\f751"}.fa-mound:before{content:"\e52d"}.fa-toilet-portable:before{content:"\e583"}.fa-compact-disc:before{content:"\f51f"}.fa-file-arrow-down:before,.fa-file-download:before{content:"\f56d"}.fa-caravan:before{content:"\f8ff"}.fa-shield-cat:before{content:"\e572"}.fa-bolt:before,.fa-zap:before{content:"\f0e7"}.fa-glass-water:before{content:"\e4f4"}.fa-oil-well:before{content:"\e532"}.fa-vault:before{content:"\e2c5"}.fa-mars:before{content:"\f222"}.fa-toilet:before{content:"\f7d8"}.fa-plane-circle-xmark:before{content:"\e557"}.fa-cny:before,.fa-jpy:before,.fa-rmb:before,.fa-yen-sign:before,.fa-yen:before{content:"\f157"}.fa-rouble:before,.fa-rub:before,.fa-ruble-sign:before,.fa-ruble:before{content:"\f158"}.fa-sun:before{content:"\f185"}.fa-guitar:before{content:"\f7a6"}.fa-face-laugh-wink:before,.fa-laugh-wink:before{content:"\f59c"}.fa-horse-head:before{content:"\f7ab"}.fa-bore-hole:before{content:"\e4c3"}.fa-industry:before{content:"\f275"}.fa-arrow-alt-circle-down:before,.fa-circle-down:before{content:"\f358"}.fa-arrows-turn-to-dots:before{content:"\e4c1"}.fa-florin-sign:before{content:"\e184"}.fa-arrow-down-short-wide:before,.fa-sort-amount-desc:before,.fa-sort-amount-down-alt:before{content:"\f884"}.fa-less-than:before{content:"\3c"}.fa-angle-down:before{content:"\f107"}.fa-car-tunnel:before{content:"\e4de"}.fa-head-side-cough:before{content:"\e061"}.fa-grip-lines:before{content:"\f7a4"}.fa-thumbs-down:before{content:"\f165"}.fa-user-lock:before{content:"\f502"}.fa-arrow-right-long:before,.fa-long-arrow-right:before{content:"\f178"}.fa-anchor-circle-xmark:before{content:"\e4ac"}.fa-ellipsis-h:before,.fa-ellipsis:before{content:"\f141"}.fa-chess-pawn:before{content:"\f443"}.fa-first-aid:before,.fa-kit-medical:before{content:"\f479"}.fa-person-through-window:before{content:"\e5a9"}.fa-toolbox:before{content:"\f552"}.fa-hands-holding-circle:before{content:"\e4fb"}.fa-bug:before{content:"\f188"}.fa-credit-card-alt:before,.fa-credit-card:before{content:"\f09d"}.fa-automobile:before,.fa-car:before{content:"\f1b9"}.fa-hand-holding-hand:before{content:"\e4f7"}.fa-book-open-reader:before,.fa-book-reader:before{content:"\f5da"}.fa-mountain-sun:before{content:"\e52f"}.fa-arrows-left-right-to-line:before{content:"\e4ba"}.fa-dice-d20:before{content:"\f6cf"}.fa-truck-droplet:before{content:"\e58c"}.fa-file-circle-xmark:before{content:"\e5a1"}.fa-temperature-arrow-up:before,.fa-temperature-up:before{content:"\e040"}.fa-medal:before{content:"\f5a2"}.fa-bed:before{content:"\f236"}.fa-h-square:before,.fa-square-h:before{content:"\f0fd"}.fa-podcast:before{content:"\f2ce"}.fa-temperature-4:before,.fa-temperature-full:before,.fa-thermometer-4:before,.fa-thermometer-full:before{content:"\f2c7"}.fa-bell:before{content:"\f0f3"}.fa-superscript:before{content:"\f12b"}.fa-plug-circle-xmark:before{content:"\e560"}.fa-star-of-life:before{content:"\f621"}.fa-phone-slash:before{content:"\f3dd"}.fa-paint-roller:before{content:"\f5aa"}.fa-hands-helping:before,.fa-handshake-angle:before{content:"\f4c4"}.fa-location-dot:before,.fa-map-marker-alt:before{content:"\f3c5"}.fa-file:before{content:"\f15b"}.fa-greater-than:before{content:"\3e"}.fa-person-swimming:before,.fa-swimmer:before{content:"\f5c4"}.fa-arrow-down:before{content:"\f063"}.fa-droplet:before,.fa-tint:before{content:"\f043"}.fa-eraser:before{content:"\f12d"}.fa-earth-america:before,.fa-earth-americas:before,.fa-earth:before,.fa-globe-americas:before{content:"\f57d"}.fa-person-burst:before{content:"\e53b"}.fa-dove:before{content:"\f4ba"}.fa-battery-0:before,.fa-battery-empty:before{content:"\f244"}.fa-socks:before{content:"\f696"}.fa-inbox:before{content:"\f01c"}.fa-section:before{content:"\e447"}.fa-gauge-high:before,.fa-tachometer-alt-fast:before,.fa-tachometer-alt:before{content:"\f625"}.fa-envelope-open-text:before{content:"\f658"}.fa-hospital-alt:before,.fa-hospital-wide:before,.fa-hospital:before{content:"\f0f8"}.fa-wine-bottle:before{content:"\f72f"}.fa-chess-rook:before{content:"\f447"}.fa-bars-staggered:before,.fa-reorder:before,.fa-stream:before{content:"\f550"}.fa-dharmachakra:before{content:"\f655"}.fa-hotdog:before{content:"\f80f"}.fa-blind:before,.fa-person-walking-with-cane:before{content:"\f29d"}.fa-drum:before{content:"\f569"}.fa-ice-cream:before{content:"\f810"}.fa-heart-circle-bolt:before{content:"\e4fc"}.fa-fax:before{content:"\f1ac"}.fa-paragraph:before{content:"\f1dd"}.fa-check-to-slot:before,.fa-vote-yea:before{content:"\f772"}.fa-star-half:before{content:"\f089"}.fa-boxes-alt:before,.fa-boxes-stacked:before,.fa-boxes:before{content:"\f468"}.fa-chain:before,.fa-link:before{content:"\f0c1"}.fa-assistive-listening-systems:before,.fa-ear-listen:before{content:"\f2a2"}.fa-tree-city:before{content:"\e587"}.fa-play:before{content:"\f04b"}.fa-font:before{content:"\f031"}.fa-rupiah-sign:before{content:"\e23d"}.fa-magnifying-glass:before,.fa-search:before{content:"\f002"}.fa-ping-pong-paddle-ball:before,.fa-table-tennis-paddle-ball:before,.fa-table-tennis:before{content:"\f45d"}.fa-diagnoses:before,.fa-person-dots-from-line:before{content:"\f470"}.fa-trash-can-arrow-up:before,.fa-trash-restore-alt:before{content:"\f82a"}.fa-naira-sign:before{content:"\e1f6"}.fa-cart-arrow-down:before{content:"\f218"}.fa-walkie-talkie:before{content:"\f8ef"}.fa-file-edit:before,.fa-file-pen:before{content:"\f31c"}.fa-receipt:before{content:"\f543"}.fa-pen-square:before,.fa-pencil-square:before,.fa-square-pen:before{content:"\f14b"}.fa-suitcase-rolling:before{content:"\f5c1"}.fa-person-circle-exclamation:before{content:"\e53f"}.fa-chevron-down:before{content:"\f078"}.fa-battery-5:before,.fa-battery-full:before,.fa-battery:before{content:"\f240"}.fa-skull-crossbones:before{content:"\f714"}.fa-code-compare:before{content:"\e13a"}.fa-list-dots:before,.fa-list-ul:before{content:"\f0ca"}.fa-school-lock:before{content:"\e56f"}.fa-tower-cell:before{content:"\e585"}.fa-down-long:before,.fa-long-arrow-alt-down:before{content:"\f309"}.fa-ranking-star:before{content:"\e561"}.fa-chess-king:before{content:"\f43f"}.fa-person-harassing:before{content:"\e549"}.fa-brazilian-real-sign:before{content:"\e46c"}.fa-landmark-alt:before,.fa-landmark-dome:before{content:"\f752"}.fa-arrow-up:before{content:"\f062"}.fa-television:before,.fa-tv-alt:before,.fa-tv:before{content:"\f26c"}.fa-shrimp:before{content:"\e448"}.fa-list-check:before,.fa-tasks:before{content:"\f0ae"}.fa-jug-detergent:before{content:"\e519"}.fa-circle-user:before,.fa-user-circle:before{content:"\f2bd"}.fa-user-shield:before{content:"\f505"}.fa-wind:before{content:"\f72e"}.fa-car-burst:before,.fa-car-crash:before{content:"\f5e1"}.fa-y:before{content:"\59"}.fa-person-snowboarding:before,.fa-snowboarding:before{content:"\f7ce"}.fa-shipping-fast:before,.fa-truck-fast:before{content:"\f48b"}.fa-fish:before{content:"\f578"}.fa-user-graduate:before{content:"\f501"}.fa-adjust:before,.fa-circle-half-stroke:before{content:"\f042"}.fa-clapperboard:before{content:"\e131"}.fa-circle-radiation:before,.fa-radiation-alt:before{content:"\f7ba"}.fa-baseball-ball:before,.fa-baseball:before{content:"\f433"}.fa-jet-fighter-up:before{content:"\e518"}.fa-diagram-project:before,.fa-project-diagram:before{content:"\f542"}.fa-copy:before{content:"\f0c5"}.fa-volume-mute:before,.fa-volume-times:before,.fa-volume-xmark:before{content:"\f6a9"}.fa-hand-sparkles:before{content:"\e05d"}.fa-grip-horizontal:before,.fa-grip:before{content:"\f58d"}.fa-share-from-square:before,.fa-share-square:before{content:"\f14d"}.fa-child-combatant:before,.fa-child-rifle:before{content:"\e4e0"}.fa-gun:before{content:"\e19b"}.fa-phone-square:before,.fa-square-phone:before{content:"\f098"}.fa-add:before,.fa-plus:before{content:"\2b"}.fa-expand:before{content:"\f065"}.fa-computer:before{content:"\e4e5"}.fa-close:before,.fa-multiply:before,.fa-remove:before,.fa-times:before,.fa-xmark:before{content:"\f00d"}.fa-arrows-up-down-left-right:before,.fa-arrows:before{content:"\f047"}.fa-chalkboard-teacher:before,.fa-chalkboard-user:before{content:"\f51c"}.fa-peso-sign:before{content:"\e222"}.fa-building-shield:before{content:"\e4d8"}.fa-baby:before{content:"\f77c"}.fa-users-line:before{content:"\e592"}.fa-quote-left-alt:before,.fa-quote-left:before{content:"\f10d"}.fa-tractor:before{content:"\f722"}.fa-trash-arrow-up:before,.fa-trash-restore:before{content:"\f829"}.fa-arrow-down-up-lock:before{content:"\e4b0"}.fa-lines-leaning:before{content:"\e51e"}.fa-ruler-combined:before{content:"\f546"}.fa-copyright:before{content:"\f1f9"}.fa-equals:before{content:"\3d"}.fa-blender:before{content:"\f517"}.fa-teeth:before{content:"\f62e"}.fa-ils:before,.fa-shekel-sign:before,.fa-shekel:before,.fa-sheqel-sign:before,.fa-sheqel:before{content:"\f20b"}.fa-map:before{content:"\f279"}.fa-rocket:before{content:"\f135"}.fa-photo-film:before,.fa-photo-video:before{content:"\f87c"}.fa-folder-minus:before{content:"\f65d"}.fa-store:before{content:"\f54e"}.fa-arrow-trend-up:before{content:"\e098"}.fa-plug-circle-minus:before{content:"\e55e"}.fa-sign-hanging:before,.fa-sign:before{content:"\f4d9"}.fa-bezier-curve:before{content:"\f55b"}.fa-bell-slash:before{content:"\f1f6"}.fa-tablet-android:before,.fa-tablet:before{content:"\f3fb"}.fa-school-flag:before{content:"\e56e"}.fa-fill:before{content:"\f575"}.fa-angle-up:before{content:"\f106"}.fa-drumstick-bite:before{content:"\f6d7"}.fa-holly-berry:before{content:"\f7aa"}.fa-chevron-left:before{content:"\f053"}.fa-bacteria:before{content:"\e059"}.fa-hand-lizard:before{content:"\f258"}.fa-notdef:before{content:"\e1fe"}.fa-disease:before{content:"\f7fa"}.fa-briefcase-medical:before{content:"\f469"}.fa-genderless:before{content:"\f22d"}.fa-chevron-right:before{content:"\f054"}.fa-retweet:before{content:"\f079"}.fa-car-alt:before,.fa-car-rear:before{content:"\f5de"}.fa-pump-soap:before{content:"\e06b"}.fa-video-slash:before{content:"\f4e2"}.fa-battery-2:before,.fa-battery-quarter:before{content:"\f243"}.fa-radio:before{content:"\f8d7"}.fa-baby-carriage:before,.fa-carriage-baby:before{content:"\f77d"}.fa-traffic-light:before{content:"\f637"}.fa-thermometer:before{content:"\f491"}.fa-vr-cardboard:before{content:"\f729"}.fa-hand-middle-finger:before{content:"\f806"}.fa-percent:before,.fa-percentage:before{content:"\25"}.fa-truck-moving:before{content:"\f4df"}.fa-glass-water-droplet:before{content:"\e4f5"}.fa-display:before{content:"\e163"}.fa-face-smile:before,.fa-smile:before{content:"\f118"}.fa-thumb-tack:before,.fa-thumbtack:before{content:"\f08d"}.fa-trophy:before{content:"\f091"}.fa-person-praying:before,.fa-pray:before{content:"\f683"}.fa-hammer:before{content:"\f6e3"}.fa-hand-peace:before{content:"\f25b"}.fa-rotate:before,.fa-sync-alt:before{content:"\f2f1"}.fa-spinner:before{content:"\f110"}.fa-robot:before{content:"\f544"}.fa-peace:before{content:"\f67c"}.fa-cogs:before,.fa-gears:before{content:"\f085"}.fa-warehouse:before{content:"\f494"}.fa-arrow-up-right-dots:before{content:"\e4b7"}.fa-splotch:before{content:"\f5bc"}.fa-face-grin-hearts:before,.fa-grin-hearts:before{content:"\f584"}.fa-dice-four:before{content:"\f524"}.fa-sim-card:before{content:"\f7c4"}.fa-transgender-alt:before,.fa-transgender:before{content:"\f225"}.fa-mercury:before{content:"\f223"}.fa-arrow-turn-down:before,.fa-level-down:before{content:"\f149"}.fa-person-falling-burst:before{content:"\e547"}.fa-award:before{content:"\f559"}.fa-ticket-alt:before,.fa-ticket-simple:before{content:"\f3ff"}.fa-building:before{content:"\f1ad"}.fa-angle-double-left:before,.fa-angles-left:before{content:"\f100"}.fa-qrcode:before{content:"\f029"}.fa-clock-rotate-left:before,.fa-history:before{content:"\f1da"}.fa-face-grin-beam-sweat:before,.fa-grin-beam-sweat:before{content:"\f583"}.fa-arrow-right-from-file:before,.fa-file-export:before{content:"\f56e"}.fa-shield-blank:before,.fa-shield:before{content:"\f132"}.fa-arrow-up-short-wide:before,.fa-sort-amount-up-alt:before{content:"\f885"}.fa-house-medical:before{content:"\e3b2"}.fa-golf-ball-tee:before,.fa-golf-ball:before{content:"\f450"}.fa-chevron-circle-left:before,.fa-circle-chevron-left:before{content:"\f137"}.fa-house-chimney-window:before{content:"\e00d"}.fa-pen-nib:before{content:"\f5ad"}.fa-tent-arrow-turn-left:before{content:"\e580"}.fa-tents:before{content:"\e582"}.fa-magic:before,.fa-wand-magic:before{content:"\f0d0"}.fa-dog:before{content:"\f6d3"}.fa-carrot:before{content:"\f787"}.fa-moon:before{content:"\f186"}.fa-wine-glass-alt:before,.fa-wine-glass-empty:before{content:"\f5ce"}.fa-cheese:before{content:"\f7ef"}.fa-yin-yang:before{content:"\f6ad"}.fa-music:before{content:"\f001"}.fa-code-commit:before{content:"\f386"}.fa-temperature-low:before{content:"\f76b"}.fa-biking:before,.fa-person-biking:before{content:"\f84a"}.fa-broom:before{content:"\f51a"}.fa-shield-heart:before{content:"\e574"}.fa-gopuram:before{content:"\f664"}.fa-earth-oceania:before,.fa-globe-oceania:before{content:"\e47b"}.fa-square-xmark:before,.fa-times-square:before,.fa-xmark-square:before{content:"\f2d3"}.fa-hashtag:before{content:"\23"}.fa-expand-alt:before,.fa-up-right-and-down-left-from-center:before{content:"\f424"}.fa-oil-can:before{content:"\f613"}.fa-t:before{content:"\54"}.fa-hippo:before{content:"\f6ed"}.fa-chart-column:before{content:"\e0e3"}.fa-infinity:before{content:"\f534"}.fa-vial-circle-check:before{content:"\e596"}.fa-person-arrow-down-to-line:before{content:"\e538"}.fa-voicemail:before{content:"\f897"}.fa-fan:before{content:"\f863"}.fa-person-walking-luggage:before{content:"\e554"}.fa-arrows-alt-v:before,.fa-up-down:before{content:"\f338"}.fa-cloud-moon-rain:before{content:"\f73c"}.fa-calendar:before{content:"\f133"}.fa-trailer:before{content:"\e041"}.fa-bahai:before,.fa-haykal:before{content:"\f666"}.fa-sd-card:before{content:"\f7c2"}.fa-dragon:before{content:"\f6d5"}.fa-shoe-prints:before{content:"\f54b"}.fa-circle-plus:before,.fa-plus-circle:before{content:"\f055"}.fa-face-grin-tongue-wink:before,.fa-grin-tongue-wink:before{content:"\f58b"}.fa-hand-holding:before{content:"\f4bd"}.fa-plug-circle-exclamation:before{content:"\e55d"}.fa-chain-broken:before,.fa-chain-slash:before,.fa-link-slash:before,.fa-unlink:before{content:"\f127"}.fa-clone:before{content:"\f24d"}.fa-person-walking-arrow-loop-left:before{content:"\e551"}.fa-arrow-up-z-a:before,.fa-sort-alpha-up-alt:before{content:"\f882"}.fa-fire-alt:before,.fa-fire-flame-curved:before{content:"\f7e4"}.fa-tornado:before{content:"\f76f"}.fa-file-circle-plus:before{content:"\e494"}.fa-book-quran:before,.fa-quran:before{content:"\f687"}.fa-anchor:before{content:"\f13d"}.fa-border-all:before{content:"\f84c"}.fa-angry:before,.fa-face-angry:before{content:"\f556"}.fa-cookie-bite:before{content:"\f564"}.fa-arrow-trend-down:before{content:"\e097"}.fa-feed:before,.fa-rss:before{content:"\f09e"}.fa-draw-polygon:before{content:"\f5ee"}.fa-balance-scale:before,.fa-scale-balanced:before{content:"\f24e"}.fa-gauge-simple-high:before,.fa-tachometer-fast:before,.fa-tachometer:before{content:"\f62a"}.fa-shower:before{content:"\f2cc"}.fa-desktop-alt:before,.fa-desktop:before{content:"\f390"}.fa-m:before{content:"\4d"}.fa-table-list:before,.fa-th-list:before{content:"\f00b"}.fa-comment-sms:before,.fa-sms:before{content:"\f7cd"}.fa-book:before{content:"\f02d"}.fa-user-plus:before{content:"\f234"}.fa-check:before{content:"\f00c"}.fa-battery-4:before,.fa-battery-three-quarters:before{content:"\f241"}.fa-house-circle-check:before{content:"\e509"}.fa-angle-left:before{content:"\f104"}.fa-diagram-successor:before{content:"\e47a"}.fa-truck-arrow-right:before{content:"\e58b"}.fa-arrows-split-up-and-left:before{content:"\e4bc"}.fa-fist-raised:before,.fa-hand-fist:before{content:"\f6de"}.fa-cloud-moon:before{content:"\f6c3"}.fa-briefcase:before{content:"\f0b1"}.fa-person-falling:before{content:"\e546"}.fa-image-portrait:before,.fa-portrait:before{content:"\f3e0"}.fa-user-tag:before{content:"\f507"}.fa-rug:before{content:"\e569"}.fa-earth-europe:before,.fa-globe-europe:before{content:"\f7a2"}.fa-cart-flatbed-suitcase:before,.fa-luggage-cart:before{content:"\f59d"}.fa-rectangle-times:before,.fa-rectangle-xmark:before,.fa-times-rectangle:before,.fa-window-close:before{content:"\f410"}.fa-baht-sign:before{content:"\e0ac"}.fa-book-open:before{content:"\f518"}.fa-book-journal-whills:before,.fa-journal-whills:before{content:"\f66a"}.fa-handcuffs:before{content:"\e4f8"}.fa-exclamation-triangle:before,.fa-triangle-exclamation:before,.fa-warning:before{content:"\f071"}.fa-database:before{content:"\f1c0"}.fa-mail-forward:before,.fa-share:before{content:"\f064"}.fa-bottle-droplet:before{content:"\e4c4"}.fa-mask-face:before{content:"\e1d7"}.fa-hill-rockslide:before{content:"\e508"}.fa-exchange-alt:before,.fa-right-left:before{content:"\f362"}.fa-paper-plane:before{content:"\f1d8"}.fa-road-circle-exclamation:before{content:"\e565"}.fa-dungeon:before{content:"\f6d9"}.fa-align-right:before{content:"\f038"}.fa-money-bill-1-wave:before,.fa-money-bill-wave-alt:before{content:"\f53b"}.fa-life-ring:before{content:"\f1cd"}.fa-hands:before,.fa-sign-language:before,.fa-signing:before{content:"\f2a7"}.fa-calendar-day:before{content:"\f783"}.fa-ladder-water:before,.fa-swimming-pool:before,.fa-water-ladder:before{content:"\f5c5"}.fa-arrows-up-down:before,.fa-arrows-v:before{content:"\f07d"}.fa-face-grimace:before,.fa-grimace:before{content:"\f57f"}.fa-wheelchair-alt:before,.fa-wheelchair-move:before{content:"\e2ce"}.fa-level-down-alt:before,.fa-turn-down:before{content:"\f3be"}.fa-person-walking-arrow-right:before{content:"\e552"}.fa-envelope-square:before,.fa-square-envelope:before{content:"\f199"}.fa-dice:before{content:"\f522"}.fa-bowling-ball:before{content:"\f436"}.fa-brain:before{content:"\f5dc"}.fa-band-aid:before,.fa-bandage:before{content:"\f462"}.fa-calendar-minus:before{content:"\f272"}.fa-circle-xmark:before,.fa-times-circle:before,.fa-xmark-circle:before{content:"\f057"}.fa-gifts:before{content:"\f79c"}.fa-hotel:before{content:"\f594"}.fa-earth-asia:before,.fa-globe-asia:before{content:"\f57e"}.fa-id-card-alt:before,.fa-id-card-clip:before{content:"\f47f"}.fa-magnifying-glass-plus:before,.fa-search-plus:before{content:"\f00e"}.fa-thumbs-up:before{content:"\f164"}.fa-user-clock:before{content:"\f4fd"}.fa-allergies:before,.fa-hand-dots:before{content:"\f461"}.fa-file-invoice:before{content:"\f570"}.fa-window-minimize:before{content:"\f2d1"}.fa-coffee:before,.fa-mug-saucer:before{content:"\f0f4"}.fa-brush:before{content:"\f55d"}.fa-mask:before{content:"\f6fa"}.fa-magnifying-glass-minus:before,.fa-search-minus:before{content:"\f010"}.fa-ruler-vertical:before{content:"\f548"}.fa-user-alt:before,.fa-user-large:before{content:"\f406"}.fa-train-tram:before{content:"\e5b4"}.fa-user-nurse:before{content:"\f82f"}.fa-syringe:before{content:"\f48e"}.fa-cloud-sun:before{content:"\f6c4"}.fa-stopwatch-20:before{content:"\e06f"}.fa-square-full:before{content:"\f45c"}.fa-magnet:before{content:"\f076"}.fa-jar:before{content:"\e516"}.fa-note-sticky:before,.fa-sticky-note:before{content:"\f249"}.fa-bug-slash:before{content:"\e490"}.fa-arrow-up-from-water-pump:before{content:"\e4b6"}.fa-bone:before{content:"\f5d7"}.fa-user-injured:before{content:"\f728"}.fa-face-sad-tear:before,.fa-sad-tear:before{content:"\f5b4"}.fa-plane:before{content:"\f072"}.fa-tent-arrows-down:before{content:"\e581"}.fa-exclamation:before{content:"\21"}.fa-arrows-spin:before{content:"\e4bb"}.fa-print:before{content:"\f02f"}.fa-try:before,.fa-turkish-lira-sign:before,.fa-turkish-lira:before{content:"\e2bb"}.fa-dollar-sign:before,.fa-dollar:before,.fa-usd:before{content:"\24"}.fa-x:before{content:"\58"}.fa-magnifying-glass-dollar:before,.fa-search-dollar:before{content:"\f688"}.fa-users-cog:before,.fa-users-gear:before{content:"\f509"}.fa-person-military-pointing:before{content:"\e54a"}.fa-bank:before,.fa-building-columns:before,.fa-institution:before,.fa-museum:before,.fa-university:before{content:"\f19c"}.fa-umbrella:before{content:"\f0e9"}.fa-trowel:before{content:"\e589"}.fa-d:before{content:"\44"}.fa-stapler:before{content:"\e5af"}.fa-masks-theater:before,.fa-theater-masks:before{content:"\f630"}.fa-kip-sign:before{content:"\e1c4"}.fa-hand-point-left:before{content:"\f0a5"}.fa-handshake-alt:before,.fa-handshake-simple:before{content:"\f4c6"}.fa-fighter-jet:before,.fa-jet-fighter:before{content:"\f0fb"}.fa-share-alt-square:before,.fa-square-share-nodes:before{content:"\f1e1"}.fa-barcode:before{content:"\f02a"}.fa-plus-minus:before{content:"\e43c"}.fa-video-camera:before,.fa-video:before{content:"\f03d"}.fa-graduation-cap:before,.fa-mortar-board:before{content:"\f19d"}.fa-hand-holding-medical:before{content:"\e05c"}.fa-person-circle-check:before{content:"\e53e"}.fa-level-up-alt:before,.fa-turn-up:before{content:"\f3bf"}
9: .fa-sr-only,.fa-sr-only-focusable:not(:focus),.sr-only,.sr-only-focusable:not(:focus){position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}:host,:root{--fa-style-family-brands:"Font Awesome 6 Brands";--fa-font-brands:normal 400 1em/1 "Font Awesome 6 Brands"}@font-face{font-family:"Font Awesome 6 Brands";font-style:normal;font-weight:400;font-display:block;src:url(../webfonts/fa-brands-400.woff2) format("woff2"),url(../webfonts/fa-brands-400.ttf) format("truetype")}.fa-brands,.fab{font-weight:400}.fa-monero:before{content:"\f3d0"}.fa-hooli:before{content:"\f427"}.fa-yelp:before{content:"\f1e9"}.fa-cc-visa:before{content:"\f1f0"}.fa-lastfm:before{content:"\f202"}.fa-shopware:before{content:"\f5b5"}.fa-creative-commons-nc:before{content:"\f4e8"}.fa-aws:before{content:"\f375"}.fa-redhat:before{content:"\f7bc"}.fa-yoast:before{content:"\f2b1"}.fa-cloudflare:before{content:"\e07d"}.fa-ups:before{content:"\f7e0"}.fa-pixiv:before{content:"\e640"}.fa-wpexplorer:before{content:"\f2de"}.fa-dyalog:before{content:"\f399"}.fa-bity:before{content:"\f37a"}.fa-stackpath:before{content:"\f842"}.fa-buysellads:before{content:"\f20d"}.fa-first-order:before{content:"\f2b0"}.fa-modx:before{content:"\f285"}.fa-guilded:before{content:"\e07e"}.fa-vnv:before{content:"\f40b"}.fa-js-square:before,.fa-square-js:before{content:"\f3b9"}.fa-microsoft:before{content:"\f3ca"}.fa-qq:before{content:"\f1d6"}.fa-orcid:before{content:"\f8d2"}.fa-java:before{content:"\f4e4"}.fa-invision:before{content:"\f7b0"}.fa-creative-commons-pd-alt:before{content:"\f4ed"}.fa-centercode:before{content:"\f380"}.fa-glide-g:before{content:"\f2a6"}.fa-drupal:before{content:"\f1a9"}.fa-hire-a-helper:before{content:"\f3b0"}.fa-creative-commons-by:before{content:"\f4e7"}.fa-unity:before{content:"\e049"}.fa-whmcs:before{content:"\f40d"}.fa-rocketchat:before{content:"\f3e8"}.fa-vk:before{content:"\f189"}.fa-untappd:before{content:"\f405"}.fa-mailchimp:before{content:"\f59e"}.fa-css3-alt:before{content:"\f38b"}.fa-reddit-square:before,.fa-square-reddit:before{content:"\f1a2"}.fa-vimeo-v:before{content:"\f27d"}.fa-contao:before{content:"\f26d"}.fa-square-font-awesome:before{content:"\e5ad"}.fa-deskpro:before{content:"\f38f"}.fa-brave:before{content:"\e63c"}.fa-sistrix:before{content:"\f3ee"}.fa-instagram-square:before,.fa-square-instagram:before{content:"\e055"}.fa-battle-net:before{content:"\f835"}.fa-the-red-yeti:before{content:"\f69d"}.fa-hacker-news-square:before,.fa-square-hacker-news:before{content:"\f3af"}.fa-edge:before{content:"\f282"}.fa-threads:before{content:"\e618"}.fa-napster:before{content:"\f3d2"}.fa-snapchat-square:before,.fa-square-snapchat:before{content:"\f2ad"}.fa-google-plus-g:before{content:"\f0d5"}.fa-artstation:before{content:"\f77a"}.fa-markdown:before{content:"\f60f"}.fa-sourcetree:before{content:"\f7d3"}.fa-google-plus:before{content:"\f2b3"}.fa-diaspora:before{content:"\f791"}.fa-foursquare:before{content:"\f180"}.fa-stack-overflow:before{content:"\f16c"}.fa-github-alt:before{content:"\f113"}.fa-phoenix-squadron:before{content:"\f511"}.fa-pagelines:before{content:"\f18c"}.fa-algolia:before{content:"\f36c"}.fa-red-river:before{content:"\f3e3"}.fa-creative-commons-sa:before{content:"\f4ef"}.fa-safari:before{content:"\f267"}.fa-google:before{content:"\f1a0"}.fa-font-awesome-alt:before,.fa-square-font-awesome-stroke:before{content:"\f35c"}.fa-atlassian:before{content:"\f77b"}.fa-linkedin-in:before{content:"\f0e1"}.fa-digital-ocean:before{content:"\f391"}.fa-nimblr:before{content:"\f5a8"}.fa-chromecast:before{content:"\f838"}.fa-evernote:before{content:"\f839"}.fa-hacker-news:before{content:"\f1d4"}.fa-creative-commons-sampling:before{content:"\f4f0"}.fa-adversal:before{content:"\f36a"}.fa-creative-commons:before{content:"\f25e"}.fa-watchman-monitoring:before{content:"\e087"}.fa-fonticons:before{content:"\f280"}.fa-weixin:before{content:"\f1d7"}.fa-shirtsinbulk:before{content:"\f214"}.fa-codepen:before{content:"\f1cb"}.fa-git-alt:before{content:"\f841"}.fa-lyft:before{content:"\f3c3"}.fa-rev:before{content:"\f5b2"}.fa-windows:before{content:"\f17a"}.fa-wizards-of-the-coast:before{content:"\f730"}.fa-square-viadeo:before,.fa-viadeo-square:before{content:"\f2aa"}.fa-meetup:before{content:"\f2e0"}.fa-centos:before{content:"\f789"}.fa-adn:before{content:"\f170"}.fa-cloudsmith:before{content:"\f384"}.fa-opensuse:before{content:"\e62b"}.fa-pied-piper-alt:before{content:"\f1a8"}.fa-dribbble-square:before,.fa-square-dribbble:before{content:"\f397"}.fa-codiepie:before{content:"\f284"}.fa-node:before{content:"\f419"}.fa-mix:before{content:"\f3cb"}.fa-steam:before{content:"\f1b6"}.fa-cc-apple-pay:before{content:"\f416"}.fa-scribd:before{content:"\f28a"}.fa-debian:before{content:"\e60b"}.fa-openid:before{content:"\f19b"}.fa-instalod:before{content:"\e081"}.fa-expeditedssl:before{content:"\f23e"}.fa-sellcast:before{content:"\f2da"}.fa-square-twitter:before,.fa-twitter-square:before{content:"\f081"}.fa-r-project:before{content:"\f4f7"}.fa-delicious:before{content:"\f1a5"}.fa-freebsd:before{content:"\f3a4"}.fa-vuejs:before{content:"\f41f"}.fa-accusoft:before{content:"\f369"}.fa-ioxhost:before{content:"\f208"}.fa-fonticons-fi:before{content:"\f3a2"}.fa-app-store:before{content:"\f36f"}.fa-cc-mastercard:before{content:"\f1f1"}.fa-itunes-note:before{content:"\f3b5"}.fa-golang:before{content:"\e40f"}.fa-kickstarter:before{content:"\f3bb"}.fa-grav:before{content:"\f2d6"}.fa-weibo:before{content:"\f18a"}.fa-uncharted:before{content:"\e084"}.fa-firstdraft:before{content:"\f3a1"}.fa-square-youtube:before,.fa-youtube-square:before{content:"\f431"}.fa-wikipedia-w:before{content:"\f266"}.fa-rendact:before,.fa-wpressr:before{content:"\f3e4"}.fa-angellist:before{content:"\f209"}.fa-galactic-republic:before{content:"\f50c"}.fa-nfc-directional:before{content:"\e530"}.fa-skype:before{content:"\f17e"}.fa-joget:before{content:"\f3b7"}.fa-fedora:before{content:"\f798"}.fa-stripe-s:before{content:"\f42a"}.fa-meta:before{content:"\e49b"}.fa-laravel:before{content:"\f3bd"}.fa-hotjar:before{content:"\f3b1"}.fa-bluetooth-b:before{content:"\f294"}.fa-square-letterboxd:before{content:"\e62e"}.fa-sticker-mule:before{content:"\f3f7"}.fa-creative-commons-zero:before{content:"\f4f3"}.fa-hips:before{content:"\f452"}.fa-behance:before{content:"\f1b4"}.fa-reddit:before{content:"\f1a1"}.fa-discord:before{content:"\f392"}.fa-chrome:before{content:"\f268"}.fa-app-store-ios:before{content:"\f370"}.fa-cc-discover:before{content:"\f1f2"}.fa-wpbeginner:before{content:"\f297"}.fa-confluence:before{content:"\f78d"}.fa-shoelace:before{content:"\e60c"}.fa-mdb:before{content:"\f8ca"}.fa-dochub:before{content:"\f394"}.fa-accessible-icon:before{content:"\f368"}.fa-ebay:before{content:"\f4f4"}.fa-amazon:before{content:"\f270"}.fa-unsplash:before{content:"\e07c"}.fa-yarn:before{content:"\f7e3"}.fa-square-steam:before,.fa-steam-square:before{content:"\f1b7"}.fa-500px:before{content:"\f26e"}.fa-square-vimeo:before,.fa-vimeo-square:before{content:"\f194"}.fa-asymmetrik:before{content:"\f372"}.fa-font-awesome-flag:before,.fa-font-awesome-logo-full:before,.fa-font-awesome:before{content:"\f2b4"}.fa-gratipay:before{content:"\f184"}.fa-apple:before{content:"\f179"}.fa-hive:before{content:"\e07f"}.fa-gitkraken:before{content:"\f3a6"}.fa-keybase:before{content:"\f4f5"}.fa-apple-pay:before{content:"\f415"}.fa-padlet:before{content:"\e4a0"}.fa-amazon-pay:before{content:"\f42c"}.fa-github-square:before,.fa-square-github:before{content:"\f092"}.fa-stumbleupon:before{content:"\f1a4"}.fa-fedex:before{content:"\f797"}.fa-phoenix-framework:before{content:"\f3dc"}.fa-shopify:before{content:"\e057"}.fa-neos:before{content:"\f612"}.fa-square-threads:before{content:"\e619"}.fa-hackerrank:before{content:"\f5f7"}.fa-researchgate:before{content:"\f4f8"}.fa-swift:before{content:"\f8e1"}.fa-angular:before{content:"\f420"}.fa-speakap:before{content:"\f3f3"}.fa-angrycreative:before{content:"\f36e"}.fa-y-combinator:before{content:"\f23b"}.fa-empire:before{content:"\f1d1"}.fa-envira:before{content:"\f299"}.fa-google-scholar:before{content:"\e63b"}.fa-gitlab-square:before,.fa-square-gitlab:before{content:"\e5ae"}.fa-studiovinari:before{content:"\f3f8"}.fa-pied-piper:before{content:"\f2ae"}.fa-wordpress:before{content:"\f19a"}.fa-product-hunt:before{content:"\f288"}.fa-firefox:before{content:"\f269"}.fa-linode:before{content:"\f2b8"}.fa-goodreads:before{content:"\f3a8"}.fa-odnoklassniki-square:before,.fa-square-odnoklassniki:before{content:"\f264"}.fa-jsfiddle:before{content:"\f1cc"}.fa-sith:before{content:"\f512"}.fa-themeisle:before{content:"\f2b2"}.fa-page4:before{content:"\f3d7"}.fa-hashnode:before{content:"\e499"}.fa-react:before{content:"\f41b"}.fa-cc-paypal:before{content:"\f1f4"}.fa-squarespace:before{content:"\f5be"}.fa-cc-stripe:before{content:"\f1f5"}.fa-creative-commons-share:before{content:"\f4f2"}.fa-bitcoin:before{content:"\f379"}.fa-keycdn:before{content:"\f3ba"}.fa-opera:before{content:"\f26a"}.fa-itch-io:before{content:"\f83a"}.fa-umbraco:before{content:"\f8e8"}.fa-galactic-senate:before{content:"\f50d"}.fa-ubuntu:before{content:"\f7df"}.fa-draft2digital:before{content:"\f396"}.fa-stripe:before{content:"\f429"}.fa-houzz:before{content:"\f27c"}.fa-gg:before{content:"\f260"}.fa-dhl:before{content:"\f790"}.fa-pinterest-square:before,.fa-square-pinterest:before{content:"\f0d3"}.fa-xing:before{content:"\f168"}.fa-blackberry:before{content:"\f37b"}.fa-creative-commons-pd:before{content:"\f4ec"}.fa-playstation:before{content:"\f3df"}.fa-quinscape:before{content:"\f459"}.fa-less:before{content:"\f41d"}.fa-blogger-b:before{content:"\f37d"}.fa-opencart:before{content:"\f23d"}.fa-vine:before{content:"\f1ca"}.fa-signal-messenger:before{content:"\e663"}.fa-paypal:before{content:"\f1ed"}.fa-gitlab:before{content:"\f296"}.fa-typo3:before{content:"\f42b"}.fa-reddit-alien:before{content:"\f281"}.fa-yahoo:before{content:"\f19e"}.fa-dailymotion:before{content:"\e052"}.fa-affiliatetheme:before{content:"\f36b"}.fa-pied-piper-pp:before{content:"\f1a7"}.fa-bootstrap:before{content:"\f836"}.fa-odnoklassniki:before{content:"\f263"}.fa-nfc-symbol:before{content:"\e531"}.fa-mintbit:before{content:"\e62f"}.fa-ethereum:before{content:"\f42e"}.fa-speaker-deck:before{content:"\f83c"}.fa-creative-commons-nc-eu:before{content:"\f4e9"}.fa-patreon:before{content:"\f3d9"}.fa-avianex:before{content:"\f374"}.fa-ello:before{content:"\f5f1"}.fa-gofore:before{content:"\f3a7"}.fa-bimobject:before{content:"\f378"}.fa-brave-reverse:before{content:"\e63d"}.fa-facebook-f:before{content:"\f39e"}.fa-google-plus-square:before,.fa-square-google-plus:before{content:"\f0d4"}.fa-mandalorian:before{content:"\f50f"}.fa-first-order-alt:before{content:"\f50a"}.fa-osi:before{content:"\f41a"}.fa-google-wallet:before{content:"\f1ee"}.fa-d-and-d-beyond:before{content:"\f6ca"}.fa-periscope:before{content:"\f3da"}.fa-fulcrum:before{content:"\f50b"}.fa-cloudscale:before{content:"\f383"}.fa-forumbee:before{content:"\f211"}.fa-mizuni:before{content:"\f3cc"}.fa-schlix:before{content:"\f3ea"}.fa-square-xing:before,.fa-xing-square:before{content:"\f169"}.fa-bandcamp:before{content:"\f2d5"}.fa-wpforms:before{content:"\f298"}.fa-cloudversify:before{content:"\f385"}.fa-usps:before{content:"\f7e1"}.fa-megaport:before{content:"\f5a3"}.fa-magento:before{content:"\f3c4"}.fa-spotify:before{content:"\f1bc"}.fa-optin-monster:before{content:"\f23c"}.fa-fly:before{content:"\f417"}.fa-aviato:before{content:"\f421"}.fa-itunes:before{content:"\f3b4"}.fa-cuttlefish:before{content:"\f38c"}.fa-blogger:before{content:"\f37c"}.fa-flickr:before{content:"\f16e"}.fa-viber:before{content:"\f409"}.fa-soundcloud:before{content:"\f1be"}.fa-digg:before{content:"\f1a6"}.fa-tencent-weibo:before{content:"\f1d5"}.fa-letterboxd:before{content:"\e62d"}.fa-symfony:before{content:"\f83d"}.fa-maxcdn:before{content:"\f136"}.fa-etsy:before{content:"\f2d7"}.fa-facebook-messenger:before{content:"\f39f"}.fa-audible:before{content:"\f373"}.fa-think-peaks:before{content:"\f731"}.fa-bilibili:before{content:"\e3d9"}.fa-erlang:before{content:"\f39d"}.fa-x-twitter:before{content:"\e61b"}.fa-cotton-bureau:before{content:"\f89e"}.fa-dashcube:before{content:"\f210"}.fa-42-group:before,.fa-innosoft:before{content:"\e080"}.fa-stack-exchange:before{content:"\f18d"}.fa-elementor:before{content:"\f430"}.fa-pied-piper-square:before,.fa-square-pied-piper:before{content:"\e01e"}.fa-creative-commons-nd:before{content:"\f4eb"}.fa-palfed:before{content:"\f3d8"}.fa-superpowers:before{content:"\f2dd"}.fa-resolving:before{content:"\f3e7"}.fa-xbox:before{content:"\f412"}.fa-searchengin:before{content:"\f3eb"}.fa-tiktok:before{content:"\e07b"}.fa-facebook-square:before,.fa-square-facebook:before{content:"\f082"}.fa-renren:before{content:"\f18b"}.fa-linux:before{content:"\f17c"}.fa-glide:before{content:"\f2a5"}.fa-linkedin:before{content:"\f08c"}.fa-hubspot:before{content:"\f3b2"}.fa-deploydog:before{content:"\f38e"}.fa-twitch:before{content:"\f1e8"}.fa-ravelry:before{content:"\f2d9"}.fa-mixer:before{content:"\e056"}.fa-lastfm-square:before,.fa-square-lastfm:before{content:"\f203"}.fa-vimeo:before{content:"\f40a"}.fa-mendeley:before{content:"\f7b3"}.fa-uniregistry:before{content:"\f404"}.fa-figma:before{content:"\f799"}.fa-creative-commons-remix:before{content:"\f4ee"}.fa-cc-amazon-pay:before{content:"\f42d"}.fa-dropbox:before{content:"\f16b"}.fa-instagram:before{content:"\f16d"}.fa-cmplid:before{content:"\e360"}.fa-upwork:before{content:"\e641"}.fa-facebook:before{content:"\f09a"}.fa-gripfire:before{content:"\f3ac"}.fa-jedi-order:before{content:"\f50e"}.fa-uikit:before{content:"\f403"}.fa-fort-awesome-alt:before{content:"\f3a3"}.fa-phabricator:before{content:"\f3db"}.fa-ussunnah:before{content:"\f407"}.fa-earlybirds:before{content:"\f39a"}.fa-trade-federation:before{content:"\f513"}.fa-autoprefixer:before{content:"\f41c"}.fa-whatsapp:before{content:"\f232"}.fa-slideshare:before{content:"\f1e7"}.fa-google-play:before{content:"\f3ab"}.fa-viadeo:before{content:"\f2a9"}.fa-line:before{content:"\f3c0"}.fa-google-drive:before{content:"\f3aa"}.fa-servicestack:before{content:"\f3ec"}.fa-simplybuilt:before{content:"\f215"}.fa-bitbucket:before{content:"\f171"}.fa-imdb:before{content:"\f2d8"}.fa-deezer:before{content:"\e077"}.fa-raspberry-pi:before{content:"\f7bb"}.fa-jira:before{content:"\f7b1"}.fa-docker:before{content:"\f395"}.fa-screenpal:before{content:"\e570"}.fa-bluetooth:before{content:"\f293"}.fa-gitter:before{content:"\f426"}.fa-d-and-d:before{content:"\f38d"}.fa-microblog:before{content:"\e01a"}.fa-cc-diners-club:before{content:"\f24c"}.fa-gg-circle:before{content:"\f261"}.fa-pied-piper-hat:before{content:"\f4e5"}.fa-kickstarter-k:before{content:"\f3bc"}.fa-yandex:before{content:"\f413"}.fa-readme:before{content:"\f4d5"}.fa-html5:before{content:"\f13b"}.fa-sellsy:before{content:"\f213"}.fa-sass:before{content:"\f41e"}.fa-wirsindhandwerk:before,.fa-wsh:before{content:"\e2d0"}.fa-buromobelexperte:before{content:"\f37f"}.fa-salesforce:before{content:"\f83b"}.fa-octopus-deploy:before{content:"\e082"}.fa-medapps:before{content:"\f3c6"}.fa-ns8:before{content:"\f3d5"}.fa-pinterest-p:before{content:"\f231"}.fa-apper:before{content:"\f371"}.fa-fort-awesome:before{content:"\f286"}.fa-waze:before{content:"\f83f"}.fa-cc-jcb:before{content:"\f24b"}.fa-snapchat-ghost:before,.fa-snapchat:before{content:"\f2ab"}.fa-fantasy-flight-games:before{content:"\f6dc"}.fa-rust:before{content:"\e07a"}.fa-wix:before{content:"\f5cf"}.fa-behance-square:before,.fa-square-behance:before{content:"\f1b5"}.fa-supple:before{content:"\f3f9"}.fa-webflow:before{content:"\e65c"}.fa-rebel:before{content:"\f1d0"}.fa-css3:before{content:"\f13c"}.fa-staylinked:before{content:"\f3f5"}.fa-kaggle:before{content:"\f5fa"}.fa-space-awesome:before{content:"\e5ac"}.fa-deviantart:before{content:"\f1bd"}.fa-cpanel:before{content:"\f388"}.fa-goodreads-g:before{content:"\f3a9"}.fa-git-square:before,.fa-square-git:before{content:"\f1d2"}.fa-square-tumblr:before,.fa-tumblr-square:before{content:"\f174"}.fa-trello:before{content:"\f181"}.fa-creative-commons-nc-jp:before{content:"\f4ea"}.fa-get-pocket:before{content:"\f265"}.fa-perbyte:before{content:"\e083"}.fa-grunt:before{content:"\f3ad"}.fa-weebly:before{content:"\f5cc"}.fa-connectdevelop:before{content:"\f20e"}.fa-leanpub:before{content:"\f212"}.fa-black-tie:before{content:"\f27e"}.fa-themeco:before{content:"\f5c6"}.fa-python:before{content:"\f3e2"}.fa-android:before{content:"\f17b"}.fa-bots:before{content:"\e340"}.fa-free-code-camp:before{content:"\f2c5"}.fa-hornbill:before{content:"\f592"}.fa-js:before{content:"\f3b8"}.fa-ideal:before{content:"\e013"}.fa-git:before{content:"\f1d3"}.fa-dev:before{content:"\f6cc"}.fa-sketch:before{content:"\f7c6"}.fa-yandex-international:before{content:"\f414"}.fa-cc-amex:before{content:"\f1f3"}.fa-uber:before{content:"\f402"}.fa-github:before{content:"\f09b"}.fa-php:before{content:"\f457"}.fa-alipay:before{content:"\f642"}.fa-youtube:before{content:"\f167"}.fa-skyatlas:before{content:"\f216"}.fa-firefox-browser:before{content:"\e007"}.fa-replyd:before{content:"\f3e6"}.fa-suse:before{content:"\f7d6"}.fa-jenkins:before{content:"\f3b6"}.fa-twitter:before{content:"\f099"}.fa-rockrms:before{content:"\f3e9"}.fa-pinterest:before{content:"\f0d2"}.fa-buffer:before{content:"\f837"}.fa-npm:before{content:"\f3d4"}.fa-yammer:before{content:"\f840"}.fa-btc:before{content:"\f15a"}.fa-dribbble:before{content:"\f17d"}.fa-stumbleupon-circle:before{content:"\f1a3"}.fa-internet-explorer:before{content:"\f26b"}.fa-stubber:before{content:"\e5c7"}.fa-telegram-plane:before,.fa-telegram:before{content:"\f2c6"}.fa-old-republic:before{content:"\f510"}.fa-odysee:before{content:"\e5c6"}.fa-square-whatsapp:before,.fa-whatsapp-square:before{content:"\f40c"}.fa-node-js:before{content:"\f3d3"}.fa-edge-legacy:before{content:"\e078"}.fa-slack-hash:before,.fa-slack:before{content:"\f198"}.fa-medrt:before{content:"\f3c8"}.fa-usb:before{content:"\f287"}.fa-tumblr:before{content:"\f173"}.fa-vaadin:before{content:"\f408"}.fa-quora:before{content:"\f2c4"}.fa-square-x-twitter:before{content:"\e61a"}.fa-reacteurope:before{content:"\f75d"}.fa-medium-m:before,.fa-medium:before{content:"\f23a"}.fa-amilia:before{content:"\f36d"}.fa-mixcloud:before{content:"\f289"}.fa-flipboard:before{content:"\f44d"}.fa-viacoin:before{content:"\f237"}.fa-critical-role:before{content:"\f6c9"}.fa-sitrox:before{content:"\e44a"}.fa-discourse:before{content:"\f393"}.fa-joomla:before{content:"\f1aa"}.fa-mastodon:before{content:"\f4f6"}.fa-airbnb:before{content:"\f834"}.fa-wolf-pack-battalion:before{content:"\f514"}.fa-buy-n-large:before{content:"\f8a6"}.fa-gulp:before{content:"\f3ae"}.fa-creative-commons-sampling-plus:before{content:"\f4f1"}.fa-strava:before{content:"\f428"}.fa-ember:before{content:"\f423"}.fa-canadian-maple-leaf:before{content:"\f785"}.fa-teamspeak:before{content:"\f4f9"}.fa-pushed:before{content:"\f3e1"}.fa-wordpress-simple:before{content:"\f411"}.fa-nutritionix:before{content:"\f3d6"}.fa-wodu:before{content:"\e088"}.fa-google-pay:before{content:"\e079"}.fa-intercom:before{content:"\f7af"}.fa-zhihu:before{content:"\f63f"}.fa-korvue:before{content:"\f42f"}.fa-pix:before{content:"\e43a"}.fa-steam-symbol:before{content:"\f3f6"}:host,:root{--fa-font-regular:normal 400 1em/1 "Font Awesome 6 Free"}@font-face{font-family:"Font Awesome 6 Free";font-style:normal;font-weight:400;font-display:block;src:url(../webfonts/fa-regular-400.woff2) format("woff2"),url(../webfonts/fa-regular-400.ttf) format("truetype")}.fa-regular,.far{font-weight:400}:host,:root{--fa-style-family-classic:"Font Awesome 6 Free";--fa-font-solid:normal 900 1em/1 "Font Awesome 6 Free"}@font-face{font-family:"Font Awesome 6 Free";font-style:normal;font-weight:900;font-display:block;src:url(../webfonts/fa-solid-900.woff2) format("woff2"),url(../webfonts/fa-solid-900.ttf) format("truetype")}.fa-solid,.fas{font-weight:900}@font-face{font-family:"Font Awesome 5 Brands";font-display:block;font-weight:400;src:url(../webfonts/fa-brands-400.woff2) format("woff2"),url(../webfonts/fa-brands-400.ttf) format("truetype")}@font-face{font-family:"Font Awesome 5 Free";font-display:block;font-weight:900;src:url(../webfonts/fa-solid-900.woff2) format("woff2"),url(../webfonts/fa-solid-900.ttf) format("truetype")}@font-face{font-family:"Font Awesome 5 Free";font-display:block;font-weight:400;src:url(../webfonts/fa-regular-400.woff2) format("woff2"),url(../webfonts/fa-regular-400.ttf) format("truetype")}@font-face{font-family:"FontAwesome";font-display:block;src:url(../webfonts/fa-solid-900.woff2) format("woff2"),url(../webfonts/fa-solid-900.ttf) format("truetype")}@font-face{font-family:"FontAwesome";font-display:block;src:url(../webfonts/fa-brands-400.woff2) format("woff2"),url(../webfonts/fa-brands-400.ttf) format("truetype")}@font-face{font-family:"FontAwesome";font-display:block;src:url(../webfonts/fa-regular-400.woff2) format("woff2"),url(../webfonts/fa-regular-400.ttf) format("truetype");unicode-range:u+f003,u+f006,u+f014,u+f016-f017,u+f01a-f01b,u+f01d,u+f022,u+f03e,u+f044,u+f046,u+f05c-f05d,u+f06e,u+f070,u+f087-f088,u+f08a,u+f094,u+f096-f097,u+f09d,u+f0a0,u+f0a2,u+f0a4-f0a7,u+f0c5,u+f0c7,u+f0e5-f0e6,u+f0eb,u+f0f6-f0f8,u+f10c,u+f114-f115,u+f118-f11a,u+f11c-f11d,u+f133,u+f147,u+f14e,u+f150-f152,u+f185-f186,u+f18e,u+f190-f192,u+f196,u+f1c1-f1c9,u+f1d9,u+f1db,u+f1e3,u+f1ea,u+f1f7,u+f1f9,u+f20a,u+f247-f248,u+f24a,u+f24d,u+f255-f25b,u+f25d,u+f271-f274,u+f278,u+f27b,u+f28c,u+f28e,u+f29c,u+f2b5,u+f2b7,u+f2ba,u+f2bc,u+f2be,u+f2c0-f2c1,u+f2c3,u+f2d0,u+f2d2,u+f2d4,u+f2dc}@font-face{font-family:"FontAwesome";font-display:block;src:url(../webfonts/fa-v4compatibility.woff2) format("woff2"),url(../webfonts/fa-v4compatibility.ttf) format("truetype");unicode-range:u+f041,u+f047,u+f065-f066,u+f07d-f07e,u+f080,u+f08b,u+f08e,u+f090,u+f09a,u+f0ac,u+f0ae,u+f0b2,u+f0d0,u+f0d6,u+f0e4,u+f0ec,u+f10a-f10b,u+f123,u+f13e,u+f148-f149,u+f14c,u+f156,u+f15e,u+f160-f161,u+f163,u+f175-f178,u+f195,u+f1f8,u+f219,u+f27a}
```

## File: switchbot_dashboard/static/vendor/js/chart.umd.min.js
```javascript
 1: /**
 2:  * Skipped minification because the original files appears to be already minified.
 3:  * Original file: /npm/chart.js@4.4.0/dist/chart.umd.js
 4:  *
 5:  * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 6:  */
 7: /*!
 8:  * Chart.js v4.4.0
 9:  * https://www.chartjs.org
10:  * (c) 2023 Chart.js Contributors
11:  * Released under the MIT License
12:  */
13: !function(t,e){"object"==typeof exports&&"undefined"!=typeof module?module.exports=e():"function"==typeof define&&define.amd?define(e):(t="undefined"!=typeof globalThis?globalThis:t||self).Chart=e()}(this,(function(){"use strict";var t=Object.freeze({__proto__:null,get Colors(){return Go},get Decimation(){return Qo},get Filler(){return ma},get Legend(){return ya},get SubTitle(){return ka},get Title(){return Ma},get Tooltip(){return Ba}});function e(){}const i=(()=>{let t=0;return()=>t++})();function s(t){return null==t}function n(t){if(Array.isArray&&Array.isArray(t))return!0;const e=Object.prototype.toString.call(t);return"[object"===e.slice(0,7)&&"Array]"===e.slice(-6)}function o(t){return null!==t&&"[object Object]"===Object.prototype.toString.call(t)}function a(t){return("number"==typeof t||t instanceof Number)&&isFinite(+t)}function r(t,e){return a(t)?t:e}function l(t,e){return void 0===t?e:t}const h=(t,e)=>"string"==typeof t&&t.endsWith("%")?parseFloat(t)/100:+t/e,c=(t,e)=>"string"==typeof t&&t.endsWith("%")?parseFloat(t)/100*e:+t;function d(t,e,i){if(t&&"function"==typeof t.call)return t.apply(i,e)}function u(t,e,i,s){let a,r,l;if(n(t))if(r=t.length,s)for(a=r-1;a>=0;a--)e.call(i,t[a],a);else for(a=0;a<r;a++)e.call(i,t[a],a);else if(o(t))for(l=Object.keys(t),r=l.length,a=0;a<r;a++)e.call(i,t[l[a]],l[a])}function f(t,e){let i,s,n,o;if(!t||!e||t.length!==e.length)return!1;for(i=0,s=t.length;i<s;++i)if(n=t[i],o=e[i],n.datasetIndex!==o.datasetIndex||n.index!==o.index)return!1;return!0}function g(t){if(n(t))return t.map(g);if(o(t)){const e=Object.create(null),i=Object.keys(t),s=i.length;let n=0;for(;n<s;++n)e[i[n]]=g(t[i[n]]);return e}return t}function p(t){return-1===["__proto__","prototype","constructor"].indexOf(t)}function m(t,e,i,s){if(!p(t))return;const n=e[t],a=i[t];o(n)&&o(a)?b(n,a,s):e[t]=g(a)}function b(t,e,i){const s=n(e)?e:[e],a=s.length;if(!o(t))return t;const r=(i=i||{}).merger||m;let l;for(let e=0;e<a;++e){if(l=s[e],!o(l))continue;const n=Object.keys(l);for(let e=0,s=n.length;e<s;++e)r(n[e],t,l,i)}return t}function x(t,e){return b(t,e,{merger:_})}function _(t,e,i){if(!p(t))return;const s=e[t],n=i[t];o(s)&&o(n)?x(s,n):Object.prototype.hasOwnProperty.call(e,t)||(e[t]=g(n))}const y={"":t=>t,x:t=>t.x,y:t=>t.y};function v(t){const e=t.split("."),i=[];let s="";for(const t of e)s+=t,s.endsWith("\\")?s=s.slice(0,-1)+".":(i.push(s),s="");return i}function M(t,e){const i=y[e]||(y[e]=function(t){const e=v(t);return t=>{for(const i of e){if(""===i)break;t=t&&t[i]}return t}}(e));return i(t)}function w(t){return t.charAt(0).toUpperCase()+t.slice(1)}const k=t=>void 0!==t,S=t=>"function"==typeof t,P=(t,e)=>{if(t.size!==e.size)return!1;for(const i of t)if(!e.has(i))return!1;return!0};function D(t){return"mouseup"===t.type||"click"===t.type||"contextmenu"===t.type}const C=Math.PI,O=2*C,A=O+C,T=Number.POSITIVE_INFINITY,L=C/180,E=C/2,R=C/4,I=2*C/3,z=Math.log10,F=Math.sign;function V(t,e,i){return Math.abs(t-e)<i}function B(t){const e=Math.round(t);t=V(t,e,t/1e3)?e:t;const i=Math.pow(10,Math.floor(z(t))),s=t/i;return(s<=1?1:s<=2?2:s<=5?5:10)*i}function W(t){const e=[],i=Math.sqrt(t);let s;for(s=1;s<i;s++)t%s==0&&(e.push(s),e.push(t/s));return i===(0|i)&&e.push(i),e.sort(((t,e)=>t-e)).pop(),e}function N(t){return!isNaN(parseFloat(t))&&isFinite(t)}function H(t,e){const i=Math.round(t);return i-e<=t&&i+e>=t}function j(t,e,i){let s,n,o;for(s=0,n=t.length;s<n;s++)o=t[s][i],isNaN(o)||(e.min=Math.min(e.min,o),e.max=Math.max(e.max,o))}function $(t){return t*(C/180)}function Y(t){return t*(180/C)}function U(t){if(!a(t))return;let e=1,i=0;for(;Math.round(t*e)/e!==t;)e*=10,i++;return i}function X(t,e){const i=e.x-t.x,s=e.y-t.y,n=Math.sqrt(i*i+s*s);let o=Math.atan2(s,i);return o<-.5*C&&(o+=O),{angle:o,distance:n}}function q(t,e){return Math.sqrt(Math.pow(e.x-t.x,2)+Math.pow(e.y-t.y,2))}function K(t,e){return(t-e+A)%O-C}function G(t){return(t%O+O)%O}function Z(t,e,i,s){const n=G(t),o=G(e),a=G(i),r=G(o-n),l=G(a-n),h=G(n-o),c=G(n-a);return n===o||n===a||s&&o===a||r>l&&h<c}function J(t,e,i){return Math.max(e,Math.min(i,t))}function Q(t){return J(t,-32768,32767)}function tt(t,e,i,s=1e-6){return t>=Math.min(e,i)-s&&t<=Math.max(e,i)+s}function et(t,e,i){i=i||(i=>t[i]<e);let s,n=t.length-1,o=0;for(;n-o>1;)s=o+n>>1,i(s)?o=s:n=s;return{lo:o,hi:n}}const it=(t,e,i,s)=>et(t,i,s?s=>{const n=t[s][e];return n<i||n===i&&t[s+1][e]===i}:s=>t[s][e]<i),st=(t,e,i)=>et(t,i,(s=>t[s][e]>=i));function nt(t,e,i){let s=0,n=t.length;for(;s<n&&t[s]<e;)s++;for(;n>s&&t[n-1]>i;)n--;return s>0||n<t.length?t.slice(s,n):t}const ot=["push","pop","shift","splice","unshift"];function at(t,e){t._chartjs?t._chartjs.listeners.push(e):(Object.defineProperty(t,"_chartjs",{configurable:!0,enumerable:!1,value:{listeners:[e]}}),ot.forEach((e=>{const i="_onData"+w(e),s=t[e];Object.defineProperty(t,e,{configurable:!0,enumerable:!1,value(...e){const n=s.apply(this,e);return t._chartjs.listeners.forEach((t=>{"function"==typeof t[i]&&t[i](...e)})),n}})})))}function rt(t,e){const i=t._chartjs;if(!i)return;const s=i.listeners,n=s.indexOf(e);-1!==n&&s.splice(n,1),s.length>0||(ot.forEach((e=>{delete t[e]})),delete t._chartjs)}function lt(t){const e=new Set(t);return e.size===t.length?t:Array.from(e)}const ht="undefined"==typeof window?function(t){return t()}:window.requestAnimationFrame;function ct(t,e){let i=[],s=!1;return function(...n){i=n,s||(s=!0,ht.call(window,(()=>{s=!1,t.apply(e,i)})))}}function dt(t,e){let i;return function(...s){return e?(clearTimeout(i),i=setTimeout(t,e,s)):t.apply(this,s),e}}const ut=t=>"start"===t?"left":"end"===t?"right":"center",ft=(t,e,i)=>"start"===t?e:"end"===t?i:(e+i)/2,gt=(t,e,i,s)=>t===(s?"left":"right")?i:"center"===t?(e+i)/2:e;function pt(t,e,i){const s=e.length;let n=0,o=s;if(t._sorted){const{iScale:a,_parsed:r}=t,l=a.axis,{min:h,max:c,minDefined:d,maxDefined:u}=a.getUserBounds();d&&(n=J(Math.min(it(r,l,h).lo,i?s:it(e,l,a.getPixelForValue(h)).lo),0,s-1)),o=u?J(Math.max(it(r,a.axis,c,!0).hi+1,i?0:it(e,l,a.getPixelForValue(c),!0).hi+1),n,s)-n:s-n}return{start:n,count:o}}function mt(t){const{xScale:e,yScale:i,_scaleRanges:s}=t,n={xmin:e.min,xmax:e.max,ymin:i.min,ymax:i.max};if(!s)return t._scaleRanges=n,!0;const o=s.xmin!==e.min||s.xmax!==e.max||s.ymin!==i.min||s.ymax!==i.max;return Object.assign(s,n),o}class bt{constructor(){this._request=null,this._charts=new Map,this._running=!1,this._lastDate=void 0}_notify(t,e,i,s){const n=e.listeners[s],o=e.duration;n.forEach((s=>s({chart:t,initial:e.initial,numSteps:o,currentStep:Math.min(i-e.start,o)})))}_refresh(){this._request||(this._running=!0,this._request=ht.call(window,(()=>{this._update(),this._request=null,this._running&&this._refresh()})))}_update(t=Date.now()){let e=0;this._charts.forEach(((i,s)=>{if(!i.running||!i.items.length)return;const n=i.items;let o,a=n.length-1,r=!1;for(;a>=0;--a)o=n[a],o._active?(o._total>i.duration&&(i.duration=o._total),o.tick(t),r=!0):(n[a]=n[n.length-1],n.pop());r&&(s.draw(),this._notify(s,i,t,"progress")),n.length||(i.running=!1,this._notify(s,i,t,"complete"),i.initial=!1),e+=n.length})),this._lastDate=t,0===e&&(this._running=!1)}_getAnims(t){const e=this._charts;let i=e.get(t);return i||(i={running:!1,initial:!0,items:[],listeners:{complete:[],progress:[]}},e.set(t,i)),i}listen(t,e,i){this._getAnims(t).listeners[e].push(i)}add(t,e){e&&e.length&&this._getAnims(t).items.push(...e)}has(t){return this._getAnims(t).items.length>0}start(t){const e=this._charts.get(t);e&&(e.running=!0,e.start=Date.now(),e.duration=e.items.reduce(((t,e)=>Math.max(t,e._duration)),0),this._refresh())}running(t){if(!this._running)return!1;const e=this._charts.get(t);return!!(e&&e.running&&e.items.length)}stop(t){const e=this._charts.get(t);if(!e||!e.items.length)return;const i=e.items;let s=i.length-1;for(;s>=0;--s)i[s].cancel();e.items=[],this._notify(t,e,Date.now(),"complete")}remove(t){return this._charts.delete(t)}}var xt=new bt;
14: /*!
15:  * @kurkle/color v0.3.2
16:  * https://github.com/kurkle/color#readme
17:  * (c) 2023 Jukka Kurkela
18:  * Released under the MIT License
19:  */function _t(t){return t+.5|0}const yt=(t,e,i)=>Math.max(Math.min(t,i),e);function vt(t){return yt(_t(2.55*t),0,255)}function Mt(t){return yt(_t(255*t),0,255)}function wt(t){return yt(_t(t/2.55)/100,0,1)}function kt(t){return yt(_t(100*t),0,100)}const St={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,A:10,B:11,C:12,D:13,E:14,F:15,a:10,b:11,c:12,d:13,e:14,f:15},Pt=[..."0123456789ABCDEF"],Dt=t=>Pt[15&t],Ct=t=>Pt[(240&t)>>4]+Pt[15&t],Ot=t=>(240&t)>>4==(15&t);function At(t){var e=(t=>Ot(t.r)&&Ot(t.g)&&Ot(t.b)&&Ot(t.a))(t)?Dt:Ct;return t?"#"+e(t.r)+e(t.g)+e(t.b)+((t,e)=>t<255?e(t):"")(t.a,e):void 0}const Tt=/^(hsla?|hwb|hsv)\(\s*([-+.e\d]+)(?:deg)?[\s,]+([-+.e\d]+)%[\s,]+([-+.e\d]+)%(?:[\s,]+([-+.e\d]+)(%)?)?\s*\)$/;function Lt(t,e,i){const s=e*Math.min(i,1-i),n=(e,n=(e+t/30)%12)=>i-s*Math.max(Math.min(n-3,9-n,1),-1);return[n(0),n(8),n(4)]}function Et(t,e,i){const s=(s,n=(s+t/60)%6)=>i-i*e*Math.max(Math.min(n,4-n,1),0);return[s(5),s(3),s(1)]}function Rt(t,e,i){const s=Lt(t,1,.5);let n;for(e+i>1&&(n=1/(e+i),e*=n,i*=n),n=0;n<3;n++)s[n]*=1-e-i,s[n]+=e;return s}function It(t){const e=t.r/255,i=t.g/255,s=t.b/255,n=Math.max(e,i,s),o=Math.min(e,i,s),a=(n+o)/2;let r,l,h;return n!==o&&(h=n-o,l=a>.5?h/(2-n-o):h/(n+o),r=function(t,e,i,s,n){return t===n?(e-i)/s+(e<i?6:0):e===n?(i-t)/s+2:(t-e)/s+4}(e,i,s,h,n),r=60*r+.5),[0|r,l||0,a]}function zt(t,e,i,s){return(Array.isArray(e)?t(e[0],e[1],e[2]):t(e,i,s)).map(Mt)}function Ft(t,e,i){return zt(Lt,t,e,i)}function Vt(t){return(t%360+360)%360}function Bt(t){const e=Tt.exec(t);let i,s=255;if(!e)return;e[5]!==i&&(s=e[6]?vt(+e[5]):Mt(+e[5]));const n=Vt(+e[2]),o=+e[3]/100,a=+e[4]/100;return i="hwb"===e[1]?function(t,e,i){return zt(Rt,t,e,i)}(n,o,a):"hsv"===e[1]?function(t,e,i){return zt(Et,t,e,i)}(n,o,a):Ft(n,o,a),{r:i[0],g:i[1],b:i[2],a:s}}const Wt={x:"dark",Z:"light",Y:"re",X:"blu",W:"gr",V:"medium",U:"slate",A:"ee",T:"ol",S:"or",B:"ra",C:"lateg",D:"ights",R:"in",Q:"turquois",E:"hi",P:"ro",O:"al",N:"le",M:"de",L:"yello",F:"en",K:"ch",G:"arks",H:"ea",I:"ightg",J:"wh"},Nt={OiceXe:"f0f8ff",antiquewEte:"faebd7",aqua:"ffff",aquamarRe:"7fffd4",azuY:"f0ffff",beige:"f5f5dc",bisque:"ffe4c4",black:"0",blanKedOmond:"ffebcd",Xe:"ff",XeviTet:"8a2be2",bPwn:"a52a2a",burlywood:"deb887",caMtXe:"5f9ea0",KartYuse:"7fff00",KocTate:"d2691e",cSO:"ff7f50",cSnflowerXe:"6495ed",cSnsilk:"fff8dc",crimson:"dc143c",cyan:"ffff",xXe:"8b",xcyan:"8b8b",xgTMnPd:"b8860b",xWay:"a9a9a9",xgYF:"6400",xgYy:"a9a9a9",xkhaki:"bdb76b",xmagFta:"8b008b",xTivegYF:"556b2f",xSange:"ff8c00",xScEd:"9932cc",xYd:"8b0000",xsOmon:"e9967a",xsHgYF:"8fbc8f",xUXe:"483d8b",xUWay:"2f4f4f",xUgYy:"2f4f4f",xQe:"ced1",xviTet:"9400d3",dAppRk:"ff1493",dApskyXe:"bfff",dimWay:"696969",dimgYy:"696969",dodgerXe:"1e90ff",fiYbrick:"b22222",flSOwEte:"fffaf0",foYstWAn:"228b22",fuKsia:"ff00ff",gaRsbSo:"dcdcdc",ghostwEte:"f8f8ff",gTd:"ffd700",gTMnPd:"daa520",Way:"808080",gYF:"8000",gYFLw:"adff2f",gYy:"808080",honeyMw:"f0fff0",hotpRk:"ff69b4",RdianYd:"cd5c5c",Rdigo:"4b0082",ivSy:"fffff0",khaki:"f0e68c",lavFMr:"e6e6fa",lavFMrXsh:"fff0f5",lawngYF:"7cfc00",NmoncEffon:"fffacd",ZXe:"add8e6",ZcSO:"f08080",Zcyan:"e0ffff",ZgTMnPdLw:"fafad2",ZWay:"d3d3d3",ZgYF:"90ee90",ZgYy:"d3d3d3",ZpRk:"ffb6c1",ZsOmon:"ffa07a",ZsHgYF:"20b2aa",ZskyXe:"87cefa",ZUWay:"778899",ZUgYy:"778899",ZstAlXe:"b0c4de",ZLw:"ffffe0",lime:"ff00",limegYF:"32cd32",lRF:"faf0e6",magFta:"ff00ff",maPon:"800000",VaquamarRe:"66cdaa",VXe:"cd",VScEd:"ba55d3",VpurpN:"9370db",VsHgYF:"3cb371",VUXe:"7b68ee",VsprRggYF:"fa9a",VQe:"48d1cc",VviTetYd:"c71585",midnightXe:"191970",mRtcYam:"f5fffa",mistyPse:"ffe4e1",moccasR:"ffe4b5",navajowEte:"ffdead",navy:"80",Tdlace:"fdf5e6",Tive:"808000",TivedBb:"6b8e23",Sange:"ffa500",SangeYd:"ff4500",ScEd:"da70d6",pOegTMnPd:"eee8aa",pOegYF:"98fb98",pOeQe:"afeeee",pOeviTetYd:"db7093",papayawEp:"ffefd5",pHKpuff:"ffdab9",peru:"cd853f",pRk:"ffc0cb",plum:"dda0dd",powMrXe:"b0e0e6",purpN:"800080",YbeccapurpN:"663399",Yd:"ff0000",Psybrown:"bc8f8f",PyOXe:"4169e1",saddNbPwn:"8b4513",sOmon:"fa8072",sandybPwn:"f4a460",sHgYF:"2e8b57",sHshell:"fff5ee",siFna:"a0522d",silver:"c0c0c0",skyXe:"87ceeb",UXe:"6a5acd",UWay:"708090",UgYy:"708090",snow:"fffafa",sprRggYF:"ff7f",stAlXe:"4682b4",tan:"d2b48c",teO:"8080",tEstN:"d8bfd8",tomato:"ff6347",Qe:"40e0d0",viTet:"ee82ee",JHt:"f5deb3",wEte:"ffffff",wEtesmoke:"f5f5f5",Lw:"ffff00",LwgYF:"9acd32"};let Ht;function jt(t){Ht||(Ht=function(){const t={},e=Object.keys(Nt),i=Object.keys(Wt);let s,n,o,a,r;for(s=0;s<e.length;s++){for(a=r=e[s],n=0;n<i.length;n++)o=i[n],r=r.replace(o,Wt[o]);o=parseInt(Nt[a],16),t[r]=[o>>16&255,o>>8&255,255&o]}return t}(),Ht.transparent=[0,0,0,0]);const e=Ht[t.toLowerCase()];return e&&{r:e[0],g:e[1],b:e[2],a:4===e.length?e[3]:255}}const $t=/^rgba?\(\s*([-+.\d]+)(%)?[\s,]+([-+.e\d]+)(%)?[\s,]+([-+.e\d]+)(%)?(?:[\s,/]+([-+.e\d]+)(%)?)?\s*\)$/;const Yt=t=>t<=.0031308?12.92*t:1.055*Math.pow(t,1/2.4)-.055,Ut=t=>t<=.04045?t/12.92:Math.pow((t+.055)/1.055,2.4);function Xt(t,e,i){if(t){let s=It(t);s[e]=Math.max(0,Math.min(s[e]+s[e]*i,0===e?360:1)),s=Ft(s),t.r=s[0],t.g=s[1],t.b=s[2]}}function qt(t,e){return t?Object.assign(e||{},t):t}function Kt(t){var e={r:0,g:0,b:0,a:255};return Array.isArray(t)?t.length>=3&&(e={r:t[0],g:t[1],b:t[2],a:255},t.length>3&&(e.a=Mt(t[3]))):(e=qt(t,{r:0,g:0,b:0,a:1})).a=Mt(e.a),e}function Gt(t){return"r"===t.charAt(0)?function(t){const e=$t.exec(t);let i,s,n,o=255;if(e){if(e[7]!==i){const t=+e[7];o=e[8]?vt(t):yt(255*t,0,255)}return i=+e[1],s=+e[3],n=+e[5],i=255&(e[2]?vt(i):yt(i,0,255)),s=255&(e[4]?vt(s):yt(s,0,255)),n=255&(e[6]?vt(n):yt(n,0,255)),{r:i,g:s,b:n,a:o}}}(t):Bt(t)}class Zt{constructor(t){if(t instanceof Zt)return t;const e=typeof t;let i;var s,n,o;"object"===e?i=Kt(t):"string"===e&&(o=(s=t).length,"#"===s[0]&&(4===o||5===o?n={r:255&17*St[s[1]],g:255&17*St[s[2]],b:255&17*St[s[3]],a:5===o?17*St[s[4]]:255}:7!==o&&9!==o||(n={r:St[s[1]]<<4|St[s[2]],g:St[s[3]]<<4|St[s[4]],b:St[s[5]]<<4|St[s[6]],a:9===o?St[s[7]]<<4|St[s[8]]:255})),i=n||jt(t)||Gt(t)),this._rgb=i,this._valid=!!i}get valid(){return this._valid}get rgb(){var t=qt(this._rgb);return t&&(t.a=wt(t.a)),t}set rgb(t){this._rgb=Kt(t)}rgbString(){return this._valid?(t=this._rgb)&&(t.a<255?`rgba(${t.r}, ${t.g}, ${t.b}, ${wt(t.a)})`:`rgb(${t.r}, ${t.g}, ${t.b})`):void 0;var t}hexString(){return this._valid?At(this._rgb):void 0}hslString(){return this._valid?function(t){if(!t)return;const e=It(t),i=e[0],s=kt(e[1]),n=kt(e[2]);return t.a<255?`hsla(${i}, ${s}%, ${n}%, ${wt(t.a)})`:`hsl(${i}, ${s}%, ${n}%)`}(this._rgb):void 0}mix(t,e){if(t){const i=this.rgb,s=t.rgb;let n;const o=e===n?.5:e,a=2*o-1,r=i.a-s.a,l=((a*r==-1?a:(a+r)/(1+a*r))+1)/2;n=1-l,i.r=255&l*i.r+n*s.r+.5,i.g=255&l*i.g+n*s.g+.5,i.b=255&l*i.b+n*s.b+.5,i.a=o*i.a+(1-o)*s.a,this.rgb=i}return this}interpolate(t,e){return t&&(this._rgb=function(t,e,i){const s=Ut(wt(t.r)),n=Ut(wt(t.g)),o=Ut(wt(t.b));return{r:Mt(Yt(s+i*(Ut(wt(e.r))-s))),g:Mt(Yt(n+i*(Ut(wt(e.g))-n))),b:Mt(Yt(o+i*(Ut(wt(e.b))-o))),a:t.a+i*(e.a-t.a)}}(this._rgb,t._rgb,e)),this}clone(){return new Zt(this.rgb)}alpha(t){return this._rgb.a=Mt(t),this}clearer(t){return this._rgb.a*=1-t,this}greyscale(){const t=this._rgb,e=_t(.3*t.r+.59*t.g+.11*t.b);return t.r=t.g=t.b=e,this}opaquer(t){return this._rgb.a*=1+t,this}negate(){const t=this._rgb;return t.r=255-t.r,t.g=255-t.g,t.b=255-t.b,this}lighten(t){return Xt(this._rgb,2,t),this}darken(t){return Xt(this._rgb,2,-t),this}saturate(t){return Xt(this._rgb,1,t),this}desaturate(t){return Xt(this._rgb,1,-t),this}rotate(t){return function(t,e){var i=It(t);i[0]=Vt(i[0]+e),i=Ft(i),t.r=i[0],t.g=i[1],t.b=i[2]}(this._rgb,t),this}}function Jt(t){if(t&&"object"==typeof t){const e=t.toString();return"[object CanvasPattern]"===e||"[object CanvasGradient]"===e}return!1}function Qt(t){return Jt(t)?t:new Zt(t)}function te(t){return Jt(t)?t:new Zt(t).saturate(.5).darken(.1).hexString()}const ee=["x","y","borderWidth","radius","tension"],ie=["color","borderColor","backgroundColor"];const se=new Map;function ne(t,e,i){return function(t,e){e=e||{};const i=t+JSON.stringify(e);let s=se.get(i);return s||(s=new Intl.NumberFormat(t,e),se.set(i,s)),s}(e,i).format(t)}const oe={values:t=>n(t)?t:""+t,numeric(t,e,i){if(0===t)return"0";const s=this.chart.options.locale;let n,o=t;if(i.length>1){const e=Math.max(Math.abs(i[0].value),Math.abs(i[i.length-1].value));(e<1e-4||e>1e15)&&(n="scientific"),o=function(t,e){let i=e.length>3?e[2].value-e[1].value:e[1].value-e[0].value;Math.abs(i)>=1&&t!==Math.floor(t)&&(i=t-Math.floor(t));return i}(t,i)}const a=z(Math.abs(o)),r=isNaN(a)?1:Math.max(Math.min(-1*Math.floor(a),20),0),l={notation:n,minimumFractionDigits:r,maximumFractionDigits:r};return Object.assign(l,this.options.ticks.format),ne(t,s,l)},logarithmic(t,e,i){if(0===t)return"0";const s=i[e].significand||t/Math.pow(10,Math.floor(z(t)));return[1,2,3,5,10,15].includes(s)||e>.8*i.length?oe.numeric.call(this,t,e,i):""}};var ae={formatters:oe};const re=Object.create(null),le=Object.create(null);function he(t,e){if(!e)return t;const i=e.split(".");for(let e=0,s=i.length;e<s;++e){const s=i[e];t=t[s]||(t[s]=Object.create(null))}return t}function ce(t,e,i){return"string"==typeof e?b(he(t,e),i):b(he(t,""),e)}class de{constructor(t,e){this.animation=void 0,this.backgroundColor="rgba(0,0,0,0.1)",this.borderColor="rgba(0,0,0,0.1)",this.color="#666",this.datasets={},this.devicePixelRatio=t=>t.chart.platform.getDevicePixelRatio(),this.elements={},this.events=["mousemove","mouseout","click","touchstart","touchmove"],this.font={family:"'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",size:12,style:"normal",lineHeight:1.2,weight:null},this.hover={},this.hoverBackgroundColor=(t,e)=>te(e.backgroundColor),this.hoverBorderColor=(t,e)=>te(e.borderColor),this.hoverColor=(t,e)=>te(e.color),this.indexAxis="x",this.interaction={mode:"nearest",intersect:!0,includeInvisible:!1},this.maintainAspectRatio=!0,this.onHover=null,this.onClick=null,this.parsing=!0,this.plugins={},this.responsive=!0,this.scale=void 0,this.scales={},this.showLine=!0,this.drawActiveElementsOnTop=!0,this.describe(t),this.apply(e)}set(t,e){return ce(this,t,e)}get(t){return he(this,t)}describe(t,e){return ce(le,t,e)}override(t,e){return ce(re,t,e)}route(t,e,i,s){const n=he(this,t),a=he(this,i),r="_"+e;Object.defineProperties(n,{[r]:{value:n[e],writable:!0},[e]:{enumerable:!0,get(){const t=this[r],e=a[s];return o(t)?Object.assign({},e,t):l(t,e)},set(t){this[r]=t}}})}apply(t){t.forEach((t=>t(this)))}}var ue=new de({_scriptable:t=>!t.startsWith("on"),_indexable:t=>"events"!==t,hover:{_fallback:"interaction"},interaction:{_scriptable:!1,_indexable:!1}},[function(t){t.set("animation",{delay:void 0,duration:1e3,easing:"easeOutQuart",fn:void 0,from:void 0,loop:void 0,to:void 0,type:void 0}),t.describe("animation",{_fallback:!1,_indexable:!1,_scriptable:t=>"onProgress"!==t&&"onComplete"!==t&&"fn"!==t}),t.set("animations",{colors:{type:"color",properties:ie},numbers:{type:"number",properties:ee}}),t.describe("animations",{_fallback:"animation"}),t.set("transitions",{active:{animation:{duration:400}},resize:{animation:{duration:0}},show:{animations:{colors:{from:"transparent"},visible:{type:"boolean",duration:0}}},hide:{animations:{colors:{to:"transparent"},visible:{type:"boolean",easing:"linear",fn:t=>0|t}}}})},function(t){t.set("layout",{autoPadding:!0,padding:{top:0,right:0,bottom:0,left:0}})},function(t){t.set("scale",{display:!0,offset:!1,reverse:!1,beginAtZero:!1,bounds:"ticks",clip:!0,grace:0,grid:{display:!0,lineWidth:1,drawOnChartArea:!0,drawTicks:!0,tickLength:8,tickWidth:(t,e)=>e.lineWidth,tickColor:(t,e)=>e.color,offset:!1},border:{display:!0,dash:[],dashOffset:0,width:1},title:{display:!1,text:"",padding:{top:4,bottom:4}},ticks:{minRotation:0,maxRotation:50,mirror:!1,textStrokeWidth:0,textStrokeColor:"",padding:3,display:!0,autoSkip:!0,autoSkipPadding:3,labelOffset:0,callback:ae.formatters.values,minor:{},major:{},align:"center",crossAlign:"near",showLabelBackdrop:!1,backdropColor:"rgba(255, 255, 255, 0.75)",backdropPadding:2}}),t.route("scale.ticks","color","","color"),t.route("scale.grid","color","","borderColor"),t.route("scale.border","color","","borderColor"),t.route("scale.title","color","","color"),t.describe("scale",{_fallback:!1,_scriptable:t=>!t.startsWith("before")&&!t.startsWith("after")&&"callback"!==t&&"parser"!==t,_indexable:t=>"borderDash"!==t&&"tickBorderDash"!==t&&"dash"!==t}),t.describe("scales",{_fallback:"scale"}),t.describe("scale.ticks",{_scriptable:t=>"backdropPadding"!==t&&"callback"!==t,_indexable:t=>"backdropPadding"!==t})}]);function fe(){return"undefined"!=typeof window&&"undefined"!=typeof document}function ge(t){let e=t.parentNode;return e&&"[object ShadowRoot]"===e.toString()&&(e=e.host),e}function pe(t,e,i){let s;return"string"==typeof t?(s=parseInt(t,10),-1!==t.indexOf("%")&&(s=s/100*e.parentNode[i])):s=t,s}const me=t=>t.ownerDocument.defaultView.getComputedStyle(t,null);function be(t,e){return me(t).getPropertyValue(e)}const xe=["top","right","bottom","left"];function _e(t,e,i){const s={};i=i?"-"+i:"";for(let n=0;n<4;n++){const o=xe[n];s[o]=parseFloat(t[e+"-"+o+i])||0}return s.width=s.left+s.right,s.height=s.top+s.bottom,s}const ye=(t,e,i)=>(t>0||e>0)&&(!i||!i.shadowRoot);function ve(t,e){if("native"in t)return t;const{canvas:i,currentDevicePixelRatio:s}=e,n=me(i),o="border-box"===n.boxSizing,a=_e(n,"padding"),r=_e(n,"border","width"),{x:l,y:h,box:c}=function(t,e){const i=t.touches,s=i&&i.length?i[0]:t,{offsetX:n,offsetY:o}=s;let a,r,l=!1;if(ye(n,o,t.target))a=n,r=o;else{const t=e.getBoundingClientRect();a=s.clientX-t.left,r=s.clientY-t.top,l=!0}return{x:a,y:r,box:l}}(t,i),d=a.left+(c&&r.left),u=a.top+(c&&r.top);let{width:f,height:g}=e;return o&&(f-=a.width+r.width,g-=a.height+r.height),{x:Math.round((l-d)/f*i.width/s),y:Math.round((h-u)/g*i.height/s)}}const Me=t=>Math.round(10*t)/10;function we(t,e,i,s){const n=me(t),o=_e(n,"margin"),a=pe(n.maxWidth,t,"clientWidth")||T,r=pe(n.maxHeight,t,"clientHeight")||T,l=function(t,e,i){let s,n;if(void 0===e||void 0===i){const o=ge(t);if(o){const t=o.getBoundingClientRect(),a=me(o),r=_e(a,"border","width"),l=_e(a,"padding");e=t.width-l.width-r.width,i=t.height-l.height-r.height,s=pe(a.maxWidth,o,"clientWidth"),n=pe(a.maxHeight,o,"clientHeight")}else e=t.clientWidth,i=t.clientHeight}return{width:e,height:i,maxWidth:s||T,maxHeight:n||T}}(t,e,i);let{width:h,height:c}=l;if("content-box"===n.boxSizing){const t=_e(n,"border","width"),e=_e(n,"padding");h-=e.width+t.width,c-=e.height+t.height}h=Math.max(0,h-o.width),c=Math.max(0,s?h/s:c-o.height),h=Me(Math.min(h,a,l.maxWidth)),c=Me(Math.min(c,r,l.maxHeight)),h&&!c&&(c=Me(h/2));return(void 0!==e||void 0!==i)&&s&&l.height&&c>l.height&&(c=l.height,h=Me(Math.floor(c*s))),{width:h,height:c}}function ke(t,e,i){const s=e||1,n=Math.floor(t.height*s),o=Math.floor(t.width*s);t.height=Math.floor(t.height),t.width=Math.floor(t.width);const a=t.canvas;return a.style&&(i||!a.style.height&&!a.style.width)&&(a.style.height=`${t.height}px`,a.style.width=`${t.width}px`),(t.currentDevicePixelRatio!==s||a.height!==n||a.width!==o)&&(t.currentDevicePixelRatio=s,a.height=n,a.width=o,t.ctx.setTransform(s,0,0,s,0,0),!0)}const Se=function(){let t=!1;try{const e={get passive(){return t=!0,!1}};window.addEventListener("test",null,e),window.removeEventListener("test",null,e)}catch(t){}return t}();function Pe(t,e){const i=be(t,e),s=i&&i.match(/^(\d+)(\.\d+)?px$/);return s?+s[1]:void 0}function De(t){return!t||s(t.size)||s(t.family)?null:(t.style?t.style+" ":"")+(t.weight?t.weight+" ":"")+t.size+"px "+t.family}function Ce(t,e,i,s,n){let o=e[n];return o||(o=e[n]=t.measureText(n).width,i.push(n)),o>s&&(s=o),s}function Oe(t,e,i,s){let o=(s=s||{}).data=s.data||{},a=s.garbageCollect=s.garbageCollect||[];s.font!==e&&(o=s.data={},a=s.garbageCollect=[],s.font=e),t.save(),t.font=e;let r=0;const l=i.length;let h,c,d,u,f;for(h=0;h<l;h++)if(u=i[h],null==u||n(u)){if(n(u))for(c=0,d=u.length;c<d;c++)f=u[c],null==f||n(f)||(r=Ce(t,o,a,r,f))}else r=Ce(t,o,a,r,u);t.restore();const g=a.length/2;if(g>i.length){for(h=0;h<g;h++)delete o[a[h]];a.splice(0,g)}return r}function Ae(t,e,i){const s=t.currentDevicePixelRatio,n=0!==i?Math.max(i/2,.5):0;return Math.round((e-n)*s)/s+n}function Te(t,e){(e=e||t.getContext("2d")).save(),e.resetTransform(),e.clearRect(0,0,t.width,t.height),e.restore()}function Le(t,e,i,s){Ee(t,e,i,s,null)}function Ee(t,e,i,s,n){let o,a,r,l,h,c,d,u;const f=e.pointStyle,g=e.rotation,p=e.radius;let m=(g||0)*L;if(f&&"object"==typeof f&&(o=f.toString(),"[object HTMLImageElement]"===o||"[object HTMLCanvasElement]"===o))return t.save(),t.translate(i,s),t.rotate(m),t.drawImage(f,-f.width/2,-f.height/2,f.width,f.height),void t.restore();if(!(isNaN(p)||p<=0)){switch(t.beginPath(),f){default:n?t.ellipse(i,s,n/2,p,0,0,O):t.arc(i,s,p,0,O),t.closePath();break;case"triangle":c=n?n/2:p,t.moveTo(i+Math.sin(m)*c,s-Math.cos(m)*p),m+=I,t.lineTo(i+Math.sin(m)*c,s-Math.cos(m)*p),m+=I,t.lineTo(i+Math.sin(m)*c,s-Math.cos(m)*p),t.closePath();break;case"rectRounded":h=.516*p,l=p-h,a=Math.cos(m+R)*l,d=Math.cos(m+R)*(n?n/2-h:l),r=Math.sin(m+R)*l,u=Math.sin(m+R)*(n?n/2-h:l),t.arc(i-d,s-r,h,m-C,m-E),t.arc(i+u,s-a,h,m-E,m),t.arc(i+d,s+r,h,m,m+E),t.arc(i-u,s+a,h,m+E,m+C),t.closePath();break;case"rect":if(!g){l=Math.SQRT1_2*p,c=n?n/2:l,t.rect(i-c,s-l,2*c,2*l);break}m+=R;case"rectRot":d=Math.cos(m)*(n?n/2:p),a=Math.cos(m)*p,r=Math.sin(m)*p,u=Math.sin(m)*(n?n/2:p),t.moveTo(i-d,s-r),t.lineTo(i+u,s-a),t.lineTo(i+d,s+r),t.lineTo(i-u,s+a),t.closePath();break;case"crossRot":m+=R;case"cross":d=Math.cos(m)*(n?n/2:p),a=Math.cos(m)*p,r=Math.sin(m)*p,u=Math.sin(m)*(n?n/2:p),t.moveTo(i-d,s-r),t.lineTo(i+d,s+r),t.moveTo(i+u,s-a),t.lineTo(i-u,s+a);break;case"star":d=Math.cos(m)*(n?n/2:p),a=Math.cos(m)*p,r=Math.sin(m)*p,u=Math.sin(m)*(n?n/2:p),t.moveTo(i-d,s-r),t.lineTo(i+d,s+r),t.moveTo(i+u,s-a),t.lineTo(i-u,s+a),m+=R,d=Math.cos(m)*(n?n/2:p),a=Math.cos(m)*p,r=Math.sin(m)*p,u=Math.sin(m)*(n?n/2:p),t.moveTo(i-d,s-r),t.lineTo(i+d,s+r),t.moveTo(i+u,s-a),t.lineTo(i-u,s+a);break;case"line":a=n?n/2:Math.cos(m)*p,r=Math.sin(m)*p,t.moveTo(i-a,s-r),t.lineTo(i+a,s+r);break;case"dash":t.moveTo(i,s),t.lineTo(i+Math.cos(m)*(n?n/2:p),s+Math.sin(m)*p);break;case!1:t.closePath()}t.fill(),e.borderWidth>0&&t.stroke()}}function Re(t,e,i){return i=i||.5,!e||t&&t.x>e.left-i&&t.x<e.right+i&&t.y>e.top-i&&t.y<e.bottom+i}function Ie(t,e){t.save(),t.beginPath(),t.rect(e.left,e.top,e.right-e.left,e.bottom-e.top),t.clip()}function ze(t){t.restore()}function Fe(t,e,i,s,n){if(!e)return t.lineTo(i.x,i.y);if("middle"===n){const s=(e.x+i.x)/2;t.lineTo(s,e.y),t.lineTo(s,i.y)}else"after"===n!=!!s?t.lineTo(e.x,i.y):t.lineTo(i.x,e.y);t.lineTo(i.x,i.y)}function Ve(t,e,i,s){if(!e)return t.lineTo(i.x,i.y);t.bezierCurveTo(s?e.cp1x:e.cp2x,s?e.cp1y:e.cp2y,s?i.cp2x:i.cp1x,s?i.cp2y:i.cp1y,i.x,i.y)}function Be(t,e,i,s,n){if(n.strikethrough||n.underline){const o=t.measureText(s),a=e-o.actualBoundingBoxLeft,r=e+o.actualBoundingBoxRight,l=i-o.actualBoundingBoxAscent,h=i+o.actualBoundingBoxDescent,c=n.strikethrough?(l+h)/2:h;t.strokeStyle=t.fillStyle,t.beginPath(),t.lineWidth=n.decorationWidth||2,t.moveTo(a,c),t.lineTo(r,c),t.stroke()}}function We(t,e){const i=t.fillStyle;t.fillStyle=e.color,t.fillRect(e.left,e.top,e.width,e.height),t.fillStyle=i}function Ne(t,e,i,o,a,r={}){const l=n(e)?e:[e],h=r.strokeWidth>0&&""!==r.strokeColor;let c,d;for(t.save(),t.font=a.string,function(t,e){e.translation&&t.translate(e.translation[0],e.translation[1]),s(e.rotation)||t.rotate(e.rotation),e.color&&(t.fillStyle=e.color),e.textAlign&&(t.textAlign=e.textAlign),e.textBaseline&&(t.textBaseline=e.textBaseline)}(t,r),c=0;c<l.length;++c)d=l[c],r.backdrop&&We(t,r.backdrop),h&&(r.strokeColor&&(t.strokeStyle=r.strokeColor),s(r.strokeWidth)||(t.lineWidth=r.strokeWidth),t.strokeText(d,i,o,r.maxWidth)),t.fillText(d,i,o,r.maxWidth),Be(t,i,o,d,r),o+=Number(a.lineHeight);t.restore()}function He(t,e){const{x:i,y:s,w:n,h:o,radius:a}=e;t.arc(i+a.topLeft,s+a.topLeft,a.topLeft,1.5*C,C,!0),t.lineTo(i,s+o-a.bottomLeft),t.arc(i+a.bottomLeft,s+o-a.bottomLeft,a.bottomLeft,C,E,!0),t.lineTo(i+n-a.bottomRight,s+o),t.arc(i+n-a.bottomRight,s+o-a.bottomRight,a.bottomRight,E,0,!0),t.lineTo(i+n,s+a.topRight),t.arc(i+n-a.topRight,s+a.topRight,a.topRight,0,-E,!0),t.lineTo(i+a.topLeft,s)}function je(t,e=[""],i,s,n=(()=>t[0])){const o=i||t;void 0===s&&(s=ti("_fallback",t));const a={[Symbol.toStringTag]:"Object",_cacheable:!0,_scopes:t,_rootScopes:o,_fallback:s,_getTarget:n,override:i=>je([i,...t],e,o,s)};return new Proxy(a,{deleteProperty:(e,i)=>(delete e[i],delete e._keys,delete t[0][i],!0),get:(i,s)=>qe(i,s,(()=>function(t,e,i,s){let n;for(const o of e)if(n=ti(Ue(o,t),i),void 0!==n)return Xe(t,n)?Je(i,s,t,n):n}(s,e,t,i))),getOwnPropertyDescriptor:(t,e)=>Reflect.getOwnPropertyDescriptor(t._scopes[0],e),getPrototypeOf:()=>Reflect.getPrototypeOf(t[0]),has:(t,e)=>ei(t).includes(e),ownKeys:t=>ei(t),set(t,e,i){const s=t._storage||(t._storage=n());return t[e]=s[e]=i,delete t._keys,!0}})}function $e(t,e,i,s){const a={_cacheable:!1,_proxy:t,_context:e,_subProxy:i,_stack:new Set,_descriptors:Ye(t,s),setContext:e=>$e(t,e,i,s),override:n=>$e(t.override(n),e,i,s)};return new Proxy(a,{deleteProperty:(e,i)=>(delete e[i],delete t[i],!0),get:(t,e,i)=>qe(t,e,(()=>function(t,e,i){const{_proxy:s,_context:a,_subProxy:r,_descriptors:l}=t;let h=s[e];S(h)&&l.isScriptable(e)&&(h=function(t,e,i,s){const{_proxy:n,_context:o,_subProxy:a,_stack:r}=i;if(r.has(t))throw new Error("Recursion detected: "+Array.from(r).join("->")+"->"+t);r.add(t);let l=e(o,a||s);r.delete(t),Xe(t,l)&&(l=Je(n._scopes,n,t,l));return l}(e,h,t,i));n(h)&&h.length&&(h=function(t,e,i,s){const{_proxy:n,_context:a,_subProxy:r,_descriptors:l}=i;if(void 0!==a.index&&s(t))return e[a.index%e.length];if(o(e[0])){const i=e,s=n._scopes.filter((t=>t!==i));e=[];for(const o of i){const i=Je(s,n,t,o);e.push($e(i,a,r&&r[t],l))}}return e}(e,h,t,l.isIndexable));Xe(e,h)&&(h=$e(h,a,r&&r[e],l));return h}(t,e,i))),getOwnPropertyDescriptor:(e,i)=>e._descriptors.allKeys?Reflect.has(t,i)?{enumerable:!0,configurable:!0}:void 0:Reflect.getOwnPropertyDescriptor(t,i),getPrototypeOf:()=>Reflect.getPrototypeOf(t),has:(e,i)=>Reflect.has(t,i),ownKeys:()=>Reflect.ownKeys(t),set:(e,i,s)=>(t[i]=s,delete e[i],!0)})}function Ye(t,e={scriptable:!0,indexable:!0}){const{_scriptable:i=e.scriptable,_indexable:s=e.indexable,_allKeys:n=e.allKeys}=t;return{allKeys:n,scriptable:i,indexable:s,isScriptable:S(i)?i:()=>i,isIndexable:S(s)?s:()=>s}}const Ue=(t,e)=>t?t+w(e):e,Xe=(t,e)=>o(e)&&"adapters"!==t&&(null===Object.getPrototypeOf(e)||e.constructor===Object);function qe(t,e,i){if(Object.prototype.hasOwnProperty.call(t,e))return t[e];const s=i();return t[e]=s,s}function Ke(t,e,i){return S(t)?t(e,i):t}const Ge=(t,e)=>!0===t?e:"string"==typeof t?M(e,t):void 0;function Ze(t,e,i,s,n){for(const o of e){const e=Ge(i,o);if(e){t.add(e);const o=Ke(e._fallback,i,n);if(void 0!==o&&o!==i&&o!==s)return o}else if(!1===e&&void 0!==s&&i!==s)return null}return!1}function Je(t,e,i,s){const a=e._rootScopes,r=Ke(e._fallback,i,s),l=[...t,...a],h=new Set;h.add(s);let c=Qe(h,l,i,r||i,s);return null!==c&&((void 0===r||r===i||(c=Qe(h,l,r,c,s),null!==c))&&je(Array.from(h),[""],a,r,(()=>function(t,e,i){const s=t._getTarget();e in s||(s[e]={});const a=s[e];if(n(a)&&o(i))return i;return a||{}}(e,i,s))))}function Qe(t,e,i,s,n){for(;i;)i=Ze(t,e,i,s,n);return i}function ti(t,e){for(const i of e){if(!i)continue;const e=i[t];if(void 0!==e)return e}}function ei(t){let e=t._keys;return e||(e=t._keys=function(t){const e=new Set;for(const i of t)for(const t of Object.keys(i).filter((t=>!t.startsWith("_"))))e.add(t);return Array.from(e)}(t._scopes)),e}function ii(t,e,i,s){const{iScale:n}=t,{key:o="r"}=this._parsing,a=new Array(s);let r,l,h,c;for(r=0,l=s;r<l;++r)h=r+i,c=e[h],a[r]={r:n.parse(M(c,o),h)};return a}const si=Number.EPSILON||1e-14,ni=(t,e)=>e<t.length&&!t[e].skip&&t[e],oi=t=>"x"===t?"y":"x";function ai(t,e,i,s){const n=t.skip?e:t,o=e,a=i.skip?e:i,r=q(o,n),l=q(a,o);let h=r/(r+l),c=l/(r+l);h=isNaN(h)?0:h,c=isNaN(c)?0:c;const d=s*h,u=s*c;return{previous:{x:o.x-d*(a.x-n.x),y:o.y-d*(a.y-n.y)},next:{x:o.x+u*(a.x-n.x),y:o.y+u*(a.y-n.y)}}}function ri(t,e="x"){const i=oi(e),s=t.length,n=Array(s).fill(0),o=Array(s);let a,r,l,h=ni(t,0);for(a=0;a<s;++a)if(r=l,l=h,h=ni(t,a+1),l){if(h){const t=h[e]-l[e];n[a]=0!==t?(h[i]-l[i])/t:0}o[a]=r?h?F(n[a-1])!==F(n[a])?0:(n[a-1]+n[a])/2:n[a-1]:n[a]}!function(t,e,i){const s=t.length;let n,o,a,r,l,h=ni(t,0);for(let c=0;c<s-1;++c)l=h,h=ni(t,c+1),l&&h&&(V(e[c],0,si)?i[c]=i[c+1]=0:(n=i[c]/e[c],o=i[c+1]/e[c],r=Math.pow(n,2)+Math.pow(o,2),r<=9||(a=3/Math.sqrt(r),i[c]=n*a*e[c],i[c+1]=o*a*e[c])))}(t,n,o),function(t,e,i="x"){const s=oi(i),n=t.length;let o,a,r,l=ni(t,0);for(let h=0;h<n;++h){if(a=r,r=l,l=ni(t,h+1),!r)continue;const n=r[i],c=r[s];a&&(o=(n-a[i])/3,r[`cp1${i}`]=n-o,r[`cp1${s}`]=c-o*e[h]),l&&(o=(l[i]-n)/3,r[`cp2${i}`]=n+o,r[`cp2${s}`]=c+o*e[h])}}(t,o,e)}function li(t,e,i){return Math.max(Math.min(t,i),e)}function hi(t,e,i,s,n){let o,a,r,l;if(e.spanGaps&&(t=t.filter((t=>!t.skip))),"monotone"===e.cubicInterpolationMode)ri(t,n);else{let i=s?t[t.length-1]:t[0];for(o=0,a=t.length;o<a;++o)r=t[o],l=ai(i,r,t[Math.min(o+1,a-(s?0:1))%a],e.tension),r.cp1x=l.previous.x,r.cp1y=l.previous.y,r.cp2x=l.next.x,r.cp2y=l.next.y,i=r}e.capBezierPoints&&function(t,e){let i,s,n,o,a,r=Re(t[0],e);for(i=0,s=t.length;i<s;++i)a=o,o=r,r=i<s-1&&Re(t[i+1],e),o&&(n=t[i],a&&(n.cp1x=li(n.cp1x,e.left,e.right),n.cp1y=li(n.cp1y,e.top,e.bottom)),r&&(n.cp2x=li(n.cp2x,e.left,e.right),n.cp2y=li(n.cp2y,e.top,e.bottom)))}(t,i)}const ci=t=>0===t||1===t,di=(t,e,i)=>-Math.pow(2,10*(t-=1))*Math.sin((t-e)*O/i),ui=(t,e,i)=>Math.pow(2,-10*t)*Math.sin((t-e)*O/i)+1,fi={linear:t=>t,easeInQuad:t=>t*t,easeOutQuad:t=>-t*(t-2),easeInOutQuad:t=>(t/=.5)<1?.5*t*t:-.5*(--t*(t-2)-1),easeInCubic:t=>t*t*t,easeOutCubic:t=>(t-=1)*t*t+1,easeInOutCubic:t=>(t/=.5)<1?.5*t*t*t:.5*((t-=2)*t*t+2),easeInQuart:t=>t*t*t*t,easeOutQuart:t=>-((t-=1)*t*t*t-1),easeInOutQuart:t=>(t/=.5)<1?.5*t*t*t*t:-.5*((t-=2)*t*t*t-2),easeInQuint:t=>t*t*t*t*t,easeOutQuint:t=>(t-=1)*t*t*t*t+1,easeInOutQuint:t=>(t/=.5)<1?.5*t*t*t*t*t:.5*((t-=2)*t*t*t*t+2),easeInSine:t=>1-Math.cos(t*E),easeOutSine:t=>Math.sin(t*E),easeInOutSine:t=>-.5*(Math.cos(C*t)-1),easeInExpo:t=>0===t?0:Math.pow(2,10*(t-1)),easeOutExpo:t=>1===t?1:1-Math.pow(2,-10*t),easeInOutExpo:t=>ci(t)?t:t<.5?.5*Math.pow(2,10*(2*t-1)):.5*(2-Math.pow(2,-10*(2*t-1))),easeInCirc:t=>t>=1?t:-(Math.sqrt(1-t*t)-1),easeOutCirc:t=>Math.sqrt(1-(t-=1)*t),easeInOutCirc:t=>(t/=.5)<1?-.5*(Math.sqrt(1-t*t)-1):.5*(Math.sqrt(1-(t-=2)*t)+1),easeInElastic:t=>ci(t)?t:di(t,.075,.3),easeOutElastic:t=>ci(t)?t:ui(t,.075,.3),easeInOutElastic(t){const e=.1125;return ci(t)?t:t<.5?.5*di(2*t,e,.45):.5+.5*ui(2*t-1,e,.45)},easeInBack(t){const e=1.70158;return t*t*((e+1)*t-e)},easeOutBack(t){const e=1.70158;return(t-=1)*t*((e+1)*t+e)+1},easeInOutBack(t){let e=1.70158;return(t/=.5)<1?t*t*((1+(e*=1.525))*t-e)*.5:.5*((t-=2)*t*((1+(e*=1.525))*t+e)+2)},easeInBounce:t=>1-fi.easeOutBounce(1-t),easeOutBounce(t){const e=7.5625,i=2.75;return t<1/i?e*t*t:t<2/i?e*(t-=1.5/i)*t+.75:t<2.5/i?e*(t-=2.25/i)*t+.9375:e*(t-=2.625/i)*t+.984375},easeInOutBounce:t=>t<.5?.5*fi.easeInBounce(2*t):.5*fi.easeOutBounce(2*t-1)+.5};function gi(t,e,i,s){return{x:t.x+i*(e.x-t.x),y:t.y+i*(e.y-t.y)}}function pi(t,e,i,s){return{x:t.x+i*(e.x-t.x),y:"middle"===s?i<.5?t.y:e.y:"after"===s?i<1?t.y:e.y:i>0?e.y:t.y}}function mi(t,e,i,s){const n={x:t.cp2x,y:t.cp2y},o={x:e.cp1x,y:e.cp1y},a=gi(t,n,i),r=gi(n,o,i),l=gi(o,e,i),h=gi(a,r,i),c=gi(r,l,i);return gi(h,c,i)}const bi=/^(normal|(\d+(?:\.\d+)?)(px|em|%)?)$/,xi=/^(normal|italic|initial|inherit|unset|(oblique( -?[0-9]?[0-9]deg)?))$/;function _i(t,e){const i=(""+t).match(bi);if(!i||"normal"===i[1])return 1.2*e;switch(t=+i[2],i[3]){case"px":return t;case"%":t/=100}return e*t}const yi=t=>+t||0;function vi(t,e){const i={},s=o(e),n=s?Object.keys(e):e,a=o(t)?s?i=>l(t[i],t[e[i]]):e=>t[e]:()=>t;for(const t of n)i[t]=yi(a(t));return i}function Mi(t){return vi(t,{top:"y",right:"x",bottom:"y",left:"x"})}function wi(t){return vi(t,["topLeft","topRight","bottomLeft","bottomRight"])}function ki(t){const e=Mi(t);return e.width=e.left+e.right,e.height=e.top+e.bottom,e}function Si(t,e){t=t||{},e=e||ue.font;let i=l(t.size,e.size);"string"==typeof i&&(i=parseInt(i,10));let s=l(t.style,e.style);s&&!(""+s).match(xi)&&(console.warn('Invalid font style specified: "'+s+'"'),s=void 0);const n={family:l(t.family,e.family),lineHeight:_i(l(t.lineHeight,e.lineHeight),i),size:i,style:s,weight:l(t.weight,e.weight),string:""};return n.string=De(n),n}function Pi(t,e,i,s){let o,a,r,l=!0;for(o=0,a=t.length;o<a;++o)if(r=t[o],void 0!==r&&(void 0!==e&&"function"==typeof r&&(r=r(e),l=!1),void 0!==i&&n(r)&&(r=r[i%r.length],l=!1),void 0!==r))return s&&!l&&(s.cacheable=!1),r}function Di(t,e,i){const{min:s,max:n}=t,o=c(e,(n-s)/2),a=(t,e)=>i&&0===t?0:t+e;return{min:a(s,-Math.abs(o)),max:a(n,o)}}function Ci(t,e){return Object.assign(Object.create(t),e)}function Oi(t,e,i){return t?function(t,e){return{x:i=>t+t+e-i,setWidth(t){e=t},textAlign:t=>"center"===t?t:"right"===t?"left":"right",xPlus:(t,e)=>t-e,leftForLtr:(t,e)=>t-e}}(e,i):{x:t=>t,setWidth(t){},textAlign:t=>t,xPlus:(t,e)=>t+e,leftForLtr:(t,e)=>t}}function Ai(t,e){let i,s;"ltr"!==e&&"rtl"!==e||(i=t.canvas.style,s=[i.getPropertyValue("direction"),i.getPropertyPriority("direction")],i.setProperty("direction",e,"important"),t.prevTextDirection=s)}function Ti(t,e){void 0!==e&&(delete t.prevTextDirection,t.canvas.style.setProperty("direction",e[0],e[1]))}function Li(t){return"angle"===t?{between:Z,compare:K,normalize:G}:{between:tt,compare:(t,e)=>t-e,normalize:t=>t}}function Ei({start:t,end:e,count:i,loop:s,style:n}){return{start:t%i,end:e%i,loop:s&&(e-t+1)%i==0,style:n}}function Ri(t,e,i){if(!i)return[t];const{property:s,start:n,end:o}=i,a=e.length,{compare:r,between:l,normalize:h}=Li(s),{start:c,end:d,loop:u,style:f}=function(t,e,i){const{property:s,start:n,end:o}=i,{between:a,normalize:r}=Li(s),l=e.length;let h,c,{start:d,end:u,loop:f}=t;if(f){for(d+=l,u+=l,h=0,c=l;h<c&&a(r(e[d%l][s]),n,o);++h)d--,u--;d%=l,u%=l}return u<d&&(u+=l),{start:d,end:u,loop:f,style:t.style}}(t,e,i),g=[];let p,m,b,x=!1,_=null;const y=()=>x||l(n,b,p)&&0!==r(n,b),v=()=>!x||0===r(o,p)||l(o,b,p);for(let t=c,i=c;t<=d;++t)m=e[t%a],m.skip||(p=h(m[s]),p!==b&&(x=l(p,n,o),null===_&&y()&&(_=0===r(p,n)?t:i),null!==_&&v()&&(g.push(Ei({start:_,end:t,loop:u,count:a,style:f})),_=null),i=t,b=p));return null!==_&&g.push(Ei({start:_,end:d,loop:u,count:a,style:f})),g}function Ii(t,e){const i=[],s=t.segments;for(let n=0;n<s.length;n++){const o=Ri(s[n],t.points,e);o.length&&i.push(...o)}return i}function zi(t,e){const i=t.points,s=t.options.spanGaps,n=i.length;if(!n)return[];const o=!!t._loop,{start:a,end:r}=function(t,e,i,s){let n=0,o=e-1;if(i&&!s)for(;n<e&&!t[n].skip;)n++;for(;n<e&&t[n].skip;)n++;for(n%=e,i&&(o+=n);o>n&&t[o%e].skip;)o--;return o%=e,{start:n,end:o}}(i,n,o,s);if(!0===s)return Fi(t,[{start:a,end:r,loop:o}],i,e);return Fi(t,function(t,e,i,s){const n=t.length,o=[];let a,r=e,l=t[e];for(a=e+1;a<=i;++a){const i=t[a%n];i.skip||i.stop?l.skip||(s=!1,o.push({start:e%n,end:(a-1)%n,loop:s}),e=r=i.stop?a:null):(r=a,l.skip&&(e=a)),l=i}return null!==r&&o.push({start:e%n,end:r%n,loop:s}),o}(i,a,r<a?r+n:r,!!t._fullLoop&&0===a&&r===n-1),i,e)}function Fi(t,e,i,s){return s&&s.setContext&&i?function(t,e,i,s){const n=t._chart.getContext(),o=Vi(t.options),{_datasetIndex:a,options:{spanGaps:r}}=t,l=i.length,h=[];let c=o,d=e[0].start,u=d;function f(t,e,s,n){const o=r?-1:1;if(t!==e){for(t+=l;i[t%l].skip;)t-=o;for(;i[e%l].skip;)e+=o;t%l!=e%l&&(h.push({start:t%l,end:e%l,loop:s,style:n}),c=n,d=e%l)}}for(const t of e){d=r?d:t.start;let e,o=i[d%l];for(u=d+1;u<=t.end;u++){const r=i[u%l];e=Vi(s.setContext(Ci(n,{type:"segment",p0:o,p1:r,p0DataIndex:(u-1)%l,p1DataIndex:u%l,datasetIndex:a}))),Bi(e,c)&&f(d,u-1,t.loop,c),o=r,c=e}d<u-1&&f(d,u-1,t.loop,c)}return h}(t,e,i,s):e}function Vi(t){return{backgroundColor:t.backgroundColor,borderCapStyle:t.borderCapStyle,borderDash:t.borderDash,borderDashOffset:t.borderDashOffset,borderJoinStyle:t.borderJoinStyle,borderWidth:t.borderWidth,borderColor:t.borderColor}}function Bi(t,e){if(!e)return!1;const i=[],s=function(t,e){return Jt(e)?(i.includes(e)||i.push(e),i.indexOf(e)):e};return JSON.stringify(t,s)!==JSON.stringify(e,s)}var Wi=Object.freeze({__proto__:null,HALF_PI:E,INFINITY:T,PI:C,PITAU:A,QUARTER_PI:R,RAD_PER_DEG:L,TAU:O,TWO_THIRDS_PI:I,_addGrace:Di,_alignPixel:Ae,_alignStartEnd:ft,_angleBetween:Z,_angleDiff:K,_arrayUnique:lt,_attachContext:$e,_bezierCurveTo:Ve,_bezierInterpolation:mi,_boundSegment:Ri,_boundSegments:Ii,_capitalize:w,_computeSegments:zi,_createResolver:je,_decimalPlaces:U,_deprecated:function(t,e,i,s){void 0!==e&&console.warn(t+': "'+i+'" is deprecated. Please use "'+s+'" instead')},_descriptors:Ye,_elementsEqual:f,_factorize:W,_filterBetween:nt,_getParentNode:ge,_getStartAndCountOfVisiblePoints:pt,_int16Range:Q,_isBetween:tt,_isClickEvent:D,_isDomSupported:fe,_isPointInArea:Re,_limitValue:J,_longestText:Oe,_lookup:et,_lookupByKey:it,_measureText:Ce,_merger:m,_mergerIf:_,_normalizeAngle:G,_parseObjectDataRadialScale:ii,_pointInLine:gi,_readValueToProps:vi,_rlookupByKey:st,_scaleRangesChanged:mt,_setMinAndMaxByKey:j,_splitKey:v,_steppedInterpolation:pi,_steppedLineTo:Fe,_textX:gt,_toLeftRightCenter:ut,_updateBezierControlPoints:hi,addRoundedRectPath:He,almostEquals:V,almostWhole:H,callback:d,clearCanvas:Te,clipArea:Ie,clone:g,color:Qt,createContext:Ci,debounce:dt,defined:k,distanceBetweenPoints:q,drawPoint:Le,drawPointLegend:Ee,each:u,easingEffects:fi,finiteOrDefault:r,fontString:function(t,e,i){return e+" "+t+"px "+i},formatNumber:ne,getAngleFromPoint:X,getHoverColor:te,getMaximumSize:we,getRelativePosition:ve,getRtlAdapter:Oi,getStyle:be,isArray:n,isFinite:a,isFunction:S,isNullOrUndef:s,isNumber:N,isObject:o,isPatternOrGradient:Jt,listenArrayEvents:at,log10:z,merge:b,mergeIf:x,niceNum:B,noop:e,overrideTextDirection:Ai,readUsedSize:Pe,renderText:Ne,requestAnimFrame:ht,resolve:Pi,resolveObjectKey:M,restoreTextDirection:Ti,retinaScale:ke,setsEqual:P,sign:F,splineCurve:ai,splineCurveMonotone:ri,supportsEventListenerOptions:Se,throttled:ct,toDegrees:Y,toDimension:c,toFont:Si,toFontString:De,toLineHeight:_i,toPadding:ki,toPercentage:h,toRadians:$,toTRBL:Mi,toTRBLCorners:wi,uid:i,unclipArea:ze,unlistenArrayEvents:rt,valueOrDefault:l});function Ni(t,e,i,s){const{controller:n,data:o,_sorted:a}=t,r=n._cachedMeta.iScale;if(r&&e===r.axis&&"r"!==e&&a&&o.length){const t=r._reversePixels?st:it;if(!s)return t(o,e,i);if(n._sharedOptions){const s=o[0],n="function"==typeof s.getRange&&s.getRange(e);if(n){const s=t(o,e,i-n),a=t(o,e,i+n);return{lo:s.lo,hi:a.hi}}}}return{lo:0,hi:o.length-1}}function Hi(t,e,i,s,n){const o=t.getSortedVisibleDatasetMetas(),a=i[e];for(let t=0,i=o.length;t<i;++t){const{index:i,data:r}=o[t],{lo:l,hi:h}=Ni(o[t],e,a,n);for(let t=l;t<=h;++t){const e=r[t];e.skip||s(e,i,t)}}}function ji(t,e,i,s,n){const o=[];if(!n&&!t.isPointInArea(e))return o;return Hi(t,i,e,(function(i,a,r){(n||Re(i,t.chartArea,0))&&i.inRange(e.x,e.y,s)&&o.push({element:i,datasetIndex:a,index:r})}),!0),o}function $i(t,e,i,s,n,o){let a=[];const r=function(t){const e=-1!==t.indexOf("x"),i=-1!==t.indexOf("y");return function(t,s){const n=e?Math.abs(t.x-s.x):0,o=i?Math.abs(t.y-s.y):0;return Math.sqrt(Math.pow(n,2)+Math.pow(o,2))}}(i);let l=Number.POSITIVE_INFINITY;return Hi(t,i,e,(function(i,h,c){const d=i.inRange(e.x,e.y,n);if(s&&!d)return;const u=i.getCenterPoint(n);if(!(!!o||t.isPointInArea(u))&&!d)return;const f=r(e,u);f<l?(a=[{element:i,datasetIndex:h,index:c}],l=f):f===l&&a.push({element:i,datasetIndex:h,index:c})})),a}function Yi(t,e,i,s,n,o){return o||t.isPointInArea(e)?"r"!==i||s?$i(t,e,i,s,n,o):function(t,e,i,s){let n=[];return Hi(t,i,e,(function(t,i,o){const{startAngle:a,endAngle:r}=t.getProps(["startAngle","endAngle"],s),{angle:l}=X(t,{x:e.x,y:e.y});Z(l,a,r)&&n.push({element:t,datasetIndex:i,index:o})})),n}(t,e,i,n):[]}function Ui(t,e,i,s,n){const o=[],a="x"===i?"inXRange":"inYRange";let r=!1;return Hi(t,i,e,((t,s,l)=>{t[a](e[i],n)&&(o.push({element:t,datasetIndex:s,index:l}),r=r||t.inRange(e.x,e.y,n))})),s&&!r?[]:o}var Xi={evaluateInteractionItems:Hi,modes:{index(t,e,i,s){const n=ve(e,t),o=i.axis||"x",a=i.includeInvisible||!1,r=i.intersect?ji(t,n,o,s,a):Yi(t,n,o,!1,s,a),l=[];return r.length?(t.getSortedVisibleDatasetMetas().forEach((t=>{const e=r[0].index,i=t.data[e];i&&!i.skip&&l.push({element:i,datasetIndex:t.index,index:e})})),l):[]},dataset(t,e,i,s){const n=ve(e,t),o=i.axis||"xy",a=i.includeInvisible||!1;let r=i.intersect?ji(t,n,o,s,a):Yi(t,n,o,!1,s,a);if(r.length>0){const e=r[0].datasetIndex,i=t.getDatasetMeta(e).data;r=[];for(let t=0;t<i.length;++t)r.push({element:i[t],datasetIndex:e,index:t})}return r},point:(t,e,i,s)=>ji(t,ve(e,t),i.axis||"xy",s,i.includeInvisible||!1),nearest(t,e,i,s){const n=ve(e,t),o=i.axis||"xy",a=i.includeInvisible||!1;return Yi(t,n,o,i.intersect,s,a)},x:(t,e,i,s)=>Ui(t,ve(e,t),"x",i.intersect,s),y:(t,e,i,s)=>Ui(t,ve(e,t),"y",i.intersect,s)}};const qi=["left","top","right","bottom"];function Ki(t,e){return t.filter((t=>t.pos===e))}function Gi(t,e){return t.filter((t=>-1===qi.indexOf(t.pos)&&t.box.axis===e))}function Zi(t,e){return t.sort(((t,i)=>{const s=e?i:t,n=e?t:i;return s.weight===n.weight?s.index-n.index:s.weight-n.weight}))}function Ji(t,e){const i=function(t){const e={};for(const i of t){const{stack:t,pos:s,stackWeight:n}=i;if(!t||!qi.includes(s))continue;const o=e[t]||(e[t]={count:0,placed:0,weight:0,size:0});o.count++,o.weight+=n}return e}(t),{vBoxMaxWidth:s,hBoxMaxHeight:n}=e;let o,a,r;for(o=0,a=t.length;o<a;++o){r=t[o];const{fullSize:a}=r.box,l=i[r.stack],h=l&&r.stackWeight/l.weight;r.horizontal?(r.width=h?h*s:a&&e.availableWidth,r.height=n):(r.width=s,r.height=h?h*n:a&&e.availableHeight)}return i}function Qi(t,e,i,s){return Math.max(t[i],e[i])+Math.max(t[s],e[s])}function ts(t,e){t.top=Math.max(t.top,e.top),t.left=Math.max(t.left,e.left),t.bottom=Math.max(t.bottom,e.bottom),t.right=Math.max(t.right,e.right)}function es(t,e,i,s){const{pos:n,box:a}=i,r=t.maxPadding;if(!o(n)){i.size&&(t[n]-=i.size);const e=s[i.stack]||{size:0,count:1};e.size=Math.max(e.size,i.horizontal?a.height:a.width),i.size=e.size/e.count,t[n]+=i.size}a.getPadding&&ts(r,a.getPadding());const l=Math.max(0,e.outerWidth-Qi(r,t,"left","right")),h=Math.max(0,e.outerHeight-Qi(r,t,"top","bottom")),c=l!==t.w,d=h!==t.h;return t.w=l,t.h=h,i.horizontal?{same:c,other:d}:{same:d,other:c}}function is(t,e){const i=e.maxPadding;function s(t){const s={left:0,top:0,right:0,bottom:0};return t.forEach((t=>{s[t]=Math.max(e[t],i[t])})),s}return s(t?["left","right"]:["top","bottom"])}function ss(t,e,i,s){const n=[];let o,a,r,l,h,c;for(o=0,a=t.length,h=0;o<a;++o){r=t[o],l=r.box,l.update(r.width||e.w,r.height||e.h,is(r.horizontal,e));const{same:a,other:d}=es(e,i,r,s);h|=a&&n.length,c=c||d,l.fullSize||n.push(r)}return h&&ss(n,e,i,s)||c}function ns(t,e,i,s,n){t.top=i,t.left=e,t.right=e+s,t.bottom=i+n,t.width=s,t.height=n}function os(t,e,i,s){const n=i.padding;let{x:o,y:a}=e;for(const r of t){const t=r.box,l=s[r.stack]||{count:1,placed:0,weight:1},h=r.stackWeight/l.weight||1;if(r.horizontal){const s=e.w*h,o=l.size||t.height;k(l.start)&&(a=l.start),t.fullSize?ns(t,n.left,a,i.outerWidth-n.right-n.left,o):ns(t,e.left+l.placed,a,s,o),l.start=a,l.placed+=s,a=t.bottom}else{const s=e.h*h,a=l.size||t.width;k(l.start)&&(o=l.start),t.fullSize?ns(t,o,n.top,a,i.outerHeight-n.bottom-n.top):ns(t,o,e.top+l.placed,a,s),l.start=o,l.placed+=s,o=t.right}}e.x=o,e.y=a}var as={addBox(t,e){t.boxes||(t.boxes=[]),e.fullSize=e.fullSize||!1,e.position=e.position||"top",e.weight=e.weight||0,e._layers=e._layers||function(){return[{z:0,draw(t){e.draw(t)}}]},t.boxes.push(e)},removeBox(t,e){const i=t.boxes?t.boxes.indexOf(e):-1;-1!==i&&t.boxes.splice(i,1)},configure(t,e,i){e.fullSize=i.fullSize,e.position=i.position,e.weight=i.weight},update(t,e,i,s){if(!t)return;const n=ki(t.options.layout.padding),o=Math.max(e-n.width,0),a=Math.max(i-n.height,0),r=function(t){const e=function(t){const e=[];let i,s,n,o,a,r;for(i=0,s=(t||[]).length;i<s;++i)n=t[i],({position:o,options:{stack:a,stackWeight:r=1}}=n),e.push({index:i,box:n,pos:o,horizontal:n.isHorizontal(),weight:n.weight,stack:a&&o+a,stackWeight:r});return e}(t),i=Zi(e.filter((t=>t.box.fullSize)),!0),s=Zi(Ki(e,"left"),!0),n=Zi(Ki(e,"right")),o=Zi(Ki(e,"top"),!0),a=Zi(Ki(e,"bottom")),r=Gi(e,"x"),l=Gi(e,"y");return{fullSize:i,leftAndTop:s.concat(o),rightAndBottom:n.concat(l).concat(a).concat(r),chartArea:Ki(e,"chartArea"),vertical:s.concat(n).concat(l),horizontal:o.concat(a).concat(r)}}(t.boxes),l=r.vertical,h=r.horizontal;u(t.boxes,(t=>{"function"==typeof t.beforeLayout&&t.beforeLayout()}));const c=l.reduce(((t,e)=>e.box.options&&!1===e.box.options.display?t:t+1),0)||1,d=Object.freeze({outerWidth:e,outerHeight:i,padding:n,availableWidth:o,availableHeight:a,vBoxMaxWidth:o/2/c,hBoxMaxHeight:a/2}),f=Object.assign({},n);ts(f,ki(s));const g=Object.assign({maxPadding:f,w:o,h:a,x:n.left,y:n.top},n),p=Ji(l.concat(h),d);ss(r.fullSize,g,d,p),ss(l,g,d,p),ss(h,g,d,p)&&ss(l,g,d,p),function(t){const e=t.maxPadding;function i(i){const s=Math.max(e[i]-t[i],0);return t[i]+=s,s}t.y+=i("top"),t.x+=i("left"),i("right"),i("bottom")}(g),os(r.leftAndTop,g,d,p),g.x+=g.w,g.y+=g.h,os(r.rightAndBottom,g,d,p),t.chartArea={left:g.left,top:g.top,right:g.left+g.w,bottom:g.top+g.h,height:g.h,width:g.w},u(r.chartArea,(e=>{const i=e.box;Object.assign(i,t.chartArea),i.update(g.w,g.h,{left:0,top:0,right:0,bottom:0})}))}};class rs{acquireContext(t,e){}releaseContext(t){return!1}addEventListener(t,e,i){}removeEventListener(t,e,i){}getDevicePixelRatio(){return 1}getMaximumSize(t,e,i,s){return e=Math.max(0,e||t.width),i=i||t.height,{width:e,height:Math.max(0,s?Math.floor(e/s):i)}}isAttached(t){return!0}updateConfig(t){}}class ls extends rs{acquireContext(t){return t&&t.getContext&&t.getContext("2d")||null}updateConfig(t){t.options.animation=!1}}const hs="$chartjs",cs={touchstart:"mousedown",touchmove:"mousemove",touchend:"mouseup",pointerenter:"mouseenter",pointerdown:"mousedown",pointermove:"mousemove",pointerup:"mouseup",pointerleave:"mouseout",pointerout:"mouseout"},ds=t=>null===t||""===t;const us=!!Se&&{passive:!0};function fs(t,e,i){t.canvas.removeEventListener(e,i,us)}function gs(t,e){for(const i of t)if(i===e||i.contains(e))return!0}function ps(t,e,i){const s=t.canvas,n=new MutationObserver((t=>{let e=!1;for(const i of t)e=e||gs(i.addedNodes,s),e=e&&!gs(i.removedNodes,s);e&&i()}));return n.observe(document,{childList:!0,subtree:!0}),n}function ms(t,e,i){const s=t.canvas,n=new MutationObserver((t=>{let e=!1;for(const i of t)e=e||gs(i.removedNodes,s),e=e&&!gs(i.addedNodes,s);e&&i()}));return n.observe(document,{childList:!0,subtree:!0}),n}const bs=new Map;let xs=0;function _s(){const t=window.devicePixelRatio;t!==xs&&(xs=t,bs.forEach(((e,i)=>{i.currentDevicePixelRatio!==t&&e()})))}function ys(t,e,i){const s=t.canvas,n=s&&ge(s);if(!n)return;const o=ct(((t,e)=>{const s=n.clientWidth;i(t,e),s<n.clientWidth&&i()}),window),a=new ResizeObserver((t=>{const e=t[0],i=e.contentRect.width,s=e.contentRect.height;0===i&&0===s||o(i,s)}));return a.observe(n),function(t,e){bs.size||window.addEventListener("resize",_s),bs.set(t,e)}(t,o),a}function vs(t,e,i){i&&i.disconnect(),"resize"===e&&function(t){bs.delete(t),bs.size||window.removeEventListener("resize",_s)}(t)}function Ms(t,e,i){const s=t.canvas,n=ct((e=>{null!==t.ctx&&i(function(t,e){const i=cs[t.type]||t.type,{x:s,y:n}=ve(t,e);return{type:i,chart:e,native:t,x:void 0!==s?s:null,y:void 0!==n?n:null}}(e,t))}),t);return function(t,e,i){t.addEventListener(e,i,us)}(s,e,n),n}class ws extends rs{acquireContext(t,e){const i=t&&t.getContext&&t.getContext("2d");return i&&i.canvas===t?(function(t,e){const i=t.style,s=t.getAttribute("height"),n=t.getAttribute("width");if(t[hs]={initial:{height:s,width:n,style:{display:i.display,height:i.height,width:i.width}}},i.display=i.display||"block",i.boxSizing=i.boxSizing||"border-box",ds(n)){const e=Pe(t,"width");void 0!==e&&(t.width=e)}if(ds(s))if(""===t.style.height)t.height=t.width/(e||2);else{const e=Pe(t,"height");void 0!==e&&(t.height=e)}}(t,e),i):null}releaseContext(t){const e=t.canvas;if(!e[hs])return!1;const i=e[hs].initial;["height","width"].forEach((t=>{const n=i[t];s(n)?e.removeAttribute(t):e.setAttribute(t,n)}));const n=i.style||{};return Object.keys(n).forEach((t=>{e.style[t]=n[t]})),e.width=e.width,delete e[hs],!0}addEventListener(t,e,i){this.removeEventListener(t,e);const s=t.$proxies||(t.$proxies={}),n={attach:ps,detach:ms,resize:ys}[e]||Ms;s[e]=n(t,e,i)}removeEventListener(t,e){const i=t.$proxies||(t.$proxies={}),s=i[e];if(!s)return;({attach:vs,detach:vs,resize:vs}[e]||fs)(t,e,s),i[e]=void 0}getDevicePixelRatio(){return window.devicePixelRatio}getMaximumSize(t,e,i,s){return we(t,e,i,s)}isAttached(t){const e=ge(t);return!(!e||!e.isConnected)}}function ks(t){return!fe()||"undefined"!=typeof OffscreenCanvas&&t instanceof OffscreenCanvas?ls:ws}var Ss=Object.freeze({__proto__:null,BasePlatform:rs,BasicPlatform:ls,DomPlatform:ws,_detectPlatform:ks});const Ps="transparent",Ds={boolean:(t,e,i)=>i>.5?e:t,color(t,e,i){const s=Qt(t||Ps),n=s.valid&&Qt(e||Ps);return n&&n.valid?n.mix(s,i).hexString():e},number:(t,e,i)=>t+(e-t)*i};class Cs{constructor(t,e,i,s){const n=e[i];s=Pi([t.to,s,n,t.from]);const o=Pi([t.from,n,s]);this._active=!0,this._fn=t.fn||Ds[t.type||typeof o],this._easing=fi[t.easing]||fi.linear,this._start=Math.floor(Date.now()+(t.delay||0)),this._duration=this._total=Math.floor(t.duration),this._loop=!!t.loop,this._target=e,this._prop=i,this._from=o,this._to=s,this._promises=void 0}active(){return this._active}update(t,e,i){if(this._active){this._notify(!1);const s=this._target[this._prop],n=i-this._start,o=this._duration-n;this._start=i,this._duration=Math.floor(Math.max(o,t.duration)),this._total+=n,this._loop=!!t.loop,this._to=Pi([t.to,e,s,t.from]),this._from=Pi([t.from,s,e])}}cancel(){this._active&&(this.tick(Date.now()),this._active=!1,this._notify(!1))}tick(t){const e=t-this._start,i=this._duration,s=this._prop,n=this._from,o=this._loop,a=this._to;let r;if(this._active=n!==a&&(o||e<i),!this._active)return this._target[s]=a,void this._notify(!0);e<0?this._target[s]=n:(r=e/i%2,r=o&&r>1?2-r:r,r=this._easing(Math.min(1,Math.max(0,r))),this._target[s]=this._fn(n,a,r))}wait(){const t=this._promises||(this._promises=[]);return new Promise(((e,i)=>{t.push({res:e,rej:i})}))}_notify(t){const e=t?"res":"rej",i=this._promises||[];for(let t=0;t<i.length;t++)i[t][e]()}}class Os{constructor(t,e){this._chart=t,this._properties=new Map,this.configure(e)}configure(t){if(!o(t))return;const e=Object.keys(ue.animation),i=this._properties;Object.getOwnPropertyNames(t).forEach((s=>{const a=t[s];if(!o(a))return;const r={};for(const t of e)r[t]=a[t];(n(a.properties)&&a.properties||[s]).forEach((t=>{t!==s&&i.has(t)||i.set(t,r)}))}))}_animateOptions(t,e){const i=e.options,s=function(t,e){if(!e)return;let i=t.options;if(!i)return void(t.options=e);i.$shared&&(t.options=i=Object.assign({},i,{$shared:!1,$animations:{}}));return i}(t,i);if(!s)return[];const n=this._createAnimations(s,i);return i.$shared&&function(t,e){const i=[],s=Object.keys(e);for(let e=0;e<s.length;e++){const n=t[s[e]];n&&n.active()&&i.push(n.wait())}return Promise.all(i)}(t.options.$animations,i).then((()=>{t.options=i}),(()=>{})),n}_createAnimations(t,e){const i=this._properties,s=[],n=t.$animations||(t.$animations={}),o=Object.keys(e),a=Date.now();let r;for(r=o.length-1;r>=0;--r){const l=o[r];if("$"===l.charAt(0))continue;if("options"===l){s.push(...this._animateOptions(t,e));continue}const h=e[l];let c=n[l];const d=i.get(l);if(c){if(d&&c.active()){c.update(d,h,a);continue}c.cancel()}d&&d.duration?(n[l]=c=new Cs(d,t,l,h),s.push(c)):t[l]=h}return s}update(t,e){if(0===this._properties.size)return void Object.assign(t,e);const i=this._createAnimations(t,e);return i.length?(xt.add(this._chart,i),!0):void 0}}function As(t,e){const i=t&&t.options||{},s=i.reverse,n=void 0===i.min?e:0,o=void 0===i.max?e:0;return{start:s?o:n,end:s?n:o}}function Ts(t,e){const i=[],s=t._getSortedDatasetMetas(e);let n,o;for(n=0,o=s.length;n<o;++n)i.push(s[n].index);return i}function Ls(t,e,i,s={}){const n=t.keys,o="single"===s.mode;let r,l,h,c;if(null!==e){for(r=0,l=n.length;r<l;++r){if(h=+n[r],h===i){if(s.all)continue;break}c=t.values[h],a(c)&&(o||0===e||F(e)===F(c))&&(e+=c)}return e}}function Es(t,e){const i=t&&t.options.stacked;return i||void 0===i&&void 0!==e.stack}function Rs(t,e,i){const s=t[e]||(t[e]={});return s[i]||(s[i]={})}function Is(t,e,i,s){for(const n of e.getMatchingVisibleMetas(s).reverse()){const e=t[n.index];if(i&&e>0||!i&&e<0)return n.index}return null}function zs(t,e){const{chart:i,_cachedMeta:s}=t,n=i._stacks||(i._stacks={}),{iScale:o,vScale:a,index:r}=s,l=o.axis,h=a.axis,c=function(t,e,i){return`${t.id}.${e.id}.${i.stack||i.type}`}(o,a,s),d=e.length;let u;for(let t=0;t<d;++t){const i=e[t],{[l]:o,[h]:d}=i;u=(i._stacks||(i._stacks={}))[h]=Rs(n,c,o),u[r]=d,u._top=Is(u,a,!0,s.type),u._bottom=Is(u,a,!1,s.type);(u._visualValues||(u._visualValues={}))[r]=d}}function Fs(t,e){const i=t.scales;return Object.keys(i).filter((t=>i[t].axis===e)).shift()}function Vs(t,e){const i=t.controller.index,s=t.vScale&&t.vScale.axis;if(s){e=e||t._parsed;for(const t of e){const e=t._stacks;if(!e||void 0===e[s]||void 0===e[s][i])return;delete e[s][i],void 0!==e[s]._visualValues&&void 0!==e[s]._visualValues[i]&&delete e[s]._visualValues[i]}}}const Bs=t=>"reset"===t||"none"===t,Ws=(t,e)=>e?t:Object.assign({},t);class Ns{static defaults={};static datasetElementType=null;static dataElementType=null;constructor(t,e){this.chart=t,this._ctx=t.ctx,this.index=e,this._cachedDataOpts={},this._cachedMeta=this.getMeta(),this._type=this._cachedMeta.type,this.options=void 0,this._parsing=!1,this._data=void 0,this._objectData=void 0,this._sharedOptions=void 0,this._drawStart=void 0,this._drawCount=void 0,this.enableOptionSharing=!1,this.supportsDecimation=!1,this.$context=void 0,this._syncList=[],this.datasetElementType=new.target.datasetElementType,this.dataElementType=new.target.dataElementType,this.initialize()}initialize(){const t=this._cachedMeta;this.configure(),this.linkScales(),t._stacked=Es(t.vScale,t),this.addElements(),this.options.fill&&!this.chart.isPluginEnabled("filler")&&console.warn("Tried to use the 'fill' option without the 'Filler' plugin enabled. Please import and register the 'Filler' plugin and make sure it is not disabled in the options")}updateIndex(t){this.index!==t&&Vs(this._cachedMeta),this.index=t}linkScales(){const t=this.chart,e=this._cachedMeta,i=this.getDataset(),s=(t,e,i,s)=>"x"===t?e:"r"===t?s:i,n=e.xAxisID=l(i.xAxisID,Fs(t,"x")),o=e.yAxisID=l(i.yAxisID,Fs(t,"y")),a=e.rAxisID=l(i.rAxisID,Fs(t,"r")),r=e.indexAxis,h=e.iAxisID=s(r,n,o,a),c=e.vAxisID=s(r,o,n,a);e.xScale=this.getScaleForId(n),e.yScale=this.getScaleForId(o),e.rScale=this.getScaleForId(a),e.iScale=this.getScaleForId(h),e.vScale=this.getScaleForId(c)}getDataset(){return this.chart.data.datasets[this.index]}getMeta(){return this.chart.getDatasetMeta(this.index)}getScaleForId(t){return this.chart.scales[t]}_getOtherScale(t){const e=this._cachedMeta;return t===e.iScale?e.vScale:e.iScale}reset(){this._update("reset")}_destroy(){const t=this._cachedMeta;this._data&&rt(this._data,this),t._stacked&&Vs(t)}_dataCheck(){const t=this.getDataset(),e=t.data||(t.data=[]),i=this._data;if(o(e))this._data=function(t){const e=Object.keys(t),i=new Array(e.length);let s,n,o;for(s=0,n=e.length;s<n;++s)o=e[s],i[s]={x:o,y:t[o]};return i}(e);else if(i!==e){if(i){rt(i,this);const t=this._cachedMeta;Vs(t),t._parsed=[]}e&&Object.isExtensible(e)&&at(e,this),this._syncList=[],this._data=e}}addElements(){const t=this._cachedMeta;this._dataCheck(),this.datasetElementType&&(t.dataset=new this.datasetElementType)}buildOrUpdateElements(t){const e=this._cachedMeta,i=this.getDataset();let s=!1;this._dataCheck();const n=e._stacked;e._stacked=Es(e.vScale,e),e.stack!==i.stack&&(s=!0,Vs(e),e.stack=i.stack),this._resyncElements(t),(s||n!==e._stacked)&&zs(this,e._parsed)}configure(){const t=this.chart.config,e=t.datasetScopeKeys(this._type),i=t.getOptionScopes(this.getDataset(),e,!0);this.options=t.createResolver(i,this.getContext()),this._parsing=this.options.parsing,this._cachedDataOpts={}}parse(t,e){const{_cachedMeta:i,_data:s}=this,{iScale:a,_stacked:r}=i,l=a.axis;let h,c,d,u=0===t&&e===s.length||i._sorted,f=t>0&&i._parsed[t-1];if(!1===this._parsing)i._parsed=s,i._sorted=!0,d=s;else{d=n(s[t])?this.parseArrayData(i,s,t,e):o(s[t])?this.parseObjectData(i,s,t,e):this.parsePrimitiveData(i,s,t,e);const a=()=>null===c[l]||f&&c[l]<f[l];for(h=0;h<e;++h)i._parsed[h+t]=c=d[h],u&&(a()&&(u=!1),f=c);i._sorted=u}r&&zs(this,d)}parsePrimitiveData(t,e,i,s){const{iScale:n,vScale:o}=t,a=n.axis,r=o.axis,l=n.getLabels(),h=n===o,c=new Array(s);let d,u,f;for(d=0,u=s;d<u;++d)f=d+i,c[d]={[a]:h||n.parse(l[f],f),[r]:o.parse(e[f],f)};return c}parseArrayData(t,e,i,s){const{xScale:n,yScale:o}=t,a=new Array(s);let r,l,h,c;for(r=0,l=s;r<l;++r)h=r+i,c=e[h],a[r]={x:n.parse(c[0],h),y:o.parse(c[1],h)};return a}parseObjectData(t,e,i,s){const{xScale:n,yScale:o}=t,{xAxisKey:a="x",yAxisKey:r="y"}=this._parsing,l=new Array(s);let h,c,d,u;for(h=0,c=s;h<c;++h)d=h+i,u=e[d],l[h]={x:n.parse(M(u,a),d),y:o.parse(M(u,r),d)};return l}getParsed(t){return this._cachedMeta._parsed[t]}getDataElement(t){return this._cachedMeta.data[t]}applyStack(t,e,i){const s=this.chart,n=this._cachedMeta,o=e[t.axis];return Ls({keys:Ts(s,!0),values:e._stacks[t.axis]._visualValues},o,n.index,{mode:i})}updateRangeFromParsed(t,e,i,s){const n=i[e.axis];let o=null===n?NaN:n;const a=s&&i._stacks[e.axis];s&&a&&(s.values=a,o=Ls(s,n,this._cachedMeta.index)),t.min=Math.min(t.min,o),t.max=Math.max(t.max,o)}getMinMax(t,e){const i=this._cachedMeta,s=i._parsed,n=i._sorted&&t===i.iScale,o=s.length,r=this._getOtherScale(t),l=((t,e,i)=>t&&!e.hidden&&e._stacked&&{keys:Ts(i,!0),values:null})(e,i,this.chart),h={min:Number.POSITIVE_INFINITY,max:Number.NEGATIVE_INFINITY},{min:c,max:d}=function(t){const{min:e,max:i,minDefined:s,maxDefined:n}=t.getUserBounds();return{min:s?e:Number.NEGATIVE_INFINITY,max:n?i:Number.POSITIVE_INFINITY}}(r);let u,f;function g(){f=s[u];const e=f[r.axis];return!a(f[t.axis])||c>e||d<e}for(u=0;u<o&&(g()||(this.updateRangeFromParsed(h,t,f,l),!n));++u);if(n)for(u=o-1;u>=0;--u)if(!g()){this.updateRangeFromParsed(h,t,f,l);break}return h}getAllParsedValues(t){const e=this._cachedMeta._parsed,i=[];let s,n,o;for(s=0,n=e.length;s<n;++s)o=e[s][t.axis],a(o)&&i.push(o);return i}getMaxOverflow(){return!1}getLabelAndValue(t){const e=this._cachedMeta,i=e.iScale,s=e.vScale,n=this.getParsed(t);return{label:i?""+i.getLabelForValue(n[i.axis]):"",value:s?""+s.getLabelForValue(n[s.axis]):""}}_update(t){const e=this._cachedMeta;this.update(t||"default"),e._clip=function(t){let e,i,s,n;return o(t)?(e=t.top,i=t.right,s=t.bottom,n=t.left):e=i=s=n=t,{top:e,right:i,bottom:s,left:n,disabled:!1===t}}(l(this.options.clip,function(t,e,i){if(!1===i)return!1;const s=As(t,i),n=As(e,i);return{top:n.end,right:s.end,bottom:n.start,left:s.start}}(e.xScale,e.yScale,this.getMaxOverflow())))}update(t){}draw(){const t=this._ctx,e=this.chart,i=this._cachedMeta,s=i.data||[],n=e.chartArea,o=[],a=this._drawStart||0,r=this._drawCount||s.length-a,l=this.options.drawActiveElementsOnTop;let h;for(i.dataset&&i.dataset.draw(t,n,a,r),h=a;h<a+r;++h){const e=s[h];e.hidden||(e.active&&l?o.push(e):e.draw(t,n))}for(h=0;h<o.length;++h)o[h].draw(t,n)}getStyle(t,e){const i=e?"active":"default";return void 0===t&&this._cachedMeta.dataset?this.resolveDatasetElementOptions(i):this.resolveDataElementOptions(t||0,i)}getContext(t,e,i){const s=this.getDataset();let n;if(t>=0&&t<this._cachedMeta.data.length){const e=this._cachedMeta.data[t];n=e.$context||(e.$context=function(t,e,i){return Ci(t,{active:!1,dataIndex:e,parsed:void 0,raw:void 0,element:i,index:e,mode:"default",type:"data"})}(this.getContext(),t,e)),n.parsed=this.getParsed(t),n.raw=s.data[t],n.index=n.dataIndex=t}else n=this.$context||(this.$context=function(t,e){return Ci(t,{active:!1,dataset:void 0,datasetIndex:e,index:e,mode:"default",type:"dataset"})}(this.chart.getContext(),this.index)),n.dataset=s,n.index=n.datasetIndex=this.index;return n.active=!!e,n.mode=i,n}resolveDatasetElementOptions(t){return this._resolveElementOptions(this.datasetElementType.id,t)}resolveDataElementOptions(t,e){return this._resolveElementOptions(this.dataElementType.id,e,t)}_resolveElementOptions(t,e="default",i){const s="active"===e,n=this._cachedDataOpts,o=t+"-"+e,a=n[o],r=this.enableOptionSharing&&k(i);if(a)return Ws(a,r);const l=this.chart.config,h=l.datasetElementScopeKeys(this._type,t),c=s?[`${t}Hover`,"hover",t,""]:[t,""],d=l.getOptionScopes(this.getDataset(),h),u=Object.keys(ue.elements[t]),f=l.resolveNamedOptions(d,u,(()=>this.getContext(i,s,e)),c);return f.$shared&&(f.$shared=r,n[o]=Object.freeze(Ws(f,r))),f}_resolveAnimations(t,e,i){const s=this.chart,n=this._cachedDataOpts,o=`animation-${e}`,a=n[o];if(a)return a;let r;if(!1!==s.options.animation){const s=this.chart.config,n=s.datasetAnimationScopeKeys(this._type,e),o=s.getOptionScopes(this.getDataset(),n);r=s.createResolver(o,this.getContext(t,i,e))}const l=new Os(s,r&&r.animations);return r&&r._cacheable&&(n[o]=Object.freeze(l)),l}getSharedOptions(t){if(t.$shared)return this._sharedOptions||(this._sharedOptions=Object.assign({},t))}includeOptions(t,e){return!e||Bs(t)||this.chart._animationsDisabled}_getSharedOptions(t,e){const i=this.resolveDataElementOptions(t,e),s=this._sharedOptions,n=this.getSharedOptions(i),o=this.includeOptions(e,n)||n!==s;return this.updateSharedOptions(n,e,i),{sharedOptions:n,includeOptions:o}}updateElement(t,e,i,s){Bs(s)?Object.assign(t,i):this._resolveAnimations(e,s).update(t,i)}updateSharedOptions(t,e,i){t&&!Bs(e)&&this._resolveAnimations(void 0,e).update(t,i)}_setStyle(t,e,i,s){t.active=s;const n=this.getStyle(e,s);this._resolveAnimations(e,i,s).update(t,{options:!s&&this.getSharedOptions(n)||n})}removeHoverStyle(t,e,i){this._setStyle(t,i,"active",!1)}setHoverStyle(t,e,i){this._setStyle(t,i,"active",!0)}_removeDatasetHoverStyle(){const t=this._cachedMeta.dataset;t&&this._setStyle(t,void 0,"active",!1)}_setDatasetHoverStyle(){const t=this._cachedMeta.dataset;t&&this._setStyle(t,void 0,"active",!0)}_resyncElements(t){const e=this._data,i=this._cachedMeta.data;for(const[t,e,i]of this._syncList)this[t](e,i);this._syncList=[];const s=i.length,n=e.length,o=Math.min(n,s);o&&this.parse(0,o),n>s?this._insertElements(s,n-s,t):n<s&&this._removeElements(n,s-n)}_insertElements(t,e,i=!0){const s=this._cachedMeta,n=s.data,o=t+e;let a;const r=t=>{for(t.length+=e,a=t.length-1;a>=o;a--)t[a]=t[a-e]};for(r(n),a=t;a<o;++a)n[a]=new this.dataElementType;this._parsing&&r(s._parsed),this.parse(t,e),i&&this.updateElements(n,t,e,"reset")}updateElements(t,e,i,s){}_removeElements(t,e){const i=this._cachedMeta;if(this._parsing){const s=i._parsed.splice(t,e);i._stacked&&Vs(i,s)}i.data.splice(t,e)}_sync(t){if(this._parsing)this._syncList.push(t);else{const[e,i,s]=t;this[e](i,s)}this.chart._dataChanges.push([this.index,...t])}_onDataPush(){const t=arguments.length;this._sync(["_insertElements",this.getDataset().data.length-t,t])}_onDataPop(){this._sync(["_removeElements",this._cachedMeta.data.length-1,1])}_onDataShift(){this._sync(["_removeElements",0,1])}_onDataSplice(t,e){e&&this._sync(["_removeElements",t,e]);const i=arguments.length-2;i&&this._sync(["_insertElements",t,i])}_onDataUnshift(){this._sync(["_insertElements",0,arguments.length])}}class Hs{static defaults={};static defaultRoutes=void 0;x;y;active=!1;options;$animations;tooltipPosition(t){const{x:e,y:i}=this.getProps(["x","y"],t);return{x:e,y:i}}hasValue(){return N(this.x)&&N(this.y)}getProps(t,e){const i=this.$animations;if(!e||!i)return this;const s={};return t.forEach((t=>{s[t]=i[t]&&i[t].active()?i[t]._to:this[t]})),s}}function js(t,e){const i=t.options.ticks,n=function(t){const e=t.options.offset,i=t._tickSize(),s=t._length/i+(e?0:1),n=t._maxLength/i;return Math.floor(Math.min(s,n))}(t),o=Math.min(i.maxTicksLimit||n,n),a=i.major.enabled?function(t){const e=[];let i,s;for(i=0,s=t.length;i<s;i++)t[i].major&&e.push(i);return e}(e):[],r=a.length,l=a[0],h=a[r-1],c=[];if(r>o)return function(t,e,i,s){let n,o=0,a=i[0];for(s=Math.ceil(s),n=0;n<t.length;n++)n===a&&(e.push(t[n]),o++,a=i[o*s])}(e,c,a,r/o),c;const d=function(t,e,i){const s=function(t){const e=t.length;let i,s;if(e<2)return!1;for(s=t[0],i=1;i<e;++i)if(t[i]-t[i-1]!==s)return!1;return s}(t),n=e.length/i;if(!s)return Math.max(n,1);const o=W(s);for(let t=0,e=o.length-1;t<e;t++){const e=o[t];if(e>n)return e}return Math.max(n,1)}(a,e,o);if(r>0){let t,i;const n=r>1?Math.round((h-l)/(r-1)):null;for($s(e,c,d,s(n)?0:l-n,l),t=0,i=r-1;t<i;t++)$s(e,c,d,a[t],a[t+1]);return $s(e,c,d,h,s(n)?e.length:h+n),c}return $s(e,c,d),c}function $s(t,e,i,s,n){const o=l(s,0),a=Math.min(l(n,t.length),t.length);let r,h,c,d=0;for(i=Math.ceil(i),n&&(r=n-s,i=r/Math.floor(r/i)),c=o;c<0;)d++,c=Math.round(o+d*i);for(h=Math.max(o,0);h<a;h++)h===c&&(e.push(t[h]),d++,c=Math.round(o+d*i))}const Ys=(t,e,i)=>"top"===e||"left"===e?t[e]+i:t[e]-i,Us=(t,e)=>Math.min(e||t,t);function Xs(t,e){const i=[],s=t.length/e,n=t.length;let o=0;for(;o<n;o+=s)i.push(t[Math.floor(o)]);return i}function qs(t,e,i){const s=t.ticks.length,n=Math.min(e,s-1),o=t._startPixel,a=t._endPixel,r=1e-6;let l,h=t.getPixelForTick(n);if(!(i&&(l=1===s?Math.max(h-o,a-h):0===e?(t.getPixelForTick(1)-h)/2:(h-t.getPixelForTick(n-1))/2,h+=n<e?l:-l,h<o-r||h>a+r)))return h}function Ks(t){return t.drawTicks?t.tickLength:0}function Gs(t,e){if(!t.display)return 0;const i=Si(t.font,e),s=ki(t.padding);return(n(t.text)?t.text.length:1)*i.lineHeight+s.height}function Zs(t,e,i){let s=ut(t);return(i&&"right"!==e||!i&&"right"===e)&&(s=(t=>"left"===t?"right":"right"===t?"left":t)(s)),s}class Js extends Hs{constructor(t){super(),this.id=t.id,this.type=t.type,this.options=void 0,this.ctx=t.ctx,this.chart=t.chart,this.top=void 0,this.bottom=void 0,this.left=void 0,this.right=void 0,this.width=void 0,this.height=void 0,this._margins={left:0,right:0,top:0,bottom:0},this.maxWidth=void 0,this.maxHeight=void 0,this.paddingTop=void 0,this.paddingBottom=void 0,this.paddingLeft=void 0,this.paddingRight=void 0,this.axis=void 0,this.labelRotation=void 0,this.min=void 0,this.max=void 0,this._range=void 0,this.ticks=[],this._gridLineItems=null,this._labelItems=null,this._labelSizes=null,this._length=0,this._maxLength=0,this._longestTextCache={},this._startPixel=void 0,this._endPixel=void 0,this._reversePixels=!1,this._userMax=void 0,this._userMin=void 0,this._suggestedMax=void 0,this._suggestedMin=void 0,this._ticksLength=0,this._borderValue=0,this._cache={},this._dataLimitsCached=!1,this.$context=void 0}init(t){this.options=t.setContext(this.getContext()),this.axis=t.axis,this._userMin=this.parse(t.min),this._userMax=this.parse(t.max),this._suggestedMin=this.parse(t.suggestedMin),this._suggestedMax=this.parse(t.suggestedMax)}parse(t,e){return t}getUserBounds(){let{_userMin:t,_userMax:e,_suggestedMin:i,_suggestedMax:s}=this;return t=r(t,Number.POSITIVE_INFINITY),e=r(e,Number.NEGATIVE_INFINITY),i=r(i,Number.POSITIVE_INFINITY),s=r(s,Number.NEGATIVE_INFINITY),{min:r(t,i),max:r(e,s),minDefined:a(t),maxDefined:a(e)}}getMinMax(t){let e,{min:i,max:s,minDefined:n,maxDefined:o}=this.getUserBounds();if(n&&o)return{min:i,max:s};const a=this.getMatchingVisibleMetas();for(let r=0,l=a.length;r<l;++r)e=a[r].controller.getMinMax(this,t),n||(i=Math.min(i,e.min)),o||(s=Math.max(s,e.max));return i=o&&i>s?s:i,s=n&&i>s?i:s,{min:r(i,r(s,i)),max:r(s,r(i,s))}}getPadding(){return{left:this.paddingLeft||0,top:this.paddingTop||0,right:this.paddingRight||0,bottom:this.paddingBottom||0}}getTicks(){return this.ticks}getLabels(){const t=this.chart.data;return this.options.labels||(this.isHorizontal()?t.xLabels:t.yLabels)||t.labels||[]}getLabelItems(t=this.chart.chartArea){return this._labelItems||(this._labelItems=this._computeLabelItems(t))}beforeLayout(){this._cache={},this._dataLimitsCached=!1}beforeUpdate(){d(this.options.beforeUpdate,[this])}update(t,e,i){const{beginAtZero:s,grace:n,ticks:o}=this.options,a=o.sampleSize;this.beforeUpdate(),this.maxWidth=t,this.maxHeight=e,this._margins=i=Object.assign({left:0,right:0,top:0,bottom:0},i),this.ticks=null,this._labelSizes=null,this._gridLineItems=null,this._labelItems=null,this.beforeSetDimensions(),this.setDimensions(),this.afterSetDimensions(),this._maxLength=this.isHorizontal()?this.width+i.left+i.right:this.height+i.top+i.bottom,this._dataLimitsCached||(this.beforeDataLimits(),this.determineDataLimits(),this.afterDataLimits(),this._range=Di(this,n,s),this._dataLimitsCached=!0),this.beforeBuildTicks(),this.ticks=this.buildTicks()||[],this.afterBuildTicks();const r=a<this.ticks.length;this._convertTicksToLabels(r?Xs(this.ticks,a):this.ticks),this.configure(),this.beforeCalculateLabelRotation(),this.calculateLabelRotation(),this.afterCalculateLabelRotation(),o.display&&(o.autoSkip||"auto"===o.source)&&(this.ticks=js(this,this.ticks),this._labelSizes=null,this.afterAutoSkip()),r&&this._convertTicksToLabels(this.ticks),this.beforeFit(),this.fit(),this.afterFit(),this.afterUpdate()}configure(){let t,e,i=this.options.reverse;this.isHorizontal()?(t=this.left,e=this.right):(t=this.top,e=this.bottom,i=!i),this._startPixel=t,this._endPixel=e,this._reversePixels=i,this._length=e-t,this._alignToPixels=this.options.alignToPixels}afterUpdate(){d(this.options.afterUpdate,[this])}beforeSetDimensions(){d(this.options.beforeSetDimensions,[this])}setDimensions(){this.isHorizontal()?(this.width=this.maxWidth,this.left=0,this.right=this.width):(this.height=this.maxHeight,this.top=0,this.bottom=this.height),this.paddingLeft=0,this.paddingTop=0,this.paddingRight=0,this.paddingBottom=0}afterSetDimensions(){d(this.options.afterSetDimensions,[this])}_callHooks(t){this.chart.notifyPlugins(t,this.getContext()),d(this.options[t],[this])}beforeDataLimits(){this._callHooks("beforeDataLimits")}determineDataLimits(){}afterDataLimits(){this._callHooks("afterDataLimits")}beforeBuildTicks(){this._callHooks("beforeBuildTicks")}buildTicks(){return[]}afterBuildTicks(){this._callHooks("afterBuildTicks")}beforeTickToLabelConversion(){d(this.options.beforeTickToLabelConversion,[this])}generateTickLabels(t){const e=this.options.ticks;let i,s,n;for(i=0,s=t.length;i<s;i++)n=t[i],n.label=d(e.callback,[n.value,i,t],this)}afterTickToLabelConversion(){d(this.options.afterTickToLabelConversion,[this])}beforeCalculateLabelRotation(){d(this.options.beforeCalculateLabelRotation,[this])}calculateLabelRotation(){const t=this.options,e=t.ticks,i=Us(this.ticks.length,t.ticks.maxTicksLimit),s=e.minRotation||0,n=e.maxRotation;let o,a,r,l=s;if(!this._isVisible()||!e.display||s>=n||i<=1||!this.isHorizontal())return void(this.labelRotation=s);const h=this._getLabelSizes(),c=h.widest.width,d=h.highest.height,u=J(this.chart.width-c,0,this.maxWidth);o=t.offset?this.maxWidth/i:u/(i-1),c+6>o&&(o=u/(i-(t.offset?.5:1)),a=this.maxHeight-Ks(t.grid)-e.padding-Gs(t.title,this.chart.options.font),r=Math.sqrt(c*c+d*d),l=Y(Math.min(Math.asin(J((h.highest.height+6)/o,-1,1)),Math.asin(J(a/r,-1,1))-Math.asin(J(d/r,-1,1)))),l=Math.max(s,Math.min(n,l))),this.labelRotation=l}afterCalculateLabelRotation(){d(this.options.afterCalculateLabelRotation,[this])}afterAutoSkip(){}beforeFit(){d(this.options.beforeFit,[this])}fit(){const t={width:0,height:0},{chart:e,options:{ticks:i,title:s,grid:n}}=this,o=this._isVisible(),a=this.isHorizontal();if(o){const o=Gs(s,e.options.font);if(a?(t.width=this.maxWidth,t.height=Ks(n)+o):(t.height=this.maxHeight,t.width=Ks(n)+o),i.display&&this.ticks.length){const{first:e,last:s,widest:n,highest:o}=this._getLabelSizes(),r=2*i.padding,l=$(this.labelRotation),h=Math.cos(l),c=Math.sin(l);if(a){const e=i.mirror?0:c*n.width+h*o.height;t.height=Math.min(this.maxHeight,t.height+e+r)}else{const e=i.mirror?0:h*n.width+c*o.height;t.width=Math.min(this.maxWidth,t.width+e+r)}this._calculatePadding(e,s,c,h)}}this._handleMargins(),a?(this.width=this._length=e.width-this._margins.left-this._margins.right,this.height=t.height):(this.width=t.width,this.height=this._length=e.height-this._margins.top-this._margins.bottom)}_calculatePadding(t,e,i,s){const{ticks:{align:n,padding:o},position:a}=this.options,r=0!==this.labelRotation,l="top"!==a&&"x"===this.axis;if(this.isHorizontal()){const a=this.getPixelForTick(0)-this.left,h=this.right-this.getPixelForTick(this.ticks.length-1);let c=0,d=0;r?l?(c=s*t.width,d=i*e.height):(c=i*t.height,d=s*e.width):"start"===n?d=e.width:"end"===n?c=t.width:"inner"!==n&&(c=t.width/2,d=e.width/2),this.paddingLeft=Math.max((c-a+o)*this.width/(this.width-a),0),this.paddingRight=Math.max((d-h+o)*this.width/(this.width-h),0)}else{let i=e.height/2,s=t.height/2;"start"===n?(i=0,s=t.height):"end"===n&&(i=e.height,s=0),this.paddingTop=i+o,this.paddingBottom=s+o}}_handleMargins(){this._margins&&(this._margins.left=Math.max(this.paddingLeft,this._margins.left),this._margins.top=Math.max(this.paddingTop,this._margins.top),this._margins.right=Math.max(this.paddingRight,this._margins.right),this._margins.bottom=Math.max(this.paddingBottom,this._margins.bottom))}afterFit(){d(this.options.afterFit,[this])}isHorizontal(){const{axis:t,position:e}=this.options;return"top"===e||"bottom"===e||"x"===t}isFullSize(){return this.options.fullSize}_convertTicksToLabels(t){let e,i;for(this.beforeTickToLabelConversion(),this.generateTickLabels(t),e=0,i=t.length;e<i;e++)s(t[e].label)&&(t.splice(e,1),i--,e--);this.afterTickToLabelConversion()}_getLabelSizes(){let t=this._labelSizes;if(!t){const e=this.options.ticks.sampleSize;let i=this.ticks;e<i.length&&(i=Xs(i,e)),this._labelSizes=t=this._computeLabelSizes(i,i.length,this.options.ticks.maxTicksLimit)}return t}_computeLabelSizes(t,e,i){const{ctx:o,_longestTextCache:a}=this,r=[],l=[],h=Math.floor(e/Us(e,i));let c,d,f,g,p,m,b,x,_,y,v,M=0,w=0;for(c=0;c<e;c+=h){if(g=t[c].label,p=this._resolveTickFontOptions(c),o.font=m=p.string,b=a[m]=a[m]||{data:{},gc:[]},x=p.lineHeight,_=y=0,s(g)||n(g)){if(n(g))for(d=0,f=g.length;d<f;++d)v=g[d],s(v)||n(v)||(_=Ce(o,b.data,b.gc,_,v),y+=x)}else _=Ce(o,b.data,b.gc,_,g),y=x;r.push(_),l.push(y),M=Math.max(_,M),w=Math.max(y,w)}!function(t,e){u(t,(t=>{const i=t.gc,s=i.length/2;let n;if(s>e){for(n=0;n<s;++n)delete t.data[i[n]];i.splice(0,s)}}))}(a,e);const k=r.indexOf(M),S=l.indexOf(w),P=t=>({width:r[t]||0,height:l[t]||0});return{first:P(0),last:P(e-1),widest:P(k),highest:P(S),widths:r,heights:l}}getLabelForValue(t){return t}getPixelForValue(t,e){return NaN}getValueForPixel(t){}getPixelForTick(t){const e=this.ticks;return t<0||t>e.length-1?null:this.getPixelForValue(e[t].value)}getPixelForDecimal(t){this._reversePixels&&(t=1-t);const e=this._startPixel+t*this._length;return Q(this._alignToPixels?Ae(this.chart,e,0):e)}getDecimalForPixel(t){const e=(t-this._startPixel)/this._length;return this._reversePixels?1-e:e}getBasePixel(){return this.getPixelForValue(this.getBaseValue())}getBaseValue(){const{min:t,max:e}=this;return t<0&&e<0?e:t>0&&e>0?t:0}getContext(t){const e=this.ticks||[];if(t>=0&&t<e.length){const i=e[t];return i.$context||(i.$context=function(t,e,i){return Ci(t,{tick:i,index:e,type:"tick"})}(this.getContext(),t,i))}return this.$context||(this.$context=Ci(this.chart.getContext(),{scale:this,type:"scale"}))}_tickSize(){const t=this.options.ticks,e=$(this.labelRotation),i=Math.abs(Math.cos(e)),s=Math.abs(Math.sin(e)),n=this._getLabelSizes(),o=t.autoSkipPadding||0,a=n?n.widest.width+o:0,r=n?n.highest.height+o:0;return this.isHorizontal()?r*i>a*s?a/i:r/s:r*s<a*i?r/i:a/s}_isVisible(){const t=this.options.display;return"auto"!==t?!!t:this.getMatchingVisibleMetas().length>0}_computeGridLineItems(t){const e=this.axis,i=this.chart,s=this.options,{grid:n,position:a,border:r}=s,h=n.offset,c=this.isHorizontal(),d=this.ticks.length+(h?1:0),u=Ks(n),f=[],g=r.setContext(this.getContext()),p=g.display?g.width:0,m=p/2,b=function(t){return Ae(i,t,p)};let x,_,y,v,M,w,k,S,P,D,C,O;if("top"===a)x=b(this.bottom),w=this.bottom-u,S=x-m,D=b(t.top)+m,O=t.bottom;else if("bottom"===a)x=b(this.top),D=t.top,O=b(t.bottom)-m,w=x+m,S=this.top+u;else if("left"===a)x=b(this.right),M=this.right-u,k=x-m,P=b(t.left)+m,C=t.right;else if("right"===a)x=b(this.left),P=t.left,C=b(t.right)-m,M=x+m,k=this.left+u;else if("x"===e){if("center"===a)x=b((t.top+t.bottom)/2+.5);else if(o(a)){const t=Object.keys(a)[0],e=a[t];x=b(this.chart.scales[t].getPixelForValue(e))}D=t.top,O=t.bottom,w=x+m,S=w+u}else if("y"===e){if("center"===a)x=b((t.left+t.right)/2);else if(o(a)){const t=Object.keys(a)[0],e=a[t];x=b(this.chart.scales[t].getPixelForValue(e))}M=x-m,k=M-u,P=t.left,C=t.right}const A=l(s.ticks.maxTicksLimit,d),T=Math.max(1,Math.ceil(d/A));for(_=0;_<d;_+=T){const t=this.getContext(_),e=n.setContext(t),s=r.setContext(t),o=e.lineWidth,a=e.color,l=s.dash||[],d=s.dashOffset,u=e.tickWidth,g=e.tickColor,p=e.tickBorderDash||[],m=e.tickBorderDashOffset;y=qs(this,_,h),void 0!==y&&(v=Ae(i,y,o),c?M=k=P=C=v:w=S=D=O=v,f.push({tx1:M,ty1:w,tx2:k,ty2:S,x1:P,y1:D,x2:C,y2:O,width:o,color:a,borderDash:l,borderDashOffset:d,tickWidth:u,tickColor:g,tickBorderDash:p,tickBorderDashOffset:m}))}return this._ticksLength=d,this._borderValue=x,f}_computeLabelItems(t){const e=this.axis,i=this.options,{position:s,ticks:a}=i,r=this.isHorizontal(),l=this.ticks,{align:h,crossAlign:c,padding:d,mirror:u}=a,f=Ks(i.grid),g=f+d,p=u?-d:g,m=-$(this.labelRotation),b=[];let x,_,y,v,M,w,k,S,P,D,C,O,A="middle";if("top"===s)w=this.bottom-p,k=this._getXAxisLabelAlignment();else if("bottom"===s)w=this.top+p,k=this._getXAxisLabelAlignment();else if("left"===s){const t=this._getYAxisLabelAlignment(f);k=t.textAlign,M=t.x}else if("right"===s){const t=this._getYAxisLabelAlignment(f);k=t.textAlign,M=t.x}else if("x"===e){if("center"===s)w=(t.top+t.bottom)/2+g;else if(o(s)){const t=Object.keys(s)[0],e=s[t];w=this.chart.scales[t].getPixelForValue(e)+g}k=this._getXAxisLabelAlignment()}else if("y"===e){if("center"===s)M=(t.left+t.right)/2-g;else if(o(s)){const t=Object.keys(s)[0],e=s[t];M=this.chart.scales[t].getPixelForValue(e)}k=this._getYAxisLabelAlignment(f).textAlign}"y"===e&&("start"===h?A="top":"end"===h&&(A="bottom"));const T=this._getLabelSizes();for(x=0,_=l.length;x<_;++x){y=l[x],v=y.label;const t=a.setContext(this.getContext(x));S=this.getPixelForTick(x)+a.labelOffset,P=this._resolveTickFontOptions(x),D=P.lineHeight,C=n(v)?v.length:1;const e=C/2,i=t.color,o=t.textStrokeColor,h=t.textStrokeWidth;let d,f=k;if(r?(M=S,"inner"===k&&(f=x===_-1?this.options.reverse?"left":"right":0===x?this.options.reverse?"right":"left":"center"),O="top"===s?"near"===c||0!==m?-C*D+D/2:"center"===c?-T.highest.height/2-e*D+D:-T.highest.height+D/2:"near"===c||0!==m?D/2:"center"===c?T.highest.height/2-e*D:T.highest.height-C*D,u&&(O*=-1),0===m||t.showLabelBackdrop||(M+=D/2*Math.sin(m))):(w=S,O=(1-C)*D/2),t.showLabelBackdrop){const e=ki(t.backdropPadding),i=T.heights[x],s=T.widths[x];let n=O-e.top,o=0-e.left;switch(A){case"middle":n-=i/2;break;case"bottom":n-=i}switch(k){case"center":o-=s/2;break;case"right":o-=s}d={left:o,top:n,width:s+e.width,height:i+e.height,color:t.backdropColor}}b.push({label:v,font:P,textOffset:O,options:{rotation:m,color:i,strokeColor:o,strokeWidth:h,textAlign:f,textBaseline:A,translation:[M,w],backdrop:d}})}return b}_getXAxisLabelAlignment(){const{position:t,ticks:e}=this.options;if(-$(this.labelRotation))return"top"===t?"left":"right";let i="center";return"start"===e.align?i="left":"end"===e.align?i="right":"inner"===e.align&&(i="inner"),i}_getYAxisLabelAlignment(t){const{position:e,ticks:{crossAlign:i,mirror:s,padding:n}}=this.options,o=t+n,a=this._getLabelSizes().widest.width;let r,l;return"left"===e?s?(l=this.right+n,"near"===i?r="left":"center"===i?(r="center",l+=a/2):(r="right",l+=a)):(l=this.right-o,"near"===i?r="right":"center"===i?(r="center",l-=a/2):(r="left",l=this.left)):"right"===e?s?(l=this.left+n,"near"===i?r="right":"center"===i?(r="center",l-=a/2):(r="left",l-=a)):(l=this.left+o,"near"===i?r="left":"center"===i?(r="center",l+=a/2):(r="right",l=this.right)):r="right",{textAlign:r,x:l}}_computeLabelArea(){if(this.options.ticks.mirror)return;const t=this.chart,e=this.options.position;return"left"===e||"right"===e?{top:0,left:this.left,bottom:t.height,right:this.right}:"top"===e||"bottom"===e?{top:this.top,left:0,bottom:this.bottom,right:t.width}:void 0}drawBackground(){const{ctx:t,options:{backgroundColor:e},left:i,top:s,width:n,height:o}=this;e&&(t.save(),t.fillStyle=e,t.fillRect(i,s,n,o),t.restore())}getLineWidthForValue(t){const e=this.options.grid;if(!this._isVisible()||!e.display)return 0;const i=this.ticks.findIndex((e=>e.value===t));if(i>=0){return e.setContext(this.getContext(i)).lineWidth}return 0}drawGrid(t){const e=this.options.grid,i=this.ctx,s=this._gridLineItems||(this._gridLineItems=this._computeGridLineItems(t));let n,o;const a=(t,e,s)=>{s.width&&s.color&&(i.save(),i.lineWidth=s.width,i.strokeStyle=s.color,i.setLineDash(s.borderDash||[]),i.lineDashOffset=s.borderDashOffset,i.beginPath(),i.moveTo(t.x,t.y),i.lineTo(e.x,e.y),i.stroke(),i.restore())};if(e.display)for(n=0,o=s.length;n<o;++n){const t=s[n];e.drawOnChartArea&&a({x:t.x1,y:t.y1},{x:t.x2,y:t.y2},t),e.drawTicks&&a({x:t.tx1,y:t.ty1},{x:t.tx2,y:t.ty2},{color:t.tickColor,width:t.tickWidth,borderDash:t.tickBorderDash,borderDashOffset:t.tickBorderDashOffset})}}drawBorder(){const{chart:t,ctx:e,options:{border:i,grid:s}}=this,n=i.setContext(this.getContext()),o=i.display?n.width:0;if(!o)return;const a=s.setContext(this.getContext(0)).lineWidth,r=this._borderValue;let l,h,c,d;this.isHorizontal()?(l=Ae(t,this.left,o)-o/2,h=Ae(t,this.right,a)+a/2,c=d=r):(c=Ae(t,this.top,o)-o/2,d=Ae(t,this.bottom,a)+a/2,l=h=r),e.save(),e.lineWidth=n.width,e.strokeStyle=n.color,e.beginPath(),e.moveTo(l,c),e.lineTo(h,d),e.stroke(),e.restore()}drawLabels(t){if(!this.options.ticks.display)return;const e=this.ctx,i=this._computeLabelArea();i&&Ie(e,i);const s=this.getLabelItems(t);for(const t of s){const i=t.options,s=t.font;Ne(e,t.label,0,t.textOffset,s,i)}i&&ze(e)}drawTitle(){const{ctx:t,options:{position:e,title:i,reverse:s}}=this;if(!i.display)return;const a=Si(i.font),r=ki(i.padding),l=i.align;let h=a.lineHeight/2;"bottom"===e||"center"===e||o(e)?(h+=r.bottom,n(i.text)&&(h+=a.lineHeight*(i.text.length-1))):h+=r.top;const{titleX:c,titleY:d,maxWidth:u,rotation:f}=function(t,e,i,s){const{top:n,left:a,bottom:r,right:l,chart:h}=t,{chartArea:c,scales:d}=h;let u,f,g,p=0;const m=r-n,b=l-a;if(t.isHorizontal()){if(f=ft(s,a,l),o(i)){const t=Object.keys(i)[0],s=i[t];g=d[t].getPixelForValue(s)+m-e}else g="center"===i?(c.bottom+c.top)/2+m-e:Ys(t,i,e);u=l-a}else{if(o(i)){const t=Object.keys(i)[0],s=i[t];f=d[t].getPixelForValue(s)-b+e}else f="center"===i?(c.left+c.right)/2-b+e:Ys(t,i,e);g=ft(s,r,n),p="left"===i?-E:E}return{titleX:f,titleY:g,maxWidth:u,rotation:p}}(this,h,e,l);Ne(t,i.text,0,0,a,{color:i.color,maxWidth:u,rotation:f,textAlign:Zs(l,e,s),textBaseline:"middle",translation:[c,d]})}draw(t){this._isVisible()&&(this.drawBackground(),this.drawGrid(t),this.drawBorder(),this.drawTitle(),this.drawLabels(t))}_layers(){const t=this.options,e=t.ticks&&t.ticks.z||0,i=l(t.grid&&t.grid.z,-1),s=l(t.border&&t.border.z,0);return this._isVisible()&&this.draw===Js.prototype.draw?[{z:i,draw:t=>{this.drawBackground(),this.drawGrid(t),this.drawTitle()}},{z:s,draw:()=>{this.drawBorder()}},{z:e,draw:t=>{this.drawLabels(t)}}]:[{z:e,draw:t=>{this.draw(t)}}]}getMatchingVisibleMetas(t){const e=this.chart.getSortedVisibleDatasetMetas(),i=this.axis+"AxisID",s=[];let n,o;for(n=0,o=e.length;n<o;++n){const o=e[n];o[i]!==this.id||t&&o.type!==t||s.push(o)}return s}_resolveTickFontOptions(t){return Si(this.options.ticks.setContext(this.getContext(t)).font)}_maxDigits(){const t=this._resolveTickFontOptions(0).lineHeight;return(this.isHorizontal()?this.width:this.height)/t}}class Qs{constructor(t,e,i){this.type=t,this.scope=e,this.override=i,this.items=Object.create(null)}isForType(t){return Object.prototype.isPrototypeOf.call(this.type.prototype,t.prototype)}register(t){const e=Object.getPrototypeOf(t);let i;(function(t){return"id"in t&&"defaults"in t})(e)&&(i=this.register(e));const s=this.items,n=t.id,o=this.scope+"."+n;if(!n)throw new Error("class does not have id: "+t);return n in s||(s[n]=t,function(t,e,i){const s=b(Object.create(null),[i?ue.get(i):{},ue.get(e),t.defaults]);ue.set(e,s),t.defaultRoutes&&function(t,e){Object.keys(e).forEach((i=>{const s=i.split("."),n=s.pop(),o=[t].concat(s).join("."),a=e[i].split("."),r=a.pop(),l=a.join(".");ue.route(o,n,l,r)}))}(e,t.defaultRoutes);t.descriptors&&ue.describe(e,t.descriptors)}(t,o,i),this.override&&ue.override(t.id,t.overrides)),o}get(t){return this.items[t]}unregister(t){const e=this.items,i=t.id,s=this.scope;i in e&&delete e[i],s&&i in ue[s]&&(delete ue[s][i],this.override&&delete re[i])}}class tn{constructor(){this.controllers=new Qs(Ns,"datasets",!0),this.elements=new Qs(Hs,"elements"),this.plugins=new Qs(Object,"plugins"),this.scales=new Qs(Js,"scales"),this._typedRegistries=[this.controllers,this.scales,this.elements]}add(...t){this._each("register",t)}remove(...t){this._each("unregister",t)}addControllers(...t){this._each("register",t,this.controllers)}addElements(...t){this._each("register",t,this.elements)}addPlugins(...t){this._each("register",t,this.plugins)}addScales(...t){this._each("register",t,this.scales)}getController(t){return this._get(t,this.controllers,"controller")}getElement(t){return this._get(t,this.elements,"element")}getPlugin(t){return this._get(t,this.plugins,"plugin")}getScale(t){return this._get(t,this.scales,"scale")}removeControllers(...t){this._each("unregister",t,this.controllers)}removeElements(...t){this._each("unregister",t,this.elements)}removePlugins(...t){this._each("unregister",t,this.plugins)}removeScales(...t){this._each("unregister",t,this.scales)}_each(t,e,i){[...e].forEach((e=>{const s=i||this._getRegistryForType(e);i||s.isForType(e)||s===this.plugins&&e.id?this._exec(t,s,e):u(e,(e=>{const s=i||this._getRegistryForType(e);this._exec(t,s,e)}))}))}_exec(t,e,i){const s=w(t);d(i["before"+s],[],i),e[t](i),d(i["after"+s],[],i)}_getRegistryForType(t){for(let e=0;e<this._typedRegistries.length;e++){const i=this._typedRegistries[e];if(i.isForType(t))return i}return this.plugins}_get(t,e,i){const s=e.get(t);if(void 0===s)throw new Error('"'+t+'" is not a registered '+i+".");return s}}var en=new tn;class sn{constructor(){this._init=[]}notify(t,e,i,s){"beforeInit"===e&&(this._init=this._createDescriptors(t,!0),this._notify(this._init,t,"install"));const n=s?this._descriptors(t).filter(s):this._descriptors(t),o=this._notify(n,t,e,i);return"afterDestroy"===e&&(this._notify(n,t,"stop"),this._notify(this._init,t,"uninstall")),o}_notify(t,e,i,s){s=s||{};for(const n of t){const t=n.plugin;if(!1===d(t[i],[e,s,n.options],t)&&s.cancelable)return!1}return!0}invalidate(){s(this._cache)||(this._oldCache=this._cache,this._cache=void 0)}_descriptors(t){if(this._cache)return this._cache;const e=this._cache=this._createDescriptors(t);return this._notifyStateChanges(t),e}_createDescriptors(t,e){const i=t&&t.config,s=l(i.options&&i.options.plugins,{}),n=function(t){const e={},i=[],s=Object.keys(en.plugins.items);for(let t=0;t<s.length;t++)i.push(en.getPlugin(s[t]));const n=t.plugins||[];for(let t=0;t<n.length;t++){const s=n[t];-1===i.indexOf(s)&&(i.push(s),e[s.id]=!0)}return{plugins:i,localIds:e}}(i);return!1!==s||e?function(t,{plugins:e,localIds:i},s,n){const o=[],a=t.getContext();for(const r of e){const e=r.id,l=nn(s[e],n);null!==l&&o.push({plugin:r,options:on(t.config,{plugin:r,local:i[e]},l,a)})}return o}(t,n,s,e):[]}_notifyStateChanges(t){const e=this._oldCache||[],i=this._cache,s=(t,e)=>t.filter((t=>!e.some((e=>t.plugin.id===e.plugin.id))));this._notify(s(e,i),t,"stop"),this._notify(s(i,e),t,"start")}}function nn(t,e){return e||!1!==t?!0===t?{}:t:null}function on(t,{plugin:e,local:i},s,n){const o=t.pluginScopeKeys(e),a=t.getOptionScopes(s,o);return i&&e.defaults&&a.push(e.defaults),t.createResolver(a,n,[""],{scriptable:!1,indexable:!1,allKeys:!0})}function an(t,e){const i=ue.datasets[t]||{};return((e.datasets||{})[t]||{}).indexAxis||e.indexAxis||i.indexAxis||"x"}function rn(t){if("x"===t||"y"===t||"r"===t)return t}function ln(t,...e){if(rn(t))return t;for(const s of e){const e=s.axis||("top"===(i=s.position)||"bottom"===i?"x":"left"===i||"right"===i?"y":void 0)||t.length>1&&rn(t[0].toLowerCase());if(e)return e}var i;throw new Error(`Cannot determine type of '${t}' axis. Please provide 'axis' or 'position' option.`)}function hn(t,e,i){if(i[e+"AxisID"]===t)return{axis:e}}function cn(t,e){const i=re[t.type]||{scales:{}},s=e.scales||{},n=an(t.type,e),a=Object.create(null);return Object.keys(s).forEach((e=>{const r=s[e];if(!o(r))return console.error(`Invalid scale configuration for scale: ${e}`);if(r._proxy)return console.warn(`Ignoring resolver passed as options for scale: ${e}`);const l=ln(e,r,function(t,e){if(e.data&&e.data.datasets){const i=e.data.datasets.filter((e=>e.xAxisID===t||e.yAxisID===t));if(i.length)return hn(t,"x",i[0])||hn(t,"y",i[0])}return{}}(e,t),ue.scales[r.type]),h=function(t,e){return t===e?"_index_":"_value_"}(l,n),c=i.scales||{};a[e]=x(Object.create(null),[{axis:l},r,c[l],c[h]])})),t.data.datasets.forEach((i=>{const n=i.type||t.type,o=i.indexAxis||an(n,e),r=(re[n]||{}).scales||{};Object.keys(r).forEach((t=>{const e=function(t,e){let i=t;return"_index_"===t?i=e:"_value_"===t&&(i="x"===e?"y":"x"),i}(t,o),n=i[e+"AxisID"]||e;a[n]=a[n]||Object.create(null),x(a[n],[{axis:e},s[n],r[t]])}))})),Object.keys(a).forEach((t=>{const e=a[t];x(e,[ue.scales[e.type],ue.scale])})),a}function dn(t){const e=t.options||(t.options={});e.plugins=l(e.plugins,{}),e.scales=cn(t,e)}function un(t){return(t=t||{}).datasets=t.datasets||[],t.labels=t.labels||[],t}const fn=new Map,gn=new Set;function pn(t,e){let i=fn.get(t);return i||(i=e(),fn.set(t,i),gn.add(i)),i}const mn=(t,e,i)=>{const s=M(e,i);void 0!==s&&t.add(s)};class bn{constructor(t){this._config=function(t){return(t=t||{}).data=un(t.data),dn(t),t}(t),this._scopeCache=new Map,this._resolverCache=new Map}get platform(){return this._config.platform}get type(){return this._config.type}set type(t){this._config.type=t}get data(){return this._config.data}set data(t){this._config.data=un(t)}get options(){return this._config.options}set options(t){this._config.options=t}get plugins(){return this._config.plugins}update(){const t=this._config;this.clearCache(),dn(t)}clearCache(){this._scopeCache.clear(),this._resolverCache.clear()}datasetScopeKeys(t){return pn(t,(()=>[[`datasets.${t}`,""]]))}datasetAnimationScopeKeys(t,e){return pn(`${t}.transition.${e}`,(()=>[[`datasets.${t}.transitions.${e}`,`transitions.${e}`],[`datasets.${t}`,""]]))}datasetElementScopeKeys(t,e){return pn(`${t}-${e}`,(()=>[[`datasets.${t}.elements.${e}`,`datasets.${t}`,`elements.${e}`,""]]))}pluginScopeKeys(t){const e=t.id;return pn(`${this.type}-plugin-${e}`,(()=>[[`plugins.${e}`,...t.additionalOptionScopes||[]]]))}_cachedScopes(t,e){const i=this._scopeCache;let s=i.get(t);return s&&!e||(s=new Map,i.set(t,s)),s}getOptionScopes(t,e,i){const{options:s,type:n}=this,o=this._cachedScopes(t,i),a=o.get(e);if(a)return a;const r=new Set;e.forEach((e=>{t&&(r.add(t),e.forEach((e=>mn(r,t,e)))),e.forEach((t=>mn(r,s,t))),e.forEach((t=>mn(r,re[n]||{},t))),e.forEach((t=>mn(r,ue,t))),e.forEach((t=>mn(r,le,t)))}));const l=Array.from(r);return 0===l.length&&l.push(Object.create(null)),gn.has(e)&&o.set(e,l),l}chartOptionScopes(){const{options:t,type:e}=this;return[t,re[e]||{},ue.datasets[e]||{},{type:e},ue,le]}resolveNamedOptions(t,e,i,s=[""]){const o={$shared:!0},{resolver:a,subPrefixes:r}=xn(this._resolverCache,t,s);let l=a;if(function(t,e){const{isScriptable:i,isIndexable:s}=Ye(t);for(const o of e){const e=i(o),a=s(o),r=(a||e)&&t[o];if(e&&(S(r)||_n(r))||a&&n(r))return!0}return!1}(a,e)){o.$shared=!1;l=$e(a,i=S(i)?i():i,this.createResolver(t,i,r))}for(const t of e)o[t]=l[t];return o}createResolver(t,e,i=[""],s){const{resolver:n}=xn(this._resolverCache,t,i);return o(e)?$e(n,e,void 0,s):n}}function xn(t,e,i){let s=t.get(e);s||(s=new Map,t.set(e,s));const n=i.join();let o=s.get(n);if(!o){o={resolver:je(e,i),subPrefixes:i.filter((t=>!t.toLowerCase().includes("hover")))},s.set(n,o)}return o}const _n=t=>o(t)&&Object.getOwnPropertyNames(t).reduce(((e,i)=>e||S(t[i])),!1);const yn=["top","bottom","left","right","chartArea"];function vn(t,e){return"top"===t||"bottom"===t||-1===yn.indexOf(t)&&"x"===e}function Mn(t,e){return function(i,s){return i[t]===s[t]?i[e]-s[e]:i[t]-s[t]}}function wn(t){const e=t.chart,i=e.options.animation;e.notifyPlugins("afterRender"),d(i&&i.onComplete,[t],e)}function kn(t){const e=t.chart,i=e.options.animation;d(i&&i.onProgress,[t],e)}function Sn(t){return fe()&&"string"==typeof t?t=document.getElementById(t):t&&t.length&&(t=t[0]),t&&t.canvas&&(t=t.canvas),t}const Pn={},Dn=t=>{const e=Sn(t);return Object.values(Pn).filter((t=>t.canvas===e)).pop()};function Cn(t,e,i){const s=Object.keys(t);for(const n of s){const s=+n;if(s>=e){const o=t[n];delete t[n],(i>0||s>e)&&(t[s+i]=o)}}}function On(t,e,i){return t.options.clip?t[i]:e[i]}class An{static defaults=ue;static instances=Pn;static overrides=re;static registry=en;static version="4.4.0";static getChart=Dn;static register(...t){en.add(...t),Tn()}static unregister(...t){en.remove(...t),Tn()}constructor(t,e){const s=this.config=new bn(e),n=Sn(t),o=Dn(n);if(o)throw new Error("Canvas is already in use. Chart with ID '"+o.id+"' must be destroyed before the canvas with ID '"+o.canvas.id+"' can be reused.");const a=s.createResolver(s.chartOptionScopes(),this.getContext());this.platform=new(s.platform||ks(n)),this.platform.updateConfig(s);const r=this.platform.acquireContext(n,a.aspectRatio),l=r&&r.canvas,h=l&&l.height,c=l&&l.width;this.id=i(),this.ctx=r,this.canvas=l,this.width=c,this.height=h,this._options=a,this._aspectRatio=this.aspectRatio,this._layers=[],this._metasets=[],this._stacks=void 0,this.boxes=[],this.currentDevicePixelRatio=void 0,this.chartArea=void 0,this._active=[],this._lastEvent=void 0,this._listeners={},this._responsiveListeners=void 0,this._sortedMetasets=[],this.scales={},this._plugins=new sn,this.$proxies={},this._hiddenIndices={},this.attached=!1,this._animationsDisabled=void 0,this.$context=void 0,this._doResize=dt((t=>this.update(t)),a.resizeDelay||0),this._dataChanges=[],Pn[this.id]=this,r&&l?(xt.listen(this,"complete",wn),xt.listen(this,"progress",kn),this._initialize(),this.attached&&this.update()):console.error("Failed to create chart: can't acquire context from the given item")}get aspectRatio(){const{options:{aspectRatio:t,maintainAspectRatio:e},width:i,height:n,_aspectRatio:o}=this;return s(t)?e&&o?o:n?i/n:null:t}get data(){return this.config.data}set data(t){this.config.data=t}get options(){return this._options}set options(t){this.config.options=t}get registry(){return en}_initialize(){return this.notifyPlugins("beforeInit"),this.options.responsive?this.resize():ke(this,this.options.devicePixelRatio),this.bindEvents(),this.notifyPlugins("afterInit"),this}clear(){return Te(this.canvas,this.ctx),this}stop(){return xt.stop(this),this}resize(t,e){xt.running(this)?this._resizeBeforeDraw={width:t,height:e}:this._resize(t,e)}_resize(t,e){const i=this.options,s=this.canvas,n=i.maintainAspectRatio&&this.aspectRatio,o=this.platform.getMaximumSize(s,t,e,n),a=i.devicePixelRatio||this.platform.getDevicePixelRatio(),r=this.width?"resize":"attach";this.width=o.width,this.height=o.height,this._aspectRatio=this.aspectRatio,ke(this,a,!0)&&(this.notifyPlugins("resize",{size:o}),d(i.onResize,[this,o],this),this.attached&&this._doResize(r)&&this.render())}ensureScalesHaveIDs(){u(this.options.scales||{},((t,e)=>{t.id=e}))}buildOrUpdateScales(){const t=this.options,e=t.scales,i=this.scales,s=Object.keys(i).reduce(((t,e)=>(t[e]=!1,t)),{});let n=[];e&&(n=n.concat(Object.keys(e).map((t=>{const i=e[t],s=ln(t,i),n="r"===s,o="x"===s;return{options:i,dposition:n?"chartArea":o?"bottom":"left",dtype:n?"radialLinear":o?"category":"linear"}})))),u(n,(e=>{const n=e.options,o=n.id,a=ln(o,n),r=l(n.type,e.dtype);void 0!==n.position&&vn(n.position,a)===vn(e.dposition)||(n.position=e.dposition),s[o]=!0;let h=null;if(o in i&&i[o].type===r)h=i[o];else{h=new(en.getScale(r))({id:o,type:r,ctx:this.ctx,chart:this}),i[h.id]=h}h.init(n,t)})),u(s,((t,e)=>{t||delete i[e]})),u(i,(t=>{as.configure(this,t,t.options),as.addBox(this,t)}))}_updateMetasets(){const t=this._metasets,e=this.data.datasets.length,i=t.length;if(t.sort(((t,e)=>t.index-e.index)),i>e){for(let t=e;t<i;++t)this._destroyDatasetMeta(t);t.splice(e,i-e)}this._sortedMetasets=t.slice(0).sort(Mn("order","index"))}_removeUnreferencedMetasets(){const{_metasets:t,data:{datasets:e}}=this;t.length>e.length&&delete this._stacks,t.forEach(((t,i)=>{0===e.filter((e=>e===t._dataset)).length&&this._destroyDatasetMeta(i)}))}buildOrUpdateControllers(){const t=[],e=this.data.datasets;let i,s;for(this._removeUnreferencedMetasets(),i=0,s=e.length;i<s;i++){const s=e[i];let n=this.getDatasetMeta(i);const o=s.type||this.config.type;if(n.type&&n.type!==o&&(this._destroyDatasetMeta(i),n=this.getDatasetMeta(i)),n.type=o,n.indexAxis=s.indexAxis||an(o,this.options),n.order=s.order||0,n.index=i,n.label=""+s.label,n.visible=this.isDatasetVisible(i),n.controller)n.controller.updateIndex(i),n.controller.linkScales();else{const e=en.getController(o),{datasetElementType:s,dataElementType:a}=ue.datasets[o];Object.assign(e,{dataElementType:en.getElement(a),datasetElementType:s&&en.getElement(s)}),n.controller=new e(this,i),t.push(n.controller)}}return this._updateMetasets(),t}_resetElements(){u(this.data.datasets,((t,e)=>{this.getDatasetMeta(e).controller.reset()}),this)}reset(){this._resetElements(),this.notifyPlugins("reset")}update(t){const e=this.config;e.update();const i=this._options=e.createResolver(e.chartOptionScopes(),this.getContext()),s=this._animationsDisabled=!i.animation;if(this._updateScales(),this._checkEventBindings(),this._updateHiddenIndices(),this._plugins.invalidate(),!1===this.notifyPlugins("beforeUpdate",{mode:t,cancelable:!0}))return;const n=this.buildOrUpdateControllers();this.notifyPlugins("beforeElementsUpdate");let o=0;for(let t=0,e=this.data.datasets.length;t<e;t++){const{controller:e}=this.getDatasetMeta(t),i=!s&&-1===n.indexOf(e);e.buildOrUpdateElements(i),o=Math.max(+e.getMaxOverflow(),o)}o=this._minPadding=i.layout.autoPadding?o:0,this._updateLayout(o),s||u(n,(t=>{t.reset()})),this._updateDatasets(t),this.notifyPlugins("afterUpdate",{mode:t}),this._layers.sort(Mn("z","_idx"));const{_active:a,_lastEvent:r}=this;r?this._eventHandler(r,!0):a.length&&this._updateHoverStyles(a,a,!0),this.render()}_updateScales(){u(this.scales,(t=>{as.removeBox(this,t)})),this.ensureScalesHaveIDs(),this.buildOrUpdateScales()}_checkEventBindings(){const t=this.options,e=new Set(Object.keys(this._listeners)),i=new Set(t.events);P(e,i)&&!!this._responsiveListeners===t.responsive||(this.unbindEvents(),this.bindEvents())}_updateHiddenIndices(){const{_hiddenIndices:t}=this,e=this._getUniformDataChanges()||[];for(const{method:i,start:s,count:n}of e){Cn(t,s,"_removeElements"===i?-n:n)}}_getUniformDataChanges(){const t=this._dataChanges;if(!t||!t.length)return;this._dataChanges=[];const e=this.data.datasets.length,i=e=>new Set(t.filter((t=>t[0]===e)).map(((t,e)=>e+","+t.splice(1).join(",")))),s=i(0);for(let t=1;t<e;t++)if(!P(s,i(t)))return;return Array.from(s).map((t=>t.split(","))).map((t=>({method:t[1],start:+t[2],count:+t[3]})))}_updateLayout(t){if(!1===this.notifyPlugins("beforeLayout",{cancelable:!0}))return;as.update(this,this.width,this.height,t);const e=this.chartArea,i=e.width<=0||e.height<=0;this._layers=[],u(this.boxes,(t=>{i&&"chartArea"===t.position||(t.configure&&t.configure(),this._layers.push(...t._layers()))}),this),this._layers.forEach(((t,e)=>{t._idx=e})),this.notifyPlugins("afterLayout")}_updateDatasets(t){if(!1!==this.notifyPlugins("beforeDatasetsUpdate",{mode:t,cancelable:!0})){for(let t=0,e=this.data.datasets.length;t<e;++t)this.getDatasetMeta(t).controller.configure();for(let e=0,i=this.data.datasets.length;e<i;++e)this._updateDataset(e,S(t)?t({datasetIndex:e}):t);this.notifyPlugins("afterDatasetsUpdate",{mode:t})}}_updateDataset(t,e){const i=this.getDatasetMeta(t),s={meta:i,index:t,mode:e,cancelable:!0};!1!==this.notifyPlugins("beforeDatasetUpdate",s)&&(i.controller._update(e),s.cancelable=!1,this.notifyPlugins("afterDatasetUpdate",s))}render(){!1!==this.notifyPlugins("beforeRender",{cancelable:!0})&&(xt.has(this)?this.attached&&!xt.running(this)&&xt.start(this):(this.draw(),wn({chart:this})))}draw(){let t;if(this._resizeBeforeDraw){const{width:t,height:e}=this._resizeBeforeDraw;this._resize(t,e),this._resizeBeforeDraw=null}if(this.clear(),this.width<=0||this.height<=0)return;if(!1===this.notifyPlugins("beforeDraw",{cancelable:!0}))return;const e=this._layers;for(t=0;t<e.length&&e[t].z<=0;++t)e[t].draw(this.chartArea);for(this._drawDatasets();t<e.length;++t)e[t].draw(this.chartArea);this.notifyPlugins("afterDraw")}_getSortedDatasetMetas(t){const e=this._sortedMetasets,i=[];let s,n;for(s=0,n=e.length;s<n;++s){const n=e[s];t&&!n.visible||i.push(n)}return i}getSortedVisibleDatasetMetas(){return this._getSortedDatasetMetas(!0)}_drawDatasets(){if(!1===this.notifyPlugins("beforeDatasetsDraw",{cancelable:!0}))return;const t=this.getSortedVisibleDatasetMetas();for(let e=t.length-1;e>=0;--e)this._drawDataset(t[e]);this.notifyPlugins("afterDatasetsDraw")}_drawDataset(t){const e=this.ctx,i=t._clip,s=!i.disabled,n=function(t,e){const{xScale:i,yScale:s}=t;return i&&s?{left:On(i,e,"left"),right:On(i,e,"right"),top:On(s,e,"top"),bottom:On(s,e,"bottom")}:e}(t,this.chartArea),o={meta:t,index:t.index,cancelable:!0};!1!==this.notifyPlugins("beforeDatasetDraw",o)&&(s&&Ie(e,{left:!1===i.left?0:n.left-i.left,right:!1===i.right?this.width:n.right+i.right,top:!1===i.top?0:n.top-i.top,bottom:!1===i.bottom?this.height:n.bottom+i.bottom}),t.controller.draw(),s&&ze(e),o.cancelable=!1,this.notifyPlugins("afterDatasetDraw",o))}isPointInArea(t){return Re(t,this.chartArea,this._minPadding)}getElementsAtEventForMode(t,e,i,s){const n=Xi.modes[e];return"function"==typeof n?n(this,t,i,s):[]}getDatasetMeta(t){const e=this.data.datasets[t],i=this._metasets;let s=i.filter((t=>t&&t._dataset===e)).pop();return s||(s={type:null,data:[],dataset:null,controller:null,hidden:null,xAxisID:null,yAxisID:null,order:e&&e.order||0,index:t,_dataset:e,_parsed:[],_sorted:!1},i.push(s)),s}getContext(){return this.$context||(this.$context=Ci(null,{chart:this,type:"chart"}))}getVisibleDatasetCount(){return this.getSortedVisibleDatasetMetas().length}isDatasetVisible(t){const e=this.data.datasets[t];if(!e)return!1;const i=this.getDatasetMeta(t);return"boolean"==typeof i.hidden?!i.hidden:!e.hidden}setDatasetVisibility(t,e){this.getDatasetMeta(t).hidden=!e}toggleDataVisibility(t){this._hiddenIndices[t]=!this._hiddenIndices[t]}getDataVisibility(t){return!this._hiddenIndices[t]}_updateVisibility(t,e,i){const s=i?"show":"hide",n=this.getDatasetMeta(t),o=n.controller._resolveAnimations(void 0,s);k(e)?(n.data[e].hidden=!i,this.update()):(this.setDatasetVisibility(t,i),o.update(n,{visible:i}),this.update((e=>e.datasetIndex===t?s:void 0)))}hide(t,e){this._updateVisibility(t,e,!1)}show(t,e){this._updateVisibility(t,e,!0)}_destroyDatasetMeta(t){const e=this._metasets[t];e&&e.controller&&e.controller._destroy(),delete this._metasets[t]}_stop(){let t,e;for(this.stop(),xt.remove(this),t=0,e=this.data.datasets.length;t<e;++t)this._destroyDatasetMeta(t)}destroy(){this.notifyPlugins("beforeDestroy");const{canvas:t,ctx:e}=this;this._stop(),this.config.clearCache(),t&&(this.unbindEvents(),Te(t,e),this.platform.releaseContext(e),this.canvas=null,this.ctx=null),delete Pn[this.id],this.notifyPlugins("afterDestroy")}toBase64Image(...t){return this.canvas.toDataURL(...t)}bindEvents(){this.bindUserEvents(),this.options.responsive?this.bindResponsiveEvents():this.attached=!0}bindUserEvents(){const t=this._listeners,e=this.platform,i=(i,s)=>{e.addEventListener(this,i,s),t[i]=s},s=(t,e,i)=>{t.offsetX=e,t.offsetY=i,this._eventHandler(t)};u(this.options.events,(t=>i(t,s)))}bindResponsiveEvents(){this._responsiveListeners||(this._responsiveListeners={});const t=this._responsiveListeners,e=this.platform,i=(i,s)=>{e.addEventListener(this,i,s),t[i]=s},s=(i,s)=>{t[i]&&(e.removeEventListener(this,i,s),delete t[i])},n=(t,e)=>{this.canvas&&this.resize(t,e)};let o;const a=()=>{s("attach",a),this.attached=!0,this.resize(),i("resize",n),i("detach",o)};o=()=>{this.attached=!1,s("resize",n),this._stop(),this._resize(0,0),i("attach",a)},e.isAttached(this.canvas)?a():o()}unbindEvents(){u(this._listeners,((t,e)=>{this.platform.removeEventListener(this,e,t)})),this._listeners={},u(this._responsiveListeners,((t,e)=>{this.platform.removeEventListener(this,e,t)})),this._responsiveListeners=void 0}updateHoverStyle(t,e,i){const s=i?"set":"remove";let n,o,a,r;for("dataset"===e&&(n=this.getDatasetMeta(t[0].datasetIndex),n.controller["_"+s+"DatasetHoverStyle"]()),a=0,r=t.length;a<r;++a){o=t[a];const e=o&&this.getDatasetMeta(o.datasetIndex).controller;e&&e[s+"HoverStyle"](o.element,o.datasetIndex,o.index)}}getActiveElements(){return this._active||[]}setActiveElements(t){const e=this._active||[],i=t.map((({datasetIndex:t,index:e})=>{const i=this.getDatasetMeta(t);if(!i)throw new Error("No dataset found at index "+t);return{datasetIndex:t,element:i.data[e],index:e}}));!f(i,e)&&(this._active=i,this._lastEvent=null,this._updateHoverStyles(i,e))}notifyPlugins(t,e,i){return this._plugins.notify(this,t,e,i)}isPluginEnabled(t){return 1===this._plugins._cache.filter((e=>e.plugin.id===t)).length}_updateHoverStyles(t,e,i){const s=this.options.hover,n=(t,e)=>t.filter((t=>!e.some((e=>t.datasetIndex===e.datasetIndex&&t.index===e.index)))),o=n(e,t),a=i?t:n(t,e);o.length&&this.updateHoverStyle(o,s.mode,!1),a.length&&s.mode&&this.updateHoverStyle(a,s.mode,!0)}_eventHandler(t,e){const i={event:t,replay:e,cancelable:!0,inChartArea:this.isPointInArea(t)},s=e=>(e.options.events||this.options.events).includes(t.native.type);if(!1===this.notifyPlugins("beforeEvent",i,s))return;const n=this._handleEvent(t,e,i.inChartArea);return i.cancelable=!1,this.notifyPlugins("afterEvent",i,s),(n||i.changed)&&this.render(),this}_handleEvent(t,e,i){const{_active:s=[],options:n}=this,o=e,a=this._getActiveElements(t,s,i,o),r=D(t),l=function(t,e,i,s){return i&&"mouseout"!==t.type?s?e:t:null}(t,this._lastEvent,i,r);i&&(this._lastEvent=null,d(n.onHover,[t,a,this],this),r&&d(n.onClick,[t,a,this],this));const h=!f(a,s);return(h||e)&&(this._active=a,this._updateHoverStyles(a,s,e)),this._lastEvent=l,h}_getActiveElements(t,e,i,s){if("mouseout"===t.type)return[];if(!i)return e;const n=this.options.hover;return this.getElementsAtEventForMode(t,n.mode,n,s)}}function Tn(){return u(An.instances,(t=>t._plugins.invalidate()))}function Ln(){throw new Error("This method is not implemented: Check that a complete date adapter is provided.")}class En{static override(t){Object.assign(En.prototype,t)}options;constructor(t){this.options=t||{}}init(){}formats(){return Ln()}parse(){return Ln()}format(){return Ln()}add(){return Ln()}diff(){return Ln()}startOf(){return Ln()}endOf(){return Ln()}}var Rn={_date:En};function In(t){const e=t.iScale,i=function(t,e){if(!t._cache.$bar){const i=t.getMatchingVisibleMetas(e);let s=[];for(let e=0,n=i.length;e<n;e++)s=s.concat(i[e].controller.getAllParsedValues(t));t._cache.$bar=lt(s.sort(((t,e)=>t-e)))}return t._cache.$bar}(e,t.type);let s,n,o,a,r=e._length;const l=()=>{32767!==o&&-32768!==o&&(k(a)&&(r=Math.min(r,Math.abs(o-a)||r)),a=o)};for(s=0,n=i.length;s<n;++s)o=e.getPixelForValue(i[s]),l();for(a=void 0,s=0,n=e.ticks.length;s<n;++s)o=e.getPixelForTick(s),l();return r}function zn(t,e,i,s){return n(t)?function(t,e,i,s){const n=i.parse(t[0],s),o=i.parse(t[1],s),a=Math.min(n,o),r=Math.max(n,o);let l=a,h=r;Math.abs(a)>Math.abs(r)&&(l=r,h=a),e[i.axis]=h,e._custom={barStart:l,barEnd:h,start:n,end:o,min:a,max:r}}(t,e,i,s):e[i.axis]=i.parse(t,s),e}function Fn(t,e,i,s){const n=t.iScale,o=t.vScale,a=n.getLabels(),r=n===o,l=[];let h,c,d,u;for(h=i,c=i+s;h<c;++h)u=e[h],d={},d[n.axis]=r||n.parse(a[h],h),l.push(zn(u,d,o,h));return l}function Vn(t){return t&&void 0!==t.barStart&&void 0!==t.barEnd}function Bn(t,e,i,s){let n=e.borderSkipped;const o={};if(!n)return void(t.borderSkipped=o);if(!0===n)return void(t.borderSkipped={top:!0,right:!0,bottom:!0,left:!0});const{start:a,end:r,reverse:l,top:h,bottom:c}=function(t){let e,i,s,n,o;return t.horizontal?(e=t.base>t.x,i="left",s="right"):(e=t.base<t.y,i="bottom",s="top"),e?(n="end",o="start"):(n="start",o="end"),{start:i,end:s,reverse:e,top:n,bottom:o}}(t);"middle"===n&&i&&(t.enableBorderRadius=!0,(i._top||0)===s?n=h:(i._bottom||0)===s?n=c:(o[Wn(c,a,r,l)]=!0,n=h)),o[Wn(n,a,r,l)]=!0,t.borderSkipped=o}function Wn(t,e,i,s){var n,o,a;return s?(a=i,t=Nn(t=(n=t)===(o=e)?a:n===a?o:n,i,e)):t=Nn(t,e,i),t}function Nn(t,e,i){return"start"===t?e:"end"===t?i:t}function Hn(t,{inflateAmount:e},i){t.inflateAmount="auto"===e?1===i?.33:0:e}class jn extends Ns{static id="doughnut";static defaults={datasetElementType:!1,dataElementType:"arc",animation:{animateRotate:!0,animateScale:!1},animations:{numbers:{type:"number",properties:["circumference","endAngle","innerRadius","outerRadius","startAngle","x","y","offset","borderWidth","spacing"]}},cutout:"50%",rotation:0,circumference:360,radius:"100%",spacing:0,indexAxis:"r"};static descriptors={_scriptable:t=>"spacing"!==t,_indexable:t=>"spacing"!==t&&!t.startsWith("borderDash")&&!t.startsWith("hoverBorderDash")};static overrides={aspectRatio:1,plugins:{legend:{labels:{generateLabels(t){const e=t.data;if(e.labels.length&&e.datasets.length){const{labels:{pointStyle:i,color:s}}=t.legend.options;return e.labels.map(((e,n)=>{const o=t.getDatasetMeta(0).controller.getStyle(n);return{text:e,fillStyle:o.backgroundColor,strokeStyle:o.borderColor,fontColor:s,lineWidth:o.borderWidth,pointStyle:i,hidden:!t.getDataVisibility(n),index:n}}))}return[]}},onClick(t,e,i){i.chart.toggleDataVisibility(e.index),i.chart.update()}}}};constructor(t,e){super(t,e),this.enableOptionSharing=!0,this.innerRadius=void 0,this.outerRadius=void 0,this.offsetX=void 0,this.offsetY=void 0}linkScales(){}parse(t,e){const i=this.getDataset().data,s=this._cachedMeta;if(!1===this._parsing)s._parsed=i;else{let n,a,r=t=>+i[t];if(o(i[t])){const{key:t="value"}=this._parsing;r=e=>+M(i[e],t)}for(n=t,a=t+e;n<a;++n)s._parsed[n]=r(n)}}_getRotation(){return $(this.options.rotation-90)}_getCircumference(){return $(this.options.circumference)}_getRotationExtents(){let t=O,e=-O;for(let i=0;i<this.chart.data.datasets.length;++i)if(this.chart.isDatasetVisible(i)&&this.chart.getDatasetMeta(i).type===this._type){const s=this.chart.getDatasetMeta(i).controller,n=s._getRotation(),o=s._getCircumference();t=Math.min(t,n),e=Math.max(e,n+o)}return{rotation:t,circumference:e-t}}update(t){const e=this.chart,{chartArea:i}=e,s=this._cachedMeta,n=s.data,o=this.getMaxBorderWidth()+this.getMaxOffset(n)+this.options.spacing,a=Math.max((Math.min(i.width,i.height)-o)/2,0),r=Math.min(h(this.options.cutout,a),1),l=this._getRingWeight(this.index),{circumference:d,rotation:u}=this._getRotationExtents(),{ratioX:f,ratioY:g,offsetX:p,offsetY:m}=function(t,e,i){let s=1,n=1,o=0,a=0;if(e<O){const r=t,l=r+e,h=Math.cos(r),c=Math.sin(r),d=Math.cos(l),u=Math.sin(l),f=(t,e,s)=>Z(t,r,l,!0)?1:Math.max(e,e*i,s,s*i),g=(t,e,s)=>Z(t,r,l,!0)?-1:Math.min(e,e*i,s,s*i),p=f(0,h,d),m=f(E,c,u),b=g(C,h,d),x=g(C+E,c,u);s=(p-b)/2,n=(m-x)/2,o=-(p+b)/2,a=-(m+x)/2}return{ratioX:s,ratioY:n,offsetX:o,offsetY:a}}(u,d,r),b=(i.width-o)/f,x=(i.height-o)/g,_=Math.max(Math.min(b,x)/2,0),y=c(this.options.radius,_),v=(y-Math.max(y*r,0))/this._getVisibleDatasetWeightTotal();this.offsetX=p*y,this.offsetY=m*y,s.total=this.calculateTotal(),this.outerRadius=y-v*this._getRingWeightOffset(this.index),this.innerRadius=Math.max(this.outerRadius-v*l,0),this.updateElements(n,0,n.length,t)}_circumference(t,e){const i=this.options,s=this._cachedMeta,n=this._getCircumference();return e&&i.animation.animateRotate||!this.chart.getDataVisibility(t)||null===s._parsed[t]||s.data[t].hidden?0:this.calculateCircumference(s._parsed[t]*n/O)}updateElements(t,e,i,s){const n="reset"===s,o=this.chart,a=o.chartArea,r=o.options.animation,l=(a.left+a.right)/2,h=(a.top+a.bottom)/2,c=n&&r.animateScale,d=c?0:this.innerRadius,u=c?0:this.outerRadius,{sharedOptions:f,includeOptions:g}=this._getSharedOptions(e,s);let p,m=this._getRotation();for(p=0;p<e;++p)m+=this._circumference(p,n);for(p=e;p<e+i;++p){const e=this._circumference(p,n),i=t[p],o={x:l+this.offsetX,y:h+this.offsetY,startAngle:m,endAngle:m+e,circumference:e,outerRadius:u,innerRadius:d};g&&(o.options=f||this.resolveDataElementOptions(p,i.active?"active":s)),m+=e,this.updateElement(i,p,o,s)}}calculateTotal(){const t=this._cachedMeta,e=t.data;let i,s=0;for(i=0;i<e.length;i++){const n=t._parsed[i];null===n||isNaN(n)||!this.chart.getDataVisibility(i)||e[i].hidden||(s+=Math.abs(n))}return s}calculateCircumference(t){const e=this._cachedMeta.total;return e>0&&!isNaN(t)?O*(Math.abs(t)/e):0}getLabelAndValue(t){const e=this._cachedMeta,i=this.chart,s=i.data.labels||[],n=ne(e._parsed[t],i.options.locale);return{label:s[t]||"",value:n}}getMaxBorderWidth(t){let e=0;const i=this.chart;let s,n,o,a,r;if(!t)for(s=0,n=i.data.datasets.length;s<n;++s)if(i.isDatasetVisible(s)){o=i.getDatasetMeta(s),t=o.data,a=o.controller;break}if(!t)return 0;for(s=0,n=t.length;s<n;++s)r=a.resolveDataElementOptions(s),"inner"!==r.borderAlign&&(e=Math.max(e,r.borderWidth||0,r.hoverBorderWidth||0));return e}getMaxOffset(t){let e=0;for(let i=0,s=t.length;i<s;++i){const t=this.resolveDataElementOptions(i);e=Math.max(e,t.offset||0,t.hoverOffset||0)}return e}_getRingWeightOffset(t){let e=0;for(let i=0;i<t;++i)this.chart.isDatasetVisible(i)&&(e+=this._getRingWeight(i));return e}_getRingWeight(t){return Math.max(l(this.chart.data.datasets[t].weight,1),0)}_getVisibleDatasetWeightTotal(){return this._getRingWeightOffset(this.chart.data.datasets.length)||1}}class $n extends Ns{static id="polarArea";static defaults={dataElementType:"arc",animation:{animateRotate:!0,animateScale:!0},animations:{numbers:{type:"number",properties:["x","y","startAngle","endAngle","innerRadius","outerRadius"]}},indexAxis:"r",startAngle:0};static overrides={aspectRatio:1,plugins:{legend:{labels:{generateLabels(t){const e=t.data;if(e.labels.length&&e.datasets.length){const{labels:{pointStyle:i,color:s}}=t.legend.options;return e.labels.map(((e,n)=>{const o=t.getDatasetMeta(0).controller.getStyle(n);return{text:e,fillStyle:o.backgroundColor,strokeStyle:o.borderColor,fontColor:s,lineWidth:o.borderWidth,pointStyle:i,hidden:!t.getDataVisibility(n),index:n}}))}return[]}},onClick(t,e,i){i.chart.toggleDataVisibility(e.index),i.chart.update()}}},scales:{r:{type:"radialLinear",angleLines:{display:!1},beginAtZero:!0,grid:{circular:!0},pointLabels:{display:!1},startAngle:0}}};constructor(t,e){super(t,e),this.innerRadius=void 0,this.outerRadius=void 0}getLabelAndValue(t){const e=this._cachedMeta,i=this.chart,s=i.data.labels||[],n=ne(e._parsed[t].r,i.options.locale);return{label:s[t]||"",value:n}}parseObjectData(t,e,i,s){return ii.bind(this)(t,e,i,s)}update(t){const e=this._cachedMeta.data;this._updateRadius(),this.updateElements(e,0,e.length,t)}getMinMax(){const t=this._cachedMeta,e={min:Number.POSITIVE_INFINITY,max:Number.NEGATIVE_INFINITY};return t.data.forEach(((t,i)=>{const s=this.getParsed(i).r;!isNaN(s)&&this.chart.getDataVisibility(i)&&(s<e.min&&(e.min=s),s>e.max&&(e.max=s))})),e}_updateRadius(){const t=this.chart,e=t.chartArea,i=t.options,s=Math.min(e.right-e.left,e.bottom-e.top),n=Math.max(s/2,0),o=(n-Math.max(i.cutoutPercentage?n/100*i.cutoutPercentage:1,0))/t.getVisibleDatasetCount();this.outerRadius=n-o*this.index,this.innerRadius=this.outerRadius-o}updateElements(t,e,i,s){const n="reset"===s,o=this.chart,a=o.options.animation,r=this._cachedMeta.rScale,l=r.xCenter,h=r.yCenter,c=r.getIndexAngle(0)-.5*C;let d,u=c;const f=360/this.countVisibleElements();for(d=0;d<e;++d)u+=this._computeAngle(d,s,f);for(d=e;d<e+i;d++){const e=t[d];let i=u,g=u+this._computeAngle(d,s,f),p=o.getDataVisibility(d)?r.getDistanceFromCenterForValue(this.getParsed(d).r):0;u=g,n&&(a.animateScale&&(p=0),a.animateRotate&&(i=g=c));const m={x:l,y:h,innerRadius:0,outerRadius:p,startAngle:i,endAngle:g,options:this.resolveDataElementOptions(d,e.active?"active":s)};this.updateElement(e,d,m,s)}}countVisibleElements(){const t=this._cachedMeta;let e=0;return t.data.forEach(((t,i)=>{!isNaN(this.getParsed(i).r)&&this.chart.getDataVisibility(i)&&e++})),e}_computeAngle(t,e,i){return this.chart.getDataVisibility(t)?$(this.resolveDataElementOptions(t,e).angle||i):0}}var Yn=Object.freeze({__proto__:null,BarController:class extends Ns{static id="bar";static defaults={datasetElementType:!1,dataElementType:"bar",categoryPercentage:.8,barPercentage:.9,grouped:!0,animations:{numbers:{type:"number",properties:["x","y","base","width","height"]}}};static overrides={scales:{_index_:{type:"category",offset:!0,grid:{offset:!0}},_value_:{type:"linear",beginAtZero:!0}}};parsePrimitiveData(t,e,i,s){return Fn(t,e,i,s)}parseArrayData(t,e,i,s){return Fn(t,e,i,s)}parseObjectData(t,e,i,s){const{iScale:n,vScale:o}=t,{xAxisKey:a="x",yAxisKey:r="y"}=this._parsing,l="x"===n.axis?a:r,h="x"===o.axis?a:r,c=[];let d,u,f,g;for(d=i,u=i+s;d<u;++d)g=e[d],f={},f[n.axis]=n.parse(M(g,l),d),c.push(zn(M(g,h),f,o,d));return c}updateRangeFromParsed(t,e,i,s){super.updateRangeFromParsed(t,e,i,s);const n=i._custom;n&&e===this._cachedMeta.vScale&&(t.min=Math.min(t.min,n.min),t.max=Math.max(t.max,n.max))}getMaxOverflow(){return 0}getLabelAndValue(t){const e=this._cachedMeta,{iScale:i,vScale:s}=e,n=this.getParsed(t),o=n._custom,a=Vn(o)?"["+o.start+", "+o.end+"]":""+s.getLabelForValue(n[s.axis]);return{label:""+i.getLabelForValue(n[i.axis]),value:a}}initialize(){this.enableOptionSharing=!0,super.initialize();this._cachedMeta.stack=this.getDataset().stack}update(t){const e=this._cachedMeta;this.updateElements(e.data,0,e.data.length,t)}updateElements(t,e,i,n){const o="reset"===n,{index:a,_cachedMeta:{vScale:r}}=this,l=r.getBasePixel(),h=r.isHorizontal(),c=this._getRuler(),{sharedOptions:d,includeOptions:u}=this._getSharedOptions(e,n);for(let f=e;f<e+i;f++){const e=this.getParsed(f),i=o||s(e[r.axis])?{base:l,head:l}:this._calculateBarValuePixels(f),g=this._calculateBarIndexPixels(f,c),p=(e._stacks||{})[r.axis],m={horizontal:h,base:i.base,enableBorderRadius:!p||Vn(e._custom)||a===p._top||a===p._bottom,x:h?i.head:g.center,y:h?g.center:i.head,height:h?g.size:Math.abs(i.size),width:h?Math.abs(i.size):g.size};u&&(m.options=d||this.resolveDataElementOptions(f,t[f].active?"active":n));const b=m.options||t[f].options;Bn(m,b,p,a),Hn(m,b,c.ratio),this.updateElement(t[f],f,m,n)}}_getStacks(t,e){const{iScale:i}=this._cachedMeta,n=i.getMatchingVisibleMetas(this._type).filter((t=>t.controller.options.grouped)),o=i.options.stacked,a=[],r=t=>{const i=t.controller.getParsed(e),n=i&&i[t.vScale.axis];if(s(n)||isNaN(n))return!0};for(const i of n)if((void 0===e||!r(i))&&((!1===o||-1===a.indexOf(i.stack)||void 0===o&&void 0===i.stack)&&a.push(i.stack),i.index===t))break;return a.length||a.push(void 0),a}_getStackCount(t){return this._getStacks(void 0,t).length}_getStackIndex(t,e,i){const s=this._getStacks(t,i),n=void 0!==e?s.indexOf(e):-1;return-1===n?s.length-1:n}_getRuler(){const t=this.options,e=this._cachedMeta,i=e.iScale,s=[];let n,o;for(n=0,o=e.data.length;n<o;++n)s.push(i.getPixelForValue(this.getParsed(n)[i.axis],n));const a=t.barThickness;return{min:a||In(e),pixels:s,start:i._startPixel,end:i._endPixel,stackCount:this._getStackCount(),scale:i,grouped:t.grouped,ratio:a?1:t.categoryPercentage*t.barPercentage}}_calculateBarValuePixels(t){const{_cachedMeta:{vScale:e,_stacked:i,index:n},options:{base:o,minBarLength:a}}=this,r=o||0,l=this.getParsed(t),h=l._custom,c=Vn(h);let d,u,f=l[e.axis],g=0,p=i?this.applyStack(e,l,i):f;p!==f&&(g=p-f,p=f),c&&(f=h.barStart,p=h.barEnd-h.barStart,0!==f&&F(f)!==F(h.barEnd)&&(g=0),g+=f);const m=s(o)||c?g:o;let b=e.getPixelForValue(m);if(d=this.chart.getDataVisibility(t)?e.getPixelForValue(g+p):b,u=d-b,Math.abs(u)<a){u=function(t,e,i){return 0!==t?F(t):(e.isHorizontal()?1:-1)*(e.min>=i?1:-1)}(u,e,r)*a,f===r&&(b-=u/2);const t=e.getPixelForDecimal(0),s=e.getPixelForDecimal(1),o=Math.min(t,s),h=Math.max(t,s);b=Math.max(Math.min(b,h),o),d=b+u,i&&!c&&(l._stacks[e.axis]._visualValues[n]=e.getValueForPixel(d)-e.getValueForPixel(b))}if(b===e.getPixelForValue(r)){const t=F(u)*e.getLineWidthForValue(r)/2;b+=t,u-=t}return{size:u,base:b,head:d,center:d+u/2}}_calculateBarIndexPixels(t,e){const i=e.scale,n=this.options,o=n.skipNull,a=l(n.maxBarThickness,1/0);let r,h;if(e.grouped){const i=o?this._getStackCount(t):e.stackCount,l="flex"===n.barThickness?function(t,e,i,s){const n=e.pixels,o=n[t];let a=t>0?n[t-1]:null,r=t<n.length-1?n[t+1]:null;const l=i.categoryPercentage;null===a&&(a=o-(null===r?e.end-e.start:r-o)),null===r&&(r=o+o-a);const h=o-(o-Math.min(a,r))/2*l;return{chunk:Math.abs(r-a)/2*l/s,ratio:i.barPercentage,start:h}}(t,e,n,i):function(t,e,i,n){const o=i.barThickness;let a,r;return s(o)?(a=e.min*i.categoryPercentage,r=i.barPercentage):(a=o*n,r=1),{chunk:a/n,ratio:r,start:e.pixels[t]-a/2}}(t,e,n,i),c=this._getStackIndex(this.index,this._cachedMeta.stack,o?t:void 0);r=l.start+l.chunk*c+l.chunk/2,h=Math.min(a,l.chunk*l.ratio)}else r=i.getPixelForValue(this.getParsed(t)[i.axis],t),h=Math.min(a,e.min*e.ratio);return{base:r-h/2,head:r+h/2,center:r,size:h}}draw(){const t=this._cachedMeta,e=t.vScale,i=t.data,s=i.length;let n=0;for(;n<s;++n)null!==this.getParsed(n)[e.axis]&&i[n].draw(this._ctx)}},BubbleController:class extends Ns{static id="bubble";static defaults={datasetElementType:!1,dataElementType:"point",animations:{numbers:{type:"number",properties:["x","y","borderWidth","radius"]}}};static overrides={scales:{x:{type:"linear"},y:{type:"linear"}}};initialize(){this.enableOptionSharing=!0,super.initialize()}parsePrimitiveData(t,e,i,s){const n=super.parsePrimitiveData(t,e,i,s);for(let t=0;t<n.length;t++)n[t]._custom=this.resolveDataElementOptions(t+i).radius;return n}parseArrayData(t,e,i,s){const n=super.parseArrayData(t,e,i,s);for(let t=0;t<n.length;t++){const s=e[i+t];n[t]._custom=l(s[2],this.resolveDataElementOptions(t+i).radius)}return n}parseObjectData(t,e,i,s){const n=super.parseObjectData(t,e,i,s);for(let t=0;t<n.length;t++){const s=e[i+t];n[t]._custom=l(s&&s.r&&+s.r,this.resolveDataElementOptions(t+i).radius)}return n}getMaxOverflow(){const t=this._cachedMeta.data;let e=0;for(let i=t.length-1;i>=0;--i)e=Math.max(e,t[i].size(this.resolveDataElementOptions(i))/2);return e>0&&e}getLabelAndValue(t){const e=this._cachedMeta,i=this.chart.data.labels||[],{xScale:s,yScale:n}=e,o=this.getParsed(t),a=s.getLabelForValue(o.x),r=n.getLabelForValue(o.y),l=o._custom;return{label:i[t]||"",value:"("+a+", "+r+(l?", "+l:"")+")"}}update(t){const e=this._cachedMeta.data;this.updateElements(e,0,e.length,t)}updateElements(t,e,i,s){const n="reset"===s,{iScale:o,vScale:a}=this._cachedMeta,{sharedOptions:r,includeOptions:l}=this._getSharedOptions(e,s),h=o.axis,c=a.axis;for(let d=e;d<e+i;d++){const e=t[d],i=!n&&this.getParsed(d),u={},f=u[h]=n?o.getPixelForDecimal(.5):o.getPixelForValue(i[h]),g=u[c]=n?a.getBasePixel():a.getPixelForValue(i[c]);u.skip=isNaN(f)||isNaN(g),l&&(u.options=r||this.resolveDataElementOptions(d,e.active?"active":s),n&&(u.options.radius=0)),this.updateElement(e,d,u,s)}}resolveDataElementOptions(t,e){const i=this.getParsed(t);let s=super.resolveDataElementOptions(t,e);s.$shared&&(s=Object.assign({},s,{$shared:!1}));const n=s.radius;return"active"!==e&&(s.radius=0),s.radius+=l(i&&i._custom,n),s}},DoughnutController:jn,LineController:class extends Ns{static id="line";static defaults={datasetElementType:"line",dataElementType:"point",showLine:!0,spanGaps:!1};static overrides={scales:{_index_:{type:"category"},_value_:{type:"linear"}}};initialize(){this.enableOptionSharing=!0,this.supportsDecimation=!0,super.initialize()}update(t){const e=this._cachedMeta,{dataset:i,data:s=[],_dataset:n}=e,o=this.chart._animationsDisabled;let{start:a,count:r}=pt(e,s,o);this._drawStart=a,this._drawCount=r,mt(e)&&(a=0,r=s.length),i._chart=this.chart,i._datasetIndex=this.index,i._decimated=!!n._decimated,i.points=s;const l=this.resolveDatasetElementOptions(t);this.options.showLine||(l.borderWidth=0),l.segment=this.options.segment,this.updateElement(i,void 0,{animated:!o,options:l},t),this.updateElements(s,a,r,t)}updateElements(t,e,i,n){const o="reset"===n,{iScale:a,vScale:r,_stacked:l,_dataset:h}=this._cachedMeta,{sharedOptions:c,includeOptions:d}=this._getSharedOptions(e,n),u=a.axis,f=r.axis,{spanGaps:g,segment:p}=this.options,m=N(g)?g:Number.POSITIVE_INFINITY,b=this.chart._animationsDisabled||o||"none"===n,x=e+i,_=t.length;let y=e>0&&this.getParsed(e-1);for(let i=0;i<_;++i){const g=t[i],_=b?g:{};if(i<e||i>=x){_.skip=!0;continue}const v=this.getParsed(i),M=s(v[f]),w=_[u]=a.getPixelForValue(v[u],i),k=_[f]=o||M?r.getBasePixel():r.getPixelForValue(l?this.applyStack(r,v,l):v[f],i);_.skip=isNaN(w)||isNaN(k)||M,_.stop=i>0&&Math.abs(v[u]-y[u])>m,p&&(_.parsed=v,_.raw=h.data[i]),d&&(_.options=c||this.resolveDataElementOptions(i,g.active?"active":n)),b||this.updateElement(g,i,_,n),y=v}}getMaxOverflow(){const t=this._cachedMeta,e=t.dataset,i=e.options&&e.options.borderWidth||0,s=t.data||[];if(!s.length)return i;const n=s[0].size(this.resolveDataElementOptions(0)),o=s[s.length-1].size(this.resolveDataElementOptions(s.length-1));return Math.max(i,n,o)/2}draw(){const t=this._cachedMeta;t.dataset.updateControlPoints(this.chart.chartArea,t.iScale.axis),super.draw()}},PieController:class extends jn{static id="pie";static defaults={cutout:0,rotation:0,circumference:360,radius:"100%"}},PolarAreaController:$n,RadarController:class extends Ns{static id="radar";static defaults={datasetElementType:"line",dataElementType:"point",indexAxis:"r",showLine:!0,elements:{line:{fill:"start"}}};static overrides={aspectRatio:1,scales:{r:{type:"radialLinear"}}};getLabelAndValue(t){const e=this._cachedMeta.vScale,i=this.getParsed(t);return{label:e.getLabels()[t],value:""+e.getLabelForValue(i[e.axis])}}parseObjectData(t,e,i,s){return ii.bind(this)(t,e,i,s)}update(t){const e=this._cachedMeta,i=e.dataset,s=e.data||[],n=e.iScale.getLabels();if(i.points=s,"resize"!==t){const e=this.resolveDatasetElementOptions(t);this.options.showLine||(e.borderWidth=0);const o={_loop:!0,_fullLoop:n.length===s.length,options:e};this.updateElement(i,void 0,o,t)}this.updateElements(s,0,s.length,t)}updateElements(t,e,i,s){const n=this._cachedMeta.rScale,o="reset"===s;for(let a=e;a<e+i;a++){const e=t[a],i=this.resolveDataElementOptions(a,e.active?"active":s),r=n.getPointPositionForValue(a,this.getParsed(a).r),l=o?n.xCenter:r.x,h=o?n.yCenter:r.y,c={x:l,y:h,angle:r.angle,skip:isNaN(l)||isNaN(h),options:i};this.updateElement(e,a,c,s)}}},ScatterController:class extends Ns{static id="scatter";static defaults={datasetElementType:!1,dataElementType:"point",showLine:!1,fill:!1};static overrides={interaction:{mode:"point"},scales:{x:{type:"linear"},y:{type:"linear"}}};getLabelAndValue(t){const e=this._cachedMeta,i=this.chart.data.labels||[],{xScale:s,yScale:n}=e,o=this.getParsed(t),a=s.getLabelForValue(o.x),r=n.getLabelForValue(o.y);return{label:i[t]||"",value:"("+a+", "+r+")"}}update(t){const e=this._cachedMeta,{data:i=[]}=e,s=this.chart._animationsDisabled;let{start:n,count:o}=pt(e,i,s);if(this._drawStart=n,this._drawCount=o,mt(e)&&(n=0,o=i.length),this.options.showLine){this.datasetElementType||this.addElements();const{dataset:n,_dataset:o}=e;n._chart=this.chart,n._datasetIndex=this.index,n._decimated=!!o._decimated,n.points=i;const a=this.resolveDatasetElementOptions(t);a.segment=this.options.segment,this.updateElement(n,void 0,{animated:!s,options:a},t)}else this.datasetElementType&&(delete e.dataset,this.datasetElementType=!1);this.updateElements(i,n,o,t)}addElements(){const{showLine:t}=this.options;!this.datasetElementType&&t&&(this.datasetElementType=this.chart.registry.getElement("line")),super.addElements()}updateElements(t,e,i,n){const o="reset"===n,{iScale:a,vScale:r,_stacked:l,_dataset:h}=this._cachedMeta,c=this.resolveDataElementOptions(e,n),d=this.getSharedOptions(c),u=this.includeOptions(n,d),f=a.axis,g=r.axis,{spanGaps:p,segment:m}=this.options,b=N(p)?p:Number.POSITIVE_INFINITY,x=this.chart._animationsDisabled||o||"none"===n;let _=e>0&&this.getParsed(e-1);for(let c=e;c<e+i;++c){const e=t[c],i=this.getParsed(c),p=x?e:{},y=s(i[g]),v=p[f]=a.getPixelForValue(i[f],c),M=p[g]=o||y?r.getBasePixel():r.getPixelForValue(l?this.applyStack(r,i,l):i[g],c);p.skip=isNaN(v)||isNaN(M)||y,p.stop=c>0&&Math.abs(i[f]-_[f])>b,m&&(p.parsed=i,p.raw=h.data[c]),u&&(p.options=d||this.resolveDataElementOptions(c,e.active?"active":n)),x||this.updateElement(e,c,p,n),_=i}this.updateSharedOptions(d,n,c)}getMaxOverflow(){const t=this._cachedMeta,e=t.data||[];if(!this.options.showLine){let t=0;for(let i=e.length-1;i>=0;--i)t=Math.max(t,e[i].size(this.resolveDataElementOptions(i))/2);return t>0&&t}const i=t.dataset,s=i.options&&i.options.borderWidth||0;if(!e.length)return s;const n=e[0].size(this.resolveDataElementOptions(0)),o=e[e.length-1].size(this.resolveDataElementOptions(e.length-1));return Math.max(s,n,o)/2}}});function Un(t,e,i,s){const n=vi(t.options.borderRadius,["outerStart","outerEnd","innerStart","innerEnd"]);const o=(i-e)/2,a=Math.min(o,s*e/2),r=t=>{const e=(i-Math.min(o,t))*s/2;return J(t,0,Math.min(o,e))};return{outerStart:r(n.outerStart),outerEnd:r(n.outerEnd),innerStart:J(n.innerStart,0,a),innerEnd:J(n.innerEnd,0,a)}}function Xn(t,e,i,s){return{x:i+t*Math.cos(e),y:s+t*Math.sin(e)}}function qn(t,e,i,s,n,o){const{x:a,y:r,startAngle:l,pixelMargin:h,innerRadius:c}=e,d=Math.max(e.outerRadius+s+i-h,0),u=c>0?c+s+i+h:0;let f=0;const g=n-l;if(s){const t=((c>0?c-s:0)+(d>0?d-s:0))/2;f=(g-(0!==t?g*t/(t+s):g))/2}const p=(g-Math.max(.001,g*d-i/C)/d)/2,m=l+p+f,b=n-p-f,{outerStart:x,outerEnd:_,innerStart:y,innerEnd:v}=Un(e,u,d,b-m),M=d-x,w=d-_,k=m+x/M,S=b-_/w,P=u+y,D=u+v,O=m+y/P,A=b-v/D;if(t.beginPath(),o){const e=(k+S)/2;if(t.arc(a,r,d,k,e),t.arc(a,r,d,e,S),_>0){const e=Xn(w,S,a,r);t.arc(e.x,e.y,_,S,b+E)}const i=Xn(D,b,a,r);if(t.lineTo(i.x,i.y),v>0){const e=Xn(D,A,a,r);t.arc(e.x,e.y,v,b+E,A+Math.PI)}const s=(b-v/u+(m+y/u))/2;if(t.arc(a,r,u,b-v/u,s,!0),t.arc(a,r,u,s,m+y/u,!0),y>0){const e=Xn(P,O,a,r);t.arc(e.x,e.y,y,O+Math.PI,m-E)}const n=Xn(M,m,a,r);if(t.lineTo(n.x,n.y),x>0){const e=Xn(M,k,a,r);t.arc(e.x,e.y,x,m-E,k)}}else{t.moveTo(a,r);const e=Math.cos(k)*d+a,i=Math.sin(k)*d+r;t.lineTo(e,i);const s=Math.cos(S)*d+a,n=Math.sin(S)*d+r;t.lineTo(s,n)}t.closePath()}function Kn(t,e,i,s,n){const{fullCircles:o,startAngle:a,circumference:r,options:l}=e,{borderWidth:h,borderJoinStyle:c,borderDash:d,borderDashOffset:u}=l,f="inner"===l.borderAlign;if(!h)return;t.setLineDash(d||[]),t.lineDashOffset=u,f?(t.lineWidth=2*h,t.lineJoin=c||"round"):(t.lineWidth=h,t.lineJoin=c||"bevel");let g=e.endAngle;if(o){qn(t,e,i,s,g,n);for(let e=0;e<o;++e)t.stroke();isNaN(r)||(g=a+(r%O||O))}f&&function(t,e,i){const{startAngle:s,pixelMargin:n,x:o,y:a,outerRadius:r,innerRadius:l}=e;let h=n/r;t.beginPath(),t.arc(o,a,r,s-h,i+h),l>n?(h=n/l,t.arc(o,a,l,i+h,s-h,!0)):t.arc(o,a,n,i+E,s-E),t.closePath(),t.clip()}(t,e,g),o||(qn(t,e,i,s,g,n),t.stroke())}function Gn(t,e,i=e){t.lineCap=l(i.borderCapStyle,e.borderCapStyle),t.setLineDash(l(i.borderDash,e.borderDash)),t.lineDashOffset=l(i.borderDashOffset,e.borderDashOffset),t.lineJoin=l(i.borderJoinStyle,e.borderJoinStyle),t.lineWidth=l(i.borderWidth,e.borderWidth),t.strokeStyle=l(i.borderColor,e.borderColor)}function Zn(t,e,i){t.lineTo(i.x,i.y)}function Jn(t,e,i={}){const s=t.length,{start:n=0,end:o=s-1}=i,{start:a,end:r}=e,l=Math.max(n,a),h=Math.min(o,r),c=n<a&&o<a||n>r&&o>r;return{count:s,start:l,loop:e.loop,ilen:h<l&&!c?s+h-l:h-l}}function Qn(t,e,i,s){const{points:n,options:o}=e,{count:a,start:r,loop:l,ilen:h}=Jn(n,i,s),c=function(t){return t.stepped?Fe:t.tension||"monotone"===t.cubicInterpolationMode?Ve:Zn}(o);let d,u,f,{move:g=!0,reverse:p}=s||{};for(d=0;d<=h;++d)u=n[(r+(p?h-d:d))%a],u.skip||(g?(t.moveTo(u.x,u.y),g=!1):c(t,f,u,p,o.stepped),f=u);return l&&(u=n[(r+(p?h:0))%a],c(t,f,u,p,o.stepped)),!!l}function to(t,e,i,s){const n=e.points,{count:o,start:a,ilen:r}=Jn(n,i,s),{move:l=!0,reverse:h}=s||{};let c,d,u,f,g,p,m=0,b=0;const x=t=>(a+(h?r-t:t))%o,_=()=>{f!==g&&(t.lineTo(m,g),t.lineTo(m,f),t.lineTo(m,p))};for(l&&(d=n[x(0)],t.moveTo(d.x,d.y)),c=0;c<=r;++c){if(d=n[x(c)],d.skip)continue;const e=d.x,i=d.y,s=0|e;s===u?(i<f?f=i:i>g&&(g=i),m=(b*m+e)/++b):(_(),t.lineTo(e,i),u=s,b=0,f=g=i),p=i}_()}function eo(t){const e=t.options,i=e.borderDash&&e.borderDash.length;return!(t._decimated||t._loop||e.tension||"monotone"===e.cubicInterpolationMode||e.stepped||i)?to:Qn}const io="function"==typeof Path2D;function so(t,e,i,s){io&&!e.options.segment?function(t,e,i,s){let n=e._path;n||(n=e._path=new Path2D,e.path(n,i,s)&&n.closePath()),Gn(t,e.options),t.stroke(n)}(t,e,i,s):function(t,e,i,s){const{segments:n,options:o}=e,a=eo(e);for(const r of n)Gn(t,o,r.style),t.beginPath(),a(t,e,r,{start:i,end:i+s-1})&&t.closePath(),t.stroke()}(t,e,i,s)}class no extends Hs{static id="line";static defaults={borderCapStyle:"butt",borderDash:[],borderDashOffset:0,borderJoinStyle:"miter",borderWidth:3,capBezierPoints:!0,cubicInterpolationMode:"default",fill:!1,spanGaps:!1,stepped:!1,tension:0};static defaultRoutes={backgroundColor:"backgroundColor",borderColor:"borderColor"};static descriptors={_scriptable:!0,_indexable:t=>"borderDash"!==t&&"fill"!==t};constructor(t){super(),this.animated=!0,this.options=void 0,this._chart=void 0,this._loop=void 0,this._fullLoop=void 0,this._path=void 0,this._points=void 0,this._segments=void 0,this._decimated=!1,this._pointsUpdated=!1,this._datasetIndex=void 0,t&&Object.assign(this,t)}updateControlPoints(t,e){const i=this.options;if((i.tension||"monotone"===i.cubicInterpolationMode)&&!i.stepped&&!this._pointsUpdated){const s=i.spanGaps?this._loop:this._fullLoop;hi(this._points,i,t,s,e),this._pointsUpdated=!0}}set points(t){this._points=t,delete this._segments,delete this._path,this._pointsUpdated=!1}get points(){return this._points}get segments(){return this._segments||(this._segments=zi(this,this.options.segment))}first(){const t=this.segments,e=this.points;return t.length&&e[t[0].start]}last(){const t=this.segments,e=this.points,i=t.length;return i&&e[t[i-1].end]}interpolate(t,e){const i=this.options,s=t[e],n=this.points,o=Ii(this,{property:e,start:s,end:s});if(!o.length)return;const a=[],r=function(t){return t.stepped?pi:t.tension||"monotone"===t.cubicInterpolationMode?mi:gi}(i);let l,h;for(l=0,h=o.length;l<h;++l){const{start:h,end:c}=o[l],d=n[h],u=n[c];if(d===u){a.push(d);continue}const f=r(d,u,Math.abs((s-d[e])/(u[e]-d[e])),i.stepped);f[e]=t[e],a.push(f)}return 1===a.length?a[0]:a}pathSegment(t,e,i){return eo(this)(t,this,e,i)}path(t,e,i){const s=this.segments,n=eo(this);let o=this._loop;e=e||0,i=i||this.points.length-e;for(const a of s)o&=n(t,this,a,{start:e,end:e+i-1});return!!o}draw(t,e,i,s){const n=this.options||{};(this.points||[]).length&&n.borderWidth&&(t.save(),so(t,this,i,s),t.restore()),this.animated&&(this._pointsUpdated=!1,this._path=void 0)}}function oo(t,e,i,s){const n=t.options,{[i]:o}=t.getProps([i],s);return Math.abs(e-o)<n.radius+n.hitRadius}function ao(t,e){const{x:i,y:s,base:n,width:o,height:a}=t.getProps(["x","y","base","width","height"],e);let r,l,h,c,d;return t.horizontal?(d=a/2,r=Math.min(i,n),l=Math.max(i,n),h=s-d,c=s+d):(d=o/2,r=i-d,l=i+d,h=Math.min(s,n),c=Math.max(s,n)),{left:r,top:h,right:l,bottom:c}}function ro(t,e,i,s){return t?0:J(e,i,s)}function lo(t){const e=ao(t),i=e.right-e.left,s=e.bottom-e.top,n=function(t,e,i){const s=t.options.borderWidth,n=t.borderSkipped,o=Mi(s);return{t:ro(n.top,o.top,0,i),r:ro(n.right,o.right,0,e),b:ro(n.bottom,o.bottom,0,i),l:ro(n.left,o.left,0,e)}}(t,i/2,s/2),a=function(t,e,i){const{enableBorderRadius:s}=t.getProps(["enableBorderRadius"]),n=t.options.borderRadius,a=wi(n),r=Math.min(e,i),l=t.borderSkipped,h=s||o(n);return{topLeft:ro(!h||l.top||l.left,a.topLeft,0,r),topRight:ro(!h||l.top||l.right,a.topRight,0,r),bottomLeft:ro(!h||l.bottom||l.left,a.bottomLeft,0,r),bottomRight:ro(!h||l.bottom||l.right,a.bottomRight,0,r)}}(t,i/2,s/2);return{outer:{x:e.left,y:e.top,w:i,h:s,radius:a},inner:{x:e.left+n.l,y:e.top+n.t,w:i-n.l-n.r,h:s-n.t-n.b,radius:{topLeft:Math.max(0,a.topLeft-Math.max(n.t,n.l)),topRight:Math.max(0,a.topRight-Math.max(n.t,n.r)),bottomLeft:Math.max(0,a.bottomLeft-Math.max(n.b,n.l)),bottomRight:Math.max(0,a.bottomRight-Math.max(n.b,n.r))}}}}function ho(t,e,i,s){const n=null===e,o=null===i,a=t&&!(n&&o)&&ao(t,s);return a&&(n||tt(e,a.left,a.right))&&(o||tt(i,a.top,a.bottom))}function co(t,e){t.rect(e.x,e.y,e.w,e.h)}function uo(t,e,i={}){const s=t.x!==i.x?-e:0,n=t.y!==i.y?-e:0,o=(t.x+t.w!==i.x+i.w?e:0)-s,a=(t.y+t.h!==i.y+i.h?e:0)-n;return{x:t.x+s,y:t.y+n,w:t.w+o,h:t.h+a,radius:t.radius}}var fo=Object.freeze({__proto__:null,ArcElement:class extends Hs{static id="arc";static defaults={borderAlign:"center",borderColor:"#fff",borderDash:[],borderDashOffset:0,borderJoinStyle:void 0,borderRadius:0,borderWidth:2,offset:0,spacing:0,angle:void 0,circular:!0};static defaultRoutes={backgroundColor:"backgroundColor"};static descriptors={_scriptable:!0,_indexable:t=>"borderDash"!==t};circumference;endAngle;fullCircles;innerRadius;outerRadius;pixelMargin;startAngle;constructor(t){super(),this.options=void 0,this.circumference=void 0,this.startAngle=void 0,this.endAngle=void 0,this.innerRadius=void 0,this.outerRadius=void 0,this.pixelMargin=0,this.fullCircles=0,t&&Object.assign(this,t)}inRange(t,e,i){const s=this.getProps(["x","y"],i),{angle:n,distance:o}=X(s,{x:t,y:e}),{startAngle:a,endAngle:r,innerRadius:h,outerRadius:c,circumference:d}=this.getProps(["startAngle","endAngle","innerRadius","outerRadius","circumference"],i),u=(this.options.spacing+this.options.borderWidth)/2,f=l(d,r-a)>=O||Z(n,a,r),g=tt(o,h+u,c+u);return f&&g}getCenterPoint(t){const{x:e,y:i,startAngle:s,endAngle:n,innerRadius:o,outerRadius:a}=this.getProps(["x","y","startAngle","endAngle","innerRadius","outerRadius"],t),{offset:r,spacing:l}=this.options,h=(s+n)/2,c=(o+a+l+r)/2;return{x:e+Math.cos(h)*c,y:i+Math.sin(h)*c}}tooltipPosition(t){return this.getCenterPoint(t)}draw(t){const{options:e,circumference:i}=this,s=(e.offset||0)/4,n=(e.spacing||0)/2,o=e.circular;if(this.pixelMargin="inner"===e.borderAlign?.33:0,this.fullCircles=i>O?Math.floor(i/O):0,0===i||this.innerRadius<0||this.outerRadius<0)return;t.save();const a=(this.startAngle+this.endAngle)/2;t.translate(Math.cos(a)*s,Math.sin(a)*s);const r=s*(1-Math.sin(Math.min(C,i||0)));t.fillStyle=e.backgroundColor,t.strokeStyle=e.borderColor,function(t,e,i,s,n){const{fullCircles:o,startAngle:a,circumference:r}=e;let l=e.endAngle;if(o){qn(t,e,i,s,l,n);for(let e=0;e<o;++e)t.fill();isNaN(r)||(l=a+(r%O||O))}qn(t,e,i,s,l,n),t.fill()}(t,this,r,n,o),Kn(t,this,r,n,o),t.restore()}},BarElement:class extends Hs{static id="bar";static defaults={borderSkipped:"start",borderWidth:0,borderRadius:0,inflateAmount:"auto",pointStyle:void 0};static defaultRoutes={backgroundColor:"backgroundColor",borderColor:"borderColor"};constructor(t){super(),this.options=void 0,this.horizontal=void 0,this.base=void 0,this.width=void 0,this.height=void 0,this.inflateAmount=void 0,t&&Object.assign(this,t)}draw(t){const{inflateAmount:e,options:{borderColor:i,backgroundColor:s}}=this,{inner:n,outer:o}=lo(this),a=(r=o.radius).topLeft||r.topRight||r.bottomLeft||r.bottomRight?He:co;var r;t.save(),o.w===n.w&&o.h===n.h||(t.beginPath(),a(t,uo(o,e,n)),t.clip(),a(t,uo(n,-e,o)),t.fillStyle=i,t.fill("evenodd")),t.beginPath(),a(t,uo(n,e)),t.fillStyle=s,t.fill(),t.restore()}inRange(t,e,i){return ho(this,t,e,i)}inXRange(t,e){return ho(this,t,null,e)}inYRange(t,e){return ho(this,null,t,e)}getCenterPoint(t){const{x:e,y:i,base:s,horizontal:n}=this.getProps(["x","y","base","horizontal"],t);return{x:n?(e+s)/2:e,y:n?i:(i+s)/2}}getRange(t){return"x"===t?this.width/2:this.height/2}},LineElement:no,PointElement:class extends Hs{static id="point";parsed;skip;stop;static defaults={borderWidth:1,hitRadius:1,hoverBorderWidth:1,hoverRadius:4,pointStyle:"circle",radius:3,rotation:0};static defaultRoutes={backgroundColor:"backgroundColor",borderColor:"borderColor"};constructor(t){super(),this.options=void 0,this.parsed=void 0,this.skip=void 0,this.stop=void 0,t&&Object.assign(this,t)}inRange(t,e,i){const s=this.options,{x:n,y:o}=this.getProps(["x","y"],i);return Math.pow(t-n,2)+Math.pow(e-o,2)<Math.pow(s.hitRadius+s.radius,2)}inXRange(t,e){return oo(this,t,"x",e)}inYRange(t,e){return oo(this,t,"y",e)}getCenterPoint(t){const{x:e,y:i}=this.getProps(["x","y"],t);return{x:e,y:i}}size(t){let e=(t=t||this.options||{}).radius||0;e=Math.max(e,e&&t.hoverRadius||0);return 2*(e+(e&&t.borderWidth||0))}draw(t,e){const i=this.options;this.skip||i.radius<.1||!Re(this,e,this.size(i)/2)||(t.strokeStyle=i.borderColor,t.lineWidth=i.borderWidth,t.fillStyle=i.backgroundColor,Le(t,i,this.x,this.y))}getRange(){const t=this.options||{};return t.radius+t.hitRadius}}});function go(t,e,i,s){const n=t.indexOf(e);if(-1===n)return((t,e,i,s)=>("string"==typeof e?(i=t.push(e)-1,s.unshift({index:i,label:e})):isNaN(e)&&(i=null),i))(t,e,i,s);return n!==t.lastIndexOf(e)?i:n}function po(t){const e=this.getLabels();return t>=0&&t<e.length?e[t]:t}function mo(t,e,{horizontal:i,minRotation:s}){const n=$(s),o=(i?Math.sin(n):Math.cos(n))||.001,a=.75*e*(""+t).length;return Math.min(e/o,a)}class bo extends Js{constructor(t){super(t),this.start=void 0,this.end=void 0,this._startValue=void 0,this._endValue=void 0,this._valueRange=0}parse(t,e){return s(t)||("number"==typeof t||t instanceof Number)&&!isFinite(+t)?null:+t}handleTickRangeOptions(){const{beginAtZero:t}=this.options,{minDefined:e,maxDefined:i}=this.getUserBounds();let{min:s,max:n}=this;const o=t=>s=e?s:t,a=t=>n=i?n:t;if(t){const t=F(s),e=F(n);t<0&&e<0?a(0):t>0&&e>0&&o(0)}if(s===n){let e=0===n?1:Math.abs(.05*n);a(n+e),t||o(s-e)}this.min=s,this.max=n}getTickLimit(){const t=this.options.ticks;let e,{maxTicksLimit:i,stepSize:s}=t;return s?(e=Math.ceil(this.max/s)-Math.floor(this.min/s)+1,e>1e3&&(console.warn(`scales.${this.id}.ticks.stepSize: ${s} would result generating up to ${e} ticks. Limiting to 1000.`),e=1e3)):(e=this.computeTickLimit(),i=i||11),i&&(e=Math.min(i,e)),e}computeTickLimit(){return Number.POSITIVE_INFINITY}buildTicks(){const t=this.options,e=t.ticks;let i=this.getTickLimit();i=Math.max(2,i);const n=function(t,e){const i=[],{bounds:n,step:o,min:a,max:r,precision:l,count:h,maxTicks:c,maxDigits:d,includeBounds:u}=t,f=o||1,g=c-1,{min:p,max:m}=e,b=!s(a),x=!s(r),_=!s(h),y=(m-p)/(d+1);let v,M,w,k,S=B((m-p)/g/f)*f;if(S<1e-14&&!b&&!x)return[{value:p},{value:m}];k=Math.ceil(m/S)-Math.floor(p/S),k>g&&(S=B(k*S/g/f)*f),s(l)||(v=Math.pow(10,l),S=Math.ceil(S*v)/v),"ticks"===n?(M=Math.floor(p/S)*S,w=Math.ceil(m/S)*S):(M=p,w=m),b&&x&&o&&H((r-a)/o,S/1e3)?(k=Math.round(Math.min((r-a)/S,c)),S=(r-a)/k,M=a,w=r):_?(M=b?a:M,w=x?r:w,k=h-1,S=(w-M)/k):(k=(w-M)/S,k=V(k,Math.round(k),S/1e3)?Math.round(k):Math.ceil(k));const P=Math.max(U(S),U(M));v=Math.pow(10,s(l)?P:l),M=Math.round(M*v)/v,w=Math.round(w*v)/v;let D=0;for(b&&(u&&M!==a?(i.push({value:a}),M<a&&D++,V(Math.round((M+D*S)*v)/v,a,mo(a,y,t))&&D++):M<a&&D++);D<k;++D){const t=Math.round((M+D*S)*v)/v;if(x&&t>r)break;i.push({value:t})}return x&&u&&w!==r?i.length&&V(i[i.length-1].value,r,mo(r,y,t))?i[i.length-1].value=r:i.push({value:r}):x&&w!==r||i.push({value:w}),i}({maxTicks:i,bounds:t.bounds,min:t.min,max:t.max,precision:e.precision,step:e.stepSize,count:e.count,maxDigits:this._maxDigits(),horizontal:this.isHorizontal(),minRotation:e.minRotation||0,includeBounds:!1!==e.includeBounds},this._range||this);return"ticks"===t.bounds&&j(n,this,"value"),t.reverse?(n.reverse(),this.start=this.max,this.end=this.min):(this.start=this.min,this.end=this.max),n}configure(){const t=this.ticks;let e=this.min,i=this.max;if(super.configure(),this.options.offset&&t.length){const s=(i-e)/Math.max(t.length-1,1)/2;e-=s,i+=s}this._startValue=e,this._endValue=i,this._valueRange=i-e}getLabelForValue(t){return ne(t,this.chart.options.locale,this.options.ticks.format)}}class xo extends bo{static id="linear";static defaults={ticks:{callback:ae.formatters.numeric}};determineDataLimits(){const{min:t,max:e}=this.getMinMax(!0);this.min=a(t)?t:0,this.max=a(e)?e:1,this.handleTickRangeOptions()}computeTickLimit(){const t=this.isHorizontal(),e=t?this.width:this.height,i=$(this.options.ticks.minRotation),s=(t?Math.sin(i):Math.cos(i))||.001,n=this._resolveTickFontOptions(0);return Math.ceil(e/Math.min(40,n.lineHeight/s))}getPixelForValue(t){return null===t?NaN:this.getPixelForDecimal((t-this._startValue)/this._valueRange)}getValueForPixel(t){return this._startValue+this.getDecimalForPixel(t)*this._valueRange}}const _o=t=>Math.floor(z(t)),yo=(t,e)=>Math.pow(10,_o(t)+e);function vo(t){return 1===t/Math.pow(10,_o(t))}function Mo(t,e,i){const s=Math.pow(10,i),n=Math.floor(t/s);return Math.ceil(e/s)-n}function wo(t,{min:e,max:i}){e=r(t.min,e);const s=[],n=_o(e);let o=function(t,e){let i=_o(e-t);for(;Mo(t,e,i)>10;)i++;for(;Mo(t,e,i)<10;)i--;return Math.min(i,_o(t))}(e,i),a=o<0?Math.pow(10,Math.abs(o)):1;const l=Math.pow(10,o),h=n>o?Math.pow(10,n):0,c=Math.round((e-h)*a)/a,d=Math.floor((e-h)/l/10)*l*10;let u=Math.floor((c-d)/Math.pow(10,o)),f=r(t.min,Math.round((h+d+u*Math.pow(10,o))*a)/a);for(;f<i;)s.push({value:f,major:vo(f),significand:u}),u>=10?u=u<15?15:20:u++,u>=20&&(o++,u=2,a=o>=0?1:a),f=Math.round((h+d+u*Math.pow(10,o))*a)/a;const g=r(t.max,f);return s.push({value:g,major:vo(g),significand:u}),s}class ko extends Js{static id="logarithmic";static defaults={ticks:{callback:ae.formatters.logarithmic,major:{enabled:!0}}};constructor(t){super(t),this.start=void 0,this.end=void 0,this._startValue=void 0,this._valueRange=0}parse(t,e){const i=bo.prototype.parse.apply(this,[t,e]);if(0!==i)return a(i)&&i>0?i:null;this._zero=!0}determineDataLimits(){const{min:t,max:e}=this.getMinMax(!0);this.min=a(t)?Math.max(0,t):null,this.max=a(e)?Math.max(0,e):null,this.options.beginAtZero&&(this._zero=!0),this._zero&&this.min!==this._suggestedMin&&!a(this._userMin)&&(this.min=t===yo(this.min,0)?yo(this.min,-1):yo(this.min,0)),this.handleTickRangeOptions()}handleTickRangeOptions(){const{minDefined:t,maxDefined:e}=this.getUserBounds();let i=this.min,s=this.max;const n=e=>i=t?i:e,o=t=>s=e?s:t;i===s&&(i<=0?(n(1),o(10)):(n(yo(i,-1)),o(yo(s,1)))),i<=0&&n(yo(s,-1)),s<=0&&o(yo(i,1)),this.min=i,this.max=s}buildTicks(){const t=this.options,e=wo({min:this._userMin,max:this._userMax},this);return"ticks"===t.bounds&&j(e,this,"value"),t.reverse?(e.reverse(),this.start=this.max,this.end=this.min):(this.start=this.min,this.end=this.max),e}getLabelForValue(t){return void 0===t?"0":ne(t,this.chart.options.locale,this.options.ticks.format)}configure(){const t=this.min;super.configure(),this._startValue=z(t),this._valueRange=z(this.max)-z(t)}getPixelForValue(t){return void 0!==t&&0!==t||(t=this.min),null===t||isNaN(t)?NaN:this.getPixelForDecimal(t===this.min?0:(z(t)-this._startValue)/this._valueRange)}getValueForPixel(t){const e=this.getDecimalForPixel(t);return Math.pow(10,this._startValue+e*this._valueRange)}}function So(t){const e=t.ticks;if(e.display&&t.display){const t=ki(e.backdropPadding);return l(e.font&&e.font.size,ue.font.size)+t.height}return 0}function Po(t,e,i,s,n){return t===s||t===n?{start:e-i/2,end:e+i/2}:t<s||t>n?{start:e-i,end:e}:{start:e,end:e+i}}function Do(t){const e={l:t.left+t._padding.left,r:t.right-t._padding.right,t:t.top+t._padding.top,b:t.bottom-t._padding.bottom},i=Object.assign({},e),s=[],o=[],a=t._pointLabels.length,r=t.options.pointLabels,l=r.centerPointLabels?C/a:0;for(let u=0;u<a;u++){const a=r.setContext(t.getPointLabelContext(u));o[u]=a.padding;const f=t.getPointPosition(u,t.drawingArea+o[u],l),g=Si(a.font),p=(h=t.ctx,c=g,d=n(d=t._pointLabels[u])?d:[d],{w:Oe(h,c.string,d),h:d.length*c.lineHeight});s[u]=p;const m=G(t.getIndexAngle(u)+l),b=Math.round(Y(m));Co(i,e,m,Po(b,f.x,p.w,0,180),Po(b,f.y,p.h,90,270))}var h,c,d;t.setCenterPoint(e.l-i.l,i.r-e.r,e.t-i.t,i.b-e.b),t._pointLabelItems=function(t,e,i){const s=[],n=t._pointLabels.length,o=t.options,{centerPointLabels:a,display:r}=o.pointLabels,l={extra:So(o)/2,additionalAngle:a?C/n:0};let h;for(let o=0;o<n;o++){l.padding=i[o],l.size=e[o];const n=Oo(t,o,l);s.push(n),"auto"===r&&(n.visible=Ao(n,h),n.visible&&(h=n))}return s}(t,s,o)}function Co(t,e,i,s,n){const o=Math.abs(Math.sin(i)),a=Math.abs(Math.cos(i));let r=0,l=0;s.start<e.l?(r=(e.l-s.start)/o,t.l=Math.min(t.l,e.l-r)):s.end>e.r&&(r=(s.end-e.r)/o,t.r=Math.max(t.r,e.r+r)),n.start<e.t?(l=(e.t-n.start)/a,t.t=Math.min(t.t,e.t-l)):n.end>e.b&&(l=(n.end-e.b)/a,t.b=Math.max(t.b,e.b+l))}function Oo(t,e,i){const s=t.drawingArea,{extra:n,additionalAngle:o,padding:a,size:r}=i,l=t.getPointPosition(e,s+n+a,o),h=Math.round(Y(G(l.angle+E))),c=function(t,e,i){90===i||270===i?t-=e/2:(i>270||i<90)&&(t-=e);return t}(l.y,r.h,h),d=function(t){if(0===t||180===t)return"center";if(t<180)return"left";return"right"}(h),u=function(t,e,i){"right"===i?t-=e:"center"===i&&(t-=e/2);return t}(l.x,r.w,d);return{visible:!0,x:l.x,y:c,textAlign:d,left:u,top:c,right:u+r.w,bottom:c+r.h}}function Ao(t,e){if(!e)return!0;const{left:i,top:s,right:n,bottom:o}=t;return!(Re({x:i,y:s},e)||Re({x:i,y:o},e)||Re({x:n,y:s},e)||Re({x:n,y:o},e))}function To(t,e,i){const{left:n,top:o,right:a,bottom:r}=i,{backdropColor:l}=e;if(!s(l)){const i=wi(e.borderRadius),s=ki(e.backdropPadding);t.fillStyle=l;const h=n-s.left,c=o-s.top,d=a-n+s.width,u=r-o+s.height;Object.values(i).some((t=>0!==t))?(t.beginPath(),He(t,{x:h,y:c,w:d,h:u,radius:i}),t.fill()):t.fillRect(h,c,d,u)}}function Lo(t,e,i,s){const{ctx:n}=t;if(i)n.arc(t.xCenter,t.yCenter,e,0,O);else{let i=t.getPointPosition(0,e);n.moveTo(i.x,i.y);for(let o=1;o<s;o++)i=t.getPointPosition(o,e),n.lineTo(i.x,i.y)}}class Eo extends bo{static id="radialLinear";static defaults={display:!0,animate:!0,position:"chartArea",angleLines:{display:!0,lineWidth:1,borderDash:[],borderDashOffset:0},grid:{circular:!1},startAngle:0,ticks:{showLabelBackdrop:!0,callback:ae.formatters.numeric},pointLabels:{backdropColor:void 0,backdropPadding:2,display:!0,font:{size:10},callback:t=>t,padding:5,centerPointLabels:!1}};static defaultRoutes={"angleLines.color":"borderColor","pointLabels.color":"color","ticks.color":"color"};static descriptors={angleLines:{_fallback:"grid"}};constructor(t){super(t),this.xCenter=void 0,this.yCenter=void 0,this.drawingArea=void 0,this._pointLabels=[],this._pointLabelItems=[]}setDimensions(){const t=this._padding=ki(So(this.options)/2),e=this.width=this.maxWidth-t.width,i=this.height=this.maxHeight-t.height;this.xCenter=Math.floor(this.left+e/2+t.left),this.yCenter=Math.floor(this.top+i/2+t.top),this.drawingArea=Math.floor(Math.min(e,i)/2)}determineDataLimits(){const{min:t,max:e}=this.getMinMax(!1);this.min=a(t)&&!isNaN(t)?t:0,this.max=a(e)&&!isNaN(e)?e:0,this.handleTickRangeOptions()}computeTickLimit(){return Math.ceil(this.drawingArea/So(this.options))}generateTickLabels(t){bo.prototype.generateTickLabels.call(this,t),this._pointLabels=this.getLabels().map(((t,e)=>{const i=d(this.options.pointLabels.callback,[t,e],this);return i||0===i?i:""})).filter(((t,e)=>this.chart.getDataVisibility(e)))}fit(){const t=this.options;t.display&&t.pointLabels.display?Do(this):this.setCenterPoint(0,0,0,0)}setCenterPoint(t,e,i,s){this.xCenter+=Math.floor((t-e)/2),this.yCenter+=Math.floor((i-s)/2),this.drawingArea-=Math.min(this.drawingArea/2,Math.max(t,e,i,s))}getIndexAngle(t){return G(t*(O/(this._pointLabels.length||1))+$(this.options.startAngle||0))}getDistanceFromCenterForValue(t){if(s(t))return NaN;const e=this.drawingArea/(this.max-this.min);return this.options.reverse?(this.max-t)*e:(t-this.min)*e}getValueForDistanceFromCenter(t){if(s(t))return NaN;const e=t/(this.drawingArea/(this.max-this.min));return this.options.reverse?this.max-e:this.min+e}getPointLabelContext(t){const e=this._pointLabels||[];if(t>=0&&t<e.length){const i=e[t];return function(t,e,i){return Ci(t,{label:i,index:e,type:"pointLabel"})}(this.getContext(),t,i)}}getPointPosition(t,e,i=0){const s=this.getIndexAngle(t)-E+i;return{x:Math.cos(s)*e+this.xCenter,y:Math.sin(s)*e+this.yCenter,angle:s}}getPointPositionForValue(t,e){return this.getPointPosition(t,this.getDistanceFromCenterForValue(e))}getBasePosition(t){return this.getPointPositionForValue(t||0,this.getBaseValue())}getPointLabelPosition(t){const{left:e,top:i,right:s,bottom:n}=this._pointLabelItems[t];return{left:e,top:i,right:s,bottom:n}}drawBackground(){const{backgroundColor:t,grid:{circular:e}}=this.options;if(t){const i=this.ctx;i.save(),i.beginPath(),Lo(this,this.getDistanceFromCenterForValue(this._endValue),e,this._pointLabels.length),i.closePath(),i.fillStyle=t,i.fill(),i.restore()}}drawGrid(){const t=this.ctx,e=this.options,{angleLines:i,grid:s,border:n}=e,o=this._pointLabels.length;let a,r,l;if(e.pointLabels.display&&function(t,e){const{ctx:i,options:{pointLabels:s}}=t;for(let n=e-1;n>=0;n--){const e=t._pointLabelItems[n];if(!e.visible)continue;const o=s.setContext(t.getPointLabelContext(n));To(i,o,e);const a=Si(o.font),{x:r,y:l,textAlign:h}=e;Ne(i,t._pointLabels[n],r,l+a.lineHeight/2,a,{color:o.color,textAlign:h,textBaseline:"middle"})}}(this,o),s.display&&this.ticks.forEach(((t,e)=>{if(0!==e){r=this.getDistanceFromCenterForValue(t.value);const i=this.getContext(e),a=s.setContext(i),l=n.setContext(i);!function(t,e,i,s,n){const o=t.ctx,a=e.circular,{color:r,lineWidth:l}=e;!a&&!s||!r||!l||i<0||(o.save(),o.strokeStyle=r,o.lineWidth=l,o.setLineDash(n.dash),o.lineDashOffset=n.dashOffset,o.beginPath(),Lo(t,i,a,s),o.closePath(),o.stroke(),o.restore())}(this,a,r,o,l)}})),i.display){for(t.save(),a=o-1;a>=0;a--){const s=i.setContext(this.getPointLabelContext(a)),{color:n,lineWidth:o}=s;o&&n&&(t.lineWidth=o,t.strokeStyle=n,t.setLineDash(s.borderDash),t.lineDashOffset=s.borderDashOffset,r=this.getDistanceFromCenterForValue(e.ticks.reverse?this.min:this.max),l=this.getPointPosition(a,r),t.beginPath(),t.moveTo(this.xCenter,this.yCenter),t.lineTo(l.x,l.y),t.stroke())}t.restore()}}drawBorder(){}drawLabels(){const t=this.ctx,e=this.options,i=e.ticks;if(!i.display)return;const s=this.getIndexAngle(0);let n,o;t.save(),t.translate(this.xCenter,this.yCenter),t.rotate(s),t.textAlign="center",t.textBaseline="middle",this.ticks.forEach(((s,a)=>{if(0===a&&!e.reverse)return;const r=i.setContext(this.getContext(a)),l=Si(r.font);if(n=this.getDistanceFromCenterForValue(this.ticks[a].value),r.showLabelBackdrop){t.font=l.string,o=t.measureText(s.label).width,t.fillStyle=r.backdropColor;const e=ki(r.backdropPadding);t.fillRect(-o/2-e.left,-n-l.size/2-e.top,o+e.width,l.size+e.height)}Ne(t,s.label,0,-n,l,{color:r.color,strokeColor:r.textStrokeColor,strokeWidth:r.textStrokeWidth})})),t.restore()}drawTitle(){}}const Ro={millisecond:{common:!0,size:1,steps:1e3},second:{common:!0,size:1e3,steps:60},minute:{common:!0,size:6e4,steps:60},hour:{common:!0,size:36e5,steps:24},day:{common:!0,size:864e5,steps:30},week:{common:!1,size:6048e5,steps:4},month:{common:!0,size:2628e6,steps:12},quarter:{common:!1,size:7884e6,steps:4},year:{common:!0,size:3154e7}},Io=Object.keys(Ro);function zo(t,e){return t-e}function Fo(t,e){if(s(e))return null;const i=t._adapter,{parser:n,round:o,isoWeekday:r}=t._parseOpts;let l=e;return"function"==typeof n&&(l=n(l)),a(l)||(l="string"==typeof n?i.parse(l,n):i.parse(l)),null===l?null:(o&&(l="week"!==o||!N(r)&&!0!==r?i.startOf(l,o):i.startOf(l,"isoWeek",r)),+l)}function Vo(t,e,i,s){const n=Io.length;for(let o=Io.indexOf(t);o<n-1;++o){const t=Ro[Io[o]],n=t.steps?t.steps:Number.MAX_SAFE_INTEGER;if(t.common&&Math.ceil((i-e)/(n*t.size))<=s)return Io[o]}return Io[n-1]}function Bo(t,e,i){if(i){if(i.length){const{lo:s,hi:n}=et(i,e);t[i[s]>=e?i[s]:i[n]]=!0}}else t[e]=!0}function Wo(t,e,i){const s=[],n={},o=e.length;let a,r;for(a=0;a<o;++a)r=e[a],n[r]=a,s.push({value:r,major:!1});return 0!==o&&i?function(t,e,i,s){const n=t._adapter,o=+n.startOf(e[0].value,s),a=e[e.length-1].value;let r,l;for(r=o;r<=a;r=+n.add(r,1,s))l=i[r],l>=0&&(e[l].major=!0);return e}(t,s,n,i):s}class No extends Js{static id="time";static defaults={bounds:"data",adapters:{},time:{parser:!1,unit:!1,round:!1,isoWeekday:!1,minUnit:"millisecond",displayFormats:{}},ticks:{source:"auto",callback:!1,major:{enabled:!1}}};constructor(t){super(t),this._cache={data:[],labels:[],all:[]},this._unit="day",this._majorUnit=void 0,this._offsets={},this._normalized=!1,this._parseOpts=void 0}init(t,e={}){const i=t.time||(t.time={}),s=this._adapter=new Rn._date(t.adapters.date);s.init(e),x(i.displayFormats,s.formats()),this._parseOpts={parser:i.parser,round:i.round,isoWeekday:i.isoWeekday},super.init(t),this._normalized=e.normalized}parse(t,e){return void 0===t?null:Fo(this,t)}beforeLayout(){super.beforeLayout(),this._cache={data:[],labels:[],all:[]}}determineDataLimits(){const t=this.options,e=this._adapter,i=t.time.unit||"day";let{min:s,max:n,minDefined:o,maxDefined:r}=this.getUserBounds();function l(t){o||isNaN(t.min)||(s=Math.min(s,t.min)),r||isNaN(t.max)||(n=Math.max(n,t.max))}o&&r||(l(this._getLabelBounds()),"ticks"===t.bounds&&"labels"===t.ticks.source||l(this.getMinMax(!1))),s=a(s)&&!isNaN(s)?s:+e.startOf(Date.now(),i),n=a(n)&&!isNaN(n)?n:+e.endOf(Date.now(),i)+1,this.min=Math.min(s,n-1),this.max=Math.max(s+1,n)}_getLabelBounds(){const t=this.getLabelTimestamps();let e=Number.POSITIVE_INFINITY,i=Number.NEGATIVE_INFINITY;return t.length&&(e=t[0],i=t[t.length-1]),{min:e,max:i}}buildTicks(){const t=this.options,e=t.time,i=t.ticks,s="labels"===i.source?this.getLabelTimestamps():this._generate();"ticks"===t.bounds&&s.length&&(this.min=this._userMin||s[0],this.max=this._userMax||s[s.length-1]);const n=this.min,o=nt(s,n,this.max);return this._unit=e.unit||(i.autoSkip?Vo(e.minUnit,this.min,this.max,this._getLabelCapacity(n)):function(t,e,i,s,n){for(let o=Io.length-1;o>=Io.indexOf(i);o--){const i=Io[o];if(Ro[i].common&&t._adapter.diff(n,s,i)>=e-1)return i}return Io[i?Io.indexOf(i):0]}(this,o.length,e.minUnit,this.min,this.max)),this._majorUnit=i.major.enabled&&"year"!==this._unit?function(t){for(let e=Io.indexOf(t)+1,i=Io.length;e<i;++e)if(Ro[Io[e]].common)return Io[e]}(this._unit):void 0,this.initOffsets(s),t.reverse&&o.reverse(),Wo(this,o,this._majorUnit)}afterAutoSkip(){this.options.offsetAfterAutoskip&&this.initOffsets(this.ticks.map((t=>+t.value)))}initOffsets(t=[]){let e,i,s=0,n=0;this.options.offset&&t.length&&(e=this.getDecimalForValue(t[0]),s=1===t.length?1-e:(this.getDecimalForValue(t[1])-e)/2,i=this.getDecimalForValue(t[t.length-1]),n=1===t.length?i:(i-this.getDecimalForValue(t[t.length-2]))/2);const o=t.length<3?.5:.25;s=J(s,0,o),n=J(n,0,o),this._offsets={start:s,end:n,factor:1/(s+1+n)}}_generate(){const t=this._adapter,e=this.min,i=this.max,s=this.options,n=s.time,o=n.unit||Vo(n.minUnit,e,i,this._getLabelCapacity(e)),a=l(s.ticks.stepSize,1),r="week"===o&&n.isoWeekday,h=N(r)||!0===r,c={};let d,u,f=e;if(h&&(f=+t.startOf(f,"isoWeek",r)),f=+t.startOf(f,h?"day":o),t.diff(i,e,o)>1e5*a)throw new Error(e+" and "+i+" are too far apart with stepSize of "+a+" "+o);const g="data"===s.ticks.source&&this.getDataTimestamps();for(d=f,u=0;d<i;d=+t.add(d,a,o),u++)Bo(c,d,g);return d!==i&&"ticks"!==s.bounds&&1!==u||Bo(c,d,g),Object.keys(c).sort(zo).map((t=>+t))}getLabelForValue(t){const e=this._adapter,i=this.options.time;return i.tooltipFormat?e.format(t,i.tooltipFormat):e.format(t,i.displayFormats.datetime)}format(t,e){const i=this.options.time.displayFormats,s=this._unit,n=e||i[s];return this._adapter.format(t,n)}_tickFormatFunction(t,e,i,s){const n=this.options,o=n.ticks.callback;if(o)return d(o,[t,e,i],this);const a=n.time.displayFormats,r=this._unit,l=this._majorUnit,h=r&&a[r],c=l&&a[l],u=i[e],f=l&&c&&u&&u.major;return this._adapter.format(t,s||(f?c:h))}generateTickLabels(t){let e,i,s;for(e=0,i=t.length;e<i;++e)s=t[e],s.label=this._tickFormatFunction(s.value,e,t)}getDecimalForValue(t){return null===t?NaN:(t-this.min)/(this.max-this.min)}getPixelForValue(t){const e=this._offsets,i=this.getDecimalForValue(t);return this.getPixelForDecimal((e.start+i)*e.factor)}getValueForPixel(t){const e=this._offsets,i=this.getDecimalForPixel(t)/e.factor-e.end;return this.min+i*(this.max-this.min)}_getLabelSize(t){const e=this.options.ticks,i=this.ctx.measureText(t).width,s=$(this.isHorizontal()?e.maxRotation:e.minRotation),n=Math.cos(s),o=Math.sin(s),a=this._resolveTickFontOptions(0).size;return{w:i*n+a*o,h:i*o+a*n}}_getLabelCapacity(t){const e=this.options.time,i=e.displayFormats,s=i[e.unit]||i.millisecond,n=this._tickFormatFunction(t,0,Wo(this,[t],this._majorUnit),s),o=this._getLabelSize(n),a=Math.floor(this.isHorizontal()?this.width/o.w:this.height/o.h)-1;return a>0?a:1}getDataTimestamps(){let t,e,i=this._cache.data||[];if(i.length)return i;const s=this.getMatchingVisibleMetas();if(this._normalized&&s.length)return this._cache.data=s[0].controller.getAllParsedValues(this);for(t=0,e=s.length;t<e;++t)i=i.concat(s[t].controller.getAllParsedValues(this));return this._cache.data=this.normalize(i)}getLabelTimestamps(){const t=this._cache.labels||[];let e,i;if(t.length)return t;const s=this.getLabels();for(e=0,i=s.length;e<i;++e)t.push(Fo(this,s[e]));return this._cache.labels=this._normalized?t:this.normalize(t)}normalize(t){return lt(t.sort(zo))}}function Ho(t,e,i){let s,n,o,a,r=0,l=t.length-1;i?(e>=t[r].pos&&e<=t[l].pos&&({lo:r,hi:l}=it(t,"pos",e)),({pos:s,time:o}=t[r]),({pos:n,time:a}=t[l])):(e>=t[r].time&&e<=t[l].time&&({lo:r,hi:l}=it(t,"time",e)),({time:s,pos:o}=t[r]),({time:n,pos:a}=t[l]));const h=n-s;return h?o+(a-o)*(e-s)/h:o}var jo=Object.freeze({__proto__:null,CategoryScale:class extends Js{static id="category";static defaults={ticks:{callback:po}};constructor(t){super(t),this._startValue=void 0,this._valueRange=0,this._addedLabels=[]}init(t){const e=this._addedLabels;if(e.length){const t=this.getLabels();for(const{index:i,label:s}of e)t[i]===s&&t.splice(i,1);this._addedLabels=[]}super.init(t)}parse(t,e){if(s(t))return null;const i=this.getLabels();return((t,e)=>null===t?null:J(Math.round(t),0,e))(e=isFinite(e)&&i[e]===t?e:go(i,t,l(e,t),this._addedLabels),i.length-1)}determineDataLimits(){const{minDefined:t,maxDefined:e}=this.getUserBounds();let{min:i,max:s}=this.getMinMax(!0);"ticks"===this.options.bounds&&(t||(i=0),e||(s=this.getLabels().length-1)),this.min=i,this.max=s}buildTicks(){const t=this.min,e=this.max,i=this.options.offset,s=[];let n=this.getLabels();n=0===t&&e===n.length-1?n:n.slice(t,e+1),this._valueRange=Math.max(n.length-(i?0:1),1),this._startValue=this.min-(i?.5:0);for(let i=t;i<=e;i++)s.push({value:i});return s}getLabelForValue(t){return po.call(this,t)}configure(){super.configure(),this.isHorizontal()||(this._reversePixels=!this._reversePixels)}getPixelForValue(t){return"number"!=typeof t&&(t=this.parse(t)),null===t?NaN:this.getPixelForDecimal((t-this._startValue)/this._valueRange)}getPixelForTick(t){const e=this.ticks;return t<0||t>e.length-1?null:this.getPixelForValue(e[t].value)}getValueForPixel(t){return Math.round(this._startValue+this.getDecimalForPixel(t)*this._valueRange)}getBasePixel(){return this.bottom}},LinearScale:xo,LogarithmicScale:ko,RadialLinearScale:Eo,TimeScale:No,TimeSeriesScale:class extends No{static id="timeseries";static defaults=No.defaults;constructor(t){super(t),this._table=[],this._minPos=void 0,this._tableRange=void 0}initOffsets(){const t=this._getTimestampsForTable(),e=this._table=this.buildLookupTable(t);this._minPos=Ho(e,this.min),this._tableRange=Ho(e,this.max)-this._minPos,super.initOffsets(t)}buildLookupTable(t){const{min:e,max:i}=this,s=[],n=[];let o,a,r,l,h;for(o=0,a=t.length;o<a;++o)l=t[o],l>=e&&l<=i&&s.push(l);if(s.length<2)return[{time:e,pos:0},{time:i,pos:1}];for(o=0,a=s.length;o<a;++o)h=s[o+1],r=s[o-1],l=s[o],Math.round((h+r)/2)!==l&&n.push({time:l,pos:o/(a-1)});return n}_generate(){const t=this.min,e=this.max;let i=super.getDataTimestamps();return i.includes(t)&&i.length||i.splice(0,0,t),i.includes(e)&&1!==i.length||i.push(e),i.sort(((t,e)=>t-e))}_getTimestampsForTable(){let t=this._cache.all||[];if(t.length)return t;const e=this.getDataTimestamps(),i=this.getLabelTimestamps();return t=e.length&&i.length?this.normalize(e.concat(i)):e.length?e:i,t=this._cache.all=t,t}getDecimalForValue(t){return(Ho(this._table,t)-this._minPos)/this._tableRange}getValueForPixel(t){const e=this._offsets,i=this.getDecimalForPixel(t)/e.factor-e.end;return Ho(this._table,i*this._tableRange+this._minPos,!0)}}});const $o=["rgb(54, 162, 235)","rgb(255, 99, 132)","rgb(255, 159, 64)","rgb(255, 205, 86)","rgb(75, 192, 192)","rgb(153, 102, 255)","rgb(201, 203, 207)"],Yo=$o.map((t=>t.replace("rgb(","rgba(").replace(")",", 0.5)")));function Uo(t){return $o[t%$o.length]}function Xo(t){return Yo[t%Yo.length]}function qo(t){let e=0;return(i,s)=>{const n=t.getDatasetMeta(s).controller;n instanceof jn?e=function(t,e){return t.backgroundColor=t.data.map((()=>Uo(e++))),e}(i,e):n instanceof $n?e=function(t,e){return t.backgroundColor=t.data.map((()=>Xo(e++))),e}(i,e):n&&(e=function(t,e){return t.borderColor=Uo(e),t.backgroundColor=Xo(e),++e}(i,e))}}function Ko(t){let e;for(e in t)if(t[e].borderColor||t[e].backgroundColor)return!0;return!1}var Go={id:"colors",defaults:{enabled:!0,forceOverride:!1},beforeLayout(t,e,i){if(!i.enabled)return;const{data:{datasets:s},options:n}=t.config,{elements:o}=n;if(!i.forceOverride&&(Ko(s)||(a=n)&&(a.borderColor||a.backgroundColor)||o&&Ko(o)))return;var a;const r=qo(t);s.forEach(r)}};function Zo(t){if(t._decimated){const e=t._data;delete t._decimated,delete t._data,Object.defineProperty(t,"data",{configurable:!0,enumerable:!0,writable:!0,value:e})}}function Jo(t){t.data.datasets.forEach((t=>{Zo(t)}))}var Qo={id:"decimation",defaults:{algorithm:"min-max",enabled:!1},beforeElementsUpdate:(t,e,i)=>{if(!i.enabled)return void Jo(t);const n=t.width;t.data.datasets.forEach(((e,o)=>{const{_data:a,indexAxis:r}=e,l=t.getDatasetMeta(o),h=a||e.data;if("y"===Pi([r,t.options.indexAxis]))return;if(!l.controller.supportsDecimation)return;const c=t.scales[l.xAxisID];if("linear"!==c.type&&"time"!==c.type)return;if(t.options.parsing)return;let{start:d,count:u}=function(t,e){const i=e.length;let s,n=0;const{iScale:o}=t,{min:a,max:r,minDefined:l,maxDefined:h}=o.getUserBounds();return l&&(n=J(it(e,o.axis,a).lo,0,i-1)),s=h?J(it(e,o.axis,r).hi+1,n,i)-n:i-n,{start:n,count:s}}(l,h);if(u<=(i.threshold||4*n))return void Zo(e);let f;switch(s(a)&&(e._data=h,delete e.data,Object.defineProperty(e,"data",{configurable:!0,enumerable:!0,get:function(){return this._decimated},set:function(t){this._data=t}})),i.algorithm){case"lttb":f=function(t,e,i,s,n){const o=n.samples||s;if(o>=i)return t.slice(e,e+i);const a=[],r=(i-2)/(o-2);let l=0;const h=e+i-1;let c,d,u,f,g,p=e;for(a[l++]=t[p],c=0;c<o-2;c++){let s,n=0,o=0;const h=Math.floor((c+1)*r)+1+e,m=Math.min(Math.floor((c+2)*r)+1,i)+e,b=m-h;for(s=h;s<m;s++)n+=t[s].x,o+=t[s].y;n/=b,o/=b;const x=Math.floor(c*r)+1+e,_=Math.min(Math.floor((c+1)*r)+1,i)+e,{x:y,y:v}=t[p];for(u=f=-1,s=x;s<_;s++)f=.5*Math.abs((y-n)*(t[s].y-v)-(y-t[s].x)*(o-v)),f>u&&(u=f,d=t[s],g=s);a[l++]=d,p=g}return a[l++]=t[h],a}(h,d,u,n,i);break;case"min-max":f=function(t,e,i,n){let o,a,r,l,h,c,d,u,f,g,p=0,m=0;const b=[],x=e+i-1,_=t[e].x,y=t[x].x-_;for(o=e;o<e+i;++o){a=t[o],r=(a.x-_)/y*n,l=a.y;const e=0|r;if(e===h)l<f?(f=l,c=o):l>g&&(g=l,d=o),p=(m*p+a.x)/++m;else{const i=o-1;if(!s(c)&&!s(d)){const e=Math.min(c,d),s=Math.max(c,d);e!==u&&e!==i&&b.push({...t[e],x:p}),s!==u&&s!==i&&b.push({...t[s],x:p})}o>0&&i!==u&&b.push(t[i]),b.push(a),h=e,m=0,f=g=l,c=d=u=o}}return b}(h,d,u,n);break;default:throw new Error(`Unsupported decimation algorithm '${i.algorithm}'`)}e._decimated=f}))},destroy(t){Jo(t)}};function ta(t,e,i,s){if(s)return;let n=e[t],o=i[t];return"angle"===t&&(n=G(n),o=G(o)),{property:t,start:n,end:o}}function ea(t,e,i){for(;e>t;e--){const t=i[e];if(!isNaN(t.x)&&!isNaN(t.y))break}return e}function ia(t,e,i,s){return t&&e?s(t[i],e[i]):t?t[i]:e?e[i]:0}function sa(t,e){let i=[],s=!1;return n(t)?(s=!0,i=t):i=function(t,e){const{x:i=null,y:s=null}=t||{},n=e.points,o=[];return e.segments.forEach((({start:t,end:e})=>{e=ea(t,e,n);const a=n[t],r=n[e];null!==s?(o.push({x:a.x,y:s}),o.push({x:r.x,y:s})):null!==i&&(o.push({x:i,y:a.y}),o.push({x:i,y:r.y}))})),o}(t,e),i.length?new no({points:i,options:{tension:0},_loop:s,_fullLoop:s}):null}function na(t){return t&&!1!==t.fill}function oa(t,e,i){let s=t[e].fill;const n=[e];let o;if(!i)return s;for(;!1!==s&&-1===n.indexOf(s);){if(!a(s))return s;if(o=t[s],!o)return!1;if(o.visible)return s;n.push(s),s=o.fill}return!1}function aa(t,e,i){const s=function(t){const e=t.options,i=e.fill;let s=l(i&&i.target,i);void 0===s&&(s=!!e.backgroundColor);if(!1===s||null===s)return!1;if(!0===s)return"origin";return s}(t);if(o(s))return!isNaN(s.value)&&s;let n=parseFloat(s);return a(n)&&Math.floor(n)===n?function(t,e,i,s){"-"!==t&&"+"!==t||(i=e+i);if(i===e||i<0||i>=s)return!1;return i}(s[0],e,n,i):["origin","start","end","stack","shape"].indexOf(s)>=0&&s}function ra(t,e,i){const s=[];for(let n=0;n<i.length;n++){const o=i[n],{first:a,last:r,point:l}=la(o,e,"x");if(!(!l||a&&r))if(a)s.unshift(l);else if(t.push(l),!r)break}t.push(...s)}function la(t,e,i){const s=t.interpolate(e,i);if(!s)return{};const n=s[i],o=t.segments,a=t.points;let r=!1,l=!1;for(let t=0;t<o.length;t++){const e=o[t],s=a[e.start][i],h=a[e.end][i];if(tt(n,s,h)){r=n===s,l=n===h;break}}return{first:r,last:l,point:s}}class ha{constructor(t){this.x=t.x,this.y=t.y,this.radius=t.radius}pathSegment(t,e,i){const{x:s,y:n,radius:o}=this;return e=e||{start:0,end:O},t.arc(s,n,o,e.end,e.start,!0),!i.bounds}interpolate(t){const{x:e,y:i,radius:s}=this,n=t.angle;return{x:e+Math.cos(n)*s,y:i+Math.sin(n)*s,angle:n}}}function ca(t){const{chart:e,fill:i,line:s}=t;if(a(i))return function(t,e){const i=t.getDatasetMeta(e),s=i&&t.isDatasetVisible(e);return s?i.dataset:null}(e,i);if("stack"===i)return function(t){const{scale:e,index:i,line:s}=t,n=[],o=s.segments,a=s.points,r=function(t,e){const i=[],s=t.getMatchingVisibleMetas("line");for(let t=0;t<s.length;t++){const n=s[t];if(n.index===e)break;n.hidden||i.unshift(n.dataset)}return i}(e,i);r.push(sa({x:null,y:e.bottom},s));for(let t=0;t<o.length;t++){const e=o[t];for(let t=e.start;t<=e.end;t++)ra(n,a[t],r)}return new no({points:n,options:{}})}(t);if("shape"===i)return!0;const n=function(t){const e=t.scale||{};if(e.getPointPositionForValue)return function(t){const{scale:e,fill:i}=t,s=e.options,n=e.getLabels().length,a=s.reverse?e.max:e.min,r=function(t,e,i){let s;return s="start"===t?i:"end"===t?e.options.reverse?e.min:e.max:o(t)?t.value:e.getBaseValue(),s}(i,e,a),l=[];if(s.grid.circular){const t=e.getPointPositionForValue(0,a);return new ha({x:t.x,y:t.y,radius:e.getDistanceFromCenterForValue(r)})}for(let t=0;t<n;++t)l.push(e.getPointPositionForValue(t,r));return l}(t);return function(t){const{scale:e={},fill:i}=t,s=function(t,e){let i=null;return"start"===t?i=e.bottom:"end"===t?i=e.top:o(t)?i=e.getPixelForValue(t.value):e.getBasePixel&&(i=e.getBasePixel()),i}(i,e);if(a(s)){const t=e.isHorizontal();return{x:t?s:null,y:t?null:s}}return null}(t)}(t);return n instanceof ha?n:sa(n,s)}function da(t,e,i){const s=ca(e),{line:n,scale:o,axis:a}=e,r=n.options,l=r.fill,h=r.backgroundColor,{above:c=h,below:d=h}=l||{};s&&n.points.length&&(Ie(t,i),function(t,e){const{line:i,target:s,above:n,below:o,area:a,scale:r}=e,l=i._loop?"angle":e.axis;t.save(),"x"===l&&o!==n&&(ua(t,s,a.top),fa(t,{line:i,target:s,color:n,scale:r,property:l}),t.restore(),t.save(),ua(t,s,a.bottom));fa(t,{line:i,target:s,color:o,scale:r,property:l}),t.restore()}(t,{line:n,target:s,above:c,below:d,area:i,scale:o,axis:a}),ze(t))}function ua(t,e,i){const{segments:s,points:n}=e;let o=!0,a=!1;t.beginPath();for(const r of s){const{start:s,end:l}=r,h=n[s],c=n[ea(s,l,n)];o?(t.moveTo(h.x,h.y),o=!1):(t.lineTo(h.x,i),t.lineTo(h.x,h.y)),a=!!e.pathSegment(t,r,{move:a}),a?t.closePath():t.lineTo(c.x,i)}t.lineTo(e.first().x,i),t.closePath(),t.clip()}function fa(t,e){const{line:i,target:s,property:n,color:o,scale:a}=e,r=function(t,e,i){const s=t.segments,n=t.points,o=e.points,a=[];for(const t of s){let{start:s,end:r}=t;r=ea(s,r,n);const l=ta(i,n[s],n[r],t.loop);if(!e.segments){a.push({source:t,target:l,start:n[s],end:n[r]});continue}const h=Ii(e,l);for(const e of h){const s=ta(i,o[e.start],o[e.end],e.loop),r=Ri(t,n,s);for(const t of r)a.push({source:t,target:e,start:{[i]:ia(l,s,"start",Math.max)},end:{[i]:ia(l,s,"end",Math.min)}})}}return a}(i,s,n);for(const{source:e,target:l,start:h,end:c}of r){const{style:{backgroundColor:r=o}={}}=e,d=!0!==s;t.save(),t.fillStyle=r,ga(t,a,d&&ta(n,h,c)),t.beginPath();const u=!!i.pathSegment(t,e);let f;if(d){u?t.closePath():pa(t,s,c,n);const e=!!s.pathSegment(t,l,{move:u,reverse:!0});f=u&&e,f||pa(t,s,h,n)}t.closePath(),t.fill(f?"evenodd":"nonzero"),t.restore()}}function ga(t,e,i){const{top:s,bottom:n}=e.chart.chartArea,{property:o,start:a,end:r}=i||{};"x"===o&&(t.beginPath(),t.rect(a,s,r-a,n-s),t.clip())}function pa(t,e,i,s){const n=e.interpolate(i,s);n&&t.lineTo(n.x,n.y)}var ma={id:"filler",afterDatasetsUpdate(t,e,i){const s=(t.data.datasets||[]).length,n=[];let o,a,r,l;for(a=0;a<s;++a)o=t.getDatasetMeta(a),r=o.dataset,l=null,r&&r.options&&r instanceof no&&(l={visible:t.isDatasetVisible(a),index:a,fill:aa(r,a,s),chart:t,axis:o.controller.options.indexAxis,scale:o.vScale,line:r}),o.$filler=l,n.push(l);for(a=0;a<s;++a)l=n[a],l&&!1!==l.fill&&(l.fill=oa(n,a,i.propagate))},beforeDraw(t,e,i){const s="beforeDraw"===i.drawTime,n=t.getSortedVisibleDatasetMetas(),o=t.chartArea;for(let e=n.length-1;e>=0;--e){const i=n[e].$filler;i&&(i.line.updateControlPoints(o,i.axis),s&&i.fill&&da(t.ctx,i,o))}},beforeDatasetsDraw(t,e,i){if("beforeDatasetsDraw"!==i.drawTime)return;const s=t.getSortedVisibleDatasetMetas();for(let e=s.length-1;e>=0;--e){const i=s[e].$filler;na(i)&&da(t.ctx,i,t.chartArea)}},beforeDatasetDraw(t,e,i){const s=e.meta.$filler;na(s)&&"beforeDatasetDraw"===i.drawTime&&da(t.ctx,s,t.chartArea)},defaults:{propagate:!0,drawTime:"beforeDatasetDraw"}};const ba=(t,e)=>{let{boxHeight:i=e,boxWidth:s=e}=t;return t.usePointStyle&&(i=Math.min(i,e),s=t.pointStyleWidth||Math.min(s,e)),{boxWidth:s,boxHeight:i,itemHeight:Math.max(e,i)}};class xa extends Hs{constructor(t){super(),this._added=!1,this.legendHitBoxes=[],this._hoveredItem=null,this.doughnutMode=!1,this.chart=t.chart,this.options=t.options,this.ctx=t.ctx,this.legendItems=void 0,this.columnSizes=void 0,this.lineWidths=void 0,this.maxHeight=void 0,this.maxWidth=void 0,this.top=void 0,this.bottom=void 0,this.left=void 0,this.right=void 0,this.height=void 0,this.width=void 0,this._margins=void 0,this.position=void 0,this.weight=void 0,this.fullSize=void 0}update(t,e,i){this.maxWidth=t,this.maxHeight=e,this._margins=i,this.setDimensions(),this.buildLabels(),this.fit()}setDimensions(){this.isHorizontal()?(this.width=this.maxWidth,this.left=this._margins.left,this.right=this.width):(this.height=this.maxHeight,this.top=this._margins.top,this.bottom=this.height)}buildLabels(){const t=this.options.labels||{};let e=d(t.generateLabels,[this.chart],this)||[];t.filter&&(e=e.filter((e=>t.filter(e,this.chart.data)))),t.sort&&(e=e.sort(((e,i)=>t.sort(e,i,this.chart.data)))),this.options.reverse&&e.reverse(),this.legendItems=e}fit(){const{options:t,ctx:e}=this;if(!t.display)return void(this.width=this.height=0);const i=t.labels,s=Si(i.font),n=s.size,o=this._computeTitleHeight(),{boxWidth:a,itemHeight:r}=ba(i,n);let l,h;e.font=s.string,this.isHorizontal()?(l=this.maxWidth,h=this._fitRows(o,n,a,r)+10):(h=this.maxHeight,l=this._fitCols(o,s,a,r)+10),this.width=Math.min(l,t.maxWidth||this.maxWidth),this.height=Math.min(h,t.maxHeight||this.maxHeight)}_fitRows(t,e,i,s){const{ctx:n,maxWidth:o,options:{labels:{padding:a}}}=this,r=this.legendHitBoxes=[],l=this.lineWidths=[0],h=s+a;let c=t;n.textAlign="left",n.textBaseline="middle";let d=-1,u=-h;return this.legendItems.forEach(((t,f)=>{const g=i+e/2+n.measureText(t.text).width;(0===f||l[l.length-1]+g+2*a>o)&&(c+=h,l[l.length-(f>0?0:1)]=0,u+=h,d++),r[f]={left:0,top:u,row:d,width:g,height:s},l[l.length-1]+=g+a})),c}_fitCols(t,e,i,s){const{ctx:n,maxHeight:o,options:{labels:{padding:a}}}=this,r=this.legendHitBoxes=[],l=this.columnSizes=[],h=o-t;let c=a,d=0,u=0,f=0,g=0;return this.legendItems.forEach(((t,o)=>{const{itemWidth:p,itemHeight:m}=function(t,e,i,s,n){const o=function(t,e,i,s){let n=t.text;n&&"string"!=typeof n&&(n=n.reduce(((t,e)=>t.length>e.length?t:e)));return e+i.size/2+s.measureText(n).width}(s,t,e,i),a=function(t,e,i){let s=t;"string"!=typeof e.text&&(s=_a(e,i));return s}(n,s,e.lineHeight);return{itemWidth:o,itemHeight:a}}(i,e,n,t,s);o>0&&u+m+2*a>h&&(c+=d+a,l.push({width:d,height:u}),f+=d+a,g++,d=u=0),r[o]={left:f,top:u,col:g,width:p,height:m},d=Math.max(d,p),u+=m+a})),c+=d,l.push({width:d,height:u}),c}adjustHitBoxes(){if(!this.options.display)return;const t=this._computeTitleHeight(),{legendHitBoxes:e,options:{align:i,labels:{padding:s},rtl:n}}=this,o=Oi(n,this.left,this.width);if(this.isHorizontal()){let n=0,a=ft(i,this.left+s,this.right-this.lineWidths[n]);for(const r of e)n!==r.row&&(n=r.row,a=ft(i,this.left+s,this.right-this.lineWidths[n])),r.top+=this.top+t+s,r.left=o.leftForLtr(o.x(a),r.width),a+=r.width+s}else{let n=0,a=ft(i,this.top+t+s,this.bottom-this.columnSizes[n].height);for(const r of e)r.col!==n&&(n=r.col,a=ft(i,this.top+t+s,this.bottom-this.columnSizes[n].height)),r.top=a,r.left+=this.left+s,r.left=o.leftForLtr(o.x(r.left),r.width),a+=r.height+s}}isHorizontal(){return"top"===this.options.position||"bottom"===this.options.position}draw(){if(this.options.display){const t=this.ctx;Ie(t,this),this._draw(),ze(t)}}_draw(){const{options:t,columnSizes:e,lineWidths:i,ctx:s}=this,{align:n,labels:o}=t,a=ue.color,r=Oi(t.rtl,this.left,this.width),h=Si(o.font),{padding:c}=o,d=h.size,u=d/2;let f;this.drawTitle(),s.textAlign=r.textAlign("left"),s.textBaseline="middle",s.lineWidth=.5,s.font=h.string;const{boxWidth:g,boxHeight:p,itemHeight:m}=ba(o,d),b=this.isHorizontal(),x=this._computeTitleHeight();f=b?{x:ft(n,this.left+c,this.right-i[0]),y:this.top+c+x,line:0}:{x:this.left+c,y:ft(n,this.top+x+c,this.bottom-e[0].height),line:0},Ai(this.ctx,t.textDirection);const _=m+c;this.legendItems.forEach(((y,v)=>{s.strokeStyle=y.fontColor,s.fillStyle=y.fontColor;const M=s.measureText(y.text).width,w=r.textAlign(y.textAlign||(y.textAlign=o.textAlign)),k=g+u+M;let S=f.x,P=f.y;r.setWidth(this.width),b?v>0&&S+k+c>this.right&&(P=f.y+=_,f.line++,S=f.x=ft(n,this.left+c,this.right-i[f.line])):v>0&&P+_>this.bottom&&(S=f.x=S+e[f.line].width+c,f.line++,P=f.y=ft(n,this.top+x+c,this.bottom-e[f.line].height));if(function(t,e,i){if(isNaN(g)||g<=0||isNaN(p)||p<0)return;s.save();const n=l(i.lineWidth,1);if(s.fillStyle=l(i.fillStyle,a),s.lineCap=l(i.lineCap,"butt"),s.lineDashOffset=l(i.lineDashOffset,0),s.lineJoin=l(i.lineJoin,"miter"),s.lineWidth=n,s.strokeStyle=l(i.strokeStyle,a),s.setLineDash(l(i.lineDash,[])),o.usePointStyle){const a={radius:p*Math.SQRT2/2,pointStyle:i.pointStyle,rotation:i.rotation,borderWidth:n},l=r.xPlus(t,g/2);Ee(s,a,l,e+u,o.pointStyleWidth&&g)}else{const o=e+Math.max((d-p)/2,0),a=r.leftForLtr(t,g),l=wi(i.borderRadius);s.beginPath(),Object.values(l).some((t=>0!==t))?He(s,{x:a,y:o,w:g,h:p,radius:l}):s.rect(a,o,g,p),s.fill(),0!==n&&s.stroke()}s.restore()}(r.x(S),P,y),S=gt(w,S+g+u,b?S+k:this.right,t.rtl),function(t,e,i){Ne(s,i.text,t,e+m/2,h,{strikethrough:i.hidden,textAlign:r.textAlign(i.textAlign)})}(r.x(S),P,y),b)f.x+=k+c;else if("string"!=typeof y.text){const t=h.lineHeight;f.y+=_a(y,t)+c}else f.y+=_})),Ti(this.ctx,t.textDirection)}drawTitle(){const t=this.options,e=t.title,i=Si(e.font),s=ki(e.padding);if(!e.display)return;const n=Oi(t.rtl,this.left,this.width),o=this.ctx,a=e.position,r=i.size/2,l=s.top+r;let h,c=this.left,d=this.width;if(this.isHorizontal())d=Math.max(...this.lineWidths),h=this.top+l,c=ft(t.align,c,this.right-d);else{const e=this.columnSizes.reduce(((t,e)=>Math.max(t,e.height)),0);h=l+ft(t.align,this.top,this.bottom-e-t.labels.padding-this._computeTitleHeight())}const u=ft(a,c,c+d);o.textAlign=n.textAlign(ut(a)),o.textBaseline="middle",o.strokeStyle=e.color,o.fillStyle=e.color,o.font=i.string,Ne(o,e.text,u,h,i)}_computeTitleHeight(){const t=this.options.title,e=Si(t.font),i=ki(t.padding);return t.display?e.lineHeight+i.height:0}_getLegendItemAt(t,e){let i,s,n;if(tt(t,this.left,this.right)&&tt(e,this.top,this.bottom))for(n=this.legendHitBoxes,i=0;i<n.length;++i)if(s=n[i],tt(t,s.left,s.left+s.width)&&tt(e,s.top,s.top+s.height))return this.legendItems[i];return null}handleEvent(t){const e=this.options;if(!function(t,e){if(("mousemove"===t||"mouseout"===t)&&(e.onHover||e.onLeave))return!0;if(e.onClick&&("click"===t||"mouseup"===t))return!0;return!1}(t.type,e))return;const i=this._getLegendItemAt(t.x,t.y);if("mousemove"===t.type||"mouseout"===t.type){const o=this._hoveredItem,a=(n=i,null!==(s=o)&&null!==n&&s.datasetIndex===n.datasetIndex&&s.index===n.index);o&&!a&&d(e.onLeave,[t,o,this],this),this._hoveredItem=i,i&&!a&&d(e.onHover,[t,i,this],this)}else i&&d(e.onClick,[t,i,this],this);var s,n}}function _a(t,e){return e*(t.text?t.text.length:0)}var ya={id:"legend",_element:xa,start(t,e,i){const s=t.legend=new xa({ctx:t.ctx,options:i,chart:t});as.configure(t,s,i),as.addBox(t,s)},stop(t){as.removeBox(t,t.legend),delete t.legend},beforeUpdate(t,e,i){const s=t.legend;as.configure(t,s,i),s.options=i},afterUpdate(t){const e=t.legend;e.buildLabels(),e.adjustHitBoxes()},afterEvent(t,e){e.replay||t.legend.handleEvent(e.event)},defaults:{display:!0,position:"top",align:"center",fullSize:!0,reverse:!1,weight:1e3,onClick(t,e,i){const s=e.datasetIndex,n=i.chart;n.isDatasetVisible(s)?(n.hide(s),e.hidden=!0):(n.show(s),e.hidden=!1)},onHover:null,onLeave:null,labels:{color:t=>t.chart.options.color,boxWidth:40,padding:10,generateLabels(t){const e=t.data.datasets,{labels:{usePointStyle:i,pointStyle:s,textAlign:n,color:o,useBorderRadius:a,borderRadius:r}}=t.legend.options;return t._getSortedDatasetMetas().map((t=>{const l=t.controller.getStyle(i?0:void 0),h=ki(l.borderWidth);return{text:e[t.index].label,fillStyle:l.backgroundColor,fontColor:o,hidden:!t.visible,lineCap:l.borderCapStyle,lineDash:l.borderDash,lineDashOffset:l.borderDashOffset,lineJoin:l.borderJoinStyle,lineWidth:(h.width+h.height)/4,strokeStyle:l.borderColor,pointStyle:s||l.pointStyle,rotation:l.rotation,textAlign:n||l.textAlign,borderRadius:a&&(r||l.borderRadius),datasetIndex:t.index}}),this)}},title:{color:t=>t.chart.options.color,display:!1,position:"center",text:""}},descriptors:{_scriptable:t=>!t.startsWith("on"),labels:{_scriptable:t=>!["generateLabels","filter","sort"].includes(t)}}};class va extends Hs{constructor(t){super(),this.chart=t.chart,this.options=t.options,this.ctx=t.ctx,this._padding=void 0,this.top=void 0,this.bottom=void 0,this.left=void 0,this.right=void 0,this.width=void 0,this.height=void 0,this.position=void 0,this.weight=void 0,this.fullSize=void 0}update(t,e){const i=this.options;if(this.left=0,this.top=0,!i.display)return void(this.width=this.height=this.right=this.bottom=0);this.width=this.right=t,this.height=this.bottom=e;const s=n(i.text)?i.text.length:1;this._padding=ki(i.padding);const o=s*Si(i.font).lineHeight+this._padding.height;this.isHorizontal()?this.height=o:this.width=o}isHorizontal(){const t=this.options.position;return"top"===t||"bottom"===t}_drawArgs(t){const{top:e,left:i,bottom:s,right:n,options:o}=this,a=o.align;let r,l,h,c=0;return this.isHorizontal()?(l=ft(a,i,n),h=e+t,r=n-i):("left"===o.position?(l=i+t,h=ft(a,s,e),c=-.5*C):(l=n-t,h=ft(a,e,s),c=.5*C),r=s-e),{titleX:l,titleY:h,maxWidth:r,rotation:c}}draw(){const t=this.ctx,e=this.options;if(!e.display)return;const i=Si(e.font),s=i.lineHeight/2+this._padding.top,{titleX:n,titleY:o,maxWidth:a,rotation:r}=this._drawArgs(s);Ne(t,e.text,0,0,i,{color:e.color,maxWidth:a,rotation:r,textAlign:ut(e.align),textBaseline:"middle",translation:[n,o]})}}var Ma={id:"title",_element:va,start(t,e,i){!function(t,e){const i=new va({ctx:t.ctx,options:e,chart:t});as.configure(t,i,e),as.addBox(t,i),t.titleBlock=i}(t,i)},stop(t){const e=t.titleBlock;as.removeBox(t,e),delete t.titleBlock},beforeUpdate(t,e,i){const s=t.titleBlock;as.configure(t,s,i),s.options=i},defaults:{align:"center",display:!1,font:{weight:"bold"},fullSize:!0,padding:10,position:"top",text:"",weight:2e3},defaultRoutes:{color:"color"},descriptors:{_scriptable:!0,_indexable:!1}};const wa=new WeakMap;var ka={id:"subtitle",start(t,e,i){const s=new va({ctx:t.ctx,options:i,chart:t});as.configure(t,s,i),as.addBox(t,s),wa.set(t,s)},stop(t){as.removeBox(t,wa.get(t)),wa.delete(t)},beforeUpdate(t,e,i){const s=wa.get(t);as.configure(t,s,i),s.options=i},defaults:{align:"center",display:!1,font:{weight:"normal"},fullSize:!0,padding:0,position:"top",text:"",weight:1500},defaultRoutes:{color:"color"},descriptors:{_scriptable:!0,_indexable:!1}};const Sa={average(t){if(!t.length)return!1;let e,i,s=0,n=0,o=0;for(e=0,i=t.length;e<i;++e){const i=t[e].element;if(i&&i.hasValue()){const t=i.tooltipPosition();s+=t.x,n+=t.y,++o}}return{x:s/o,y:n/o}},nearest(t,e){if(!t.length)return!1;let i,s,n,o=e.x,a=e.y,r=Number.POSITIVE_INFINITY;for(i=0,s=t.length;i<s;++i){const s=t[i].element;if(s&&s.hasValue()){const t=q(e,s.getCenterPoint());t<r&&(r=t,n=s)}}if(n){const t=n.tooltipPosition();o=t.x,a=t.y}return{x:o,y:a}}};function Pa(t,e){return e&&(n(e)?Array.prototype.push.apply(t,e):t.push(e)),t}function Da(t){return("string"==typeof t||t instanceof String)&&t.indexOf("\n")>-1?t.split("\n"):t}function Ca(t,e){const{element:i,datasetIndex:s,index:n}=e,o=t.getDatasetMeta(s).controller,{label:a,value:r}=o.getLabelAndValue(n);return{chart:t,label:a,parsed:o.getParsed(n),raw:t.data.datasets[s].data[n],formattedValue:r,dataset:o.getDataset(),dataIndex:n,datasetIndex:s,element:i}}function Oa(t,e){const i=t.chart.ctx,{body:s,footer:n,title:o}=t,{boxWidth:a,boxHeight:r}=e,l=Si(e.bodyFont),h=Si(e.titleFont),c=Si(e.footerFont),d=o.length,f=n.length,g=s.length,p=ki(e.padding);let m=p.height,b=0,x=s.reduce(((t,e)=>t+e.before.length+e.lines.length+e.after.length),0);if(x+=t.beforeBody.length+t.afterBody.length,d&&(m+=d*h.lineHeight+(d-1)*e.titleSpacing+e.titleMarginBottom),x){m+=g*(e.displayColors?Math.max(r,l.lineHeight):l.lineHeight)+(x-g)*l.lineHeight+(x-1)*e.bodySpacing}f&&(m+=e.footerMarginTop+f*c.lineHeight+(f-1)*e.footerSpacing);let _=0;const y=function(t){b=Math.max(b,i.measureText(t).width+_)};return i.save(),i.font=h.string,u(t.title,y),i.font=l.string,u(t.beforeBody.concat(t.afterBody),y),_=e.displayColors?a+2+e.boxPadding:0,u(s,(t=>{u(t.before,y),u(t.lines,y),u(t.after,y)})),_=0,i.font=c.string,u(t.footer,y),i.restore(),b+=p.width,{width:b,height:m}}function Aa(t,e,i,s){const{x:n,width:o}=i,{width:a,chartArea:{left:r,right:l}}=t;let h="center";return"center"===s?h=n<=(r+l)/2?"left":"right":n<=o/2?h="left":n>=a-o/2&&(h="right"),function(t,e,i,s){const{x:n,width:o}=s,a=i.caretSize+i.caretPadding;return"left"===t&&n+o+a>e.width||"right"===t&&n-o-a<0||void 0}(h,t,e,i)&&(h="center"),h}function Ta(t,e,i){const s=i.yAlign||e.yAlign||function(t,e){const{y:i,height:s}=e;return i<s/2?"top":i>t.height-s/2?"bottom":"center"}(t,i);return{xAlign:i.xAlign||e.xAlign||Aa(t,e,i,s),yAlign:s}}function La(t,e,i,s){const{caretSize:n,caretPadding:o,cornerRadius:a}=t,{xAlign:r,yAlign:l}=i,h=n+o,{topLeft:c,topRight:d,bottomLeft:u,bottomRight:f}=wi(a);let g=function(t,e){let{x:i,width:s}=t;return"right"===e?i-=s:"center"===e&&(i-=s/2),i}(e,r);const p=function(t,e,i){let{y:s,height:n}=t;return"top"===e?s+=i:s-="bottom"===e?n+i:n/2,s}(e,l,h);return"center"===l?"left"===r?g+=h:"right"===r&&(g-=h):"left"===r?g-=Math.max(c,u)+n:"right"===r&&(g+=Math.max(d,f)+n),{x:J(g,0,s.width-e.width),y:J(p,0,s.height-e.height)}}function Ea(t,e,i){const s=ki(i.padding);return"center"===e?t.x+t.width/2:"right"===e?t.x+t.width-s.right:t.x+s.left}function Ra(t){return Pa([],Da(t))}function Ia(t,e){const i=e&&e.dataset&&e.dataset.tooltip&&e.dataset.tooltip.callbacks;return i?t.override(i):t}const za={beforeTitle:e,title(t){if(t.length>0){const e=t[0],i=e.chart.data.labels,s=i?i.length:0;if(this&&this.options&&"dataset"===this.options.mode)return e.dataset.label||"";if(e.label)return e.label;if(s>0&&e.dataIndex<s)return i[e.dataIndex]}return""},afterTitle:e,beforeBody:e,beforeLabel:e,label(t){if(this&&this.options&&"dataset"===this.options.mode)return t.label+": "+t.formattedValue||t.formattedValue;let e=t.dataset.label||"";e&&(e+=": ");const i=t.formattedValue;return s(i)||(e+=i),e},labelColor(t){const e=t.chart.getDatasetMeta(t.datasetIndex).controller.getStyle(t.dataIndex);return{borderColor:e.borderColor,backgroundColor:e.backgroundColor,borderWidth:e.borderWidth,borderDash:e.borderDash,borderDashOffset:e.borderDashOffset,borderRadius:0}},labelTextColor(){return this.options.bodyColor},labelPointStyle(t){const e=t.chart.getDatasetMeta(t.datasetIndex).controller.getStyle(t.dataIndex);return{pointStyle:e.pointStyle,rotation:e.rotation}},afterLabel:e,afterBody:e,beforeFooter:e,footer:e,afterFooter:e};function Fa(t,e,i,s){const n=t[e].call(i,s);return void 0===n?za[e].call(i,s):n}class Va extends Hs{static positioners=Sa;constructor(t){super(),this.opacity=0,this._active=[],this._eventPosition=void 0,this._size=void 0,this._cachedAnimations=void 0,this._tooltipItems=[],this.$animations=void 0,this.$context=void 0,this.chart=t.chart,this.options=t.options,this.dataPoints=void 0,this.title=void 0,this.beforeBody=void 0,this.body=void 0,this.afterBody=void 0,this.footer=void 0,this.xAlign=void 0,this.yAlign=void 0,this.x=void 0,this.y=void 0,this.height=void 0,this.width=void 0,this.caretX=void 0,this.caretY=void 0,this.labelColors=void 0,this.labelPointStyles=void 0,this.labelTextColors=void 0}initialize(t){this.options=t,this._cachedAnimations=void 0,this.$context=void 0}_resolveAnimations(){const t=this._cachedAnimations;if(t)return t;const e=this.chart,i=this.options.setContext(this.getContext()),s=i.enabled&&e.options.animation&&i.animations,n=new Os(this.chart,s);return s._cacheable&&(this._cachedAnimations=Object.freeze(n)),n}getContext(){return this.$context||(this.$context=(t=this.chart.getContext(),e=this,i=this._tooltipItems,Ci(t,{tooltip:e,tooltipItems:i,type:"tooltip"})));var t,e,i}getTitle(t,e){const{callbacks:i}=e,s=Fa(i,"beforeTitle",this,t),n=Fa(i,"title",this,t),o=Fa(i,"afterTitle",this,t);let a=[];return a=Pa(a,Da(s)),a=Pa(a,Da(n)),a=Pa(a,Da(o)),a}getBeforeBody(t,e){return Ra(Fa(e.callbacks,"beforeBody",this,t))}getBody(t,e){const{callbacks:i}=e,s=[];return u(t,(t=>{const e={before:[],lines:[],after:[]},n=Ia(i,t);Pa(e.before,Da(Fa(n,"beforeLabel",this,t))),Pa(e.lines,Fa(n,"label",this,t)),Pa(e.after,Da(Fa(n,"afterLabel",this,t))),s.push(e)})),s}getAfterBody(t,e){return Ra(Fa(e.callbacks,"afterBody",this,t))}getFooter(t,e){const{callbacks:i}=e,s=Fa(i,"beforeFooter",this,t),n=Fa(i,"footer",this,t),o=Fa(i,"afterFooter",this,t);let a=[];return a=Pa(a,Da(s)),a=Pa(a,Da(n)),a=Pa(a,Da(o)),a}_createItems(t){const e=this._active,i=this.chart.data,s=[],n=[],o=[];let a,r,l=[];for(a=0,r=e.length;a<r;++a)l.push(Ca(this.chart,e[a]));return t.filter&&(l=l.filter(((e,s,n)=>t.filter(e,s,n,i)))),t.itemSort&&(l=l.sort(((e,s)=>t.itemSort(e,s,i)))),u(l,(e=>{const i=Ia(t.callbacks,e);s.push(Fa(i,"labelColor",this,e)),n.push(Fa(i,"labelPointStyle",this,e)),o.push(Fa(i,"labelTextColor",this,e))})),this.labelColors=s,this.labelPointStyles=n,this.labelTextColors=o,this.dataPoints=l,l}update(t,e){const i=this.options.setContext(this.getContext()),s=this._active;let n,o=[];if(s.length){const t=Sa[i.position].call(this,s,this._eventPosition);o=this._createItems(i),this.title=this.getTitle(o,i),this.beforeBody=this.getBeforeBody(o,i),this.body=this.getBody(o,i),this.afterBody=this.getAfterBody(o,i),this.footer=this.getFooter(o,i);const e=this._size=Oa(this,i),a=Object.assign({},t,e),r=Ta(this.chart,i,a),l=La(i,a,r,this.chart);this.xAlign=r.xAlign,this.yAlign=r.yAlign,n={opacity:1,x:l.x,y:l.y,width:e.width,height:e.height,caretX:t.x,caretY:t.y}}else 0!==this.opacity&&(n={opacity:0});this._tooltipItems=o,this.$context=void 0,n&&this._resolveAnimations().update(this,n),t&&i.external&&i.external.call(this,{chart:this.chart,tooltip:this,replay:e})}drawCaret(t,e,i,s){const n=this.getCaretPosition(t,i,s);e.lineTo(n.x1,n.y1),e.lineTo(n.x2,n.y2),e.lineTo(n.x3,n.y3)}getCaretPosition(t,e,i){const{xAlign:s,yAlign:n}=this,{caretSize:o,cornerRadius:a}=i,{topLeft:r,topRight:l,bottomLeft:h,bottomRight:c}=wi(a),{x:d,y:u}=t,{width:f,height:g}=e;let p,m,b,x,_,y;return"center"===n?(_=u+g/2,"left"===s?(p=d,m=p-o,x=_+o,y=_-o):(p=d+f,m=p+o,x=_-o,y=_+o),b=p):(m="left"===s?d+Math.max(r,h)+o:"right"===s?d+f-Math.max(l,c)-o:this.caretX,"top"===n?(x=u,_=x-o,p=m-o,b=m+o):(x=u+g,_=x+o,p=m+o,b=m-o),y=x),{x1:p,x2:m,x3:b,y1:x,y2:_,y3:y}}drawTitle(t,e,i){const s=this.title,n=s.length;let o,a,r;if(n){const l=Oi(i.rtl,this.x,this.width);for(t.x=Ea(this,i.titleAlign,i),e.textAlign=l.textAlign(i.titleAlign),e.textBaseline="middle",o=Si(i.titleFont),a=i.titleSpacing,e.fillStyle=i.titleColor,e.font=o.string,r=0;r<n;++r)e.fillText(s[r],l.x(t.x),t.y+o.lineHeight/2),t.y+=o.lineHeight+a,r+1===n&&(t.y+=i.titleMarginBottom-a)}}_drawColorBox(t,e,i,s,n){const a=this.labelColors[i],r=this.labelPointStyles[i],{boxHeight:l,boxWidth:h}=n,c=Si(n.bodyFont),d=Ea(this,"left",n),u=s.x(d),f=l<c.lineHeight?(c.lineHeight-l)/2:0,g=e.y+f;if(n.usePointStyle){const e={radius:Math.min(h,l)/2,pointStyle:r.pointStyle,rotation:r.rotation,borderWidth:1},i=s.leftForLtr(u,h)+h/2,o=g+l/2;t.strokeStyle=n.multiKeyBackground,t.fillStyle=n.multiKeyBackground,Le(t,e,i,o),t.strokeStyle=a.borderColor,t.fillStyle=a.backgroundColor,Le(t,e,i,o)}else{t.lineWidth=o(a.borderWidth)?Math.max(...Object.values(a.borderWidth)):a.borderWidth||1,t.strokeStyle=a.borderColor,t.setLineDash(a.borderDash||[]),t.lineDashOffset=a.borderDashOffset||0;const e=s.leftForLtr(u,h),i=s.leftForLtr(s.xPlus(u,1),h-2),r=wi(a.borderRadius);Object.values(r).some((t=>0!==t))?(t.beginPath(),t.fillStyle=n.multiKeyBackground,He(t,{x:e,y:g,w:h,h:l,radius:r}),t.fill(),t.stroke(),t.fillStyle=a.backgroundColor,t.beginPath(),He(t,{x:i,y:g+1,w:h-2,h:l-2,radius:r}),t.fill()):(t.fillStyle=n.multiKeyBackground,t.fillRect(e,g,h,l),t.strokeRect(e,g,h,l),t.fillStyle=a.backgroundColor,t.fillRect(i,g+1,h-2,l-2))}t.fillStyle=this.labelTextColors[i]}drawBody(t,e,i){const{body:s}=this,{bodySpacing:n,bodyAlign:o,displayColors:a,boxHeight:r,boxWidth:l,boxPadding:h}=i,c=Si(i.bodyFont);let d=c.lineHeight,f=0;const g=Oi(i.rtl,this.x,this.width),p=function(i){e.fillText(i,g.x(t.x+f),t.y+d/2),t.y+=d+n},m=g.textAlign(o);let b,x,_,y,v,M,w;for(e.textAlign=o,e.textBaseline="middle",e.font=c.string,t.x=Ea(this,m,i),e.fillStyle=i.bodyColor,u(this.beforeBody,p),f=a&&"right"!==m?"center"===o?l/2+h:l+2+h:0,y=0,M=s.length;y<M;++y){for(b=s[y],x=this.labelTextColors[y],e.fillStyle=x,u(b.before,p),_=b.lines,a&&_.length&&(this._drawColorBox(e,t,y,g,i),d=Math.max(c.lineHeight,r)),v=0,w=_.length;v<w;++v)p(_[v]),d=c.lineHeight;u(b.after,p)}f=0,d=c.lineHeight,u(this.afterBody,p),t.y-=n}drawFooter(t,e,i){const s=this.footer,n=s.length;let o,a;if(n){const r=Oi(i.rtl,this.x,this.width);for(t.x=Ea(this,i.footerAlign,i),t.y+=i.footerMarginTop,e.textAlign=r.textAlign(i.footerAlign),e.textBaseline="middle",o=Si(i.footerFont),e.fillStyle=i.footerColor,e.font=o.string,a=0;a<n;++a)e.fillText(s[a],r.x(t.x),t.y+o.lineHeight/2),t.y+=o.lineHeight+i.footerSpacing}}drawBackground(t,e,i,s){const{xAlign:n,yAlign:o}=this,{x:a,y:r}=t,{width:l,height:h}=i,{topLeft:c,topRight:d,bottomLeft:u,bottomRight:f}=wi(s.cornerRadius);e.fillStyle=s.backgroundColor,e.strokeStyle=s.borderColor,e.lineWidth=s.borderWidth,e.beginPath(),e.moveTo(a+c,r),"top"===o&&this.drawCaret(t,e,i,s),e.lineTo(a+l-d,r),e.quadraticCurveTo(a+l,r,a+l,r+d),"center"===o&&"right"===n&&this.drawCaret(t,e,i,s),e.lineTo(a+l,r+h-f),e.quadraticCurveTo(a+l,r+h,a+l-f,r+h),"bottom"===o&&this.drawCaret(t,e,i,s),e.lineTo(a+u,r+h),e.quadraticCurveTo(a,r+h,a,r+h-u),"center"===o&&"left"===n&&this.drawCaret(t,e,i,s),e.lineTo(a,r+c),e.quadraticCurveTo(a,r,a+c,r),e.closePath(),e.fill(),s.borderWidth>0&&e.stroke()}_updateAnimationTarget(t){const e=this.chart,i=this.$animations,s=i&&i.x,n=i&&i.y;if(s||n){const i=Sa[t.position].call(this,this._active,this._eventPosition);if(!i)return;const o=this._size=Oa(this,t),a=Object.assign({},i,this._size),r=Ta(e,t,a),l=La(t,a,r,e);s._to===l.x&&n._to===l.y||(this.xAlign=r.xAlign,this.yAlign=r.yAlign,this.width=o.width,this.height=o.height,this.caretX=i.x,this.caretY=i.y,this._resolveAnimations().update(this,l))}}_willRender(){return!!this.opacity}draw(t){const e=this.options.setContext(this.getContext());let i=this.opacity;if(!i)return;this._updateAnimationTarget(e);const s={width:this.width,height:this.height},n={x:this.x,y:this.y};i=Math.abs(i)<.001?0:i;const o=ki(e.padding),a=this.title.length||this.beforeBody.length||this.body.length||this.afterBody.length||this.footer.length;e.enabled&&a&&(t.save(),t.globalAlpha=i,this.drawBackground(n,t,s,e),Ai(t,e.textDirection),n.y+=o.top,this.drawTitle(n,t,e),this.drawBody(n,t,e),this.drawFooter(n,t,e),Ti(t,e.textDirection),t.restore())}getActiveElements(){return this._active||[]}setActiveElements(t,e){const i=this._active,s=t.map((({datasetIndex:t,index:e})=>{const i=this.chart.getDatasetMeta(t);if(!i)throw new Error("Cannot find a dataset at index "+t);return{datasetIndex:t,element:i.data[e],index:e}})),n=!f(i,s),o=this._positionChanged(s,e);(n||o)&&(this._active=s,this._eventPosition=e,this._ignoreReplayEvents=!0,this.update(!0))}handleEvent(t,e,i=!0){if(e&&this._ignoreReplayEvents)return!1;this._ignoreReplayEvents=!1;const s=this.options,n=this._active||[],o=this._getActiveElements(t,n,e,i),a=this._positionChanged(o,t),r=e||!f(o,n)||a;return r&&(this._active=o,(s.enabled||s.external)&&(this._eventPosition={x:t.x,y:t.y},this.update(!0,e))),r}_getActiveElements(t,e,i,s){const n=this.options;if("mouseout"===t.type)return[];if(!s)return e;const o=this.chart.getElementsAtEventForMode(t,n.mode,n,i);return n.reverse&&o.reverse(),o}_positionChanged(t,e){const{caretX:i,caretY:s,options:n}=this,o=Sa[n.position].call(this,t,e);return!1!==o&&(i!==o.x||s!==o.y)}}var Ba={id:"tooltip",_element:Va,positioners:Sa,afterInit(t,e,i){i&&(t.tooltip=new Va({chart:t,options:i}))},beforeUpdate(t,e,i){t.tooltip&&t.tooltip.initialize(i)},reset(t,e,i){t.tooltip&&t.tooltip.initialize(i)},afterDraw(t){const e=t.tooltip;if(e&&e._willRender()){const i={tooltip:e};if(!1===t.notifyPlugins("beforeTooltipDraw",{...i,cancelable:!0}))return;e.draw(t.ctx),t.notifyPlugins("afterTooltipDraw",i)}},afterEvent(t,e){if(t.tooltip){const i=e.replay;t.tooltip.handleEvent(e.event,i,e.inChartArea)&&(e.changed=!0)}},defaults:{enabled:!0,external:null,position:"average",backgroundColor:"rgba(0,0,0,0.8)",titleColor:"#fff",titleFont:{weight:"bold"},titleSpacing:2,titleMarginBottom:6,titleAlign:"left",bodyColor:"#fff",bodySpacing:2,bodyFont:{},bodyAlign:"left",footerColor:"#fff",footerSpacing:2,footerMarginTop:6,footerFont:{weight:"bold"},footerAlign:"left",padding:6,caretPadding:2,caretSize:5,cornerRadius:6,boxHeight:(t,e)=>e.bodyFont.size,boxWidth:(t,e)=>e.bodyFont.size,multiKeyBackground:"#fff",displayColors:!0,boxPadding:0,borderColor:"rgba(0,0,0,0)",borderWidth:0,animation:{duration:400,easing:"easeOutQuart"},animations:{numbers:{type:"number",properties:["x","y","width","height","caretX","caretY"]},opacity:{easing:"linear",duration:200}},callbacks:za},defaultRoutes:{bodyFont:"font",footerFont:"font",titleFont:"font"},descriptors:{_scriptable:t=>"filter"!==t&&"itemSort"!==t&&"external"!==t,_indexable:!1,callbacks:{_scriptable:!1,_indexable:!1},animation:{_fallback:!1},animations:{_fallback:"animation"}},additionalOptionScopes:["interaction"]};return An.register(Yn,jo,fo,t),An.helpers={...Wi},An._adapters=Rn,An.Animation=Cs,An.Animations=Os,An.animator=xt,An.controllers=en.controllers.items,An.DatasetController=Ns,An.Element=Hs,An.elements=fo,An.Interaction=Xi,An.layouts=as,An.platforms=Ss,An.Scale=Js,An.Ticks=ae,Object.assign(An,Yn,jo,fo,t,Ss),An.Chart=An,"undefined"!=typeof window&&(window.Chart=An),An}));
20: //# sourceMappingURL=chart.umd.js.map
```

## File: switchbot_dashboard/static/vendor/js/chartjs-adapter-date-fns.bundle.min.js
```javascript
1: /*!
2:  * chartjs-adapter-date-fns v3.0.0
3:  * https://www.chartjs.org
4:  * (c) 2022 chartjs-adapter-date-fns Contributors
5:  * Released under the MIT license
6:  */
7: !function(t,e){"object"==typeof exports&&"undefined"!=typeof module?e(require("chart.js")):"function"==typeof define&&define.amd?define(["chart.js"],e):e((t="undefined"!=typeof globalThis?globalThis:t||self).Chart)}(this,(function(t){"use strict";function e(t){if(null===t||!0===t||!1===t)return NaN;var e=Number(t);return isNaN(e)?e:e<0?Math.ceil(e):Math.floor(e)}function r(t,e){if(e.length<t)throw new TypeError(t+" argument"+(t>1?"s":"")+" required, but only "+e.length+" present")}function n(t){r(1,arguments);var e=Object.prototype.toString.call(t);return t instanceof Date||"object"==typeof t&&"[object Date]"===e?new Date(t.getTime()):"number"==typeof t||"[object Number]"===e?new Date(t):("string"!=typeof t&&"[object String]"!==e||"undefined"==typeof console||(console.warn("Starting with v2.0.0-beta.1 date-fns doesn't accept strings as date arguments. Please use `parseISO` to parse strings. See: https://git.io/fjule"),console.warn((new Error).stack)),new Date(NaN))}function a(t,a){r(2,arguments);var i=n(t),o=e(a);return isNaN(o)?new Date(NaN):o?(i.setDate(i.getDate()+o),i):i}function i(t,a){r(2,arguments);var i=n(t),o=e(a);if(isNaN(o))return new Date(NaN);if(!o)return i;var u=i.getDate(),s=new Date(i.getTime());s.setMonth(i.getMonth()+o+1,0);var c=s.getDate();return u>=c?s:(i.setFullYear(s.getFullYear(),s.getMonth(),u),i)}function o(t,a){r(2,arguments);var i=n(t).getTime(),o=e(a);return new Date(i+o)}var u=36e5;function s(t,a){r(1,arguments);var i=a||{},o=i.locale,u=o&&o.options&&o.options.weekStartsOn,s=null==u?0:e(u),c=null==i.weekStartsOn?s:e(i.weekStartsOn);if(!(c>=0&&c<=6))throw new RangeError("weekStartsOn must be between 0 and 6 inclusively");var d=n(t),l=d.getDay(),f=(l<c?7:0)+l-c;return d.setDate(d.getDate()-f),d.setHours(0,0,0,0),d}function c(t){var e=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate(),t.getHours(),t.getMinutes(),t.getSeconds(),t.getMilliseconds()));return e.setUTCFullYear(t.getFullYear()),t.getTime()-e.getTime()}function d(t){r(1,arguments);var e=n(t);return e.setHours(0,0,0,0),e}var l=864e5;function f(t,e){r(2,arguments);var n=d(t),a=d(e),i=n.getTime()-c(n),o=a.getTime()-c(a);return Math.round((i-o)/l)}function h(t,e){r(2,arguments);var a=n(t),i=n(e),o=a.getTime()-i.getTime();return o<0?-1:o>0?1:o}function m(t){r(1,arguments);var e=n(t);return!isNaN(e)}function w(t,e){r(2,arguments);var a=n(t),i=n(e),o=a.getFullYear()-i.getFullYear(),u=a.getMonth()-i.getMonth();return 12*o+u}function g(t,e){r(2,arguments);var a=n(t),i=n(e);return a.getFullYear()-i.getFullYear()}function v(t,e){var r=t.getFullYear()-e.getFullYear()||t.getMonth()-e.getMonth()||t.getDate()-e.getDate()||t.getHours()-e.getHours()||t.getMinutes()-e.getMinutes()||t.getSeconds()-e.getSeconds()||t.getMilliseconds()-e.getMilliseconds();return r<0?-1:r>0?1:r}function y(t,e){r(2,arguments);var a=n(t),i=n(e),o=v(a,i),u=Math.abs(f(a,i));a.setDate(a.getDate()-o*u);var s=v(a,i)===-o,c=o*(u-s);return 0===c?0:c}function b(t,e){r(2,arguments);var a=n(t),i=n(e);return a.getTime()-i.getTime()}var T=36e5;function p(t){r(1,arguments);var e=n(t);return e.setHours(23,59,59,999),e}function C(t){r(1,arguments);var e=n(t),a=e.getMonth();return e.setFullYear(e.getFullYear(),a+1,0),e.setHours(23,59,59,999),e}function M(t){r(1,arguments);var e=n(t);return p(e).getTime()===C(e).getTime()}function D(t,e){r(2,arguments);var a,i=n(t),o=n(e),u=h(i,o),s=Math.abs(w(i,o));if(s<1)a=0;else{1===i.getMonth()&&i.getDate()>27&&i.setDate(30),i.setMonth(i.getMonth()-u*s);var c=h(i,o)===-u;M(n(t))&&1===s&&1===h(t,o)&&(c=!1),a=u*(s-c)}return 0===a?0:a}var x={lessThanXSeconds:{one:"less than a second",other:"less than {{count}} seconds"},xSeconds:{one:"1 second",other:"{{count}} seconds"},halfAMinute:"half a minute",lessThanXMinutes:{one:"less than a minute",other:"less than {{count}} minutes"},xMinutes:{one:"1 minute",other:"{{count}} minutes"},aboutXHours:{one:"about 1 hour",other:"about {{count}} hours"},xHours:{one:"1 hour",other:"{{count}} hours"},xDays:{one:"1 day",other:"{{count}} days"},aboutXWeeks:{one:"about 1 week",other:"about {{count}} weeks"},xWeeks:{one:"1 week",other:"{{count}} weeks"},aboutXMonths:{one:"about 1 month",other:"about {{count}} months"},xMonths:{one:"1 month",other:"{{count}} months"},aboutXYears:{one:"about 1 year",other:"about {{count}} years"},xYears:{one:"1 year",other:"{{count}} years"},overXYears:{one:"over 1 year",other:"over {{count}} years"},almostXYears:{one:"almost 1 year",other:"almost {{count}} years"}};function k(t){return function(e){var r=e||{},n=r.width?String(r.width):t.defaultWidth;return t.formats[n]||t.formats[t.defaultWidth]}}var U={date:k({formats:{full:"EEEE, MMMM do, y",long:"MMMM do, y",medium:"MMM d, y",short:"MM/dd/yyyy"},defaultWidth:"full"}),time:k({formats:{full:"h:mm:ss a zzzz",long:"h:mm:ss a z",medium:"h:mm:ss a",short:"h:mm a"},defaultWidth:"full"}),dateTime:k({formats:{full:"{{date}} 'at' {{time}}",long:"{{date}} 'at' {{time}}",medium:"{{date}}, {{time}}",short:"{{date}}, {{time}}"},defaultWidth:"full"})},Y={lastWeek:"'last' eeee 'at' p",yesterday:"'yesterday at' p",today:"'today at' p",tomorrow:"'tomorrow at' p",nextWeek:"eeee 'at' p",other:"P"};function N(t){return function(e,r){var n,a=r||{};if("formatting"===(a.context?String(a.context):"standalone")&&t.formattingValues){var i=t.defaultFormattingWidth||t.defaultWidth,o=a.width?String(a.width):i;n=t.formattingValues[o]||t.formattingValues[i]}else{var u=t.defaultWidth,s=a.width?String(a.width):t.defaultWidth;n=t.values[s]||t.values[u]}return n[t.argumentCallback?t.argumentCallback(e):e]}}function S(t){return function(e,r){var n=String(e),a=r||{},i=a.width,o=i&&t.matchPatterns[i]||t.matchPatterns[t.defaultMatchWidth],u=n.match(o);if(!u)return null;var s,c=u[0],d=i&&t.parsePatterns[i]||t.parsePatterns[t.defaultParseWidth];return s="[object Array]"===Object.prototype.toString.call(d)?function(t,e){for(var r=0;r<t.length;r++)if(e(t[r]))return r}(d,(function(t){return t.test(c)})):function(t,e){for(var r in t)if(t.hasOwnProperty(r)&&e(t[r]))return r}(d,(function(t){return t.test(c)})),s=t.valueCallback?t.valueCallback(s):s,{value:s=a.valueCallback?a.valueCallback(s):s,rest:n.slice(c.length)}}}var P,q={code:"en-US",formatDistance:function(t,e,r){var n;return r=r||{},n="string"==typeof x[t]?x[t]:1===e?x[t].one:x[t].other.replace("{{count}}",e),r.addSuffix?r.comparison>0?"in "+n:n+" ago":n},formatLong:U,formatRelative:function(t,e,r,n){return Y[t]},localize:{ordinalNumber:function(t,e){var r=Number(t),n=r%100;if(n>20||n<10)switch(n%10){case 1:return r+"st";case 2:return r+"nd";case 3:return r+"rd"}return r+"th"},era:N({values:{narrow:["B","A"],abbreviated:["BC","AD"],wide:["Before Christ","Anno Domini"]},defaultWidth:"wide"}),quarter:N({values:{narrow:["1","2","3","4"],abbreviated:["Q1","Q2","Q3","Q4"],wide:["1st quarter","2nd quarter","3rd quarter","4th quarter"]},defaultWidth:"wide",argumentCallback:function(t){return Number(t)-1}}),month:N({values:{narrow:["J","F","M","A","M","J","J","A","S","O","N","D"],abbreviated:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],wide:["January","February","March","April","May","June","July","August","September","October","November","December"]},defaultWidth:"wide"}),day:N({values:{narrow:["S","M","T","W","T","F","S"],short:["Su","Mo","Tu","We","Th","Fr","Sa"],abbreviated:["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],wide:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]},defaultWidth:"wide"}),dayPeriod:N({values:{narrow:{am:"a",pm:"p",midnight:"mi",noon:"n",morning:"morning",afternoon:"afternoon",evening:"evening",night:"night"},abbreviated:{am:"AM",pm:"PM",midnight:"midnight",noon:"noon",morning:"morning",afternoon:"afternoon",evening:"evening",night:"night"},wide:{am:"a.m.",pm:"p.m.",midnight:"midnight",noon:"noon",morning:"morning",afternoon:"afternoon",evening:"evening",night:"night"}},defaultWidth:"wide",formattingValues:{narrow:{am:"a",pm:"p",midnight:"mi",noon:"n",morning:"in the morning",afternoon:"in the afternoon",evening:"in the evening",night:"at night"},abbreviated:{am:"AM",pm:"PM",midnight:"midnight",noon:"noon",morning:"in the morning",afternoon:"in the afternoon",evening:"in the evening",night:"at night"},wide:{am:"a.m.",pm:"p.m.",midnight:"midnight",noon:"noon",morning:"in the morning",afternoon:"in the afternoon",evening:"in the evening",night:"at night"}},defaultFormattingWidth:"wide"})},match:{ordinalNumber:(P={matchPattern:/^(\d+)(th|st|nd|rd)?/i,parsePattern:/\d+/i,valueCallback:function(t){return parseInt(t,10)}},function(t,e){var r=String(t),n=e||{},a=r.match(P.matchPattern);if(!a)return null;var i=a[0],o=r.match(P.parsePattern);if(!o)return null;var u=P.valueCallback?P.valueCallback(o[0]):o[0];return{value:u=n.valueCallback?n.valueCallback(u):u,rest:r.slice(i.length)}}),era:S({matchPatterns:{narrow:/^(b|a)/i,abbreviated:/^(b\.?\s?c\.?|b\.?\s?c\.?\s?e\.?|a\.?\s?d\.?|c\.?\s?e\.?)/i,wide:/^(before christ|before common era|anno domini|common era)/i},defaultMatchWidth:"wide",parsePatterns:{any:[/^b/i,/^(a|c)/i]},defaultParseWidth:"any"}),quarter:S({matchPatterns:{narrow:/^[1234]/i,abbreviated:/^q[1234]/i,wide:/^[1234](th|st|nd|rd)? quarter/i},defaultMatchWidth:"wide",parsePatterns:{any:[/1/i,/2/i,/3/i,/4/i]},defaultParseWidth:"any",valueCallback:function(t){return t+1}}),month:S({matchPatterns:{narrow:/^[jfmasond]/i,abbreviated:/^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)/i,wide:/^(january|february|march|april|may|june|july|august|september|october|november|december)/i},defaultMatchWidth:"wide",parsePatterns:{narrow:[/^j/i,/^f/i,/^m/i,/^a/i,/^m/i,/^j/i,/^j/i,/^a/i,/^s/i,/^o/i,/^n/i,/^d/i],any:[/^ja/i,/^f/i,/^mar/i,/^ap/i,/^may/i,/^jun/i,/^jul/i,/^au/i,/^s/i,/^o/i,/^n/i,/^d/i]},defaultParseWidth:"any"}),day:S({matchPatterns:{narrow:/^[smtwf]/i,short:/^(su|mo|tu|we|th|fr|sa)/i,abbreviated:/^(sun|mon|tue|wed|thu|fri|sat)/i,wide:/^(sunday|monday|tuesday|wednesday|thursday|friday|saturday)/i},defaultMatchWidth:"wide",parsePatterns:{narrow:[/^s/i,/^m/i,/^t/i,/^w/i,/^t/i,/^f/i,/^s/i],any:[/^su/i,/^m/i,/^tu/i,/^w/i,/^th/i,/^f/i,/^sa/i]},defaultParseWidth:"any"}),dayPeriod:S({matchPatterns:{narrow:/^(a|p|mi|n|(in the|at) (morning|afternoon|evening|night))/i,any:/^([ap]\.?\s?m\.?|midnight|noon|(in the|at) (morning|afternoon|evening|night))/i},defaultMatchWidth:"any",parsePatterns:{any:{am:/^a/i,pm:/^p/i,midnight:/^mi/i,noon:/^no/i,morning:/morning/i,afternoon:/afternoon/i,evening:/evening/i,night:/night/i}},defaultParseWidth:"any"})},options:{weekStartsOn:0,firstWeekContainsDate:1}};function H(t,n){r(2,arguments);var a=e(n);return o(t,-a)}function E(t,e){for(var r=t<0?"-":"",n=Math.abs(t).toString();n.length<e;)n="0"+n;return r+n}var O={y:function(t,e){var r=t.getUTCFullYear(),n=r>0?r:1-r;return E("yy"===e?n%100:n,e.length)},M:function(t,e){var r=t.getUTCMonth();return"M"===e?String(r+1):E(r+1,2)},d:function(t,e){return E(t.getUTCDate(),e.length)},a:function(t,e){var r=t.getUTCHours()/12>=1?"pm":"am";switch(e){case"a":case"aa":return r.toUpperCase();case"aaa":return r;case"aaaaa":return r[0];default:return"am"===r?"a.m.":"p.m."}},h:function(t,e){return E(t.getUTCHours()%12||12,e.length)},H:function(t,e){return E(t.getUTCHours(),e.length)},m:function(t,e){return E(t.getUTCMinutes(),e.length)},s:function(t,e){return E(t.getUTCSeconds(),e.length)},S:function(t,e){var r=e.length,n=t.getUTCMilliseconds();return E(Math.floor(n*Math.pow(10,r-3)),e.length)}},F=864e5;function W(t){r(1,arguments);var e=1,a=n(t),i=a.getUTCDay(),o=(i<e?7:0)+i-e;return a.setUTCDate(a.getUTCDate()-o),a.setUTCHours(0,0,0,0),a}function L(t){r(1,arguments);var e=n(t),a=e.getUTCFullYear(),i=new Date(0);i.setUTCFullYear(a+1,0,4),i.setUTCHours(0,0,0,0);var o=W(i),u=new Date(0);u.setUTCFullYear(a,0,4),u.setUTCHours(0,0,0,0);var s=W(u);return e.getTime()>=o.getTime()?a+1:e.getTime()>=s.getTime()?a:a-1}function Q(t){r(1,arguments);var e=L(t),n=new Date(0);n.setUTCFullYear(e,0,4),n.setUTCHours(0,0,0,0);var a=W(n);return a}var R=6048e5;function I(t){r(1,arguments);var e=n(t),a=W(e).getTime()-Q(e).getTime();return Math.round(a/R)+1}function G(t,a){r(1,arguments);var i=a||{},o=i.locale,u=o&&o.options&&o.options.weekStartsOn,s=null==u?0:e(u),c=null==i.weekStartsOn?s:e(i.weekStartsOn);if(!(c>=0&&c<=6))throw new RangeError("weekStartsOn must be between 0 and 6 inclusively");var d=n(t),l=d.getUTCDay(),f=(l<c?7:0)+l-c;return d.setUTCDate(d.getUTCDate()-f),d.setUTCHours(0,0,0,0),d}function X(t,a){r(1,arguments);var i=n(t,a),o=i.getUTCFullYear(),u=a||{},s=u.locale,c=s&&s.options&&s.options.firstWeekContainsDate,d=null==c?1:e(c),l=null==u.firstWeekContainsDate?d:e(u.firstWeekContainsDate);if(!(l>=1&&l<=7))throw new RangeError("firstWeekContainsDate must be between 1 and 7 inclusively");var f=new Date(0);f.setUTCFullYear(o+1,0,l),f.setUTCHours(0,0,0,0);var h=G(f,a),m=new Date(0);m.setUTCFullYear(o,0,l),m.setUTCHours(0,0,0,0);var w=G(m,a);return i.getTime()>=h.getTime()?o+1:i.getTime()>=w.getTime()?o:o-1}function j(t,n){r(1,arguments);var a=n||{},i=a.locale,o=i&&i.options&&i.options.firstWeekContainsDate,u=null==o?1:e(o),s=null==a.firstWeekContainsDate?u:e(a.firstWeekContainsDate),c=X(t,n),d=new Date(0);d.setUTCFullYear(c,0,s),d.setUTCHours(0,0,0,0);var l=G(d,n);return l}var B=6048e5;function z(t,e){r(1,arguments);var a=n(t),i=G(a,e).getTime()-j(a,e).getTime();return Math.round(i/B)+1}var A="midnight",Z="noon",K="morning",$="afternoon",_="evening",J="night",V={G:function(t,e,r){var n=t.getUTCFullYear()>0?1:0;switch(e){case"G":case"GG":case"GGG":return r.era(n,{width:"abbreviated"});case"GGGGG":return r.era(n,{width:"narrow"});default:return r.era(n,{width:"wide"})}},y:function(t,e,r){if("yo"===e){var n=t.getUTCFullYear(),a=n>0?n:1-n;return r.ordinalNumber(a,{unit:"year"})}return O.y(t,e)},Y:function(t,e,r,n){var a=X(t,n),i=a>0?a:1-a;return"YY"===e?E(i%100,2):"Yo"===e?r.ordinalNumber(i,{unit:"year"}):E(i,e.length)},R:function(t,e){return E(L(t),e.length)},u:function(t,e){return E(t.getUTCFullYear(),e.length)},Q:function(t,e,r){var n=Math.ceil((t.getUTCMonth()+1)/3);switch(e){case"Q":return String(n);case"QQ":return E(n,2);case"Qo":return r.ordinalNumber(n,{unit:"quarter"});case"QQQ":return r.quarter(n,{width:"abbreviated",context:"formatting"});case"QQQQQ":return r.quarter(n,{width:"narrow",context:"formatting"});default:return r.quarter(n,{width:"wide",context:"formatting"})}},q:function(t,e,r){var n=Math.ceil((t.getUTCMonth()+1)/3);switch(e){case"q":return String(n);case"qq":return E(n,2);case"qo":return r.ordinalNumber(n,{unit:"quarter"});case"qqq":return r.quarter(n,{width:"abbreviated",context:"standalone"});case"qqqqq":return r.quarter(n,{width:"narrow",context:"standalone"});default:return r.quarter(n,{width:"wide",context:"standalone"})}},M:function(t,e,r){var n=t.getUTCMonth();switch(e){case"M":case"MM":return O.M(t,e);case"Mo":return r.ordinalNumber(n+1,{unit:"month"});case"MMM":return r.month(n,{width:"abbreviated",context:"formatting"});case"MMMMM":return r.month(n,{width:"narrow",context:"formatting"});default:return r.month(n,{width:"wide",context:"formatting"})}},L:function(t,e,r){var n=t.getUTCMonth();switch(e){case"L":return String(n+1);case"LL":return E(n+1,2);case"Lo":return r.ordinalNumber(n+1,{unit:"month"});case"LLL":return r.month(n,{width:"abbreviated",context:"standalone"});case"LLLLL":return r.month(n,{width:"narrow",context:"standalone"});default:return r.month(n,{width:"wide",context:"standalone"})}},w:function(t,e,r,n){var a=z(t,n);return"wo"===e?r.ordinalNumber(a,{unit:"week"}):E(a,e.length)},I:function(t,e,r){var n=I(t);return"Io"===e?r.ordinalNumber(n,{unit:"week"}):E(n,e.length)},d:function(t,e,r){return"do"===e?r.ordinalNumber(t.getUTCDate(),{unit:"date"}):O.d(t,e)},D:function(t,e,a){var i=function(t){r(1,arguments);var e=n(t),a=e.getTime();e.setUTCMonth(0,1),e.setUTCHours(0,0,0,0);var i=e.getTime(),o=a-i;return Math.floor(o/F)+1}(t);return"Do"===e?a.ordinalNumber(i,{unit:"dayOfYear"}):E(i,e.length)},E:function(t,e,r){var n=t.getUTCDay();switch(e){case"E":case"EE":case"EEE":return r.day(n,{width:"abbreviated",context:"formatting"});case"EEEEE":return r.day(n,{width:"narrow",context:"formatting"});case"EEEEEE":return r.day(n,{width:"short",context:"formatting"});default:return r.day(n,{width:"wide",context:"formatting"})}},e:function(t,e,r,n){var a=t.getUTCDay(),i=(a-n.weekStartsOn+8)%7||7;switch(e){case"e":return String(i);case"ee":return E(i,2);case"eo":return r.ordinalNumber(i,{unit:"day"});case"eee":return r.day(a,{width:"abbreviated",context:"formatting"});case"eeeee":return r.day(a,{width:"narrow",context:"formatting"});case"eeeeee":return r.day(a,{width:"short",context:"formatting"});default:return r.day(a,{width:"wide",context:"formatting"})}},c:function(t,e,r,n){var a=t.getUTCDay(),i=(a-n.weekStartsOn+8)%7||7;switch(e){case"c":return String(i);case"cc":return E(i,e.length);case"co":return r.ordinalNumber(i,{unit:"day"});case"ccc":return r.day(a,{width:"abbreviated",context:"standalone"});case"ccccc":return r.day(a,{width:"narrow",context:"standalone"});case"cccccc":return r.day(a,{width:"short",context:"standalone"});default:return r.day(a,{width:"wide",context:"standalone"})}},i:function(t,e,r){var n=t.getUTCDay(),a=0===n?7:n;switch(e){case"i":return String(a);case"ii":return E(a,e.length);case"io":return r.ordinalNumber(a,{unit:"day"});case"iii":return r.day(n,{width:"abbreviated",context:"formatting"});case"iiiii":return r.day(n,{width:"narrow",context:"formatting"});case"iiiiii":return r.day(n,{width:"short",context:"formatting"});default:return r.day(n,{width:"wide",context:"formatting"})}},a:function(t,e,r){var n=t.getUTCHours()/12>=1?"pm":"am";switch(e){case"a":case"aa":return r.dayPeriod(n,{width:"abbreviated",context:"formatting"});case"aaa":return r.dayPeriod(n,{width:"abbreviated",context:"formatting"}).toLowerCase();case"aaaaa":return r.dayPeriod(n,{width:"narrow",context:"formatting"});default:return r.dayPeriod(n,{width:"wide",context:"formatting"})}},b:function(t,e,r){var n,a=t.getUTCHours();switch(n=12===a?Z:0===a?A:a/12>=1?"pm":"am",e){case"b":case"bb":return r.dayPeriod(n,{width:"abbreviated",context:"formatting"});case"bbb":return r.dayPeriod(n,{width:"abbreviated",context:"formatting"}).toLowerCase();case"bbbbb":return r.dayPeriod(n,{width:"narrow",context:"formatting"});default:return r.dayPeriod(n,{width:"wide",context:"formatting"})}},B:function(t,e,r){var n,a=t.getUTCHours();switch(n=a>=17?_:a>=12?$:a>=4?K:J,e){case"B":case"BB":case"BBB":return r.dayPeriod(n,{width:"abbreviated",context:"formatting"});case"BBBBB":return r.dayPeriod(n,{width:"narrow",context:"formatting"});default:return r.dayPeriod(n,{width:"wide",context:"formatting"})}},h:function(t,e,r){if("ho"===e){var n=t.getUTCHours()%12;return 0===n&&(n=12),r.ordinalNumber(n,{unit:"hour"})}return O.h(t,e)},H:function(t,e,r){return"Ho"===e?r.ordinalNumber(t.getUTCHours(),{unit:"hour"}):O.H(t,e)},K:function(t,e,r){var n=t.getUTCHours()%12;return"Ko"===e?r.ordinalNumber(n,{unit:"hour"}):E(n,e.length)},k:function(t,e,r){var n=t.getUTCHours();return 0===n&&(n=24),"ko"===e?r.ordinalNumber(n,{unit:"hour"}):E(n,e.length)},m:function(t,e,r){return"mo"===e?r.ordinalNumber(t.getUTCMinutes(),{unit:"minute"}):O.m(t,e)},s:function(t,e,r){return"so"===e?r.ordinalNumber(t.getUTCSeconds(),{unit:"second"}):O.s(t,e)},S:function(t,e){return O.S(t,e)},X:function(t,e,r,n){var a=(n._originalDate||t).getTimezoneOffset();if(0===a)return"Z";switch(e){case"X":return et(a);case"XXXX":case"XX":return rt(a);default:return rt(a,":")}},x:function(t,e,r,n){var a=(n._originalDate||t).getTimezoneOffset();switch(e){case"x":return et(a);case"xxxx":case"xx":return rt(a);default:return rt(a,":")}},O:function(t,e,r,n){var a=(n._originalDate||t).getTimezoneOffset();switch(e){case"O":case"OO":case"OOO":return"GMT"+tt(a,":");default:return"GMT"+rt(a,":")}},z:function(t,e,r,n){var a=(n._originalDate||t).getTimezoneOffset();switch(e){case"z":case"zz":case"zzz":return"GMT"+tt(a,":");default:return"GMT"+rt(a,":")}},t:function(t,e,r,n){var a=n._originalDate||t;return E(Math.floor(a.getTime()/1e3),e.length)},T:function(t,e,r,n){return E((n._originalDate||t).getTime(),e.length)}};function tt(t,e){var r=t>0?"-":"+",n=Math.abs(t),a=Math.floor(n/60),i=n%60;if(0===i)return r+String(a);var o=e||"";return r+String(a)+o+E(i,2)}function et(t,e){return t%60==0?(t>0?"-":"+")+E(Math.abs(t)/60,2):rt(t,e)}function rt(t,e){var r=e||"",n=t>0?"-":"+",a=Math.abs(t);return n+E(Math.floor(a/60),2)+r+E(a%60,2)}var nt=V;function at(t,e){switch(t){case"P":return e.date({width:"short"});case"PP":return e.date({width:"medium"});case"PPP":return e.date({width:"long"});default:return e.date({width:"full"})}}function it(t,e){switch(t){case"p":return e.time({width:"short"});case"pp":return e.time({width:"medium"});case"ppp":return e.time({width:"long"});default:return e.time({width:"full"})}}var ot={p:it,P:function(t,e){var r,n=t.match(/(P+)(p+)?/),a=n[1],i=n[2];if(!i)return at(t,e);switch(a){case"P":r=e.dateTime({width:"short"});break;case"PP":r=e.dateTime({width:"medium"});break;case"PPP":r=e.dateTime({width:"long"});break;default:r=e.dateTime({width:"full"})}return r.replace("{{date}}",at(a,e)).replace("{{time}}",it(i,e))}},ut=ot,st=["D","DD"],ct=["YY","YYYY"];function dt(t){return-1!==st.indexOf(t)}function lt(t){return-1!==ct.indexOf(t)}function ft(t,e,r){if("YYYY"===t)throw new RangeError("Use `yyyy` instead of `YYYY` (in `".concat(e,"`) for formatting years to the input `").concat(r,"`; see: https://git.io/fxCyr"));if("YY"===t)throw new RangeError("Use `yy` instead of `YY` (in `".concat(e,"`) for formatting years to the input `").concat(r,"`; see: https://git.io/fxCyr"));if("D"===t)throw new RangeError("Use `d` instead of `D` (in `".concat(e,"`) for formatting days of the month to the input `").concat(r,"`; see: https://git.io/fxCyr"));if("DD"===t)throw new RangeError("Use `dd` instead of `DD` (in `".concat(e,"`) for formatting days of the month to the input `").concat(r,"`; see: https://git.io/fxCyr"))}var ht=/[yYQqMLwIdDecihHKkms]o|(\w)\1*|''|'(''|[^'])+('|$)|./g,mt=/P+p+|P+|p+|''|'(''|[^'])+('|$)|./g,wt=/^'([^]*?)'?$/,gt=/''/g,vt=/[a-zA-Z]/;function yt(t){return t.match(wt)[1].replace(gt,"'")}function bt(t,e){if(null==t)throw new TypeError("assign requires that input parameter not be null or undefined");for(var r in e=e||{})e.hasOwnProperty(r)&&(t[r]=e[r]);return t}function Tt(t,a,i){r(2,arguments);var o=i||{},u=o.locale,s=u&&u.options&&u.options.weekStartsOn,c=null==s?0:e(s),d=null==o.weekStartsOn?c:e(o.weekStartsOn);if(!(d>=0&&d<=6))throw new RangeError("weekStartsOn must be between 0 and 6 inclusively");var l=n(t),f=e(a),h=l.getUTCDay(),m=f%7,w=(m+7)%7,g=(w<d?7:0)+f-h;return l.setUTCDate(l.getUTCDate()+g),l}var pt=/^(1[0-2]|0?\d)/,Ct=/^(3[0-1]|[0-2]?\d)/,Mt=/^(36[0-6]|3[0-5]\d|[0-2]?\d?\d)/,Dt=/^(5[0-3]|[0-4]?\d)/,xt=/^(2[0-3]|[0-1]?\d)/,kt=/^(2[0-4]|[0-1]?\d)/,Ut=/^(1[0-1]|0?\d)/,Yt=/^(1[0-2]|0?\d)/,Nt=/^[0-5]?\d/,St=/^[0-5]?\d/,Pt=/^\d/,qt=/^\d{1,2}/,Ht=/^\d{1,3}/,Et=/^\d{1,4}/,Ot=/^-?\d+/,Ft=/^-?\d/,Wt=/^-?\d{1,2}/,Lt=/^-?\d{1,3}/,Qt=/^-?\d{1,4}/,Rt=/^([+-])(\d{2})(\d{2})?|Z/,It=/^([+-])(\d{2})(\d{2})|Z/,Gt=/^([+-])(\d{2})(\d{2})((\d{2}))?|Z/,Xt=/^([+-])(\d{2}):(\d{2})|Z/,jt=/^([+-])(\d{2}):(\d{2})(:(\d{2}))?|Z/;function Bt(t,e,r){var n=e.match(t);if(!n)return null;var a=parseInt(n[0],10);return{value:r?r(a):a,rest:e.slice(n[0].length)}}function zt(t,e){var r=e.match(t);return r?"Z"===r[0]?{value:0,rest:e.slice(1)}:{value:("+"===r[1]?1:-1)*(36e5*(r[2]?parseInt(r[2],10):0)+6e4*(r[3]?parseInt(r[3],10):0)+1e3*(r[5]?parseInt(r[5],10):0)),rest:e.slice(r[0].length)}:null}function At(t,e){return Bt(Ot,t,e)}function Zt(t,e,r){switch(t){case 1:return Bt(Pt,e,r);case 2:return Bt(qt,e,r);case 3:return Bt(Ht,e,r);case 4:return Bt(Et,e,r);default:return Bt(new RegExp("^\\d{1,"+t+"}"),e,r)}}function Kt(t,e,r){switch(t){case 1:return Bt(Ft,e,r);case 2:return Bt(Wt,e,r);case 3:return Bt(Lt,e,r);case 4:return Bt(Qt,e,r);default:return Bt(new RegExp("^-?\\d{1,"+t+"}"),e,r)}}function $t(t){switch(t){case"morning":return 4;case"evening":return 17;case"pm":case"noon":case"afternoon":return 12;default:return 0}}function _t(t,e){var r,n=e>0,a=n?e:1-e;if(a<=50)r=t||100;else{var i=a+50;r=t+100*Math.floor(i/100)-(t>=i%100?100:0)}return n?r:1-r}var Jt=[31,28,31,30,31,30,31,31,30,31,30,31],Vt=[31,29,31,30,31,30,31,31,30,31,30,31];function te(t){return t%400==0||t%4==0&&t%100!=0}var ee={G:{priority:140,parse:function(t,e,r,n){switch(e){case"G":case"GG":case"GGG":return r.era(t,{width:"abbreviated"})||r.era(t,{width:"narrow"});case"GGGGG":return r.era(t,{width:"narrow"});default:return r.era(t,{width:"wide"})||r.era(t,{width:"abbreviated"})||r.era(t,{width:"narrow"})}},set:function(t,e,r,n){return e.era=r,t.setUTCFullYear(r,0,1),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["R","u","t","T"]},y:{priority:130,parse:function(t,e,r,n){var a=function(t){return{year:t,isTwoDigitYear:"yy"===e}};switch(e){case"y":return Zt(4,t,a);case"yo":return r.ordinalNumber(t,{unit:"year",valueCallback:a});default:return Zt(e.length,t,a)}},validate:function(t,e,r){return e.isTwoDigitYear||e.year>0},set:function(t,e,r,n){var a=t.getUTCFullYear();if(r.isTwoDigitYear){var i=_t(r.year,a);return t.setUTCFullYear(i,0,1),t.setUTCHours(0,0,0,0),t}var o="era"in e&&1!==e.era?1-r.year:r.year;return t.setUTCFullYear(o,0,1),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["Y","R","u","w","I","i","e","c","t","T"]},Y:{priority:130,parse:function(t,e,r,n){var a=function(t){return{year:t,isTwoDigitYear:"YY"===e}};switch(e){case"Y":return Zt(4,t,a);case"Yo":return r.ordinalNumber(t,{unit:"year",valueCallback:a});default:return Zt(e.length,t,a)}},validate:function(t,e,r){return e.isTwoDigitYear||e.year>0},set:function(t,e,r,n){var a=X(t,n);if(r.isTwoDigitYear){var i=_t(r.year,a);return t.setUTCFullYear(i,0,n.firstWeekContainsDate),t.setUTCHours(0,0,0,0),G(t,n)}var o="era"in e&&1!==e.era?1-r.year:r.year;return t.setUTCFullYear(o,0,n.firstWeekContainsDate),t.setUTCHours(0,0,0,0),G(t,n)},incompatibleTokens:["y","R","u","Q","q","M","L","I","d","D","i","t","T"]},R:{priority:130,parse:function(t,e,r,n){return Kt("R"===e?4:e.length,t)},set:function(t,e,r,n){var a=new Date(0);return a.setUTCFullYear(r,0,4),a.setUTCHours(0,0,0,0),W(a)},incompatibleTokens:["G","y","Y","u","Q","q","M","L","w","d","D","e","c","t","T"]},u:{priority:130,parse:function(t,e,r,n){return Kt("u"===e?4:e.length,t)},set:function(t,e,r,n){return t.setUTCFullYear(r,0,1),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["G","y","Y","R","w","I","i","e","c","t","T"]},Q:{priority:120,parse:function(t,e,r,n){switch(e){case"Q":case"QQ":return Zt(e.length,t);case"Qo":return r.ordinalNumber(t,{unit:"quarter"});case"QQQ":return r.quarter(t,{width:"abbreviated",context:"formatting"})||r.quarter(t,{width:"narrow",context:"formatting"});case"QQQQQ":return r.quarter(t,{width:"narrow",context:"formatting"});default:return r.quarter(t,{width:"wide",context:"formatting"})||r.quarter(t,{width:"abbreviated",context:"formatting"})||r.quarter(t,{width:"narrow",context:"formatting"})}},validate:function(t,e,r){return e>=1&&e<=4},set:function(t,e,r,n){return t.setUTCMonth(3*(r-1),1),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["Y","R","q","M","L","w","I","d","D","i","e","c","t","T"]},q:{priority:120,parse:function(t,e,r,n){switch(e){case"q":case"qq":return Zt(e.length,t);case"qo":return r.ordinalNumber(t,{unit:"quarter"});case"qqq":return r.quarter(t,{width:"abbreviated",context:"standalone"})||r.quarter(t,{width:"narrow",context:"standalone"});case"qqqqq":return r.quarter(t,{width:"narrow",context:"standalone"});default:return r.quarter(t,{width:"wide",context:"standalone"})||r.quarter(t,{width:"abbreviated",context:"standalone"})||r.quarter(t,{width:"narrow",context:"standalone"})}},validate:function(t,e,r){return e>=1&&e<=4},set:function(t,e,r,n){return t.setUTCMonth(3*(r-1),1),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["Y","R","Q","M","L","w","I","d","D","i","e","c","t","T"]},M:{priority:110,parse:function(t,e,r,n){var a=function(t){return t-1};switch(e){case"M":return Bt(pt,t,a);case"MM":return Zt(2,t,a);case"Mo":return r.ordinalNumber(t,{unit:"month",valueCallback:a});case"MMM":return r.month(t,{width:"abbreviated",context:"formatting"})||r.month(t,{width:"narrow",context:"formatting"});case"MMMMM":return r.month(t,{width:"narrow",context:"formatting"});default:return r.month(t,{width:"wide",context:"formatting"})||r.month(t,{width:"abbreviated",context:"formatting"})||r.month(t,{width:"narrow",context:"formatting"})}},validate:function(t,e,r){return e>=0&&e<=11},set:function(t,e,r,n){return t.setUTCMonth(r,1),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["Y","R","q","Q","L","w","I","D","i","e","c","t","T"]},L:{priority:110,parse:function(t,e,r,n){var a=function(t){return t-1};switch(e){case"L":return Bt(pt,t,a);case"LL":return Zt(2,t,a);case"Lo":return r.ordinalNumber(t,{unit:"month",valueCallback:a});case"LLL":return r.month(t,{width:"abbreviated",context:"standalone"})||r.month(t,{width:"narrow",context:"standalone"});case"LLLLL":return r.month(t,{width:"narrow",context:"standalone"});default:return r.month(t,{width:"wide",context:"standalone"})||r.month(t,{width:"abbreviated",context:"standalone"})||r.month(t,{width:"narrow",context:"standalone"})}},validate:function(t,e,r){return e>=0&&e<=11},set:function(t,e,r,n){return t.setUTCMonth(r,1),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["Y","R","q","Q","M","w","I","D","i","e","c","t","T"]},w:{priority:100,parse:function(t,e,r,n){switch(e){case"w":return Bt(Dt,t);case"wo":return r.ordinalNumber(t,{unit:"week"});default:return Zt(e.length,t)}},validate:function(t,e,r){return e>=1&&e<=53},set:function(t,a,i,o){return G(function(t,a,i){r(2,arguments);var o=n(t),u=e(a),s=z(o,i)-u;return o.setUTCDate(o.getUTCDate()-7*s),o}(t,i,o),o)},incompatibleTokens:["y","R","u","q","Q","M","L","I","d","D","i","t","T"]},I:{priority:100,parse:function(t,e,r,n){switch(e){case"I":return Bt(Dt,t);case"Io":return r.ordinalNumber(t,{unit:"week"});default:return Zt(e.length,t)}},validate:function(t,e,r){return e>=1&&e<=53},set:function(t,a,i,o){return W(function(t,a){r(2,arguments);var i=n(t),o=e(a),u=I(i)-o;return i.setUTCDate(i.getUTCDate()-7*u),i}(t,i,o),o)},incompatibleTokens:["y","Y","u","q","Q","M","L","w","d","D","e","c","t","T"]},d:{priority:90,subPriority:1,parse:function(t,e,r,n){switch(e){case"d":return Bt(Ct,t);case"do":return r.ordinalNumber(t,{unit:"date"});default:return Zt(e.length,t)}},validate:function(t,e,r){var n=te(t.getUTCFullYear()),a=t.getUTCMonth();return n?e>=1&&e<=Vt[a]:e>=1&&e<=Jt[a]},set:function(t,e,r,n){return t.setUTCDate(r),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["Y","R","q","Q","w","I","D","i","e","c","t","T"]},D:{priority:90,subPriority:1,parse:function(t,e,r,n){switch(e){case"D":case"DD":return Bt(Mt,t);case"Do":return r.ordinalNumber(t,{unit:"date"});default:return Zt(e.length,t)}},validate:function(t,e,r){return te(t.getUTCFullYear())?e>=1&&e<=366:e>=1&&e<=365},set:function(t,e,r,n){return t.setUTCMonth(0,r),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["Y","R","q","Q","M","L","w","I","d","E","i","e","c","t","T"]},E:{priority:90,parse:function(t,e,r,n){switch(e){case"E":case"EE":case"EEE":return r.day(t,{width:"abbreviated",context:"formatting"})||r.day(t,{width:"short",context:"formatting"})||r.day(t,{width:"narrow",context:"formatting"});case"EEEEE":return r.day(t,{width:"narrow",context:"formatting"});case"EEEEEE":return r.day(t,{width:"short",context:"formatting"})||r.day(t,{width:"narrow",context:"formatting"});default:return r.day(t,{width:"wide",context:"formatting"})||r.day(t,{width:"abbreviated",context:"formatting"})||r.day(t,{width:"short",context:"formatting"})||r.day(t,{width:"narrow",context:"formatting"})}},validate:function(t,e,r){return e>=0&&e<=6},set:function(t,e,r,n){return(t=Tt(t,r,n)).setUTCHours(0,0,0,0),t},incompatibleTokens:["D","i","e","c","t","T"]},e:{priority:90,parse:function(t,e,r,n){var a=function(t){var e=7*Math.floor((t-1)/7);return(t+n.weekStartsOn+6)%7+e};switch(e){case"e":case"ee":return Zt(e.length,t,a);case"eo":return r.ordinalNumber(t,{unit:"day",valueCallback:a});case"eee":return r.day(t,{width:"abbreviated",context:"formatting"})||r.day(t,{width:"short",context:"formatting"})||r.day(t,{width:"narrow",context:"formatting"});case"eeeee":return r.day(t,{width:"narrow",context:"formatting"});case"eeeeee":return r.day(t,{width:"short",context:"formatting"})||r.day(t,{width:"narrow",context:"formatting"});default:return r.day(t,{width:"wide",context:"formatting"})||r.day(t,{width:"abbreviated",context:"formatting"})||r.day(t,{width:"short",context:"formatting"})||r.day(t,{width:"narrow",context:"formatting"})}},validate:function(t,e,r){return e>=0&&e<=6},set:function(t,e,r,n){return(t=Tt(t,r,n)).setUTCHours(0,0,0,0),t},incompatibleTokens:["y","R","u","q","Q","M","L","I","d","D","E","i","c","t","T"]},c:{priority:90,parse:function(t,e,r,n){var a=function(t){var e=7*Math.floor((t-1)/7);return(t+n.weekStartsOn+6)%7+e};switch(e){case"c":case"cc":return Zt(e.length,t,a);case"co":return r.ordinalNumber(t,{unit:"day",valueCallback:a});case"ccc":return r.day(t,{width:"abbreviated",context:"standalone"})||r.day(t,{width:"short",context:"standalone"})||r.day(t,{width:"narrow",context:"standalone"});case"ccccc":return r.day(t,{width:"narrow",context:"standalone"});case"cccccc":return r.day(t,{width:"short",context:"standalone"})||r.day(t,{width:"narrow",context:"standalone"});default:return r.day(t,{width:"wide",context:"standalone"})||r.day(t,{width:"abbreviated",context:"standalone"})||r.day(t,{width:"short",context:"standalone"})||r.day(t,{width:"narrow",context:"standalone"})}},validate:function(t,e,r){return e>=0&&e<=6},set:function(t,e,r,n){return(t=Tt(t,r,n)).setUTCHours(0,0,0,0),t},incompatibleTokens:["y","R","u","q","Q","M","L","I","d","D","E","i","e","t","T"]},i:{priority:90,parse:function(t,e,r,n){var a=function(t){return 0===t?7:t};switch(e){case"i":case"ii":return Zt(e.length,t);case"io":return r.ordinalNumber(t,{unit:"day"});case"iii":return r.day(t,{width:"abbreviated",context:"formatting",valueCallback:a})||r.day(t,{width:"short",context:"formatting",valueCallback:a})||r.day(t,{width:"narrow",context:"formatting",valueCallback:a});case"iiiii":return r.day(t,{width:"narrow",context:"formatting",valueCallback:a});case"iiiiii":return r.day(t,{width:"short",context:"formatting",valueCallback:a})||r.day(t,{width:"narrow",context:"formatting",valueCallback:a});default:return r.day(t,{width:"wide",context:"formatting",valueCallback:a})||r.day(t,{width:"abbreviated",context:"formatting",valueCallback:a})||r.day(t,{width:"short",context:"formatting",valueCallback:a})||r.day(t,{width:"narrow",context:"formatting",valueCallback:a})}},validate:function(t,e,r){return e>=1&&e<=7},set:function(t,a,i,o){return t=function(t,a){r(2,arguments);var i=e(a);i%7==0&&(i-=7);var o=1,u=n(t),s=u.getUTCDay(),c=((i%7+7)%7<o?7:0)+i-s;return u.setUTCDate(u.getUTCDate()+c),u}(t,i,o),t.setUTCHours(0,0,0,0),t},incompatibleTokens:["y","Y","u","q","Q","M","L","w","d","D","E","e","c","t","T"]},a:{priority:80,parse:function(t,e,r,n){switch(e){case"a":case"aa":case"aaa":return r.dayPeriod(t,{width:"abbreviated",context:"formatting"})||r.dayPeriod(t,{width:"narrow",context:"formatting"});case"aaaaa":return r.dayPeriod(t,{width:"narrow",context:"formatting"});default:return r.dayPeriod(t,{width:"wide",context:"formatting"})||r.dayPeriod(t,{width:"abbreviated",context:"formatting"})||r.dayPeriod(t,{width:"narrow",context:"formatting"})}},set:function(t,e,r,n){return t.setUTCHours($t(r),0,0,0),t},incompatibleTokens:["b","B","H","K","k","t","T"]},b:{priority:80,parse:function(t,e,r,n){switch(e){case"b":case"bb":case"bbb":return r.dayPeriod(t,{width:"abbreviated",context:"formatting"})||r.dayPeriod(t,{width:"narrow",context:"formatting"});case"bbbbb":return r.dayPeriod(t,{width:"narrow",context:"formatting"});default:return r.dayPeriod(t,{width:"wide",context:"formatting"})||r.dayPeriod(t,{width:"abbreviated",context:"formatting"})||r.dayPeriod(t,{width:"narrow",context:"formatting"})}},set:function(t,e,r,n){return t.setUTCHours($t(r),0,0,0),t},incompatibleTokens:["a","B","H","K","k","t","T"]},B:{priority:80,parse:function(t,e,r,n){switch(e){case"B":case"BB":case"BBB":return r.dayPeriod(t,{width:"abbreviated",context:"formatting"})||r.dayPeriod(t,{width:"narrow",context:"formatting"});case"BBBBB":return r.dayPeriod(t,{width:"narrow",context:"formatting"});default:return r.dayPeriod(t,{width:"wide",context:"formatting"})||r.dayPeriod(t,{width:"abbreviated",context:"formatting"})||r.dayPeriod(t,{width:"narrow",context:"formatting"})}},set:function(t,e,r,n){return t.setUTCHours($t(r),0,0,0),t},incompatibleTokens:["a","b","t","T"]},h:{priority:70,parse:function(t,e,r,n){switch(e){case"h":return Bt(Yt,t);case"ho":return r.ordinalNumber(t,{unit:"hour"});default:return Zt(e.length,t)}},validate:function(t,e,r){return e>=1&&e<=12},set:function(t,e,r,n){var a=t.getUTCHours()>=12;return a&&r<12?t.setUTCHours(r+12,0,0,0):a||12!==r?t.setUTCHours(r,0,0,0):t.setUTCHours(0,0,0,0),t},incompatibleTokens:["H","K","k","t","T"]},H:{priority:70,parse:function(t,e,r,n){switch(e){case"H":return Bt(xt,t);case"Ho":return r.ordinalNumber(t,{unit:"hour"});default:return Zt(e.length,t)}},validate:function(t,e,r){return e>=0&&e<=23},set:function(t,e,r,n){return t.setUTCHours(r,0,0,0),t},incompatibleTokens:["a","b","h","K","k","t","T"]},K:{priority:70,parse:function(t,e,r,n){switch(e){case"K":return Bt(Ut,t);case"Ko":return r.ordinalNumber(t,{unit:"hour"});default:return Zt(e.length,t)}},validate:function(t,e,r){return e>=0&&e<=11},set:function(t,e,r,n){return t.getUTCHours()>=12&&r<12?t.setUTCHours(r+12,0,0,0):t.setUTCHours(r,0,0,0),t},incompatibleTokens:["a","b","h","H","k","t","T"]},k:{priority:70,parse:function(t,e,r,n){switch(e){case"k":return Bt(kt,t);case"ko":return r.ordinalNumber(t,{unit:"hour"});default:return Zt(e.length,t)}},validate:function(t,e,r){return e>=1&&e<=24},set:function(t,e,r,n){var a=r<=24?r%24:r;return t.setUTCHours(a,0,0,0),t},incompatibleTokens:["a","b","h","H","K","t","T"]},m:{priority:60,parse:function(t,e,r,n){switch(e){case"m":return Bt(Nt,t);case"mo":return r.ordinalNumber(t,{unit:"minute"});default:return Zt(e.length,t)}},validate:function(t,e,r){return e>=0&&e<=59},set:function(t,e,r,n){return t.setUTCMinutes(r,0,0),t},incompatibleTokens:["t","T"]},s:{priority:50,parse:function(t,e,r,n){switch(e){case"s":return Bt(St,t);case"so":return r.ordinalNumber(t,{unit:"second"});default:return Zt(e.length,t)}},validate:function(t,e,r){return e>=0&&e<=59},set:function(t,e,r,n){return t.setUTCSeconds(r,0),t},incompatibleTokens:["t","T"]},S:{priority:30,parse:function(t,e,r,n){return Zt(e.length,t,(function(t){return Math.floor(t*Math.pow(10,3-e.length))}))},set:function(t,e,r,n){return t.setUTCMilliseconds(r),t},incompatibleTokens:["t","T"]},X:{priority:10,parse:function(t,e,r,n){switch(e){case"X":return zt(Rt,t);case"XX":return zt(It,t);case"XXXX":return zt(Gt,t);case"XXXXX":return zt(jt,t);default:return zt(Xt,t)}},set:function(t,e,r,n){return e.timestampIsSet?t:new Date(t.getTime()-r)},incompatibleTokens:["t","T","x"]},x:{priority:10,parse:function(t,e,r,n){switch(e){case"x":return zt(Rt,t);case"xx":return zt(It,t);case"xxxx":return zt(Gt,t);case"xxxxx":return zt(jt,t);default:return zt(Xt,t)}},set:function(t,e,r,n){return e.timestampIsSet?t:new Date(t.getTime()-r)},incompatibleTokens:["t","T","X"]},t:{priority:40,parse:function(t,e,r,n){return At(t)},set:function(t,e,r,n){return[new Date(1e3*r),{timestampIsSet:!0}]},incompatibleTokens:"*"},T:{priority:20,parse:function(t,e,r,n){return At(t)},set:function(t,e,r,n){return[new Date(r),{timestampIsSet:!0}]},incompatibleTokens:"*"}},re=ee,ne=/[yYQqMLwIdDecihHKkms]o|(\w)\1*|''|'(''|[^'])+('|$)|./g,ae=/P+p+|P+|p+|''|'(''|[^'])+('|$)|./g,ie=/^'([^]*?)'?$/,oe=/''/g,ue=/\S/,se=/[a-zA-Z]/;function ce(t,e){if(e.timestampIsSet)return t;var r=new Date(0);return r.setFullYear(t.getUTCFullYear(),t.getUTCMonth(),t.getUTCDate()),r.setHours(t.getUTCHours(),t.getUTCMinutes(),t.getUTCSeconds(),t.getUTCMilliseconds()),r}function de(t){return t.match(ie)[1].replace(oe,"'")}var le=36e5,fe={dateTimeDelimiter:/[T ]/,timeZoneDelimiter:/[Z ]/i,timezone:/([Z+-].*)$/},he=/^-?(?:(\d{3})|(\d{2})(?:-?(\d{2}))?|W(\d{2})(?:-?(\d{1}))?|)$/,me=/^(\d{2}(?:[.,]\d*)?)(?::?(\d{2}(?:[.,]\d*)?))?(?::?(\d{2}(?:[.,]\d*)?))?$/,we=/^([+-])(\d{2})(?::?(\d{2}))?$/;function ge(t){var e,r={},n=t.split(fe.dateTimeDelimiter);if(n.length>2)return r;if(/:/.test(n[0])?(r.date=null,e=n[0]):(r.date=n[0],e=n[1],fe.timeZoneDelimiter.test(r.date)&&(r.date=t.split(fe.timeZoneDelimiter)[0],e=t.substr(r.date.length,t.length))),e){var a=fe.timezone.exec(e);a?(r.time=e.replace(a[1],""),r.timezone=a[1]):r.time=e}return r}function ve(t,e){var r=new RegExp("^(?:(\\d{4}|[+-]\\d{"+(4+e)+"})|(\\d{2}|[+-]\\d{"+(2+e)+"})$)"),n=t.match(r);if(!n)return{year:null};var a=n[1]&&parseInt(n[1]),i=n[2]&&parseInt(n[2]);return{year:null==i?a:100*i,restDateString:t.slice((n[1]||n[2]).length)}}function ye(t,e){if(null===e)return null;var r=t.match(he);if(!r)return null;var n=!!r[4],a=be(r[1]),i=be(r[2])-1,o=be(r[3]),u=be(r[4]),s=be(r[5])-1;if(n)return function(t,e,r){return e>=1&&e<=53&&r>=0&&r<=6}(0,u,s)?function(t,e,r){var n=new Date(0);n.setUTCFullYear(t,0,4);var a=n.getUTCDay()||7,i=7*(e-1)+r+1-a;return n.setUTCDate(n.getUTCDate()+i),n}(e,u,s):new Date(NaN);var c=new Date(0);return function(t,e,r){return e>=0&&e<=11&&r>=1&&r<=(Me[e]||(De(t)?29:28))}(e,i,o)&&function(t,e){return e>=1&&e<=(De(t)?366:365)}(e,a)?(c.setUTCFullYear(e,i,Math.max(a,o)),c):new Date(NaN)}function be(t){return t?parseInt(t):1}function Te(t){var e=t.match(me);if(!e)return null;var r=pe(e[1]),n=pe(e[2]),a=pe(e[3]);return function(t,e,r){if(24===t)return 0===e&&0===r;return r>=0&&r<60&&e>=0&&e<60&&t>=0&&t<25}(r,n,a)?r*le+6e4*n+1e3*a:NaN}function pe(t){return t&&parseFloat(t.replace(",","."))||0}function Ce(t){if("Z"===t)return 0;var e=t.match(we);if(!e)return 0;var r="+"===e[1]?-1:1,n=parseInt(e[2]),a=e[3]&&parseInt(e[3])||0;return function(t,e){return e>=0&&e<=59}(0,a)?r*(n*le+6e4*a):NaN}var Me=[31,null,31,30,31,30,31,31,30,31,30,31];function De(t){return t%400==0||t%4==0&&t%100}const xe={datetime:"MMM d, yyyy, h:mm:ss aaaa",millisecond:"h:mm:ss.SSS aaaa",second:"h:mm:ss aaaa",minute:"h:mm aaaa",hour:"ha",day:"MMM d",week:"PP",month:"MMM yyyy",quarter:"qqq - yyyy",year:"yyyy"};t._adapters._date.override({_id:"date-fns",formats:function(){return xe},parse:function(t,a){if(null==t)return null;const i=typeof t;return"number"===i||t instanceof Date?t=n(t):"string"===i&&(t="string"==typeof a?function(t,a,i,o){r(3,arguments);var u=String(t),s=String(a),d=o||{},l=d.locale||q;if(!l.match)throw new RangeError("locale must contain match property");var f=l.options&&l.options.firstWeekContainsDate,h=null==f?1:e(f),m=null==d.firstWeekContainsDate?h:e(d.firstWeekContainsDate);if(!(m>=1&&m<=7))throw new RangeError("firstWeekContainsDate must be between 1 and 7 inclusively");var w=l.options&&l.options.weekStartsOn,g=null==w?0:e(w),v=null==d.weekStartsOn?g:e(d.weekStartsOn);if(!(v>=0&&v<=6))throw new RangeError("weekStartsOn must be between 0 and 6 inclusively");if(""===s)return""===u?n(i):new Date(NaN);var y,b={firstWeekContainsDate:m,weekStartsOn:v,locale:l},T=[{priority:10,subPriority:-1,set:ce,index:0}],p=s.match(ae).map((function(t){var e=t[0];return"p"===e||"P"===e?(0,ut[e])(t,l.formatLong,b):t})).join("").match(ne),C=[];for(y=0;y<p.length;y++){var M=p[y];!d.useAdditionalWeekYearTokens&&lt(M)&&ft(M,s,t),!d.useAdditionalDayOfYearTokens&&dt(M)&&ft(M,s,t);var D=M[0],x=re[D];if(x){var k=x.incompatibleTokens;if(Array.isArray(k)){for(var U=void 0,Y=0;Y<C.length;Y++){var N=C[Y].token;if(-1!==k.indexOf(N)||N===D){U=C[Y];break}}if(U)throw new RangeError("The format string mustn't contain `".concat(U.fullToken,"` and `").concat(M,"` at the same time"))}else if("*"===x.incompatibleTokens&&C.length)throw new RangeError("The format string mustn't contain `".concat(M,"` and any other token at the same time"));C.push({token:D,fullToken:M});var S=x.parse(u,M,l.match,b);if(!S)return new Date(NaN);T.push({priority:x.priority,subPriority:x.subPriority||0,set:x.set,validate:x.validate,value:S.value,index:T.length}),u=S.rest}else{if(D.match(se))throw new RangeError("Format string contains an unescaped latin alphabet character `"+D+"`");if("''"===M?M="'":"'"===D&&(M=de(M)),0!==u.indexOf(M))return new Date(NaN);u=u.slice(M.length)}}if(u.length>0&&ue.test(u))return new Date(NaN);var P=T.map((function(t){return t.priority})).sort((function(t,e){return e-t})).filter((function(t,e,r){return r.indexOf(t)===e})).map((function(t){return T.filter((function(e){return e.priority===t})).sort((function(t,e){return e.subPriority-t.subPriority}))})).map((function(t){return t[0]})),E=n(i);if(isNaN(E))return new Date(NaN);var O=H(E,c(E)),F={};for(y=0;y<P.length;y++){var W=P[y];if(W.validate&&!W.validate(O,W.value,b))return new Date(NaN);var L=W.set(O,F,W.value,b);L[0]?(O=L[0],bt(F,L[1])):O=L}return O}(t,a,new Date,this.options):function(t,n){r(1,arguments);var a=n||{},i=null==a.additionalDigits?2:e(a.additionalDigits);if(2!==i&&1!==i&&0!==i)throw new RangeError("additionalDigits must be 0, 1 or 2");if("string"!=typeof t&&"[object String]"!==Object.prototype.toString.call(t))return new Date(NaN);var o,u=ge(t);if(u.date){var s=ve(u.date,i);o=ye(s.restDateString,s.year)}if(isNaN(o)||!o)return new Date(NaN);var c,d=o.getTime(),l=0;if(u.time&&(l=Te(u.time),isNaN(l)||null===l))return new Date(NaN);if(!u.timezone){var f=new Date(d+l),h=new Date(0);return h.setFullYear(f.getUTCFullYear(),f.getUTCMonth(),f.getUTCDate()),h.setHours(f.getUTCHours(),f.getUTCMinutes(),f.getUTCSeconds(),f.getUTCMilliseconds()),h}return c=Ce(u.timezone),isNaN(c)?new Date(NaN):new Date(d+l+c)}(t,this.options)),m(t)?t.getTime():null},format:function(t,a){return function(t,a,i){r(2,arguments);var o=String(a),u=i||{},s=u.locale||q,d=s.options&&s.options.firstWeekContainsDate,l=null==d?1:e(d),f=null==u.firstWeekContainsDate?l:e(u.firstWeekContainsDate);if(!(f>=1&&f<=7))throw new RangeError("firstWeekContainsDate must be between 1 and 7 inclusively");var h=s.options&&s.options.weekStartsOn,w=null==h?0:e(h),g=null==u.weekStartsOn?w:e(u.weekStartsOn);if(!(g>=0&&g<=6))throw new RangeError("weekStartsOn must be between 0 and 6 inclusively");if(!s.localize)throw new RangeError("locale must contain localize property");if(!s.formatLong)throw new RangeError("locale must contain formatLong property");var v=n(t);if(!m(v))throw new RangeError("Invalid time value");var y=c(v),b=H(v,y),T={firstWeekContainsDate:f,weekStartsOn:g,locale:s,_originalDate:v},p=o.match(mt).map((function(t){var e=t[0];return"p"===e||"P"===e?(0,ut[e])(t,s.formatLong,T):t})).join("").match(ht).map((function(e){if("''"===e)return"'";var r=e[0];if("'"===r)return yt(e);var n=nt[r];if(n)return!u.useAdditionalWeekYearTokens&&lt(e)&&ft(e,a,t),!u.useAdditionalDayOfYearTokens&&dt(e)&&ft(e,a,t),n(b,e,s.localize,T);if(r.match(vt))throw new RangeError("Format string contains an unescaped latin alphabet character `"+r+"`");return e})).join("");return p}(t,a,this.options)},add:function(t,n,s){switch(s){case"millisecond":return o(t,n);case"second":return function(t,n){r(2,arguments);var a=e(n);return o(t,1e3*a)}(t,n);case"minute":return function(t,n){r(2,arguments);var a=e(n);return o(t,6e4*a)}(t,n);case"hour":return function(t,n){r(2,arguments);var a=e(n);return o(t,a*u)}(t,n);case"day":return a(t,n);case"week":return function(t,n){r(2,arguments);var i=e(n),o=7*i;return a(t,o)}(t,n);case"month":return i(t,n);case"quarter":return function(t,n){r(2,arguments);var a=e(n),o=3*a;return i(t,o)}(t,n);case"year":return function(t,n){r(2,arguments);var a=e(n);return i(t,12*a)}(t,n);default:return t}},diff:function(t,e,a){switch(a){case"millisecond":return b(t,e);case"second":return function(t,e){r(2,arguments);var n=b(t,e)/1e3;return n>0?Math.floor(n):Math.ceil(n)}(t,e);case"minute":return function(t,e){r(2,arguments);var n=b(t,e)/6e4;return n>0?Math.floor(n):Math.ceil(n)}(t,e);case"hour":return function(t,e){r(2,arguments);var n=b(t,e)/T;return n>0?Math.floor(n):Math.ceil(n)}(t,e);case"day":return y(t,e);case"week":return function(t,e){r(2,arguments);var n=y(t,e)/7;return n>0?Math.floor(n):Math.ceil(n)}(t,e);case"month":return D(t,e);case"quarter":return function(t,e){r(2,arguments);var n=D(t,e)/3;return n>0?Math.floor(n):Math.ceil(n)}(t,e);case"year":return function(t,e){r(2,arguments);var a=n(t),i=n(e),o=h(a,i),u=Math.abs(g(a,i));a.setFullYear("1584"),i.setFullYear("1584");var s=h(a,i)===-o,c=o*(u-s);return 0===c?0:c}(t,e);default:return 0}},startOf:function(t,e,a){switch(e){case"second":return function(t){r(1,arguments);var e=n(t);return e.setMilliseconds(0),e}(t);case"minute":return function(t){r(1,arguments);var e=n(t);return e.setSeconds(0,0),e}(t);case"hour":return function(t){r(1,arguments);var e=n(t);return e.setMinutes(0,0,0),e}(t);case"day":return d(t);case"week":return s(t);case"isoWeek":return s(t,{weekStartsOn:+a});case"month":return function(t){r(1,arguments);var e=n(t);return e.setDate(1),e.setHours(0,0,0,0),e}(t);case"quarter":return function(t){r(1,arguments);var e=n(t),a=e.getMonth(),i=a-a%3;return e.setMonth(i,1),e.setHours(0,0,0,0),e}(t);case"year":return function(t){r(1,arguments);var e=n(t),a=new Date(0);return a.setFullYear(e.getFullYear(),0,1),a.setHours(0,0,0,0),a}(t);default:return t}},endOf:function(t,a){switch(a){case"second":return function(t){r(1,arguments);var e=n(t);return e.setMilliseconds(999),e}(t);case"minute":return function(t){r(1,arguments);var e=n(t);return e.setSeconds(59,999),e}(t);case"hour":return function(t){r(1,arguments);var e=n(t);return e.setMinutes(59,59,999),e}(t);case"day":return p(t);case"week":return function(t,a){r(1,arguments);var i=a||{},o=i.locale,u=o&&o.options&&o.options.weekStartsOn,s=null==u?0:e(u),c=null==i.weekStartsOn?s:e(i.weekStartsOn);if(!(c>=0&&c<=6))throw new RangeError("weekStartsOn must be between 0 and 6 inclusively");var d=n(t),l=d.getDay(),f=6+(l<c?-7:0)-(l-c);return d.setDate(d.getDate()+f),d.setHours(23,59,59,999),d}(t);case"month":return C(t);case"quarter":return function(t){r(1,arguments);var e=n(t),a=e.getMonth(),i=a-a%3+3;return e.setMonth(i,0),e.setHours(23,59,59,999),e}(t);case"year":return function(t){r(1,arguments);var e=n(t),a=e.getFullYear();return e.setFullYear(a+1,0,0),e.setHours(23,59,59,999),e}(t);default:return t}}})}));
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
  1: import logging
  2: import threading
  3: from typing import Callable
  4: 
  5: from apscheduler.schedulers.background import BackgroundScheduler
  6: 
  7: from .config_store import BaseStore
  8: 
  9: 
 10: class SchedulerService:
 11:     def __init__(self, settings_store: BaseStore, tick_callable: Callable[[], None], *, logger: logging.Logger | None = None) -> None:
 12:         self._settings_store = settings_store
 13:         self._tick_callable = tick_callable
 14:         self._scheduler: BackgroundScheduler | None = None
 15:         self._job_id = "automation_tick"
 16:         self._lock = threading.Lock()
 17:         self._logger = logger or logging.getLogger(__name__)
 18: 
 19:     def _run_tick_safe(self) -> None:
 20:         """Execute tick callable while guarding against uncaught exceptions."""
 21:         try:
 22:             self._tick_callable()
 23:         except Exception as exc:  # pragma: no cover - exercised via tests
 24:             self._logger.error(
 25:                 "[scheduler] Automation tick raised exception: %s",
 26:                 exc,
 27:                 exc_info=True,
 28:             )
 29: 
 30:     def _get_interval_seconds(self) -> int:
 31:         settings = self._settings_store.read()
 32:         raw = settings.get("poll_interval_seconds", 120)
 33: 
 34:         try:
 35:             interval = int(raw)
 36:         except (TypeError, ValueError):
 37:             interval = 120
 38: 
 39:         if interval < 15:
 40:             interval = 15
 41: 
 42:         return interval
 43: 
 44:     def start(self) -> None:
 45:         with self._lock:
 46:             if self._scheduler is not None:
 47:                 self._logger.warning("[scheduler] Scheduler already started, ignoring duplicate start() call")
 48:                 return
 49: 
 50:             self._scheduler = BackgroundScheduler(daemon=True)
 51:             self._scheduler.start()
 52:             self._logger.info("[scheduler] BackgroundScheduler started successfully")
 53:             self._schedule_or_reschedule_locked()
 54:             self._logger.info("[scheduler] Triggering immediate first tick")
 55:             self._run_tick_safe()
 56: 
 57:     def _schedule_or_reschedule_locked(self) -> None:
 58:         if self._scheduler is None:
 59:             self._logger.warning("[scheduler] Cannot schedule job: scheduler is None")
 60:             return
 61: 
 62:         interval = self._get_interval_seconds()
 63: 
 64:         existing_job = self._scheduler.get_job(self._job_id)
 65:         if existing_job is not None:
 66:             self._logger.debug("[scheduler] Removing existing job before rescheduling")
 67:             existing_job.remove()
 68: 
 69:         self._scheduler.add_job(
 70:             func=self._run_tick_safe,
 71:             trigger="interval",
 72:             seconds=interval,
 73:             id=self._job_id,
 74:             replace_existing=True,
 75:             max_instances=1,
 76:             coalesce=True,
 77:         )
 78:         self._logger.info("[scheduler] Job scheduled with interval=%d seconds", interval)
 79: 
 80:     def reschedule(self) -> None:
 81:         with self._lock:
 82:             if self._scheduler is None:
 83:                 self._logger.debug("[scheduler] Reschedule called but scheduler not started (normal if SCHEDULER_ENABLED=false)")
 84:                 return
 85:             
 86:             self._logger.info("[scheduler] Rescheduling automation job")
 87:             self._schedule_or_reschedule_locked()
 88: 
 89:     def stop(self) -> None:
 90:         with self._lock:
 91:             if self._scheduler is None:
 92:                 self._logger.debug("[scheduler] Stop called but scheduler already stopped")
 93:                 return
 94: 
 95:             self._logger.info("[scheduler] Shutting down scheduler")
 96:             self._scheduler.shutdown(wait=False)
 97:             self._scheduler = None
 98: 
 99:     def is_running(self) -> bool:
100:         with self._lock:
101:             if self._scheduler is None:
102:                 return False
103: 
104:             return getattr(self._scheduler, "running", False)
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
119:                   <div class="col-12 col-md-4">
120:                     <label class="form-label" for="off_repeat_count">Répétitions arrêt OFF</label>
121:                     <input
122:                       class="form-control"
123:                       id="off_repeat_count"
124:                       name="off_repeat_count"
125:                       value="{{ settings.get('off_repeat_count', 1) }}"
126:                       inputmode="numeric"
127:                       min="1"
128:                       max="10"
129:                     />
130:                     <div class="form-text">Nombre total d'ordres OFF envoyés (1 = aucune répétition).</div>
131:                   </div>
132: 
133:                   <div class="col-12 col-md-4">
134:                     <label class="form-label" for="off_repeat_interval_seconds">Intervalle entre OFF (s)</label>
135:                     <input
136:                       class="form-control"
137:                       id="off_repeat_interval_seconds"
138:                       name="off_repeat_interval_seconds"
139:                       value="{{ settings.get('off_repeat_interval_seconds', 10) }}"
140:                       inputmode="numeric"
141:                       min="1"
142:                     />
143:                     <div class="form-text">Délai entre deux OFF successifs (ex. 10 s).</div>
144:                   </div>
145:                 </div>
146: 
147:                 <div class="row g-3">
148:                   <div class="col-12 col-md-6">
149:                     <label class="form-label" for="hysteresis_celsius">Hystérésis (°C)</label>
150:                     <input
151:                       class="form-control"
152:                       id="hysteresis_celsius"
153:                       name="hysteresis_celsius"
154:                       value="{{ settings.get('hysteresis_celsius') }}"
155:                     />
156:                   </div>
157: 
158:                   <div class="col-12 col-md-6">
159:                     <label class="form-label" for="api_quota_warning_threshold">Seuil d'alerte quota</label>
160:                     <input
161:                       class="form-control"
162:                       id="api_quota_warning_threshold"
163:                       name="api_quota_warning_threshold"
164:                       type="number"
165:                       min="0"
166:                       max="10000"
167:                       value="{{ settings.get('api_quota_warning_threshold', quota_warning_threshold) }}"
168:                     />
169:                     <div class="form-text">Bannière d'alerte lorsque les appels restants passent sous cette valeur.</div>
170:                   </div>
171: 
172:                   <div class="col-12 col-md-6">
173:                     <label class="form-label" for="timezone">Fuseau horaire</label>
174:                     <input
175:                       class="form-control"
176:                       id="timezone"
177:                       name="timezone"
178:                       value="{{ settings.get('timezone', 'Europe/Paris') }}"
179:                       placeholder="Europe/Paris"
180:                       autocapitalize="none"
181:                       autocomplete="off"
182:                       spellcheck="false"
183:                     />
184:                     <div class="form-text">Utilisé pour interpréter les fenêtres horaires (identifiant IANA, ex: Europe/Paris, UTC).</div>
185:                   </div>
186: 
187:                   <div class="col-12">
188:                     <div class="form-check mb-2">
189:                       <input
190:                         class="form-check-input"
191:                         type="checkbox"
192:                         id="turn_off_outside_windows"
193:                         name="turn_off_outside_windows"
194:                         {% if settings.get('turn_off_outside_windows') %}checked{% endif %}
195:                       />
196:                       <label class="form-check-label" for="turn_off_outside_windows">Éteindre en dehors des fenêtres horaires</label>
197:                     </div>
198:                   </div>
199: 
200:                   <div class="col-12 col-md-6">
201:                     <label class="form-label" for="meter_device_id">ID du capteur Meter</label>
202:                     <input class="form-control" id="meter_device_id" name="meter_device_id" value="{{ settings.get('meter_device_id') }}" />
203:                   </div>
204: 
205:                   <div class="col-12 col-md-6">
206:                     <label class="form-label" for="aircon_device_id">ID de la télécommande IR</label>
207:                     <input class="form-control" id="aircon_device_id" name="aircon_device_id" value="{{ settings.get('aircon_device_id') }}" />
208:                     <div class="form-text">Identifiant de la télécommande infrarouge (remoteType: Air Conditioner).</div>
209:                   </div>
210:                 </div>
211: 
212:                 <hr />
213: 
214:                 <div class="section-heading mb-2">
215:                   <label class="form-label mb-0">Fenêtre horaire</label>
216:                   <span class="badge rounded-pill bg-secondary-subtle text-secondary-emphasis">optimisé mobile</span>
217:                 </div>
218:                 <div class="small text-muted mb-2">Sélectionnez les jours puis choisissez l'heure de début et de fin (format 24h).</div>
219:                 <div class="border rounded-3 p-3 mb-3 time-window-card">
220:                   <div class="row g-3">
221:                     <div class="col-12">
222:                       <label class="form-label d-block">Jours</label>
223:                       <div class="d-flex flex-wrap gap-2">
224:                         {% for day in day_choices %}
225:                           <div class="form-check form-check-inline day-chip">
226:                             <input
227:                               class="btn-check"
228:                               type="checkbox"
229:                               id="day_{{ day.value }}"
230:                               name="time_window_days"
231:                               value="{{ day.value }}"
232:                               aria-describedby="time_window_days_summary"
233:                               {% if day.value in time_window_form['days'] %}checked{% endif %}
234:                             />
235:                             <label class="btn btn-outline-primary btn-sm" for="day_{{ day.value }}">{{ day.label }}</label>
236:                           </div>
237:                         {% endfor %}
238:                       </div>
239:                       <div id="time_window_days_summary" class="form-text" aria-live="polite">
240:                         {{ time_window_form['days'] | length }} jour(s) sélectionné(s).
241:                       </div>
242:                     </div>
243:                     <div class="col-6">
244:                       <label class="form-label" for="time_window_start">Début</label>
245:                       <select class="form-select" id="time_window_start" name="time_window_start" aria-describedby="time_window_help">
246:                         <option value="">Choisir…</option>
247:                         {% for choice in time_choices %}
248:                           <option value="{{ choice }}" {% if time_window_form['start'] == choice %}selected{% endif %}>{{ choice }}</option>
249:                         {% endfor %}
250:                       </select>
251:                     </div>
252:                     <div class="col-6">
253:                       <label class="form-label" for="time_window_end">Fin</label>
254:                       <select class="form-select" id="time_window_end" name="time_window_end" aria-describedby="time_window_help">
255:                         <option value="">Choisir…</option>
256:                         {% for choice in time_choices %}
257:                           <option value="{{ choice }}" {% if time_window_form['end'] == choice %}selected{% endif %}>{{ choice }}</option>
258:                         {% endfor %}
259:                       </select>
260:                     </div>
261:                     <div class="col-12">
262:                       <div id="time_window_help" class="form-text">
263:                         Astuce : si aucun jour n'est sélectionné, la fenêtre horaire est considérée comme inactive.
264:                       </div>
265:                     </div>
266:                   </div>
267:                 </div>
268: 
269:                 <hr />
270: 
271:                 {% set winter_profile = settings.get('winter', {}) %}
272:                 <h2 class="h6">Profil hiver</h2>
273:                 <div class="row g-2 mb-3">
274:                   <div class="col-4">
275:                     <label class="form-label" for="winter_min_temp">Min.</label>
276:                     <select class="form-select" id="winter_min_temp" name="winter_min_temp">
277:                       {% for choice in temp_choices %}
278:                         <option value="{{ choice.value }}" {% if (winter_profile.get('min_temp') | float) == choice.value %}selected{% endif %}>
279:                           {{ choice.label }}°C
280:                         </option>
281:                       {% endfor %}
282:                     </select>
283:                   </div>
284:                   <div class="col-4">
285:                     <label class="form-label" for="winter_max_temp">Max.</label>
286:                     <select class="form-select" id="winter_max_temp" name="winter_max_temp">
287:                       {% for choice in temp_choices %}
288:                         <option value="{{ choice.value }}" {% if (winter_profile.get('max_temp') | float) == choice.value %}selected{% endif %}>
289:                           {{ choice.label }}°C
290:                         </option>
291:                       {% endfor %}
292:                     </select>
293:                   </div>
294:                   <div class="col-4">
295:                     <label class="form-label" for="winter_target_temp">Cible</label>
296:                     <select class="form-select" id="winter_target_temp" name="winter_target_temp">
297:                       {% for choice in temp_choices %}
298:                         <option value="{{ choice.value }}" {% if (winter_profile.get('target_temp') | float) == choice.value %}selected{% endif %}>
299:                           {{ choice.label }}°C
300:                         </option>
301:                       {% endfor %}
302:                     </select>
303:                   </div>
304:                   <div class="col-6">
305:                     <label class="form-label" for="winter_ac_mode">Mode clim</label>
306:                     <select class="form-select" id="winter_ac_mode" name="winter_ac_mode">
307:                       {% for choice in ac_mode_choices %}
308:                         <option value="{{ choice.value }}" {% if (winter_profile.get('ac_mode') | int) == choice.value %}selected{% endif %}>
309:                           {{ choice.label }}
310:                         </option>
311:                       {% endfor %}
312:                     </select>
313:                   </div>
314:                   <div class="col-6">
315:                     <label class="form-label" for="winter_fan_speed">Vitesse ventilateur</label>
316:                     <select class="form-select" id="winter_fan_speed" name="winter_fan_speed">
317:                       {% for choice in fan_speed_choices %}
318:                         <option value="{{ choice.value }}" {% if (winter_profile.get('fan_speed') | int) == choice.value %}selected{% endif %}>
319:                           {{ choice.label }}
320:                         </option>
321:                       {% endfor %}
322:                     </select>
323:                   </div>
324:                 </div>
325: 
326:                 {% set summer_profile = settings.get('summer', {}) %}
327:                 <h2 class="h6">Profil été</h2>
328:                 <div class="row g-2">
329:                   <div class="col-4">
330:                     <label class="form-label" for="summer_min_temp">Min.</label>
331:                     <select class="form-select" id="summer_min_temp" name="summer_min_temp">
332:                       {% for choice in temp_choices %}
333:                         <option value="{{ choice.value }}" {% if (summer_profile.get('min_temp') | float) == choice.value %}selected{% endif %}>
334:                           {{ choice.label }}°C
335:                         </option>
336:                       {% endfor %}
337:                     </select>
338:                   </div>
339:                   <div class="col-4">
340:                     <label class="form-label" for="summer_max_temp">Max.</label>
341:                     <select class="form-select" id="summer_max_temp" name="summer_max_temp">
342:                       {% for choice in temp_choices %}
343:                         <option value="{{ choice.value }}" {% if (summer_profile.get('max_temp') | float) == choice.value %}selected{% endif %}>
344:                           {{ choice.label }}°C
345:                         </option>
346:                       {% endfor %}
347:                     </select>
348:                   </div>
349:                   <div class="col-4">
350:                     <label class="form-label" for="summer_target_temp">Cible</label>
351:                     <select class="form-select" id="summer_target_temp" name="summer_target_temp">
352:                       {% for choice in temp_choices %}
353:                         <option value="{{ choice.value }}" {% if (summer_profile.get('target_temp') | float) == choice.value %}selected{% endif %}>
354:                           {{ choice.label }}°C
355:                         </option>
356:                       {% endfor %}
357:                     </select>
358:                   </div>
359:                   <div class="col-6">
360:                     <label class="form-label" for="summer_ac_mode">Mode clim</label>
361:                     <select class="form-select" id="summer_ac_mode" name="summer_ac_mode">
362:                       {% for choice in ac_mode_choices %}
363:                         <option value="{{ choice.value }}" {% if (summer_profile.get('ac_mode') | int) == choice.value %}selected{% endif %}>
364:                           {{ choice.label }}
365:                         </option>
366:                       {% endfor %}
367:                     </select>
368:                   </div>
369:                   <div class="col-6">
370:                     <label class="form-label" for="summer_fan_speed">Vitesse ventilateur</label>
371:                     <select class="form-select" id="summer_fan_speed" name="summer_fan_speed">
372:                       {% for choice in fan_speed_choices %}
373:                         <option value="{{ choice.value }}" {% if (summer_profile.get('fan_speed') | int) == choice.value %}selected{% endif %}>
374:                           {{ choice.label }}
375:                         </option>
376:                       {% endfor %}
377:                     </select>
378:                   </div>
379:                 </div>
380: 
381:                 <div class="mt-4">
382:                   <button class="btn btn-primary w-100 w-md-auto" type="submit">Enregistrer les réglages</button>
383:                 </div>
384: 
385:                 <hr class="my-4" />
386: 
387:                 <h2 class="h6">Webhooks IFTTT (Priorité)</h2>
388:                 <p class="small text-muted">
389:                   Renseignez les URLs des webhooks IFTTT pour déclencher vos scènes via le cloud. Les webhooks sont prioritaires sur les scènes SwitchBot natives.
390:                 </p>
391:                 <div class="row g-3 mb-4">
392:                   {% for key in aircon_scene_keys %}
393:                     <div class="col-12 col-md-6">
394:                       <label class="form-label" for="webhook_{{ key }}_url">{{ aircon_scene_labels[key] }}</label>
395:                       <input
396:                         class="form-control"
397:                         id="webhook_{{ key }}_url"
398:                         name="webhook_{{ key }}_url"
399:                         value="{{ ifttt_webhooks[key] }}"
400:                         placeholder="https://maker.ifttt.com/trigger/..."
401:                         type="url"
402:                       />
403:                       {% if missing_webhooks[key] %}
404:                         <div class="form-text text-warning">Non configuré (fallback vers scène SwitchBot)</div>
405:                       {% else %}
406:                         <div class="form-text text-success">Prêt</div>
407:                       {% endif %}
408:                     </div>
409:                   {% endfor %}
410:                 </div>
411: 
412:                 <h2 class="h6">Scènes favorites SwitchBot (Fallback)</h2>
413:                 <p class="small text-muted">
414:                   Renseignez les IDs des scènes favorites (SwitchBot → Scenes). Elles servent de fallback si les webhooks IFTTT échouent ou ne sont pas configurés.
415:                 </p>
416:                 <div class="row g-3">
417:                   {% for key in aircon_scene_keys %}
418:                     <div class="col-12 col-md-6 col-lg-3">
419:                       <label class="form-label" for="scene_{{ key }}_id">{{ aircon_scene_labels[key] }}</label>
420:                       <input
421:                         class="form-control"
422:                         id="scene_{{ key }}_id"
423:                         name="scene_{{ key }}_id"
424:                         value="{{ aircon_scenes[key] }}"
425:                         placeholder="UUID scène"
426:                       />
427:                       {% if missing_scenes[key] %}
428:                         <div class="form-text text-warning">Non configuré</div>
429:                       {% else %}
430:                         <div class="form-text text-success">Prêt</div>
431:                       {% endif %}
432:                     </div>
433:                   {% endfor %}
434:                 </div>
435:               </form>
436:             </div>
437:           </div>
438:         </div>
439: 
440:         <div class="col-12 col-xl-3">
441:           <div class="card h-100">
442:             <div class="card-header">Résumé rapide</div>
443:             <div class="card-body">
444:               <dl class="row mb-0 small">
445:                 <dt class="col-7">Mode actuel</dt>
446:                 <dd class="col-5 text-end text-capitalize">{{ settings.get('mode', 'winter') }}</dd>
447: 
448:                 <dt class="col-7">Seuil alerte quota</dt>
449:                 <dd class="col-5 text-end">{{ quota_warning_threshold }}</dd>
450: 
451:                 <dt class="col-7">Fenêtre horaire</dt>
452:                 <dd class="col-5 text-end">
453:                   {% if time_window_form['days'] %}
454:                     {{ time_window_form['start'] or '--:--' }} → {{ time_window_form['end'] or '--:--' }}
455:                   {% else %}
456:                     Aucune
457:                   {% endif %}
458:                 </dd>
459: 
460:                 <dt class="col-7">Webhooks IFTTT</dt>
461:                 <dd class="col-5 text-end">
462:                   {{ configured_webhooks_count }} / {{ aircon_scene_keys | length }}
463:                 </dd>
464: 
465:                 <dt class="col-7">Scènes configurées</dt>
466:                 <dd class="col-5 text-end">
467:                   {{ configured_scenes_count }} / {{ aircon_scene_keys | length }}
468:                 </dd>
469:               </dl>
470:               <div class="mt-3">
471:                 <p class="small text-muted mb-2">Besoin d'un rafraîchissement ?</p>
472:                 <a class="btn btn-outline-light w-100" href="{{ url_for('dashboard.index') }}">Voir l'état en temps réel</a>
473:               </div>
474:             </div>
475:           </div>
476:         </div>
477:       </div>
478:     </div>
479:     
480:     {% include '_footer_nav.html' %}
481:     
482:     <script src="{{ url_for('static', filename='js/alerts.js') }}"></script>
483:     <script src="{{ url_for('static', filename='js/settings.js') }}"></script>
484:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
485:     <script src="{{ url_for('static', filename='js/bottom-nav.js') }}"></script>
486:     <script src="{{ url_for('static', filename='js/performance-optimizer.js') }}"></script>
487:   </body>
488: </html>
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
203:         logger=app.logger,
204:     )
205: 
206:     app.extensions["settings_store"] = settings_store
207:     app.extensions["state_store"] = state_store
208:     app.extensions["switchbot_client"] = client
209:     app.extensions["ifttt_client"] = ifttt_client
210:     app.extensions["automation_service"] = automation_service
211:     app.extensions["scheduler_service"] = scheduler_service
212:     app.extensions["quota_tracker"] = quota_tracker
213:     if history_service:
214:         app.extensions["history_service"] = history_service
215: 
216:     app.register_blueprint(dashboard_bp)
217: 
218:     _mark_temperature_stale(app, state_store, reason="app_start")
219:     try:
220:         automation_service.poll_meter()
221:     except Exception as exc:  # pragma: no cover - defensive safeguard
222:         app.logger.warning("Initial meter poll failed: %s", exc)
223: 
224:     scheduler_enabled = os.environ.get("SCHEDULER_ENABLED", "true").strip().lower()
225: 
226:     if scheduler_enabled == "true":
227:         is_flask_dev_reloader_parent = (
228:             os.environ.get("FLASK_DEBUG", "").strip().lower() not in ("", "0", "false")
229:             and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
230:             and not os.environ.get("SERVER_SOFTWARE")
231:         )
232: 
233:         if is_flask_dev_reloader_parent:
234:             app.logger.info("[scheduler] Skipping start in Flask development reloader parent process")
235:         else:
236:             scheduler_service.start()
237:             app.logger.info("[scheduler] APScheduler enabled and started")
238:     else:
239:         app.logger.info("[scheduler] APScheduler disabled via SCHEDULER_ENABLED=false")
240: 
241:     return app
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
 439:     settings["hysteresis_celsius"] = _as_float(
 440:         request.form.get("hysteresis_celsius"),
 441:         default=float(settings.get("hysteresis_celsius", 0.3) or 0.3),
 442:         minimum=0.0,
 443:         maximum=5.0,
 444:     )
 445: 
 446:     settings["command_cooldown_seconds"] = _as_int(
 447:         request.form.get("command_cooldown_seconds"),
 448:         default=int(settings.get("command_cooldown_seconds", 180) or 180),
 449:         minimum=0,
 450:         maximum=3600,
 451:     )
 452:     settings["action_on_cooldown_seconds"] = _as_int(
 453:         request.form.get("action_on_cooldown_seconds"),
 454:         default=int(settings.get("action_on_cooldown_seconds", 0) or 0),
 455:         minimum=0,
 456:         maximum=3600,
 457:     )
 458:     settings["action_off_cooldown_seconds"] = _as_int(
 459:         request.form.get("action_off_cooldown_seconds"),
 460:         default=int(settings.get("action_off_cooldown_seconds", 0) or 0),
 461:         minimum=0,
 462:         maximum=3600,
 463:     )
 464:     settings["off_repeat_count"] = _as_int(
 465:         request.form.get("off_repeat_count"),
 466:         default=int(settings.get("off_repeat_count", 1) or 1),
 467:         minimum=1,
 468:         maximum=10,
 469:     )
 470:     settings["off_repeat_interval_seconds"] = _as_int(
 471:         request.form.get("off_repeat_interval_seconds"),
 472:         default=int(settings.get("off_repeat_interval_seconds", 10) or 10),
 473:         minimum=1,
 474:         maximum=600,
 475:     )
 476: 
 477:     settings["turn_off_outside_windows"] = _as_bool(request.form.get("turn_off_outside_windows"))
 478: 
 479:     timezone_raw = request.form.get("timezone")
 480:     if timezone_raw is None:
 481:         settings.setdefault("timezone", DEFAULT_TIMEZONE)
 482:     else:
 483:         requested_timezone = str(timezone_raw).strip() or DEFAULT_TIMEZONE
 484:         try:
 485:             ZoneInfo(requested_timezone)
 486:         except ZoneInfoNotFoundError:
 487:             flash(
 488:                 "Fuseau horaire invalide : utilisez un identifiant IANA (ex: Europe/Paris, UTC).",
 489:                 "error",
 490:             )
 491:         else:
 492:             settings["timezone"] = requested_timezone
 493: 
 494:     settings["api_quota_warning_threshold"] = _as_int(
 495:         request.form.get("api_quota_warning_threshold"),
 496:         default=int(settings.get("api_quota_warning_threshold", DEFAULT_QUOTA_WARNING_THRESHOLD) or DEFAULT_QUOTA_WARNING_THRESHOLD),
 497:         minimum=0,
 498:         maximum=10_000,
 499:     )
 500: 
 501:     settings["meter_device_id"] = str(request.form.get("meter_device_id", "")).strip()
 502:     settings["aircon_device_id"] = str(request.form.get("aircon_device_id", "")).strip()
 503: 
 504:     time_window_days_raw = request.form.getlist("time_window_days")
 505:     time_window_start = request.form.get("time_window_start", "").strip()
 506:     time_window_end = request.form.get("time_window_end", "").strip()
 507: 
 508:     if time_window_days_raw or time_window_start or time_window_end:
 509:         try:
 510:             parsed_days = [
 511:                 int(token.strip())
 512:                 for token in time_window_days_raw
 513:                 if token.strip() != ""
 514:             ]
 515:         except ValueError:
 516:             parsed_days = []
 517: 
 518:         parsed_days = sorted({day for day in parsed_days if 0 <= day <= 6})
 519: 
 520:         if parsed_days and time_window_start and time_window_end:
 521:             settings["time_windows"] = [
 522:                 {
 523:                     "days": parsed_days,
 524:                     "start": time_window_start,
 525:                     "end": time_window_end,
 526:                 }
 527:             ]
 528:         else:
 529:             flash(
 530:                 "Fenêtre horaire invalide : les jours doivent être compris entre 0 et 6 et les heures de début/fin sont obligatoires.",
 531:                 "error",
 532:             )
 533:     else:
 534:         settings["time_windows"] = []
 535: 
 536:     for key in ("winter", "summer"):
 537:         profile = settings.get(key, {})
 538:         if not isinstance(profile, dict):
 539:             profile = {}
 540: 
 541:         profile["min_temp"] = _as_float(request.form.get(f"{key}_min_temp"), default=float(profile.get("min_temp", 0.0) or 0.0))
 542:         profile["max_temp"] = _as_float(request.form.get(f"{key}_max_temp"), default=float(profile.get("max_temp", 0.0) or 0.0))
 543:         profile["target_temp"] = _as_float(request.form.get(f"{key}_target_temp"), default=float(profile.get("target_temp", 0.0) or 0.0))
 544:         profile["fan_speed"] = _as_int(request.form.get(f"{key}_fan_speed"), default=int(profile.get("fan_speed", 3) or 3), minimum=1, maximum=4)
 545:         profile["ac_mode"] = _as_int(request.form.get(f"{key}_ac_mode"), default=int(profile.get("ac_mode", 5 if key == "winter" else 2) or 0), minimum=0, maximum=5)
 546: 
 547:         settings[key] = profile
 548: 
 549:     updated_aircon_scenes: dict[str, str] = {}
 550:     for key in AIRCON_SCENE_KEYS:
 551:         updated_aircon_scenes[key] = str(
 552:             request.form.get(f"scene_{key}_id", current_aircon_scenes.get(key, ""))
 553:         ).strip()
 554: 
 555:     settings["aircon_scenes"] = updated_aircon_scenes
 556: 
 557:     current_webhooks = _extract_ifttt_webhooks(settings)
 558:     updated_webhooks: dict[str, str] = {}
 559:     for key in AIRCON_SCENE_KEYS:
 560:         updated_webhooks[key] = str(
 561:             request.form.get(f"webhook_{key}_url", current_webhooks.get(key, ""))
 562:         ).strip()
 563: 
 564:     settings["ifttt_webhooks"] = updated_webhooks
 565: 
 566:     settings_store.write(settings)
 567:     scheduler_service.reschedule()
 568: 
 569:     flash("Paramètres enregistrés.")
 570:     return redirect(url_for("dashboard.index"))
 571: 
 572: 
 573: @dashboard_bp.route("/actions/run_once", methods=["GET", "POST"])
 574: def run_once() -> Any:
 575:     """Execute a single automation cycle manually.
 576: 
 577:     Triggers the automation service to run one complete cycle
 578:     of temperature monitoring and device control.
 579: 
 580:     Returns:
 581:         Redirect to home page with success flash message
 582:     """
 583:     automation_service = current_app.extensions["automation_service"]
 584: 
 585:     automation_service.run_once()
 586:     flash("Cycle d'automatisation exécuté.")
 587:     return redirect(url_for("dashboard.index"))
 588: 
 589: 
 590: @dashboard_bp.post("/actions/aircon_off")
 591: def aircon_off() -> Any:
 592:     return _execute_aircon_action(
 593:         "off",
 594:         state_reason="manual_off",
 595:         flash_label="Climatisation arrêtée.",
 596:         assumed_power="off",
 597:     )
 598: 
 599: 
 600: def _execute_aircon_action(
 601:     action_key: str,
 602:     *,
 603:     state_reason: str,
 604:     flash_label: str,
 605:     assumed_power: str = "unknown",
 606: ) -> Any:
 607:     settings_store = current_app.extensions["settings_store"]
 608:     state_store = current_app.extensions["state_store"]
 609:     client = current_app.extensions["switchbot_client"]
 610:     ifttt_client = current_app.extensions["ifttt_client"]
 611: 
 612:     settings = settings_store.read()
 613:     webhooks = _extract_ifttt_webhooks(settings)
 614:     scenes = _extract_aircon_scenes(settings)
 615:     aircon_id = str(settings.get("aircon_device_id", "")).strip()
 616: 
 617:     webhook_url = webhooks.get(action_key, "").strip()
 618:     scene_id = scenes.get(action_key, "").strip()
 619: 
 620:     if webhook_url:
 621:         try:
 622:             ifttt_client.trigger_webhook(webhook_url)
 623:             state = state_store.read()
 624:             state["assumed_aircon_power"] = assumed_power
 625:             state["assumed_aircon_mode"] = None
 626:             state["assumed_aircon_parameter"] = None
 627:             state["last_action"] = f"ifttt_webhook({action_key}) ({state_reason})"
 628:             state["last_action_at"] = _utc_now_iso()
 629:             state["last_error"] = None
 630:             state_store.write(state)
 631:             flash(flash_label)
 632:             return redirect(url_for("dashboard.index"))
 633:         except IFTTTWebhookError as exc:
 634:             current_app.logger.warning(f"IFTTT webhook failed for {action_key}: {exc}. Falling back to scene.")
 635: 
 636:     if scene_id:
 637:         try:
 638:             client.run_scene(scene_id)
 639:             state = state_store.read()
 640:             state["assumed_aircon_power"] = assumed_power
 641:             state["assumed_aircon_mode"] = None
 642:             state["assumed_aircon_parameter"] = None
 643:             state["last_action"] = f"scene({scene_id}) ({state_reason})"
 644:             state["last_action_at"] = _utc_now_iso()
 645:             state["last_error"] = None
 646:             state_store.write(state)
 647:             flash(flash_label)
 648:             return redirect(url_for("dashboard.index"))
 649:         except SwitchBotApiError as exc:
 650:             if not aircon_id:
 651:                 state = state_store.read()
 652:                 state["last_error"] = str(exc)
 653:                 state_store.write(state)
 654:                 flash(str(exc), "error")
 655:                 return redirect(url_for("dashboard.index"))
 656:             current_app.logger.warning(f"Scene execution failed for {action_key}: {exc}. Falling back to direct command.")
 657: 
 658:     if not webhook_url and not scene_id:
 659:         action_label = AIRCON_SCENE_LABELS.get(action_key, action_key)
 660:         flash(f"Aucun webhook ou scène configuré pour {action_label}", "error")
 661:         return redirect(url_for("dashboard.index"))
 662: 
 663:     if action_key == "off":
 664:         if not aircon_id:
 665:             flash("aircon_device_id manquant", "error")
 666:             return redirect(url_for("dashboard.index"))
 667:         try:
 668:             client.send_command(aircon_id, command="turnOff", parameter="default", command_type="command")
 669:             state = state_store.read()
 670:             state["assumed_aircon_power"] = "off"
 671:             state["assumed_aircon_mode"] = None
 672:             state["assumed_aircon_parameter"] = None
 673:             state["last_action"] = f"turnOff ({state_reason})"
 674:             state["last_action_at"] = _utc_now_iso()
 675:             state["last_error"] = None
 676:             state_store.write(state)
 677:             flash(flash_label)
 678:             return redirect(url_for("dashboard.index"))
 679:         except SwitchBotApiError as exc:
 680:             state = state_store.read()
 681:             state["last_error"] = str(exc)
 682:             state_store.write(state)
 683:             flash(str(exc), "error")
 684:             return redirect(url_for("dashboard.index"))
 685:     else:
 686:         flash(f"Impossible d'exécuter l'action {action_key} : aucune méthode disponible", "error")
 687:         return redirect(url_for("dashboard.index"))
 688: 
 689: 
 690: @dashboard_bp.post("/actions/aircon_on")
 691: def aircon_on() -> Any:
 692:     """Route to the current mode scene for backward compatibility."""
 693:     settings_store = current_app.extensions["settings_store"]
 694:     settings = settings_store.read()
 695:     mode = str(settings.get("mode", "winter")).strip().lower()
 696:     scene_key = mode if mode in AIRCON_SCENE_KEYS else "winter"
 697:     return _execute_aircon_action(
 698:         scene_key,
 699:         state_reason=f"manual_{scene_key}",
 700:         flash_label=f"Action {scene_key} exécutée.",
 701:     )
 702: 
 703: 
 704: @dashboard_bp.post("/actions/aircon_on_winter")
 705: def aircon_on_winter() -> Any:
 706:     return _execute_aircon_action(
 707:         "winter",
 708:         state_reason="manual_winter",
 709:         flash_label="Mode hiver activé.",
 710:         assumed_power="on",
 711:     )
 712: 
 713: 
 714: @dashboard_bp.post("/actions/aircon_on_summer")
 715: def aircon_on_summer() -> Any:
 716:     return _execute_aircon_action(
 717:         "summer",
 718:         state_reason="manual_summer",
 719:         flash_label="Mode été activé.",
 720:         assumed_power="on",
 721:     )
 722: 
 723: 
 724: @dashboard_bp.post("/actions/aircon_on_fan")
 725: def aircon_on_fan() -> Any:
 726:     return _execute_aircon_action(
 727:         "fan",
 728:         state_reason="manual_fan",
 729:         flash_label="Mode ventilateur activé.",
 730:         assumed_power="on",
 731:     )
 732: 
 733: 
 734: @dashboard_bp.get("/devices")
 735: def devices() -> str:
 736:     client = current_app.extensions["switchbot_client"]
 737: 
 738:     data = None
 739:     error = None
 740: 
 741:     try:
 742:         data = client.get_devices()
 743:     except SwitchBotApiError as exc:
 744:         error = str(exc)
 745: 
 746:     return render_template("devices.html", data=data, error=error)
 747: 
 748: 
 749: @dashboard_bp.post("/actions/quick_off")
 750: def quick_off() -> Any:
 751:     settings_store = current_app.extensions["settings_store"]
 752:     
 753:     settings = settings_store.read()
 754:     settings["automation_enabled"] = False
 755:     settings_store.write(settings)
 756:     
 757:     return _execute_aircon_action(
 758:         "off",
 759:         state_reason="quick_off",
 760:         flash_label="Automatisation désactivée et climatisation éteinte.",
 761:         assumed_power="off",
 762:     )
 763: 
 764: 
 765: @dashboard_bp.get("/history")
 766: def history_page() -> str:
 767:     return render_template("history.html")
 768: 
 769: 
 770: @dashboard_bp.get("/actions")
 771: def actions_page() -> str:
 772:     settings_store = current_app.extensions["settings_store"]
 773:     state_store = current_app.extensions["state_store"]
 774:     
 775:     try:
 776:         settings = settings_store.read()
 777:     except StoreError:
 778:         settings = {}
 779:     
 780:     try:
 781:         state = state_store.read()
 782:     except StoreError:
 783:         state = {}
 784:     
 785:     # Get scene configuration for status display
 786:     aircon_scenes = settings.get("aircon_scenes", {})
 787:     missing_scenes = {
 788:         key: not aircon_scenes.get(key)
 789:         for key in ["winter", "summer", "fan", "off"]
 790:     }
 791:     
 792:     return render_template(
 793:         "actions.html",
 794:         settings=settings,
 795:         state=state,
 796:         missing_scenes=missing_scenes,
 797:     )
 798: 
 799: 
 800: @dashboard_bp.get("/history/api/data")
 801: def history_api_data() -> Any:
 802:     history_service = current_app.extensions.get("history_service")
 803:     if not history_service:
 804:         # Return mock data when service is not available
 805:         import random
 806:         
 807:         end = dt.datetime.now(dt.timezone.utc)
 808:         start = end - dt.timedelta(hours=6)
 809:         mock_data = []
 810:         
 811:         current = start
 812:         while current <= end:
 813:             mock_data.append({
 814:                 "timestamp": current.isoformat() + "Z",
 815:                 "temperature": round(20 + random.random() * 10, 1),
 816:                 "humidity": round(40 + random.random() * 20, 1),
 817:                 "assumed_aircon_power": random.choice(["on", "off", "unknown"]),
 818:                 "last_action": random.choice(["automation_winter_on", "automation_summer_on", "automation_winter_off", None]),
 819:                 "api_requests_today": random.randint(100, 200),
 820:                 "error_count": random.randint(0, 2)
 821:             })
 822:             current += timedelta(minutes=5)
 823:         
 824:         return {
 825:             "data": mock_data,
 826:             "start": start.isoformat() + "Z",
 827:             "end": end.isoformat() + "Z",
 828:             "granularity": "minute",
 829:             "metrics": ["temperature", "humidity", "assumed_aircon_power"],
 830:             "count": len(mock_data),
 831:             "mock": True
 832:         }
 833: 
 834:     try:
 835:         # Parse query parameters
 836:         start_str = request.args.get("start")
 837:         end_str = request.args.get("end")
 838:         metrics_param = request.args.get("metrics")
 839:         granularity = request.args.get("granularity", "minute")
 840:         limit = int(request.args.get("limit", 1000))
 841: 
 842:         # Parse metrics parameter (can be comma-separated string or list)
 843:         metrics = []
 844:         if metrics_param:
 845:             if isinstance(metrics_param, str):
 846:                 metrics = [m.strip() for m in metrics_param.split(",") if m.strip()]
 847:             else:
 848:                 metrics = metrics_param
 849: 
 850:         # Default to last 6 hours if no time range specified
 851:         if not start_str or not end_str:
 852:             end = dt.datetime.now(dt.timezone.utc)
 853:             start = end - dt.timedelta(hours=6)
 854:         else:
 855:             start = dt.datetime.fromisoformat(start_str.replace("Z", "+00:00"))
 856:             end = dt.datetime.fromisoformat(end_str.replace("Z", "+00:00"))
 857: 
 858:         # Validate granularity
 859:         valid_granularities = ["minute", "5min", "15min", "hour"]
 860:         if granularity not in valid_granularities:
 861:             granularity = "minute"
 862: 
 863:         # Get historical data
 864:         data = history_service.get_history(start, end, metrics, granularity, limit)
 865:         
 866:         # Return empty data structure if no data found
 867:         if not data:
 868:             return {
 869:                 "data": [],
 870:                 "start": start.isoformat(),
 871:                 "end": end.isoformat(),
 872:                 "granularity": granularity,
 873:                 "metrics": metrics or ["timestamp", "temperature", "humidity", "assumed_aircon_power"],
 874:                 "count": 0,
 875:                 "message": "No historical data available yet"
 876:             }
 877:         
 878:         return {
 879:             "data": data,
 880:             "start": start.isoformat(),
 881:             "end": end.isoformat(),
 882:             "granularity": granularity,
 883:             "metrics": metrics or ["timestamp", "temperature", "humidity", "assumed_aircon_power"],
 884:             "count": len(data),
 885:         }
 886: 
 887:     except ValueError as exc:
 888:         return {"error": f"Invalid parameters: {exc}"}, 400
 889:     except Exception as exc:
 890:         current_app.logger.error(f"[history] API error: {exc}")
 891:         # Return empty data structure on error to avoid breaking the frontend
 892:         return {
 893:             "data": [],
 894:             "start": start.isoformat() if 'start' in locals() else dt.datetime.now(dt.timezone.utc).isoformat(),
 895:             "end": end.isoformat() if 'end' in locals() else dt.datetime.now(dt.timezone.utc).isoformat(),
 896:             "granularity": "minute",
 897:             "metrics": ["timestamp", "temperature", "humidity", "assumed_aircon_power"],
 898:             "count": 0,
 899:             "message": "Error retrieving data"
 900:         }
 901: 
 902: 
 903: @dashboard_bp.get("/history/api/aggregates")
 904: def history_api_aggregates() -> Any:
 905:     """API endpoint for aggregated statistics."""
 906:     history_service = current_app.extensions.get("history_service")
 907:     if not history_service:
 908:         # Return mock aggregates when service is not available
 909:         import random
 910:         
 911:         return {
 912:             "period_hours": 6,
 913:             "aggregates": {
 914:                 "total_records": random.randint(50, 100),
 915:                 "avg_temperature": round(20 + random.random() * 10, 1),
 916:                 "min_temperature": round(18 + random.random() * 2, 1),
 917:                 "max_temperature": round(28 + random.random() * 2, 1),
 918:                 "avg_humidity": round(40 + random.random() * 20, 1),
 919:                 "min_humidity": round(35 + random.random() * 5, 1),
 920:                 "max_humidity": round(60 + random.random() * 5, 1),
 921:                 "common_aircon_state": random.choice(["on", "off"]),
 922:                 "distinct_actions": random.randint(2, 4),
 923:                 "total_errors": random.randint(0, 5),
 924:                 "max_api_requests": random.randint(150, 250)
 925:             },
 926:             "mock": True
 927:         }
 928: 
 929:     try:
 930:         period_hours = int(request.args.get("period_hours", 1))
 931:         if period_hours < 1 or period_hours > 24:
 932:             period_hours = 1
 933: 
 934:         aggregates = history_service.get_aggregates(period_hours)
 935:         
 936:         # Return empty aggregates if no data
 937:         if not aggregates:
 938:             return {
 939:                 "period_hours": period_hours,
 940:                 "aggregates": {
 941:                     "total_records": 0,
 942:                     "avg_temperature": 0,
 943:                     "min_temperature": 0,
 944:                     "max_temperature": 0,
 945:                     "avg_humidity": 0,
 946:                     "min_humidity": 0,
 947:                     "max_humidity": 0,
 948:                     "common_aircon_state": "unknown",
 949:                     "distinct_actions": 0,
 950:                     "total_errors": 0,
 951:                     "max_api_requests": 0
 952:                 },
 953:                 "message": "No historical data available yet"
 954:             }
 955:         
 956:         return {
 957:             "period_hours": period_hours,
 958:             "aggregates": aggregates,
 959:         }
 960: 
 961:     except Exception as exc:
 962:         current_app.logger.error(f"[history] Aggregates API error: {exc}")
 963:         # Return empty aggregates on error to avoid breaking the frontend
 964:         return {
 965:             "period_hours": 1,
 966:             "aggregates": {
 967:                 "total_records": 0,
 968:                 "avg_temperature": 0,
 969:                 "min_temperature": 0,
 970:                 "max_temperature": 0,
 971:                 "avg_humidity": 0,
 972:                 "min_humidity": 0,
 973:                 "max_humidity": 0,
 974:                 "common_aircon_state": "unknown",
 975:                 "distinct_actions": 0,
 976:                 "total_errors": 0,
 977:                 "max_api_requests": 0
 978:             },
 979:             "message": "Error retrieving data"
 980:         }
 981: 
 982: 
 983: @dashboard_bp.get("/history/api/latest")
 984: def history_api_latest() -> Any:
 985:     history_service = current_app.extensions.get("history_service")
 986:     if not history_service:
 987:         # Return mock latest records when service is not available
 988:         import random
 989:         
 990:         mock_latest = []
 991:         for i in range(10):
 992:             timestamp = dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=i * 5)
 993:             mock_latest.append({
 994:                 "id": i + 1,
 995:                 "timestamp": timestamp.isoformat() + "Z",
 996:                 "temperature": round(20 + random.random() * 10, 1),
 997:                 "humidity": round(40 + random.random() * 20, 1),
 998:                 "assumed_aircon_power": random.choice(["on", "off", "unknown"]),
 999:                 "last_action": random.choice(["automation_winter_on", "automation_summer_on", "automation_winter_off", None]),
1000:                 "error_count": random.randint(0, 2),
1001:                 "metadata": {
1002:                     "last_read_at": timestamp.isoformat() + "Z",
1003:                     "automation_active": random.choice([True, False])
1004:                 }
1005:             })
1006:         
1007:         return {
1008:             "latest": mock_latest,
1009:             "count": len(mock_latest),
1010:             "mock": True
1011:         }
1012: 
1013:     try:
1014:         limit = int(request.args.get("limit", 10))
1015:         if limit < 1 or limit > 100:
1016:             limit = 10
1017: 
1018:         latest = history_service.get_latest_records(limit)
1019:         
1020:         # Return empty latest if no data
1021:         if not latest:
1022:             return {
1023:                 "latest": [],
1024:                 "count": 0,
1025:                 "message": "No historical data available yet"
1026:             }
1027:         
1028:         return {
1029:             "latest": latest,
1030:             "count": len(latest),
1031:         }
1032: 
1033:     except Exception as exc:
1034:         current_app.logger.error(f"[history] Latest API error: {exc}")
1035:         # Return empty latest on error to avoid breaking the frontend
1036:         return {
1037:             "latest": [],
1038:             "count": 0,
1039:             "message": "Error retrieving data"
1040:         }
```
