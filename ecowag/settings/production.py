from .base import *

DEBUG = True

CORS_ALLOWED_ORIGINS = [
    "http://webecolog.ru",
    "http://www.webecolog.ru",
    "https://webecolog.ru",
    "https://www.webecolog.ru",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

ALLOWED_HOSTS = ['.api.webecolog.ru'] 
CSRF_TRUSTED_ORIGINS = ['https://*.webecolog.ru'] 
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

try:
    from .local import *
except ImportError:
    pass
