"""
Django settings for {{ project_name }} project.
For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

# Use 12factor inspired environment variables or from a file
import environ

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = environ.Path(__file__) - 3
LOG_FILE = BASE_DIR.path('logs')
print('BASE_DIR = ' + str(BASE_DIR))

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    RECAPTCHA_PUBLIC_KEY=(str, 'Changeme'),
    RECAPTCHA_PRIVATE_KEY=(str, 'Changeme'),
    PRODUCTION=(bool, False),
    DOMAIN_NAME=(str, 'mydomain.com'),
    COMPANY_NAME=(str, 'COMPANY_NAME'),
)

ADMINS = (
    # ('Username', 'your_email@domain.com'),
    ('admin', 'admin@mydomain.com'),
)

SITE_ID = 1

# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = os.path.join(os.path.dirname(__file__), '.local.env')
if os.path.exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []

PRODUCTION = env('PRODUCTION')
DOMAIN_NAME = env('DOMAIN_NAME')
COMPANY_NAME = env('COMPANY_NAME')

# Application definition

DJANGO_APPS = (
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
    'storages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'corsheaders',
    'captcha',
    'crispy_forms',
)

# Apps specific for this project go here.
COMMON_APPS = (
    'apps.authentication',
)

INSTALLED_APPS = DJANGO_APPS + COMMON_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': env.db(),
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

ROOT_DIR = environ.Path(__file__) - 4
STATIC_ROOT = str(ROOT_DIR.path('staticfiles'))
STATICFILES_DIRS = []

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authentication.Account'
#LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
#LOGIN_URL = reverse_lazy("accounts:login")

# Recaptcha https://www.google.com/recaptcha/admin
# https://github.com/praekelt/django-recaptcha
RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY')
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True

# https://github.com/ottoyiu/django-cors-headers/
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api.*$'
CORS_ORIGIN_WHITELIST = (
    'mydomain.com',
    'xxxxxxxxxx.cloudfront.net',
)

CSRF_COOKIE_HTTPONLY = False # Most be False for javascript APIs to be able to post/put/delete
SESSION_COOKIE_HTTPONLY = True

# http://www.django-rest-framework.org/
REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    #'DEFAULT_PAGINATION_CLASS': 'apps.utils.pagination.StandardResultsSetPagination'
}
