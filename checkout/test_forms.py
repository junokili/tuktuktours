from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    def test_tour_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')

    def test_street_add1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0], 'This field is required.')

    def test_street_add2_is_not_required(self):
        form = OrderForm({'street_address2': 'My Order'})
        self.assertFalse(form.is_valid())

    def test_town_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0], 'This field is required.')

    def test_postcode_is_not_required(self):
        form = OrderForm({'postcode': 'My Order'})
        self.assertFalse(form.is_valid())

    def test_country_required(self):
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')

    def test_county_is_not_required(self):
        form = OrderForm({'county': 'My Order'})
        self.assertFalse(form.is_valid())
