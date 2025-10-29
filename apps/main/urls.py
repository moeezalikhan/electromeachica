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
    path('product_singal/', views.product_singal, name='product_singal'),
    path('our_team/', views.our_team, name='our_team'),
    path('market_sector/', views.market_sector, name='market_sector'),
    path('our_mission/', views.our_mission, name='our_mission'),
    path('construction_products/', views.construction_products, name='construction_products'),
    path('aero_space_service/', views.aero_space_service, name='aero_space_service'),
    path('railway_infrastructure/', views.railway_infrastructure, name='railway_infrastructure'),
    path('ship_building_industry/', views.ship_building_industry, name='ship_building_industry'),
    path('power_energy/', views.power_energy, name='power_energy'),
    path('automative_system/', views.automative_system, name='automative_system'),
    
    
]

# /contact us/
# about us/

# our vision
# our mission 