# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0002_home_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='home',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
