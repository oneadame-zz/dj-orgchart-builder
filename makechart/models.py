from django.db import models
from django.urls import reverse


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    manager = models.ForeignKey('self', on_delete=models.CASCADE)
    lead = models.BooleanField(default=False)

    def getTeam(self):
        teams = Team.objects.all()
        for t in teams:
            if self in t.employees.all():
                return t.name

    def allTeams(self):
        return Team.objects.all()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('makechart:index')


class Team(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    employees = models.ManyToManyField(Employee)
    lead = models.ForeignKey(Employee, related_name='Employee', on_delete=models.CASCADE)

    def employee_count(self):
        return self.employees.count()

    def notemployees(self):
        unattached = []
        attached = []
        emps = Employee.objects.all()
        teams = Team.objects.all()
        for t in teams:
            for e in t.employees.all():
                attached.append(e)
        for e in emps:
            if e not in attached:
                unattached.append(e)
        return unattached

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('makechart:index')
