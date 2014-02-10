from django.db import models


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
