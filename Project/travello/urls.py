from django.contrib import admin
from django.urls import path
from .views import travello,travello1

urlpatterns = [
    path('travello/',travello,name='travello'),
    path('travello1/',travello1,name='travello1')
]