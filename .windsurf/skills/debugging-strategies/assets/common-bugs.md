# Bugs Fréquents et Solutions

1. **Quota API Exceed (429)**
   - *Cause* : Trop d'appels à l'API SwitchBot.
   - *Solution* : Vérifier l'`ApiQuotaTracker` et augmenter le `poll_interval_seconds`.

2. **Database Timeout (psycopg_pool)**
   - *Cause* : Pool de connexion saturé ou connexion interrompue.
   - *Solution* : Implémenter des retries côté scheduler ou redémarrer le service Render.

3. **Bandeau de loader bloqué**
   - *Cause* : Une action réseau n'a pas déclenché son `finally` en JavaScript.
   - *Solution* : Vérifier `static/js/loaders.js` et s'assurer que le failsafe de 15s est bien actif.
