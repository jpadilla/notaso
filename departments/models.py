from django.db import models

# Create your models here.
class Department(models.Model):
	department_name = models.CharField(max_length=50, unique = True)

	def __unicode__(self):
		return self.department_name 