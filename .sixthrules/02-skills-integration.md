# Sixth Skills Integration System

## Hybrid Rules + Skills Approach

Ce système implémente une détection automatique des skills basée sur les patterns de requêtes utilisateurs, combinant la puissance des règles Sixth avec la richesse des skills spécialisés.

## Skill Detection Matrix

### Debugging & Investigation Patterns
**Déclencheurs**: `bug`, `crash`, `erreur`, `error`, `performance`, `lent`, `slow`, `unexpected`, `weird`, `investigate`, `debug`

**Action**: Charger `.sixthskills/debugging-strategies/SKILL.md`

**Méthodologie imposée**:
1. **Reproduce** - Isoler et reproduire le problème
2. **Gather** - Collecter informations (logs, environnement, changements)
3. **Hypothesize** - Former des hypothèses basées sur les données
4. **Test** - Tester systématiquement chaque hypothèse
5. **Analyze** - Analyser les résultats et itérer

### Feature Development Patterns
**Déclencheurs**: `feature`, `add`, `implement`, `create`, `new functionality`, `develop`, `build`

**Action**: Charger `.sixthskills/add-feature/SKILL.md` + skills métier associés

**Workflow imposé**:
1. **Analysis** - Analyser les besoins et impacts
2. **Design** - Concevoir l'architecture
3. **Implementation** - Implémenter avec tests
4. **Integration** - Intégrer avec les services existants
5. **Documentation** - Documenter les changements

### Performance & Optimization Patterns
**Déclencheurs**: `performance`, `optimization`, `optimize`, `profiling`, `slow`, `bottleneck`, `improve speed`

**Action**: Charger `.sixthskills/performance-audit-runbook/SKILL.md`

**Audit obligatoire**:
- Core Web Vitals (LCP, FID, CLS)
- Resource hints et optimisations
- Critical CSS et inlining
- Database queries (N+1, indexing)
- Memory usage et leaks

### Automation Service Patterns
**Déclencheurs**: `automation`, `scheduler`, `windows`, `time windows`, `hysteresis`, `cooldown`, `tick`, `run_once`

**Action**: Charger `.sixthskills/automation-diagnostics/SKILL.md`

**Diagnostics ciblés**:
- État des fenêtres horaires
- Configuration hystérésis
- Files OFF et cooldowns
- Timezone handling
- Logs `[automation]`

### API Development Patterns
**Déclencheurs**: `api`, `switchbot api`, ` HMAC`, `quota`, `rate limiting`, `endpoint`, `webhook`

**Action**: Charger `.sixthskills/switchbot-api-dev/SKILL.md`

**Vérifications obligatoires**:
- Signature HMAC et authentification
- Gestion des quotas et 429
- Validation des endpoints
- Tests de charge
- Documentation API

### Database Operations Patterns
**Déclencheurs**: `postgres`, `database`, `migration`, `store`, `schema`, `sql`, `pool`, `connection`

**Action**: Charger `.sixthskills/postgres-store-maintenance/SKILL.md`

**Maintenance requise**:
- État du pool psycopg
- Logs `[store]` et erreurs
- Migration Alembic
- Fallback Postgres ↔ JsonStore
- Performance des requêtes

### History & Dashboard Patterns
**Déclencheurs**: `history`, `chart`, `dashboard`, `graph`, `visualization`, `Chart.js`, `LTTB`

**Action**: Charger `.sixthskills/history-dashboard-updater/SKILL.md`

**Spécifications**:
- Décimation LTTB pour les graphiques
- Service History (Postgres uniquement)
- Nettoyage des entrées >6h
- Responsive design mobile
- Performance des renderings

### Quota Management Patterns
**Déclencheurs**: `quota`, `tracking`, `alerting`, `bandeau`, `API limit`, `rate limit`

**Action**: Charger `.sixthskills/quota-alerting/SKILL.md`

**Implémentation requise**:
- ApiQuotaTracker integration
- Bandeau UI dynamique
- Tests BeautifulSoup
- Logs quota par requête
- Reset quotidien

### UI Loaders Patterns
**Déclencheurs**: `loader`, `data-loader`, `overlay`, `aria`, `UX`, `loading`, `spinner`

**Action**: Charger `.sixthskills/loader-patterns/SKILL.md`

**Standards obligatoires**:
- `data-loader` attributs
- `static/js/loaders.js` integration
- Failsafe 15 secondes
- Labels ARIA complets
- Tests d'accessibilité

### IFTTT Integration Patterns
**Déclencheurs**: `IFTTT`, `webhook`, `cascade`, `scene`, `trigger`, `automation flow`

**Action**: Charger `.sixthskills/ifttt-cascade/SKILL.md`

**Cascade obligatoire**:
- Extract IFTTT webhooks
- Extract aircon scenes
- HTTPS URLs uniquement
- `_execute_aircon_action` tracking
- Observabilité complète

### Scheduler Operations Patterns
**Déclencheurs**: `scheduler`, `start`, `stop`, `reschedule`, `healthcheck`, `APScheduler`

**Action**: Charger `.sixthskills/scheduler-ops/SKILL.md`

**Opérations supportées**:
- Démarrage/arrêt propre
- Rescheduling après mutations
- Healthchecks automatiques
- Gestion Gunicorn vs flask run
- Logs `[scheduler]`

### Documentation Patterns
**Déclencheurs**: `documentation`, `docs`, `README`, `guide`, `markdown`, `writing`

**Action**: Charger `.sixthskills/documentation/SKILL.md`

**Checkpoints obligatoires**:
- TL;DR d'abord
- Ouverture orientée problème  
- Blocs ❌/✅ comparatifs
- Tableaux de compromis si pertinent
- Golden Rule
- Vérification ponctuation

## Skill Loading Protocol

### Automatic Detection
1. **Analyser la requête utilisateur** pour les patterns ci-dessus
2. **Identifier le skill principal** (priorité aux patterns les plus spécifiques)
3. **Charger le skill** via `read_file(".sixthskills/[skill-name]/SKILL.md")`
4. **Appliquer la méthodologie** imposée par le skill
5. **Mentionner explicitement** le skill utilisé dans la réponse

### Multi-Scenarios
Pour les requêtes complexes :
1. **Identifier le skill principal**
2. **Charger les skills secondaires** si nécessaire
3. **Combiner les méthodologies** de manière cohérente
4. **Documenter les skills utilisés** dans la réponse

### Fallback
Si aucun pattern ne correspond :
1. **Utiliser les coding standards** de `.sixthrules/01-coding-standards.md`
2. **Appliquer les bonnes pratiques** générales du projet
3. **Proposer un skill** si la tâche évolue vers un pattern connu

## Integration Examples

### Debugging Scenario
```
User: "J'ai un bug dans l'automation, les devices ne répondent plus"
→ Detection: "bug", "automation" 
→ Skills: debugging-strategies + automation-diagnostics
→ Response: Application de la méthode scientifique + diagnostics automation
```

### Feature Development Scenario  
```
User: "Je veux ajouter un système d'alertes quota dans l'UI"
→ Detection: "feature", "quota", "UI"
→ Skills: add-feature + quota-alerting + loader-patterns
→ Response: Workflow feature development + implémentation quota + UX loaders
```

## Quality Assurance

### Validation Checklist
- [ ] Skill correctement détecté et chargé
- [ ] Méthodologie du skill respectée
- [ ] Références au skill mentionnées dans la réponse
- [ ] Intégration avec coding standards maintenue
- [ ] Documentation mise à jour si nécessaire

### Continuous Improvement
- Surveiller les patterns qui manquent
- Ajouter nouveaux skills si nécessaire
- Affiner les déclencheurs existants
- Maintenir la cohérence avec l'évolution du projet

---
Ce système hybride garantit que chaque tâche bénéficie de l'expertise spécialisée appropriée tout en maintenant la cohérence globale du projet.
