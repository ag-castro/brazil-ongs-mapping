from .base import *
import dj_database_url


ALLOWED_HOSTS = ['*']
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
BASE_URL = env('BASE_URL')
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
