from django.core.management.base import BaseCommand
import requests
import json
from products.models import Product, Category, Brand, Store, CategoryProduct


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

                for element in item['stores'].split(','):
                    store = Store(name=element)
                    store_obj.append(store)

                for element in item['brands'].split(','):
                    brand = Brand(name=element)
                    brand_obj.append(brand)

            except KeyError:
                continue

        product_db = []
        category_db = []
        brand_db = []
        store_db = []

        Product.objects.bulk_create(products_obj, ignore_conflicts=True)
        all_product_db = Product.objects.all()
        for element in all_product_db:
            product_db.append((element.id, element.name))

        Category.objects.bulk_create(category_obj, ignore_conflicts=True)
        all_category_db = Category.objects.all()
        for element in all_category_db:
            category_db.append((element.id, element.name))

        Store.objects.bulk_create(category_obj, ignore_conflicts=True)
        all_store_db = Store.objects.all()
        for element in all_store_db:
            store_db.append((element.id, element.name))

        Brand.objects.bulk_create(category_obj, ignore_conflicts=True)
        all_brand_db = Brand.objects.all()
        for element in all_brand_db:
            brand_db.append((element.id, element.name))

        product_non_saved = []
        for item in products_api:
            product = {"name": item['product_name_fr'],
                       "categories": item['categories'].split(','),
                       "brands": item['brands'].split(','),
                       "stores": item['stores'].split(',')}
            product_non_saved.append(product)

        productcategory = []
        productstore = []
        productbrand = []

        for product in product_db:
            non_saved_product = next(filter(lambda prod: prod['name'] == product[1], product_non_saved), None)
            if non_saved_product:
                for category in non_saved_product['categories']:
                    saved_category = next(filter(lambda cat: cat[1] == category, category_db), None)
                    if saved_category:
                        productcategory.append(CategoryProduct(id_product=product[0], id_category=saved_category[0]))
                for store in non_saved_product['stores']:
                    saved_store = next(filter(lambda sto: sto[1] == store, store_db), None)
                    if saved_store:
                        productstore.append((product[0], saved_store[0]))
                for brand in non_saved_product['brands']:
                    saved_brand = next(filter(lambda bra: bra[1] == brand, brand_db), None)
                    if saved_brand:
                        productbrand.append((product[0], saved_brand[0]))


        CategoryProduct.objects.bulk_create(productcategory)
