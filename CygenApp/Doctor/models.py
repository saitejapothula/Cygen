from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
class DoctorModel(models.Model):
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
        db_table = "Doctor_Data"
        
class DoctorScheduler(models.Model):
    DId = models.OneToOneField('Doctor.DoctorModel', on_delete=models.CASCADE, related_name='Schedule')
    FromDate = models.DateField()
    ToDate = models.DateField()
    FromTIme = models.TimeField(default=None)
    ToTime = models.TimeField()
    Fees = models.IntegerField(blank=True, default=None)
    CurrentDate = models.DateTimeField(auto_now_add=True)
    AppointmentType = models.CharField(max_length=250, default=None)
    Fees = models.IntegerField(default=None)
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "Doctor_Scheduler"
