from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nutriscore = models.CharField(max_length=1)
    url = models.URLField(max_length=200)
    calories = models.TextField(max_length=200)
    picture = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    products = models.ManyToManyField(Product, related_name='brands')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)
    products = models.ManyToManyField(Product, related_name='stores')

    def __str__(self):
        return self.name
