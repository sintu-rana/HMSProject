from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['name','email','date','department','mobileno','msg']



