""" =========== Imports ============== """

from django.db import models
from apps.utilities.models import BaseModel


""" ============ categories Model ============ """

class Categories(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

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
from django.db import models
from apps.utilities.models import BaseModel
from django.utils.html import format_html

class ProductImage(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    list_image = models.ImageField(upload_to='list_images/', default='default.jpg')

    def __str__(self):
        return f"Image for {self.product.title}"

    # ====== Move image preview here ======
    def image_tag(self):
        if self.image:
            return format_html('<img src="{}" style="width:100px; height:auto;" />', self.image.url)
        return "-"
    image_tag.short_description = 'Image' # type: ignore

    def list_image_tag(self):
        if self.list_image:
            return format_html('<img src="{}" style="width:100px; height:auto;" />', self.list_image.url)
        return "-"
    list_image_tag.short_description = 'List Image' # type: ignore


