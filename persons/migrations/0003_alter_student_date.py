# Generated by Django 4.1.5 on 2023-01-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_alter_department_id_alter_faculty_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
