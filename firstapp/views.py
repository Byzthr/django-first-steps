from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(f"<h1>Main Page<h1/>")

def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}<h1/>")

def number(request, number):
    return HttpResponse(f"<h1>Your number: {number}<h1/>")

def about(request):
    return HttpResponse("<h1>About page<h1/>")