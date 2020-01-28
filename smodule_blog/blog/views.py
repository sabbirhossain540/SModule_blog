from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posts

# Create your views here.
posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'august 2019'
    },
    {
        'author':'Sabbir',
        'title':'Blog Post c',
        'content':'second Post Content',
        'date_posted':'jan 2019'
    },
    {
        'author':'Sakib Al Jubair',
        'title':'Morning Habit',
        'content':'Tried Post Content',
        'date_posted':'january 2020'
    }

]

def home(request):
    #return HttpResponse('This our home page')
    context = {
        'posts':Posts.objects.all()
    }
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Posts
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'blog/post_conform_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
