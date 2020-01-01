from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'login.html'
