from django.shortcuts import render
from django.http import JsonResponse
from flightApp.models import Flight,Passenger,Reservation
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes # used for function based views
from rest_framework.views import APIView #used for class based views
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework import generics,mixins #used for mixins
from rest_framework import viewsets
from rest_framework import filters # this has the search filter class inside it
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
# Create your views here.

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))#this line is used to provide permission on function based views
def find_flights(request): 
    #flightss is the list of flight objects
    flights = Flight.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'],dateofDeparture=request.data['dateofDeparture'])
    #serializer contains the list of flights meeting the filter criteria which will be converted into json format from DB
    serializer = FlightSerializer(flights, many=True)
    #the serializer will return the data in form of http resposne
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))#this line is used to provide permission on function based views
def save_reservations(request):
    #get the flightId from the request
    flight = Flight.objects.get(id=request.data['flightId'])# this will give us one specific flight that we want to reserve
    
    #we assign all the values to the passenger object
    #set all the fields on the passenger
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.age = request.data['age']
    passenger.email = request.data['email']
    passenger.phoneNumber = request.data['phoneNumber']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    Reservation.save(reservation)
    return Response(status=status.HTTP_201_CREATED)

class UserPagination(PageNumberPagination):
    page_size=5

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()#gathers all the objects from Flight model
    #it tells which serializer class should be used
    serializer_class = FlightSerializer
    pagination_class = UserPagination#custom is used 
    #filter_backends = [DjangoFilterBackend] # it will create a filterset object for us which will do the filtering for us
    #filterset_fields = ['flightNumber', 'operatingAirlines'] # based on which fields the client will do the filtering
    filter_backends = [filters.SearchFilter]
    search_fields = ['^operatingAirlines', '=flightNumber', '^departureCity','^arrivalCity', '=dateofDeparture','=timeofDeparture']

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()#gathers all the objects from Flight model
    #it tells which serializer class should be used
    serializer_class = PassengerSerializer
    pagination_class = PageNumberPagination#default is used from settings  
    filter_backends = [filters.SearchFilter]
    search_fields = ['^firstName', '=email', '^lastName','^arrivalCity', '=phoneNumber']

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()#gathers all the objects from Flight model
    #it tells which serializer class should be used
    serializer_class = ReservationSerializer


#Generic Views
"""
#Non-Primary key based operations
class UserList(generics.ListCreateAPIView):
    # it tells the mixin which model should be used
    queryset = User.objects.all()
    #it tells which serializer class should be used
    serializer_class = UserSerialzier
class CarList(generics.ListCreateAPIView):
    # it tells the mixin which model should be used
    queryset = Car.objects.all()
    #it tells which serializer class should be used
    serializer_class = CarSerialzier
#primary key based operations
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    # it tells the mixin which model should be used
    queryset = User.objects.all()
    #it tells which serializer class should be used
    serializer_class = UserSerialzier    
class CarDetails(generics.RetrieveUpdateDestroyAPIView):
    # it tells the mixin which model should be used
    queryset = Car.objects.all()
    #it tells which serializer class should be used
    serializer_class = CarSerialzier   
"""

# It is used for Mixins, It basically reduces the liens of code that is used for Class based and function based views
"""
class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # it tells the mixin which model should be used
    queryset = User.objects.all()
    #it tells which serializer class should be used
    serializer_class = UserSerialzier
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class UserDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    # it tells the mixin which model should be used
    queryset = User.objects.all()
    #it tells which serializer class should be used
    serializer_class = UserSerialzier
    def get(self, requst, pk):
        return self.retrieve(requst, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
"""


# It is used for class based View, works same as function based views

"""
class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerialzier(users, many = True)
        return Response(serializer.data)
    
    def post(self, request):
         #it converts the json data to post it in the DB
        serializer = UserSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class UserDetails(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerialzier(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerialzier(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


# It is used for fucntion based views
"""
def userView(request):
    #static user object which is returned as a JSON
    #dictionary in Python is like hashmap of Java
    # usr = {
    #     'id':1,
    #     'name':'Tester1',
    #     'age': 24,
    #     'profession':'Developer',
    #     'sal':1000000,
    #     'email':'tester1@gmail.com'
    # }
    data = User.objects.all();#fetch all the records in the database
    # we return a dictionaly as it may contain multiple users
    # here user is the json key
    response = {'user':list(data.values('name','sal', 'age', 'profession', 'email'))}
    #return JsonResponse(usr)
    return JsonResponse(response)
@api_view(['GET','Post'])
def user_list(request):
    if request.method == 'GET':
        #users is the list of student objects
        users = User.objects.all() # it will give us all the user records
        #serializer contains the list of students which will be converted into json format from DB
        serializer = UserSerialzier(users, many = True )
        #the serializer will return the data in form of http resposne
        return Response(serializer.data)
    
    elif request.method == 'POST':
        #it converts the json data to post it in the DB
        serializer = UserSerialzier(data = request.data)
        if serializer.is_valid():
            #save the data in the DB
            serializer.save()
            #return the status and the data
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def user_details(request, pk):
    try:
        #we retrieve a single student using the primary key
        user = User.objects.get(pk=pk)
    except User.DoesNotExist :
        # if not founnd then show the status
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =  UserSerialzier(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerialzier(user, data=request.data)
        # it checks if the data already exists or not
        if serializer.is_valid():
            #update the data
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""