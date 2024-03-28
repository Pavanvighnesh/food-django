from django import forms
from .models import item
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class item_form(forms.ModelForm):
    class Meta:
        model=item
        fields='__all__'

class registration_form(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']