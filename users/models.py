from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	email = models.EmailField(max_length=40)
	gender = models.CharField(max_length=1)
	facebook_user_id = models.CharField(max_length=30, null=True)

	def __unicode__(self):
		return self.user.username