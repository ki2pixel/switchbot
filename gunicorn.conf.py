"""Gunicorn configuration for SwitchBot Dashboard.

Uses a single worker to avoid APScheduler conflicts.
For background job scheduling (APScheduler), multiple workers would
create duplicate scheduled tasks running in parallel.
"""
import os


# Single worker to prevent APScheduler conflicts
# Force 1 worker if scheduler is enabled to prevent duplicate jobs
scheduler_enabled = str(os.environ.get("SCHEDULER_ENABLED", "true")).lower() == "true"
if scheduler_enabled:
    workers = 1
else:
    workers = int(os.environ.get("WEB_CONCURRENCY", "1"))
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
timeout = 30
accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("LOG_LEVEL", "info").lower()

# Worker class optimized for I/O bound operations (SwitchBot API calls)
worker_class = "gthread"
threads = 4
