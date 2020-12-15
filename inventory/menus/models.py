from django.db import models

class Restaurant(models.Model):
    name = models.CharField("Restaurant Name", max_length=500)
    description = models.CharField("Description", max_length=2000)
    map_url = models.URLField("Google Map Url", max_length=2000)
    country = models.CharField("Country", max_length=200)
    date_added = models.DateField("Date Added", auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Category Name", max_length=100)
    date_added = models.DateField("Date Added", auto_now_add=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField("Food Name", max_length=500)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField("Description", max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField("Date Added", auto_now_add=True)

    def __str__(self):
        return self.name