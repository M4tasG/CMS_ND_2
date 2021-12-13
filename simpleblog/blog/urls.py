from django.urls import path, include
from .views import MainView, PostDetailView

urlpatterns = [
    path('', MainView.as_view(), name='blog-main'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-post'),
]
