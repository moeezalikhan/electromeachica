""" =========== Imports ============== """

from django.db import models
from apps.utilities.models import BaseModel


""" ============ Products Model ============ """
class Product(BaseModel):
    """ Defining choices for categories"""
    CATEGORY_CHOICES = [
        ('business_growth', 'Business Growth'),
        ('consulting', 'Consulting'),
        ('management', 'Management'),
        ('customer_insights', 'Customer Insights'),
        ('organization', 'Organization')
    ]
    
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    availability = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title

""" =========== Product Image Model =========== """

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    list_image = models.ImageField(upload_to='list_images/', default='default.jpg')

    def __str__(self):
        return f"Image for {self.product.title}"
