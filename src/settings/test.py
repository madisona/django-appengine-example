
from .dev import *

TEST_RUNNER = "appengine_utils.test_utils.AppEngineTestRunner"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.test_db',
    }
}
