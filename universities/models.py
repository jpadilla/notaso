from django.db import models

# Create your models here.
def get_upload_file_name(intance, filename):
	return "uploaded_files/%s" % (filename)

class Universities(models.Model):
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=25)
	emblem = models.FileField(upload_to = get_upload_file_name)
	departments = models.ManyToManyField('departments.Departments')

	def __unicode__(self):
		return u'%s %s' % (self.name, self.city)
