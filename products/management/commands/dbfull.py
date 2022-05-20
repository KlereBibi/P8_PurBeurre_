from django.core.management.base import BaseCommand
import requests
import json
from products.models import Product, Category, CategoryProduct


class Command(BaseCommand):

    def handle(self, *args, **options):

        categories_find = requests. \
            get("https://fr.openfoodfacts.org/categories.json")
        read = json.loads(categories_find.text)
        categories = read['tags']
        categories.sort(key=lambda x: x["products"], reverse=True)
        six_categories = categories[:6]
        name_categories = []
        for element in six_categories:
            name_categories.append(element['name'])

        products_api = []
        category_obj = []
        products_obj = []
        store_obj = []
        brand_obj = []

        for element in name_categories:
            products_find = requests. \
                get("https://fr.openfoodfacts.org/cgi/search.pl?action=process"
                    "&tagtype_0=categories&tag_contains_0=contains&"
                    "tag_0={}&page_size=1&json=1".format(element))
            result = json.loads(products_find.text)
            products_api += result['products']

        for item in products_api:
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

            except KeyError:
                continue

        Product.objects.bulk_create(products_obj, ignore_conflicts=True)
        product_db = Product.objects.all()

        Category.objects.bulk_create(category_obj, ignore_conflicts=True)
        category_db = Category.objects.all()

        product_non_saved = []
        for item in products_api:
            product = {"name": item['product_name_fr'],
                       "categories": item['categories'].split(','),
                       "brands": item['brands'].split(','),
                       "stores": item['stores'].split(',')}
            product_non_saved.append(product)

        productcategory = []

        for product in product_db:
            non_saved_product = next(filter(lambda prod: prod['name'] == product.name, product_non_saved), None)
            if non_saved_product:
                for category in non_saved_product['categories']:
                    saved_category = next(filter(lambda cat: cat.name == category, category_db), None)
                    if saved_category:
                        productcategory.append(CategoryProduct(product=product, category=saved_category))

        CategoryProduct.objects.bulk_create(productcategory)
