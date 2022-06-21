from django.db import models

# Create your models here.
dept=[
    ('General Health','General Health'),
    ('Cardiology','Cardiology'),
    ('Dental','Dental'),
    ('Medical Research','Medical Research'),
]

class Appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    date=models.DateField()
    department=models.CharField(max_length=40,choices=dept)
    mobileno=models.CharField(max_length=15)
    msg=models.TextField()
    def __str__(self):
        return self.name
        
#xlsx file upload

class Number_store(models.Model):
    Date=models.DateField(max_length=15)
    Solar_Generation_MU=models.ImageField()
    class Meta:
        db_table='Number_store'


