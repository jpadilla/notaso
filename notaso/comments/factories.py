import random

import factory
from factory.django import DjangoModelFactory

from notaso.professors.factories import ProfessorFactory
from notaso.users.factories import UserFactory

from .models import Comment


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    created_by = factory.SubFactory(UserFactory)
    professor = factory.SubFactory(ProfessorFactory)

    body = factory.Faker(
        "paragraph", nb_sentences=4, variable_nb_sentences=True, ext_word_list=None
    )
    created_at = factory.Faker("date_between", start_date="-4y", end_date="today")
    is_anonymous = factory.Faker("boolean", chance_of_getting_true=75)

    responsibility = random.randint(1, 5)
    personality = random.randint(1, 5)
    workload = random.randint(1, 5)
    difficulty = random.randint(1, 5)
