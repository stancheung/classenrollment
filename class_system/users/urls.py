from django.contrib import admin
from django.urls import path
from . import views 
from classes import views as classes_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home),
    path('profile/', views.Profile, name='Profile'),
]