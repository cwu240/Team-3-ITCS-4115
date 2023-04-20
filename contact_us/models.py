from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=2000,null=True,blank=True)
    email =  models.EmailField(max_length = 254)
    subject = models.CharField(max_length=2000,null=True,blank=True)
    message = models.CharField(max_length=2000,null=True,blank=True)
    
    