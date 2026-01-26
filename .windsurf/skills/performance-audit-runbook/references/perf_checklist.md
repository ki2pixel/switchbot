# Gabarit Audit Core Web Vitals

## 1. Préparation des mesures
- Commande Lighthouse (mobile):
  ```bash
  npx lighthouse http://localhost:5009 --preset=desktop --output=json --output-path=debug/perf/lh-desktop.json
  ```
- Commande Lighthouse (mobile):
  ```bash
  npx lighthouse http://localhost:5009 --preset=mobile --output=json --output-path=debug/perf/lh-mobile.json
  ```
- WebPageTest : profil "Moto G4 + 4G".

## 2. Table de suivi
| Date | Page | LCP | FID | CLS | Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-01-26 | / | 1.78 s | 28 ms | 0.03 | Critical CSS ok |

## 3. Contrôles front
- Vérifier `templates/index.html` : balises `<link rel="preload">`, `<meta http-equiv="x-dns-prefetch-control">`.
- `static/js/performance-optimizer.js` : garder `requestIdleCallback` et passive listeners.
- `static/css/critical.css` : aucun import externe, variables limitées.

## 4. Checklist micro-interactions
- `prefers-reduced-motion` : toggles CSS dans `theme.css`.
- Transitions `transform/opacity` uniquement.
- `will-change` nettoyé après animation (`animationend`).

## 5. Archivage
- Sauvegarder JSON Lighthouse + captures dans `debug/perf/<date>/`.
- Reporter résultats dans `docs/frontend-mobile-audit.md` + Memory Bank (decisionLog/progress).
