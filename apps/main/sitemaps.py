from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = 'http' 

    def items(self):
        return [
            'main:home',           
            'main:brochure',      
            'about_us:our_mission',
            'about_us:our_vision',
            'contact_us:contact_us',
            'contact_us:faqs',
            'contact_us:privacy_policy',
            'contact_us:term_of_use',
        ]

    def location(self, item):
        return reverse(item)
    
    
