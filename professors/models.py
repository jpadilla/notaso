from django.db import models
from django.conf import settings

from autoslug import AutoSlugField


def populate_professor_slug(instance):
    return instance.get_full_name()


class Professor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=75)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    university = models.ForeignKey('universities.University')
    department = models.ForeignKey('departments.Department')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    slug = AutoSlugField(populate_from=populate_professor_slug, unique=True)

    score = models.FloatField(editable=False)
    responsability = models.FloatField(editable=False)
    personality = models.FloatField(editable=False)
    workload = models.FloatField(editable=False)
    difficulty = models.FloatField(editable=False)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name

    def get_percent(self):
        return self.score*100

    def get_grade(instance):
        if instance.get_percent() >= 90:
            return 'A'
        elif instance.get_percent() >= 80:
            return 'B'
        elif instance.get_percent() >= 70:
            return 'C'
        elif instance.get_percent() >= 60:
            return 'D'
        else:
            return 'F'

    def get_responsability(self):
        responsability_percent = self.responsability*100
        if responsability_percent >= 90:
            return 'A'
        elif responsability_percent >= 80:
            return 'B'
        elif responsability_percent >= 70:
            return 'C'
        elif responsability_percent >= 60:
            return 'D'
        else:
            return 'F'

    def get_personality(self):
        personality_percent = self.responsability*100
        if personality_percent >= 90:
            return 'A'
        elif personality_percent >= 80:
            return 'B'
        elif personality_percent >= 70:
            return 'C'
        elif personality_percent >= 60:
            return 'D'
        else:
            return 'F'

    def get_workload(self):
        workload_percent = self.workload*100
        if workload_percent >= 90:
            return 1
        elif workload_percent >= 80:
            return 2
        elif workload_percent >= 70:
            return 3
        elif workload_percent >= 60:
            return 4
        else:
            return 5

    def get_dificulty(self):
        dificulty_percent = self.dificulty*100
        if dificulty_percent >= 90:
            return 1
        elif dificulty_percent >= 80:
            return 2
        elif dificulty_percent >= 70:
            return 3
        elif dificulty_percent >= 60:
            return 4
        else:
            return 5
