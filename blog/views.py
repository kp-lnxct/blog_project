from django.http import request
from django.shortcuts import render
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
# Create your views here.

posts = [
    {
    'author':'Name',
    'title': 'Blog Post',
    'content' : 'First Post Content',
    'data_posted' : 'December 30, 2021'
    },
    {
    'author':'Name2',
    'title': 'Blog Post2',
    'content' : 'Second Post Content',
    'data_posted' : 'December 30, 2021'
    },
]



def home_page(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html',{'post':posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about_page():
    return render(request,'blog/about.html')

