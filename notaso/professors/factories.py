import random

import factory
from factory.django import DjangoModelFactory

from notaso.departments.factories import DepartmentFactory
from notaso.universities.factories import UniversityFactory
from notaso.users.factories import UserFactory

from .models import Professor


class ProfessorFactory(DjangoModelFactory):
    class Meta:
        model = Professor

    first_name = factory.Faker("first_name", locale="es_MX")
    last_name = factory.Faker("last_name", locale="es_MX")
    gender = random.choice(("M", "F"))

    university = factory.SubFactory(UniversityFactory)
    department = factory.SubFactory(DepartmentFactory)
    created_by = factory.SubFactory(UserFactory)
    # slug = AutoSlugField(populate_from=populate_professor_slug, unique=True)

    score = random.random()
    responsibility = random.random()
    personality = random.random()
    workload = random.random()
    difficulty = random.random()
