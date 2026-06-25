from celery import Celery
from config import config

# Create Celery application
celery_app = Celery(
    "research_tasks",
    broker=config.CELERY_BROKER_URL,
    backend=config.CELERY_RESULT_BACKEND
)

# Optional: Celery configuration
celery_app.conf.update(
    task_track_started=True,
    result_expires=3600,   # 1 hour
)
