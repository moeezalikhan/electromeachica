""" ============= Imports =============== """
from django.db import models
from apps.utilities.models import BaseModel


""" ============= Team Model =============== """

class Team(BaseModel):
    
    DESINATION_CHOICES = [
        ('presedent', 'Presedent'),
        ('engineer', 'Engineer'),
        ('team_lead', 'Team Lead'),
        ('manager', 'Manager'),
    
]
    image = models.ImageField(upload_to='teams/')
    full_name = models.CharField(max_length=255)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    desination = models.CharField(max_length=25, choices=DESINATION_CHOICES)
    active = models.BooleanField(default=True)
    priority = models.PositiveIntegerField(default=0)

    class Meta: # pyright: ignore[reportIncompatibleVariableOverride]
        ordering = ['priority']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
