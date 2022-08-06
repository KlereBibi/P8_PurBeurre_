"""module returning the different views of the authentication"""

from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from authentification.forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):

    """class returning the form login page
    return a login template"""

    form_class = LoginForm
    template_name = 'authentification/login.html'


class RegisterView(generic.CreateView):

    """class returning the form register page
    attach a register template
    if success return a login template"""

    form_class = RegisterForm
    template_name = 'authentification/register.html'
    success_url = reverse_lazy('authentification:login')


class TemplateView(auth_views.TemplateView):

    """class attach the user's account page"""

    template_name = "authentification/account.html"




