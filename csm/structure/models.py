from datetime import timezone
from django.db import models

# from user_managment.models import User

class Structure(models.Model):

    removed = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=255,  null=False,)
    amharic_name = models.CharField(max_length=255,  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
 
class Pull(models.Model):
    name = models.CharField(max_length=255)
    removed = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    amharic_name = models.CharField(max_length=255, blank=True)
    #managed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Organization(models.Model):
    removed = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    amharic_name = models.CharField(max_length=255, blank=True)
    structure = models.ForeignKey('Structure', on_delete=models.CASCADE)
    # managed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
class Subcity(models.Model):
    
    name = models.CharField(max_length=255)
    removed = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    amharic_name = models.CharField(max_length=255, blank=True)
    structure = models.ForeignKey('Structure', on_delete=models.CASCADE)
    # managed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pulls = models.ManyToManyField('Pull')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
		
		
class DepartmentType(models.Model):
 
        name = models.CharField(max_length=255, unique=True)
        amharic_name = models.CharField(max_length=255, blank=True)
        removed = models.BooleanField(default=False)
        enabled = models.BooleanField(default=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        
        def __str__(self):
            return self.name
		
		
class Division(models.Model):
    removed = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    amharic_name = models.CharField(max_length=255, blank=True, )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # managed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = (('name', 'organization'))		


class Department(models.Model):
    
        removed = models.BooleanField(default=False)
        enabled = models.BooleanField(default=True)
        name = models.CharField(max_length=255, blank=False, null=False, )
        amharic_name = models.CharField(max_length=255, blank=True, )
        department_type = models.ForeignKey(DepartmentType, on_delete=models.CASCADE)
        division = models.ForeignKey(Division, on_delete=models.CASCADE)
       # managed_by = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
        
            return self.name

        class Meta:
            ordering = ['name']
            unique_together = (('name', 'department_type', 'division'),)
	
		
		

		
class Region(models.Model):
    
        regionName = models.CharField(max_length=200)
        structureID = models.ForeignKey(Structure, on_delete=models.CASCADE, null=True)
        date_registered = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.regionName    


class Zone(models.Model):
    zoneName = models.CharField(max_length=100)
    regionID = models.ForeignKey(Region, on_delete=models.CASCADE)
    structureID = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, blank=True)
    date_registered = models.DateField()

    def __str__(self):
        return self.zoneName
    from django.db import models


class Wereda(models.Model):
    weredaName = models.CharField(max_length=100)
    regionID = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    zoneID = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True)
    date_registered = models.DateField()
    max = models.IntegerField()

    def __str__(self):
        return self.weredaName

