from django.contrib import admin
from django.urls import path
from apps.main import views

# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('our_vision/', views.our_vision, name='our_vision'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('projects/', views.projects, name='projects'),
    path('products/', views.products, name='products'),
    path('our_team/', views.our_team, name='our_team'),
     path('our_mission/', views.our_mission, name='our_mission'),

]

# /contact us/
# about us/

# our vision
# our mission 