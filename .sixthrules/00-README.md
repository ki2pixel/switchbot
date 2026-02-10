# Sixth Rules Priority System - SwitchBot Dashboard

## 📋 Ordre de priorité des règles

Les fichiers sont chargés par Sixth dans l'ordre numérique suivant :

### 🔥 **Priorité 1-4 : Règles fondamentales**
- `01-coding-standards.md` - Standards de codage et architecture du projet SwitchBot Dashboard v2
- `02-skills-integration.md` - Intégration des skills spécialisés (automation, IFTTT, history, quota, etc.)
- `03-memory-bank-protocol.md` - Protocole de gestion de la mémoire persistante
- `04-pr-message-format.md` - Format des Pull Requests

### ⚡ **Priorité 5-6 : Tests & Sécurité**
- `05-prompt-injection-guard.md` - Sécurité contre injections externes
- `06-test-strategy.md` - Stratégie et règles de testing pour le Dashboard SwitchBot

### 📝 **Priorité 7-8 : Assistance & Communication**
- `07-v5-coding-assistance.md` - Règles d'assistance au codage (tâches, outils, flux)
- `08-commit-message-format.md` - Format des messages de commit

## 🔄 **Logique de priorisation**

1. **Règles de base** (01-04) : Fondamentaux qui s'appliquent à tout le projet SwitchBot
2. **Skills & Tests** (05-06) : Comportements spécialisés pour l'écosystème SwitchBot (automation, API, quotas, history)
3. **Communication** (07-08) : Formatage pour collaboration et maintenance

## 🎯 **Contexte SwitchBot Dashboard**

Ce système de règles priorisées s'applique spécifiquement au projet SwitchBot Dashboard v2 :
- Backend Flask avec services injectés
- Frontend offline-first avec Bootstrap/Chart.js
- Stores Postgres优先 avec fallback JsonStore
- Cascade IFTTT → Scènes → Commandes directes
- Skills spécialisés dans `.windsurf/skills/`

## 💡 **Ajout de nouvelles règles**

Utiliser des préfixes numériques continus :
- `09-nouvelle-regle.md` pour les règles additionnelles
- Insérer à la position logique selon la priorité
- Respecter la numérotation existante pour maintenir l'ordre

---
*Dernière mise à jour : 2026-02-10*
*Projet : SwitchBot Dashboard v2*
