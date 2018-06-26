from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    fields = ['name', 'manager', 'department']


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'manager', 'department']


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('makechart:index')


class TeamAdd(CreateView):
    model = Team
    fields = ['name']


class TeamUpdate(UpdateView):
    model = Team
    fields = ['name']


class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('makechart:index')
