from django.urls import path

from authentification.views import LoginView, RegisterView, LogoutView


app_name = "authentification"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(template_name="authentification/logout.html"), name='logout'),
]
