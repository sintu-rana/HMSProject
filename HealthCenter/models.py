from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
dept=[
    ('General Health','General Health'),
    ('Cardiology','Cardiology'),
    ('Dental','Dental'),
    ('Medical Research','Medical Research'),
]

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    date=models.DateField(default=date.today)
    department=models.CharField(max_length=40,choices=dept)
    mobileno=models.CharField(max_length=15)
    msg=models.TextField()
    def __str__(self):
        return self.name

