from django.urls import path

from authentification.views import LoginView, RegisterView
from authentification import views


app_name = "authentification"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('account/', views.account_user, name='account'),
]
