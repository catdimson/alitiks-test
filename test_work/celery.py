import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_work.settings')

app = Celery('test_work')       # передаем название проекта
app.config_from_object('django.conf:settings', namespace='CELERY')  # подцепляются настройки с преффиксом CELERY
app.autodiscover_tasks()    # автоматически подцеплять наши таски
