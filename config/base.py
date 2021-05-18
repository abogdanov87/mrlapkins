"""
Django settings for safety_work project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

AUTH_USER_MODEL = 'common.User'

RELATIVE_PATH = ''

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, RELATIVE_PATH, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!yj$dlst)mr15$xwz2&g2$grkgiyovp5dfpwc(wqp0u9o(o-lc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apps
    'corsheaders',
    'django_filters',
    'djoser',
    'rest_framework',
    'webpack_loader',
    'easy_thumbnails',
    'transliterate',
    'simple_history',
    'djrichtextfield',

    # project apps
    'catalogs',
    'common',
    'feedbacks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, RELATIVE_PATH, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
        # 'catalogs.api.v1.permissions.CatalogPermission',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'],
}

DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.ckeditor.com/4.14.0/standard/ckeditor.js'],
    'init_template': 'djrichtextfield/init/ckeditor.js',
    'settings': {
        'toolbar': [
            {'items': ['Format', '-', 'Bold', 'Italic', '-',
                    'RemoveFormat']},
            {'items': ['Link', 'Unlink', 'Image', 'Table']},
            {'items': ['Source']},
            {'items': ['BulletedList', 'NumberedList']}
        ],
        'format_tags': 'p;h1;h2;h3',
        'width': 700
    }
}

BASE_URL = 'http://localhost:8000'
LOGIN_FORM_URL = BASE_URL + '/admin/json/api-auth/login/'
HOME_FORM_URL = BASE_URL + '/#/catalogs/'

LOGOUT_REDIRECT_URL = LOGIN_FORM_URL
LOGIN_REDIRECT_URL = LOGIN_FORM_URL
LOGIN_URL = LOGIN_FORM_URL

STATIC_ROOT = os.path.join(BASE_DIR, RELATIVE_PATH, 'static/')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, RELATIVE_PATH, 'ui/build/'),
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '/',
        'STATS_FILE': os.path.join(BASE_DIR, RELATIVE_PATH, 'ui/webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    },
}

MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'files/')
MEDIA_URL = '/files/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Host for sending e-mail.
EMAIL_HOST = 'mail.4paws.io'

# Port for sending e-mail.
EMAIL_PORT = 465

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = 'support@4paws.io'
EMAIL_HOST_PASSWORD = 'mN1iF1lV6adP8x'
EMAIL_USE_TLS = False
