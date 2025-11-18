from django.contrib import admin
from django.urls import path
from apps.main import views

# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('our_vision/', views.our_vision, name='our_vision'),
    path('contact_us/', views.contact_us, name='contact_page'),
    path('projectss/', views.projects, name='projects'),
    path('products/', views.products, name='products'),
    path('product_singal/', views.product_singal, name='product_singal'),
    path('our_team/', views.our_team, name='our_team'),
    path('market_sector/', views.market_sector, name='market_sector'),
    path('textile_sector/', views.textile_sector, name='textile_sector'),
    path('educational_trainers/', views.educational_trainers, name='educational_trainers'),
    path('industrial_trainers/', views.industrial_trainers, name='industrial_trainers'),
    path('testing_benches/', views.testing_benches, name='testing_benches'),
    path('our_mission/', views.our_mission, name='our_mission'),
    path('cement/', views.cement, name='cement'),
    path('fmcg/', views.fmcg, name='fmcg'),
    path('chemicals/', views.chemicals, name='chemicals'),
    path('faqs/', views.faqs, name='faqs'),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),

]

# /contact us/
# about us/

# our vision
# our mission
