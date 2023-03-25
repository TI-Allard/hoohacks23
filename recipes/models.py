from django.db import models

# Create your models here.

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField(blank=True, null=True)
    time=models.CharField(max_length=20, default = "")
    steps = models.TextField(blank=True, null=True)