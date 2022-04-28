import requests
import json
from products.entities.product import Product


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
        products = []
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
                    item['product_name_fr'],
                    item['nutriscore_grade'],
                    item['categories'],
                    item['url'],
                    item['brands'],
                    item['stores'],
                    item['image_front_url'],
                    item['energy-kcal_100g']
                )
                products.append(newprod)
            except KeyError:
                continue
#du model avec les bonnes informations
        return products

    def searchallinformation(self):

        products = self.search_products()



