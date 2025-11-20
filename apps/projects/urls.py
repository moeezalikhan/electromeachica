""" ============= Imports =============== """
from django.contrib import admin
from django.urls import path
from . import views


""" ============= URL Patterns =============== """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.projects, name='projects'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]
