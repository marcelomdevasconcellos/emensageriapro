# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1295', '0003_auto_20181120_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]