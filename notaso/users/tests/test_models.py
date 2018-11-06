from django.test import TestCase
from django.contrib.auth import get_user_model

from ..factories import UserFactory


class TestProfessorModel(TestCase):
    class Meta:
        model = get_user_model()

    def test_can_create_user(self):
        user = UserFactory()
        self.assertIsInstance(user, get_user_model())

    def test_get_user_name(self):
        user = UserFactory(first_name="Test", last_name="McTester")
        self.assertEquals(user.get_full_name(), "Test McTester")
        self.assertEquals(user.get_short_name(), "Test")

    def test_get_user_email(self):
        user = UserFactory(email="test@notaso.com")
        self.assertEquals(user.email, "test@notaso.com")
        self.assertEquals(str(user), "test@notaso.com")
