""" ============== Imports ============= """
from django.urls import path
from apps.teams import views


""" ============ URLS =============== """

urlpatterns = [
    path('', views.team_list, name='team_list'),
]
