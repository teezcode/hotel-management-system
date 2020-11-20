from .base import *
import debug_toolbar

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS +=[
    'debug_toolbar',
]

MIDDLEWARE +=['debug_toolbar.middleware.DebugToolbarMiddleware',]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}