"""
WSGI config for pyowa_talk project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

# we're wanting to use django 1.7 and it is not included with App Engine yet.
# Need to remove old version & reload stuff
for key in [key for key in sys.modules if key.startswith('django')]:
  del sys.modules[key]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")


# Force Django to reload its settings.
from django.conf import settings
settings._target = None


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
