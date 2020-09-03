import os
from datetime import timedelta
import dj_database_url
# import environ

# env = environ.Env()
# env.read_env(env.str('ENV_PATH', '.testenv'))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = ['*']
DATABASES = {'default': {}}


DATABASES['default'] = dj_database_url.config(
    default=os.environ.get('DATABASE_URL'),
    engine='django.db.backends.postgresql'
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'modelcluster',
    'rest_framework',
    'debug_toolbar',
    'mptt',
    'corsheaders',

    # APPLICATION
    'core',
    'user',
    'locales',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'ressonantes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ressonantes.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

UserAttributeSimilarityValidator = \
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
MinimumLengthValidator = \
    'django.contrib.auth.password_validation.MinimumLengthValidator'
CommonPasswordValidator = \
    'django.contrib.auth.password_validation.CommonPasswordValidator'
NumericPasswordValidator = \
    'django.contrib.auth.password_validation.NumericPasswordValidator'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': UserAttributeSimilarityValidator,
    },
    {
        'NAME': MinimumLengthValidator,
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': CommonPasswordValidator,
    },
    {
        'NAME': NumericPasswordValidator,
    },
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/vol/web/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/vol/web/media'

AUTH_USER_MODEL = 'core.User'

BASE_URL = 'http://localhost:8000/'


# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    BASE_URL,
]


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
}
