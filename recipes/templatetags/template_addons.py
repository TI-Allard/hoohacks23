from django import template
from django.utils.text import slugify

register = template.Library()

@register.simple_tag
def get_index(i, j):
    return 4*int(i) + int(j)

@register.simple_tag
def get_recipe_name(list, i, j):
    try:
        return list[get_index(i,j)].recipe_name
    except:
        return "None"

@register.simple_tag
def get_slug_from_name(list, i, j):
    return "recipes/" + slugify(get_recipe_name(list, i, j))