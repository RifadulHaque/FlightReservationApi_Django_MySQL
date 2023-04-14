from django.db import models
from django.db.models.signals import post_save # signal we will receive
from django.dispatch import receiver # it is reciever which is a decprator
from rest_framework.authtoken.models import Token # model object Token
from django.conf import settings

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length= 10)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=15)
    arrivalCity = models.CharField(max_length=15)
    dateofDeparture = models.DateField()
    timeofDeparture = models.TimeField()

        #returns the string represenation of the object when the object is called
    def __str__(self):
        return 'flightNumber: '+self.flightNumber+', operatingAirlines: '+self.operatingAirlines+', departureCity: '+self.departureCity+ ', arrivalCity: '+self.arrivalCity+', dateofDeparture: '+str(self.dateofDeparture)+', timeofDeparture: '+str(self.timeofDeparture)

class Passenger(models.Model):
    firstName=models.CharField(max_length= 10)
    lastName=models.CharField(max_length= 10)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    phoneNumber=models.CharField(max_length= 10)

     #returns the string represenation of the object when the object is called
    def __str__(self):
        return 'firstName: '+self.firstName+', age: '+str(self.age)+', lastName: '+self.lastName+ ', phoneNumber: '+self.phoneNumber+', email: '+self.email

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

#this is a reciever of signal
@receiver(post_save,sender = settings.AUTH_USER_MODEL) #when a authentication user is used in a databse
def createAuthToken(sender, instance, created,**kwargs):
    if created:
        Token.objects.create(user=instance)