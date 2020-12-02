from django.shortcuts import render
from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer

# Create your views here.
class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer