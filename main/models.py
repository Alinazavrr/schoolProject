from django.db import models
from django.contrib.auth.models import User


 # Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CountryFood(models.Model):
    name = models.CharField(max_length=200)
    national_food_info = models.TextField()

    def __str__(self):
        return "CountryFood: " + self.name

class Diets(models.Model):
    name = models.CharField(max_length=100)
    overview = models.TextField()
    duration = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    countries_food = models.ManyToManyField(CountryFood, null=True, blank=True)
    fluid_intake_recommendation = models.TextField(blank=True, null=True)
    restrictions_recommendations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FavoritesDiets(models.Model):
    diet = models.ManyToManyField(Diets)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "User: " + self.user + "favorite diets" + self.diet