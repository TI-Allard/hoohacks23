from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:recipes_id>', views.recipe, name='recipe'),
    path('recipe-finder/', views.search, name='search'),

]