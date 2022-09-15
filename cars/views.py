from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from cars.models import Car
from cars.serializer import CarSerializer, CreateCarSerializer
from rest_framework.response import Response
from rest_framework import status
from config.get_client_ip import get_client_ip

class CarViewSet(ModelViewSet):
    queryset=Car.objects.all()
    serializer_class = CarSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(created_by=get_client_ip(request))
        serialized = CarSerializer(queryset, many=True)
        return Response(serialized.data)

    def create(self, request, *args, **kwargs):
        request.data['created_by']=get_client_ip(request)
        serialized = CreateCarSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(status = status.HTTP_400_BAD_REQUEST, data = serialized.errors)
        else:
            serialized.save()
            serialized = CarSerializer(serialized.data)
            return Response(status = status.HTTP_201_CREATED, data = serialized.data)
