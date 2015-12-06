"""
WSGI config for notaso project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import dotenv


try:
    dotenv.read_dotenv(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
except Exception as e:
    print(e)


ENVIRONMENT = os.getenv('ENVIRONMENT', 'DEVELOPMENT').title()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notaso.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', ENVIRONMENT)

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
