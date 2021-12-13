from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm

class AuthenticationLoginView(LoginView):
    template_name = "authentication/login.html"

class AuthenticationLogoutView(LoginRequiredMixin ,LogoutView):
    template_name = "authentication/logout.html"

class AuthenticationSignupView(CreateView):
    form_class = SignUpForm
    template_name = "authentication/signup.html"
    success_url = reverse_lazy('authentication-login')