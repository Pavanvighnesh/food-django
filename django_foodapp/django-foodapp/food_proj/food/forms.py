from django import forms
from .models import item


class item_form(forms.ModelForm):
    class Meta:
        model=item
        fields='__all__'