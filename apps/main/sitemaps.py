from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = 'http' 

    def items(self):
        return [
            'home',           
            'brochure',      
            'our_mission',
            'our_vision',
            'contact_us',
            'faqs',
            'privacy_policy',
            'term_of_use',
            'teams',
            'market_sector',
            'textile_sector',
            'educational_trainers',
            'industrial_trainers',
            'testing_benches',
            'cement',
            'chemicals',
        ]

    def location(self, item):
        return reverse(item)
    
    
