import factory

from factory.django import DjangoModelFactory, FileField

from .models import University


class UniversityFactory(DjangoModelFactory):
    class Meta:
        model = University

    name = f"{factory.Faker('name').generate({})} University"
    city = factory.Faker("city")
    emblem = FileField(filename=factory.Faker("file_name", category="image"))
    # slug = models.SlugField(null=False)
