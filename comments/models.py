from django.db import models
from django.conf import settings

from professors.models import Professor


class Comments(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    professor = models.ForeignKey(Professor)

    body = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    is_anonimo = models.BooleanField()

    responsibility = models.IntegerField()
    personality = models.IntegerField()
    workload = models.IntegerField()
    dificulty = models.IntegerField()

    def __unicode__(self):
        return self.id
