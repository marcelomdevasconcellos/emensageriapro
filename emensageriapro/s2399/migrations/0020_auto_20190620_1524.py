# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2399', '0019_auto_20190620_1408'),
        ('controle_de_acesso', '0026_auto_20190620_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s2399detoper',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399detplano',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399detverbas',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399dmdev',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399ideestablot',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399infoagnocivo',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399infomv',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399infosaudecolet',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399infosimples',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399mudancacpf',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399procjudtrab',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399quarentena',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399remunoutrempr',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2399verbasresc',
            name='excluido',
        ),
    ]
