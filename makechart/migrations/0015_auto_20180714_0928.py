# Generated by Django 2.0.7 on 2018-07-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makechart', '0014_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='blank.png', upload_to='uploads/'),
        ),
    ]
