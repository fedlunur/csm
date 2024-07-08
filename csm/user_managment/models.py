from django.db import models
from django.db.models.signals import post_save # helps 
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class User(AbstractUser):
   
    first_name = models.CharField(max_length=1000,null=True)
    middle_name=models.CharField(max_length=1000,null=True)
    last_name=models.CharField(max_length=1000,null=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    pullID = models.IntegerField(null=True, blank=True)
    org = models.CharField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey('Zone', on_delete=models.SET_NULL, null=True, blank=True)
    wereda = models.ForeignKey('Wereda', on_delete=models.SET_NULL, null=True, blank=True)
 
   





    USERNAME_FIELD = 'email' # make the default email as user name 
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username
    
    # def profile(self):
    #     profile = Profile.objects.get(user=self)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.first_name

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
  

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
