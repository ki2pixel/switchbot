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
      core-web-vitals-tester.js
      devices.js
      history.js
      loaders.js
      micro-interactions-test.js
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

## File: switchbot_dashboard/static/js/core-web-vitals-tester.js
```javascript
  1: /**
  2:  * Core Web Vitals Testing Script
  3:  * Tests and validates performance metrics for Phase 5 optimizations
  4:  */
  5: (function() {
  6:   'use strict';
  7:   
  8:   class CoreWebVitalsTester {
  9:     constructor() {
 10:       this.metrics = {
 11:         lcp: 0,
 12:         fid: 0,
 13:         cls: 0,
 14:         ttfb: 0,
 15:         fcp: 0,
 16:         loadTime: 0
 17:       };
 18:       
 19:       this.thresholds = {
 20:         lcp: { good: 2500, needsImprovement: 4000 },
 21:         fid: { good: 100, needsImprovement: 300 },
 22:         cls: { good: 0.1, needsImprovement: 0.25 },
 23:         ttfb: { good: 800, needsImprovement: 1800 },
 24:         fcp: { good: 1800, needsImprovement: 3000 }
 25:       };
 26:       
 27:       this.testResults = [];
 28:       this.init();
 29:     }
 30:     
 31:     init() {
 32:       console.log('🧪 Core Web Vitals Tester initialized');
 33:       this.setupPerformanceObservers();
 34:       this.measurePageLoad();
 35:       this.runAutomatedTests();
 36:       this.generateReport();
 37:     }
 38:     
 39:     setupPerformanceObservers() {
 40:       // LCP Observer
 41:       if ('PerformanceObserver' in window) {
 42:         const lcpObserver = new PerformanceObserver((list) => {
 43:           const entries = list.getEntries();
 44:           const lastEntry = entries[entries.length - 1];
 45:           this.metrics.lcp = lastEntry.renderTime || lastEntry.loadTime;
 46:           console.log('🎨 LCP measured:', this.metrics.lcp.toFixed(2), 'ms');
 47:         });
 48:         lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
 49:         
 50:         // FID Observer
 51:         const fidObserver = new PerformanceObserver((list) => {
 52:           const entries = list.getEntries();
 53:           entries.forEach(entry => {
 54:             this.metrics.fid = entry.processingStart - entry.startTime;
 55:             console.log('⚡ FID measured:', this.metrics.fid.toFixed(2), 'ms');
 56:           });
 57:         });
 58:         fidObserver.observe({ entryTypes: ['first-input'] });
 59:         
 60:         // CLS Observer
 61:         let clsValue = 0;
 62:         const clsObserver = new PerformanceObserver((list) => {
 63:           list.getEntries().forEach(entry => {
 64:             if (!entry.hadRecentInput) {
 65:               clsValue += entry.value;
 66:             }
 67:           });
 68:           this.metrics.cls = clsValue;
 69:           console.log('📐 CLS measured:', this.metrics.cls.toFixed(3));
 70:         });
 71:         clsObserver.observe({ entryTypes: ['layout-shift'] });
 72:         
 73:         // FCP Observer
 74:         const fcpObserver = new PerformanceObserver((list) => {
 75:           const entries = list.getEntries();
 76:           entries.forEach(entry => {
 77:             if (entry.name === 'first-contentful-paint') {
 78:               this.metrics.fcp = entry.startTime;
 79:               console.log('🖼️ FCP measured:', this.metrics.fcp.toFixed(2), 'ms');
 80:             }
 81:           });
 82:         });
 83:         fcpObserver.observe({ entryTypes: ['paint'] });
 84:       }
 85:     }
 86:     
 87:     measurePageLoad() {
 88:       window.addEventListener('load', () => {
 89:         setTimeout(() => {
 90:           const navigation = performance.getEntriesByType('navigation')[0];
 91:           if (navigation) {
 92:             this.metrics.ttfb = navigation.responseStart - navigation.requestStart;
 93:             this.metrics.loadTime = navigation.loadEventEnd - navigation.startTime;
 94:             
 95:             console.log('🌐 TTFB measured:', this.metrics.ttfb.toFixed(2), 'ms');
 96:             console.log('⏱️ Load Time measured:', this.metrics.loadTime.toFixed(2), 'ms');
 97:           }
 98:           
 99:           // Run tests after page is fully loaded
100:           setTimeout(() => {
101:             this.runPerformanceTests();
102:           }, 1000);
103:         }, 0);
104:       });
105:     }
106:     
107:     runAutomatedTests() {
108:       console.log('🔬 Running automated performance tests...');
109:       
110:       // Test 1: Critical CSS Inlining
111:       this.testCriticalCSSInlining();
112:       
113:       // Test 2: Resource Loading
114:       this.testResourceLoading();
115:       
116:       // Test 3: Font Loading
117:       this.testFontLoading();
118:       
119:       // Test 4: Image Optimization
120:       this.testImageOptimization();
121:       
122:       // Test 5: JavaScript Execution
123:       this.testJavaScriptExecution();
124:     }
125:     
126:     testCriticalCSSInlining() {
127:       const criticalCSS = document.querySelector('style');
128:       const hasCriticalCSS = criticalCSS && criticalCSS.textContent.includes('Critical CSS');
129:       
130:       this.addTestResult({
131:         name: 'Critical CSS Inlining',
132:         passed: hasCriticalCSS,
133:         details: hasCriticalCSS ? '✅ Critical CSS found inline' : '❌ Critical CSS not found',
134:         impact: hasCriticalCSS ? 'Positive impact on LCP' : 'Negative impact on LCP'
135:       });
136:     }
137:     
138:     testResourceLoading() {
139:       const preloads = document.querySelectorAll('link[rel="preload"]');
140:       const preconnects = document.querySelectorAll('link[rel="preconnect"]');
141:       
142:       this.addTestResult({
143:         name: 'Resource Loading Optimization',
144:         passed: preloads.length > 0 && preconnects.length > 0,
145:         details: `Found ${preloads.length} preloads and ${preconnects.length} preconnects`,
146:         impact: 'Reduces network latency for critical resources'
147:       });
148:     }
149:     
150:     testFontLoading() {
151:       const fontPreload = document.querySelector('link[href*="fonts.googleapis.com"]');
152:       const fontDisplay = document.querySelector('style')?.textContent.includes('font-display: swap');
153:       
154:       this.addTestResult({
155:         name: 'Font Loading Optimization',
156:         passed: fontPreload && fontDisplay,
157:         details: fontPreload ? '✅ Font preloading enabled' : '❌ Font preloading missing',
158:         impact: 'Improves FCP and reduces FOIT/FOUT'
159:       });
160:     }
161:     
162:     testImageOptimization() {
163:       const images = document.querySelectorAll('img');
164:       const optimizedImages = Array.from(images).filter(img => 
165:         img.loading || img.style.width || img.style.height
166:       );
167:       
168:       this.addTestResult({
169:         name: 'Image Optimization',
170:         passed: optimizedImages.length === images.length,
171:         details: `${optimizedImages.length}/${images.length} images optimized`,
172:         impact: 'Reduces CLS and improves LCP'
173:       });
174:     }
175:     
176:     testJavaScriptExecution() {
177:       const scripts = document.querySelectorAll('script');
178:       const hasAdvancedOptimizer = Array.from(scripts).some(script => 
179:         script.src.includes('advanced-optimizer.js')
180:       );
181:       
182:       this.addTestResult({
183:         name: 'JavaScript Optimization',
184:         passed: hasAdvancedOptimizer,
185:         details: hasAdvancedOptimizer ? '✅ Advanced optimizer loaded' : '❌ Advanced optimizer missing',
186:         impact: 'Improves FID and main thread performance'
187:       });
188:     }
189:     
190:     runPerformanceTests() {
191:       console.log('🚀 Running performance tests...');
192:       
193:       // Test DOM readiness
194:       this.testDOMReadiness();
195:       
196:       // Test rendering performance
197:       this.testRenderingPerformance();
198:       
199:       // Test memory usage
200:       this.testMemoryUsage();
201:       
202:       // Test network performance
203:       this.testNetworkPerformance();
204:     }
205:     
206:     testDOMReadiness() {
207:       const domContentLoaded = performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart;
208:       const isOptimal = domContentLoaded < 1000;
209:       
210:       this.addTestResult({
211:         name: 'DOM Readiness',
212:         passed: isOptimal,
213:         details: `DOM Content Loaded: ${domContentLoaded.toFixed(2)}ms`,
214:         impact: isOptimal ? 'Good DOM parsing performance' : 'Slow DOM parsing detected'
215:       });
216:     }
217:     
218:     testRenderingPerformance() {
219:       const renderTime = performance.timing.loadEventEnd - performance.timing.domContentLoadedEventEnd;
220:       const isOptimal = renderTime < 500;
221:       
222:       this.addTestResult({
223:         name: 'Rendering Performance',
224:         passed: isOptimal,
225:         details: `Render time: ${renderTime.toFixed(2)}ms`,
226:         impact: isOptimal ? 'Good rendering performance' : 'Slow rendering detected'
227:       });
228:     }
229:     
230:     testMemoryUsage() {
231:       if (performance.memory) {
232:         const memoryUsage = performance.memory.usedJSHeapSize / 1048576; // MB
233:         const isOptimal = memoryUsage < 50;
234:         
235:         this.addTestResult({
236:           name: 'Memory Usage',
237:           passed: isOptimal,
238:           details: `Memory usage: ${memoryUsage.toFixed(2)}MB`,
239:           impact: isOptimal ? 'Good memory efficiency' : 'High memory usage detected'
240:         });
241:       }
242:     }
243:     
244:     testNetworkPerformance() {
245:       const resources = performance.getEntriesByType('resource');
246:       const totalSize = resources.reduce((sum, resource) => sum + (resource.transferSize || 0), 0);
247:       const totalSizeKB = totalSize / 1024;
248:       const isOptimal = totalSizeKB < 500;
249:       
250:       this.addTestResult({
251:         name: 'Network Performance',
252:         passed: isOptimal,
253:         details: `Total transfer size: ${totalSizeKB.toFixed(2)}KB`,
254:         impact: isOptimal ? 'Good network efficiency' : 'Large payload detected'
255:       });
256:     }
257:     
258:     addTestResult(result) {
259:       this.testResults.push(result);
260:       console.log(`${result.passed ? '✅' : '❌'} ${result.name}: ${result.details}`);
261:     }
262:     
263:     evaluateMetrics() {
264:       const evaluation = {};
265:       
266:       Object.keys(this.metrics).forEach(metric => {
267:         const value = this.metrics[metric];
268:         const threshold = this.thresholds[metric];
269:         
270:         if (threshold) {
271:           if (value <= threshold.good) {
272:             evaluation[metric] = 'good';
273:           } else if (value <= threshold.needsImprovement) {
274:             evaluation[metric] = 'needs-improvement';
275:           } else {
276:             evaluation[metric] = 'poor';
277:           }
278:         } else {
279:           evaluation[metric] = 'measured';
280:         }
281:       });
282:       
283:       return evaluation;
284:     }
285:     
286:     generateReport() {
287:       // Wait for all metrics to be collected
288:       setTimeout(() => {
289:         console.log('\n📊 CORE WEB VITALS REPORT');
290:         console.log('================================');
291:         
292:         const evaluation = this.evaluateMetrics();
293:         
294:         console.log('\n🎯 Metrics:');
295:         Object.keys(this.metrics).forEach(metric => {
296:           const value = this.metrics[metric];
297:           const status = evaluation[metric];
298:           const emoji = status === 'good' ? '🟢' : status === 'needs-improvement' ? '🟡' : '🔴';
299:           console.log(`${emoji} ${metric.toUpperCase()}: ${value.toFixed(2)}${metric === 'cls' ? '' : 'ms'} (${status})`);
300:         });
301:         
302:         console.log('\n🧪 Test Results:');
303:         this.testResults.forEach(test => {
304:           const emoji = test.passed ? '✅' : '❌';
305:           console.log(`${emoji} ${test.name}: ${test.details}`);
306:         });
307:         
308:         console.log('\n📈 Summary:');
309:         const passedTests = this.testResults.filter(t => t.passed).length;
310:         const totalTests = this.testResults.length;
311:         console.log(`Tests passed: ${passedTests}/${totalTests} (${((passedTests/totalTests)*100).toFixed(1)}%)`);
312:         
313:         const goodMetrics = Object.values(evaluation).filter(s => s === 'good').length;
314:         const totalMetrics = Object.keys(evaluation).length;
315:         console.log(`Good metrics: ${goodMetrics}/${totalMetrics} (${((goodMetrics/totalMetrics)*100).toFixed(1)}%)`);
316:         
317:         // Overall assessment
318:         const overallScore = ((passedTests/totalTests) * 0.5 + (goodMetrics/totalMetrics) * 0.5) * 100;
319:         console.log(`\n🏆 Overall Performance Score: ${overallScore.toFixed(1)}%`);
320:         
321:         if (overallScore >= 90) {
322:           console.log('🎉 EXCELLENT: Phase 5 optimizations successful!');
323:         } else if (overallScore >= 75) {
324:           console.log('👍 GOOD: Phase 5 optimizations mostly successful');
325:         } else if (overallScore >= 60) {
326:           console.log('⚠️ NEEDS IMPROVEMENT: Some optimizations need attention');
327:         } else {
328:           console.log('❌ POOR: Significant optimization issues detected');
329:         }
330:         
331:         console.log('\n💡 Recommendations:');
332:         this.generateRecommendations(evaluation);
333:         
334:         // Store results for later analysis
335:         this.storeResults();
336:         
337:       }, 3000); // Wait 3 seconds for all metrics
338:     }
339:     
340:     generateRecommendations(evaluation) {
341:       const recommendations = [];
342:       
343:       if (evaluation.lcp === 'poor') {
344:         recommendations.push('• Optimize largest contentful paint: reduce image sizes, improve server response time');
345:       }
346:       
347:       if (evaluation.fid === 'poor') {
348:         recommendations.push('• Reduce first input delay: minimize JavaScript execution time, use code splitting');
349:       }
350:       
351:       if (evaluation.cls === 'poor') {
352:         recommendations.push('• Fix cumulative layout shift: specify image dimensions, avoid dynamic content insertion');
353:       }
354:       
355:       if (evaluation.ttfb === 'poor') {
356:         recommendations.push('• Improve time to first byte: optimize server response, use CDN');
357:       }
358:       
359:       if (recommendations.length === 0) {
360:         recommendations.push('• All Core Web Vitals are within good thresholds!');
361:       }
362:       
363:       recommendations.forEach(rec => console.log(rec));
364:     }
365:     
366:     storeResults() {
367:       const results = {
368:         timestamp: new Date().toISOString(),
369:         url: window.location.href,
370:         metrics: this.metrics,
371:         evaluation: this.evaluateMetrics(),
372:         testResults: this.testResults,
373:         userAgent: navigator.userAgent,
374:         viewport: {
375:           width: window.innerWidth,
376:           height: window.innerHeight
377:         }
378:       };
379:       
380:       // Store in localStorage for analysis
381:       localStorage.setItem('core-web-vitals-results', JSON.stringify(results));
382:       
383:       // Send to console for easy copying
384:       console.log('\n📋 Results stored in localStorage under key: core-web-vitals-results');
385:     }
386:     
387:     // Public API
388:     getResults() {
389:       return {
390:         metrics: this.metrics,
391:         evaluation: this.evaluateMetrics(),
392:         testResults: this.testResults
393:       };
394:     }
395:     
396:     runManualTest() {
397:       console.log('🔧 Running manual performance test...');
398:       this.runPerformanceTests();
399:       setTimeout(() => this.generateReport(), 1000);
400:     }
401:   }
402:   
403:   // Initialize tester
404:   window.CoreWebVitalsTester = CoreWebVitalsTester;
405:   window.coreWebVitalsTester = new CoreWebVitalsTester();
406:   
407:   // Expose manual testing
408:   window.runPerformanceTest = () => {
409:     window.coreWebVitalsTester.runManualTest();
410:   };
411:   
412:   console.log('🧪 Core Web Vitals Tester ready. Run window.runPerformanceTest() for manual testing.');
413: })();
```

## File: switchbot_dashboard/static/js/micro-interactions-test.js
```javascript
  1: /**
  2:  * Micro-interactions Test Script
  3:  * Tests the CSS animations and micro-interactions
  4:  * Used for validation during development
  5:  */
  6: 
  7: class MicroInteractionsTest {
  8:   constructor() {
  9:     this.testResults = [];
 10:     this.animationClasses = [
 11:       'sb-pulse',
 12:       'sb-success-flash',
 13:       'sb-temp-change',
 14:       'sb-data-update',
 15:       'sb-loading',
 16:       'sb-cooldown'
 17:     ];
 18:   }
 19: 
 20:   // Test if animations are properly disabled with prefers-reduced-motion
 21:   testReducedMotion() {
 22:     const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
 23:     const testElement = document.createElement('div');
 24:     testElement.className = 'sb-pulse';
 25:     document.body.appendChild(testElement);
 26: 
 27:     const computedStyle = window.getComputedStyle(testElement);
 28:     const animationDuration = computedStyle.animationDuration;
 29:     
 30:     const isReduced = motionQuery.matches;
 31:     const isDisabled = animationDuration === '0.01s' || animationDuration === '0.01ms';
 32:     
 33:     this.testResults.push({
 34:       test: 'prefers-reduced-motion',
 35:       passed: isReduced ? isDisabled : true,
 36:       details: `Motion preference: ${isReduced}, Animation duration: ${animationDuration}`
 37:     });
 38: 
 39:     document.body.removeChild(testElement);
 40:     return isReduced ? isDisabled : true;
 41:   }
 42: 
 43:   // Test GPU acceleration
 44:   testGPUAcceleration() {
 45:     const testElement = document.createElement('div');
 46:     testElement.className = 'sb-gpu-accelerated';
 47:     document.body.appendChild(testElement);
 48: 
 49:     const computedStyle = window.getComputedStyle(testElement);
 50:     const transform = computedStyle.transform;
 51:     const willChange = computedStyle.willChange;
 52:     
 53:     const hasGPUAcceleration = transform !== 'none' || willChange.includes('transform');
 54:     
 55:     this.testResults.push({
 56:       test: 'gpu-acceleration',
 57:       passed: hasGPUAcceleration,
 58:       details: `Transform: ${transform}, Will-change: ${willChange}`
 59:     });
 60: 
 61:     document.body.removeChild(testElement);
 62:     return hasGPUAcceleration;
 63:   }
 64: 
 65:   // Test if CSS variables are properly defined
 66:   testCSSVariables() {
 67:     const testElement = document.createElement('div');
 68:     document.body.appendChild(testElement);
 69: 
 70:     const computedStyle = window.getComputedStyle(testElement);
 71:     const requiredVariables = [
 72:       '--sb-scale-hover',
 73:       '--sb-scale-active',
 74:       '--sb-translate-hover',
 75:       '--sb-transition-fast',
 76:       '--sb-transition-normal'
 77:     ];
 78: 
 79:     const missingVars = requiredVariables.filter(varName => {
 80:       const value = computedStyle.getPropertyValue(varName);
 81:       return !value || value.trim() === '';
 82:     });
 83: 
 84:     this.testResults.push({
 85:       test: 'css-variables',
 86:       passed: missingVars.length === 0,
 87:       details: `Missing variables: ${missingVars.join(', ')}`
 88:     });
 89: 
 90:     document.body.removeChild(testElement);
 91:     return missingVars.length === 0;
 92:   }
 93: 
 94:   // Test animation performance
 95:   testAnimationPerformance() {
 96:     const testElement = document.createElement('div');
 97:     testElement.className = 'sb-pulse sb-gpu-accelerated';
 98:     testElement.style.position = 'absolute';
 99:     testElement.style.left = '-9999px';
100:     document.body.appendChild(testElement);
101: 
102:     const startTime = performance.now();
103:     
104:     // Trigger animation
105:     testElement.classList.add('sb-pulse');
106:     
107:     // Measure after animation should start
108:     setTimeout(() => {
109:       const endTime = performance.now();
110:       const duration = endTime - startTime;
111:       
112:       this.testResults.push({
113:         test: 'animation-performance',
114:         passed: duration < 50, // Should start within 50ms
115:         details: `Animation start time: ${duration.toFixed(2)}ms`
116:       });
117: 
118:       document.body.removeChild(testElement);
119:     }, 10);
120: 
121:     return true;
122:   }
123: 
124:   // Test focus accessibility
125:   testFocusAccessibility() {
126:     const testElement = document.createElement('button');
127:     testElement.className = 'sb-focus-enhanced';
128:     testElement.textContent = 'Test Button';
129:     document.body.appendChild(testElement);
130: 
131:     testElement.focus();
132:     const computedStyle = window.getComputedStyle(testElement);
133:     const outline = computedStyle.outline;
134:     const outlineOffset = computedStyle.outlineOffset;
135:     
136:     const hasFocusStyle = outline !== 'none' && outlineOffset !== '0px';
137:     
138:     this.testResults.push({
139:       test: 'focus-accessibility',
140:       passed: hasFocusStyle,
141:       details: `Outline: ${outline}, Outline-offset: ${outlineOffset}`
142:     });
143: 
144:     document.body.removeChild(testElement);
145:     return hasFocusStyle;
146:   }
147: 
148:   // Run all tests
149:   runAllTests() {
150:     console.log('🧪 Running Micro-interactions Tests...');
151:     
152:     this.testReducedMotion();
153:     this.testGPUAcceleration();
154:     this.testCSSVariables();
155:     this.testAnimationPerformance();
156:     this.testFocusAccessibility();
157: 
158:     const passedTests = this.testResults.filter(result => result.passed).length;
159:     const totalTests = this.testResults.length;
160: 
161:     console.log(`📊 Test Results: ${passedTests}/${totalTests} tests passed`);
162:     
163:     this.testResults.forEach(result => {
164:       const icon = result.passed ? '✅' : '❌';
165:       console.log(`${icon} ${result.test}: ${result.details}`);
166:     });
167: 
168:     return {
169:       passed: passedTests,
170:       total: totalTests,
171:       success: passedTests === totalTests,
172:       results: this.testResults
173:     };
174:   }
175: }
176: 
177: // Auto-run tests if in development mode
178: if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
179:   document.addEventListener('DOMContentLoaded', () => {
180:     const tester = new MicroInteractionsTest();
181:     setTimeout(() => tester.runAllTests(), 1000);
182:   });
183: }
184: 
185: // Export for manual testing
186: window.MicroInteractionsTest = MicroInteractionsTest;
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

## File: switchbot_dashboard/templates/actions.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>Actions · SwitchBot Dashboard</title>
  7:     <link
  8:       href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
  9:       rel="stylesheet"
 10:       integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDS..."
 11:       crossorigin="anonymous"
 12:     />
 13:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 14:     <link rel="stylesheet" href="{{ url_for('static', filename='css/actions.css') }}" />
 15:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 16:     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
 17:   </head>
 18:   <body class="sb-dark">
 19:     <div class="container py-4">
 20:       <header class="page-header mb-4">
 21:         <div class="page-header-main">
 22:           <h1 class="h3 mb-0">Actions Rapides</h1>
 23:           <p class="page-subtitle text-muted mb-0">
 24:             Déclenchez manuellement les scènes et commandes de climatisation.
 25:           </p>
 26:         </div>
 27:       </header>
 28: 
 29:       {% with messages = get_flashed_messages(with_categories=true) %}
 30:         {% if messages %}
 31:           <div class="mb-3" aria-live="polite" aria-atomic="true">
 32:             {% for category, message in messages %}
 33:               {% if category == 'error' %}
 34:                 <div class="alert alert-danger" role="alert" data-auto-dismiss="6000">
 35:                   {{ message }}
 36:                 </div>
 37:               {% else %}
 38:                 <div class="alert alert-success" role="alert" data-auto-dismiss="6000">
 39:                   {{ message }}
 40:                 </div>
 41:               {% endif %}
 42:             {% endfor %}
 43:           </div>
 44:         {% endif %}
 45:       {% endwith %}
 46: 
 47:       <!-- Actions principales -->
 48:       <section class="actions-section mb-4">
 49:         <div class="card sb-card">
 50:           <div class="card-header">
 51:             <h5 class="card-title mb-0">Actions principales</h5>
 52:             <small class="text-muted">Déclenchements manuels de l'automatisation</small>
 53:           </div>
 54:           <div class="card-body">
 55:             <div class="row g-3">
 56:               <div class="col-12 col-md-6">
 57:                 <form method="post" action="{{ url_for('dashboard.run_once') }}" data-loader>
 58:                   <button class="btn btn-primary w-100 action-btn rounded-m shadow-l" type="submit">
 59:                     <i class="fas fa-play me-2"></i>
 60:                     Exécuter une fois
 61:                   </button>
 62:                 </form>
 63:               </div>
 64:               <div class="col-12 col-md-6">
 65:                 <form method="post" action="{{ url_for('dashboard.quick_off') }}" data-loader>
 66:                   <button class="btn btn-secondary w-100 action-btn rounded-m shadow-l" type="submit">
 67:                     <i class="fas fa-stop me-2"></i>
 68:                     Arrêt rapide
 69:                   </button>
 70:                 </form>
 71:               </div>
 72:             </div>
 73:           </div>
 74:         </div>
 75:       </section>
 76: 
 77:       <!-- Scènes de climatisation -->
 78:       <section class="scenes-section mb-4">
 79:         <div class="card sb-card">
 80:           <div class="card-header">
 81:             <h5 class="card-title mb-0">Scènes de climatisation</h5>
 82:             <small class="text-muted">Déclenchez les scènes SwitchBot configurées</small>
 83:           </div>
 84:           <div class="card-body">
 85:             <div class="row g-3">
 86:               <div class="col-12 col-md-6">
 87:                 <form method="post" action="{{ url_for('dashboard.aircon_on_winter') }}" data-loader>
 88:                   <button
 89:                     class="btn btn-outline-success w-100 scene-btn rounded-m shadow-l"
 90:                     type="submit"
 91:                     aria-label="Activer la scène hiver SwitchBot"
 92:                     {% if missing_scenes['winter'] %}disabled aria-disabled="true"{% endif %}>
 93:                     <div class="scene-content">
 94:                       <div class="scene-icon scene-icon--winter" aria-hidden="true">
 95:                         <svg viewBox="0 0 24 24" role="img" focusable="false">
 96:                           <circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.6" fill="none" />
 97:                           <line x1="12" y1="3" x2="12" y2="1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
 98:                           <line x1="12" y1="23" x2="12" y2="21" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
 99:                           <line x1="4.22" y1="4.22" x2="2.81" y2="2.81" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
100:                           <line x1="21.19" y1="21.19" x2="19.78" y2="19.78" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
101:                           <line x1="3" y1="12" x2="1" y2="12" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
102:                           <line x1="23" y1="12" x2="21" y2="12" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
103:                           <line x1="4.22" y1="19.78" x2="2.81" y2="21.19" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
104:                           <line x1="21.19" y1="2.81" x2="19.78" y2="4.22" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
105:                         </svg>
106:                       </div>
107:                       <div class="scene-info">
108:                         <div class="scene-title">Climatisation ON – Hiver</div>
109:                         <div class="scene-status small {% if missing_scenes['winter'] %}text-warning{% else %}text-muted{% endif %}">
110:                           {% if missing_scenes['winter'] %}
111:                             Scène manquante
112:                           {% else %}
113:                             Scène configurée
114:                           {% endif %}
115:                         </div>
116:                       </div>
117:                     </div>
118:                   </button>
119:                 </form>
120:               </div>
121:               
122:               <div class="col-12 col-md-6">
123:                 <form method="post" action="{{ url_for('dashboard.aircon_on_summer') }}" data-loader>
124:                   <button
125:                     class="btn btn-outline-success w-100 scene-btn rounded-m shadow-l"
126:                     type="submit"
127:                     aria-label="Activer la scène été SwitchBot"
128:                     {% if missing_scenes['summer'] %}disabled aria-disabled="true"{% endif %}>
129:                     <div class="scene-content">
130:                       <div class="scene-icon scene-icon--summer" aria-hidden="true">
131:                         <svg viewBox="0 0 24 24" role="img" focusable="false">
132:                           <path
133:                             d="M12 2v20M4.93 4.93l14.14 14.14M2 12h20M4.93 19.07 19.07 4.93"
134:                             stroke="currentColor"
135:                             stroke-width="1.6"
136:                             stroke-linecap="round"
137:                             stroke-linejoin="round"
138:                             fill="none"
139:                           />
140:                           <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.6" fill="none" />
141:                         </svg>
142:                       </div>
143:                       <div class="scene-info">
144:                         <div class="scene-title">Climatisation ON – Été</div>
145:                         <div class="scene-status small {% if missing_scenes['summer'] %}text-warning{% else %}text-muted{% endif %}">
146:                           {% if missing_scenes['summer'] %}
147:                             Scène manquante
148:                           {% else %}
149:                             Scène configurée
150:                           {% endif %}
151:                         </div>
152:                       </div>
153:                     </div>
154:                   </button>
155:                 </form>
156:               </div>
157:               
158:               <div class="col-12 col-md-6">
159:                 <form method="post" action="{{ url_for('dashboard.aircon_on_fan') }}" data-loader>
160:                   <button
161:                     class="btn btn-outline-success w-100 scene-btn rounded-m shadow-l"
162:                     type="submit"
163:                     aria-label="Activer la scène ventilation SwitchBot"
164:                     {% if missing_scenes['fan'] %}disabled aria-disabled="true"{% endif %}>
165:                     <div class="scene-content">
166:                       <div class="scene-icon scene-icon--fan" aria-hidden="true">
167:                         <svg viewBox="0 0 24 24" role="img" focusable="false">
168:                           <path
169:                             d="M12 12c1.2-2.7 3.7-5.5 7.5-4.5 2.2.6 2.5 3.2.6 4.2-1.9 1-4.8.2-8.1.3M12 12c2.7 1.2 5.5 3.7 4.5 7.5-.6 2.2-3.2 2.5-4.2.6-1-1.9-.2-4.8-.3-8.1M12 12c-1.2 2.7-3.7 5.5-7.5 4.5-2.2-.6-2.5-3.2-.6-4.2 1.9-1 4.8-.2 8.1-.3"
170:                             stroke="currentColor"
171:                             stroke-width="1.6"
172:                             stroke-linecap="round"
173:                             stroke-linejoin="round"
174:                             fill="none"
175:                           />
176:                           <circle cx="12" cy="12" r="1.8" fill="currentColor" />
177:                         </svg>
178:                       </div>
179:                       <div class="scene-info">
180:                         <div class="scene-title">Climatisation ON – Mode neutre</div>
181:                         <div class="scene-status small {% if missing_scenes['fan'] %}text-warning{% else %}text-muted{% endif %}">
182:                           {% if missing_scenes['fan'] %}
183:                             Scène manquante
184:                           {% else %}
185:                             Scène configurée
186:                           {% endif %}
187:                         </div>
188:                       </div>
189:                     </div>
190:                   </button>
191:                 </form>
192:               </div>
193:               
194:               <div class="col-12 col-md-6">
195:                 <form method="post" action="{{ url_for('dashboard.aircon_off') }}" data-loader>
196:                   <button
197:                     class="btn btn-outline-danger w-100 scene-btn rounded-m shadow-l"
198:                     type="submit"
199:                     aria-label="Éteindre le climatiseur via la scène SwitchBot"
200:                     {% if missing_scenes['off'] %}disabled aria-disabled="true"{% endif %}>
201:                     <div class="scene-content">
202:                       <div class="scene-icon scene-icon--off" aria-hidden="true">
203:                         <svg viewBox="0 0 24 24" role="img" focusable="false">
204:                           <path
205:                             d="M12 2v10M7 4.5A9 9 0 1 0 17 4.5"
206:                             stroke="currentColor"
207:                             stroke-width="1.6"
208:                             stroke-linecap="round"
209:                             stroke-linejoin="round"
210:                             fill="none"
211:                           />
212:                         </svg>
213:                       </div>
214:                       <div class="scene-info">
215:                         <div class="scene-title">Climatisation OFF</div>
216:                         <div class="scene-status small {% if missing_scenes['off'] %}text-warning{% else %}text-muted{% endif %}">
217:                           {% if missing_scenes['off'] %}
218:                             Scène manquante
219:                           {% else %}
220:                             Scène configurée
221:                           {% endif %}
222:                         </div>
223:                       </div>
224:                     </div>
225:                   </button>
226:                 </form>
227:               </div>
228:             </div>
229:           </div>
230:         </div>
231:       </section>
232: 
233:       <!-- Informations d'état -->
234:       <section class="status-info">
235:         <div class="card sb-card">
236:           <div class="card-header">
237:             <h5 class="card-title mb-0">État actuel</h5>
238:           </div>
239:           <div class="card-body">
240:             <div class="row g-3">
241:               <div class="col-12 col-md-6">
242:                 <div class="status-item">
243:                   <div class="status-label">Température</div>
244:                   <div class="status-value">{{ state.get('last_temperature') }}</div>
245:                 </div>
246:               </div>
247:               <div class="col-12 col-md-6">
248:                 <div class="status-item">
249:                   <div class="status-label">Climatisation</div>
250:                   <div class="status-value">
251:                     {% if state.get('assumed_aircon_power') == 'on' %}
252:                       <span class="text-success">ON</span>
253:                     {% else %}
254:                       <span class="text-secondary">OFF</span>
255:                     {% endif %}
256:                   </div>
257:                 </div>
258:               </div>
259:             </div>
260:           </div>
261:         </div>
262:       </section>
263:     </div>
264:     
265:     {% include '_footer_nav.html' %}
266:     
267:     <script src="{{ url_for('static', filename='js/alerts.js') }}"></script>
268:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
269:     <script src="{{ url_for('static', filename='js/bottom-nav.js') }}"></script>
270:   </body>
271: </html>
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

## File: switchbot_dashboard/static/js/loaders.js
```javascript
  1: (() => {
  2:     const LOADER_CLASS = 'sb-loader';
  3:     const LOADER_ACTIVE_CLASS = 'sb-loader--active';
  4:     const LOADER_OVERLAY_CLASS = 'sb-loader-overlay';
  5:     const LOADER_SPINNER_CLASS = 'sb-loader-spinner';
  6:     const GLOBAL_LOADER_ID = 'sb-global-loader';
  7:     const GLOBAL_LOADER_ACTIVE_CLASS = 'sb-global-loader--active';
  8:     
  9:     const createLoaderOverlay = () => {
 10:         const overlay = document.createElement('span');
 11:         overlay.className = LOADER_OVERLAY_CLASS;
 12:         overlay.setAttribute('aria-hidden', 'true');
 13:         overlay.setAttribute('role', 'presentation');
 14:         
 15:         const spinner = document.createElement('span');
 16:         spinner.className = LOADER_SPINNER_CLASS;
 17:         spinner.setAttribute('role', 'img');
 18:         spinner.setAttribute('aria-label', 'Chargement...');
 19:         
 20:         overlay.appendChild(spinner);
 21:         return overlay;
 22:     };
 23: 
 24:     const ensureGlobalLoader = () => {
 25:         let overlay = document.getElementById(GLOBAL_LOADER_ID);
 26:         if (overlay) {
 27:             return overlay;
 28:         }
 29: 
 30:         overlay = document.createElement('div');
 31:         overlay.id = GLOBAL_LOADER_ID;
 32:         overlay.className = 'sb-global-loader';
 33:         overlay.setAttribute('aria-hidden', 'true');
 34:         overlay.setAttribute('role', 'presentation');
 35: 
 36:         const spinner = document.createElement('div');
 37:         spinner.className = 'sb-global-loader__spinner';
 38:         spinner.setAttribute('role', 'img');
 39:         spinner.setAttribute('aria-label', 'Chargement...');
 40: 
 41:         overlay.appendChild(spinner);
 42:         document.body.appendChild(overlay);
 43:         return overlay;
 44:     };
 45: 
 46:     const showGlobalLoader = () => {
 47:         const overlay = ensureGlobalLoader();
 48:         overlay.classList.add(GLOBAL_LOADER_ACTIVE_CLASS);
 49:         document.body.classList.add('sb-loading');
 50:     };
 51: 
 52:     const hideGlobalLoader = () => {
 53:         const overlay = document.getElementById(GLOBAL_LOADER_ID);
 54:         if (!overlay) {
 55:             return;
 56:         }
 57:         overlay.classList.remove(GLOBAL_LOADER_ACTIVE_CLASS);
 58:         document.body.classList.remove('sb-loading');
 59:     };
 60:     
 61:     const showLoader = (element) => {
 62:         if (!element || element.classList.contains(LOADER_ACTIVE_CLASS)) {
 63:             return;
 64:         }
 65:         
 66:         element.classList.add(LOADER_ACTIVE_CLASS);
 67:         element.setAttribute('aria-busy', 'true');
 68:         
 69:         const overlay = createLoaderOverlay();
 70:         element.style.position = 'relative';
 71:         element.appendChild(overlay);
 72:         
 73:         requestAnimationFrame(() => {
 74:             overlay.style.opacity = '1';
 75:         });
 76:     };
 77:     
 78:     const hideLoader = (element) => {
 79:         if (!element || !element.classList.contains(LOADER_ACTIVE_CLASS)) {
 80:             return;
 81:         }
 82:         
 83:         element.classList.remove(LOADER_ACTIVE_CLASS);
 84:         element.removeAttribute('aria-busy');
 85:         
 86:         const overlay = element.querySelector(`.${LOADER_OVERLAY_CLASS}`);
 87:         if (overlay) {
 88:             overlay.style.opacity = '0';
 89:             
 90:             setTimeout(() => {
 91:                 if (overlay.parentElement) {
 92:                     overlay.parentElement.removeChild(overlay);
 93:                 }
 94:             }, 200);
 95:         }
 96:     };
 97:     
 98:     const setupFormLoaders = () => {
 99:         const forms = document.querySelectorAll('form[data-loader]');
100:         forms.forEach((form) => {
101:             form.addEventListener('submit', (event) => {
102:                 const submitButton = form.querySelector('button[type="submit"], input[type="submit"]');
103:                 if (submitButton && !submitButton.disabled) {
104:                     event.preventDefault();
105:                     showGlobalLoader();
106:                     showLoader(submitButton);
107:                     
108:                     const originalText = submitButton.textContent;
109:                     submitButton.textContent = 'Chargement...';
110:                     submitButton.disabled = true;
111:                     
112:                     setTimeout(() => {
113:                         form.submit();
114:                     }, 1000);
115:                     setTimeout(() => {
116:                         hideGlobalLoader();
117:                         hideLoader(submitButton);
118:                         submitButton.textContent = originalText;
119:                         submitButton.disabled = false;
120:                     }, 10000);
121:                 }
122:             });
123:         });
124:     };
125:     
126:     const setupButtonLoaders = () => {
127:         document.querySelectorAll('button[data-loader]').forEach(button => {
128:             button.addEventListener('click', (event) => {
129:                 if (button.disabled) {
130:                     event.preventDefault();
131:                     return;
132:                 }
133:                 
134:                 showLoader(button);
135:                 
136:                 const originalText = button.textContent;
137:                 button.textContent = 'Chargement...';
138:                 button.disabled = true;
139:                 
140:                 setTimeout(() => {
141:                     hideLoader(button);
142:                     button.textContent = originalText;
143:                     button.disabled = false;
144:                 }, 3000);
145:             });
146:         });
147:     };
148:     
149:     const setupNavigationLoaders = () => {
150:         document.querySelectorAll('a[data-loader]').forEach((link) => {
151:             link.addEventListener('click', (event) => {
152:                 if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) {
153:                     return;
154:                 }
155: 
156:                 const href = link.getAttribute('href') || '';
157:                 if (!href || href.startsWith('#') || href.startsWith('javascript:')) {
158:                     return;
159:                 }
160: 
161:                 event.preventDefault();
162:                 showGlobalLoader();
163:                 showLoader(link);
164:                 setTimeout(() => {
165:                     window.location.href = href;
166:                 }, 150);
167:             });
168:         });
169:     };
170:     
171:     document.addEventListener('DOMContentLoaded', () => {
172:         ensureGlobalLoader();
173:         hideGlobalLoader();
174:         setupFormLoaders();
175:         setupButtonLoaders();
176:         setupNavigationLoaders();
177:         
178:         window.SwitchBotLoaders = {
179:             show: showLoader,
180:             hide: hideLoader,
181:             showGlobal: showGlobalLoader,
182:             hideGlobal: hideGlobalLoader,
183:         };
184:     });
185: })();
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
 10:         this.currentFilters = {
 11:             timeRange: '6h',
 12:             granularity: 'minute',
 13:             metrics: ['temperature', 'humidity', 'assumed_aircon_power']
 14:         };
 15:         
 16:         this.init();
 17:     }
 18: 
 19:     init() {
 20:         this.initCharts();
 21:         this.bindEvents();
 22:         this.loadInitialData();
 23:         this.startRealTimeUpdates();
 24:     }
 25: 
 26:     initCharts() {
 27:         // Viewport-based responsive configuration
 28:         const isMobile = window.innerWidth <= 768;
 29:         const isSmallMobile = window.innerWidth <= 480;
 30:         
 31:         const chartOptions = {
 32:             responsive: true,
 33:             maintainAspectRatio: false,
 34:             interaction: {
 35:                 mode: 'index',
 36:                 intersect: false,
 37:             },
 38:             plugins: {
 39:                 legend: {
 40:                     position: isMobile ? 'bottom' : 'top',
 41:                     labels: {
 42:                         color: '#e9ecef',
 43:                         font: {
 44:                             size: isSmallMobile ? 10 : (isMobile ? 11 : 12)
 45:                         },
 46:                         padding: isSmallMobile ? 10 : 20,
 47:                         boxWidth: isSmallMobile ? 12 : 15
 48:                     }
 49:                 },
 50:                 tooltip: {
 51:                     backgroundColor: 'rgba(33, 37, 41, 0.9)',
 52:                     titleColor: '#ffffff',
 53:                     bodyColor: '#e9ecef',
 54:                     borderColor: '#495057',
 55:                     borderWidth: 1,
 56:                     titleFont: {
 57:                         size: isSmallMobile ? 11 : 12
 58:                     },
 59:                     bodyFont: {
 60:                         size: isSmallMobile ? 10 : 11
 61:                     },
 62:                     padding: isSmallMobile ? 6 : 10
 63:                 }
 64:             },
 65:             scales: {
 66:                 x: {
 67:                     type: 'time',
 68:                     time: {
 69:                         displayFormats: {
 70:                             minute: isSmallMobile ? 'H:mm' : 'HH:mm',
 71:                             hour: isSmallMobile ? 'H:mm' : 'HH:mm'
 72:                         }
 73:                     },
 74:                     ticks: {
 75:                         color: '#6c757d',
 76:                         font: {
 77:                             size: isSmallMobile ? 9 : 10
 78:                         },
 79:                         maxTicksLimit: isSmallMobile ? 6 : 8
 80:                     },
 81:                     grid: {
 82:                         color: 'rgba(108, 117, 125, 0.2)'
 83:                     }
 84:                 }
 85:             }
 86:         };
 87: 
 88:         // Temperature & Humidity Chart
 89:         this.charts.tempHumidity = new Chart(document.getElementById('tempHumidityChart'), {
 90:             type: 'line',
 91:             data: {
 92:                 datasets: [
 93:                     {
 94:                         label: 'Température (°C)',
 95:                         data: [],
 96:                         borderColor: '#dc3545',
 97:                         backgroundColor: 'rgba(220, 53, 69, 0.1)',
 98:                         tension: 0.4,
 99:                         yAxisID: 'y'
100:                     },
101:                     {
102:                         label: 'Humidité (%)',
103:                         data: [],
104:                         borderColor: '#0d6efd',
105:                         backgroundColor: 'rgba(13, 110, 253, 0.1)',
106:                         tension: 0.4,
107:                         yAxisID: 'y1'
108:                     }
109:                 ]
110:             },
111:             options: {
112:                 ...chartOptions,
113:                 scales: {
114:                     ...chartOptions.scales,
115:                     y: {
116:                         type: 'linear',
117:                         display: true,
118:                         position: 'left',
119:                         title: {
120:                             display: !isMobile,
121:                             text: 'Température (°C)',
122:                             color: '#dc3545',
123:                             font: {
124:                                 size: isSmallMobile ? 9 : 10
125:                             }
126:                         },
127:                         ticks: {
128:                             color: '#6c757d',
129:                             font: {
130:                                 size: isSmallMobile ? 9 : 10
131:                             },
132:                             maxTicksLimit: isSmallMobile ? 4 : 6
133:                         },
134:                         grid: {
135:                             color: 'rgba(108, 117, 125, 0.2)'
136:                         }
137:                     },
138:                     y1: {
139:                         type: 'linear',
140:                         display: true,
141:                         position: 'right',
142:                         title: {
143:                             display: !isMobile,
144:                             text: 'Humidité (%)',
145:                             color: '#0d6efd',
146:                             font: {
147:                                 size: isSmallMobile ? 9 : 10
148:                             }
149:                         },
150:                         ticks: {
151:                             color: '#6c757d',
152:                             font: {
153:                                 size: isSmallMobile ? 9 : 10
154:                             },
155:                             maxTicksLimit: isSmallMobile ? 4 : 6
156:                         },
157:                         grid: {
158:                             drawOnChartArea: false
159:                         }
160:                     }
161:                 }
162:             }
163:         });
164: 
165:         // Aircon State Chart
166:         this.charts.airconState = new Chart(document.getElementById('airconStateChart'), {
167:             type: 'doughnut',
168:             data: {
169:                 labels: ['ON', 'OFF', 'Unknown'],
170:                 datasets: [{
171:                     data: [0, 0, 0],
172:                     backgroundColor: [
173:                         '#198754',
174:                         '#dc3545',
175:                         '#6c757d'
176:                     ],
177:                     borderWidth: 0
178:                 }]
179:             },
180:             options: {
181:                 responsive: true,
182:                 maintainAspectRatio: false,
183:                 plugins: {
184:                     legend: {
185:                         position: 'bottom',
186:                         labels: {
187:                             color: '#e9ecef',
188:                             padding: isSmallMobile ? 10 : 20,
189:                             font: {
190:                                 size: isSmallMobile ? 10 : 11
191:                             },
192:                             boxWidth: isSmallMobile ? 12 : 15
193:                         }
194:                     },
195:                     tooltip: {
196:                         backgroundColor: 'rgba(33, 37, 41, 0.9)',
197:                         titleColor: '#ffffff',
198:                         bodyColor: '#e9ecef',
199:                         borderColor: '#495057',
200:                         borderWidth: 1,
201:                         titleFont: {
202:                             size: isSmallMobile ? 11 : 12
203:                         },
204:                         bodyFont: {
205:                             size: isSmallMobile ? 10 : 11
206:                         },
207:                         padding: isSmallMobile ? 6 : 10
208:                     }
209:                 }
210:             }
211:         });
212:     }
213: 
214:     bindEvents() {
215:         // Filter form submission
216:         document.getElementById('filtersForm').addEventListener('submit', (e) => {
217:             e.preventDefault();
218:             this.applyFilters();
219:         });
220: 
221:         // Time range change
222:         document.getElementById('timeRange').addEventListener('change', (e) => {
223:             const customGroups = ['customStartGroup', 'customEndGroup'];
224:             customGroups.forEach(id => {
225:                 document.getElementById(id).style.display = 
226:                     e.target.value === 'custom' ? 'block' : 'none';
227:             });
228:         });
229: 
230:         // Reset zoom button
231:         document.getElementById('resetZoomTemp').addEventListener('click', () => {
232:             this.charts.tempHumidity.resetZoom();
233:         });
234: 
235:         // Refresh latest records
236:         document.getElementById('refreshLatest').addEventListener('click', () => {
237:             this.loadLatestRecords();
238:         });
239: 
240:         // Metric checkboxes
241:         document.querySelectorAll('.metric-checkboxes input').forEach(checkbox => {
242:             checkbox.addEventListener('change', () => {
243:                 this.updateMetrics();
244:             });
245:         });
246:     }
247: 
248:     async loadInitialData() {
249:         try {
250:             const [historyData, aggregates, latestRecords] = await Promise.all([
251:                 this.loadHistoryData(),
252:                 this.loadAggregates(),
253:                 this.loadLatestRecords()
254:             ]);
255:             
256:             // Check if data is mocked (handle undefined safely)
257:             const isMockData = (historyData && historyData.mock) || 
258:                               (aggregates && aggregates.mock) || 
259:                               (latestRecords && latestRecords.mock);
260:             if (isMockData) {
261:                 this.showMockDataWarning();
262:             }
263:             
264:             this.updateStatus('success', 'Données chargées');
265:         } catch (error) {
266:             console.error('Error loading initial data:', error);
267:             this.updateStatus('error', 'Erreur de chargement');
268:         }
269:     }
270: 
271:     showMockDataWarning() {
272:         // Add a warning banner for mock data
273:         const banner = document.createElement('div');
274:         banner.className = 'alert alert-warning alert-dismissible fade show mb-3';
275:         banner.innerHTML = `
276:             <strong>⚠️ Mode démonstration</strong><br>
277:             Le service d'historique n'est pas disponible. Données simulées affichées.
278:             <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
279:         `;
280:         
281:         const container = document.querySelector('.container');
282:         container.insertBefore(banner, container.firstChild);
283:     }
284: 
285:     async loadHistoryData() {
286:         const params = new URLSearchParams({
287:             start: this.getTimeRangeStart(),
288:             end: new Date().toISOString(),
289:             granularity: this.currentFilters.granularity,
290:             metrics: this.currentFilters.metrics
291:         });
292: 
293:         try {
294:             const response = await fetch(`/history/api/data?${params}`);
295:             if (!response.ok) {
296:                 throw new Error(`HTTP ${response.status}: ${response.statusText}`);
297:             }
298: 
299:             const data = await response.json();
300:             this.updateCharts(data.data || []);
301:             return data; // Return the full response for mock checking
302:         } catch (error) {
303:             console.error('Failed to load history data:', error);
304:             this.updateStatus('error', 'Erreur de chargement des données');
305:             this.renderChartErrorState(error);
306:             throw error;
307:         }
308:     }
309: 
310:     renderChartErrorState(error) {
311:         document.querySelectorAll('.chart-container').forEach((container) => {
312:             container.innerHTML = `
313:                 <div class="d-flex flex-column align-items-center justify-content-center text-muted py-4">
314:                     <div class="fs-3 mb-2">⚠️</div>
315:                     <div class="text-center">Impossible de charger les données</div>
316:                     <small class="d-block mt-2">${error.message}</small>
317:                 </div>
318:             `;
319:         });
320:     }
321: 
322:     async loadAggregates() {
323:         const response = await fetch('/history/api/aggregates?period_hours=6');
324:         if (!response.ok) throw new Error('Failed to load aggregates');
325:         
326:         const data = await response.json();
327:         this.updateStatusCards(data.aggregates || {});
328:         return data; // Return the full response for mock checking
329:     }
330: 
331:     async loadLatestRecords() {
332:         const response = await fetch('/history/api/latest?limit=10');
333:         if (!response.ok) throw new Error('Failed to load latest records');
334:         
335:         const data = await response.json();
336:         this.updateLatestTable(data.latest || []);
337:         return data; // Return the full response for mock checking
338:     }
339: 
340:     updateCharts(historyData) {
341:         if (!historyData || historyData.length === 0) return;
342: 
343:         // Update temperature & humidity chart
344:         const tempData = historyData.map(d => ({
345:             x: d.timestamp,
346:             y: d.temperature
347:         })).filter(d => d.y !== null);
348: 
349:         const humidityData = historyData.map(d => ({
350:             x: d.timestamp,
351:             y: d.humidity
352:         })).filter(d => d.y !== null);
353: 
354:         this.charts.tempHumidity.data.datasets[0].data = tempData;
355:         this.charts.tempHumidity.data.datasets[1].data = humidityData;
356:         this.charts.tempHumidity.update('none');
357: 
358:         // Update aircon state chart
359:         const airconStates = historyData.reduce((acc, d) => {
360:             const state = d.assumed_aircon_power || 'unknown';
361:             acc[state] = (acc[state] || 0) + 1;
362:             return acc;
363:         }, {});
364: 
365:         this.charts.airconState.data.datasets[0].data = [
366:             airconStates['on'] || 0,
367:             airconStates['off'] || 0,
368:             airconStates['unknown'] || 0
369:         ];
370:         this.charts.airconState.update('none');
371:     }
372: 
373:     updateStatusCards(aggregates) {
374:         console.log('updateStatusCards called with:', aggregates);
375:         
376:         const avgTemp = aggregates.avg_temperature ? parseFloat(aggregates.avg_temperature).toFixed(1) : '--';
377:         const avgHumidity = aggregates.avg_humidity ? parseFloat(aggregates.avg_humidity).toFixed(1) : '--';
378:         
379:         console.log('Processed values - Temp:', avgTemp, 'Humidity:', avgHumidity);
380:         
381:         const tempElement = document.getElementById('avgTemp');
382:         const humidityElement = document.getElementById('avgHumidity');
383:         
384:         console.log('Elements found:', !!tempElement, !!humidityElement);
385:         
386:         if (tempElement) tempElement.textContent = avgTemp;
387:         if (humidityElement) humidityElement.textContent = avgHumidity;
388:     }
389: 
390:     updateLatestTable(latestRecords) {
391:         const tbody = document.getElementById('latestTableBody');
392:         
393:         if (!latestRecords || latestRecords.length === 0) {
394:             tbody.innerHTML = `
395:                 <tr>
396:                     <td colspan="5" class="text-center text-muted">
397:                         Aucun enregistrement trouvé
398:                     </td>
399:                 </tr>
400:             `;
401:             return;
402:         }
403: 
404:         tbody.innerHTML = latestRecords.map(record => {
405:             const timestamp = new Date(record.timestamp).toLocaleString('fr-FR');
406:             const temp = record.temperature ? `${record.temperature}°C` : '--';
407:             const humidity = record.humidity ? `${record.humidity}%` : '--';
408:             const airconState = this.formatAirconState(record.assumed_aircon_power);
409:             const action = record.last_action || '--';
410:             
411:             return `
412:                 <tr>
413:                     <td>${timestamp}</td>
414:                     <td>${temp}</td>
415:                     <td>${humidity}</td>
416:                     <td>${airconState}</td>
417:                     <td>${action}</td>
418:                 </tr>
419:             `;
420:         }).join('');
421:     }
422: 
423:     formatAirconState(state) {
424:         const stateMap = {
425:             'on': '<span class="badge bg-success">ON</span>',
426:             'off': '<span class="badge bg-danger">OFF</span>',
427:             'unknown': '<span class="badge bg-secondary">?</span>'
428:         };
429:         return stateMap[state] || stateMap['unknown'];
430:     }
431: 
432:     getTimeRangeStart() {
433:         const now = new Date();
434:         const range = this.currentFilters.timeRange;
435:         
436:         switch (range) {
437:             case '1h':
438:                 return new Date(now.getTime() - 60 * 60 * 1000).toISOString();
439:             case '6h':
440:                 return new Date(now.getTime() - 6 * 60 * 60 * 1000).toISOString();
441:             case '24h':
442:                 return new Date(now.getTime() - 24 * 60 * 60 * 1000).toISOString();
443:             case 'custom':
444:                 const customStart = document.getElementById('customStart').value;
445:                 return customStart ? new Date(customStart).toISOString() : this.getTimeRangeStart();
446:             default:
447:                 return this.getTimeRangeStart();
448:         }
449:     }
450: 
451:     applyFilters() {
452:         const timeRange = document.getElementById('timeRange').value;
453:         const granularity = document.getElementById('granularity').value;
454:         const metrics = Array.from(document.querySelectorAll('.metric-checkboxes input:checked'))
455:             .map(cb => cb.value);
456: 
457:         this.currentFilters = { timeRange, granularity, metrics };
458:         this.loadHistoryData();
459:         this.updateStatus('loading', 'Application des filtres...');
460:     }
461: 
462:     updateMetrics() {
463:         const checkedMetrics = Array.from(document.querySelectorAll('.metric-checkboxes input:checked'))
464:             .map(cb => cb.value);
465:         this.currentFilters.metrics = checkedMetrics;
466:         this.loadHistoryData();
467:     }
468: 
469:     updateStatus(type, message) {
470:         const indicator = document.getElementById('statusIndicator');
471:         const text = document.getElementById('statusText');
472:         const lastUpdate = document.getElementById('lastUpdate');
473: 
474:         // Update indicator
475:         indicator.className = 'status-indicator';
476:         if (type === 'success') {
477:             indicator.classList.add('status-success');
478:         } else if (type === 'error') {
479:             indicator.classList.add('status-error');
480:         } else if (type === 'loading') {
481:             indicator.classList.add('status-loading');
482:         }
483: 
484:         // Update text
485:         text.textContent = message;
486:         lastUpdate.textContent = new Date().toLocaleTimeString('fr-FR');
487:     }
488: 
489:     startRealTimeUpdates() {
490:         // Update every 30 seconds
491:         this.updateInterval = setInterval(() => {
492:             this.loadHistoryData();
493:             this.loadAggregates();
494:             this.loadLatestRecords();
495:         }, 30000);
496:     }
497: 
498:     destroy() {
499:         if (this.updateInterval) {
500:             clearInterval(this.updateInterval);
501:         }
502:         
503:         // Destroy charts
504:         Object.values(this.charts).forEach(chart => {
505:             if (chart) chart.destroy();
506:         });
507:     }
508: }
509: 
510: // Initialize dashboard when DOM is ready
511: document.addEventListener('DOMContentLoaded', () => {
512:     window.historyDashboard = new HistoryDashboard();
513: });
514: 
515: // Cleanup on page unload
516: window.addEventListener('beforeunload', () => {
517:     if (window.historyDashboard) {
518:         window.historyDashboard.destroy();
519:     }
520: });
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

## File: switchbot_dashboard/templates/devices.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>Appareils - SwitchBot Dashboard</title>
  7:     <link
  8:       href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
  9:       rel="stylesheet"
 10:       integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDS..."
 11:       crossorigin="anonymous"
 12:     />
 13:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 14:     <link rel="stylesheet" href="{{ url_for('static', filename='css/devices.css') }}" />
 15:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 16:     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
 17:   </head>
 18:   <body class="sb-dark">
 19:     <div class="container py-4">
 20:       <h1 class="h3 mb-4">Appareils</h1>
 21: 
 22:       {% if error %}
 23:         <div class="alert alert-danger">{{ error }}</div>
 24:       {% endif %}
 25: 
 26:       {% if data %}
 27:         {% set body = data.get("body", {}) or {} %}
 28:         {% set device_list = body.get("deviceList") or [] %}
 29:         {% set remote_list = body.get("infraredRemoteList") or [] %}
 30: 
 31:         <div class="card highlight-card mb-4" aria-live="polite">
 32:           <div class="card-body d-flex flex-column flex-lg-row align-items-lg-center gap-3">
 33:             <div>
 34:               <p class="text-uppercase small text-muted fw-semibold mb-1">Instantané d'inventaire</p>
 35:               <h2 class="h4 mb-0">{{ device_list | length }} physiques · {{ remote_list | length }} infrarouges</h2>
 36:             </div>
 37:             <div class="ms-lg-auto">
 38:               <p class="mb-0 text-muted">
 39:                 Utilise ces listes pour retrouver rapidement <code>meter_device_id</code> et <code>aircon_device_id</code>
 40:                 avant de mettre à jour <strong>config/settings.json</strong> (cf. docs/README.md).
 41:               </p>
 42:             </div>
 43:           </div>
 44:         </div>
 45: 
 46:         <section aria-labelledby="devices-heading" class="mb-5">
 47:           <div class="section-title">
 48:             <div>
 49:               <p class="text-uppercase small text-muted fw-semibold mb-1">Appareils physiques</p>
 50:               <h2 id="devices-heading" class="h4 mb-0">Liste des appareils</h2>
 51:             </div>
 52:             {% if device_list %}
 53:               <span class="badge rounded-pill bg-glass">{{ device_list | length }} trouvés</span>
 54:             {% endif %}
 55:           </div>
 56: 
 57:           {% if device_list %}
 58:             <div class="device-grid">
 59:               {% for device in device_list %}
 60:                 <article class="device-card" aria-label="{{ device.get('deviceName') or 'Appareil SwitchBot' }}">
 61:                   <div class="device-card__header">
 62:                     <div>
 63:                       <h3 class="device-name">{{ device.get("deviceName") or "Appareil sans nom" }}</h3>
 64:                       <p class="device-type text-muted mb-0">{{ device.get("deviceType") or "Type inconnu" }}</p>
 65:                     </div>
 66:                     <span class="badge rounded-pill bg-accent">
 67:                       {{ "Hub" if device.get("hubDeviceId") else "Autonome" }}
 68:                     </span>
 69:                   </div>
 70: 
 71:                   <dl class="device-meta device-meta--primary">
 72:                     <div>
 73:                       <dt>ID</dt>
 74:                       <dd class="device-id">{{ device.get("deviceId") or "—" }}</dd>
 75:                     </div>
 76:                     <div>
 77:                       <dt>Statut</dt>
 78:                       <dd class="{{ 'text-success' if device.get('status') == 'online' else 'text-warning' }}">
 79:                         {{ device.get("status") or "n/d" }}
 80:                       </dd>
 81:                     </div>
 82:                   </dl>
 83: 
 84:                   <details class="device-details">
 85:                     <summary>Voir les détails</summary>
 86:                     <dl class="device-meta device-meta--secondary">
 87:                       <div>
 88:                         <dt>Hub</dt>
 89:                         <dd>{{ device.get("hubDeviceId") or "Aucun" }}</dd>
 90:                       </div>
 91:                       <div>
 92:                         <dt>Firmware</dt>
 93:                         <dd>{{ device.get("firmwareVersion") or "Inconnu" }}</dd>
 94:                       </div>
 95:                       <div>
 96:                         <dt>Cloud</dt>
 97:                         <dd>{{ "Activé" if device.get("enableCloudService") else "Désactivé" }}</dd>
 98:                       </div>
 99:                       <div>
100:                         <dt>Batterie</dt>
101:                         <dd>{{ device.get("battery") or "—" }}</dd>
102:                       </div>
103:                     </dl>
104:                   </details>
105: 
106:                   <div class="device-actions">
107:                     <button
108:                       type="button"
109:                       class="btn btn-copy"
110:                       data-copy="{{ device.get('deviceId') }}"
111:                       aria-label="Copier l'identifiant {{ device.get('deviceName') }}"
112:                     >
113:                       Copier l'ID
114:                     </button>
115:                     {% if device.get("virtualModel") %}
116:                       <span class="badge rounded-pill bg-outline">{{ device.get("virtualModel") }}</span>
117:                     {% endif %}
118:                   </div>
119:                 </article>
120:               {% endfor %}
121:             </div>
122:           {% else %}
123:             <p class="text-muted fst-italic">Aucun appareil physique n'a été renvoyé.</p>
124:           {% endif %}
125: 
126:           <!-- Collapsible raw JSON retained for troubleshooting without overwhelming the main UI -->
127:           <details class="raw-block mt-3">
128:             <summary>Afficher le JSON brut deviceList</summary>
129:             <pre>{{ device_list | tojson(indent=2) }}</pre>
130:           </details>
131:         </section>
132: 
133:         <section aria-labelledby="remotes-heading">
134:           <div class="section-title">
135:             <div>
136:               <p class="text-uppercase small text-muted fw-semibold mb-1">Télécommandes infrarouges</p>
137:               <h2 id="remotes-heading" class="h4 mb-0">Liste des télécommandes</h2>
138:             </div>
139:             {% if remote_list %}
140:               <span class="badge rounded-pill bg-glass">{{ remote_list | length }} trouvées</span>
141:             {% endif %}
142:           </div>
143: 
144:           {% if remote_list %}
145:             <div class="device-grid">
146:               {% for remote in remote_list %}
147:                 <article class="device-card" aria-label="{{ remote.get('remoteName') or 'Télécommande infrarouge' }}">
148:                   <div class="device-card__header">
149:                     <div>
150:                       <h3 class="device-name">{{ remote.get("remoteName") or "Télécommande sans nom" }}</h3>
151:                       <p class="device-type text-muted mb-0">{{ remote.get("remoteType") or "Type inconnu" }}</p>
152:                     </div>
153:                     <span class="badge rounded-pill bg-accent">
154:                       {{ remote.get("hubDeviceId") or "Hub n/d" }}
155:                     </span>
156:                   </div>
157: 
158:                   <dl class="device-meta device-meta--primary">
159:                     <div>
160:                       <dt>ID</dt>
161:                       <dd class="device-id">{{ remote.get("deviceId") or "—" }}</dd>
162:                     </div>
163:                     <div>
164:                       <dt>Marque</dt>
165:                       <dd>{{ remote.get("remoteBrand") or "Inconnue" }}</dd>
166:                     </div>
167:                   </dl>
168: 
169:                   <details class="device-details">
170:                     <summary>Voir les détails</summary>
171:                     <dl class="device-meta device-meta--secondary">
172:                       <div>
173:                         <dt>Modèle</dt>
174:                         <dd>{{ remote.get("remoteModel") or "Inconnu" }}</dd>
175:                       </div>
176:                       <div>
177:                         <dt>Catégorie</dt>
178:                         <dd>{{ remote.get("remoteDeviceType") or "n/d" }}</dd>
179:                       </div>
180:                       <div>
181:                         <dt>Cloud</dt>
182:                         <dd>{{ "Activé" if remote.get("enableCloudService") else "Désactivé" }}</dd>
183:                       </div>
184:                     </dl>
185:                   </details>
186: 
187:                   <div class="device-actions">
188:                     <button
189:                       type="button"
190:                       class="btn btn-copy"
191:                       data-copy="{{ remote.get('deviceId') }}"
192:                       aria-label="Copier l'identifiant {{ remote.get('remoteName') }}"
193:                     >
194:                       Copier l'ID
195:                     </button>
196:                     {% if remote.get("hubDeviceId") %}
197:                       <span class="badge rounded-pill bg-outline">Hub {{ remote.get("hubDeviceId") }}</span>
198:                     {% endif %}
199:                   </div>
200:                 </article>
201:               {% endfor %}
202:             </div>
203:           {% else %}
204:             <p class="text-muted fst-italic">Aucune télécommande IR n'a été renvoyée.</p>
205:           {% endif %}
206: 
207:           <details class="raw-block mt-3">
208:             <summary>Afficher le JSON brut infraredRemoteList</summary>
209:             <pre>{{ remote_list | tojson(indent=2) }}</pre>
210:           </details>
211:         </section>
212:       {% else %}
213:         <div class="alert alert-warning">Aucune donnée.</div>
214:       {% endif %}
215:     </div>
216:     
217:     {% include '_footer_nav.html' %}
218:     
219:     <script src="{{ url_for('static', filename='js/devices.js') }}"></script>
220:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
221:   </body>
222: </html>
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

## File: switchbot_dashboard/templates/history.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>Historique Monitoring - SwitchBot Dashboard</title>
  7:     <link
  8:       href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
  9:       rel="stylesheet"
 10:       integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDS..."
 11:       crossorigin="anonymous"
 12:     />
 13:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 14:     <link rel="stylesheet" href="{{ url_for('static', filename='css/history.css') }}" />
 15:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 16:     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
 17:     <style>
 18:       /* Centrage et blocs des checkboxes de métriques */
 19:       .metric-checkboxes {
 20:         display: flex;
 21:         justify-content: center;
 22:         align-items: stretch;
 23:         gap: 1rem;
 24:         flex-wrap: wrap;
 25:       }
 26:       
 27:       .metric-checkboxes .metric-option {
 28:         flex: 1 1 140px;
 29:         min-width: 140px;
 30:         background: var(--sb-card);
 31:         border: 1px solid var(--sb-card-border);
 32:         border-radius: 0.75rem;
 33:         padding: 0.75rem 1rem;
 34:         display: flex;
 35:         align-items: center;
 36:         gap: 0.75rem;
 37:         margin: 0;
 38:         box-shadow: var(--sb-shadow);
 39:       }
 40:       
 41:       .metric-checkboxes .metric-option:hover {
 42:         border-color: var(--sb-accent);
 43:       }
 44:       
 45:       .metric-checkboxes .metric-option .form-check-input {
 46:         margin: 0;
 47:         width: 1.1rem;
 48:         height: 1.1rem;
 49:       }
 50:       
 51:       .metric-checkboxes .metric-option .form-check-label {
 52:         margin: 0;
 53:         font-weight: 600;
 54:         color: var(--sb-text);
 55:         display: flex;
 56:         align-items: center;
 57:       }
 58:       
 59:       @media (max-width: 768px) {
 60:         .metric-checkboxes {
 61:           flex-direction: column;
 62:           gap: 0.75rem;
 63:         }
 64:       }
 65:     </style>
 66:   </head>
 67:   <body class="sb-dark">
 68:     <div class="container py-4">
 69:       <header class="page-header mb-4">
 70:         <div class="page-header-main">
 71:           <h1 class="h3 mb-0">Historique Monitoring</h1>
 72:           <p class="page-subtitle text-muted mb-0">
 73:             Visualisez les tendances et analysez les données historiques.
 74:           </p>
 75:         </div>
 76:       </header>
 77: 
 78:       <!-- Filters Section -->
 79:       <section class="history-filters mb-4">
 80:         <div class="card sb-card">
 81:           <div class="card-body">
 82:             <form id="filtersForm" class="row g-3 align-items-end">
 83:               <div class="col-md-3">
 84:                 <label for="timeRange" class="form-label">Période</label>
 85:                 <select class="form-select sb-select" id="timeRange" name="timeRange">
 86:                   <option value="1h">Dernière heure</option>
 87:                   <option value="6h" selected>Dernières 6 heures</option>
 88:                   <option value="24h">Dernières 24 heures</option>
 89:                   <option value="custom">Personnalisé</option>
 90:                 </select>
 91:               </div>
 92:               <div class="col-md-3" id="customStartGroup" style="display: none;">
 93:                 <label for="customStart" class="form-label">Début</label>
 94:                 <input type="datetime-local" class="form-control sb-input" id="customStart" name="customStart">
 95:               </div>
 96:               <div class="col-md-3" id="customEndGroup" style="display: none;">
 97:                 <label for="customEnd" class="form-label">Fin</label>
 98:                 <input type="datetime-local" class="form-control sb-input" id="customEnd" name="customEnd">
 99:               </div>
100:               <div class="col-md-2">
101:                 <label for="granularity" class="form-label">Granularité</label>
102:                 <select class="form-select sb-select" id="granularity" name="granularity">
103:                   <option value="minute">Par minute</option>
104:                   <option value="5min">Par 5 minutes</option>
105:                   <option value="15min">Par 15 minutes</option>
106:                   <option value="hour">Par heure</option>
107:                 </select>
108:               </div>
109:               <div class="col-md-4">
110:                 <label class="form-label">Métriques</label>
111:                 <div class="metric-checkboxes">
112:                   <div class="form-check metric-option">
113:                     <input class="form-check-input" type="checkbox" id="metricTemp" value="temperature" checked>
114:                     <label class="form-check-label" for="metricTemp">
115:                       <span>Température</span>
116:                     </label>
117:                   </div>
118:                   <div class="form-check metric-option">
119:                     <input class="form-check-input" type="checkbox" id="metricHumidity" value="humidity" checked>
120:                     <label class="form-check-label" for="metricHumidity">
121:                       <span>Humidité</span>
122:                     </label>
123:                   </div>
124:                   <div class="form-check metric-option">
125:                     <input class="form-check-input" type="checkbox" id="metricAircon" value="assumed_aircon_power" checked>
126:                     <label class="form-check-label" for="metricAircon">
127:                       <span>Climatisation</span>
128:                     </label>
129:                   </div>
130:                 </div>
131:               </div>
132:               <div class="col-md-2">
133:                 <button type="submit" class="btn btn-primary w-100" data-loader>
134:                   Appliquer
135:                 </button>
136:               </div>
137:             </form>
138:           </div>
139:         </div>
140:       </section>
141: 
142:       <!-- Status Cards -->
143:       <section class="status-cards mb-4">
144:         <div class="row g-3">
145:           <div class="col-md-6">
146:             <div class="card sb-card status-card">
147:               <div class="card-body text-center">
148:                 <div class="status-card__value" id="avgTemp">--</div>
149:                 <div class="status-card__label">Température moyenne</div>
150:                 <div class="status-card__unit">°C</div>
151:               </div>
152:             </div>
153:           </div>
154:           <div class="col-md-6">
155:             <div class="card sb-card status-card">
156:               <div class="card-body text-center">
157:                 <div class="status-card__value" id="avgHumidity">--</div>
158:                 <div class="status-card__label">Humidité moyenne</div>
159:                 <div class="status-card__unit">%</div>
160:               </div>
161:             </div>
162:           </div>
163:         </div>
164:       </section>
165: 
166:       <!-- Charts Section -->
167:       <section class="charts-section mb-4">
168:         <div class="row g-4">
169:           <!-- Temperature & Humidity Chart -->
170:           <div class="col-12">
171:             <div class="card sb-card">
172:               <div class="card-header d-flex justify-content-between align-items-center">
173:                 <h5 class="card-title mb-0">Température & Humidité</h5>
174:                 <div class="chart-controls">
175:                   <button class="btn btn-sm btn-outline-secondary" id="resetZoomTemp">
176:                     Réinitialiser zoom
177:                   </button>
178:                 </div>
179:               </div>
180:               <div class="card-body">
181:                 <div class="chart-container">
182:                   <canvas id="tempHumidityChart"></canvas>
183:                 </div>
184:               </div>
185:             </div>
186:           </div>
187: 
188:           <!-- Aircon State Chart -->
189:           <div class="col-12">
190:             <div class="card sb-card">
191:               <div class="card-header">
192:                 <h5 class="card-title mb-0">État Climatisation</h5>
193:               </div>
194:               <div class="card-body">
195:                 <div class="chart-container" style="max-height: 300px;">
196:                   <canvas id="airconStateChart"></canvas>
197:                 </div>
198:               </div>
199:             </div>
200:           </div>
201:         </div>
202:       </section>
203: 
204:       <!-- Latest Records Table -->
205:       <section class="latest-records mb-4">
206:         <div class="card sb-card">
207:           <div class="card-header d-flex justify-content-between align-items-center">
208:             <h5 class="card-title mb-0">Derniers enregistrements</h5>
209:             <button class="btn btn-sm btn-outline-secondary" id="refreshLatest">
210:               Actualiser
211:             </button>
212:           </div>
213:           <div class="card-body">
214:             <div class="table-responsive">
215:               <table class="table table-dark table-hover" id="latestTable">
216:                 <thead>
217:                   <tr>
218:                     <th>Timestamp</th>
219:                     <th>Température</th>
220:                     <th>Humidité</th>
221:                     <th>Climatisation</th>
222:                     <th>Action</th>
223:                   </tr>
224:                 </thead>
225:                 <tbody id="latestTableBody">
226:                   <tr>
227:                     <td colspan="5" class="text-center text-muted">
228:                       <div class="spinner-border spinner-border-sm me-2" role="status"></div>
229:                       Chargement...
230:                     </td>
231:                   </tr>
232:                 </tbody>
233:               </table>
234:             </div>
235:           </div>
236:         </div>
237:       </section>
238: 
239:       <!-- Real-time Status -->
240:       <section class="real-time-status">
241:         <div class="card sb-card">
242:           <div class="card-body">
243:             <div class="d-flex justify-content-between align-items-center">
244:               <div>
245:                 <small class="text-muted">Dernière mise à jour</small>
246:                 <div class="fw-bold" id="lastUpdate">--</div>
247:               </div>
248:               <div class="d-flex align-items-center">
249:                 <div class="status-indicator me-2" id="statusIndicator"></div>
250:                 <span id="statusText">En attente</span>
251:               </div>
252:             </div>
253:           </div>
254:         </div>
255:       </section>
256:     </div>
257: 
258:     {% include '_footer_nav.html' %}
259: 
260:     <!-- Scripts -->
261:     <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
262:     <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3.0.0/dist/chartjs-adapter-date-fns.bundle.min.js"></script>
263:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
264:     <script src="{{ url_for('static', filename='js/history.js') }}"></script>
265:   </body>
266: </html>
```

## File: switchbot_dashboard/templates/quota.html
```html
  1: <!doctype html>
  2: <html lang="fr">
  3:   <head>
  4:     <meta charset="utf-8" />
  5:     <meta name="viewport" content="width=device-width, initial-scale=1" />
  6:     <title>Quota API SwitchBot</title>
  7:     <link
  8:       href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
  9:       rel="stylesheet"
 10:       integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDS..."
 11:       crossorigin="anonymous"
 12:     />
 13:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 14:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 15:     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
 16:   </head>
 17:   <body class="sb-dark">
 18:     <div class="container py-4">
 19:       <header class="page-header mb-4">
 20:         <div class="page-header-main">
 21:           <h1 class="h3 mb-0">Quota API quotidien</h1>
 22:           <p class="page-subtitle text-muted mb-0">
 23:             Surveillez votre consommation SwitchBot et anticipez les coupures.
 24:           </p>
 25:         </div>
 26:       </header>
 27: 
 28:       {% with messages = get_flashed_messages(with_categories=true) %}
 29:         {% if messages %}
 30:           <div class="mb-3" aria-live="polite" aria-atomic="true">
 31:             {% for category, message in messages %}
 32:               {% if category == 'error' %}
 33:                 <div class="alert alert-danger" role="alert" data-auto-dismiss="6000">
 34:                   {{ message }}
 35:                 </div>
 36:               {% elif category == 'success' %}
 37:                 <div class="alert alert-success" role="alert" data-auto-dismiss="6000">
 38:                   {{ message }}
 39:                 </div>
 40:               {% else %}
 41:                 <div class="alert alert-info" role="alert" data-auto-dismiss="6000">
 42:                   {{ message }}
 43:                 </div>
 44:               {% endif %}
 45:             {% endfor %}
 46:           </div>
 47:         {% endif %}
 48:       {% endwith %}
 49: 
 50:       <article class="card">
 51:         <div class="card-body">
 52:           <div class="d-flex flex-column flex-lg-row align-items-lg-center gap-4">
 53:             <div class="api-quota flex-grow-1">
 54:               <span class="api-quota-label">Suivi journalier</span>
 55:               {% if api_quota_day %}
 56:                 <div class="api-quota-meta">
 57:                   Jour suivi : <strong>{{ api_quota_day }}</strong>
 58:                   {% if api_quota_reset_at %}
 59:                     <span class="separator">•</span>
 60:                     Reset prévu : <strong>{{ api_quota_reset_at }}</strong>
 61:                   {% else %}
 62:                     <span class="separator">•</span>
 63:                     Reset automatique à 00:00 UTC
 64:                   {% endif %}
 65:                 </div>
 66:               {% endif %}
 67: 
 68:               <div class="api-quota-values">
 69:                 <div class="api-quota-metric">
 70:                   <span class="metric-label">Restantes</span>
 71:                   <span class="metric-value">
 72:                     {{ api_requests_remaining if api_requests_remaining is not none else "N/A" }}
 73:                   </span>
 74:                 </div>
 75:                 <span class="api-quota-separator" aria-hidden="true"></span>
 76:                 <div class="api-quota-metric">
 77:                   <span class="metric-label">Utilisées</span>
 78:                   <span class="metric-value">
 79:                     {{ api_requests_total if api_requests_total is not none else "N/A" }}
 80:                   </span>
 81:                   <span class="metric-cap">
 82:                     / {{ api_requests_limit if api_requests_limit is not none else "10,000" }}
 83:                   </span>
 84:                 </div>
 85:               </div>
 86: 
 87:               {% if show_quota_warning %}
 88:                 <div class="quota-alert alert alert-warning mt-3" role="status">
 89:                   <strong>Attention : quota critique.</strong>
 90:                   <span>
 91:                     Il ne reste que {{ api_requests_remaining }} appels (seuil fixé à {{ quota_warning_threshold }}).
 92:                   </span>
 93:                 </div>
 94:               {% endif %}
 95:             </div>
 96: 
 97:             <div class="text-muted small flex-grow-1">
 98:               <p class="mb-2">
 99:                 Le compteur s'appuie sur <strong>ApiQuotaTracker</strong> :
100:               </p>
101:               <ul class="mb-3 ps-4">
102:                 <li>Réinitialisation automatique à minuit (UTC)</li>
103:                 <li>Fallback local si les en-têtes SwitchBot sont absents</li>
104:                 <li>Inclut les appels manuels, scènes et boucles d'automatisation</li>
105:               </ul>
106:               <p class="mb-0">
107:                 Ajustez le seuil d'alerte dans les réglages de l'accueil pour être prévenu suffisamment tôt.
108:               </p>
109:             </div>
110:           </div>
111:         </div>
112:       </article>
113:     </div>
114:     
115:     {% include '_footer_nav.html' %}
116:     
117:     <script src="{{ url_for('static', filename='js/alerts.js') }}"></script>
118:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
119:   </body>
120: </html>
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
  7:     <link
  8:       href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
  9:       rel="stylesheet"
 10:       integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDS..."
 11:       crossorigin="anonymous"
 12:     />
 13:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
 14:     <link rel="stylesheet" href="{{ url_for('static', filename='css/settings.css') }}" />
 15:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" />
 16:     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
 17:   </head>
 18:   <body class="sb-dark">
 19:     <div class="container py-4">
 20:       <header class="page-header mb-4">
 21:         <div class="page-header-main">
 22:           <h1 class="h3 mb-0">Réglages SwitchBot</h1>
 23:           <p class="page-subtitle text-muted mb-0">
 24:             Configurez les fenêtres horaires, profils hiver/été, scènes et seuils avancés.
 25:           </p>
 26:         </div>
 27:       </header>
 28: 
 29:       {% with messages = get_flashed_messages(with_categories=true) %}
 30:         {% if messages %}
 31:           <div class="mb-3" aria-live="polite" aria-atomic="true">
 32:             {% for category, message in messages %}
 33:               {% if category == 'error' %}
 34:                 <div class="alert alert-danger" role="alert" data-auto-dismiss="6000">
 35:                   {{ message }}
 36:                 </div>
 37:               {% else %}
 38:                 <div class="alert alert-success" role="alert" data-auto-dismiss="6000">
 39:                   {{ message }}
 40:                 </div>
 41:               {% endif %}
 42:             {% endfor %}
 43:           </div>
 44:         {% endif %}
 45:       {% endwith %}
 46: 
 47:       <div class="row g-3">
 48:         <div class="col-12 col-xl-9">
 49:           <div class="card">
 50:             <div class="card-header">Paramètres d'automatisation</div>
 51:             <div class="card-body">
 52:               <form method="post" action="{{ url_for('dashboard.update_settings') }}" class="settings-form" data-loader>
 53:                 <div class="form-check form-switch mb-3">
 54:                   <input
 55:                     class="form-check-input"
 56:                     type="checkbox"
 57:                     role="switch"
 58:                     id="automation_enabled"
 59:                     name="automation_enabled"
 60:                     {% if settings.get('automation_enabled') %}checked{% endif %}
 61:                   />
 62:                   <label class="form-check-label" for="automation_enabled">Automatisation activée</label>
 63:                 </div>
 64: 
 65:                 <div class="row g-3">
 66:                   <div class="col-12 col-md-4">
 67:                     <label class="form-label" for="mode">Mode</label>
 68:                     <select class="form-select" id="mode" name="mode">
 69:                       <option value="winter" {% if settings.get('mode') == 'winter' %}selected{% endif %}>hiver</option>
 70:                       <option value="summer" {% if settings.get('mode') == 'summer' %}selected{% endif %}>été</option>
 71:                     </select>
 72:                   </div>
 73: 
 74:                   <div class="col-12 col-md-4">
 75:                     <label class="form-label" for="poll_interval_seconds">Intervalle de sondage (s)</label>
 76:                     <input
 77:                       class="form-control"
 78:                       id="poll_interval_seconds"
 79:                       name="poll_interval_seconds"
 80:                       value="{{ settings.get('poll_interval_seconds') }}"
 81:                       inputmode="numeric"
 82:                     />
 83:                   </div>
 84: 
 85:                   <div class="col-12 col-md-4">
 86:                     <label class="form-label" for="command_cooldown_seconds">Cooldown par défaut (s)</label>
 87:                     <input
 88:                       class="form-control"
 89:                       id="command_cooldown_seconds"
 90:                       name="command_cooldown_seconds"
 91:                       value="{{ settings.get('command_cooldown_seconds') }}"
 92:                       inputmode="numeric"
 93:                     />
 94:                     <div class="form-text">Utilisé si les champs ci-dessous sont vides.</div>
 95:                   </div>
 96: 
 97:                   <div class="col-12 col-md-4">
 98:                     <label class="form-label" for="action_on_cooldown_seconds">Cooldown après démarrage (s)</label>
 99:                     <input
100:                       class="form-control"
101:                       id="action_on_cooldown_seconds"
102:                       name="action_on_cooldown_seconds"
103:                       value="{{ settings.get('action_on_cooldown_seconds') }}"
104:                       inputmode="numeric"
105:                     />
106:                     <div class="form-text">Recommandé : 300 s (5 min) pour laisser la pompe chauffer.</div>
107:                   </div>
108: 
109:                   <div class="col-12 col-md-4">
110:                     <label class="form-label" for="action_off_cooldown_seconds">Cooldown après arrêt (s)</label>
111:                     <input
112:                       class="form-control"
113:                       id="action_off_cooldown_seconds"
114:                       name="action_off_cooldown_seconds"
115:                       value="{{ settings.get('action_off_cooldown_seconds') }}"
116:                       inputmode="numeric"
117:                     />
118:                     <div class="form-text">Recommandé : 60 s pour garder un arrêt réactif.</div>
119:                   </div>
120:                 </div>
121: 
122:                 <div class="row g-3">
123:                   <div class="col-12 col-md-4">
124:                     <label class="form-label" for="off_repeat_count">Répétitions arrêt OFF</label>
125:                     <input
126:                       class="form-control"
127:                       id="off_repeat_count"
128:                       name="off_repeat_count"
129:                       value="{{ settings.get('off_repeat_count', 1) }}"
130:                       inputmode="numeric"
131:                       min="1"
132:                       max="10"
133:                     />
134:                     <div class="form-text">Nombre total d'ordres OFF envoyés (1 = aucune répétition).</div>
135:                   </div>
136: 
137:                   <div class="col-12 col-md-4">
138:                     <label class="form-label" for="off_repeat_interval_seconds">Intervalle entre OFF (s)</label>
139:                     <input
140:                       class="form-control"
141:                       id="off_repeat_interval_seconds"
142:                       name="off_repeat_interval_seconds"
143:                       value="{{ settings.get('off_repeat_interval_seconds', 10) }}"
144:                       inputmode="numeric"
145:                       min="1"
146:                     />
147:                     <div class="form-text">Délai entre deux OFF successifs (ex. 10 s).</div>
148:                   </div>
149:                 </div>
150: 
151:                 <div class="row g-3">
152:                   <div class="col-12 col-md-6">
153:                     <label class="form-label" for="hysteresis_celsius">Hystérésis (°C)</label>
154:                     <input
155:                       class="form-control"
156:                       id="hysteresis_celsius"
157:                       name="hysteresis_celsius"
158:                       value="{{ settings.get('hysteresis_celsius') }}"
159:                     />
160:                   </div>
161: 
162:                   <div class="col-12 col-md-6">
163:                     <label class="form-label" for="api_quota_warning_threshold">Seuil d'alerte quota</label>
164:                     <input
165:                       class="form-control"
166:                       id="api_quota_warning_threshold"
167:                       name="api_quota_warning_threshold"
168:                       type="number"
169:                       min="0"
170:                       max="10000"
171:                       value="{{ settings.get('api_quota_warning_threshold', quota_warning_threshold) }}"
172:                     />
173:                     <div class="form-text">Bannière d'alerte lorsque les appels restants passent sous cette valeur.</div>
174:                   </div>
175: 
176:                   <div class="col-12 col-md-6">
177:                     <label class="form-label" for="timezone">Fuseau horaire</label>
178:                     <input
179:                       class="form-control"
180:                       id="timezone"
181:                       name="timezone"
182:                       value="{{ settings.get('timezone', 'Europe/Paris') }}"
183:                       placeholder="Europe/Paris"
184:                       autocapitalize="none"
185:                       autocomplete="off"
186:                       spellcheck="false"
187:                     />
188:                     <div class="form-text">Utilisé pour interpréter les fenêtres horaires (identifiant IANA, ex: Europe/Paris, UTC).</div>
189:                   </div>
190: 
191:                   <div class="col-12">
192:                     <div class="form-check mb-2">
193:                       <input
194:                         class="form-check-input"
195:                         type="checkbox"
196:                         id="turn_off_outside_windows"
197:                         name="turn_off_outside_windows"
198:                         {% if settings.get('turn_off_outside_windows') %}checked{% endif %}
199:                       />
200:                       <label class="form-check-label" for="turn_off_outside_windows">Éteindre en dehors des fenêtres horaires</label>
201:                     </div>
202:                   </div>
203: 
204:                   <div class="col-12 col-md-6">
205:                     <label class="form-label" for="meter_device_id">ID du capteur Meter</label>
206:                     <input class="form-control" id="meter_device_id" name="meter_device_id" value="{{ settings.get('meter_device_id') }}" />
207:                   </div>
208: 
209:                   <div class="col-12 col-md-6">
210:                     <label class="form-label" for="aircon_device_id">ID de la télécommande IR</label>
211:                     <input class="form-control" id="aircon_device_id" name="aircon_device_id" value="{{ settings.get('aircon_device_id') }}" />
212:                     <div class="form-text">Identifiant de la télécommande infrarouge (remoteType: Air Conditioner).</div>
213:                   </div>
214:                 </div>
215: 
216:                 <hr />
217: 
218:                 <div class="section-heading mb-2">
219:                   <label class="form-label mb-0">Fenêtre horaire</label>
220:                   <span class="badge rounded-pill bg-secondary-subtle text-secondary-emphasis">optimisé mobile</span>
221:                 </div>
222:                 <div class="small text-muted mb-2">Sélectionnez les jours puis choisissez l'heure de début et de fin (format 24h).</div>
223:                 <div class="border rounded-3 p-3 mb-3 time-window-card">
224:                   <div class="row g-3">
225:                     <div class="col-12">
226:                       <label class="form-label d-block">Jours</label>
227:                       <div class="d-flex flex-wrap gap-2">
228:                         {% for day in day_choices %}
229:                           <div class="form-check form-check-inline day-chip">
230:                             <input
231:                               class="btn-check"
232:                               type="checkbox"
233:                               id="day_{{ day.value }}"
234:                               name="time_window_days"
235:                               value="{{ day.value }}"
236:                               aria-describedby="time_window_days_summary"
237:                               {% if day.value in time_window_form['days'] %}checked{% endif %}
238:                             />
239:                             <label class="btn btn-outline-primary btn-sm" for="day_{{ day.value }}">{{ day.label }}</label>
240:                           </div>
241:                         {% endfor %}
242:                       </div>
243:                       <div id="time_window_days_summary" class="form-text" aria-live="polite">
244:                         {{ time_window_form['days'] | length }} jour(s) sélectionné(s).
245:                       </div>
246:                     </div>
247:                     <div class="col-6">
248:                       <label class="form-label" for="time_window_start">Début</label>
249:                       <select class="form-select" id="time_window_start" name="time_window_start" aria-describedby="time_window_help">
250:                         <option value="">Choisir…</option>
251:                         {% for choice in time_choices %}
252:                           <option value="{{ choice }}" {% if time_window_form['start'] == choice %}selected{% endif %}>{{ choice }}</option>
253:                         {% endfor %}
254:                       </select>
255:                     </div>
256:                     <div class="col-6">
257:                       <label class="form-label" for="time_window_end">Fin</label>
258:                       <select class="form-select" id="time_window_end" name="time_window_end" aria-describedby="time_window_help">
259:                         <option value="">Choisir…</option>
260:                         {% for choice in time_choices %}
261:                           <option value="{{ choice }}" {% if time_window_form['end'] == choice %}selected{% endif %}>{{ choice }}</option>
262:                         {% endfor %}
263:                       </select>
264:                     </div>
265:                     <div class="col-12">
266:                       <div id="time_window_help" class="form-text">
267:                         Astuce : si aucun jour n'est sélectionné, la fenêtre horaire est considérée comme inactive.
268:                       </div>
269:                     </div>
270:                   </div>
271:                 </div>
272: 
273:                 <hr />
274: 
275:                 {% set winter_profile = settings.get('winter', {}) %}
276:                 <h2 class="h6">Profil hiver</h2>
277:                 <div class="row g-2 mb-3">
278:                   <div class="col-4">
279:                     <label class="form-label" for="winter_min_temp">Min.</label>
280:                     <select class="form-select" id="winter_min_temp" name="winter_min_temp">
281:                       {% for choice in temp_choices %}
282:                         <option value="{{ choice.value }}" {% if (winter_profile.get('min_temp') | float) == choice.value %}selected{% endif %}>
283:                           {{ choice.label }}°C
284:                         </option>
285:                       {% endfor %}
286:                     </select>
287:                   </div>
288:                   <div class="col-4">
289:                     <label class="form-label" for="winter_max_temp">Max.</label>
290:                     <select class="form-select" id="winter_max_temp" name="winter_max_temp">
291:                       {% for choice in temp_choices %}
292:                         <option value="{{ choice.value }}" {% if (winter_profile.get('max_temp') | float) == choice.value %}selected{% endif %}>
293:                           {{ choice.label }}°C
294:                         </option>
295:                       {% endfor %}
296:                     </select>
297:                   </div>
298:                   <div class="col-4">
299:                     <label class="form-label" for="winter_target_temp">Cible</label>
300:                     <select class="form-select" id="winter_target_temp" name="winter_target_temp">
301:                       {% for choice in temp_choices %}
302:                         <option value="{{ choice.value }}" {% if (winter_profile.get('target_temp') | float) == choice.value %}selected{% endif %}>
303:                           {{ choice.label }}°C
304:                         </option>
305:                       {% endfor %}
306:                     </select>
307:                   </div>
308:                   <div class="col-6">
309:                     <label class="form-label" for="winter_ac_mode">Mode clim</label>
310:                     <select class="form-select" id="winter_ac_mode" name="winter_ac_mode">
311:                       {% for choice in ac_mode_choices %}
312:                         <option value="{{ choice.value }}" {% if (winter_profile.get('ac_mode') | int) == choice.value %}selected{% endif %}>
313:                           {{ choice.label }}
314:                         </option>
315:                       {% endfor %}
316:                     </select>
317:                   </div>
318:                   <div class="col-6">
319:                     <label class="form-label" for="winter_fan_speed">Vitesse ventilateur</label>
320:                     <select class="form-select" id="winter_fan_speed" name="winter_fan_speed">
321:                       {% for choice in fan_speed_choices %}
322:                         <option value="{{ choice.value }}" {% if (winter_profile.get('fan_speed') | int) == choice.value %}selected{% endif %}>
323:                           {{ choice.label }}
324:                         </option>
325:                       {% endfor %}
326:                     </select>
327:                   </div>
328:                 </div>
329: 
330:                 {% set summer_profile = settings.get('summer', {}) %}
331:                 <h2 class="h6">Profil été</h2>
332:                 <div class="row g-2">
333:                   <div class="col-4">
334:                     <label class="form-label" for="summer_min_temp">Min.</label>
335:                     <select class="form-select" id="summer_min_temp" name="summer_min_temp">
336:                       {% for choice in temp_choices %}
337:                         <option value="{{ choice.value }}" {% if (summer_profile.get('min_temp') | float) == choice.value %}selected{% endif %}>
338:                           {{ choice.label }}°C
339:                         </option>
340:                       {% endfor %}
341:                     </select>
342:                   </div>
343:                   <div class="col-4">
344:                     <label class="form-label" for="summer_max_temp">Max.</label>
345:                     <select class="form-select" id="summer_max_temp" name="summer_max_temp">
346:                       {% for choice in temp_choices %}
347:                         <option value="{{ choice.value }}" {% if (summer_profile.get('max_temp') | float) == choice.value %}selected{% endif %}>
348:                           {{ choice.label }}°C
349:                         </option>
350:                       {% endfor %}
351:                     </select>
352:                   </div>
353:                   <div class="col-4">
354:                     <label class="form-label" for="summer_target_temp">Cible</label>
355:                     <select class="form-select" id="summer_target_temp" name="summer_target_temp">
356:                       {% for choice in temp_choices %}
357:                         <option value="{{ choice.value }}" {% if (summer_profile.get('target_temp') | float) == choice.value %}selected{% endif %}>
358:                           {{ choice.label }}°C
359:                         </option>
360:                       {% endfor %}
361:                     </select>
362:                   </div>
363:                   <div class="col-6">
364:                     <label class="form-label" for="summer_ac_mode">Mode clim</label>
365:                     <select class="form-select" id="summer_ac_mode" name="summer_ac_mode">
366:                       {% for choice in ac_mode_choices %}
367:                         <option value="{{ choice.value }}" {% if (summer_profile.get('ac_mode') | int) == choice.value %}selected{% endif %}>
368:                           {{ choice.label }}
369:                         </option>
370:                       {% endfor %}
371:                     </select>
372:                   </div>
373:                   <div class="col-6">
374:                     <label class="form-label" for="summer_fan_speed">Vitesse ventilateur</label>
375:                     <select class="form-select" id="summer_fan_speed" name="summer_fan_speed">
376:                       {% for choice in fan_speed_choices %}
377:                         <option value="{{ choice.value }}" {% if (summer_profile.get('fan_speed') | int) == choice.value %}selected{% endif %}>
378:                           {{ choice.label }}
379:                         </option>
380:                       {% endfor %}
381:                     </select>
382:                   </div>
383:                 </div>
384: 
385:                 <div class="mt-4">
386:                   <button class="btn btn-primary w-100 w-md-auto" type="submit">Enregistrer les réglages</button>
387:                 </div>
388: 
389:                 <hr class="my-4" />
390: 
391:                 <h2 class="h6">Webhooks IFTTT (Priorité)</h2>
392:                 <p class="small text-muted">
393:                   Renseignez les URLs des webhooks IFTTT pour déclencher vos scènes via le cloud. Les webhooks sont prioritaires sur les scènes SwitchBot natives.
394:                 </p>
395:                 <div class="row g-3 mb-4">
396:                   {% for key in aircon_scene_keys %}
397:                     <div class="col-12 col-md-6">
398:                       <label class="form-label" for="webhook_{{ key }}_url">{{ aircon_scene_labels[key] }}</label>
399:                       <input
400:                         class="form-control"
401:                         id="webhook_{{ key }}_url"
402:                         name="webhook_{{ key }}_url"
403:                         value="{{ ifttt_webhooks[key] }}"
404:                         placeholder="https://maker.ifttt.com/trigger/..."
405:                         type="url"
406:                       />
407:                       {% if missing_webhooks[key] %}
408:                         <div class="form-text text-warning">Non configuré (fallback vers scène SwitchBot)</div>
409:                       {% else %}
410:                         <div class="form-text text-success">Prêt</div>
411:                       {% endif %}
412:                     </div>
413:                   {% endfor %}
414:                 </div>
415: 
416:                 <h2 class="h6">Scènes favorites SwitchBot (Fallback)</h2>
417:                 <p class="small text-muted">
418:                   Renseignez les IDs des scènes favorites (SwitchBot → Scenes). Elles servent de fallback si les webhooks IFTTT échouent ou ne sont pas configurés.
419:                 </p>
420:                 <div class="row g-3">
421:                   {% for key in aircon_scene_keys %}
422:                     <div class="col-12 col-md-6 col-lg-3">
423:                       <label class="form-label" for="scene_{{ key }}_id">{{ aircon_scene_labels[key] }}</label>
424:                       <input
425:                         class="form-control"
426:                         id="scene_{{ key }}_id"
427:                         name="scene_{{ key }}_id"
428:                         value="{{ aircon_scenes[key] }}"
429:                         placeholder="UUID scène"
430:                       />
431:                       {% if missing_scenes[key] %}
432:                         <div class="form-text text-warning">Non configuré</div>
433:                       {% else %}
434:                         <div class="form-text text-success">Prêt</div>
435:                       {% endif %}
436:                     </div>
437:                   {% endfor %}
438:                 </div>
439:               </form>
440:             </div>
441:           </div>
442:         </div>
443: 
444:         <div class="col-12 col-xl-3">
445:           <div class="card h-100">
446:             <div class="card-header">Résumé rapide</div>
447:             <div class="card-body">
448:               <dl class="row mb-0 small">
449:                 <dt class="col-7">Mode actuel</dt>
450:                 <dd class="col-5 text-end text-capitalize">{{ settings.get('mode', 'winter') }}</dd>
451: 
452:                 <dt class="col-7">Seuil alerte quota</dt>
453:                 <dd class="col-5 text-end">{{ quota_warning_threshold }}</dd>
454: 
455:                 <dt class="col-7">Fenêtre horaire</dt>
456:                 <dd class="col-5 text-end">
457:                   {% if time_window_form['days'] %}
458:                     {{ time_window_form['start'] or '--:--' }} → {{ time_window_form['end'] or '--:--' }}
459:                   {% else %}
460:                     Aucune
461:                   {% endif %}
462:                 </dd>
463: 
464:                 <dt class="col-7">Webhooks IFTTT</dt>
465:                 <dd class="col-5 text-end">
466:                   {{ configured_webhooks_count }} / {{ aircon_scene_keys | length }}
467:                 </dd>
468: 
469:                 <dt class="col-7">Scènes configurées</dt>
470:                 <dd class="col-5 text-end">
471:                   {{ configured_scenes_count }} / {{ aircon_scene_keys | length }}
472:                 </dd>
473:               </dl>
474:               <div class="mt-3">
475:                 <p class="small text-muted mb-2">Besoin d'un rafraîchissement ?</p>
476:                 <a class="btn btn-outline-light w-100" href="{{ url_for('dashboard.index') }}">Voir l'état en temps réel</a>
477:               </div>
478:             </div>
479:           </div>
480:         </div>
481:       </div>
482:     </div>
483:     
484:     {% include '_footer_nav.html' %}
485:     
486:     <script src="{{ url_for('static', filename='js/alerts.js') }}"></script>
487:     <script src="{{ url_for('static', filename='js/settings.js') }}"></script>
488:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
489:     <script src="{{ url_for('static', filename='js/bottom-nav.js') }}"></script>
490:     <script src="{{ url_for('static', filename='js/performance-optimizer.js') }}"></script>
491:   </body>
492: </html>
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
395:     <!-- Preconnect for External Domains -->
396:     <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin="anonymous" />
397:     <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin="anonymous" />
398:     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
399:     
400:     <!-- Preload Critical Resources -->
401:     <link rel="preload" href="{{ url_for('static', filename='css/theme.css') }}" as="style" onload="this.onload=null;this.rel='stylesheet'" />
402:     <link rel="preload" href="{{ url_for('static', filename='css/index.css') }}" as="style" onload="this.onload=null;this.rel='stylesheet'" />
403:     <link rel="preload" href="{{ url_for('static', filename='js/loaders.js') }}" as="script" />
404:     <link rel="preload" href="{{ url_for('static', filename='js/advanced-optimizer.js') }}" as="script" />
405:     
406:     <!-- Font Loading Optimization -->
407:     <link rel="preload" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'" />
408:     
409:     <!-- Bootstrap CSS -->
410:     <link
411:       href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
412:       rel="stylesheet"
413:       integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDS..."
414:       crossorigin="anonymous"
415:     />
416:     
417:     <!-- Non-Critical CSS (loaded after critical) -->
418:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-cards.css') }}" media="print" onload="this.media='all'" />
419:     <link rel="stylesheet" href="{{ url_for('static', filename='css/sticky-footer.css') }}" media="print" onload="this.media='all'" />
420:     
421:     <!-- FontAwesome -->
422:     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
423:     
424:     <!-- Critical JS for Performance -->
425:     <script>
426:       // Performance mark for critical resources start
427:       if ('performance' in window && 'mark' in performance) {
428:         performance.mark('critical-css-start');
429:       }
430:     </script>
431:     <link rel="stylesheet" href="{{ url_for('static', filename='css/theme.css') }}" />
432:     <link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}" />
433:   </head>
434:   <body class="sb-dark sb-page sb-dashboard">
435: 
436: <!-- Enhanced anti-flash script for body -->
437: <script>
438:   // Ensure dark theme is applied immediately when body loads
439:   document.body.style.backgroundColor = '#030712';
440:   document.body.style.color = '#f4f7ff';
441:   
442:   // Add dark theme class immediately
443:   document.body.classList.add('sb-dark');
444: </script>
445:     <div class="sb-page__gradient"></div>
446:     <main class="sb-page__content">
447:       <div class="container py-5 py-lg-6">
448:         <section class="sb-card sb-card-hero sb-card-hover mb-4" role="region" aria-label="Présentation SwitchBot">
449:           <div class="sb-card-hero__content">
450:             <div class="sb-card-hero__text">
451:               <p class="sb-card__eyebrow">Tableau de bord</p>
452:               <h1 class="sb-hero__title">SwitchBot Dashboard</h1>
453:               <p class="sb-hero__subtitle">
454:                 Surveillez l'état actuel, vos quotas et déclenchez les actions clés sans quitter cette page.
455:               </p>
456:             </div>
457:             <div class="sb-hero__cta">
458:               <a class="btn btn-outline-light sb-button-active" href="{{ url_for('dashboard.settings_page') }}" data-loader>
459:                 <i class="fas fa-sliders-h me-2"></i>
460:                 Voir les réglages
461:               </a>
462:               <a class="btn btn-primary sb-button-active" href="{{ url_for('dashboard.actions_page') }}" data-loader>
463:                 <i class="fas fa-bolt me-2"></i>
464:                 Actions rapides
465:               </a>
466:             </div>
467:           </div>
468:         </section>
469: 
470:         {% if show_quota_warning %}
471:           <section class="sb-card sb-card--warning sb-card-hover mb-3 quota-panel" role="status">
472:             <div class="quota-panel__icon">
473:               <i class="fas fa-triangle-exclamation"></i>
474:             </div>
475:             <div class="quota-panel__content">
476:               <p class="quota-panel__title">Attention : quota API faible</p>
477:               <p class="quota-panel__subtitle">
478:                 Il ne reste que {{ api_requests_remaining }} appels (seuil {{ quota_warning_threshold }}).
479:               </p>
480:             </div>
481:             <div class="quota-panel__action">
482:               <a class="btn btn-outline-light btn-sm" href="{{ url_for('dashboard.quota') }}" data-loader>
483:                 Voir le quota
484:               </a>
485:             </div>
486:           </section>
487:         {% endif %}
488: 
489:         {% with messages = get_flashed_messages(with_categories=true) %}
490:           {% if messages %}
491:             <section class="mb-3" aria-live="polite" aria-atomic="true">
492:               {% for category, message in messages %}
493:                 <article class="alert {{ 'alert-danger' if category == 'error' else 'alert-success' }}" role="alert" data-auto-dismiss="6000">
494:                   {{ message }}
495:                 </article>
496:               {% endfor %}
497:             </section>
498:           {% endif %}
499:         {% endwith %}
500: 
501:         <section class="sb-card sb-card-hover mb-4">
502:           <div class="sb-card__header">
503:             <div>
504:               <p class="sb-card__eyebrow">Statut actuel</p>
505:               <h2 class="sb-card__title">Données en temps réel</h2>
506:             </div>
507:             <div class="sb-card__meta text-muted">Dernière mise à jour {{ state.get('last_read_at') }}</div>
508:           </div>
509:           <div class="sb-card__body">
510:             <div class="status-grid">
511:               <article class="status-item sb-card-hover">
512:                 <div class="status-label">Température</div>
513:                 <div class="status-value temperature-value">
514:                   {{ state.get('last_temperature') }}
515:                 </div>
516:                 {% if state.get('last_temperature_stale') %}
517:                   <span class="badge bg-secondary-subtle text-secondary-emphasis status-badge">
518:                     Donnée potentiellement obsolète
519:                   </span>
520:                 {% endif %}
521:               </article>
522: 
523:               <article class="status-item sb-card-hover">
524:                 <div class="status-label">Humidité</div>
525:                 <div class="status-value humidity-value">
526:                   {{ state.get('last_humidity') }}
527:                 </div>
528:               </article>
529: 
530:               <article class="status-item sb-card-hover">
531:                 <div class="status-label">Climatisation supposée</div>
532:                 <div class="status-value">
533:                   {% if state.get('assumed_aircon_power') == 'on' %}
534:                     <span class="text-success">ON</span>
535:                   {% else %}
536:                     <span class="text-secondary">OFF</span>
537:                   {% endif %}
538:                 </div>
539:                 <p class="status-value--muted mb-0">
540:                   {{ state.get('last_action') or 'Aucune action' }}
541:                 </p>
542:               </article>
543: 
544:               <article class="status-item sb-card-hover">
545:                 <div class="status-label">Dernière erreur</div>
546:                 <div class="status-value status-value--muted">
547:                   {{ state.get('last_error') or 'Aucune erreur' }}
548:                 </div>
549:               </article>
550:             </div>
551:           </div>
552:         </section>
553: 
554:         <section class="scene-actions-wrapper sb-card sb-card-hover">
555:           <div class="scene-actions-container text-center">
556:             <p class="text-muted mb-0 scene-actions__subtitle">
557:               <i class="fas fa-bolt me-2"></i>
558:               Accédez à toutes les actions manuelles via la page <strong>Actions</strong>
559:             </p>
560:             <a href="{{ url_for('dashboard.actions_page') }}" class="btn btn-primary rounded-m shadow-l" data-loader>
561:               <i class="fas fa-arrow-right me-2"></i>
562:               Voir les actions
563:             </a>
564:           </div>
565:         </section>
566:       </div>
567:     </main>
568:     
569:     {% include '_footer_nav.html' %}
570:     
571:     <script src="{{ url_for('static', filename='js/alerts.js') }}"></script>
572:     <script src="{{ url_for('static', filename='js/loaders.js') }}"></script>
573:     <script src="{{ url_for('static', filename='js/bottom-nav.js') }}"></script>
574:     <script src="{{ url_for('static', filename='js/performance-optimizer.js') }}"></script>
575:     <script src="{{ url_for('static', filename='js/advanced-optimizer.js') }}"></script>
576:     
577:     <!-- Enhanced Performance Optimization Script -->
578:     <script>
579:       // Mark critical CSS loading complete
580:       if ('performance' in window && 'mark' in performance) {
581:         performance.mark('critical-css-loaded');
582:         performance.measure('critical-css-load-time', 'critical-css-start', 'critical-css-loaded');
583:       }
584:       
585:       // Initialize advanced performance optimizations
586:       if ('requestIdleCallback' in window) {
587:         requestIdleCallback(() => {
588:           console.log('🚀 Advanced Performance Optimizer initialized');
589:         });
590:       }
591:       
592:       // Ensure dark theme is maintained after load
593:       window.addEventListener('load', function() {
594:         document.body.style.backgroundColor = '#030712';
595:         document.body.style.color = '#f4f7ff';
596:       });
597:     </script>
598:   </body>
599: </html>
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
