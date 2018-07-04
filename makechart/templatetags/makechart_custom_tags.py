from django import template

register = template.Library()


def getTeam(value, arg):

    return value.replace(arg, '')
