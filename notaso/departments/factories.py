import random

from factory.django import DjangoModelFactory

from .models import Department


class DepartmentFactory(DjangoModelFactory):
    class Meta:
        model = Department

    name = random.choice(
        (
            "Matemática",
            "Ciencias de Cómputos",
            "Ciencias Sociales",
            "Ingeniería Civil",
            "Biología",
            "Literatura" "Química",
        )
    )
