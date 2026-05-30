# Guide de Déploiement Sans Interruption (Zero-Downtime)

Ce document décrit la stratégie de déploiement "Blue/Green" et de migration de base de données sans interruption pour l'application SwitchBot.

## Objectifs
- Maintenir une disponibilité de 100% lors des mises à jour.
- Valider la nouvelle version sur une portion du trafic avant bascule totale.

## Stratégie
1. Déploiement d'une nouvelle instance (Green).
2. Vérification des health checks.
3. Bascule du trafic via le load balancer Render.
4. Destruction de l'ancienne instance (Blue) après période d'observation.
