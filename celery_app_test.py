from celery import Celery

from celery_config import celery_app
# celery_app = Celery(
#     "worker",
#     broker="redis://localhost:6379/0",
#     backend="redis://localhost:6379/0"
# )

@celery_app.task
def background_task(x, y):
    return x + y
