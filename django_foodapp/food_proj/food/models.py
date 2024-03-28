from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class item(models.Model):
    item_name=models.CharField(max_length=220)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField(default=0)
    item_image=models.CharField(max_length=500,default='https://lh3.googleusercontent.com/RLo2nYsnoSNTVTCZoiRslZwFtt3FFCFZZG1wVPTAVgZ60P5thfiEWMuGesDHqOff983Z=w170')


    def __str__(self):
     return self.item_name

class profile(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   
   image_field=models.ImageField(default='profile.jpg',upload_to='profile_pictures')  
   location=models.CharField(max_length=250)


   def __str__(self):
      return self.user.username 



