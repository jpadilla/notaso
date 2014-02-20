from django.db import models

from professors.models import Professor

def get_upload_file_name(intance, filename):
    return "uploaded_files/%s" % (filename)


class University(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    emblem = models.FileField(upload_to=get_upload_file_name)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.city)

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super(University, self).save(*args, **kwargs)

    def get_grade(instance):
        count = Professor.objects.filter(university=instance).count()
        professors = Professor.objects.filter(university=instance)
        
        percent = 0;
        for p in professors:
            percent += p.get_percent()

        percent = percent/count

        print percent

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