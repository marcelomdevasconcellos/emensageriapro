# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-23 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r3010', '0017_auto_20190620_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r3010boletim',
            name='codmunic',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]