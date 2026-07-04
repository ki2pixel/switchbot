[2026-05-27 13:22:00] - Remédiation Phase 3 : Scalabilité & Expérience Native (Frontend)
- Décision : Déporter le monitoring continu de performances (FPS, JS Heap) vers un Web Worker dédié (`perf-worker.js`) et implémenter un routeur asynchrone natif (`spa-router.js`) pour éliminer les rechargements complets de pages (SPA Light).
- Motivation : Les calculs de FPS continus sur le thread principal consommaient de la CPU et risquaient de causer des micro-saccades lors du rendu des graphiques. De plus, les rechargements complets de pages lors du changement de menu nuisaient à la fluidité ressentie comme "native".
- Implémentation :
  1. **Web Worker** : Création de `static/js/perf-worker.js` gérant l'agrégation glissante des metrics et l'émission d'avertissements de performance. Remplacement des calculs lourds de `performance-optimizer.js` par un simple comptage de frames envoyé toutes les 10s au worker.
  2. **SPA Light Router** : Création de `static/js/spa-router.js` interceptant les clics de navigation, effectuant un fetch AJAX de fragment, remplaçant `#app-content` avec effet de fondu (150ms), gérant nativement `pushState`/`popstate`, mettant à jour la bottom navigation, et ré-évaluant à chaud les scripts spécifiques de la page (après leur mise en conformité `document.readyState` pour history.js, settings.js et alerts.js).
  3. **Standardisation HTML** : Enveloppement des sections centrales de tous les templates dans un conteneur `#app-content` unifié.
- Implication : L'application offre désormais un rendu asynchrone instantané et soyeux type application native (sans aucun rechargement complet), tout en soulageant totalement le thread principal des calculs de monitoring. Zéro dépendance externe lourde requise, parfaite compatibilité offline-first conservée.


[2026-07-04 15:05:00] - Durcissement de la sécurité et observabilité du Backend (Phases A, B, C)
- Décision : Appliquer les préconisations d'isolement de secrets, durcissement du démarrage Flask, sécurisation SSRF DNS pour IFTTT, bufferisation amortie en mémoire de l'historique et enrichissement de `/healthz`.
- Motivation : L'audit a révélé des failles potentielles de fuite de secrets de configuration locale, de contrefaçon de cookies de session Flask (clés par défaut), de rebonds SSRF internes, ainsi qu'un manque d'observabilité de la latence du planificateur de ticks.
- Implémentation :
  1. **Sécurité & Secrets** : Déplacement de la clé IFTTT de settings.json vers l'environnement. Durcissement de `validate_webhook_url` pour résoudre le DNS des webhooks IFTTT et rejeter les adresses privées/locales. Blocage du démarrage en production avec `FLASK_SECRET_KEY` non sécurisée.
  2. **Refactoring & Tests** : Validation systématique de la property `pool` de `PostgresStore`, fermeture sécurisée des curseurs sur échec transactionnel, et création d'une suite de tests `tests/test_backend_hardening.py` couvrant ces sécurités.
  3. **Amortissement & Observabilité** : Rétention en mémoire tampon (max 100) en cas d'erreur d'écriture d'historique PostgreSQL avec planification automatique de retries. Route `/healthz` enrichie avec la connectivité PostgreSQL réelle, la latence moyenne de tick et le dernier tick APScheduler (retourne 503 si dégradé).
- Implication : Le backend est désormais conforme aux meilleures pratiques de sécurité de production et d'isolation des secrets. Il tolère les micro-coupures de base de données PostgreSQL sans perte de données d'historique immédiates et offre aux outils de monitoring un diagnostic riche.

[Archives Q1 2026](file:///home/kidpixel/SwitchBot/memory-bank/archives/decisionLog_2026Q1.md)
