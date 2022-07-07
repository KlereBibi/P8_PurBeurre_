from django.test import TestCase

from django.test import Client
from authentification.models import User


class TestViews(TestCase):
    def setUp(self):
        user = User(username='test', email='test@gmail.com', is_active=True)
        user.set_password('testpassword')
        user.save()

    def test_login_page(self):
        c = Client()
        response = c.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/login.html')

    def test_login_succes(self):
        c = Client()
        response = c.post('/auth/login/', {'username': 'test', 'password': 'testpasswrd'})
        self.assertRedirects(response, '/')





