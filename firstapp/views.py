from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Project, Task

# Create your views here.

def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}<h1/>")

def number(request, number):
    return HttpResponse(f"<h1>Your number: {number}<h1/>")

def index(request):
    title = "Welcome to my first page"
    return render(request, 'index.html', {'title':title})

def about(request):
    return render(request, 'about.html')

def projects(request):
    return JsonResponse(list(Project.objects.values()), safe=False)

def tasks(request):
    return JsonResponse(list(Task.objects.values()), safe=False)

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"Task {id}: {task.title}")

def myprojects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects':projects})

def mytasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks':tasks})
