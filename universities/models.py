from django.db import models
from time import time

# Create your models here.
def get_upload_file_name(intance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Universities(models.Model):
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=25)
	emblem = models.FileField(upload_to = get_upload_file_name)
	departments = models.ManyToManyField('departments.Departments')

	def __unicode__(self):
		return self.name
