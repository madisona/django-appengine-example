
#https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

from .base import *

DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
