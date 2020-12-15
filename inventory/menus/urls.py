from django.urls import path

from .views import RestaurantList, FoodList, CategoryList

urlpatterns = [
    path('restaurants', RestaurantList.as_view(), name="restaurants"),
    path('categories', CategoryList.as_view(), name="categories"),
    path('foods', FoodList.as_view(), name="foods"),
]