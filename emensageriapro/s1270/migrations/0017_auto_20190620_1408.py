# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 14:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s1270', '0016_auto_20190602_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='s1270remunavnp',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s1270remunavnp',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s1270remunavnp',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1270remunavnp_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
