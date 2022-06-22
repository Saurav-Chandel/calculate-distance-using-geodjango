from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.gis.db.models import PointField
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models
from django.contrib.gis.db import models as giomodels

class Distance(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200,null=True,blank=True)
    # lat=models.CharField(max_length=200,null=-True,blank=True)
    # lon=models.CharField(max_length=200,blank=True,null=True)
    point = giomodels.PointField(srid=4326,null=True,blank=True)
    # objects = models.GeoManager()


    # def __str__(self):
    #     return self.address
    