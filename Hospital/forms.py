from django.forms import ModelForm
# your_app/forms.py
from django import forms
from .models import Bookings, Doctor
class AppointmentForm(forms.ModelForm):
   class Meta:
       model = Bookings
       fields = ['doctor', 'disease', 'email','phone','department','message']

   def __init__(self, *args, **kwargs):
       super(AppointmentForm, self).__init__(*args, **kwargs)
        # You can customize the doctor field widget to display a dropdown/select input
       self.fields['doctor'].widget = forms.Select(choices=Doctor.objects.all().values_list('id', 'name'))
