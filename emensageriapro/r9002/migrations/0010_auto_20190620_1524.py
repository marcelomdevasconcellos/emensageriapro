# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r9002', '0009_auto_20190620_1350'),
        ('controle_de_acesso', '0026_auto_20190620_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r9002infototal',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r9002regocorrs',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdec',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdia',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r9002totapurmen',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r9002totapurqui',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='r9002totapursem',
            name='excluido',
        ),
    ]