# FlightReservationApi_Django_Angular_MySQL

Summary:
This is basically a Flight Reservation API which is used to reserve flights for clients depending on flight destination, arrival and date.
The logged in authority can post flights and passengers in the system, if the authority has the permission then he/she can also delete users and flights and also reservations. Even if the permission is given the updates on each of the service is also possible. The super user has all the permissions.


Password for the databse is not given yet.

Default path:
http://localhost:8000/api/

Note: Check this link for setting permissions
http://localhost:8000/admin/auth/
User:
username:Tester1
password:djangotest1

Note: for authentication and Security : POST - http://localhost:8000/api-token-auth/
User:
username:Tester1
password:djangotest1

NOTE: Post fligts
POST http://localhost:8000/api/flights/

NOTE : Get al flights
GET http://localhost:8000/api/flights/

NOTE: Find flights:
POST http://localhost:8000/api/flights/

NOTE: save reservation
POST http://localhost:8000/api/saveReservation/

first to start the project :

Step1: create virtual env
-python -m venv venv
-source venv/Scripts/activate (prefer to do it in gitbash)

  Extra for everytime we start the vscode: activate the veirtual env
  - source venv/Scripts/activate

step2:
-django-admin startproject <name of the project without spaces>
  in our case it is userProject

Step-3: to create apps inside the project
-pytho3 manage.py startapp <name of the app without spaces>
    in our case it is userApp

Step-4:
-add the two names in the INSTALLED_APPS
        'rest_framework',
        'userApp'

Step-5:
create the view/Rest endPoint (this is the service for Spring boot)
 import: from django.http import JsonResponse

Step-5:
-add the endPoint URL in the url.py and mention the view that it relates and Test it
   ex:  path('',views.userView)

Extra info:
 For connecting to the mysql database:
  - go to setting of the project
  - seach for databases- change it sqlit to mysql
  - add the NAME(name of the database), USER(root) and PASSWORD(mysql password)

Extra step for SQL: used to do database migration to Mysql
- pyhton3 manage.py makemigrations   (It craetes the MYSQL table for User Model)
- python3 manage.py migrate          (It applies all the migration)

Step-6: run the python server
- python3 manage.py runserver

Step-7: create app level url
- copy the url.py from the userProject to the userApp and remove the admin level permission and the url for admin
- add the view for the userApp in the userApp url
- in the django.urls import include and add this 
- path('userApp/',include('userApp.urls')) - this will add all the urls from the userApp


--------------------------------------------------------------------
