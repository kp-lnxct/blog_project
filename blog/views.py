from django.db.models.signals import pre_migrate
from django.http import request
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.models import User
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
    return render(request, 'blog/home.html',{'post':posts, })

def like(request,pk):
    login = request.user.is_authenticated
    if login == True:
        user = User.objects.get(id = request.user.id)
        alredy_like = Like.objects.filter(post_id = pk ,user_id = user)
        if not alredy_like:
            post_id = Post.objects.get(id=pk)
            Like.objects.create(post_id = post_id, user_id = user)
        return redirect('/')
    else:
        return redirect('admin_login')

def post_like_count(request):
    posts = Post.objects.all()
    ls = []
    for i in posts:
        a = Like.objects.all().filter(post_id = i.id).count()
        print('----------------------',a )
        ls.append(a)
    return ls
    

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date']

    def get_context_data(self, ):
        posts = Post.objects.all()
        t_user = User.objects.count()
        t_post = len(posts)
        p_like = post_like_count(self.request)
        post_data = zip(posts, p_like)


        login = self.request.user.is_authenticated
        if login == True:
            user = User.objects.get(id = self.request.user.id)
            u_post = Post.objects.all().filter(author = user )
            
            my_post =  len(u_post)
            return {'post_data':post_data, 'u_post': u_post, 't_user':t_user, 't_post':t_post, 'mypost':my_post, 'p_like':p_like }
        else:
            total = {}
            for i in range(t_post):
                name = posts[i].author.username
                print('== ', name )
                if name in total:
                    total[name] = total[name] + 1
                else:
                    total[name] =  1
            print('*********************', total)
            
            return {'post_data':post_data,  't_user':t_user, 't_post':t_post,'t_key': total, 't_value': total.values() }

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about_page():
    return render(request,'blog/about.html')

