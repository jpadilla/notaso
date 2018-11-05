from autoslug import AutoSlugField
from django.db import models

from ..professors.models import Professor


class Department(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self):
        return self.name

    def count(self, university):
        return Professor.objects.filter(
            department=self.id, university=university
        ).count()

    def get_grade(instance, university):
        professors = Professor.objects.filter(
            university=university, department=instance
        )
        count = 0
        percent = 0
        for p in professors:
            percent += p.get_percent()
            count += 1

        if count == 0:
            percent = 0
        else:
            percent = percent / count

        if percent >= 90:
            return "A"
        elif percent >= 80:
            return "B"
        elif percent >= 70:
            return "C"
        elif percent >= 60:
            return "D"
        else:
            return "F"
