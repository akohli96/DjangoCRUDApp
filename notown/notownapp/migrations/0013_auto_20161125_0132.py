# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notownapp', '0012_auto_20161116_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruments',
            name='instrld',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
