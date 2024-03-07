from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello Tamed Team<h1/>")

def about(request):
    return HttpResponse("<h1>About page<h1/>")