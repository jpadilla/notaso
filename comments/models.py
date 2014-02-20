from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404


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

def recalculate_score(sender, **kwargs):
    c = kwargs['instance']
    comments = Comment.objects.filter(professor=c.professor.id).count()

    sum_responsibility = Comment.objects.filter(professor=c.professor.id).aggregate(Sum('responsibility'))['responsibility__sum']
    sum_personality = Comment.objects.filter(professor=c.professor.id).aggregate(Sum('personality'))['personality__sum']
    sum_workload = Comment.objects.filter(professor=c.professor.id).aggregate(Sum('workload'))['workload__sum']
    sum_difficulty = Comment.objects.filter(professor=c.professor.id).aggregate(Sum('difficulty'))['difficulty__sum']

    score = float((sum_responsibility+sum_personality+sum_workload+sum_difficulty))/(comments*20)

    p = get_object_or_404(Professor, pk=c.professor.id)
    p.score = score
    p.responsibility = float(sum_responsibility)/(comments*5)
    p.personality = float(sum_personality)/(comments*5)
    p.workload = float(sum_workload)/(comments*5)
    p.difficulty = float(sum_difficulty)/(comments*5)
    p.save()

post_save.connect(recalculate_score, sender=Comment)
