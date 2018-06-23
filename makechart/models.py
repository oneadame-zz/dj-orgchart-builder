from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    department = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    manager = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
