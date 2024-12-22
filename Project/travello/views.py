from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

def travello(request):
    return redirect(reverse('travello1'))

def travello1(request):
    return render(request,'travello.html')