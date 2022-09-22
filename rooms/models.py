from statistics import mode
from turtle import title
from django.db import models

# Create your models here.

class Room(models.Model):
    image = models.FileField(upload_to='null')
    title = models.CharField(max_length=150)
    create_ad = models.DateField(auto_now_add=True)
    update_ad = models.DateField(auto_now=True)