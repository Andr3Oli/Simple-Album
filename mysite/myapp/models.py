from django.db import models

# Create your models here.
import datetime
import os

class Photo(models.Model):
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)