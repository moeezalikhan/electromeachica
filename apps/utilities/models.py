
""" ======== Imports ========= """
from django.db import models


""" ============= BaseModel ================ """

from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # fixed typo
    is_active = models.BooleanField(default=True)     # fixed typo

    class Meta:
        abstract = True
