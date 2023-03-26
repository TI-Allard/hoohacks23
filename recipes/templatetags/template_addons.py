from django import template

register = template.Library()

@register.simple_tag
def get_recipe_name(list, i, j):
    try:
        return list[int(i)*4+int(j)].recipe_name
    except:
        return None