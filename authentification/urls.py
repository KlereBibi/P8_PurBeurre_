from django.contrib import admin
from django.urls import path

from products import views

app_name="auhentification"

urlpatterns = [
    path('login', views.user, name="login"),
]