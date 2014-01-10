from django.db import models

# Create your models here.
class Departments(models.Model):
	department_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.department_name 