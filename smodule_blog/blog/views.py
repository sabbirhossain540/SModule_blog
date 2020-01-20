from django.shortcuts import render
from django.http import HttpResponse

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
        'posts':posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
