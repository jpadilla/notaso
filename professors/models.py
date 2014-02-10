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
    university =  models.ForeignKey('universities.Universities')
    department = models.ForeignKey('departments.Department')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    slug = AutoSlugField(populate_from=populate_professor_slug, unique=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name
