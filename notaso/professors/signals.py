from django.contrib.postgres.search import SearchVector
from django.db import models
from django.dispatch import receiver

from .models import Professor


@receiver(models.signals.post_save, sender=Professor)
def update_search_index(sender, instance, **kwargs):
    """
    Runs after a Professor instance has been created or updated.
    Updates the instance's search_index field.
    """

    config = kwargs.get("config", "pg_catalog.spanish")
    search_index = SearchVector("first_name", "last_name", config=config)
    Professor.objects.filter(pk=instance.pk).update(search_index=search_index)
