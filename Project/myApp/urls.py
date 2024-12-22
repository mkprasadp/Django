from django.contrib import admin
from django.urls import path
from .views import Home,Loginpage,Registration,Forgot_password,submit_form,Home1

urlpatterns = [
    path('',Home1,name='Home'),
    path('submit/', submit_form, name='submit_form'),
    path('Home/',Home,name='Home'),
    path('Loginpage/',Loginpage, name='Loginpage'),
    path('Registration/',Registration,name='Registration'),
    path('Forgot_password/',Forgot_password,name='Forgot_password')
]