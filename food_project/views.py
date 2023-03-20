from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class Login(LoginView):
    authentication_form = AuthenticationForm
    template_name = "authentication/login.html"
