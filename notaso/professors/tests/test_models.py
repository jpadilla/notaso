from django.test import TestCase

from ..factories import ProfessorFactory
from ..models import Professor


class TestProfessorModel(TestCase):
    def test_can_create_professor(self):
        professor = ProfessorFactory()
        self.assertIsInstance(professor, Professor)

    def test_professor_full_name(self):
        professor = ProfessorFactory(first_name="Fulano", last_name="de Tal")
        self.assertEquals(professor.get_full_name(), "Fulano de Tal")
        self.assertEquals(str(professor), "Fulano de Tal")

    def test_get_professor_attribute_grades(self):
        professor = ProfessorFactory(
            responsibility=0.70, personality=0.85, workload=0.40, difficulty=1.0
        )
        self.assertEquals(professor.get_responsibility(), "C")
        self.assertEquals(professor.get_personality(), "B")
        self.assertEquals(professor.get_workload(), 1)
        self.assertEquals(professor.get_difficulty(), 5)
