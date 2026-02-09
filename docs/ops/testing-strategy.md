# Stratégie de Tests pour SwitchBot Dashboard v2

**TL;DR** : Maintenez ≥85% de couverture avec pytest, testez la cascade IFTTT→scènes→commandes, et validez la résilience du système via les logs structurés et l'endpoint `/healthz`.

## Le Problème : Pourquoi des Tests Structurés ?

Vous déployez un dashboard de domotique qui contrôle votre climatisation. Un bug dans l'automatisation peut faire surchauffer votre système ou laisser votre climatisation tourner toute la nuit. Pire encore, une fuite de quota API peut vous coûter cher en appels SwitchBot inutiles.

Les tests ne sont pas une option ; ils sont votre filet de sécurité. Mais tester une application qui mélange Flask, APScheduler, des webhooks IFTTT et des commandes hardware demande une approche systématique.

## La Solution : Une Architecture de Tests en Couches

Le SwitchBot Dashboard utilise une architecture de tests à trois niveaux qui reflète sa structure technique :

1. **Tests unitaires** : Validateurs et conversions (`_as_bool`, `_as_int`, `_as_float`)
2. **Tests d'intégration** : Services injectés, cascade IFTTT→scènes→commandes
3. **Tests end-to-end** : Interface utilisateur, quotas API, résilience système

Cette approche garantit que chaque composant fonctionne isolément ET que l'ensemble reste cohérent.

## L'Implémentation : Le Code et la Configuration

### Commandes Canoniques

```bash
# Toujours utiliser l'interpréteur du projet pour éviter les divergences d'environnement
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest

# Alternative avec environnement local
source venv/bin/activate
python -m pytest
```

### Variables d'Environnement Critiques

```bash
# .env.example - NE JAMAIS COMMITTER LES VALEURS RÉELLES
SWITCHBOT_TOKEN=votre_token_ici
SWITCHBOT_SECRET=votre_secret_ici
LOG_LEVEL=info
STORE_BACKEND=filesystem
SCHEDULER_ENABLED=true
```

### Configuration JSON Essentielle

```json
// config/settings.json - Structure de test
{
  "meter_device_id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  "aircon_device_id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  "poll_interval_seconds": 60,
  "min_temperature": 22,
  "max_temperature": 26,
  "hysteresis_celsius": 0.5,
  "api_quota_warning_threshold": 100
}
```

### Tests de Santé Systeme

L'endpoint `/healthz` est votre premier indicateur de problème :

```bash
curl -v http://localhost:8000/healthz
```

**Réponse attendue en fonctionnement normal** :
```json
{
  "status": "ok",
  "scheduler_running": true,
  "automation_enabled": true,
  "last_tick": "2024-01-10T14:30:00Z",
  "api_requests_total": 42,
  "api_requests_remaining": 958,
  "api_quota_day": "2024-01-10",
  "version": "1.0.0"
}
```

### Tests de la Cascade IFTTT→Scènes→Commandes

La logique métier suit une cascade stricte :

1. **IFTTT Webhook** (priorité 1)
2. **Scène SwitchBot** (priorité 2) 
3. **Commande directe** (fallback)

```python
# Exemple de test de la cascade
def test_ifttt_scene_command_cascade():
    # 1. Configurer webhook IFTTT valide
    # 2. Déclencher action
    # 3. Vérifier utilisation webhook
    # 4. Supprimer webhook, vérifier fallback scène
    # 5. Supprimer scène, vérifier fallback commande
```

### Logs Structurés pour le Debugging

Les préfixes de logs facilitent le diagnostic :

```bash
# Logs IFTTT
[ifttt] IFTTT webhook triggered successfully | status_code=200, url=https://maker.ifttt.com/trigger/...

# Logs d'automatisation  
[automation] Automation tick started | trigger=scheduler, interval=60s
[automation] Using SwitchBot scene (webhook unavailable) | action_key=winter, scene_id=scene-w

# Logs de santé
[health] Health check completed | status=ok, scheduler_running=true
```

### Tests de Résilience

```bash
# Simulation de panne API
export SWITCHBOT_TOKEN=invalid_token
python app.py
# Vérifier que l'application ne crash pas

# Test de quota épuisé
# Modifier state.json : api_requests_remaining = 0
# Vérifier bandeau d'alerte dans l'UI
```

## Les Pièges : Ce Qui Fait Échouer les Tests

### Piège #1 : Environnement Incohérent

**Le problème** : Utiliser `python` système au lieu du venv du projet.

**La solution** : Toujours utiliser le chemin complet vers l'interpréteur du projet :
```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest
```

### Piège #2 : Tests Asynchrones sans Attente

**Le problème** : Les tests vérifient l'état immédiatement après une action asynchrone.

**La solution** : Utiliser `time.sleep()` ou `pytest-asyncio` pour les opérations scheduler :
```python
def test_scheduled_action():
    # Déclencher action
    time.sleep(2)  # Attendre la planification
    # Vérifier résultat
```

### Piège #3 : Mock Incomplet des Services Externes

**Le problème** : Mocker seulement l'API SwitchBot mais pas IFTTT.

**La solution** : Mocker toute la chaîne de dépendances :
```python
@patch('switchbot_dashboard.automation.IFTTTClient')
@patch('switchbot_dashboard.automation.SwitchBotClient')
def test_full_cascade(mock_ifttt, mock_switchbot):
    # Configuration des mocks
    # Test de la cascade complète
```

### Piège #4 : État Persistant entre Tests

**Le problème** : Les tests modifient `state.json` et se contaminent mutuellement.

**La solution** : Nettoyage systématique dans `teardown` :
```python
def teardown_method(self):
    # Restaurer state.json original
    # Nettoyer les tâches scheduler
```

### Piège #5 : Timezones et Heures d'Été

**Le problème** : Les tests de fenêtres horaires échouent à cause des changements d'heure.

**La solution** : Utiliser des dates fixes en UTC pour les tests :
```python
def test_time_window_handling():
    # Utiliser datetime(2024, 1, 15, 10, 0, tzinfo=timezone.utc)
    # Éviter datetime.now() qui dépend du système
```

## Checklist de Validation

### Installation et Configuration
- [ ] Venv activé avec dépendances installées
- [ ] `.env` présent avec tokens (non commités)
- [ ] `settings.json` valide avec device IDs
- [ ] Serveur démarre sur `http://127.0.0.1:5000/`

### Tests Automatisés
- [ ] Suite pytest complète passe (≥85% couverture)
- [ ] Tests IFTTT : validation HTTPS, timeouts, fallbacks
- [ ] Tests automation : hystérésis, cooldown, fenêtres horaires
- [ ] Tests UI : bandeau quota, responsivité mobile

### Résilience Système
- [ ] `/healthz` retourne 200 avec métriques cohérentes
- [ ] Logs structurés présents avec préfixes corrects
- [ ] Gestion des erreurs API (429, timeout) sans crash
- [ ] Fallback store (Redis → filesystem) fonctionnel

### Interface Utilisateur
- [ ] Bandeau quota s'affiche au seuil configuré
- [ ] Scènes SwitchBot exécutables depuis l'UI
- [ ] Navigation responsive desktop/mobile
- [ ] Messages d'erreur clairs et informatifs

## Références Techniques

- **Commandes pytest** : `/mnt/venv_ext4/venv_switchbot/bin/python -m pytest --tb=short -q`
- **Fichiers de test** : `tests/test_ifttt.py`, `tests/test_automation_service.py`, `tests/test_dashboard_routes.py`
- **Configuration** : `.env.example`, `config/settings.json`, `config/state.json`
- **Logs** : Préfixes `[ifttt]`, `[automation]`, `[health]`, `[scheduler]`

### ❌ Tests Sans Mocks / ✅ Tests Avec Mocks Complets

❌ **Tests sans mocks** : Appels API réels, dépendances externes, tests lents et non déterministes. Un test échoue si SwitchBot API est down, pas si votre code a un bug.

✅ **Tests avec mocks complets** : Réponses contrôlées, exécution rapide, tests déterministes. Vous testez votre logique, pas la disponibilité des services externes.

### Tableau Comparatif des Types de Tests

| Type | Couverture | Maintenance | Fiabilité | Vitesse |
|------|------------|-------------|-----------|---------|
| **Unitaires** | Moyenne | Faible | Élevée | Très rapide |
| **Intégration** | Élevée | Moyenne | Moyenne | Moyenne |
| **E2E** | Très élevée | Élevée | Faible | Lente |

## La Règle d'Or : Couverture Résiliente, Mocks Intelligents

Testez ce que vous contrôlez avec des mocks, testez ce que vous ne contrôlez pas avec des intégrations ciblées. La résilience des tests garantit la résilience du système.

---

Cette stratégie de tests garantit que chaque modification du code reste sécurisée pour votre système de domotique. Les tests ne sont pas une barrière ; ils sont votre assurance que votre climatisation ne vous jouera pas de tours.
