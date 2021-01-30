from django.test import TestCase
from .forms import CommentForm, BlogPostForm


class TestCommentForm(TestCase):

    def test_name_is_required(self):
        form = CommentForm({'writer': 'Test Writer not required'})
        self.assertTrue(form.is_valid)

    def test_comment_is_not_required(self):
        form = CommentForm({'comment': 'Test Comment not required'})
        self.assertTrue(form.is_valid)


class TestBlogPostForm(TestCase):
    def test_title_is_required(self):
        form = BlogPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_content_is_required(self):
        form = BlogPostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_author_is_required(self):
        form = BlogPostForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')

    def test_tour_is_not_required(self):
        form = BlogPostForm({'tour': 'My Post'})
        self.assertTrue(form.is_valid)

    def test_image_url_is_not_required(self):
        form = BlogPostForm({'image_url': 'My Post'})
        self.assertTrue(form.is_valid)

    def test_image_is_not_required(self):
        form = BlogPostForm({'image': 'My Pst'})
        self.assertTrue(form.is_valid)
