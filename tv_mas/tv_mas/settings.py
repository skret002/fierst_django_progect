"""
Django settings for tv_mas project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ig2$@lvzeclp4f0drn0_k0k4qyj5os$zctt_kdapw+8#&f*fae'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS =  ['*']

# Application definition
if DEBUG:
    INTERNAL_IPS = ('127.0.0.1', 'localhost',)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'debug_toolbar',
    'django_summernote',
    'django_user_agents',
    'django.contrib.postgres',
    'imagekit',
    'djcelery',
    'phonenumber_field',
    #'django_celery_beat',
    'import_export',


    'main',
    'SEO',
    'suvenirka_product',
    'suvenirka_order',
    'slider_up',
    'accounts',
    'emails',
    'utils',
    'repair_tv',
    'smartfon',
    'notebook',
    'photo',
    'just_print_photo',
    'print_documents',
    'refcartridges',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'tv_mas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'suvenirka_order.context_processors.getting_basket_info',

            ],
        },
    },
]

WSGI_APPLICATION = 'tv_mas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'RU-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "templates","static", "media")
#STATIC_ROOT = os.path.join(BASE_DIR, 'templates/static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static') # /home/user/app/static
]
AUTH_PROFILE_MODULE = 'accounts.Profile'


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
#LOGIN_REDIRECT_URL = ''


#DEBUG_TOOLBAR_PANELS = [
#       'debug_toolbar.panels.versions.VersionsPanel',
#       'debug_toolbar.panels.timer.TimerPanel',
#       'debug_toolbar.panels.settings.SettingsPanel',
#       'debug_toolbar.panels.headers.HeadersPanel',
#       'debug_toolbar.panels.request.RequestPanel',
#       'debug_toolbar.panels.sql.SQLPanel',
#       'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#       'debug_toolbar.panels.templates.TemplatesPanel',
#       'debug_toolbar.panels.cache.CachePanel',
#       'debug_toolbar.panels.signals.SignalsPanel',
#       'debug_toolbar.panels.logging.LoggingPanel',
#       'debug_toolbar.panels.redirects.RedirectsPanel',
#]
#Celery
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab
import djcelery
djcelery.setup_loader()

#Redis
REDIS_BACKEND = {
    'HOST': 'localhost',
    'PORT':6379,
    'DB':0
}
REDIS_BACKEND_URL = 'redis://{host}:{port}/{db}'.format(
    host=REDIS_BACKEND['HOST'],
    port=REDIS_BACKEND['PORT'],
    db=REDIS_BACKEND['DB'],
)

CELERY_RESULT_BACKEND = 'djcelery.backends.database.DatabaseBackend'
CELERY_TASK_RESULT_EXPIRES = 18000
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
BROKER_URL = REDIS_BACKEND_URL

CELERYBEAT_SCHEDULER ="djcelery.schedulers.DatabaseScheduler"
CELERYBEAT_SCHEDULE={
    #'parser_rem_aud':{

        #'task':'repair_tv.tasks.main_rem_aud',
        #'schedule':crontab(hour=13, minute=12, day_of_week=2),
    #},
    #'parser_main_toshiba':{

        #'task':'repair_tv.tasks.main_toshiba',
        #'schedule':crontab(hour=13, minute=12, day_of_week=2),
    #},
    #    'parser_main_lg':{

        #'task':'repair_tv.tasks.main_lg',
        #'schedule':crontab(hour=13, minute=12, day_of_week=2),
    #},
    #    'parser_main_sony':{

        #'task':'repair_tv.tasks.main_sony',
        #'schedule':crontab(hour=11, minute=00, day_of_week=2),
    #},
    #    'parser_main_samsung':{

        #'task':'repair_tv.tasks.main_samsung',
        #'schedule':crontab(hour=13, minute=12, day_of_week=2),
    #},
    #    'parser_main_philips':{
        #'task':'repair_tv.tasks.main_philips',
        #'schedule':crontab(hour=13, minute=12, day_of_week=2),
    #},
    #    'parser_gadget':{
    #    'task':'smartfon.tasks.main',
    #    'schedule':crontab(hour=14, minute=28,day_of_week=5 ),
    #}   
        'parser_partsderect':{
        'task':'notebook.tasks.main',
        'schedule':crontab(hour=11, minute=42, day_of_week=6),
    }


}

#DEBUG
DEBUG_TOOLBAR_CONFIG = {
       'INTERCEPT_REDIRECTS': False,
   }


SESSION_ENGINE = 'suvenirka_order.session_backend'

#MAIL
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "79219032885@ya.ru"
EMAIL_HOST_PASSWORD = "oltexservis36"
EMAIL_USE_SSL = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
FROM_EMAIL = "79219032885@ya.ru"
EMAIL_ADMIN = "79219032885@ya.ru"
