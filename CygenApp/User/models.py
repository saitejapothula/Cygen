from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
class UserModel(models.Model):
    firstname_regex = RegexValidator(regex=r'[A-Za-z]{3}([A-Za-z]+ ?)*',
                                     message="firstname "
                                             "must string and should not be less than 3 and greater than 12")
    lastname_regex = RegexValidator(regex=r'[A-Za-z]{3}([A-Za-z]+ ?)*',
                                    message="lastname "
                                            "must string and should not be less than 3 and greater than 12")
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")
    Firstname = models.CharField(max_length=30, null=True, default=None, blank=True, validators=[firstname_regex])
    Lastname = models.CharField(max_length=30, null=True, default=None, blank=True, validators=[lastname_regex])
    Email = models.EmailField(max_length=50, null=True, default=None, blank=True)
    Username = models.CharField(max_length=60, unique=True, null=True, default=None, blank=True)
    Password = models.CharField(max_length=50, null=True, default=None, blank=True, validators=[password_regex])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    DeviceToken = models.CharField(max_length=255, default=None)
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "User_Data"
        
        
class Symptoms(models.Model):
    Symptom = models.CharField(max_length=250)
    comments = models.TextField()
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.manager

    class Meta:
        db_table = "symptomtable"


class AppointmentModel(models.Model):
    class Status(models.TextChoices):
        CREATED = 'CREATED'
        CONFIRMED = 'CONFIRMED'
        ACCEPTED = 'ACCEPTED'
        CANCELLED = 'CANCELLED'
        COMPLETED = 'COMPLETED'
        PENDING = 'PENDING'


    UserId = models.ForeignKey('User.UserModel', related_name='appointment', on_delete=models.CASCADE)
    DoctorId = models.ForeignKey('Doctor.DoctorModel', related_name='Appointments', on_delete=models.CASCADE)
    ScheduleId = models.ForeignKey('Doctor.DoctorScheduler', related_name='Scheduleid', on_delete=models.CASCADE,
                                   null=True)
    Date = models.DateField()
    Time = models.TimeField()
    Specialization = models.CharField(max_length=200)
    CurrentDate = models.DateTimeField(auto_now_add=True)
    Fees = models.IntegerField(default=None)
    symptoms = models.ForeignKey('Symptoms', related_name='symptoms_id', on_delete=models.CASCADE, default=None,
                                 null=True)
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "User_Appointment"
