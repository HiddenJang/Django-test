from django.urls import path
from . import views

urlpatterns = [
    path('developer/', views.developer, name='develop'),
    path('settings/', views.setting, name='settings'),
]