# Generated by Django 2.2.6 on 2019-11-04 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newseries',
            name='series_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='new',
            name='new_publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 3, 21, 54, 17, 184696), verbose_name='date published'),
        ),
    ]
