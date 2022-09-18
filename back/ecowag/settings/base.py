import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = os.getenv('SECRET_KEY')

INSTALLED_APPS = [
    'home',
    'search',

    'litsource',
    'streams',
    'substance',
    'ecouser',
    'blog',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',
    'wagtail_headless_preview',

    'wagtail.api.v2',
    'rest_framework',
    'corsheaders',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',


    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'ecowag.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'ecowag.wsgi.application'


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('SERVICE_DB_NAME', ''),
        'USER': os.environ.get('SERVICE_DB_USER', ''),
        'PASSWORD': os.environ.get('SERVICE_DB_PASS', ''),
        'HOST': os.environ.get('SERVICE_DB_HOST', '10.100.8.35'),
        'PORT': os.environ.get('SERVICE_DB_PORT', '5432'),
        'OPTIONS': {
            'options': f'-c search_path={os.environ.get("SERVICE_SCHEME_NAME", "public")}'
        }
    }
}

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

WAGTAIL_HEADLESS_PREVIEW = {
    "CLIENT_URLS": {
        "default": os.getenv('FRONT_URL'),
    },  # defaults to an empty dict. You must at the very least define the default client URL.
    "LIVE_PREVIEW": True,  # set to True to enable live preview functionality
    "SERVE_BASE_URL": os.getenv('FRONT_URL'),
    "REDIRECT_ON_PREVIEW": False,  # set to True to redirect to the preview instead of using the Wagtail default mechanism
}

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

WAGTAIL_ALLOW_UNICODE_SLUGS = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')# '/opt/static/'  #os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media') #os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

REPORTS_ROOT = f'{MEDIA_ROOT}/reports/'
if not os.path.exists(REPORTS_ROOT):
    os.makedirs(REPORTS_ROOT)


# Wagtail settings
WAGTAIL_SITE_NAME = "ecowag"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash

WAGTAILADMIN_BASE_URL = os.getenv('API_URL', 'localhost:8000')
WAGTAILAPI_BASE_URL = os.getenv('API_URL', 'localhost:8000')

AUTH_USER_MODEL = 'ecouser.EcoUser'

WAGTAILAPI_LIMIT_MAX = 20
WAGTAIL_PASSWORD_MANAGEMENT_ENABLED = True
WAGTAIL_PASSWORD_RESET_ENABLED = True
WAGTAIL_EMAIL_MANAGEMENT_ENABLED = False

# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
EMAIL_USE_SSL = True
WAGTAILADMIN_NOTIFICATION_USE_HTML = True
