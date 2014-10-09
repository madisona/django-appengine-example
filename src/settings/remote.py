# Use these settings when you want to access production information, but locally.

from .production import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '<ip_address>',
        'NAME': '<db_name>',
        'USER': '<user_name>',
        'PASSWORD': '<pswd>',
    }
}
