""" ============= Imports =============== """
from django.db import models
from apps.utilities.models import BaseModel


""" ============= Team Model =============== """

class Team(BaseModel):
    
    image = models.ImageField(upload_to='teams/')
    full_name = models.CharField(max_length=255)
    designation = models.ForeignKey('Designation', on_delete=models.CASCADE, related_name='teams')
    active = models.BooleanField(default=True)
    priority = models.PositiveIntegerField(default=0)

    class Meta: # pyright: ignore[reportIncompatibleVariableOverride]
        ordering = ['priority']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

class Designation(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
