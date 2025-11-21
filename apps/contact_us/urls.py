from django.contrib import admin
from django.urls import path
from apps.contact_us import views

# urls.py
urlpatterns = [

path('', views.contact_us, name='contact_us'),
path('faqs/', views.faqs, name='faqs'),
path("privacy-policy/", views.privacy_policy, name="privacy_policy"),

 
]