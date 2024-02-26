import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY_INSECURE = 'django-insecure-16dazm@-1k@jc(q-raqc#x8+zveqa@6lp-d#_22=@d1-gg=cf4-'
SECRET_KEY = os.environ.get("SECRET_KEY", default=SECRET_KEY_INSECURE)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=1))

# Set access rights
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="127.0.0.1").split(",")

# Database scheme setup
DATABASES = {
    'default': {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", None),
        "PASSWORD": os.environ.get("SQL_PASSWORD", None),
        "HOST": os.environ.get("SQL_HOST", None),
        "PORT": os.environ.get("SQL_PORT", None),
    }
}

# Debug/Production dependent settings
if DEBUG:
    STATICFILES_DIRS = [
        # add static dirs for all apps here
    ]
else:
    # HTTPS settings
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    # HSTS settings
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # PROXY settings
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # Set static files path
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd-party
    'django_celery_results',
    "django_celery_beat",    
    'celery_progress',
    'rest_framework',
    'widget_tweaks',
    'sweetify',
    'rosetta',
    'corsheaders',    
    # My apps
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cyberion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')),],
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

WSGI_APPLICATION = 'cyberion.wsgi.application'

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = os.environ.get('TIME_ZONE','UTC')
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
MEDIA_URL = 'media/'
STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Other
SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'

# REST framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}    

# Rosetta (for translations)
ROSETTA_MESSAGES_PER_PAGE =  50
ROSETTA_SHOW_AT_ADMIN_PANEL = True
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
DEEPL_AUTH_KEY = os.environ.get('DEEPL_AUTH_KEY', None)

# Celery & Redis
CELERY_TIMEZONE = os.environ.get('TIME_ZONE','UTC')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'    
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "django-db")
# Scheduled tasks
"""
CELERY_BEAT_SCHEDULE = {
}
"""