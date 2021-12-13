from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import Post

class MainView(LoginRequiredMixin, ListView):
    template_name = 'blog/main.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.filter(author = self.request.user).order_by('-created_on')
        return queryset

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'blog/post.html'
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create_post.html'
    model = Post
    context_object_name = 'form'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)