# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onestock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='locations',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
