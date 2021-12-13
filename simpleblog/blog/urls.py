from django.urls import path, include
from .views import MainView, PostDetailView, CreatePostView, ProfileDetailView

urlpatterns = [
    path('', MainView.as_view(), name='blog-main'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-post'),
    path('post/new/', CreatePostView.as_view(), name='blog-post-new'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='blog-profile'),

]
