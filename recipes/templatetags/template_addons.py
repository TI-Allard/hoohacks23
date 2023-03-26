from django import template
from django.utils.text import slugify

register = template.Library()


@register.simple_tag
def get_iterator(ingredient_list):
    return range((len(ingredient_list) // 4) + 1)


@register.simple_tag
def get_index(i, j):
    return 4 * int(i) + int(j)


@register.simple_tag
def get_recipe(ingredient_list, i, j):
    try:
        return ingredient_list[get_index(i, j)]
    except:
        return None


@register.simple_tag
def get_address(recipe):
    return "recipes/" + slugify(recipe.recipe_name)
