L'audit architectural et technique complet du backend de **SwitchBot Dashboard v2** est finalisé à partir des deux archives du dépôt.

* **Statut global de l'audit** : **NON CONFORME POUR LA PRODUCTION (Rejet d'intégration en l'état)**.


* **Invariants architecturaux violés (`architecte.md` & `codingstandards.md`)** :
1. **Thread-Safety & Concurrence** : Partage inter-threads sans verrou d'un cache mutable (`CachedStoreWrapper`), auto-deadlock sur transactions imbriquées (`PostgresStore` et `JsonStore`), et contournement du fencing token par les routes HTTP manuelles.


2. **Résilience & Failover Store** : Absence de bascule dynamique vers `JsonStore` après 3 échecs consécutifs en cours d'exécution (seul le failover au démarrage dans `_build_store` est implémenté) et crash non capturé de `_maybe_reschedule_after_tick()` si le store tombe.


3. **Zéro Exception Silencieuse & Hygiène des Logs** : Présence de 4 blocs `except Exception: pass` dans `postgres_store.py`, absence du préfixe `[api]` dans `switchbot_api.py`, et journalisation brute des en-têtes HTTP.


4. **Défense SSRF & Validation des Entrées** : Absence de validation HTTPS et IP privée sur `SwitchBotClient._base_url`, et appels directs à `int()` / `fromisoformat()` sur `request.args` dans les routes `/history/api/*`.





---

## 1. Matrice Globale de Sévérité des Anomalies

| ID Anomalie | Catégorie | Sévérité | Fichier & Ligne | Impact Production |
| --- | --- | --- | --- | --- |
| **AUD-CONC-01** | Race Condition Cache | **Critique** | `automation.py:101` | Corruption d'état inter-threads

 |
| **AUD-DB-01** | Self-Deadlock SQL/Lock | **Critique** | `postgres_store.py:29` | Blocage complet worker/pool

 |
| **AUD-SCHED-01** | Crash Reschedule | **Critique** | `scheduler.py:45` | Mort silencieuse du scheduler

 |
| **AUD-SEC-01** | Défense SSRF absente | **Haute** | `switchbot_api.py:48` | Fuite token API vers hôte arbitraire

 |
| **AUD-DB-02** | Failover Runtime absent | **Haute** | `postgres_store.py:121` | Indisponibilité 503 sur coupure Neon

 |
| **AUD-CONC-02** | Bypass Fencing Token | **Haute** | `routes.py:591` | Écrasement d'état concurrent

 |
| **AUD-API-01** | Comptage Quota & 429 | **Haute** | `switchbot_api.py:152` | Quota 429 ignoré sur retry échoué

 |
| **AUD-SEC-02** | Fuite Jeton CSRF | **Haute** | `loaders.js:9` | Envoi `X-CSRFToken` hors origine

 |
| **AUD-SEC-03** | Bypass Nonce CSP | **Haute** | `spa-router.js:338` | Exécution script inline non signé

 |
| **AUD-DB-03** | Fuite Pool Migration | **Haute** | `migrate_to_postgres.py:135` | Connexions Neon non libérées

 |
| **AUD-SEC-04** | Masquage URL incomplet | **Haute** | `migrate_to_postgres.py:214` | Secrets exposés dans les logs

 |
| **AUD-DB-04** | Exceptions muettes | **Moyenne** | `postgres_store.py:57` | Masquage d'erreurs pool SQL

 |
| **AUD-PERF-01** | Requête Seq Scan + Sort | **Moyenne** | `history_service.py:338` | Tri complet table toutes les 30s

 |
| **AUD-DB-05** | Verrou pendant I/O SQL | **Moyenne** | `history_service.py:100` | Contention threads sur `_pending_lock`

 |
| **AUD-DB-06** | Sérialisation Decimal | **Moyenne** | `history_service.py:216` | `Decimal` brut non converti en `float`

 |
| **AUD-AUTO-01** | Reset `assumed_mode` | **Moyenne** | `automation.py:676` | Perte de l'état fan après scène

 |
| **AUD-AUTO-02** | Trou d'historique | **Moyenne** | `automation.py:926` | Panne capteur non historisée en créneau

 |
| **AUD-SEC-05** | Validation `_as_int` | **Moyenne** | `routes.py:784` | Exceptions non gérées sur `/history/api`

 |
| **AUD-SEC-06** | Unicode `compare_digest` | **Moyenne** | `routes.py:320` | Crash 500 si mot de passe non-ASCII

 |
| **AUD-API-02** | Absence `Session` HTTP | **Moyenne** | `switchbot_api.py:127` | Handshake TLS recréé à chaque appel

 |
| **AUD-CONC-03** | Threads `run_once` | **Moyenne** | `routes.py:562` | Création non bornée de threads

 |
| **AUD-TEST-01** | Test complaisant | **Moyenne** | `test_scheduler_service.py:72` | Masque la défaillance périodique

 |
| **AUD-SQL-01** | Index dupliqués & GIN | **Basse** | `postgres_store.py:166` | Surcharge d'écriture sur `json_store`

 |

---

## 2. Analyse Technique par Axe & Correctifs Prêts à Intégrer

### Axe 1 : Couche Persistance & Gestion du Pool (`postgres_store.py`, `config_store.py`, `history_service.py`)

#### 1.1 Auto-Deadlock sur transactions imbriquées (`AUD-DB-01` — Critique)

* **Constat** : Dans `PostgresStoreTransactionContext.__enter__` (`postgres_store.py:29-39`), l'entrée dans un bloc `with store.transaction():` sauvegarde `self._previous_transaction` mais emprunte inconditionnellement une **nouvelle connexion** au pool (`self._store.pool.connection()`) et exécute `SELECT data FROM json_store WHERE kind = %s FOR UPDATE`. Si une méthode appelée dans une transaction ouvre elle-même une transaction sur le même store (ex: `_update_state` ou `quota_tracker`), le thread courant tente de verrouiller en base la ligne qu'il détient déjà sur sa première connexion, provoquant un **auto-deadlock garanti** jusqu'au `statement_timeout` (5 s) ou un épuisement du pool (`PoolTimeout`). Dans `JsonStoreTransactionContext.__enter__` (`config_store.py:31-35`), `self._store._lock` est un `threading.Lock()` non-réentrant : une transaction imbriquée bloque définitivement le thread.


* **Constat connexe (`AUD-DB-04` — Moyenne)** : `postgres_store.py` contient 4 blocs `except Exception: pass` aux lignes 57, 62, 110 et 115, violant l'interdiction absolue des exceptions muettes de `codingstandards.md`.



```python
# Fichier : switchbot_dashboard/config_store.py (Remplacement dans JsonStore & JsonStoreTransactionContext)
class JsonStoreTransactionContext:
    def __init__(self, store: JsonStore):
        self._store = store
        self._cached_data: dict[str, Any] | None = None
        self._dirty = False
        self._is_nested = False

    def __enter__(self) -> JsonStoreTransactionContext:
        active_tx = getattr(self._store._local, "active_transaction", None)
        if active_tx is not None:
            self._is_nested = True
            return active_tx

        self._store._lock.acquire()
        try:
            self._cached_data = self._store._read_without_lock()
            self._store._local.active_transaction = self
            return self
        except Exception:
            self._store._lock.release()
            raise

    def read(self) -> dict[str, Any]:
        import copy
        return copy.deepcopy(self._cached_data or {})

    def write(self, data: dict[str, Any]) -> None:
        import copy
        self._cached_data = copy.deepcopy(data)
        self._dirty = True

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if self._is_nested:
            return
        self._store._local.active_transaction = None
        try:
            if exc_type is None and self._dirty and self._cached_data is not None:
                self._store._write_without_lock(self._cached_data)
        finally:
            self._store._lock.release()

```

```python
# Fichier : switchbot_dashboard/postgres_store.py (Remplacement de PostgresStoreTransactionContext)
class PostgresStoreTransactionContext:
    def __init__(self, store: PostgresStore):
        self._store = store
        self._conn_ctx: Any = None
        self._conn: Any = None
        self._cur: Any = None
        self._cached_data: dict[str, Any] | None = None
        self._dirty = False
        self._is_nested = False

    def __enter__(self) -> PostgresStoreTransactionContext:
        active_tx = getattr(self._store._local, "active_transaction", None)
        if active_tx is not None:
            self._is_nested = True
            return active_tx

        try:
            self._conn_ctx = self._store.pool.connection()
            self._conn = self._conn_ctx.__enter__()
            self._conn.autocommit = False
            self._cur = self._conn.cursor(row_factory=dict_row)

            # Garantit l'existence de la ligne pour poser un vrai verrou FOR UPDATE
            self._cur.execute(
                """
                INSERT INTO json_store (kind, data, updated_at)
                VALUES (%s, '{}'::jsonb, NOW())
                ON CONFLICT (kind) DO NOTHING
                """,
                (self._store._kind,),
            )
            self._cur.execute(
                "SELECT data FROM json_store WHERE kind = %s FOR UPDATE",
                (self._store._kind,),
            )
            result = self._cur.fetchone()
            data = result["data"] if result else {}
            if isinstance(data, str):
                self._cached_data = json.loads(data)
            elif isinstance(data, dict):
                self._cached_data = data
            else:
                self._cached_data = {}

            self._store._local.active_transaction = self
            return self
        except Exception as exc:
            self._cleanup_resources(type(exc), exc, exc.__traceback__)
            raise PostgresStoreError(
                f"Failed to start transaction for {self._store._kind} store"
            ) from exc

    def _cleanup_resources(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if self._cur is not None:
            try:
                self._cur.close()
            except Exception as cur_exc:
                self._store._logger.warning(
                    "[store] Failed to close cursor for %s store (%s)",
                    self._store._kind,
                    cur_exc,
                )
            finally:
                self._cur = None
        if self._conn_ctx is not None:
            try:
                self._conn_ctx.__exit__(exc_type, exc_val, exc_tb)
            except Exception as conn_exc:
                self._store._logger.warning(
                    "[store] Failed to return connection to pool for %s store (%s)",
                    self._store._kind,
                    conn_exc,
                )
            finally:
                self._conn_ctx = None
                self._conn = None

    def read(self) -> dict[str, Any]:
        import copy
        return copy.deepcopy(self._cached_data or {})

    def write(self, data: dict[str, Any]) -> None:
        import copy
        self._cached_data = copy.deepcopy(data)
        self._dirty = True

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if self._is_nested:
            return
        self._store._local.active_transaction = None
        try:
            if exc_type is not None:
                self._conn.rollback()
                self._store._logger.info(
                    "[store] Transaction rolled back for %s store due to exception: %s",
                    self._store._kind,
                    exc_val,
                )
            elif self._dirty:
                query = sql.SQL("""
                    INSERT INTO json_store (kind, data, updated_at)
                    VALUES (%s, %s, NOW())
                    ON CONFLICT (kind)
                    DO UPDATE SET
                        data = EXCLUDED.data,
                        updated_at = EXCLUDED.updated_at
                """)
                self._cur.execute(query, (self._store._kind, Jsonb(self._cached_data)))
                self._conn.commit()
            else:
                self._conn.commit()
        except Exception as exc:
            self._store._logger.error(
                "[store] Failed to finalize transaction for %s store (%s)",
                self._store._kind,
                exc,
            )
            if exc_type is None:
                raise PostgresStoreError(
                    f"Failed to commit PostgreSQL transaction for {self._store._kind} store"
                ) from exc
        finally:
            self._cleanup_resources(exc_type, exc_val, exc_tb)

```

#### 1.2 Absence de Failover Runtime `PostgresStore` -> `JsonStore` après 3 échecs (`AUD-DB-02` — Haute)

* **Constat** : `codingstandards.md` impose : *"Sur incident Postgres (pool KO, SSL, timeout), consigner l’erreur, retenter côté scheduler, puis alerter si >3 échecs consécutifs."* Or, la bascule n'est implémentée qu'à l'initialisation de l'application (`_build_store`). Si Neon PostgreSQL coupe les connexions en cours d'exécution, `PostgresStore` lève `PostgresStoreError` indéfiniment sans compteur d'échecs consécutifs ni dégradation contrôlée. De plus, les logs de `postgres_store.py` utilisent le préfixe `[postgres]` au lieu du préfixe réglementaire `[store]`.



#### 1.3 Performances SQL, Verrouillage et Conversion `Decimal` dans `HistoryService` (`AUD-PERF-01`, `AUD-DB-05`, `AUD-DB-06` — Moyenne)

* **Constat** :
1. `get_latest_records()` (`history_service.py:338-343`) exécute `SELECT DISTINCT ON (date_trunc('minute', timestamp)) * FROM state_history ORDER BY date_trunc('minute', timestamp) DESC, timestamp DESC LIMIT %s`. PostgreSQL ne pouvant pas exploiter l'index `idx_state_history_timestamp` sur une expression `date_trunc(...)`, il effectue un tri complet des lignes de la table à chaque rafraîchissement (toutes les 30s).


2. `get_aggregates()` (`history_service.py:216`) retourne directement le dictionnaire `psycopg` contenant des instances `decimal.Decimal` (`avg_temperature`, `min_temperature`, etc.) sans les convertir en `float`, contrairement à `_format_history_results()`.


3. `record_state()` (`history_service.py:100-101`) appelle `_flush_pending_records_locked()` en maintenant `self._pending_lock` pendant toute la transaction réseau PostgreSQL.





```python
# Fichier : switchbot_dashboard/history_service.py (Optimisation get_aggregates et get_latest_records)
    def get_aggregates(self, period_hours: int = 1) -> dict[str, Any]:
        from decimal import Decimal
        query = sql.SQL("""
            SELECT 
                COUNT(*) as total_records,
                ROUND(AVG(temperature)::numeric, 1) as avg_temperature,
                MIN(temperature) as min_temperature,
                MAX(temperature) as max_temperature,
                ROUND(AVG(humidity)::numeric, 1) as avg_humidity,
                MIN(humidity) as min_humidity,
                MAX(humidity) as max_humidity,
                MODE() WITHIN GROUP (ORDER BY assumed_aircon_power) as common_aircon_state,
                COUNT(DISTINCT last_action) as distinct_actions,
                COALESCE(SUM(error_count), 0) as total_errors,
                COALESCE(MAX(api_requests_today), 0) as max_api_requests
            FROM state_history
            WHERE timestamp >= NOW() - make_interval(hours => %s)
        """)
        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, (period_hours,))
                    result = cur.fetchone()
                    if not result:
                        return {}
                    return {
                        k: float(v) if isinstance(v, Decimal) else v
                        for k, v in result.items()
                    }
        except Exception as exc:
            self._logger.error("[history] Failed to get aggregates (%s)", exc)
            raise HistoryServiceError("Failed to get aggregated statistics") from exc

    def get_latest_records(self, limit: int = 10) -> list[dict[str, Any]]:
        from decimal import Decimal
        # Utilise un sous-ensemble indexé sur timestamp DESC avant déduplication par minute
        query = sql.SQL("""
            SELECT DISTINCT ON (date_trunc('minute', sub.timestamp)) sub.*
            FROM (
                SELECT *
                FROM state_history
                ORDER BY timestamp DESC
                LIMIT %s
            ) sub
            ORDER BY date_trunc('minute', sub.timestamp) DESC, sub.timestamp DESC
            LIMIT %s
        """)
        try:
            with self._pool.connection() as conn:
                with conn.cursor(row_factory=dict_row) as cur:
                    cur.execute(query, (max(limit * 10, 100), limit))
                    results = cur.fetchall()
                    for result in results:
                        if "timestamp" in result and result["timestamp"]:
                            result["timestamp"] = result["timestamp"].isoformat()
                        if "metadata" in result and result["metadata"]:
                            result["metadata"] = dict(result["metadata"])
                        for k, v in result.items():
                            if isinstance(v, Decimal):
                                result[k] = float(v)
                    return results
        except Exception as exc:
            self._logger.error("[history] Failed to get latest records (%s)", exc)
            raise HistoryServiceError("Failed to get latest records") from exc

```

---

### Axe 2 : Concurrence & Moteur d'Automatisation (`automation.py`, `routes.py`)

#### 2.1 Race Condition critique dans `CachedStoreWrapper` et pollution de `ApiQuotaTracker` (`AUD-CONC-01` — Critique)

* **Constat** :
1. `CachedStoreWrapper` (`automation.py:101-143`) stocke `self._cache` comme attribut d'instance (`self._cache: dict[str, Any] | None = None`) **partagé entre tous les threads** sans `threading.local()` ni `threading.Lock()`.


2. Aux lignes 183-185, `AutomationService.__init__` écrase la référence `_state_store` du singleton `ApiQuotaTracker` par ce `CachedStoreWrapper` (`self._client._quota_tracker._state_store = self._state_store`).


3. Lorsqu'un thread HTTP exécute `/devices`, `/quota/refresh` ou `/actions/*` pendant ou en dehors d'un tick du scheduler, il lit et écrit dans le même `self._cache` non protégé que le thread APScheduler, et `run_once()` appelle `clear_cache()` (ligne 787) de manière asynchrone vis-à-vis des requêtes HTTP. En isolant le cache dans `threading.local()`, chaque thread dispose de son propre cycle de vie de cache sans jamais corrompre un thread concurrent.





```python
# Fichier : switchbot_dashboard/automation.py (Remplacement de CachedStoreWrapper, lignes 101-143)
class CachedStoreWrapper:
    """Thread-local proxy store that caches reads and writes during a single execution context."""

    def __init__(self, store: BaseStore) -> None:
        self._store = store
        import threading
        self._local = threading.local()

    def clear_cache(self) -> None:
        self._local.cache = None

    def read(self) -> dict[str, Any]:
        cache = getattr(self._local, "cache", None)
        if cache is None:
            cache = self._store.read()
            self._local.cache = cache
        return copy.deepcopy(cache)

    def write(self, data: dict[str, Any]) -> None:
        self._local.cache = copy.deepcopy(data)
        self._store.write(data)

    def transaction(self) -> Any:
        import contextlib

        @contextlib.contextmanager
        def _tx_scope() -> Any:
            self.clear_cache()
            try:
                if hasattr(self._store, "transaction"):
                    with self._store.transaction() as tx:
                        yield tx
                else:
                    yield
            finally:
                self.clear_cache()

        return _tx_scope()

```

#### 2.2 Contournement du Fencing Token et incohérence `assumed_aircon_mode` (`AUD-CONC-02` — Haute, `AUD-AUTO-01` & `AUD-AUTO-02` — Moyenne)

* **Constat** :
1. Dans `routes.py` (`_handle_direct_action`, lignes 591-677), la route acquiert le verrou via `automation_service._acquire_lock()`, mais effectue ses écritures via `_update_state_on_success(state_store, ...)` et `state_store.write(state)` directement sur l'objet `state_store` brut sans vérifier `automation_lock_token` ni nettoyer `current_lock_token` dans `finally:`.


2. Dans `automation.py` (`_trigger_scene`, lignes 675-680), l'exécution d'une scène réinitialise `assumed_aircon_mode=None` alors que `_handle_direct_action` (`routes.py:601-616`) affecte `4` (fan), `5` (winter) ou `2` (summer). Fixer le mode correspondant à `action_key` dans `_trigger_scene` garantit la cohérence de `is_in_fan_mode`.


3. Dans `automation.py` (`_run_once_impl`, lignes 926-930), un échec de `poll_meter()` à l'intérieur d'une fenêtre horaire interrompt la fonction (`return`) avant `self._record_history_snapshot(timezone_name, trigger=trigger)`, omettant d'historiser l'état `last_temperature_stale=True`.





```python
# Fichier : switchbot_dashboard/automation.py (Correction dans _trigger_scene et _run_once_impl)
        # Dans _trigger_scene (lignes 673-683) :
        mode_map = {"fan": 4, "winter": 5, "summer": 2}
        try:
            self._client.run_scene(scene_id)
            self._log_quota_snapshot(context=f"scene_{action_key}")
            self._update_state(
                assumed_aircon_power=assumed_power,
                assumed_aircon_mode=mode_map.get(action_key),
                assumed_aircon_parameter=None,
                last_action=f"scene({scene_id}) ({state_reason})",
                last_action_at=_utc_now_iso(),
                last_error=None,
            )
            return True

        # Dans _run_once_impl (lignes 928-931) :
        if not reading or reading.get("temperature") is None:
            self._debug("Meter reading unavailable; aborting automation tick", trigger=trigger)
            self._record_history_snapshot(timezone_name, trigger=trigger)
            self._log_tick_completion(trigger, outcome="missing_meter")
            return

```

---

### Axe 3 : Planificateur & Cycle de Vie (`scheduler.py`)

#### 3.1 Exception non gérée dans `_maybe_reschedule_after_tick()` et suppression prématurée du Job (`AUD-SCHED-01` — Critique)

* **Constat** : Dans `SchedulerService._run_tick_safe()` (`scheduler.py:34-46`), `self._maybe_reschedule_after_tick()` est appelé dans le bloc `finally:` sans protection `try/except`. Or, `_maybe_reschedule_after_tick()` appelle `_get_effective_interval_seconds()` qui interroge `self._settings_store.read()` (ligne 109) et `self._state_store.read()` (ligne 59). Si la base PostgreSQL est momentanément indisponible, `_maybe_reschedule_after_tick()` lève une `PostgresStoreError` non interceptée. De plus, dans `_schedule_or_reschedule_locked()` (lignes 206-219), `existing_job.remove()` est appelé avant `add_job(..., replace_existing=True)` : si une erreur survient entre les deux ou dans `reschedule()`, le job disparaît définitivement du scheduler.



```python
# Fichier : switchbot_dashboard/scheduler.py (Remplacement des lignes 34-47 et 167-230)
    def _run_tick_safe(self) -> None:
        """Execute tick callable while guarding against uncaught exceptions."""
        self._last_tick_time = dt.datetime.now(dt.timezone.utc)
        try:
            self._tick_callable()
        except Exception as exc:
            self._logger.error(
                "[scheduler] Automation tick raised exception: %s",
                exc,
                exc_info=True,
            )
        finally:
            try:
                self._maybe_reschedule_after_tick()
            except Exception as exc:
                self._logger.error(
                    "[scheduler] Post-tick reschedule failed (store unavailable?): %s",
                    exc,
                    exc_info=True,
                )

    def _schedule_or_reschedule_locked(self, desired_interval: int | None = None) -> None:
        if self._scheduler is None:
            self._logger.warning("[scheduler] Cannot schedule job: scheduler is None")
            return

        interval = desired_interval if desired_interval is not None else self._get_interval_seconds()

        # Utiliser replace_existing=True de manière atomique sans supprimer le job au préalable
        self._scheduler.add_job(
            func=self._run_tick_safe,
            trigger="interval",
            seconds=interval,
            id=self._job_id,
            replace_existing=True,
            max_instances=1,
            coalesce=True,
        )
        self._current_interval_seconds = interval
        self._logger.info("[scheduler] Job scheduled with interval=%d seconds", interval)

    def reschedule(self) -> None:
        with self._lock:
            if self._scheduler is None:
                self._logger.debug(
                    "[scheduler] Reschedule called but scheduler not started (normal if SCHEDULER_ENABLED=false)"
                )
                return

            try:
                self._logger.info("[scheduler] Rescheduling automation job")
                self._schedule_or_reschedule_locked()
            except Exception as exc:
                self._logger.error(
                    "[scheduler] Failed to reschedule automation job: %s",
                    exc,
                    exc_info=True,
                )

```

---

### Axe 4 : Intégration API Externe & Gestion Quotas (`switchbot_api.py`, `quota.py`)

#### 4.1 Défense SSRF sur `base_url`, Préfixe `[api]`, Session HTTP et Quotas sur Retry (`AUD-SEC-01`, `AUD-API-01` — Haute, `AUD-API-02` — Moyenne)

* **Constat** :
1. **SSRF & HTTPS** : `SwitchBotClient.__init__` (`switchbot_api.py:48`) accepte n'importe quelle `base_url` sans vérifier le schéma `https://` ni bloquer les adresses IP privées, loopback ou link-local (`169.254.169.254`, `127.0.0.0/8`, RFC 1918), exposant les en-têtes `Authorization` et `sign` en cas de mauvaise configuration.


2. **Perte de suivi quota sur HTTP 429/5xx retryable** : Dans `_request()` (`switchbot_api.py:152-158`), lorsqu'un `GET` reçoit un code 429 ou 5xx et qu'il reste une tentative, la boucle exécute `continue` **avant** `self._capture_quota_metadata(response)`. Si la tentative suivante échoue sur un timeout réseau (`requests.RequestException`), le `remaining=0` du 429 initial est perdu et les appels consommés ne sont jamais enregistrés.


3. **Absence de préfixe `[api]` et fuite des headers** : Aucun log de `switchbot_api.py` ne porte le préfixe `[api]`, et la ligne 148 loggue `dict(response.headers)` brut.





```python
# Fichier : switchbot_dashboard/switchbot_api.py (Validation SSRF et capture systématique du quota)
import ipaddress
import socket
from urllib.parse import urlsplit

def _validate_https_base_url(raw_url: str) -> str:
    parsed = urlsplit(raw_url.strip())
    if parsed.scheme.lower() != "https" or not parsed.hostname:
        raise SwitchBotApiError(f"[api] Invalid SwitchBot base_url (HTTPS required): {raw_url!r}")
    if parsed.username or parsed.password:
        raise SwitchBotApiError("[api] Credentials in base_url are forbidden")
    try:
        ip_obj = ipaddress.ip_address(parsed.hostname)
        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local or ip_obj.is_reserved:
            raise SwitchBotApiError(f"[api] Private or loopback IP forbidden in base_url: {parsed.hostname}")
    except ValueError:
        # Hostname DNS standard
        if parsed.hostname.lower() in ("localhost", "localhost.localdomain"):
            raise SwitchBotApiError("[api] Localhost forbidden in base_url")
    return raw_url.strip().rstrip("/")

```

Dans `SwitchBotClient._request` (`switchbot_api.py:143-167`), placez `tracker_updated = self._capture_quota_metadata(response)` **immédiatement après** `requests.request(...)`, avant le branchement `if retryable_http and is_get`:

```python
            tracker_updated = self._capture_quota_metadata(response)
            logger.debug(
                "[api] SwitchBot %s %s -> HTTP %s",
                method,
                path,
                response.status_code,
            )

            retryable_http = response.status_code == 429 or 500 <= response.status_code <= 599
            if retryable_http and is_get and attempt_index < (self._retry_attempts - 1):
                delay = self._parse_retry_after(response, attempt_index)
                time.sleep(delay)
                continue

```

---

### Axe 5 : Sécurité des Contrôleurs, Validation & Utilitaires (`routes.py`, `utils.py`)

#### 5.1 Contournement de `_as_int` et crash `TypeError` sur `/history/api/*` (`AUD-SEC-05` — Moyenne)

* **Constat** :
1. `routes.py:884` (`int(request.args.get("period_hours", 1))`) et `routes.py:954` (`int(request.args.get("limit", 10))`) n'utilisent pas `_as_int`, contrairement aux règles de `codingstandards.md`. Toute chaîne non numérique déclenche `logger.exception`.


2. Dans `_parse_history_query_params` (`routes.py:784-788`), `dt.datetime.fromisoformat()` est utilisé directement au lieu de `_parse_iso_datetime()` de `utils.py`. Si un paramètre a un fuseau et l'autre non, `if start >= end:` lève `TypeError` (non capturée par `except ValueError:` à la ligne 840). De plus, les métriques demandées ne sont pas filtrées par une liste blanche avant d'être renvoyées dans la réponse JSON.





```python
# Fichier : switchbot_dashboard/routes.py (Remplacement de _parse_history_query_params et validation /history/api/*)
ALLOWED_HISTORY_METRICS = {
    "timestamp",
    "temperature",
    "humidity",
    "assumed_aircon_power",
    "last_action",
    "api_requests_today",
    "error_count",
    "last_temperature_stale",
}

def _parse_history_query_params(request_args: Any) -> tuple[dt.datetime, dt.datetime, list[str], str, int]:
    start_str = request_args.get("start")
    end_str = request_args.get("end")
    metrics_param = request_args.get("metrics")
    granularity = request_args.get("granularity", "minute")
    limit = _as_int(request_args.get("limit"), default=1000, minimum=1, maximum=10000)

    metrics: list[str] = []
    if metrics_param:
        raw_metrics = (
            [m.strip() for m in metrics_param.split(",") if m.strip()]
            if isinstance(metrics_param, str)
            else list(metrics_param)
        )
        metrics = [m for m in raw_metrics if m in ALLOWED_HISTORY_METRICS]

    if not start_str or not end_str:
        end = dt.datetime.now(dt.timezone.utc)
        start = end - dt.timedelta(hours=6)
    else:
        parsed_start = _parse_iso_datetime(start_str)
        parsed_end = _parse_iso_datetime(end_str)
        if parsed_start is None or parsed_end is None:
            raise ValueError("invalid ISO-8601 datetime format")
        start, end = parsed_start, parsed_end

    if start >= end:
        raise ValueError("start time must be before end time")

    if (end - start) > dt.timedelta(days=31):
        raise ValueError("requested time range exceeds 31 days maximum")

    valid_granularities = {"minute", "5min", "15min", "hour"}
    if granularity not in valid_granularities:
        granularity = "minute"

    return start, end, metrics, granularity, limit

```

Dans `history_api_aggregates` (`routes.py:884`) et `history_api_latest` (`routes.py:954`), remplacez les conversions `int(...)` brutes par :

```python
# Dans history_api_aggregates (ligne 884) :
period_hours = _as_int(request.args.get("period_hours"), default=1, minimum=1, maximum=24)

# Dans history_api_latest (ligne 954) :
limit = _as_int(request.args.get("limit"), default=10, minimum=1, maximum=100)

```

#### 5.2 Crash `TypeError` sur `hmac.compare_digest` avec entrées UTF-8 et booléens dans `_safe_int` (`AUD-SEC-06` — Moyenne)

* **Constat** :
1. Dans `routes.py:320` et `357`, `hmac.compare_digest(provided_password, expected_password)` est appelé sur des objets `str`. En Python, `hmac.compare_digest` lève `TypeError: unsupported operand types(s) or combination of types: 'str' and 'str'` dès que l'utilisateur saisit un caractère accentué ou non-ASCII (ex: `é`, `€`).


2. Dans `utils.py:7` (`_safe_int`), `int(True)` retourne `1` car `bool` hérite de `int` en Python.





```python
# Fichier : switchbot_dashboard/routes.py (Lignes 319-321 et 357)
        elif expected_password:
            is_valid = hmac.compare_digest(
                provided_password.encode("utf-8"),
                expected_password.encode("utf-8"),
            )

```

```python
# Fichier : switchbot_dashboard/utils.py (Ligne 7)
def _safe_int(value: Any, *, default: int, minimum: int | None = None, maximum: int | None = None) -> int:
    if isinstance(value, bool):
        parsed = default
    else:
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            parsed = default

```

---

### Axe 6 : Évaluation de la Suite de Tests & Zones Non Couvertes (`tests/`)

1. **Neutralisation d'un test critique dans `tests/test_scheduler_service.py:72-116` (`AUD-TEST-01`)** :
Le test `test_scheduler_interval_job_executes_periodically` contient un commentaire explicite indiquant que les ticks périodiques échouaient sous certains environnements et abaisse l'assertion finale à `assert len(call_timestamps) >= 1` (toujours vraie grâce au tick initial synchrone). Cela viole l'invariant 1 de `architecte.md` (*"Tout code temporaire ou complaisant doit être traité comme permanent et dangereux"*).


2. **Zones critiques non couvertes par la suite actuelle** :
* **Transactions imbriquées (`PostgresStore` / `JsonStore`)** : Aucun test dans `test_phase3.py` ne vérifie l'ouverture d'un bloc `with store.transaction():` à l'intérieur d'un autre bloc `with store.transaction():` (qui aurait immédiatement révélé le deadlock `AUD-DB-01`).


* **Concurrence multi-threads sur `CachedStoreWrapper**` : Aucun test n'exécute simultanément `AutomationService.run_once()` et une route HTTP consommant `ApiQuotaTracker` (`AUD-CONC-01`).


* **Résilience de `SchedulerService._run_tick_safe()` sur panne DB** : `test_run_tick_safe_logs_exceptions` (`test_scheduler_service.py:165`) utilise un `MemoryStore` qui ne lève jamais `StoreError` lors de l'appel à `_maybe_reschedule_after_tick()` dans le bloc `finally:` (`AUD-SCHED-01`).


* **Entrées malformées sur `/history/api/***` : Aucun test ne passe `?period_hours=invalid`, `?limit=invalid`, ou des dates mixtes naive/aware à `/history/api/data` (`AUD-SEC-05`).





---

## 3. Plan de Remédiation Priorisé

1. **Priorité P0 — Stabilité & Concurrence (Immédiat, < 2h)** :
* Isoler `CachedStoreWrapper` avec `threading.local()` dans `switchbot_dashboard/automation.py` (`AUD-CONC-01`).


* Rendre `PostgresStoreTransactionContext` et `JsonStoreTransactionContext` réentrants par thread et supprimer les 4 blocs `except Exception: pass` dans `postgres_store.py` (`AUD-DB-01`, `AUD-DB-04`).


* Encapsuler `self._maybe_reschedule_after_tick()` et `reschedule()` dans un bloc `try/except` au sein de `switchbot_dashboard/scheduler.py` et supprimer le `existing_job.remove()` prématuré (`AUD-SCHED-01`).




2. **Priorité P1 — Sécurité Applicative & Réseau (Court terme, < 3h)** :
* Ajouter `_validate_https_base_url()` dans `switchbot_api.py` et déplacer `_capture_quota_metadata()` avant le branchement de retry HTTP (`AUD-SEC-01`, `AUD-API-01`).


* Restreindre l'intercepteur CSRF de `loaders.js` à la même origine (`isSameOrigin`) et vérifier le `nonce` CSP serveur dans `spa-router.js` (`AUD-SEC-02`, `AUD-SEC-03`).


* Encoder les chaînes en UTF-8 avant `hmac.compare_digest` dans `routes.py` et remplacer les `int()` / `fromisoformat()` directs des routes `/history/api/*` par `_as_int` et `_parse_iso_datetime` (`AUD-SEC-05`, `AUD-SEC-06`).


* Corriger la fuite du pool `kind="temp"` et le masquage d'URL dans `scripts/migrate_to_postgres.py` (`AUD-DB-03`, `AUD-SEC-04`).




3. **Priorité P2 — Performance SQL & Cohérence Métier (Moyen terme, < 4h)** :
* Optimiser `get_latest_records()` et convertir les `Decimal` en `float` dans `get_aggregates()` au sein de `history_service.py` (`AUD-PERF-01`, `AUD-DB-06`).


* Conserver `assumed_aircon_mode` lors de l'exécution de scènes dans `automation.py` et appeler `_record_history_snapshot` en cas d'échec de `poll_meter()` (`AUD-AUTO-01`, `AUD-AUTO-02`).


* Ajouter les tests unitaires de non-régression couvrant les transactions imbriquées, la panne de store pendant `_maybe_reschedule_after_tick()`, et les entrées non-ASCII/malformées sur `/login` et `/history/api/*`.