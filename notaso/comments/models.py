from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404

from ..professors.models import Professor


class Comment(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    body = models.TextField()
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    is_anonymous = models.BooleanField()

    responsibility = models.IntegerField(null=True)
    personality = models.IntegerField(null=True)
    workload = models.IntegerField(null=True)
    difficulty = models.IntegerField(null=True)

    def __str__(self):
        return self.body

    @property
    def score(self):
        return (
            float(
                self.responsibility + self.personality + self.workload + self.difficulty
            )
            * 5
        )


def recalculate_score(sender, **kwargs):
    c = kwargs["instance"]

    if c.responsibility and c.personality and c.workload and c.difficulty:
        comments = Comment.objects.filter(
            professor=c.professor.id,
            responsibility__isnull=False,
            personality__isnull=False,
            workload__isnull=False,
            difficulty__isnull=False,
        ).exclude(responsibility=0, personality=0, workload=0, difficulty=0)

        comments_count = 0
        sum_responsibility = 0
        sum_personality = 0
        sum_workload = 0
        sum_difficulty = 0

        for c in comments:
            sum_responsibility += c.responsibility
            sum_personality += c.personality
            sum_workload += c.workload
            sum_difficulty += c.difficulty
            comments_count += 1

        score = float(
            (sum_responsibility + sum_personality + sum_workload + sum_difficulty)
        ) / (comments_count * 20)

        p = get_object_or_404(Professor, pk=c.professor.id)
        p.score = score
        p.responsibility = float(sum_responsibility) / (comments_count * 5)
        p.personality = float(sum_personality) / (comments_count * 5)
        p.workload = float(sum_workload) / (comments_count * 5)
        p.difficulty = float(sum_difficulty) / (comments_count * 5)

        p.save()


post_save.connect(recalculate_score, sender=Comment)
