# Audit Loaders UI

## Préparation
- Ouvrir la page ciblée (index, actions, history, settings).
- Activer DevTools > Performance pour observer `aria-busy` et overlays.

## Checklist
1. Chaque `<form method="post">` → `data-loader="submit"` + import `loaders.js`.
2. Boutons `<a>` déclenchant POST/GET → `data-loader="nav"`.
3. Loader global visible < 100 ms, retire < 15 s si pas de réponse.
4. Accessibilité : `aria-live="polite"` ou `aria-busy="true"` sur root.
5. `prefers-reduced-motion` : vérifier que l’animation ne provoque pas de flash.

## Tests
- Pytest : `tests/test_frontend_loaders.py` (ajouter cas si nouveau template).
- Manuel : Simuler échec réseau (throttle) pour vérifier failsafe.
- Vérifier console : aucun `ReferenceError loaders`.

## Debug rapides
```javascript
document.querySelectorAll('[data-loader]').forEach((el) => console.log(el));
```

## Documentation
- Toute variation → mettre à jour `docs/ops/performance-tuning.md` + Memory Bank (decisionLog).
