from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='index'),
    path('about/', views.childTemplate, name='about'),
]