from django.db import models
from django.urls import reverse


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    manager = models.ForeignKey('self', on_delete=models.CASCADE)
    lead = models.BooleanField(default=False)

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('makechart:index')
