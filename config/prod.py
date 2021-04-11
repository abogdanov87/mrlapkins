from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '37.140.192.51',
    'mrlapkins.ru',
    'www.mrlapkins.ru',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u1344503_default',
        'USER': 'u1344503_default',
        'PASSWORD': 'N_7Q2iDd',
        'HOST': 'localhost',
    }
}

BASE_URL = 'http://www.mrlapkins.ru'
LOGIN_FORM_URL = BASE_URL + '/admin/json/api-auth/login/'
HOME_FORM_URL = BASE_URL + '/#/catalogs/'

LOGOUT_REDIRECT_URL = LOGIN_FORM_URL
LOGIN_REDIRECT_URL = LOGIN_FORM_URL
LOGIN_URL = LOGIN_FORM_URL