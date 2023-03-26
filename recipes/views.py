from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.utils.text import slugify
from django.http import HttpResponse, HttpResponseNotFound
from .models import Recipes


def home(request):
    template = loader.get_template('recipes/home.html')

    recipes_list = Recipes.objects.order_by('id')[:]

    context = {
        'recipes_list': recipes_list
    }
    return HttpResponse(template.render(context, request))


def recipe(request, slug):
    template = loader.get_template('recipes/recipes.html')

    recipes_list = Recipes.objects.order_by('id')[:]

    for recipe in recipes_list:
        if slugify(recipe.recipe_name) == slug:
            context = {
                'recipe': recipe
            }
            return HttpResponse(template.render(context, request))

    return HttpResponseNotFound("The address does not correspond to a valid recipe.")


def about(request):
    template = loader.get_template('recipes/about.html')

    context = {}
    return HttpResponse(template.render(context, request))


class RecipeFinderView(TemplateView):
    template_name = 'recipes/recipe-finder.html'


class SearchResultsView(ListView):
    model = Recipes
    template_name = 'recipes/search-results.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        recipes_list = Recipes.objects.filter(
            Q(recipe_name__icontains=query) | Q(ingredients__icontains=query)
        )
        return recipes_list
