# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5013', '0016_auto_20190620_1408'),
        ('controle_de_acesso', '0026_auto_20190620_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s5013baseperante',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s5013baseperapur',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s5013dpsperante',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s5013dpsperapur',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s5013infobasefgts',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s5013infobaseperante',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s5013infodpsfgts',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s5013infodpsperante',
            name='excluido',
        ),
    ]
