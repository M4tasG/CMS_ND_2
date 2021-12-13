from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Post

class MainView(LoginRequiredMixin, ListView):
    template_name = 'blog/main.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_on')
        return queryset

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'blog/post.html'
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create_post.html'
    model = Post
    context_object_name = 'form'
    fields = ['title', 'body']
    success_url = reverse_lazy('blog-main')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'blog/profile.html'
    model = User
    context_object_name = 'user_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        context['posts'] = Post.objects.filter(author__id = self.kwargs['pk'])[:2]
        return context