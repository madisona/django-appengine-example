
from .dev import *

TEST_RUNNER = "django.test.runner.DiscoverRunner"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.test_db',
    }
}
