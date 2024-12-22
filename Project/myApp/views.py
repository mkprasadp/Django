from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages
import csv

def Home1(request):
    return redirect(reverse('Home'))

def Home(request):
    return render(request,'Home.html',{'Homepage':"Welcome Home"})


@csrf_exempt
def Loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        if not email or not password:
            return render(request,'Loginpage.html',{'error':'Email and Password cannot be empty'})
        
        csv_file_path = '' # write your file path and create data.csv

        with open(csv_file_path,mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['email'] == email and row['password'] == password:
                    # Store email in session and redirect to the logout page
                    request.session['email'] = email
                    Home = reverse('Home')
                    Loginpage = reverse('Loginpage')
                    return render(request, 'logout.html', {'email': email, 'Home': Home, 'Loginpage': Loginpage})
        # If no match is found in the CSV
        return render(request, 'Loginpage.html', {'error': 'Invalid Email or Password'})
    else:
        return render(request,'Loginpage.html')
    


@csrf_exempt
def Registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        dob = request.POST.get('DOB')

        if not all([name, email, password, dob]):
            return render(request, 'Registration.html', {'error': 'All fields are required'})
        
        csv_file_path = '' # write your file path and create data.csv

        with open(csv_file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['email'] == email:
                    return render(request, 'Registration.html', {'errors': 'Email is already registered'})
                elif row['name'] == name:
                    return render(request,'Registration.html', {'errors':'Name is already registered'})
                
        with open(csv_file_path, mode='a', newline='') as file:
            fieldnames = ['name', 'email', 'password', 'dob']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                'name': name, 
                'email': email, 
                'password': password,
                'dob': dob
                })
        return redirect(reverse('Loginpage'))
    else:
        return render(request, 'Registration.html')

def Forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if not email:
            return render(request, 'Forgot_password', {'error':'Email is required'})


@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        data = request.POST.get('name')
        return HttpResponse(f'<h1 style="color:red">{data}</h1>')
    else:
        return render(request,'form.html')