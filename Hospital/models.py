from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
       return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)

    def __str__(self):
       return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
       return self.doctor.name+"--"+self.patient.name

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id
    
class Bookings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    disease = models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    department=models.CharField(max_length=50)
    message=models.TextField(max_length=100)
    
    

    def __str__(self):
        return f"{self.user.username} - {self.doctor.name} "



class Order(models.Model) :
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=500,default="")
    city = models.CharField(max_length=50,default="")
    cars = models.CharField(max_length=50,default="")
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50,default="")
    loc_from = models.CharField(max_length=50,default="")
    loc_to = models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name