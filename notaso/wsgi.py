import os

from configurations.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

ENVIRONMENT = os.getenv("ENVIRONMENT", "DEVELOPMENT").title()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notaso.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", ENVIRONMENT)


application = get_wsgi_application()
application = DjangoWhiteNoise(application)
