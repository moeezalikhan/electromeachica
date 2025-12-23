from django.db import models
from apps.utilities.models import BaseModel

# Create your models here.
class ContactUs(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.name
