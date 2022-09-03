from rest_framework.response import Response
from rest_framework import generics
from User.serializers import UserSerializer
from User.models import UserModel

class GetUserList(generics.GenericAPIView):
    serializer_class = UserSerializer


    def get(self, request):
        """Here We Get All The User Details """
        try:
            queryset = UserModel.objects.all()
            serializer_class = UserSerializer(queryset, many=True)
            return Response({'Message': 'Successful',
                                 'Result': serializer_class.data,
                                 'HasError': False,
                                 'Status': 200})
        except Exception as e:
            return Response({'Message': 'Fail',
                             'Result': 'Fail',
                             'HasError': True,
                             'Status': 400})