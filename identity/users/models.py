from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import FoodlyUserManager


class FoodlyUser(AbstractUser):

    email = models.EmailField(verbose_name="Email Adddress", max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = FoodlyUserManager()

    def __str__(self):
        return self.email