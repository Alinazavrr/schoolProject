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
    name = models.CharField(max_length=200)
    overview = models.TextField()
    colories = models.IntegerField()
    category = models.ManyToManyField(Category)
    countries_food = models.ManyToManyField(CountryFood)

    def __str__(self):
        return self.name + ': colories per day ' + self.colories_pd_medium


class FavoritesDiets(models.Model):
    diet = models.ManyToManyField(Diets)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "User: " + self.user + "favorite diets" + self.diet