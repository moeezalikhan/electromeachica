from django.contrib.sitemaps import Sitemap
from .models import Project
from django.urls import reverse

class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Project.objects.filter(is_active=True)  

    def location(self, obj):
        
        return reverse('projects') 
    def lastmod(self, obj):
        return obj.updated_at
