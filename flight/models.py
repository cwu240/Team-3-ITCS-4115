from django.db import models

# Create your models here.
class MyModelName(models.Model):
    flight = models.CharField(max_length=1000, help_text='xx')
    passenger = models.CharField(max_length=1000, help_text='xx')