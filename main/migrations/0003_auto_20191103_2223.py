# Generated by Django 2.2.6 on 2019-11-04 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191103_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newseries',
            name='series_slug',
        ),
        migrations.AlterField(
            model_name='new',
            name='new_publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 3, 22, 23, 30, 787574), verbose_name='date published'),
        ),
    ]
