# Audit Backend Complet - SwitchBot Dashboard v2

---

## 1) Aperçu rapide

- Le backend est une architecture Python Flask avec une approche de stockage unifiée via PostgreSQL (Neon) par défaut et un fallback JSON filesystem. Il intègre un système d’orchestration d’actions (IFTTT → Scènes SwitchBot → Commandes directes), un planificateur APScheduler et une logique de gestion des quotas API SwitchBot.
- Les composants clés: stores (PostgresStore, JsonStore, RedisJsonStore deprecated), HistoryService, SchedulerService, AutomationService, SwitchBotClient, IFTTTWebhookClient, ApiQuotaTracker, routes Flask.
- Déploiement/OPS: Docker multi-stage, Gunicorn mono-worker (ou worker dédié selon le mode), Render GHCR déployement, healthz endpoint. Tests unitaires via pytest avec mocks.
- Points forts: architecture modulaire, sauvegarde/transparence Failover (PG + JSON), quotas API surveillés localement et via headers, observabilité via logs structurés et endpoint healthz.

---

## 2) Architecture et composants Backend

- Stockage
  - PostgreSQL comme source de vérité principale (PostgresStore) avec un fallback automatique vers JsonStore en cas d’échec (pattern “Stockage Unifié, Fallback Transparent”).
  - Schéma json_store (kind: settings ou state) et table state_history pour l’historique, avec retention alignée sur Neon PITR (6h).
  - Connexion via psycopg_pool; pool partagé optimalisé et injection dans les divers services.
- Cœur métier
  - AutomationService: boucle principale (tick) qui lit meters, applique fenêtres temporelles, hysteresis et orchestrations cascade IFTTT → Scènes → Direct.
  - SchedulerService: APScheduler intégré, unique worker, intervalle adaptatif (in-window / warmup / idle), gestion des OFF repeats, et wrapper `_run_tick_safe()` pour éviter les crashes.
  - HistoryService: écriture par lot (batch inserts) dans PostgreSQL, avec flush périodique et logique d’agrégation et récupération history (get_history, get_aggregates, get_latest_records).
- Intégrations et API externe
  - SwitchBotClient: gestion des appels SwitchBot (signature HMAC, retries, quotas via ApiQuotaTracker).
  - IFTTTWebhookClient: déclenchement des webhooks IFTTT, validation strict des URLs HTTPS uniquement et protection SSRF.
  - ApiQuotaTracker: double mécanisme (compte local + synchronisation via headers X-RateLimit-*) et réinitialisation quotidienne à minuit UTC.
- UI et endpoints
  - Routes Flask: routes UI, endpoints historiques (/history/api/*), quota, healthz, debug/state.
  - CSRF protection généralisée via Flask-WTF CSRFProtect et intercepteurs JS pour CSRF sur les requêtes XHR/FETCH.
- Déploiement et Observabilité
  - Dockerfile multi-stage, Gunicorn avec un seul worker en production pour éviter les duplications APScheduler.
  - HEALTHCHECK et endpoint /healthz pour le monitoring interne.
- Tests et qualité
  - Tests unitaires et d’intégration couvrant les modules clés (switchbot_api, history_service, scheduler, routes).
  - Mocks et fixtures (tests/conftest.py) pour isoler les couches et éviter les appels réseau réels en CI.

---

## 3) Points forts identifiés

- Disponibilité et résilience: mécanisme de fallback store (Postgres → JsonStore) et base pour robustesse en cas d’indisponibilité du back-end principal.
- Contrôle du quota: double tracking (local + header) et alertes UI via quota banner, avec réinitialisation quotidienne.
- Performance backend: écriture historisée en batch (HistoryService), planificateur APScheduler avec un seul worker pour éviter les duplicates, cache timezone dans AutomationService.
- Observabilité: logs structurés, endpoint healthz riche, tests et couverture en amélioration continue (Phase 2/3 dans memory bank).
- Architecture offline-first côté frontend est bien prise en compte et documentée, mais cela influence aussi le backend en termes de cohérence et de tests (voir section sécurité).

---

## 4) Risques et vulnérabilités potentielles

- Sécurité des secrets
  - CRIT-01 dans le plan d’audit mentionne fuite de clé IFTTT dans config/settings.json (exemple - durcis). Risque élevé si secrets exposés publiquement.
  CRITIQUE: stocker les secrets dans l’environnement (env vars) plutôt que dans fichiers commités, et ajouter des règles .gitignore robustes.
- Secret Flask par défaut
  - Clé FLASK_SECRET_KEY par défaut en production peut permettre la falsification de cookies (CRIT-02). Mise en place nécessaire: bloquer le démarrage sans secret en prod.
- Points de démarrage
  - CRIT-03 NameError éventuel lors de Postgres KO si import manquant (timedelta). Vérifier l’import correct (dt.timedelta) et tests dans routes/history.
- Couverture de tests
  - Tests actuels à 70% dans le doc backend, objectif 85%. Besoin d’augmenter la couverture, en particulier autour du SwitchBotClient, HistoryService, et l’intégration du pipeline IFTTT.
- Cas d’erreur produit
  - Scénarios “history api data” retournant 503 en prod si store indisponible; vérifier les messages d’erreur et UX correspondante.

---

## 5) Plan d’action priorisé (high level)

- Phase A - Sécurité et conformité (1-2 semaines)
  1) Sécurité des secrets
     - Supprimer les secrets des dépôts (move vers env). Ajouter settings.json.example et(.gitignore) pour exclure settings.json/state.json de git.
     - Remplacer SWITCHBOT_TOKEN et SWITCHBOT_SECRET dans le code par des appels via les variables d’environnement ou un vault secret si disponible.
  2) Clé Flask en prod
     - Modifier switchbot_dashboard/__init__.py pour bloquer le démarrage si FLASK_SECRET_KEY manquante et non en mode debug.
  3) Webhooks IFTTT
     - S’assurer SSRF defense sur validate_webhook_url et restreindre les destinations à maker.ifttt.com
  4) Correctifs critiques du Backlog Sonar
     - Corriger le NameError sur timedelta dans routes.py et robustifier les imports.
- Phase B - Stabilisation et qualité (2-4 semaines)
  5) Couverture des tests et mocks
     - Élargir tests sur switchbot_api, quota, history_service et les endpoints historiques.
  6) Agriculture du code et robustesse
     - Unifier le pattern de transaction au niveau PostgresStore (exposer pool via property), éviter l’accès à des attributs privés.
     - Ajout de tests d’intégration autour du pipeline IFTTT → Scènes → Commandes directes.
  7) Hardened health et monitoring
     - Améliorer healthz: inclure plus d’indicateurs (latence moyenne du tick, état de la base, last_tick exact).
- Phase C - Performance et scalabilité (4-8 semaines)
  8) Déport du planificateur
     - Envisager un worker APScheduler séparé ou Redis/Celery pour permettre scale-out horizontal sans duplication des ticks.
  9) Optimisations performance avancées
     - Mise en place de batching plus agressif dans HistoryService et consolidation des appels d’écriture.
     - Vérifier l’utilisation des Web Workers côté frontend mais prévoir impacts backend.
  10) Sécurité et compliance continue
     - Mettre en place des scans automatiques (SonarCloud) et un plan de remediation pour les futures vulnérabilités.

---

## 6) Recommandations techniques spécifiques (gaps et améliorations)

- Stockage et sécurité
  - Migration progressive vers une gestion strictement centralisée des secrets via variables d’environnement et un coffre (Secrets Manager).
  - Vérifier les endpoints sensibles (/history/api/*) et limiter le débit via Flask-Limiter (déjà présent) et s’assurer que le fallback est bien protégé.
- Endpoints et architecture
  - Consolider la gestion du pool Postgres pour éviter les connexions excessives lors du démarrage et du scaling.
  - Assurer que HistoryService est toujours opérationnel ou qu’un fallback mock est disponible dans l’UI.
- Tests et CI
  - Étendre les tests sur les cas critiques (Ifttt, quotas, historique, scheduler).
  - Ajouter des tests de failover et de résilience (Postgres KO, RedisJsonStore forced fallback).
- Déploiement et sécurité
  - Vérifier les secrets dans `.env.example` et tests ne doivent pas lire des secrets réels.
  - Considérer checks dans CI pour s’assurer que .env et settings.json ne sont pas commités.

---

## 7) Vérifications opérationnelles (checklist rapide)

- [ ] Secrets stockés hors code et protégés par l’environnement (et .gitignore renforcé)
- [ ] Clé Flask en prod est obligatoirement définie (ou arrêt du boot)
- [ ] Validation des webhooks IFTTT uniquement en HTTPS et domaine maker.ifttt.com
- [ ] Cas de KO Postgres gérés correctement (fallback + logs)
- [ ] Plan d’action et tickets ouverts pour les failles identifiées
- [ ] Couverture des tests ≥ 85% (priorité sur switchbot_api, history_service, routes)
- [ ] Endpoint /healthz donne une image exacte de l’état système
- [ ] Déploiement CI/CD avec détection d’échecs et rollback possible
- [ ] Documentation technique mise à jour pour les choix d’architecture et les patterns sécurisés

---

## 8) Conclusion

Le backend SwitchBot Dashboard v2 est une architecture robuste et bien pensée, conçue pour la résilience opérationnelle (double store, cascade d’action, quotas). Toutefois, il y a des risques critiques autour des secrets et des configurations par défaut, et la couverture de tests doit être renforcée pour atteindre les objectifs qualité. Un plan d’action structuré, avec des quick wins (sécurité et correctifs critiques) et des évolutions progressives vers la scalabilité et le monitoring, permettra d’assurer une stabilité et une sécurité durables tout en conservant les bénéfices de l’approche 
