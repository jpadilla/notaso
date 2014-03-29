from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return self.username

User._meta.get_field_by_name('username')[0]._unique = False
User._meta.get_field_by_name('username')[0]._blank = True
User._meta.get_field_by_name('email')[0]._blank = False
User._meta.get_field_by_name('email')[0]._unique = True
