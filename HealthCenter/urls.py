from django.urls import path
from .views import *

#Base URL = http://127.0.0.1:8000/hms/

urlpatterns=[
    
   path('',view_home,name='home'),
   path('task/',view_task,name='task'),
   path('about/',view_about,name='about'),
   path('doctor/',view_doctor,name='doctor'),
   path('news/',view_news,name='news'),
   path('contact/',view_contact,name='contact'),
   path('appointment/',view_appointment,name='appointment'),
]