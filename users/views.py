from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'accounts/login.html'
