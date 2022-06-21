from dataclasses import fields
from HealthCenter.models import Appointment
from django import forms
from .models import  Number_store

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'


class  Number_store(forms.Form):
	class meta:
		model =  Number_store
		fields = '__all__' 