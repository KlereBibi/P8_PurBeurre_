from django.urls import path

from authentification.views import LoginView, RegisterView


app_name = "authentification"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]