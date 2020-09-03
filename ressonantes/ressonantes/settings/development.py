from datetime import timedelta
from .base import os
from .base import AUTHENTICATION_BACKENDS
from .base import AUTH_PASSWORD_VALIDATORS
from .base import AUTH_USER_MODEL
from .base import BASE_DIR
from .base import BASE_URL
from .base import CORS_ALLOWED_ORIGINS
# from .base import DEFAULT_FROM_EMAIL
from .base import env
from .base import INSTALLED_APPS
from .base import LANGUAGE_CODE
from .base import MEDIA_ROOT
from .base import MEDIA_URL
from .base import MIDDLEWARE
from .base import PASSWORD_HASHERS
from .base import PROJECT_DIR
from .base import REST_FRAMEWORK
from .base import ROOT_URLCONF
from .base import STATIC_ROOT
from .base import STATIC_URL
from .base import TEMPLATES
from .base import TIME_ZONE
from .base import USE_I18N
from .base import USE_L10N
from .base import USE_TZ
from .base import WSGI_APPLICATION
import dj_database_url


WSGI_APPLICATION = 'ressonantes.wsgi.application'

# SECURITY WARNING: keep the secret key used in production secret!


SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']
DATABASES = {'default': {}}


DATABASES['default'] = dj_database_url.config(
    default=env('DATABASE_URL'),
    engine='django.db.backends.postgresql'
)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': os.environ.get('DB_HOST'),
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#     }
# }

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ['127.0.0.1', 'localhost']

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
    'debug_toolbar.panels.profiling.ProfilingPanel',
]
