# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r5011', '0016_auto_20190620_1339'),
        ('controle_de_acesso', '0026_auto_20190620_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r5011infocrtom',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r5011infototalcontrib',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r5011rcoml',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r5011rcprb',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r5011regocorrs',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r5011rprest',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r5011rrecrepad',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r5011rtom',
            name='excluido',
        ),
    ]
