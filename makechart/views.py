from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Team, Employee


class IndexView(generic.ListView):
    template_name = 'makechart/index.html'
    context_object_name = 'latest_teams_list'

    def get_queryset(self):
        return Team.objects.all()


class EmployeeIndex(generic.ListView):
    template_name = 'makechart/employee_index.html'
    context_object_name = 'employee_list'

    def get_queryset(self):
        return Employee.objects.all()


class DetailView(generic.DetailView):
    model = Team
    template_name = 'makechart/detail.html'


class EmployeeAdd(CreateView):
    model = Employee
    fields = ['name', 'manager']


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'manager']


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('makechart:index')


class TeamAdd(CreateView):
    model = Team
    fields = ['name', 'desc', 'employees', 'lead']


class TeamUpdate(UpdateView):
    model = Team
    template_name = 'makechart/team_form_wip.html'
    fields = ['name', 'desc', 'employees', 'lead']
    success_url = reverse_lazy('makechart:index')


def confirm_update(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.name = request.POST['name']
    team.desc = request.POST['desc']
    team.lead = team.employees.get(pk=request.POST['lead'])
    team.save()
    return HttpResponseRedirect(reverse('makechart:index'))


class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('makechart:index')
