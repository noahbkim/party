# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-08 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20161207_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]