from django.test import TestCase

from notaso.professors.factories import ProfessorFactory

from ..factories import UniversityFactory
from ..models import University


class TestUniversityModel(TestCase):
    def test_can_create_university(self):
        university = UniversityFactory()
        self.assertIsInstance(university, University)

    def test_get_university_name(self):
        university = UniversityFactory(name="Notaso", city="San Juan")
        self.assertEquals(university.name, "Notaso")
        self.assertEquals(str(university), "Notaso San Juan")

    def test_produces_correct_count(self):
        university = UniversityFactory()
        self.assertEquals(university.count(), 0)

        ProfessorFactory(university=university)
        self.assertEquals(university.count(), 1)

        bad_professor = ProfessorFactory(university=university)
        self.assertEquals(university.count(), 2)

        bad_professor.delete()
        self.assertEquals(university.count(), 1)

    def test_get_university_grade(self):
        university = UniversityFactory()

        ProfessorFactory(score=0.95, university=university)
        self.assertEquals(university.get_grade(), "A")

        ProfessorFactory(score=0.85, university=university)
        self.assertEquals(university.get_grade(), "A")

        ProfessorFactory(score=0.70, university=university)
        self.assertEquals(university.get_grade(), "B")

        ProfessorFactory(score=0.30, university=university)
        self.assertEquals(university.get_grade(), "C")

        ProfessorFactory(score=0.00, university=university)
        self.assertEquals(university.get_grade(), "F")
