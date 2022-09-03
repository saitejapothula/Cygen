from rest_framework import generics
from rest_framework.response import Response
from django.apps import apps
from Doctor.serializers import DoctorAppointSerializers
import logging

logger = logging.getLogger('django')


class DoctorSchedulerRegAPI(generics.GenericAPIView):
        serializer_class = DoctorAppointSerializers

        def post(self, request, *args, **kwargs):
            try:
                serializer = self.get_serializer(data=request.data)
                print("Testing for prod")
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                return Response({'Message': 'Successful',
                                 'Result': DoctorAppointSerializers(user).data,
                                 'HasError': False,
                                 'Status': 200})

            except Exception as e:
                return Response({'Message': 'Fail',
                             'Result': 'Fail',
                             'HasError': True,
                             'Status': 400})
