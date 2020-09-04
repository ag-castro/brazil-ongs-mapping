from .base import *
import dj_database_url


SECRET_KEY = '^@%h28h9wit$ous5j^3%rq-4j%*!t^#2-d4pbvzkdxkz%edg64'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {'default': {}}


DATABASES['default'] = dj_database_url.config(
    default='psql://postgres:K8YvzabSrzeGUAecJ8hQkfuXZEjU9ZcY@ressonantes_db/db_ressonantes_app',
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
