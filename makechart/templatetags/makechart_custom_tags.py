from django import template
from makechart.models import Team
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def showAllTeams():
    teams = Team.objects.all()
    options = ""
    for t in teams:
    	newoption = "<option value='" + str(t.id) + "'>" + t.name + "</option>"
    	options += newoption
    return mark_safe(options)
