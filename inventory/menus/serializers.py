from rest_framework.serializers import ModelSerializer
from .models import  Restaurant, Food


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
