from django.urls import path

from .views import RestaurantList

urlpatterns = [
    path('', RestaurantList.as_view(), name="restaurant"),
]