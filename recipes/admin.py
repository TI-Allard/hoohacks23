from django.contrib import admin

# Register your models here.

from .models import Recipes

admin.site.register(Recipes)