
""" ============= Imports ============="""
from django.urls import path
from  . import views
""" ============== Urls ================= """

urlpatterns = [
       path('our_vision/', views.our_vision, name='our_vision'),
    path('our_team/', views.our_team, name='our_team'),
    path('our_mission/', views.our_mission, name='our_mission'),
]


