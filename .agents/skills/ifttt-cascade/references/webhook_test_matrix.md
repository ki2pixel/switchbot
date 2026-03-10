# Matrice de test cascade IFTTT

## Cas Webhooks
| Cas | Entrée | Résultat attendu |
| --- | --- | --- |
| HTTPS valide | URL `https://maker.ifttt.com/trigger/...` | 200 < 3 s, `state.last_action` mis à jour |
| Timeout | URL volontairement lente (>4 s) | Fallback vers scène, log `[automation] Webhook timeout` |
| 500 | URL renvoyant 500 | Fallback scène puis commande directe |

## Cas Scènes
1. Supprimer `scene_id` → doit basculer sur commande directe.
2. Scène invalide → `SwitchBotApiError`, log `[automation] Scene execution failed`.

## Commandes Directes
- Vérifier `aircon_device_id` présent.
- Cooldown respecté (`assumed_aircon_power`).

## Scripts utiles
Exécuter `python -m tests.test_ifttt` pour valider les cas unitaires.

## Observabilité
- Inspecter `state.json` (`pending_off_repeat`, `last_error`).
- Vérifier les flashs UI sur `index.html` (succès/erreur).
