from django.contrib import admin
from . models import Restaurant, Food, Category

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Category)
