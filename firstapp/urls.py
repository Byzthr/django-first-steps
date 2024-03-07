from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('number/<int:number>', views.number),
    path('hello/<str:username>', views.hello),
    path('about/', views.about)
]