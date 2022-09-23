from statistics import mode
from turtle import title
from django.db import models

# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to='rooms')    
    create_ad = models.DateField(auto_now_add=True)
    update_ad = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return self.title