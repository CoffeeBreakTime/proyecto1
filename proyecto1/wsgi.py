
import os
import sys

path = os.path.expanduser('/home/Mamiko/proyecto1/proyecto1')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'proyecto1.settings'
from django.core.wsgi import get_wsgi_application # type: ignore
from django.contrib.staticfiles.handlers import StaticFilesHandler # type: ignore
application = StaticFilesHandler(get_wsgi_application())

"""
WSGI config for proyecto1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto1.settings')

application = get_wsgi_application()

