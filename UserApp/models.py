from django.db import models
from AdminApp.models import*

# Create your models here.
class Contacttable(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.CharField(max_length=20)


class Registertable(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    number=models.IntegerField(default=0)
    password=models.CharField(max_length=20)


class Booktable(models.Model):
    u_id=models.ForeignKey(Registertable,on_delete=models.CASCADE,null=True,blank=True)
    Venu_id=models.ForeignKey(VenueTable,on_delete=models.CASCADE,null=True)
    function=models.CharField(max_length=50,default='')
    date=models.DateField(null=True,blank=True)
    starttime=models.TimeField(null=True,blank=True)
    endtime=models.TimeField(null=True,blank=True)