""" =========== Imports ============== """

from django.db import models
from apps.utilities.models import BaseModel


""" ============ Products Model ============ """
class Product(BaseModel):
    """ Defining choices for categories"""

    
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
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



class Categories(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name