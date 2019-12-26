from django.test import TestCase

from notaso.professors.factories import ProfessorFactory
from notaso.universities.factories import UniversityFactory

from ..factories import DepartmentFactory
from ..models import Department


class TestDepartmentModel(TestCase):
    def setUp(self):
        self.department = DepartmentFactory()

    def test_can_create_department(self):
        self.assertIsInstance(self.department, Department)

    def test_produces_correct_count(self):
        university = UniversityFactory()

        self.assertEquals(self.department.count(university=university), 0)

        ProfessorFactory(university=university, department=self.department)
        self.assertEquals(self.department.count(university=university), 1)

        ProfessorFactory(university=university, department=self.department)
        self.assertEquals(self.department.count(university=university), 2)

    def test_get_department_grade(self):
        university = UniversityFactory()

        ProfessorFactory(score=0.95, university=university, department=self.department)
        self.assertEquals(self.department.get_grade(university=university), "A")

        ProfessorFactory(score=0.85, university=university, department=self.department)
        self.assertEquals(self.department.get_grade(university=university), "A")

        ProfessorFactory(score=0.70, university=university, department=self.department)
        self.assertEquals(self.department.get_grade(university=university), "B")

        ProfessorFactory(score=0.30, university=university, department=self.department)
        self.assertEquals(self.department.get_grade(university=university), "C")

        ProfessorFactory(score=0.00, university=university, department=self.department)
        self.assertEquals(self.department.get_grade(university=university), "F")
