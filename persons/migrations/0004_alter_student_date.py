# Generated by Django 4.1.5 on 2023-01-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_alter_student_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
