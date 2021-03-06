import dj_database_url

from .base import *


BASE_NAME = BASE_DOMAIN = "localhost"
BASE_URL = f"http://{BASE_DOMAIN}:8000"

###############################################################################
# Core

DEBUG = True
SECRET_KEY = "dev"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", ".ngrok.io"]

INSTALLED_APPS += ["livereload"]

MIDDLEWARE += ["livereload.middleware.LiveReloadScript"]

###############################################################################
# Databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "elections_dev",
        "HOST": "127.0.0.1",
    },
    "remote": dj_database_url.config(),
}
