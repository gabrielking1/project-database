# Generated by Django 4.1.5 on 2023-01-19 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_alter_student_department_alter_student_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.DateField(),
        ),
    ]
