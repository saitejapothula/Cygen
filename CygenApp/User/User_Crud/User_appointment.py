from ast import parse
from rest_framework import generics
from rest_framework.response import Response
from django.apps import apps
from User.serializers import NewAppointmentSerializer
from django.template.loader import get_template
import logging
logger = logging.getLogger('django')

class CreateUserAppointment(generics.GenericAPIView):
    serializer_class = NewAppointmentSerializer

    def post(self, request):

        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                'message': 'Successful',
                'Result': NewAppointmentSerializer(user).data,
                'HasError': False,
                'status': 200})
        
        except Exception as e:
            return Response({'Message': 'Fail',
                             'Result': 'Fail',
                             'HasError': True,
                             'Status': 400})


        
