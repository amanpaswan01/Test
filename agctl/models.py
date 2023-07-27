from django.db import models

# Create your models here.
class ConnectedAgent(models.Model):
    client_channel_name =   models.CharField(max_length=255)
    group               =   models.CharField(max_length=10)
    ip_address          =   models.CharField(max_length=64)
    created_at          =   models.DateTimeField(auto_now_add=True)


class Device(models.Model):
    connection=models.ForeignKey(ConnectedAgent,on_delete=models.SET_NULL,null=True,blank=True)
    product_id=models.CharField(max_length=64)
    username=models.CharField(max_length=64)
    full_name=models.CharField(max_length=64)
    other_info=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)