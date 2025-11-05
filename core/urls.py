"""
URL configuration for electromeachica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


""" ========== Imports ============= """

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

""" =============== Main Urls ================= """
urlpatterns = [
    # Admin Url
    path('admin/', admin.site.urls),

    # Projects Urls
    path('projects/', include('apps.projects.urls')),
    
    # teams urls
    path('teams/', include('apps.teams.urls')),

    # Products Urls
    path('products/', include('apps.products.urls')),
    
    # Products Urls
    path('about_us/', include('apps.about_us.urls')),

    # Main Urls
    path('', include('apps.main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
