from django.test import TestCase

from ..factories import CommentFactory
from ..models import Comment


class TestCommentModel(TestCase):
    def test_can_create_comment(self):
        comment = CommentFactory()
        self.assertIsInstance(comment, Comment)

    def test_comment_body_is_correct(self):
        msg = "El mejor profesor que hay,no duden en tomar su curso"
        comment = CommentFactory(body=msg)

        self.assertEquals(comment.body, msg)
        self.assertEquals(str(comment), msg)

    def test_comment_score(self):
        comment = CommentFactory(
            responsibility=5, personality=5, workload=5, difficulty=5
        )
        self.assertEquals(comment.score, 100.0)

        comment = CommentFactory(
            responsibility=1, personality=1, workload=1, difficulty=1
        )
        self.assertEquals(comment.score, 20.0)

    def test_can_edit_comment(self):
        comment = CommentFactory(
            responsibility=5, personality=5, workload=5, difficulty=5
        )
        comment.responsibility = 1
        comment.personality = 1
        comment.workload = 1
        comment.difficulty = 1
        comment.save()
        self.assertEquals(comment.score, 20.0)
