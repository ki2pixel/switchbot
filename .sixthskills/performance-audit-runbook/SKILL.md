
# Runbook Audit Performance

Utiliser ce skill pour vérifier/étendre les optimisations LCP/FID/CLS.

## 1. Préparer les outils
- Scripts : Lighthouse (CLI), WebPageTest, ou Chrome DevTools.
- Fichiers clés : `switchbot_dashboard/static/css/critical.css`, `switchbot_dashboard/static/js/advanced-optimizer.js`, `switchbot_dashboard/static/js/performance-optimizer.js`, `templates/index.html` (resource hints).
- Docs : `docs/guides/ui-navigation.md` (UX mobile), `docs/ops/performance-tuning.md` (optimisations back/front).

## 2. Workflow d’audit
1. **Critical CSS** :
   - Vérifier que le contenu above-the-fold est couvert.
   - Confirmer que le CSS non critique est chargé async (`media="print"`).
2. **Resource hints** :
   - Preconnect/Preload cohérents (Space Grotesk, scripts critiques).
   - Aucun CDN externe non autorisé.
3. **JS optimisations** :
   - `performance-optimizer.js` ne bloque pas le main thread.
   - Prefer `requestIdleCallback`, `Passive event listeners` activés.
4. **Micro-interactions** :
   - Tokens `--sb-scale-*` respectés, `prefers-reduced-motion` géré.
   - Pas de reflow > 10ms.

## 3. Mesures
- Cibles : LCP < 1.8s, FID < 50ms, CLS < 0.05, FCP < 1.2s.
- Enregistrer les résultats (screenshot + JSON) dans `debug/perf/`.
- Comparer mobile (Moto G4) et desktop (Simulated).

## 4. Documentation & communication
- Mettre à jour `docs/guides/ui-navigation.md` (UX) et `docs/ops/performance-tuning.md` (optimisations).
- Ajouter les constats dans Memory Bank (decisionLog + progress) avec date + métriques.
- Si régression détectée, ouvrir un ticket interne (TODO section progress) et planifier correctifs.
