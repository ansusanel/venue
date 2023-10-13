from django.db import models

# Create your models here.
class LocationTable(models.Model):
    street=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    image=models.ImageField(upload_to="imagefolder",default='null.jpg')
    state=models.CharField(max_length=20)


class VenueTable(models.Model):
    street=models.CharField(max_length=20,default='')
    VenuName=models.CharField(max_length=20,default='')
    VenuType=models.CharField(max_length=20,default='')
    VenuOwner=models.CharField(max_length=20)
    VenuNumber=models.IntegerField(default=0)
    VenuDescription=models.CharField(max_length=20,default='')
    image=models.ImageField(upload_to="imagefolder",default='null.jpg')

class ManagerTable(models.Model):
    VenuName=models.CharField(max_length=20)
    ManagerName=models.CharField(max_length=20)
    ManagerPlace=models.CharField(max_length=20)
    ManagerNumber=models.IntegerField()