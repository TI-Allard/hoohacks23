from django.urls import path
from . import views
from .views import RecipeFinderView, SearchResultsView

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<slug:slug>/', views.recipe, name='recipe'),
    path('about/', views.about, name='about'),
    #path('recipe-finder/', views.search, name='search'),
    path('recipe-finder/', RecipeFinderView.as_view(), name='recipe-finder'),
    path('recipe-finder/results', SearchResultsView.as_view(), name='search-results'),
]