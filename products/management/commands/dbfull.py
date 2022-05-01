from django.core.management.base import BaseCommand
from products.apimanager import ApiManager


class Command(BaseCommand):

    def handle(self, *args, **options):
        apimanager = ApiManager()
        apimanager.search_products()