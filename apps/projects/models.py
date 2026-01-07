""" ============= Imports =============== """
from django.db import models
from apps.utilities.models import BaseModel
from django.urls import reverse


""" ============= Project Model =============== """
class Project(BaseModel):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=250)
    category = models.ForeignKey('ProjectCategory', on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name

class ProjectCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

""" ============= Project Image Model =============== """
class ProjectImage(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Image for {self.project.name}"
