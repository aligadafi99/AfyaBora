from django.contrib import admin
from .models import *
# Register your models here.  Car, Order

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Bookings)

admin.site.register(Order)
