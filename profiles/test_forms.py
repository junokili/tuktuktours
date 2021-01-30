from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForm(TestCase):
    def test_full_name_is_required(self):
        form = UserProfileForm({'default_full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('default_full_name', form.errors.keys())
        self.assertEqual(form.errors['default_full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = UserProfileForm({'default_email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('default_email', form.errors.keys())
        self.assertEqual(form.errors['default_email'][0], 'This field is required.')

    def test_phone_number_is_not_required(self):
        form = UserProfileForm({'default_phone_number': 'My Name'})
        self.assertTrue(form.is_valid)

    def test_postcode_is_not_required(self):
        form = UserProfileForm({'default_postcode': 'My Name'})
        self.assertTrue(form.is_valid)

    def test_town_is_not_required(self):
        form = UserProfileForm({'default_town_or_city': 'My Name'})
        self.assertTrue(form.is_valid)

    def test_street_add1_is_not_required(self):
        form = UserProfileForm({'default_street_address1': 'My Name'})
        self.assertTrue(form.is_valid)

    def test_street_add2_is_not_required(self):
        form = UserProfileForm({'default_street_address2': 'My Name'})
        self.assertTrue(form.is_valid)

    def test_country_is_not_required(self):
        form = UserProfileForm({'default_country': 'My Name'})
        self.assertTrue(form.is_valid)
