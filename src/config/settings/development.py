from .base_settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-edg!$#qlqr7-=p!x)#7quqk9=)t&kuool-2ca=eh+!i^c$-52c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
