
""" ============= Imports ============="""
from django.urls import path
from  . import views
""" ============== Urls ================= """

urlpatterns = [
    path('', views.contact_us, name="contact_us"),
]


