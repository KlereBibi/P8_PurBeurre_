from django.urls import path

from products import views

app_name = "products"

urlpatterns = [
    path('', views.home, name="home"),
    path('mentions/', views.mentions_legales, name="mentions"),
    path('search/', views.search_product, name="search"),
    path('food/<int:product_id>', views.food, name="food"),
    path('substitute/<int:product_id>/<int:original_product_id>', views.save_substitute, name="save"),
    path('userfood/', views.user_food, name="userfood")
]
