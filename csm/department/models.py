from django.db import models

# Create your models here.

from structure.models import *



class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True)
    wereda = models.ForeignKey(Wereda, on_delete=models.SET_NULL, null=True, blank=True)
    pull = models.ForeignKey(Pull, on_delete=models.SET_NULL, null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dept_name
    
    
class Position(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True)
    wereda = models.ForeignKey(Wereda, on_delete=models.SET_NULL, null=True, blank=True)
    position_name = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.position_name
    
class Service(models.Model):
    service_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True)
    wereda = models.ForeignKey(Wereda, on_delete=models.SET_NULL, null=True, blank=True)
    service_place = models.TextField()
    service_quality = models.TextField()
    service_status = models.TextField()
    service_requirement = models.TextField()
    service_fee = models.FloatField()
    service_time = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_name    