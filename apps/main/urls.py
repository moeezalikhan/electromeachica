from django.contrib import admin
from django.urls import path
from apps.main import views

# urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('brochure/', views.brochure, name='brochure'),
    
    
  
     
]

# /contact us/
# about us/

# our vision
# our mission
