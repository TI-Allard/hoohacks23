from django import template
from django.utils.text import slugify

register = template.Library()


@register.simple_tag
def get_index(i, j):
    return 4 * int(i) + int(j)


@register.simple_tag
def get_recipe(list, i, j):
    try:
        return list[get_index(i, j)]
    except:
        return None


@register.simple_tag
def get_address(recipe):
    return "recipes/" + slugify(recipe.recipe_name)
