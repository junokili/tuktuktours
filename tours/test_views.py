from django.test import TestCase, Client
from .models import Tour, Category
from django.contrib.auth.models import User

""" django create superuser code from
https://gist.github.com/tommorris/cd1048418cccfa346fef"""


class TestViews(TestCase):
    def test_get_tours_list(self):
        response = self.client.get('/tours/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tours/tours.html')

    def create_user(self):
        self.username = "test_admin"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def test_get_add_tour(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/tours/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tours/add_tour.html')

    def test_get_edit_tour(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        tour = Tour.objects.create(name='Cat Tour', price='20')
        response = client.get(f'/tours/edit/{tour.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tours/edit_tour.html')

    def test_can_delete_tour(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        tour = Tour.objects.create(name='Cat Tour', price='20')
        response = client.get(f'/tours/delete/{tour.id}')
        self.assertRedirects(response, '/tours/')
        existing_tours = Tour.objects.filter(id=tour.id)
        self.assertEqual(len(existing_tours), 0)

    def test_get_categories_list(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/tours/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tours/categories.html')

    def test_get_add_category(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/tours/categories/add_category', {}, True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tours/categories/add_category.html')

    def test_get_edit_category(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        category = Category.objects.create(name='Cat Tour')
        response = client.get(f'/tours/categories/edit_category/{category.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tours/categories/edit_category.html')
