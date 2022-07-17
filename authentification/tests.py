from django.test import TestCase

from django.test import Client
from authentification.models import User


class TestViews(TestCase):
    def setUp(self):
        user = User(username='test', email='test@gmail.com', is_active=True)
        user.set_password('test@.test')
        user.save()

    def test_login_page(self):
        c = Client()
        response = c.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/login.html')

    def test_login_succes(self):
        c = Client()
        response = c.post('/auth/login/', {'username': 'test', 'password': 'test@.test'})
        self.assertRedirects(response, '/')

    def test_login_error(self):
        c = Client()
        response = c.post('/auth/login/', {'username': 'false', 'password': 'false'})
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        c = Client()
        response = c.get('/auth/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/register.html')

    def test_register_error(self):
        c = Client()
        response = c.post('/auth/register/', {'email': 'claire@gmail.com', 'username': 'Claire', 'first_name': 'TheBest', 'last_name': 'OfTheWorld', 'password1': 'password', 'password2': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/register.html')

    def test_register_success(self):
        c = Client()
        response = c.post('/auth/register/', {'email': 'claire@gmail.com', 'username': 'Claire', 'first_name': 'TheBest', 'last_name': 'OfTheWorld', 'password1': 'test@.test', 'password2': 'test@.test'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/login/')

    def test_account_page(self):
        c = Client()
        response = c.get('/auth/account/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/account.html')
