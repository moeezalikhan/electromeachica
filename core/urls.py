"""
URL configuration for Electromechanica project.

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
from django.contrib.sitemaps.views import sitemap
from apps.products.sitemaps import ProductSitemap
from apps.projects.sitemaps import ProjectSitemap
from apps.main.sitemaps import StaticViewSitemap
from django.conf.urls import handler404, handler500


handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'

sitemaps = {
    'products': ProductSitemap,
    'projects': ProjectSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps URLs with namespaces
    path('', include('apps.main.urls', )),
    path('', include('apps.about_us.urls',)),
    path('', include('apps.contact_us.urls',)),
    path('products/', include('apps.products.urls')),
    path('projects/', include('apps.projects.urls')),
    path('teams/', include('apps.teams.urls', )),
    path('market-sectors/', include('apps.market_sector.urls', )),



    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

