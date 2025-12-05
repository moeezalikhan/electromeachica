from django.db import models
from apps.utilities.models import BaseModel

# Create your models here.
class Brochure(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brochure = models.FileField(upload_to='brochures/')

    def __str__(self):
        return self.title


class Banner(BaseModel):
    MARKET_SECTOR_CHOICES = [
        ('textile', 'Textile'),
        ('chemicals', 'Chemicals'),
        ('FMGC', 'FMGC'),
        ('Cement', 'Cement'),
        ('TEST_BENCH', 'Test Bench'),
        ('EDUCATIONAL_TRAINERS', 'Educational Trainers'),
        ('INDUSTRIAL_TRAINERS', 'Industrial Trainers'),
        ('OTHERS', 'Others'),
    ]
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='banners/')
    category = models.CharField(max_length=255, choices=MARKET_SECTOR_CHOICES)
    priority = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title