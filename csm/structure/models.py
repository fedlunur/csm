from django.db import models

# Create your models here.
class Structure(models.Model):
    structureName = models.CharField(max_length=200)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.structureName
 
class Pull(models.Model):
    pullName = models.CharField(max_length=200)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pullName
class Region(models.Model):
    regionName = models.CharField(max_length=200)
    structureID = models.ForeignKey(Structure, on_delete=models.CASCADE, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.regionName    
    
from django.db import models
from .models import Region, Structure  # Import the Region and Structure models if they are defined in the same app

class Zone(models.Model):
    zoneName = models.CharField(max_length=100)
    regionID = models.ForeignKey(Region, on_delete=models.CASCADE)
    structureID = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, blank=True)
    date_registered = models.DateField()

    def __str__(self):
        return self.zoneName
    from django.db import models
from .models import Region, Zone  # Import the Region and Zone models if they are defined in the same app

class Wereda(models.Model):
    weredaName = models.CharField(max_length=100)
    regionID = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    zoneID = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True)
    date_registered = models.DateField()
    max = models.IntegerField()

    def __str__(self):
        return self.weredaName
