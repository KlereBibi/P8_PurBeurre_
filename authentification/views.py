from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.urls import reverse
from authentification.formulaire import LoginForm, RegisterForm
from django.shortcuts import render


def account_user(request):
    return render(request, "authentification/account.html")


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'authentification/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'authentification/register.html'
    success_url = reverse_lazy('authentification:login')



