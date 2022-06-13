from .base import *

DEBUG = False

CORS_ALLOWED_ORIGINS = [
    "http://webecolog.ru",
    "http://www.webecolog.ru",
    "https://webecolog.ru",
    "https://www.webecolog.ru",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

ALLOWED_HOSTS = ['.webecolog.ru'] 
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
#SECURE_SSL_REDIRECT = True
#SECURE_HSTS_SECONDS = 60
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_PRELOAD = True

try:
    from .local import *
except ImportError:
    pass
