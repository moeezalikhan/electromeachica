""" =========== Imports ============== """

from django.db import models
from apps.utilities.models import BaseModel
import uuid


""" ============ categories Model ============ """

class Categories(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta: # type: ignore
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

""" ============ Products Model ============ """
class Product(BaseModel):
    """ Defining choices for categories"""

    CATEGORY_CHOICES = [
        ('IN_STOCK', 'In Stock'),
        ('OUT_OF_STOCK', 'Out of Stock'),
        ('MAKE_TO_ORDER', 'Make to Order'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
    availability = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='IN_STOCK')
    model_number = models.CharField(max_length=255, null=True, blank=True)
    part_number = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.title}"