from .models import Car
from rest_framework.serializers import ModelSerializer

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'color', 'year', 'price')

class CreateCarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'color', 'year', 'price', 'created_by')
        