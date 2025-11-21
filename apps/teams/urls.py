""" ============== Imports ============= """
from django.urls import path
from apps.teams import views


""" ============ URLS =============== """

urlpatterns = [
    path('', views.teams, name='teams'),
]
