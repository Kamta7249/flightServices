from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    # departureCity = models.CharField(max_length=20) or
    departureCity = models.CharField(max_length=20,blank=True,null=True)   
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatdTimeOfDeparture = models.TimeField()

class Passenger(models.Model):
    firstName = models.CharField(max_length=25)
    middleName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

class Reservation(models.Model):
    #ForeignKey is many to one Relationship with Reservation and Flight
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE) 
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)