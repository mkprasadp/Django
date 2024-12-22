from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse


def webpage(request):
    return  HttpResponse('<h1 style="color:blue">Padala Manikanta Prasad</h1>')