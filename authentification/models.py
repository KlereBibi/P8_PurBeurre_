from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)


