from rest_framework import generics
from rest_framework.views import Response
from User.serializers import GetAppointment
from User.models import AppointmentModel

class GetAppointments(generics.GenericAPIView):
    serializer_class = GetAppointment


    def get(self, request):
        """Here We Get All The Appointments Details"""
        try:
            result = AppointmentModel.objects.all()
            serializer_class = GetAppointment(result, many=True)

            if serializer_class.data:
                return Response({'Message': 'Successful',
                                 'Result': serializer_class.data,
                                 'HasError': False,
                                 'Status': 200})
                
        except Exception as e:
            return Response({'Message': 'Fail',
                             'Result': 'Fail',
                             'HasError': True,
                             'Status': 400})