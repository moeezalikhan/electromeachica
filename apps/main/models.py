from django.db import models
from apps.utilities.models import BaseModel
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.core.exceptions import ValidationError


""" =========== Validator for file size ============="""

def validate_file_size(file):
    max_size = settings.BROCHURE_MAX_FILE_SIZE_MB * 1024 * 1024  # Convert MB to Bytes
    if file.size > max_size:
        raise ValidationError(f"File size should not exceed {settings.BROCHURE_MAX_FILE_SIZE_MB} MB.")
    

# Create your models here.
class Brochure(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brochure = models.FileField(upload_to='brochures/',validators=[
        FileExtensionValidator(allowed_extensions=settings.BROCHURE_ALLOWED_EXTENSIONS),
        validate_file_size
    ])
    
    priority = models.IntegerField(default=0)

    class Meta:  # type: ignore
        verbose_name = "Brochure"
        verbose_name_plural = "Brochures"
        ordering = ['priority']

    def __str__(self):
        return self.title


class Banner(BaseModel):
    MARKET_SECTOR_CHOICES = [
        ('textile', 'Textile'),
        ('chemicals', 'Chemicals'),
        ('FMCG', 'FMCG'),
        ('Cement', 'Cement'),
        ('TEST_BENCH', 'Test Bench'),
        ('EDUCATIONAL_TRAINERS', 'Educational Trainers'),
        ('INDUSTRIAL_TRAINERS', 'Industrial Trainers'),
        ('OTHERS', 'Others'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='banners/')
    category = models.CharField(max_length=255, choices=MARKET_SECTOR_CHOICES)
    priority = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


class OurClient(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='our_clients/')
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta: # type: ignore
        verbose_name = "Our Client"
        verbose_name_plural = "Our Clients"
        ordering = ['priority']