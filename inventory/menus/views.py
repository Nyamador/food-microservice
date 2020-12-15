from django.shortcuts import render
from rest_framework import generics
from .models import Restaurant, Food, Category
from .serializers import RestaurantSerializer, FoodSerializer, CategorySerializer

# Create your views here.
class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FoodList(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer