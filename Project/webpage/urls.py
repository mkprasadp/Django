from django.contrib import admin
from django.urls import path
from .views import webpage

urlpatterns = [
    path('webpage.html/',webpage,name='Webpage'),
]
