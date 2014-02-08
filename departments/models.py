from django.db import models
from autoslug import AutoSlugField


class Department(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name
