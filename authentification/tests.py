"""module containing the Authentication application tests"""

from django.test import TestCase
from django.test import Client
from authentification.models import User


class TestViews(TestCase):

    """class to test the different feature about authentification"""

    def setUp(self):

        """user settings initialization for test"""

        user = User(username='test', email='test@gmail.com', is_active=True)
        user.set_password('test@.test')
        user.save()

    def test_login_page(self):

        """page login test """

        c = Client()
        response = c.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/login.html')

    def test_login_succes(self):

        """login success test with identifiant"""

        c = Client()
        response = c.post('/auth/login/', {'username': 'test', 'password': 'test@.test'})
        self.assertRedirects(response, '/')

    def test_login_error(self):

        """login success test with identifiant"""

        c = Client()
        response = c.post('/auth/login/', {'username': 'false', 'password': 'false'})
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):

        """page register test """

        c = Client()
        response = c.get('/auth/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/register.html')

    def test_register_error(self):

        """register error test with identifiant"""

        c = Client()
        response = c.post('/auth/register/', {'email': 'claire@gmail.com', 'username': 'Claire',
                                              'first_name': 'TheBest', 'last_name': 'OfTheWorld',
                                              'password1': 'password', 'password2': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/register.html')

    def test_register_success(self):

        """register success test with identifiant"""

        c = Client()
        response = c.post('/auth/register/', {'email': 'claire@gmail.com', 'username': 'Claire',
                                              'first_name': 'TheBest', 'last_name': 'OfTheWorld',
                                              'password1': 'test@.test', 'password2': 'test@.test'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/login/')

    def test_account_page(self):

        """page account test """

        c = Client()
        response = c.get('/auth/account/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/account.html')
