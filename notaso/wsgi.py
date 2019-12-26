import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "DEVELOPMENT").title()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notaso.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", ENVIRONMENT)

from configurations.wsgi import get_wsgi_application  # noqa isort:skip

application = get_wsgi_application()
