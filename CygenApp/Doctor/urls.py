from django.urls import path
from .views import *
urlpatterns = [
    path('Register/', RegisterAPI.as_view(), name='Register the doctor'),
    path('DoctorSchedulerRegAPI/', DoctorSchedulerRegAPI.as_view(), name="create doctor scheduler"),    
]