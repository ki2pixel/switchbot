# Contexte Actif

## Objectifs
- [x] Optimisation de l'usage du quota SwitchBot par l'introduction d'un cache cooldown sur le sondage AC et renforcement des validations d'intervalles.
- [x] Correction du rendu de la time scale Chart.js côté frontend et alignement des timestamps lors des écritures groupées (batch flushes) côté backend.
- [x] Implémentation complète de l'Audit Backend (Sécurité, Stabilisation Store, Observabilité/Healthz, et Amortissement historique).
- [x] Correction de la pollution d'état (`last_error`) dans `automation.py` lors d'un fallback direct sans scène configurée.
- [x] Campagne d'archivage de la Memory Bank effectuée.
- [x] Audit d'alignement des Skills IA avec la base de code réalisé et validé.
- [x] Alignement de la documentation technique (v2) avec le code réel, via le workflow `/docs-updater`.
- [x] Polling temps réel du statut AC (Air Conditioner) depuis l'API SwitchBot pour corriger l'incohérence d'état de l'automatisation en mode direct.

## Décisions Clés
- Cache/cooldown de 15 minutes sur `poll_aircon_status` pour limiter drastiquement les requêtes SwitchBot API, avec option `force=True` uniquement lors de décisions critiques de commande climatiseur.
- Augmentation de la validation minimale des intervalles de polling (60s pour `poll_interval_seconds`, 300s pour `idle_poll_interval_seconds`) sur le backend et le frontend.
- Synchronisation de l'état supposé de l'AC avec le statut physique via `poll_aircon_status()` avant l'évaluation de température dans `_run_once_impl`, conditionné au mode `direct` et à la fenêtre horaire active.
- DummyClient des tests enrichi pour simuler l'état physique de l'AC et ses transitions lors de l'exécution de scènes/commandes.
- Utilisation systématique d'objets `Date` JavaScript et tri croissant (ASC) côté frontend pour le rendu correct de Chart.js en mode `parsing: false`.
- Masquage et désactivation du bouton "Réinitialiser zoom" si le plugin de zoom Chart.js n'est pas chargé (résolution d'un TypeError).
- Déclaration explicite de la colonne `timestamp` lors des insertions groupées dans `state_history` pour éviter l'alignement artificiel des timestamps d'un même batch via `DEFAULT NOW()`.
- Déplacement des secrets (webhooks IFTTT) hors de `settings.json` vers l'environnement (.env).
- Mise en œuvre de protections SSRF strictes au niveau DNS pour les appels de webhooks externes.
- Amortissement résilient des écritures d'historique en mémoire tampon si PostgreSQL est hors-ligne.
- Utilisation systématique de la property `pool` de `PostgresStore` pour forcer les vérifications d'initialisation de connexion.
- Blocage strict du démarrage Flask en production si `FLASK_SECRET_KEY` est vulnérable ou manquante.

## Modifications Skills Effectuées
- Mise à jour de `add-feature/SKILL.md` (SPA Router, CSRF).
- Mise à jour de `postgres-store-maintenance/SKILL.md` (gestion de contextes psycopg_pool).
- Mise à jour de `ifttt-cascade/SKILL.md` (sécurité SSRF et timing attacks).

## Modifications Documentaires Effectuées
- **`docs/README.md`** : Correction de l'information sur le suivi de quota (approche hybride et synchronisation des headers SwitchBot confirmées).
- **`docs/architecture/storage-layer.md`** : Ajout de la gestion du connection pool (`psycopg_pool`) et des transactions avec row-level locking.
- **`docs/guides/ifttt-setup.md`** : Documentation des sécurités SSRF (blocage IPs locales et domaine strict) et contre les Timing Attacks (`hmac.compare_digest`).
- **`docs/guides/ui-navigation.md`** : Explication du cycle de vie des pages SPA (`spa-router.js`) et de la protection CSRF globale.

## Questions/Problèmes Ouverts
- Aucun.

## Prochaines Étapes
- En attente de nouvelles instructions.
