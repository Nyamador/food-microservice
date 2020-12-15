from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import FoodlyUser

class VelocityUserCreationForm(UserCreationForm):

    class Meta:
        model = FoodlyUser
        fields = ('email',)

class VelocityUserChangeForm(UserChangeForm):

    class Meta:
        model = FoodlyUser
        # fields = UserChangeForm.Meta.fields
        fields = ('email',)
