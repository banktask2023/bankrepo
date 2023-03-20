from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=50)
    cpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class district(models.Model):
    districtname = models.CharField(max_length=100)

    class Meta:
        db_table = 'bankapp_district'

    def __str__(self):
        return self.districtname

class city(models.Model):
    distid = models.ForeignKey(district, on_delete=CASCADE)
    cityname = models.CharField(max_length=100)
    cityname1 = models.CharField(max_length=100)
    cityname2 = models.CharField(max_length=100)

    class Meta:
        ordering = 'cityname',
        db_table = 'CITY'

    def __str__(self):
        return self.cityname

class Application(models.Model):
    aname = models.CharField(max_length=100)
    adob = models.DateField()
    aage = models.CharField(max_length=50)

    def __str__(self):
        return self.aname