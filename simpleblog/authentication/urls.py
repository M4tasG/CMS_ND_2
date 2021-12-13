from django.urls import path
from . import views
from .views import AuthenticationLoginView, AuthenticationLogoutView, AuthenticationSignupView

# URL Patterns for pages
# Class based views are imported and displayed with .as_view() method
# Function based views are imported and displayed as views.viewname
urlpatterns = [
    path('login/', AuthenticationLoginView.as_view(), name='authentication-login'),
    path('logout/', AuthenticationLogoutView.as_view(), name='authentication-logout'),
    path('signup/', AuthenticationSignupView.as_view(), name='authentication-signup')
]
