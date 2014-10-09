
from .base import *

DEBUG = TEMPLATE_DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pyowa_talk',
        'USER': 'test',
        'PASSWORD': 'test',
    }
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

EMAIL_BACKEND = 'appengine_utils.mail.EmailBackend'
