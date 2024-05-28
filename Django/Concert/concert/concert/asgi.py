"""
ASGI config for concert project.

It sets up the ASGI application callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django

from django.core.asgi import get_asgi_application

# Load Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concert.settings')
django.setup()

# Get the ASGI application
application = get_asgi_application()

