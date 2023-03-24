from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AndroidApp(models.Model):
    name = models.CharField(max_length=255)
    download_link = models.URLField()
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class UserPoints(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    android_app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)
    points = models.IntegerField()



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=100)
    link = models.URLField()
    points = models.IntegerField()