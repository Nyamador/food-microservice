from django.shortcuts import render
from rest_framework.decorators import  api_view
from rest_framework.views import Response

# Create your views here.
@api_view()
def some_protected_view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})