from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# for user authticcation 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import AppointmentForm
from .models import Bookings,  Order



def choose_doctor(request):
   if request.method == 'POST':
       form = AppointmentForm(request.POST)
       if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('home')  # Create a success_page view
   else:
        form = AppointmentForm()

        appointments = Bookings.objects.filter(user=request.user)

        return render(request, 'choose_doctor.html', {'form': form, 'appointments': appointments})

# Create your views here.
def  admin_panel(request):
    return render(request , "admin_panel.html")


def  dashboard(request):
    return render(request , "dashboard.html")

def  home(request):
    return render(request , "index.html")


def signUp(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        fpass = request.POST.get("pass1")
        cpass = request.POST.get("pass2")
        

        # validation for user
        if User.objects.filter(username=uname):
            messages.error(request,"Username already exist!")
            return redirect('signUp')

        if User.objects.filter(email=email):
            messages.error(request,"email already registerd")
            return redirect('signUp')

        if len(uname) >10:
            messages.error(request,"the username must be under 10 character!")
            return redirect('signUp')

        if fpass != cpass:
            messages.error(request,"Passwords didn't match.Try agian!")
            return redirect('signUp')

        if not uname.isalnum():
            messages.error(request,"Username must be alpha-numeric!")
            return redirect('signUp')

        my_user = User.objects.create_user(uname,email,fpass)
        my_user.first_name = fname
        my_user.last_name = lname

        my_user.save()

        messages.success(request, 'Thank you! your account has been successfully created.')

        return redirect('login')

    return render(request,'signUp.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass1")
        doc_pat = request.POST.get("doc_pat")

        user = authenticate(request, username = username, password = password)
        if user is not None:
            authlogin(request, user)
            fname = user.first_name
            messages.success(request,' Adminsuccessfully logged in ')
            
            return render(request, 'admin_home.html', {'fname':fname})
 
        else:
            messages.error(request, ' Username or Password did not match. Try aging.')
            return redirect('admin_login')


    return render(request,'login.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass1")
        doc_pat = request.POST.get("doc_pat")

        user = authenticate(request, username = username, password = password)
        if user is not None:
            authlogin(request, user)
            fname = user.first_name
            messages.success(request,' Your are successfully logged in ')
            
            return render(request, 'dashboard.html', {'fname':fname})
 
        else:
            messages.error(request, ' Username or Password did not match. Try aging.')
            return redirect('login')


    return render(request,'login.html')

def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect('home')


def add_patient(request):
   
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a)
            error = "no"
        except:
            error = "yes"
    return render(request,'add_patient.html', locals())

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html', d)


def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient.html')

def edit_patient(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    patient = Patient.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        g1 = request.POST['gender']
        a1 = request.POST['address']

        patient.name = n1
        patient.mobile = m1
        patient.gender = g1
        patient.address = a1
        try:
            patient.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_patient.html', locals())




def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    dc = Doctor.objects.all().count()
    pc = Patient.objects.all().count()
    ac = Appointment.objects.all().count()

    d = {'dc': dc, 'pc': pc, 'ac': ac}
    return render(request,'admin_home.html', d)


def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html', d)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    d = {'appointment':appointment}
    return render(request,'view_appointment.html', d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment1 = Appointment.objects.get(id=pid)
    appointment1.delete()
    return redirect('view_appointment.html')


def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=m,special=sp)
            error="no"
        except:
            error="yes"
    return render(request,'add_doctor.html', locals())

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html', d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor.html')

def edit_doctor(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    doctor = Doctor.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        s1 = request.POST['special']

        doctor.name = n1
        doctor.mobile = m1
        doctor.special = s1

        try:
            doctor.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_doctor.html', locals())


def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname','')
        billemail = request.POST.get('billemail','')
        billphone = request.POST.get('billphone','')
        billaddress = request.POST.get('billaddress','')
        billcity = request.POST.get('billcity','')
        cars11 = request.POST['cars11']
        dayss = request.POST.get('dayss','')
        date = request.POST.get('date','')
        fl = request.POST.get('fl','')
        tl = request.POST.get('tl','')
        
        
        order = Order(name = billname,email = billemail,phone = billphone,address = billaddress,city=billcity,cars = cars11,days_for_rent = dayss,date = date,loc_from = fl,loc_to = tl)
        order.save()
        return redirect('home')
    else:
        print("error")
        return render(request,'bill.html')