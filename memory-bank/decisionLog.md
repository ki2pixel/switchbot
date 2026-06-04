[2026-05-27 13:22:00] - Remédiation Phase 3 : Scalabilité & Expérience Native (Frontend)
- Décision : Déporter le monitoring continu de performances (FPS, JS Heap) vers un Web Worker dédié (`perf-worker.js`) et implémenter un routeur asynchrone natif (`spa-router.js`) pour éliminer les rechargements complets de pages (SPA Light).
- Motivation : Les calculs de FPS continus sur le thread principal consommaient de la CPU et risquaient de causer des micro-saccades lors du rendu des graphiques. De plus, les rechargements complets de pages lors du changement de menu nuisaient à la fluidité ressentie comme "native".
- Implémentation :
  1. **Web Worker** : Création de `static/js/perf-worker.js` gérant l'agrégation glissante des metrics et l'émission d'avertissements de performance. Remplacement des calculs lourds de `performance-optimizer.js` par un simple comptage de frames envoyé toutes les 10s au worker.
  2. **SPA Light Router** : Création de `static/js/spa-router.js` interceptant les clics de navigation, effectuant un fetch AJAX de fragment, remplaçant `#app-content` avec effet de fondu (150ms), gérant nativement `pushState`/`popstate`, mettant à jour la bottom navigation, et ré-évaluant à chaud les scripts spécifiques de la page (après leur mise en conformité `document.readyState` pour history.js, settings.js et alerts.js).
  3. **Standardisation HTML** : Enveloppement des sections centrales de tous les templates dans un conteneur `#app-content` unifié.
- Implication : L'application offre désormais un rendu asynchrone instantané et soyeux type application native (sans aucun rechargement complet), tout en soulageant totalement le thread principal des calculs de monitoring. Zéro dépendance externe lourde requise, parfaite compatibilité offline-first conservée.


[Archives Q1 2026](file:///home/kidpixel/SwitchBot/memory-bank/archives/decisionLog_2026Q1.md)
