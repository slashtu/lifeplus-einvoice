from django import template

register = template.Library()

@register.filter
def get(value, arg):
    print arg[value]['name']
    return arg[value]['name']

