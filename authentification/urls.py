from django.urls import path
from django.contrib.auth.views import LogoutView
from authentification.views import LoginView, RegisterView, TemplateView
from purbeurre import settings
from django.conf.urls.static import static


app_name = "authentification"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(template_name='products/home.html', next_page=None), name='logout'),
    path('account/', TemplateView.as_view(), name='account')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
