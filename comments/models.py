from django.db import models
from django.conf import settings

from professors.models import Professor


class Comment(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    professor = models.ForeignKey(Professor)

    body = models.TextField()
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    is_anonymous = models.BooleanField()

    responsibility = models.IntegerField(null=True)
    personality = models.IntegerField(null=True)
    workload = models.IntegerField(null=True)
    difficulty = models.IntegerField(null=True)

    def __unicode__(self):
        return self.body
