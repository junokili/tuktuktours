from django.test import TestCase
from .forms import TourDetailForm


class TestTourDetailForm(TestCase):
    def test_tour_name_is_required(self):
        form = TourDetailForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_start_time_is_not_required(self):
        form = TourDetailForm({'name': 'Tour Name'})
        self.assertTrue(form.is_valid)
