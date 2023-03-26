from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, ListView
from django.db.models import Q

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


def recipe(request, recipes_id):
    recipe = Recipes.objects.get(id=recipes_id)
    template = loader.get_template('recipes/recipe.html')
    context = {
        'recipe': recipe
    }
    return HttpResponse(template.render(context, request))


def search(request):
    template = loader.get_template('recipes/search-results.html')

    recipes_list = Recipes.objects.order_by('id')[:]

    context = {
        'recipes_list': recipes_list
    }
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
