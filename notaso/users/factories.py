import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Faker("email", locale="es_MX")
    first_name = factory.Faker("first_name", locale="es_MX")
    last_name = factory.Faker("last_name", locale="es_MX")
    is_admin = factory.Faker("boolean", chance_of_getting_true=50)
    is_active = factory.Faker("boolean", chance_of_getting_true=85)
