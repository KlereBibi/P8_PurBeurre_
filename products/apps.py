"""product to configure the product table in the database"""

from django.apps import AppConfig


class ProductsConfig(AppConfig):

    """change of id increment configuration"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
