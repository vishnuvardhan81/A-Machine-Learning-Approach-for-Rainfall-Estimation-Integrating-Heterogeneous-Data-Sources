from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address= models.CharField(max_length=300)
    gender= models.CharField(max_length=30)

class rainfall_estimation(models.Model):

    Date1= models.CharField(max_length=300)
    Location= models.CharField(max_length=300)
    MinTemp= models.CharField(max_length=300)
    MaxTemp= models.CharField(max_length=300)
    Rainfall= models.CharField(max_length=300)
    Evaporation= models.CharField(max_length=300)
    Sunshine= models.CharField(max_length=300)
    WindGustDir= models.CharField(max_length=300)
    WindGustSpeed= models.CharField(max_length=300)
    WindDir= models.CharField(max_length=300)
    WindSpeed= models.CharField(max_length=300)
    Humidity= models.CharField(max_length=300)
    Pressure= models.CharField(max_length=300)
    Cloud= models.CharField(max_length=300)
    Temp= models.CharField(max_length=300)
    idnumber= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)



class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



