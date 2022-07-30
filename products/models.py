""""module with different class to create table in databse and object"""

from django.db import models
from authentification.models import User


class Product(models.Model):

    """"class to creat product"""

    name = models.CharField(max_length=100, unique=True)
    nutriscore = models.CharField(max_length=1)
    url = models.URLField(max_length=200)
    calories = models.TextField(max_length=200)
    picture = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):

    """"class to creat category"""

    name = models.CharField(max_length=100, unique=True)
    products = models.ManyToManyField(Product, through='CategoryProduct', related_name="categories")

    def __str__(self):
        return self.name


class CategoryProduct(models.Model):

    """"relationship class between category and product"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Substitute(models.Model):

    """"relationship class between user and substitute in product search"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="substitute")

    class Meta:
        unique_together = ["product", "user"]