""" ============= Imports =============== """
from django.db import models
from apps.utilities.models import BaseModel
from django.urls import reverse


""" ============= Project Model =============== """
class Project(BaseModel):
    """ Defining choices for categories """
    CATEGORY_CHOICES = [
        ('business_growth', 'Business Growth'),
        ('consulting', 'Consulting'),
        ('management', 'Management'),
        ('customer_insights', 'Customer Insights'),
        ('organization', 'Organization'),
    ]

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    

    def __str__(self):
        return self.name
   

""" ============= Project Image Model =============== """
class ProjectImage(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Image for {self.project.name}"
