from django.db import models

from autoslug import AutoSlugField

from professors.models import Professor

class Department(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name

    def get_grade(instance, university):
    	professors = Professor.objects.filter(university=university, department=instance)
        
        count = 0
        percent = 0;
        for p in professors:
            percent += p.get_percent()
            count += 1

        percent = percent/count

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
