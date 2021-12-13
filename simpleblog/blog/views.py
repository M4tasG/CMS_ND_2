from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import Post

class MainView(LoginRequiredMixin, ListView):
    template_name = 'blog/main.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        queryset = Post.objects.filter(user=self.request.user).order_by('-created_at')
        return queryset
