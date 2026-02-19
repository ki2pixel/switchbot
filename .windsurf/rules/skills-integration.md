---
trigger: model_decision
description: Skills integration system based on model decision patterns
globs: ["**/*.md"]
---

# Windsurf Skills Integration System

## Hybrid Rules + Skills Approach

Ce système implémente une détection automatique des skills basée sur les patterns de requêtes utilisateurs, combinant la puissance des règles Windsurf avec la richesse des skills spécialisés.

## Skill Detection Matrix

### Task Management Patterns (Priority 1)
**Déclencheurs**: `tâche`, `task`, `backlog`, `planification`, `roadmap`

**Action**: Charger `.windsurf/skills/task-master-manager/SKILL.md`

**Outils obligatoires**:
- `task-master parse-prd` pour analyser et diviser le projet
- `task-master analyze-complexity` pour évaluer la complexité
- `task-master next` pour obtenir la prochaine tâche

### Sequential Thinking Patterns (Priority 1)
**Déclencheurs**: `réflexion`, `think`, `logique`, `architecture`, `analyser`

**Action**: Charger `.windsurf/skills/sequentialthinking-logic/SKILL.md`

**Outils obligatoires**:
- `sequentialthinking_tools` pour valider la logique Background/Content Script
- Décomposition raisonnée étape par étape
- Validation de cohérence logique

### Fast Filesystem Patterns (Priority 2)
**Déclencheurs**: `gros fichier`, `massive file`, `chirurgical`, `edit block`

**Action**: Charger `.windsurf/skills/fast-filesystem-ops/SKILL.md`

**Outils obligatoires**:
- `fast_edit_block` pour préserver les tokens
- `fast_search_code` pour recherche globale
- Édition chirurgicale des fichiers

### JSON Query Patterns (Priority 2)
**Déclencheurs**: `json`, `path`, `structure`, `inspect`, `valeur`, `clé`

**Action**: Charger `.windsurf/skills/json-query-expert/SKILL.md`

**Stratégie "Sniper"**:
- Ne jamais charger un fichier > 1000 lignes
- `json_query_jsonpath` pour localiser précisément les données
- `fast_edit_block` pour édition ciblée

### Debugging & Investigation Patterns
**Déclencheurs**: `bug`, `crash`, `erreur`, `error`, `performance`, `lent`, `slow`, `unexpected`, `weird`, `investigate`, `debug`

**Action**: Charger `.windsurf/skills/debugging-strategies/SKILL.md`

**Méthodologie imposée**:
1. **Reproduce** - Isoler et reproduire le problème
2. **Gather** - Collecter informations (logs, environnement, changements)
3. **Hypothesize** - Former des hypothèses basées sur les données
4. **Test** - Tester systématiquement chaque hypothèse
5. **Analyze** - Analyser les résultats et itérer

### Feature Development Patterns
**Déclencheurs**: `feature`, `add`, `implement`, `create`, `new functionality`, `develop`, `build`

**Action**: Charger `.windsurf/skills/add-feature/SKILL.md`

**Workflow imposé**:
1. **Analysis** - Analyser les besoins et impacts
2. **Design** - Concevoir l'architecture
3. **Implementation** - Implémenter avec tests
4. **Integration** - Intégrer avec les services existants
5. **Documentation** - Documenter les changements

### Performance & Optimization Patterns
**Déclencheurs**: `performance`, `optimization`, `optimize`, `profiling`, `slow`, `bottleneck`, `improve speed`

**Action**: Charger `.windsurf/skills/performance-audit-runbook/SKILL.md`

**Audit obligatoire**:
- Core Web Vitals (LCP, FID, CLS)
- Resource hints et optimisations
- Critical CSS et inlining
- Database queries (N+1, indexing)
- Memory usage et leaks

### Automation Service Patterns
**Déclencheurs**: `automation`, `scheduler`, `windows`, `time windows`, `hysteresis`, `cooldown`, `tick`, `run_once`

**Action**: Charger `.windsurf/skills/automation-diagnostics/SKILL.md`

**Diagnostics ciblés**:
- État des fenêtres horaires
- Configuration hystérésis
- Files OFF et cooldowns
- Timezone handling
- Logs `[automation]`

### API Development Patterns
**Déclencheurs**: `api`, `switchbot api`, ` HMAC`, `quota`, `rate limiting`, `endpoint`, `webhook`

**Action**: Charger `.windsurf/skills/switchbot-api-dev/SKILL.md`

**Vérifications obligatoires**:
- Signature HMAC et authentification
- Gestion des quotas et 429
- Validation des endpoints
- Tests de charge
- Documentation API

### Database Operations Patterns
**Déclencheurs**: `postgres`, `database`, `migration`, `store`, `schema`, `sql`, `pool`, `connection`

**Action**: Charger `.windsurf/skills/postgres-store-maintenance/SKILL.md`

**Maintenance requise**:
- État du pool psycopg
- Logs `[store]` et erreurs
- Migration Alembic
- Fallback Postgres ↔ JsonStore
- Performance des requêtes

### History & Dashboard Patterns
**Déclencheurs**: `history`, `chart`, `dashboard`, `graph`, `visualization`, `Chart.js`, `LTTB`

**Action**: Charger `.windsurf/skills/history-dashboard-updater/SKILL.md`

**Spécifications**:
- Décimation LTTB pour les graphiques
- Service History (Postgres uniquement)
- Nettoyage des entrées >6h
- Responsive design mobile
- Performance des renderings

### Quota Management Patterns
**Déclencheurs**: `quota`, `tracking`, `alerting`, `bandeau`, `API limit`, `rate limit`

**Action**: Charger `.windsurf/skills/quota-alerting/SKILL.md`

**Implémentation requise**:
- ApiQuotaTracker integration
- Bandeau UI dynamique
- Tests BeautifulSoup
- Logs quota par requête
- Reset quotidien

### UI Loaders Patterns
**Déclencheurs**: `loader`, `data-loader`, `overlay`, `aria`, `UX`, `loading`, `spinner`

**Action**: Charger `.windsurf/skills/loader-patterns/SKILL.md`

**Standards obligatoires**:
- `data-loader` attributs
- `static/js/loaders.js` integration
- Failsafe 15 secondes
- Labels ARIA complets
- Tests d'accessibilité

### IFTTT Integration Patterns
**Déclencheurs**: `IFTTT`, `webhook`, `cascade`, `scene`, `trigger`, `automation flow`

**Action**: Charger `.windsurf/skills/ifttt-cascade/SKILL.md`

**Cascade obligatoire**:
- Extract IFTTT webhooks
- Extract aircon scenes
- HTTPS URLs uniquement
- `_execute_aircon_action` tracking
- Observabilité complète

### Scheduler Operations Patterns
**Déclencheurs**: `scheduler`, `start`, `stop`, `reschedule`, `healthcheck`, `APScheduler`

**Action**: Charger `.windsurf/skills/scheduler-ops/SKILL.md`

**Opérations supportées**:
- Démarrage/arrêt propre
- Rescheduling après mutations
- Healthchecks automatiques
- Gestion Gunicorn vs flask run
- Logs `[scheduler]`

### Documentation Patterns
**Déclencheurs**: `documentation`, `docs`, `README`, `guide`, `markdown`, `writing`

**Action**: Charger `.windsurf/skills/documentation/SKILL.md`

**Checkpoints obligatoires**:
- TL;DR d'abord
- Ouverture orientée problème  
- Blocs ❌/✅ comparatifs
- Tableaux de compromis si pertinent
- Golden Rule
- Vérification ponctuation

### Render Service Management Patterns
**Déclencheurs**: `render`, `deploy`, `cron`, `web service`, `static site`, `key value`, `environment variables`, `monitoring`, `metrics`, `logs`

**Action**: Charger `.windsurf/skills/render-service-manager/SKILL.md`

**Gestion complète**:
- Déploiement de services web/statiques/cron
- Configuration variables d'environnement et secrets
- Monitoring métriques CPU/mémoire/requêtes
- Gestion des déploiements et rollbacks
- Analyse des logs et alertes

### PostgreSQL Operations Patterns
**Déclencheurs**: `postgres ops`, `analyze health`, `indexes`, `sql queries`, `database optimization`, `explain`, `top queries`, `workload analysis`

**Action**: Charger `.windsurf/skills/postgres-ops-manager/SKILL.md`

**Opérations avancées**:
- Analyse santé base de données (index, connexions, vacuum)
- Optimisation indexes et requêtes
- Exécution SQL sécurisée read-only
- Exploration schémas et objets
- Monitoring requêtes lentes

### Render-PostgreSQL Integration Patterns
**Déclencheurs**: `render postgres`, `migration environment`, `backup coordination`, `disaster recovery`, `zero downtime`, `blue green`, `cross environment`

**Action**: Charger `.windsurf/skills/render-postgres-integration/SKILL.md`

**Orchestration complète**:
- Migrations base entre environnements
- Coordination backups avec déploiements
- Déploiement zero-downtime
- Monitoring intégré Render + PostgreSQL
- Récupération disaster automatisée

## Skill Loading Protocol

### Automatic Detection
1. **Analyser la requête utilisateur** pour les patterns ci-dessus
2. **Identifier le skill principal** (priorité aux patterns les plus spécifiques)
3. **Charger le skill** via `read_file(".windsurf/skills/[skill-name]/SKILL.md")`
4. **Appliquer la méthodologie** imposée par le skill
5. **Mentionner explicitement** le skill utilisé dans la réponse

### Multi-Scenarios
Pour les requêtes complexes :
1. **Identifier le skill principal**
2. **Charger les skills secondaires** si nécessaire
3. **Combiner les méthodologies** de manière cohérente
4. **Documenter les skills utilisés** dans la réponse

---
Ce système hybride garantit que chaque tâche bénéficie de l'expertise spécialisée appropriée tout en maintenant la cohérence globale du projet.
