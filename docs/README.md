# Carte de la Documentation SwitchBot Dashboard v2

**TL;DR** : SwitchBot Dashboard transforme vos appareils SwitchBot en hub domotique avec automatisation locale, persistance PostgreSQL et contrôle à 2 niveaux (Scènes / Direct) : commencez dans `core/`, explorez dans `guides/`, comprenez dans `architecture/`, réparez dans `ops/`.

---

## Le Problème Que Nous Avons Résolu

L'ancienne documentation vivait dans des fichiers éparpillés avec des objectifs mélangés. Les guides d'installation côtoyaient des plongées profondes dans l'architecture, les workflows utilisateur étaient enterrés dans des rapports d'audit, et le dépannage signifiait fouiller dans trois répertoires différents. Impossible de répondre à "Comment installer ça ?" sans lire les internes du déploiement.

## Notre Solution : Documentation Narrative D'abord

Nous avons tout réorganisé autour de votre parcours :

- **`core/`** vous fait démarrer en moins de 5 minutes
- **`guides/`** vous apprend à utiliser le dashboard au quotidien  
- **`architecture/`** explique pourquoi ça marche comme ça (pas juste comment)
- **`ops/`** vous maintient en marche quand ça casse

Chaque article suit le pattern SKILL : problème → solution → implémentation → pièges. Pas de marketing, juste du conseil concret.

### ❌ Documentation Monolithique / ✅ Guides Thématiques

❌ **Ancienne approche** : Un README.md de 200 lignes mélangeant installation, architecture, dépannage et déploiement. Impossible de trouver rapidement "Comment configurer les scènes ?" sans lire tout le document.

✅ **Nouvelle approche** : Guides thématiques ciblés avec navigation par cas d'usage. Chaque fichier répond à une question spécifique avec des exemples concrets et des pièges évités.

## Ce Que Fait Réellement SwitchBot Dashboard

Au fond, c'est une application Flask qui :

1. **Lit les capteurs SwitchBot Meter** toutes les 15 secondes (configurable)
2. **Prend des décisions intelligentes** sur chauffage/climatisation avec hystérésis, fenêtres horaires et logique timezone-aware
3. **Exécute les actions via une cascade à deux niveaux** : scènes SwitchBot → commandes directes
4. **Stocke tout dans PostgreSQL** avec fallback automatique vers des fichiers JSON
5. **Suit les quotas API** via une approche hybride (comptage local + synchronisation des en-têtes SwitchBot `X-RateLimit`)
6. **Surveille l'historique** avec des dashboards Chart.js et rétention de 6 heures

La magie est dans les détails : le polling adaptatif réduit la charge base de données pendant les périodes d'inactivité, le scheduler survit aux redémarrages Gunicorn, et chaque appel API est enveloppé dans une logique de retry avec rate limiting propre.

## Comment Naviguer Cette Documentation

| Vous voulez... | Allez ici | Fichiers clés |
|---|---|---|
| **Installer localement** | `core/` | [Démarrage rapide](core/quickstart.md), [Configuration](core/configuration.md) |
| **Déployer en production** | `core/` | [Déploiement](core/deployment.md) |
| **Utiliser le dashboard** | `guides/` | [Navigation UI](guides/ui-navigation.md), [Monitoring](guides/monitoring-dashboard.md) |
| **Comprendre l'automatisation** | `architecture/` | [Moteur d'automatisation](architecture/automation-engine.md), [Scheduler](architecture/scheduler.md) |
| **Apprendre le stockage** | `architecture/` | [Couche de stockage](architecture/storage-layer.md) |
| **Gérer les quotas** | `architecture/` | [Gestion des quotas](architecture/quota-management.md) |
| **Tester les choses** | `ops/` | [Stratégie de test](ops/testing-strategy.md) |
| **Déboguer les problèmes** | `ops/` | [Dépannage](ops/troubleshooting.md), [Optimisation performance](ops/performance-tuning.md) |

## Ce Qui Rend Cette Architecture Spéciale

### Tableau Comparatif des Approches de Stockage

| Approche | Complexité | Coût | Résilience | Cas d'usage idéal |
|----------|------------|------|------------|-------------------|
| **PostgreSQL Neon** | Moyenne | Gratuit (100h CU/mois) | Élevée (PITR 6h) | Production, multi-utilisateurs |
| **Redis Cloud** | Élevée | Payant (quota limité) | Moyenne (backup manuel) | Cache temporaire, déprécié |
| **JSON Fichiers** | Faible | Gratuit | Faible (local only) | Développement, testing |

### La Couche de Stockage
Nous utilisons **PostgreSQL Neon** comme store principal avec un **fallback JsonStore**. Le `PostgresStore` implémente le connection pooling, les schémas JSONB et la création automatique de tables. Si Neon tombe, nous retombons proprement sur des fichiers JSON locaux sans perdre la logique d'automatisation.

### La Cascade d'Automatisation
Chaque action essaie deux chemins dans l'ordre :
1. **Scènes SwitchBot** (configurations natives de l'app)
2. **Commandes directes** (`setAll`/`turnOff` en dernier recours si aucune scène n'est définie)

Cette cascade allie la flexibilité des scènes à la résilience des commandes directes comme solution de secours.

### Le Polling Adaptatif
Le `SchedulerService` ne pollue pas toutes les 15 secondes. Il calcule les intervalles effectifs selon :
- Sommes-nous dans une fenêtre horaire active ?
- Sommes-nous dans la période de warmup avant une fenêtre ?
- Y a-t-il une séquence off-repeat en attente ?
- Devrions-nous idle à 600 secondes pour réduire la charge base de données ?

### Gestion des Quotas
Le suivi du quota API utilise une architecture "Double Track". L'application compte d'abord chaque appel localement pour une réactivité immédiate, puis extrait les en-têtes `X-RateLimit-Limit` et `X-RateLimit-Remaining` renvoyés par l'API v1.1 pour resynchroniser son état dans `state.json`. Ce mécanisme hybride vous protège de tout dépassement silencieux des 10 000 requêtes journalières. Le `ApiQuotaTracker` assure la réinitialisation automatique à minuit UTC et gère les alertes préventives.

## Pièges Courants Que Nous Avons Déjà Résolus

- **Confusion timezone** : Toutes les fenêtres horaires utilisent le timezone configuré (Europe/Paris par défaut), pas l'UTC du serveur
- **Staleness température** : Nous marquons les températures comme obsolètes après redéploy pour éviter l'automatisation sur vieilles données
- **Conflits scheduler** : Le scheduler détecte Gunicorn vs mode développement Flask et ajuste en conséquence
- **Épuisement connexions base de données** : Nous utilisons le connection pooling et les insertions batch pour l'historique
- **Responsivité mobile** : Toute l'UI fonctionne offline-first avec les assets Bootstrap/Chart.js locaux

## Le Chemin de Migration

Cette structure `docs/v2/` remplace la documentation legacy. La Phase 4 du plan de migration (commandes bash manuelles) déplacera ces fichiers en place. D'ici là, considérez ceci comme l'aperçu de la nouvelle organisation.

## La Règle d'Or : Documentation Modulaire, Décisions Éclairées

Chaque guide thématique inclut des comparatifs ❌/✅, des tables de trade-offs et une Golden Rule finale pour que vous puissiez prendre des décisions techniques informées sans lire tout le codebase.
