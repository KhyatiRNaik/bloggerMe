# from django.contrib import messages
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# def home(request):
#     context={
#         'posts': Post.objects.all().order_by('-posted_on')
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blog/home.html' #default searches for  : <app>/<model>_<viewtype>.html  here blog/post_list.html 
    ordering = '-posted_on'
    paginate_by = 6


class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blog/user_posts.html' #default searches for  : <app>/<model>_<viewtype>.html  here blog/post_list.html 
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-posted_on')

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # unlike others template_name searches for <app>/<model>_forms.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # unlike others template_name searches for <app>/<model>_forms.html

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
    context_object_name = 'post' 
    success_url = '/'
    # messages.success(f'Deleted post successfully')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False