from django.test import TestCase, Client
from .models import BlogPost
from django.contrib.auth.models import User

""" django create superuser code from
https://gist.github.com/tommorris/cd1048418cccfa346fef"""


class TestViews(TestCase):
    def test_get_posts_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/posts.html')

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

    def test_get_add_post(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/blog/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/add_post.html')

    def test_get_edit_post(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        post = BlogPost.objects.create(title='Cat Tour')
        response = client.get(f'/blog/edit/{post.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/edit_post.html')

    def test_can_delete_post(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        post = BlogPost.objects.create(title='Cat Tour')
        response = client.get(f'/blog/delete/{post.id}')
        self.assertRedirects(response, '/blog/')
        existing_posts = BlogPost.objects.filter(id=post.id)
        self.assertEqual(len(existing_posts), 0)
