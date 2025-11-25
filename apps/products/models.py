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
    ]
    
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
    availability = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='IN_STOCK')
    sku = models.CharField(max_length=255,unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f"PRO-{uuid.uuid4().hex[:5].upper()}"
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.title}"