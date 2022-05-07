from django.core.management.base import BaseCommand
from products.apimanager import ApiManager
import requests
import json
from products.models import Product, Category, Brand, Store


class ApiManager:
    """Class used to query the API, retrieve data,
       process it and send it to the product manager."""

    def search_categories(self):
        """Method querying the OpenFoodFac API to retrieve categories.
        Methode sort them by increasing popularity.
        returns:
        - name_categories (liste) : list name of the first six categories"""

        categories_find = requests. \
            get("https://fr.openfoodfacts.org/categories.json")
        read = json.loads(categories_find.text)
        categories = read['tags']
        categories.sort(key=lambda x: x["products"], reverse=True)
        six_categories = categories[:6]
        name_categories = []
        for element in six_categories:
            name_categories.append(element['name'])

        return name_categories

    def search_products(self):

        """ Method requesting the OpenFoodFac API
        to find the products with the category list.
        The method registers products with the Product class.
        returns:
        - products (liste) : list of product with ID = None."""

        products_saved = []
        category_obj = []
        products_obj = []
        store_obj = []
        brand_obj = []
        for element in self.search_categories():
            products_find = requests. \
                get("https://fr.openfoodfacts.org/cgi/search.pl?action=process"
                    "&tagtype_0=categories&tag_contains_0=contains&"
                    "tag_0={}&page_size=1&json=1".format(element))
            result = json.loads(products_find.text)
            products_saved += result['products']

        for item in products_saved:
            try:

                newprod = Product(
                     name=item['product_name_fr'],
                     nutriscore=item['nutriscore_grade'],
                     url=item['url'],
                     calories=item['image_nutrition_url'],
                     picture=item['image_front_url'])
                products_obj.append(newprod)

                for element in item['categories'].split(','):
                    catego = Category(name=element)
                    category_obj.append(catego)

                for element in item['stores'].split(','):
                    store = Store(name=element)
                    store_obj.append(store)

                for element in item['brands'].split(','):
                    brand = Brand(name=element)
                    brand_obj.append(brand)

            except KeyError:
                continue

        Product.objects.bulk_create(products_obj, ignore_conflicts=True)
        Brand.objects.bulk_create(brand_obj, ignore_conflicts=True)
        Store.objects.bulk_create(store_obj, ignore_conflicts=True)
        Category.objects.bulk_create(category_obj, ignore_conflicts=True)

        x = Product.objects.all()
        print(x)

class Command(BaseCommand):

    def handle(self, *args, **options):
        apimanager = ApiManager()
        apimanager.search_products()