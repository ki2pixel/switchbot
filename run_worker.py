#!/usr/bin/env python
from __future__ import annotations

import os
import time
import logging

# Force scheduler to be enabled inside this worker process
os.environ["SCHEDULER_ENABLED"] = "true"

# Prevent the Flask debug reloader from spawning duplicate schedulers in the worker
os.environ["FLASK_DEBUG"] = "0"
os.environ["WERKZEUG_RUN_MAIN"] = "true"

from switchbot_dashboard import create_app

if __name__ == "__main__":
    app = create_app()
    app.logger.info("[worker] Standalone background worker started successfully")

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        app.logger.info("[worker] Standalone background worker stopping")
        raise
