from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('myApp.urls')),
    path('webApp/',include('travello.urls')),
    path('Manikanta/',include('webpage.urls')),
]