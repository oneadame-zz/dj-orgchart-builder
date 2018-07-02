# Generated by Django 2.0 on 2018-07-01 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makechart', '0008_employee_lead'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.AddField(
            model_name='team',
            name='employees',
            field=models.ManyToManyField(to='makechart.Employee'),
        ),
    ]