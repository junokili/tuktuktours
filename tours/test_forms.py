from django.test import TestCase
from .forms import TourDetailForm, CategoryForm, ReviewForm


class TestTourDetailForm(TestCase):
    def test_tour_name_is_required(self):
        form = TourDetailForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_sku_is_required(self):
        form = TourDetailForm({'sku': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('sku', form.errors.keys())
        self.assertEqual(form.errors['sku'][0], 'This field is required.')

    def test_description_is_required(self):
        form = TourDetailForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_includes_is_required(self):
        form = TourDetailForm({'includes': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('includes', form.errors.keys())
        self.assertEqual(form.errors['includes'][0], 'This field is required.')

    def test_price_is_required(self):
        form = TourDetailForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_duration_is_required(self):
        form = TourDetailForm({'duration': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('duration', form.errors.keys())
        self.assertEqual(form.errors['duration'][0], 'This field is required.')

    def test_category_is_not_required(self):
        form = TourDetailForm({'name': 'Tour Name'})
        self.assertTrue(form.is_valid)

    def test_start_time_is_not_required(self):
        form = TourDetailForm({'name': 'Tour Name'})
        self.assertTrue(form.is_valid)

    def test_image_url_is_not_required(self):
        form = TourDetailForm({'image_url': 'Tour Name'})
        self.assertTrue(form.is_valid)

    def test_image_is_not_required(self):
        form = TourDetailForm({'image': 'Tour Name'})
        self.assertTrue(form.is_valid)


class TestCategoryForm(TestCase):
    def test_category_name_is_required(self):
        form = CategoryForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_category_friendly_name_is_not_required(self):
        form = CategoryForm({'friendly_name': ''})
        self.assertTrue(form.is_valid)


class TestReviewForm(TestCase):
    def test_review_content_is_required(self):
        form = ReviewForm({'review_content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review_content', form.errors.keys())
        self.assertEqual(form.errors['review_content'][0], 'This field is required.')

    def test_review_emoji_is_required(self):
        form = ReviewForm({'review_emoji': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review_emoji', form.errors.keys())
        self.assertEqual(form.errors['review_emoji'][0], 'This field is required.')

    def test_author_is_required(self):
        form = ReviewForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')
