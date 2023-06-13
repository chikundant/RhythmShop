import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rhythm.settings')

celery = Celery('rhythm')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()

celery.conf.beat_schedule = {
    'send-mail-every-first-day-of-month': {
        'task': 'orders.tasks.send_beat_email',
        'schedule': crontab(day_of_month='*/1')
    }
}


@celery.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
