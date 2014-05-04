from import_export import resources
from .models import User


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        exclude = ('password', 'imported',)
