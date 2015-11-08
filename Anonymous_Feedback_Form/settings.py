"""
Django settings for Anonymous_Feedback_Form project.

https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
from enum import Enum

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Environment = Enum('Environment', ("development", "production"))

ENVIRONMENT = (Environment.development if os.path.exists('.development')
               else Environment.production)


if ENVIRONMENT is Environment.development:
    SECRET_KEY = (os.environ.get('DJANGO_SECRET_KEY')
                  or "fake_development_unsecret_key")
else:
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')


DEBUG = os.environ.get('DJANGO_DEBUG') or ENVIRONMENT is Environment.development

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feedback',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Anonymous_Feedback_Form.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Anonymous_Feedback_Form.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

FEEDBACK_SUBJECT = os.environ.get('FEEDBACK_SUBJECT')
FEEDBACK_SUBJECT_INITIALS = os.environ.get('FEEDBACK_SUBJECT_INITIALS')
