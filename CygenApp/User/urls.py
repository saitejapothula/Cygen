from django.urls import path, include
from .views import *
urlpatterns = [
    path('Register/', RegisterAPI.as_view(), name='Register the user'),
    path('GetUserData/', GetUserList.as_view(), name='Get the user data'),
    path("CreateUserAppointment/", CreateUserAppointment.as_view(), name="create an appointment by user"),
    path('GetAppointments/', GetAppointments.as_view(), name="get all the userappointment"),
    ]