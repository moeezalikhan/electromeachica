""" ============= Imports =============== """
from django.contrib import admin
from django.urls import path
from . import views


""" ============= URL Patterns =============== """
urlpatterns = [
    path('', views.projects, name='projects'),
   
]
