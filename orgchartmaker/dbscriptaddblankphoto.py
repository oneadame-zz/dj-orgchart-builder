# This script is for adding blank profile photos 
# for employees that have none.

from makechart.models import Employee

employees = Employee.objects.all()

# Iterate through each Team's employees. If
# the employee has a photo, do nothing. If 
# not, add the blank photo placeholder.

for e in employees:
	if e.photo == "0":
		e.photo = "uploads/blank.png"
		e.save()
		print(e.name + "'s photo updated to blank placeholder")
	else:
		print(e.name + "had a photo already.")