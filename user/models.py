from django.db import models

# Create your models here.
class User(models.Model):
    icon = models.CharField(max_length=10)
    heding = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)

class Counts(models.Model):
    number = models.CharField(max_length=30)
    name = models.CharField(max_length=200)

class Items(models.Model):
    itemimage = models.ImageField(upload_to='images/')  
    itemname = models.CharField(max_length=30)
    itemabout = models.CharField(max_length=50)
    itemprice = models.CharField(max_length=20)

class Chef(models.Model):
    about = models.CharField(max_length=3000)
    chefname = models.CharField(max_length=30)
    postion = models.CharField(max_length=30)
    chefimage = models.CharField(max_length=20)

class Party(models.Model):
    pryimg = models.CharField(max_length=10)
    pryname = models.CharField(max_length=30)
    pryamount = models.CharField(max_length=30)
    pryabout = models.CharField(max_length=2000)

class Chefs(models.Model):
    chefimg = models.CharField(max_length=3000)
    chefsname = models.CharField(max_length=30)
    chefpostion = models.CharField(max_length=30)
    chefinfo = models.CharField(max_length=20)

class Gimg(models.Model):
    galleryimg = models.CharField(max_length=30)
