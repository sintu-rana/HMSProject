from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['name','email','date','department','mobileno','msg']



@admin.register(Number_store)
class Number_storeAdmin(ImportExportModelAdmin):
    pass