# Analyse de Complexité Cyclomatique

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Vue d'ensemble

Ce document présente l'analyse de complexité cyclomatique du codebase SwitchBot Dashboard, identifie les points critiques et propose des recommandations pour améliorer la maintenabilité.

> 📊 **Métriques actuelles** : Complexité moyenne C (17.79), 14 blocs analysés avec radon cc

## Analyse Radon

### Résultats Complets

```bash
$ radon cc switchbot_dashboard app.py scripts -a -nc

switchbot_dashboard/routes.py
    F 411:0 update_settings - E
    F 817:0 history_api_data - C
    F 616:0 _execute_aircon_action - C

switchbot_dashboard/automation.py
    M 658:4 AutomationService.run_once - E
    F 26:0 _is_now_in_windows - C
    M 259:4 AutomationService._cooldown_active - C
    M 432:4 AutomationService._process_off_repeat_task - C

switchbot_dashboard/history_service.py
    M 105:4 HistoryService.get_history - C

switchbot_dashboard/scheduler.py
    M 77:4 SchedulerService._next_window_start - C
    M 113:4 SchedulerService._get_effective_interval_seconds - C

switchbot_dashboard/switchbot_api.py
    M 78:4 SwitchBotClient._request - D
    M 197:4 SwitchBotClient._capture_quota_metadata - C

switchbot_dashboard/__init__.py
    F 106:0 create_app - C
scripts/migrate_to_postgres.py
    F 101:0 migrate_to_postgres - C

14 blocks (classes, functions, methods) analyzed.
Average complexity: C (17.785714285714285)
```

## Points de Complexité Critique

### 1. AutomationService.run_once() - Complexité E

**Fichier** : `switchbot_dashboard/automation.py:658`
**Lignes** : 935 lignes
**Complexité** : E (Élevée)

#### Problèmes Identifiés

```python
# switchbot_dashboard/automation.py:658-935
def run_once(self, trigger: str = "scheduler") -> str:
    """Exécute un cycle d'automatisation complet."""
    
    # 1. Validation et initialisation (20+ lignes)
    if not self._settings.get("automation_enabled", False):
        return "automation_disabled"
    
    # 2. Lecture capteur avec retry (50+ lignes)
    try:
        meter_data = self._switchbot_client.poll_meter()
    except SwitchBotApiError as e:
        # Gestion erreur complexe
        
    # 3. Évaluation fenêtres horaires (30+ lignes)
    now_utc = datetime.utcnow()
    timezone = self._get_timezone()
    now_local = now_utc.astimezone(timezone)
    in_window = _is_now_in_windows(self._settings.get("time_windows", []), now_local)
    
    # 4. Logique température complexe (100+ lignes)
    current_temp = meter_data.get("temperature")
    mode = self._settings.get("mode", "summer")
    
    if mode == "winter":
        min_temp = self._settings.get("winter", {}).get("min_temp", 18.0)
        max_temp = self._settings.get("winter", {}).get("max_temp", 22.0)
        # ... logique hiver
        
    elif mode == "summer":
        min_temp = self._settings.get("summer", {}).get("min_temp", 22.0)
        max_temp = self._settings.get("summer", {}).get("max_temp", 26.0)
        # ... logique été
        
    # 5. Gestion cooldown (40+ lignes)
    if self._cooldown_active():
        return "cooldown"
        
    # 6. Exécution actions avec cascade (200+ lignes)
    if current_temp < min_temp - hysteresis:
        if mode == "winter":
            return self._trigger_aircon_action("winter", "automation_winter_on")
        # ...
        
    # 7. Gestion OFF hors fenêtres (50+ lignes)
    if not in_window and self._settings.get("turn_off_outside_windows", False):
        # ...
        
    # 8. Traitement répétitions OFF (100+ lignes)
    if self._process_off_repeat_task():
        return "off_repeat_executed"
        
    # 9. Mise à jour état (30+ lignes)
    self._update_state(meter_data, ...)
    
    return "no_action"
```

#### Recommandations

1. **Extraire la logique température** :
```python
def _evaluate_temperature_logic(self, current_temp: float, mode: str) -> tuple[str, dict]:
    """Évalue les seuils de température et retourne l'action recommandée."""
    
def _get_temperature_thresholds(self, mode: str) -> dict:
    """Récupère les seuils pour un mode donné."""
```

2. **Simplifier la gestion des actions** :
```python
def _determine_action(self, temp_eval: dict, in_window: bool) -> Optional[str]:
    """Détermine l'action à exécuter basée sur l'évaluation."""
    
def _execute_automation_action(self, action: str, context: dict) -> str:
    """Exécute l'action avec gestion complète des side-effects."""
```

3. **Modulariser la lecture capteur** :
```python
def _read_meter_with_retry(self) -> dict:
    """Lit le capteur avec gestion des erreurs et retries."""
```

### 2. routes.update_settings() - Complexité E

**Fichier** : `switchbot_dashboard/routes.py:411`
**Lignes** : 411 lignes
**Complexité** : E (Élevée)

#### Problèmes Identifiés

```python
# switchbot_dashboard/routes.py:411-822
@dashboard_bp.route("/settings", methods=["POST"])
def update_settings():
    """Met à jour les paramètres depuis le formulaire."""
    
    # 1. Validation formulaire (100+ lignes)
    automation_enabled = _as_bool(request.form, "automation_enabled")
    mode = request.form.get("mode", "summer")
    poll_interval = _as_int(request.form, "poll_interval_seconds", 15, 3600)
    # ... 20+ validations
    
    # 2. Gestion fenêtres horaires (80+ lignes)
    time_windows = []
    days_selected = _as_list(request.form, "time_window_days")
    start_time = request.form.get("time_window_start", "")
    end_time = request.form.get("time_window_end", "")
    # ... logique complexe de construction
    
    # 3. Validation scènes IFTTT (50+ lignes)
    ifttt_webhooks = {}
    for key in ["winter", "summer", "fan", "off"]:
        webhook_url = request.form.get(f"ifttt_webhook_{key}", "").strip()
        if webhook_url:
            if not webhook_url.startswith("https://"):
                flash(f"URL IFTTT {key} doit commencer par https://", "error")
                return redirect(url_for("dashboard.settings"))
        ifttt_webhooks[key] = webhook_url
    
    # 4. Validation scènes SwitchBot (40+ lignes)
    aircon_scenes = {}
    for key in ["winter", "summer", "fan", "off"]:
        scene_id = request.form.get(f"aircon_scene_{key}", "").strip()
        if scene_id:
            aircon_scenes[key] = scene_id
    
    # 5. Mise à jour settings (50+ lignes)
    settings_store = current_app.extensions["settings_store"]
    current_settings = settings_store.read()
    
    updated_settings = {
        **current_settings,
        "automation_enabled": automation_enabled,
        "mode": mode,
        "poll_interval_seconds": poll_interval,
        "time_windows": time_windows,
        "ifttt_webhooks": ifttt_webhooks,
        "aircon_scenes": aircon_scenes,
        # ... 10+ autres champs
    }
    
    # 6. Rescheduling (30+ lignes)
    scheduler_service = current_app.extensions.get("scheduler_service")
    if scheduler_service:
        scheduler_service.reschedule()
    
    flash("Paramètres mis à jour avec succès", "success")
    return redirect(url_for("dashboard.index"))
```

#### Recommandations

1. **Extraire la validation formulaire** :
```python
def _validate_automation_form(request) -> dict:
    """Valide et extrait les données du formulaire d'automatisation."""
    
def _validate_time_windows(request) -> list[dict]:
    """Valide et construit les fenêtres horaires."""
    
def _validate_scenes(request) -> tuple[dict, dict]:
    """Valide les scènes IFTTT et SwitchBot."""
```

2. **Simplifier la mise à jour** :
```python
def _build_settings_update(form_data: dict, current: dict) -> dict:
    """Construit le dictionnaire de mise à jour des settings."""
    
def _apply_settings_update(updated_settings: dict) -> None:
    """Applique la mise à jour et gère le rescheduling."""
```

### 3. SwitchBotClient._request() - Complexité D

**Fichier** : `switchbot_dashboard/switchbot_api.py:78`
**Lignes** : 173 lignes
**Complexité** : D (Élevée)

#### Problèmes Identifiés

```python
# switchbot_dashboard/switchbot_api.py:78-251
def _request(self, method: str, endpoint: str, body: dict | None = None) -> SwitchBotResponse:
    """Effectue une requête HTTP avec signature HMAC et retries."""
    
    # 1. Construction URL et headers (30+ lignes)
    url = f"{self._base_url}{endpoint}"
    headers = {
        "Authorization": self._build_auth_header(),
        "Content-Type": "application/json",
        "User-Agent": "SwitchBotDashboard/1.0"
    }
    
    # 2. Signature HMAC (20+ lignes)
    timestamp = str(int(time.time()))
    nonce = str(uuid.uuid4())
    sign_str = f"{method}{endpoint}{timestamp}{nonce}"
    signature = base64.b64encode(
        hmac.new(self._secret.encode(), sign_str.encode(), hashlib.sha256).digest()
    ).decode()
    
    headers.update({
        "t": timestamp,
        "nonce": nonce,
        "sign": signature
    })
    
    # 3. Logique de retry (50+ lignes)
    for attempt in range(self._retry_attempts + 1):
        try:
            response = requests.request(method, url, headers=headers, json=body, timeout=10)
            
            # Gestion des codes d'erreur
            if response.status_code == 429:
                if attempt < self._retry_attempts:
                    time.sleep(self._retry_delay_seconds * (2 ** attempt))
                    continue
                raise SwitchBotApiError("Rate limit exceeded")
                
            elif response.status_code == 190:
                # Erreur spécifique SwitchBot
                error_body = response.json()
                raise SwitchBotApiError(f"SwitchBot error 190: {error_body}")
                
            elif response.status_code >= 500:
                if attempt < self._retry_attempts:
                    time.sleep(self._retry_delay_seconds * (2 ** attempt))
                    continue
                raise SwitchBotApiError(f"Server error: {response.status_code}")
                
            # Succès
            break
            
        except requests.RequestException as e:
            if attempt < self._retry_attempts:
                time.sleep(self._retry_delay_seconds * (2 ** attempt))
                continue
            raise SwitchBotApiError(f"Request failed: {e}")
    
    # 4. Capture quota (30+ lignes)
    if self._quota_tracker:
        self._quota_tracker.record_call(context=endpoint)
        self._capture_quota_metadata(response)
    
    # 5. Construction réponse (20+ lignes)
    try:
        body = response.json()
    except ValueError:
        body = response.text
    
    return SwitchBotResponse(
        status_code=response.status_code,
        message=response.reason,
        body=body
    )
```

#### Recommandations

1. **Extraire la signature HMAC** :
```python
def _build_auth_headers(self, method: str, endpoint: str) -> dict:
    """Construit les headers d'authentification HMAC."""
    
def _generate_signature(self, method: str, endpoint: str) -> dict:
    """Génère timestamp, nonce et signature."""
```

2. **Simplifier la logique de retry** :
```python
def _execute_request_with_retry(self, method: str, url: str, headers: dict, body: dict) -> requests.Response:
    """Exécute la requête avec logique de retry."""
    
def _handle_response_errors(self, response: requests.Response, attempt: int) -> None:
    """Gère les codes d'erreur et décide du retry."""
```

3. **Modulariser la capture quota** :
```python
def _process_quota_tracking(self, endpoint: str, response: requests.Response) -> None:
    """Traite le suivi des quotas pour un appel."""
```

## Recommandations Globales

### 1. Priorités de Refactoring

#### Haute Priorité (Complexité E)
1. **AutomationService.run_once()** - Extraire 5-8 méthodes privées
2. **routes.update_settings()** - Créer 4-6 fonctions de validation

#### Moyenne Priorité (Complexité D/C)
1. **SwitchBotClient._request()** - Modulariser auth et retry
2. **AutomationService._process_off_repeat_task()** - Simplifier la logique
3. **HistoryService.get_history()** - Extraire construction SQL

### 2. Patterns de Refactoring

#### Single Responsibility Principle
```python
# Avant (trop de responsabilités)
def run_once(self):
    # lecture + validation + logique + exécution + état
    
# Après (responsabilités séparées)
def run_once(self):
    meter_data = self._read_meter_with_retry()
    action = self._evaluate_automation_logic(meter_data)
    result = self._execute_action(action)
    self._update_system_state(result)
```

#### Extraction de Méthodes
```python
# Méthode complexe extraite
def _evaluate_temperature_logic(self, current_temp: float) -> dict:
    """Évalue les seuils de température."""
    mode = self._settings.get("mode", "summer")
    thresholds = self._get_temperature_thresholds(mode)
    hysteresis = self._settings.get("hysteresis_celsius", 0.5)
    
    return {
        "mode": mode,
        "current": current_temp,
        "min": thresholds["min"],
        "max": thresholds["max"],
        "hysteresis": hysteresis,
        "action": self._determine_temperature_action(current_temp, thresholds, hysteresis)
    }
```

#### Validation Centralisée
```python
# Validation formulaire réutilisable
class AutomationFormValidator:
    @staticmethod
    def validate_temperature_range(form_data: dict) -> dict:
        """Valide les seuils de température."""
        
    @staticmethod
    def validate_time_windows(form_data: dict) -> list[dict]:
        """Valide les fenêtres horaires."""
        
    @staticmethod
    def validate_scenes(form_data: dict) -> tuple[dict, dict]:
        """Valide les scènes IFTTT et SwitchBot."""
```

### 3. Outils de Monitoring

#### Radon Configuration
```toml
# pyproject.toml
[tool.radon]
cc_min = "B"
exclude = ["tests/*", "migrations/*"]

[tool.radon.cc]
show_complexity = true
average = true
min = "B"
```

#### CI/CD Integration
```yaml
# .github/workflows/complexity.yml
- name: Check complexity
  run: |
    radon cc switchbot_dashboard --min B
    radon mi switchbot_dashboard --min B
```

### 4. Objectifs de Qualité

#### Cibles à Atteindre
- **Complexité moyenne** : B (≤ 10) vs actuel C (18.58)
- **Fonctions complexes** : 0 (complexité E) vs actuel 2
- **Maintenabilité** : A (≥ 85) vs actuel B

#### Métriques de Suivi
```bash
# Monitoring mensuel
radon cc switchbot_dashboard --json > complexity_report.json
radon mi switchbot_dashboard --json > maintainability_report.json

# Tendance sur 6 mois
git log --since="6 months ago" --stat | grep "switchbot_dashboard"
```

## Plan d'Action

### Phase 1 (Sprint 1-2)
1. **AutomationService.run_once()** - Extraire 3 méthodes critiques
2. **Tests unitaires** - Couvrir les méthodes extraites
3. **Validation** : Radon score B pour run_once()

### Phase 2 (Sprint 3-4)
1. **routes.update_settings()** - Modulariser validation
2. **SwitchBotClient._request()** - Simplifier auth/retry
3. **Intégration** : Tests E2E maintenus

### Phase 3 (Sprint 5-6)
1. **Refactoring restant** - Fonctions complexité C/D
2. **Documentation** : Mettre à jour les patterns
3. **Monitoring** : CI/CD complex checks

---

*Pour les standards de codage et patterns architecturaux, consultez [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) et [Automation Patterns](automation-patterns.md).*
