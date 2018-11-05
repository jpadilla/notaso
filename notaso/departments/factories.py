import random

from factory.django import DjangoModelFactory

from .models import Department


class DepartmentFactory(DjangoModelFactory):
    class Meta:
        model = Department

    name = random.choice(
        (
            "Mathematics",
            "Computer Science",
            "Social Science",
            "Civil Engineering",
            "Biology",
        )
    )
