# SwitchBot API Checklist

## Avant modification
1. Lire `switchbot_dashboard/switchbot_api.py` (méthodes existantes, `_request`, `_build_headers`).
2. Vérifier injection client via `current_app.extensions["switchbot_client"]`.
3. Confirmer que `quota_tracker` est disponible (sinon instancier stub pour tests).

## Ajout d'une commande
- Ajout méthode `SwitchBotClient.my_command()` :
  - Paramètres typés (`device_id: str` ...).
  - Validation (strip, raise `SwitchBotApiError` si vide).
  - Appel `_request` avec `json_body` complet (`command`, `parameter`, `commandType`).
- Ajouter helper côté routes/services si exposé.

## Gestion quota
- `SwitchBotClient._capture_quota_metadata()` doit être appelé avant tout retour.
- Si nouveaux endpoints, vérifier présence headers `X-RateLimit-*`.

## Tests
| Test | Fichier | Points clés |
| --- | --- | --- |
| Unitaire client | `tests/test_switchbot_api.py` (à créer si absent) | signature HMAC, retries, erreurs |
| Intégré | `tests/test_automation_service.py` | interactions via mocks/quota |
| UI/Routes | `tests/test_dashboard_routes.py` | flash, validation formulaire |

## Outils
```bash
# Prévisualiser les headers sans appeler l'API
python .windsurf/skills/switchbot-api-dev/scripts/preview_headers.py
```

## Documentation/Sécurité
- Jamais logguer `SWITCHBOT_SECRET` ou Authorization.
- MAJ `docs/core/configuration.md` pour toute nouvelle variable.
- Memory Bank : consigner les nouveaux endpoints/commandes (decisionLog).
