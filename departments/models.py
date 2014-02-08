from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super(Department, self).save(*args, **kwargs)
