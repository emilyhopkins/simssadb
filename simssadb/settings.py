"""
Django settings for simssadb project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from distutils.util import strtobool

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'database',
                            'templates')  # you can define multiple template
# dir and Django will
# look through all of them. This one is used for customized resetting
# password page of the user
TEMPLATE_DIR2 = os.path.join(BASE_DIR, 'database', 'templates', 'database')
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'database', 'locale'),
    # include translation file path
    )
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f1(1=m5ze=@ne023nnabwz(%x^j+8!y+py&n$4#lwv$8o0&(#c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'database.apps.DatabaseConfig',
    'rest_framework',
    'django_db_constraints',
    'haystack',
    'dal',
    'dal_select2',
    'viapy',
    'autotranslate',
    'django.contrib.admindocs',
    'widget_tweaks',
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/simssadb',
        'ADMIN_URL': 'http://127.0.0.1:8983/solr/',
        'INCLUDE_SPELLING': 'True'
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'simssadb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, TEMPLATE_DIR2],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'simssadb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'simssadb',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
        'PASSWORD': 'debug'
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '@gmail.com'  # please consult lab wiki for email address and password
EMAIL_HOST_PASSWORD = 'PASSWORD'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # Use Django "dummy" email service which sends emails through the Django console
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

#LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True # activate internationalization

USE_L10N = True # activate localization

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('de', _('German')),
    ('zh', _('Chinese')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('es', _('Spanish')),
    ('pt', _('Portuguese')),
    ('it', _('Italian')),
    ('ar', _('Arabic')),
    ('fa', _('Persian')),
)
#AUTOTRANSLATE_TRANSLATOR_SERVICE = 'autotranslate.services.GoogleAPITranslatorService'  # use google translate api
#GOOGLE_TRANSLATE_KEY = '<google-api-key>'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1', 'localhost',)

    INSTALLED_APPS += (
       'debug_toolbar',
    )

    DEBUG_TOOLBAR_PANELS = [
       'debug_toolbar.panels.versions.VersionsPanel',
       'debug_toolbar.panels.timer.TimerPanel',
       'debug_toolbar.panels.settings.SettingsPanel',
       'debug_toolbar.panels.headers.HeadersPanel',
       'debug_toolbar.panels.request.RequestPanel',
       'debug_toolbar.panels.sql.SQLPanel',
       'debug_toolbar.panels.staticfiles.StaticFilesPanel',
       'debug_toolbar.panels.templates.TemplatesPanel',
       'debug_toolbar.panels.cache.CachePanel',
       'debug_toolbar.panels.signals.SignalsPanel',
       'debug_toolbar.panels.logging.LoggingPanel',
       'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
       'INTERCEPT_REDIRECTS': False,
    }
# Media files (symbolic music files, audio, images)
MEDIA_URL = os.path.join(BASE_DIR, 'media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
