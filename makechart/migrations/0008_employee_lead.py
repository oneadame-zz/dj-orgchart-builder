# Generated by Django 2.0 on 2018-07-01 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makechart', '0007_team_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='lead',
            field=models.BooleanField(default=False),
        ),
    ]
