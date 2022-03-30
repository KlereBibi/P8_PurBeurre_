from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=15)
    is_active = models.BooleanField


