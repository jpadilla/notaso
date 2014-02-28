from django.db import models
from django.conf import settings

from autoslug import AutoSlugField


def populate_professor_slug(instance):
    return instance.get_full_name()


class Professor(models.Model):
    MALE = 'm'
    FEMALE = 'f'
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
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        self.first_name = full_name.split(' ')[0]
        self.last_name = full_name.split(' ')[1]
        return full_name

    def save(self, *args, **kwargs):
        super(Professor, self).save(*args, **kwargs)

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

    def get_responsibility(self):
        responsibility_percent = self.responsibility*100
        if responsibility_percent >= 90:
            return 'A'
        elif responsibility_percent >= 80:
            return 'B'
        elif responsibility_percent >= 70:
            return 'C'
        elif responsibility_percent >= 60:
            return 'D'
        else:
            return 'F'

    def get_personality(self):
        personality_percent = self.personality*100
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

    def get_difficulty(self):
        difficulty_percent = self.difficulty*100
        if difficulty_percent >= 90:
            return 1
        elif difficulty_percent >= 80:
            return 2
        elif difficulty_percent >= 70:
            return 3
        elif difficulty_percent >= 60:
            return 4
        else:
            return 5
