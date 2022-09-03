from rest_framework import serializers
from django.apps import apps
from .models import UserModel, Symptoms, AppointmentModel
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id', 'Firstname', 'Lastname', 'Email', 'Username', 'MobileNumber','DeviceToken']

class UserRegSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id', 'Firstname', 'Lastname', 'Email', 'Username', 'Password', 'MobileNumber', 'DeviceToken']
        extra_kwargs = {'Password': {'write_only': True}, }

    def create(self, validated_data):
        user = UserModel.objects.create(Firstname=validated_data['Firstname'], Lastname=validated_data['Lastname'],
                                        Email=validated_data['Email'], Username=validated_data['Username'],
                                        Password=make_password(validated_data['Password']),
                                        MobileNumber=validated_data['MobileNumber'],
                                        DeviceToken=validated_data['DeviceToken'])

        user.save()
        return user
    


class Symtomsserializer(serializers.ModelSerializer):
    class Meta:
        model = Symptoms
        fields = ['Symptom', 'comments']

class NewAppointmentSerializer(serializers.ModelSerializer):
    symptoms = Symtomsserializer()


    class Meta:
        model = AppointmentModel
        fields = ['id','Date', 'Time', 'Specialization', 'Fees', 'UserId','DoctorId',
                  'ScheduleId', 'symptoms']

    def create(self, validated_data):
        b = validated_data.pop('symptoms')
        c = Symptoms.objects.create(**b)
        user = AppointmentModel.objects.create(symptoms=c, **validated_data)
        return user

    def to_representation(self, instance):
        rep = super(NewAppointmentSerializer, self).to_representation(instance)
        rep['DoctorId'] = instance.DoctorId.Username
        return rep

    def update(self, instance, validated_data):
        user_data = validated_data.pop('symptoms')
        print(user_data)
        user_serializer = Symtomsserializer()
        print(user_serializer)
        super(NewAppointmentSerializer, self).update(instance, validated_data)
        super(Symtomsserializer, user_serializer).update(instance.UserId, user_data)
        return instance
 
class DoctorDetails(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('Doctor', 'Doctormodel')
        fields = ['Firstname', 'Lastname', 'Email', 'Username', 'Password', 'MobileNumber']
    
class GetUserDetails(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('User', 'UserModel')
        fields = '__all__'    


class GetAppointment(serializers.ModelSerializer):
    DoctorId = DoctorDetails()
    symptoms = Symtomsserializer()
    UserId = GetUserDetails()

    class Meta:
        model = AppointmentModel
        fields = ['id', 'UserId', 'DoctorId', 'ScheduleId',  'Date', 'Fees', 'Time', 'Specialization'
                  , 'CurrentDate', 'symptoms']