from django.contrib import admin
from .models import Category, CountryFood, Diets

# Register your models here.

a = [Category, CountryFood, Diets]
for i in a:
    admin.site.register(i)