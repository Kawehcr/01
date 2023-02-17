from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import vitinSerializers
from .models import Vitin


class RequestTestAPI(APIView):

    def get(self, request, format=None):
        return Response({'API': 'OK'})

class VitincreateViewSet(generics.CreateAPIView):

    queryset = Vitin.objects.all()
    serializer_class = vitinSerializers

class VitinRetrieveUpdateDeleteViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = Vitin.objects.all()
    serializer_class = vitinSerializers

class VitinListViewSet(generics.ListAPIView):

    queryset = Vitin.objects.all()
    serializer_class = vitinSerializers