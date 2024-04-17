from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('index/', views.index),
    path('number/<int:number>', views.number),
    path('hello/<str:username>', views.hello),
    path('about/', views.about),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('task/<int:id>', views.task),
    path('myprojects/', views.myprojects),
    path('mytasks/', views.mytasks),
]