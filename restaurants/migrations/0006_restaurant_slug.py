# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20171023_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
