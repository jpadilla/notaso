import factory

from factory.django import DjangoModelFactory, ImageField

from .models import University


class UniversityFactory(DjangoModelFactory):
    class Meta:
        model = University

    name = f"{factory.Faker('full_name')} University"
    city = factory.Faker("city")
    emblem = ImageField()
    # slug = models.SlugField(null=False)
