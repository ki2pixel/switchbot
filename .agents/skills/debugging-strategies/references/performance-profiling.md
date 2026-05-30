# Guide de Profilage des Performances

Ce document détaille les méthodes pour identifier les goulots d'étranglement dans le backend SwitchBot.

## Étapes de Profilage
1. **cProfile** : Exécuter des modules spécifiques pour mesurer le temps CPU.
2. **EXPLAIN ANALYZE** : Pour profiler les requêtes PostgreSQL lentes.
3. **Network Tab** : Pour profiler les temps de chargement des assets offline-first.
