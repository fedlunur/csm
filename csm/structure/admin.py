from django.contrib import admin
from .models import *
# Register your models here.
class  StructureAdmin(admin.ModelAdmin):
 
         def get_list_display(self, request):
          return [field.name for field in self.model._meta.fields]
    
     
admin.site.register(Structure,StructureAdmin)    

class  RegionAdmin(admin.ModelAdmin):
 
         def get_list_display(self, request):
          return [field.name for field in self.model._meta.fields]
   
admin.site.register( Region, RegionAdmin)    

class ZoneAdmin(admin.ModelAdmin):
 
         def get_list_display(self, request):
          return [field.name for field in self.model._meta.fields]
   
admin.site.register( Zone, ZoneAdmin)    

class WeredaAdmin(admin.ModelAdmin):
 
         def get_list_display(self, request):
          return [field.name for field in self.model._meta.fields]
   
admin.site.register( Wereda, WeredaAdmin)    

 

class PullAdmin(admin.ModelAdmin):
 
         def get_list_display(self, request):
          return [field.name for field in self.model._meta.fields]
   
admin.site.register( Pull, PullAdmin)    