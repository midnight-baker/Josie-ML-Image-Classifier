"""
Definition of models.
"""

from django.db import models

class YourModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

# Create your models here.
