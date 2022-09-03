from rest_framework import generics
from rest_framework.response import Response
from Doctor.serializers import DoctorRegSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = DoctorRegSerializer
    def post(self, request, *args, **kwargs):
        """Here User Can Register But MobileNumber Is Mandatory"""
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user=serializer.save()
            return Response({'Message': 'Successful',
                                 'Result': DoctorRegSerializer(user).data,
                                 'HasError': False,
                                 'Status': 200})

        except Exception as e:
            return Response({'Message': 'Fail',
                             'Result': 'Fail',
                             'HasError': True,
                             'Status': 400})
