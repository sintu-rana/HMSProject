from django.shortcuts import render, redirect
from HealthCenter.forms import AppointmentForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def view_home(request):
    resp=render(request,'HealthCenter/home.html')
    return resp


@login_required(login_url='/login/')
def view_about(request):
    resp=render(request,'HealthCenter/about.html')
    return resp

@login_required(login_url='/login/')
def view_doctor(request):
    resp=render(request,'HealthCenter/doctor.html')
    return resp

@login_required(login_url='/login/')
def view_news(request):
    resp=render(request,'HealthCenter/news.html')
    return resp

@login_required(login_url='/login/')
def view_contact(request):
    resp=render(request,'HealthCenter/contact.html')
    return resp

@login_required(login_url='/login/')
def view_appointment(request):
    if request.method=='GET':
        frm_unbound=AppointmentForm()
        d1={'forms':frm_unbound}
        resp=render(request,'HealthCenter/appointment.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=AppointmentForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("<h1>Appointment Saved SuccessFully!!!</h1>")



def view_register(request):
    
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username is already taken")
            return redirect('/login_register/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
            )
        
        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully")

        return redirect('/')
    return render(request , 'HealthCenter/register.html')


def view_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/HealthCenter/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/HealthCenter/login/')
        
        else:
            login(request, user)
            return redirect('/')
        

    return render(request , 'HealthCenter/login.html')


def view_logout(request):
    logout(request)
    return redirect('/login/')