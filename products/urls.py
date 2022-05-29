from django.urls import path

from products import views

app_name = "products"

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search_product, name="search"),
    path('food/<product_id>', views.food, name="food")
]
