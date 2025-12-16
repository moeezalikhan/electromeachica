from django.urls import path
from . import views


urlpatterns = [
    path('our-mission/', views.our_mission, name='our_mission'),
    path('our-vision/', views.our_vision, name='our_vision'),
]
