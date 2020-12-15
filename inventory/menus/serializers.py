from rest_framework.serializers import ModelSerializer
from .models import  Restaurant, Food, Category


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'