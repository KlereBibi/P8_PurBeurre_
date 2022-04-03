from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    fullname = forms.CharField(label="First name")
    fullname2 = forms.CharField(label="Last name")

    class Meta:
        model = get_user_model()
        fields = ('email', 'fullname', 'fullname2', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
