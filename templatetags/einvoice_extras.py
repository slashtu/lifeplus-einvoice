from django import template

register = template.Library()

@register.filter
def get( obj, key):
    return obj[key]


@register.filter
def getTerminal( tree ):

    array = []
    child = tree['child']

    for key in child:
        if child[key]['type'] == 'terminal':
            array.append(child[key])

    return array


@register.filter
def getG2( tree ):

    array = []
    child = tree['child']

    for key in child:
        if child[key]['type'] == 'group2':
            array.append(child[key])

    return array


