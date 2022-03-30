from django.urls import path

from authentification.views import LoginView, RegisterView

from products import views

app_name="auhentification"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]