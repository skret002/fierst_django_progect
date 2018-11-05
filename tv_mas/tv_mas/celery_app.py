import os
from celery import Celery
from django.conf import settings

__autor__ = 'mevlutov'

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'tv_mas.settings')

app = Celery('parser')


app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)