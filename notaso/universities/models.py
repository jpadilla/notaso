from django.db import models

from ..professors.models import Professor


def get_upload_file_name(instance, filename):
    return "static/uploaded_files/%s" % (filename)


class University(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    emblem = models.FileField(upload_to=get_upload_file_name)
    slug = models.SlugField(null=False)

    def __str__(self):
        return f"{self.name} {self.city}"

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super(University, self).save(*args, **kwargs)

    def count(instance):
        return Professor.objects.filter(university=instance).count()

    def get_grade(instance):
        professors = Professor.objects.filter(university=instance)
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
