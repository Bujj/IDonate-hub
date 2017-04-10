# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 07:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to=events.models.upload_location)),
                ('about_home', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('managers_name', models.CharField(max_length=250)),
                ('phone_number', models.IntegerField()),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
