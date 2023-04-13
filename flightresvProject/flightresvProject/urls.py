"""flightresvProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from flightApp import views
from rest_framework.routers import DefaultRouter

#used for mixins, generics, viewSets
router= DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passenger', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/',include('flightApp.urls')),
    path('api/', include(router.urls)),
    path('api/findFlights/', views.find_flights),
    path('api/saveReservation/', views.save_reservations)
]