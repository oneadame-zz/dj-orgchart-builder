from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Team, Employee


class IndexView(generic.ListView):
    template_name = 'makechart/index.html'
    context_object_name = 'latest_teams_list'

    def get_queryset(self):
        return Team.objects.all()


class DetailView(generic.DetailView):
    model = Team
    template_name = 'makechart/detail.html'
