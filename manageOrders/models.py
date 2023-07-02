from django.db import models
# Create your models here.
# Tutorial!



class Clients(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=7)

class Articles(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()

class Orders(models.Model):
    number= models.IntegerField()
    date=models.DateField()
    delivered=models.BooleanField()
