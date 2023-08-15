from dataclasses import fields
from HealthCenter.models import Appointment
from django import forms


class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

        # fields=['name', 'email', 'date', 'department', 'mobileno', 'msg']


