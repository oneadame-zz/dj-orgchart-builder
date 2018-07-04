from django.db import models
from django.urls import reverse


class Team(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('makechart:index')


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    department = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    manager = models.ForeignKey('self', on_delete=models.CASCADE)
    lead = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('makechart:index')
