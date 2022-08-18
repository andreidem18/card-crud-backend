from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from cars.models import Car
from cars.serializer import CarSerializer
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
        car = Car.objects.create(
            model=request.data['model'], 
            brand=request.data['brand'], 
            color=request.data['color'], 
            year=request.data['year'], 
            price=request.data['price'],
            created_by=get_client_ip(request)
        )
        serialized = CarSerializer(car)
        return Response(status = status.HTTP_201_CREATED, data = serialized.data)
