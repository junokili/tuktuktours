from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_name_is_required(self):
        form = CommentForm({'writer': 'Test Writer not required'})
        self.assertTrue(form.is_valid)

    def test_comment_is_not_required(self):
        form = CommentForm({'comment': 'Test Comment not required'})
        self.assertTrue(form.is_valid)
