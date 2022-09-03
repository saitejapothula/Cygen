from rest_framework import serializers
from .models import DoctorModel, DoctorScheduler
from django.contrib.auth.hashers import make_password

class DoctorRegSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorModel
        fields = ['id', 'Firstname', 'Lastname', 'Email', 'Username', 'Password', 'MobileNumber', 'DeviceToken']
        extra_kwargs = {'Password': {'write_only': True}, }

    def create(self, validated_data):
        doctor = DoctorModel.objects.create(Firstname=validated_data['Firstname'], Lastname=validated_data['Lastname'],
                                        Email=validated_data['Email'], Username=validated_data['Username'],
                                        Password=make_password(validated_data['Password']),
                                        MobileNumber=validated_data['MobileNumber'],
                                        DeviceToken=validated_data['DeviceToken'])

        doctor.save()
        return doctor
    
class DoctorAppointSerializers(serializers.ModelSerializer):

    class Meta:
        model = DoctorScheduler
        fields = ['id', 'DId', 'FromDate', 'ToDate', 'FromTIme', 'ToTime', 'Fees']

    def create(self, validated_data):
        user = DoctorScheduler.objects.create(DId=validated_data['DId'], FromDate=validated_data['FromDate'],
                                           ToDate=validated_data['ToDate'],
                                           FromTIme=validated_data['FromTIme'], ToTime=validated_data['ToTime'],
                                           Fees=validated_data["Fees"])
        user.save()
        return user