from .settings import *
import dj_database_url

DEBUG=False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "whitenoise.runserver_nostatic", # SERVE  STATICFILE WITH WHITENOISE THIS THE FIRST METHOD TO SERVE STATIC FILE YOU CAN USE NGINX OR APACHE

    
# third party applications
    'formtools',
    'widget_tweaks',
    'import_export',
    'django_extensions',
    'bootstrap4',

# my applications
    'main_app',
    'compte',
    'dashboard',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DATABASES = {
        'default': dj_database_url.parse(config('DATABASE_URL'))
    }

CELERY_BROKER_URL = 'redis://red-ckcmr36smu8c73djkrt0:6379'
CELERY_RESULT_BACKEND = 'redis://red-ckcmr36smu8c73djkrt0:6379'