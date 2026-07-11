## Verdict : corrections requises avant exposition publique

La suite passe (`157 passed, 1 skipped`), mais l’application n’est pas prête à être accessible publiquement dans son état actuel.

| Priorité | Constat | Emplacement |
|---|---|---|
| P0 | Aucune authentification/autorisation : tout visiteur peut modifier les réglages et commander la climatisation. Le CSRF ne remplace pas une authentification. | [routes.py](/home/kidpixel/SwitchBot/switchbot_dashboard/routes.py:509), [routes.py](/home/kidpixel/SwitchBot/switchbot_dashboard/routes.py:633) |
| P1 | Gunicorn 21.2 est imposé, malgré deux vulnérabilités de request smuggling corrigées en 22.0.0. | [requirements.txt](/home/kidpixel/SwitchBot/requirements.txt:5) |
| P1 | `POSTGRES_SSL_MODE` est lu mais jamais appliqué aux pools PostgreSQL ; le chiffrement annoncé n’est donc pas garanti. | [__init__.py](/home/kidpixel/SwitchBot/switchbot_dashboard/__init__.py:53), [postgres_store.py](/home/kidpixel/SwitchBot/switchbot_dashboard/postgres_store.py:130) |
| P1 | Le repli automatique sur des JSON locaux en production peut désynchroniser le service Web et le worker Render, puis faire fonctionner l’automatisation avec une configuration périmée. | [__init__.py](/home/kidpixel/SwitchBot/switchbot_dashboard/__init__.py:42), [deployment.md](/home/kidpixel/SwitchBot/docs/core/deployment.md:120) |
| P1 | Une transaction PostgreSQL verrouille l’état pendant les appels réseau SwitchBot. Les actions HTTP concurrentes peuvent attendre, écraser un état récent, ou produire des commandes incohérentes. | [automation.py](/home/kidpixel/SwitchBot/switchbot_dashboard/automation.py:806), [postgres_store.py](/home/kidpixel/SwitchBot/switchbot_dashboard/postgres_store.py:40) |
| P2 | L’historique enregistre `api_requests_today`, alors que le quota réel est stocké sous `api_requests_total` : les métriques historiques de quota restent à 0. | [history_service.py](/home/kidpixel/SwitchBot/switchbot_dashboard/history_service.py:269), [quota.py](/home/kidpixel/SwitchBot/switchbot_dashboard/quota.py:30) |
| P2 | « Actualiser le quota » incrémente artificiellement le compteur sans appel à SwitchBot. | [routes.py](/home/kidpixel/SwitchBot/switchbot_dashboard/routes.py:323) |
| P2 | Seules les API d’historique sont limitées ; les actions de contrôle ne le sont pas. De plus, le limiteur est en mémoire, donc non partagé entre processus. | [extensions.py](/home/kidpixel/SwitchBot/switchbot_dashboard/extensions.py:6), [__init__.py](/home/kidpixel/SwitchBot/switchbot_dashboard/__init__.py:135) |
| P2 | Le jeton de diagnostic est transmis dans l’URL : il peut se retrouver dans les logs, l’historique du navigateur ou les en-têtes Referer. | [routes.py](/home/kidpixel/SwitchBot/switchbot_dashboard/routes.py:336) |

La dépendance Gunicorn est concernée par [CVE-2024-1135](https://github.com/advisories/GHSA-w3h3-4rj7-4ph4) et [CVE-2024-6827](https://github.com/advisories/GHSA-hc5x-x2vx-497g). La correction minimale est Gunicorn 22.0.0.

Ordre de remédiation recommandé :

1. Ajouter une authentification obligatoire devant le blueprint, puis limiter les actions de contrôle.
2. Mettre Gunicorn à `>=22` et reconstruire l’image.
3. Rendre PostgreSQL obligatoire en production : pas de fallback JSON implicite, ou fallback partagé avec réconciliation.
4. Appliquer réellement `sslmode=require` aux deux chemins de création des pools.
5. Réduire la transaction d’automatisation à la lecture/réservation d’état ; exécuter l’appel SwitchBot hors verrou avec un verrou distribué commun aux actions manuelles.
6. Corriger les incohérences du quota et déplacer le jeton de debug dans un en-tête d’autorisation.

Contrôles complémentaires : Bandit ne relève aucune alerte moyenne/élevée ; Ruff relève 11 problèmes de propreté, tous corrigeables automatiquement. Aucun fichier du dépôt n’a été modifié.