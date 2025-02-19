from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffee_shop_backend.settings')  # Replace 'your_project' with your project name

app = Celery('coffee_shop_backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
