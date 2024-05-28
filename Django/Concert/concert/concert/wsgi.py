"""
WSGI config for concert project.

It sets up the WSGI application callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application

# Load Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concert.settings')
django.setup()

# Get the WSGI application
application = get_wsgi_application()

