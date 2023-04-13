from django.db import models

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