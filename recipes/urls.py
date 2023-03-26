from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipe-finder/', views.search, name='search'),
    path('recipes/<slug:slug>/', views.recipe, name='recipe'),
]