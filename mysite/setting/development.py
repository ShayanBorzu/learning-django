from mysite.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-a$=zjayutuob=a_@6i5dyy_4l&*ze@l=k0sc-+e%zun=xn-v7&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 2


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
