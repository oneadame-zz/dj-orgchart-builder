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

# TODO: Comment this horrific mess

    def get_queryset(self):
        e = []
        teams = Team.objects.all()
        for i in teams:
            for r in i.employees.all():
                if r not in e:
                    r.teams = []
                    e.append(r)
        for i in teams:
            for r in e:
                if r in i.employees.all():
                    r.teams.append(i.name)
        for r in e:
            r.str_teams = ", ".join(r.teams)
            if len(r.teams) > 1:
                r.multipleteams = True
            else:
                r.multipleteams = False
        for n in Employee.objects.all():
            if n not in e:
                e.append(n)
        return e


class DetailView(generic.DetailView):
    model = Team
    template_name = 'makechart/detail.html'


class EmployeeAdd(CreateView):
    model = Employee
    fields = ['name', 'manager']


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'manager']


def confirm_emp_update(request, employee_id):
    emp = get_object_or_404(Employee, pk=employee_id)
    emp.name = request.POST['name']
    emp.manager = Employee.objects.get(pk=request.POST['manager'])
    newteam = Team.objects.filter(pk=request.POST['team']).first()
    oldteam = Team.objects.filter(name=request.POST['oldteam']).first()
    oldteam.employees.remove(employee_id)
    newteam.employees.add(employee_id)
    newteam.save()
    emp.save()
    return HttpResponseRedirect(reverse('makechart:employee-index'))


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


class TeamMemberUpdate(UpdateView):
    model = Team
    template_name = 'makechart/team_employee_update.html'
    fields = ['employees']
    success_url = reverse_lazy('makechart:index')


def add_member(request, pk):
    team = get_object_or_404(Team, pk=pk)
    new =Employee.objects.get(pk=request.POST['id'])
    team.employees.add(new)
    team.save()
    return HttpResponseRedirect(reverse_lazy('makechart:team-member-update', args=[pk]))


def rm_member(request, pk):
    team = get_object_or_404(Team, pk=pk)
    rm = team.employees.get(pk=request.POST['id'])
    team.employees.remove(rm)
    team.save()
    return HttpResponseRedirect(reverse_lazy('makechart:team-member-update', args=[pk]))


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
