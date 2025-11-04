
""" ======== Imports ========= """
from django.db import models


""" ============= BaseModel ================ """

class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     Update_aat = models.DateTimeField(auto_now=True)
     is_actve = models.BooleanField(default=True)
     
     class Meta:
          abstract = True