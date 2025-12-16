from django.urls import path
from apps.market_sector import views



# urls.py
urlpatterns = [
    path('', views.market_sector, name='market_sector'),
    path('textile_sector/', views.textile_sector, name='textile_sector'),
    path('educational_trainers/', views.educational_trainers, name='educational_trainers'),
    path('industrial_trainers/', views.industrial_trainers, name='industrial_trainers'),
    path('testing_benches/', views.testing_benches, name='testing_benches'),
    path('cement/', views.cement, name='cement'),
    path('fmcg/', views.fmcg, name='fmcg'),
    path('chemicals/', views.chemicals, name='chemicals'),
]