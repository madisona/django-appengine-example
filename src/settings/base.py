"""
Django settings for pyowa_talk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import fix_path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os import pardir
from os.path import abspath, dirname, join
BASE_DIR = abspath(join(dirname(__file__), pardir))


SECRET_KEY = 'bg8ko%lqx#ijy%$(tc^$vnu=erf1hr0oiw4#ap!c8tddb^9#48'

SERVER_EMAIL = 'test@example.com'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

# Application definition

PROJECT_APPS = (
    'polls',
    'users',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
) + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'




# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = True


# Template Directory
TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = join(BASE_DIR, 'production_static')
STATIC_URL = '/static/'


# defining custom user model
AUTH_USER_MODEL = 'users.User'
