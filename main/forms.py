from django import forms
from .models import CountryFood

class SpecialDietForm(forms.Form):
    height = forms.DecimalField(max_digits=1, decimal_places=2)
    weight = forms.DecimalField(max_digits=3)
    country = forms.CharField(max_length=200)
    duration = forms.IntegerField()
