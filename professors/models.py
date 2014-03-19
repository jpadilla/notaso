from django.db import models
from django.conf import settings

from autoslug import AutoSlugField


def populate_professor_slug(instance):
    return instance.get_full_name()


def evaluate_with_grade(percent):
    if percent >= 90:
        return 'A'
    elif percent >= 80:
        return 'B'
    elif percent >= 70:
        return 'C'
    elif percent >= 60:
        return 'D'
    else:
        return 'F'


def evaluate_with_number(percent):
    if percent >= 90:
        return 1
    elif percent >= 80:
        return 2
    elif percent >= 70:
        return 3
    elif percent >= 60:
        return 4
    else:
        return 5


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

    score = models.FloatField(editable=False, default=0)
    responsibility = models.FloatField(editable=False, default=0)
    personality = models.FloatField(editable=False, default=0)
    workload = models.FloatField(editable=False, default=0)
    difficulty = models.FloatField(editable=False, default=0)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name

    def save(self, *args, **kwargs):
        super(Professor, self).save(*args, **kwargs)

    def get_percent(self):
        return self.score*100

    def get_grade(instance):
        return evaluate_with_grade(instance.get_percent)

    def get_responsibility(self):
        return evaluate_with_grade(self.responsibility*100)

    def get_personality(self):
        return evaluate_with_grade(self.personality*100)

    def get_workload(self):
        return evaluate_with_number(self.workload*100)

    def get_difficulty(self):
        return evaluate_with_number(self.difficulty*100)
