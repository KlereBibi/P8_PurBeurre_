from django.test import TestCase
from django.test import Client
from products.models import Product
from authentification.models import User


class TestViews(TestCase):

    def test_home_page(self):
        c = Client()
        response = c.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/home.html')

    def test_food_page(self):
        c = Client()
        product = Product.objects.create(name='Pain', nutriscore='d', url='pain.fr', calories='5', picture='pain.fr')
        response = c.get('/food/{}'.format(product.pk))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/food.html')
        #faire un assert pour vérifier le contenu (bon produit)
        #substitut et qui ont bien des catégories en commun (créer des substitut avec les même catégories et pas même catégotir
        #coverage : quel ligne est tester ou pas

    def test_substitute_page(self):
        user = User(username='test', email='test@gmail.com', is_active=True)
        user.set_password('test@.test')
        user.save()
        c = Client()
        c.login(email='test@gmail.com', password='test@.test')
        product = Product.objects.create(name='Pain', nutriscore='d', url='pain.fr', calories='5', picture='pain.fr')
        substitute = Product.objects.create(name='rien', nutriscore='d', url='pain.fr', calories='5', picture='pain.fr')
        response = c.get(f'/subistitute/{product.pk}/{substitute.pk}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/food.html')
        #tester l'intérieur de la vue
        #que dans la page il y est bien le produit demandé
        #créer un objet qui n'a rien à voir

    def test_userfood_page(self):
         user = User(username='test', email='test@gmail.com', is_active=True)
         user.set_password('test@.test')
         user.save()
         c = Client()
         c.login(email='test@gmail.com', password='test@.test')
         response = c.get('/userfood/')
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'products/userfood.html')
