from rest_framework import serializers
from flightApp.models import Flight,Passenger,Reservation

#Serializer converts DB info to JSON
#De-Serializer Converts JSON data to DB info

#note: Hence this serializers are used below

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields='__all__'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        #fields =['firstName','lastName','age','email','phoneNumber']
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        #fields = ['reservationNumber','flight','passenger']
        fields = '__all__'