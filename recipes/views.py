from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Recipes

def home(request):
    recipes_list = Recipes.objects.order_by('id')[:5]
    template = loader.get_template('recipes/recipe.html')
    context = {
        'recipes_list': recipes_list
    }
    return HttpResponse(template.render(context, request))


def recipe(request, recipes_id):
    recipe = Recipes.objects.get(id=recipes_id)
    template = loader.get_template('recipes/recipe.html')
    context = {
        'recipe': recipe
    }
    return HttpResponse(template.render(context, request))
