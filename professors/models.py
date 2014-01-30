from django.db import models
from django import forms
from django.conf import settings


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

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
