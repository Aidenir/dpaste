from dpaste.settings.base import *

DEBUG = True

ADMINS = (
    #('Your Name', 'name@example.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/dpaste.sqlite'
    }
}

ALLOWED_HOSTS = (
        '127.0.0.1',
        'localhost',
        'paste.viha.se',
)


SECRET_KEY = 'sdfasfaslkfjalksfj'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
