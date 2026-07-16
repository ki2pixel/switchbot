# Contexte Actif

## Session 2026-07-16 — Remédiation Backend Complète (P0 + P1 + P2)

### Derniers changements accomplis

**Phase P1 (Robustesse & Sécurité) — TERMINÉE**
- **PERF-01 / REL-03** : ThreadPoolExecutor pour l'enrichissement des devices, threading.Lock sur le cache SwitchBotClient, rate limit `/devices` (10/min), actions manuelles en arrière-plan (202 immédiat), timeouts HTTP (15s default, 5s actions).
- **SEC-02 / SEC-03** : Validation regex `scene_id`, bornes températures 10–35°C avec auto-swap min/max, validation `HH:MM` stricte.
- **REL-04 / REL-05** : Retries exponentiels avec jitter uniquement sur GET/429/5xx, parsing `Retry-After`, `timeout=5.0` + `statement_timeout=5000ms` sur le pool psycopg.
- **SEC-04 / SEC-05 / SEC-07** : `sslmode=verify-full` via env, masquage des credentials DB dans les logs de migration, `@limiter.limit("5 per minute")` sur `/debug/state`.

**Phase P2 (Durcissement & Cycle de vie) — TERMINÉE**
- **SEC-06** : Route `/logout` passée en POST-only, bouton de déconnexion CSRF-protégé dans `settings.html`, support hachages Werkzeug (`pbkdf2:`, `scrypt:`, `argon2:`) pour `DASHBOARD_PASSWORD`.
- **MAIN-01** : Suppression de la classe morte `SimpleTransactionContext` dans `config_store.py`.
- **MAIN-02** : `AGENTS.md` mis à jour : IFTTT officiellement qualifié de retiré du produit.

### État de la base de tests
- **206 tests passent** (+ 7 nouveaux : validation inputs, logout POST, hachage Werkzeug).
- Aucun test rouge.

## Objectifs actuels
- **Aucune tâche active.** La remédiation backend complète est terminée.
- Prochaine session possible : déploiement Render (ajouter `PROXY_FIX_FOR=1` dans les variables d'environnement Render) et suivi des métriques en production.

## Bloqueurs actifs
- Aucun.

## Note configuration Render
- `PROXY_FIX_FOR=1` : **à configurer** dans l'interface Render (Render met un proxy devant l'app).
- `RATELIMIT_STORAGE_URI` : **non nécessaire** — Gunicorn est forcé à 1 seul worker quand le scheduler APScheduler est actif (voir `gunicorn.conf.py`), donc le stockage mémoire par défaut suffit.
