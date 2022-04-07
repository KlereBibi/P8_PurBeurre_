from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from authentification.formulaire import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'authentification/login.html'
    success_url = reverse_lazy('authentification:user')


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'authentification/register.html'
    success_url = reverse_lazy('authentification:login')
