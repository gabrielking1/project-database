# Generated by Django 3.2.18 on 2023-03-14 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0013_student_dayo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dayo',
        ),
    ]