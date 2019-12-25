from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProfessorsConfig(AppConfig):
    name = "notaso.professors"
    verbose_name = _("professors")

    def ready(self):
        import notaso.professors.signals  # noqa isort:skip
