# This script is for cleaning Employee
# database entries with > 1 Team associated.
# Under normal circumstances this situation
# should not be possible.

from makechart.models import Team

teams = Team.objects.all()

allemployees = []

# Iterate through each Team's employees. If
# the employee is not in the allemployees
# array, add it. If it is, remove the given
# employee from the current iteration's team.

for t in teams:
    for e in t.employees.all():
        if e in allemployees:
            t.employees.remove(e)
            t.save()
            print("Duplicate detected! Removed " + t.name + " from " + e.name)
        if e not in allemployees:
            allemployees.append(e)
