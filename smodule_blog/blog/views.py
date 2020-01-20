from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('This our home page')

def about(request):
    return HttpResponse("<h1>Blog About</h1>")
