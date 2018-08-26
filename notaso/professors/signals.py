from django.db import connections, models, transaction
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector

from .models import Professor


@receiver(models.signals.post_save, sender=Professor)
def update_search_index(sender, instance, **kwargs):
    """
    
    """

    config = kwargs.get("config", "pg_catalog.spanish")
    search_index = SearchVector("first_name", "last_name", config=config)
    Professor.objects.filter(pk=instance.pk).update(search_index=search_index)
