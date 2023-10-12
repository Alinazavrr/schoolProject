from django.db import models

# Create your models here.
class Type:
    name = models.CharField(max_length=200)

class Diets:
    name = models.CharField(max_length=200)
    overview = models.TextField()
    colories = models.IntegerField()
    type = models.ManyToManyField(Type, on_delete=models.CASCADE)
