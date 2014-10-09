
#https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

from .base import *

DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    ".appspot.com"
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '/cloudsql/<database-string>',  # this will come from Google Cloud Console
        'NAME': '<db_name>',
        'STORAGE_ENGINE': 'INNODB',
        'USER': 'root',
    },
}


TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

EMAIL_BACKEND = 'appengine_utils.mail.AsyncEmailBackend'
# Specify a queue name for the async. email backend.
EMAIL_QUEUE_NAME = 'default'
