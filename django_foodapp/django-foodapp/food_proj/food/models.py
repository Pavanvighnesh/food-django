from django.db import models

# Create your models here.
class item(models.Model):
    item_name=models.CharField(max_length=220)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField(default=0)
    item_image=models.CharField(max_length=500,default='https://lh3.googleusercontent.com/RLo2nYsnoSNTVTCZoiRslZwFtt3FFCFZZG1wVPTAVgZ60P5thfiEWMuGesDHqOff983Z=w170')


    def __str__(self):
     return self.item_name



