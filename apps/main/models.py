from django.db import models
from apps.utilities.models import BaseModel

# Create your models here.
class Brochure(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brochure = models.FileField(upload_to='brochures/')

    def __str__(self):
        return self.title