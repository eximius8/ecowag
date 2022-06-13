DJANGO_ALLOW_AYNSC_UNSAFE = True
DJANGO_ALLOW_ASYNC_UNSAFE = True
import os
from dotenv import load_dotenv
from .base import *

load_dotenv(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CORS_ALLOW_ALL_ORIGINS = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS += ['django_extensions']

