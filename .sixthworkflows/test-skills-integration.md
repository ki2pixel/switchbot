---
description: Test and validate Sixth Skills Integration System
---

# Test Skills Integration

## Objectif
Valider que le système Skills Integration (Option C - Hybrid) fonctionne correctement avec Sixth.

## Scénarios de Test

### Test 1 - Debugging Pattern
**Commande**: `/test-skills-integration --scenario=debugging`

**Simulation**:
```
User: "J'ai un bug de performance dans l'automation, les devices répondent lentement"
→ Déclencheurs: "bug", "performance", "automation" 
→ Skills attendus: debugging-strategies + automation-diagnostics
→ Validation: Méthode scientifique + diagnostics automation
```

### Test 2 - Feature Development Pattern
**Commande**: `/test-skills-integration --scenario=feature`

**Simulation**:
```
User: "Je veux ajouter une fonctionnalité de tracking quota dans l'UI"
→ Déclencheurs: "feature", "tracking", "quota", "UI"
→ Skills attendus: add-feature + quota-alerting + loader-patterns
→ Validation: Workflow feature + implémentation quota + UX loaders
```

### Test 3 - Performance Pattern
**Commande**: `/test-skills-integration --scenario=performance`

**Simulation**:
```
User: "Le dashboard est lent, faut optimiser les Core Web Vitals"
→ Déclencheurs: "lent", "optimiser", "Core Web Vitals"
→ Skills attendus: performance-audit-runbook
→ Validation: Audit CWV + critical CSS + resource hints
```

## Validation Steps

### 1. Skill Loading Verification
```bash
# Vérifier que tous les skills sont accessibles
find .sixthskills -name "SKILL.md" | wc -l
# Expected: 12 skills

# Vérifier les frontmatter
grep -l "name:" .sixthskills/*/SKILL.md | wc -l
# Expected: 12 skills with frontmatter
```

### 2. Pattern Detection Test
```bash
# Tester les déclencheurs depuis la règle
grep -A 5 -B 5 "bug.*crash.*erreur" .sixthrules/02-skills-integration.md
# Expected: Debugging patterns section

# Vérifier les mappings skills
grep -c "Charger.*SKILL.md" .sixthrules/02-skills-integration.md
# Expected: 12 skill mappings
```

### 3. Integration Validation
```bash
# Vérifier la cohérence des références
grep -r "\.sixthskills/" .sixthrules/ .sixthworkflows/ | wc -l
# Expected: Multiple references to .sixthskills/

# Vérifier l'absence de références Windsurf dans les fichiers actifs
grep -r "\.windsurf/" .sixthrules/ .sixthworkflows/ --exclude="test-skills-integration.md" | wc -l  
# Expected: 0 (no Windsurf references in active files - all migrated to .sixthskills/)
```

## Test Execution Protocol

### Phase 1 - Structure Verification
1. **Lister les skills**: `ls -la .sixthskills/`
2. **Vérifier les SKILL.md**: `find .sixthskills -name "SKILL.md"`
3. **Valider les frontmatter**: `head -5 .sixthskills/*/SKILL.md`

### Phase 2 - Pattern Testing
1. **Lire la règle d'intégration**: `cat .sixthrules/02-skills-integration.md`
2. **Tester les déclencheurs**: Simuler des requêtes utilisateurs
3. **Valider les mappings**: Vérifier skill → pattern correspondance

### Phase 3 - End-to-End Validation
1. **Workflow test**: Utiliser `/enhance` avec différents scénarios
2. **Skill loading**: Confirmer que les skills sont chargés automatiquement
3. **Methodology application**: Vérifier l'application des méthodologies de skill

## Success Criteria

### ✅ Structure
- [ ] 12 skills copiés dans `.sixthskills/`
- [ ] Chaque skill a un `SKILL.md` valide
- [ ] Frontmatter correct pour chaque skill

### ✅ Integration  
- [ ] Règle `02-skills-integration.md` créée
- [ ] 12 patterns de détection définis
- [ ] Mapping skill ↔ pattern cohérent

### ✅ Functionality
- [ ] Détection automatique des skills
- [ ] Chargement correct des SKILL.md
- [ ] Application des méthodologies
- [ ] Références mises à jour (sixthskills)

### ✅ Compatibility
- [ ] Workflows fonctionnent avec `.sixthskills/`
- [ ] Coding standards intègrent les skills
- [ ] Plus de références `.windsurf/` dans les fichiers actifs (toutes migrées vers `.sixthskills/`)

## Troubleshooting

### Issue: Skill not loading
**Symptoms**: Pattern détecté mais skill non chargé
**Solution**: Vérifier le chemin dans `02-skills-integration.md`

### Issue: Wrong skill detected
**Symptoms**: Mauvais skill pour une requête
**Solution**: Affiner les déclencheurs dans la matrice

### Issue: Methodology not applied
**Symptoms**: Skill chargé mais méthode non suivie
**Solution**: Vérifier l'implémentation dans la réponse

## Next Steps

After successful validation:
1. Document the integration in `docs/sixth-integration.md`
2. Update team onboarding materials  
3. Plan migration from Windsurf to Sixth
4. Archive Windsurf configuration
