from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from cars.models import Car
from cars.serializer import CarSerializer

class CarViewSet(ModelViewSet):
    queryset=Car.objects.all()
    serializer_class = CarSerializer
