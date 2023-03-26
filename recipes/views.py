from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Recipes

def home(request):
    template = loader.get_template('recipes/home.html')

    recipes_list = Recipes.objects.order_by('id')[:]
    iterator = range((len(recipes_list) // 4) + 1)

    context = {
        'row_iterator': iterator,
        'recipes_list': recipes_list
    }
    return HttpResponse(template.render(context, request))


def recipe(request, slug):
    template = loader.get_template('recipes/recipes.html')

    context = {}
    return HttpResponse(template.render(context, request))


def search(request):
    template = loader.get_template('recipes/finder-template.html')

    context = {}
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('recipes/about.html')

    context = {}
    return HttpResponse(template.render(context, request))