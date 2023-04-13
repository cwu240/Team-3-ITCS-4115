from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ticket_purchased_time = models.DateTimeField(auto_now =True)
    json_ticket_data = models.CharField(max_length=2000,null=True,blank=True)
    