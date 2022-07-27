from django.test import TestCase
from django.test import Client
from products.models import Product
from products.models import Category
from products.models import CategoryProduct


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

    def test_food_page_product_ok(self):
        c = Client()
        product = Product.objects.create(name='Pain', nutriscore='d', url='pain.fr', calories='5', picture='pain.fr')
        response = c.get('/food/{}'.format(product.pk))
        self.assertEqual(response.context['product'], product)

    def test_food_page_substitute_ok(self):
        c = Client()
        product_user = Product.objects.create(name='Pain', nutriscore='d', url='pain.fr', calories='5', picture='pain.fr')
        product_good = Product.objects.create(name='Pain Céréale', nutriscore='b', url='paincereal.fr', calories='3', picture='paincereal.fr')
        product_bad = Product.objects.create(name='Nutella', nutriscore='e', url='nut.fr', calories='20', picture='nut.fr')
        cat1 = Category.objects.create(name='boulangerie')
        cat2 = Category.objects.create(name='chocolat')
        cat3 = Category.objects.create(name='farine')
        CategoryProduct.objects.create(product=product_user,  category=cat1)
        CategoryProduct.objects.create(product=product_user, category=cat3)
        CategoryProduct.objects.create(product=product_good, category=cat1)
        CategoryProduct.objects.create(product=product_bad, category=cat2)

        response = c.get('/food/{}'.format(product_user.pk))
        substitute_query = response.context['substitutes']
        substitute_list = substitute_query.all()
        for element in substitute_list:
            substitute_name = (str(element))
        product_substitute_good = (str(product_good.name))
        self.assertEqual(substitute_name, product_substitute_good)

    def test_substitute_page(self):
        c = Client()
        c.login(email='test@gmail.com', password='test@.test')
        product = Product.objects.create(name='Pain', nutriscore='d', url='pain.fr', calories='5', picture='pain.fr')
        original_product_id = Product.objects.create(name='rien', nutriscore='d', url='pain.fr', calories='5', picture='pain.fr')
        response = c.get(f'/substitute/{product.pk}/{original_product_id.pk}')
        self.assertRedirects(response, f'/auth/login/?next=/substitute/{product.pk}/{original_product_id.pk}')

    def test_userfood_page(self):
         c = Client()
         c.login(email='test@gmail.com', password='test@.test')
         response = c.get('/userfood/')
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'products/userfood.html')

