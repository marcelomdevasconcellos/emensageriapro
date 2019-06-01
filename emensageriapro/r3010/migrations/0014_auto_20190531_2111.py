# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r3010', '0013_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r3010boletim',
            options={'managed': True, 'ordering': ['r3010_evtespdesportivo', 'nrboletim', 'tpcompeticao', 'categevento', 'moddesportiva', 'nomecompeticao', 'cnpjmandante', 'pracadesportiva', 'uf', 'qtdepagantes', 'qtdenaopagantes'], 'permissions': (('can_view_r3010boletim', 'Can view R3010BOLETIM'), ('can_view_menu_r3010boletim', 'Can view menu R3010BOLETIM'))},
        ),
        migrations.AlterModelOptions(
            name='r3010infoproc',
            options={'managed': True, 'ordering': ['r3010_evtespdesportivo', 'tpproc', 'nrproc', 'vlrcpsusp'], 'permissions': (('can_view_r3010infoProc', 'Can view R3010INFOPROC'), ('can_view_menu_r3010infoProc', 'Can view menu R3010INFOPROC'))},
        ),
        migrations.AlterModelOptions(
            name='r3010outrasreceitas',
            options={'managed': True, 'ordering': ['r3010_boletim', 'tpreceita', 'vlrreceita', 'descreceita'], 'permissions': (('can_view_r3010outrasReceitas', 'Can view R3010OUTRASRECEITAS'), ('can_view_menu_r3010outrasReceitas', 'Can view menu R3010OUTRASRECEITAS'))},
        ),
        migrations.AlterModelOptions(
            name='r3010receitaingressos',
            options={'managed': True, 'ordering': ['r3010_boletim', 'tpingresso', 'descingr', 'qtdeingrvenda', 'qtdeingrvendidos', 'qtdeingrdev', 'precoindiv', 'vlrtotal'], 'permissions': (('can_view_r3010receitaIngressos', 'Can view R3010RECEITAINGRESSOS'), ('can_view_menu_r3010receitaIngressos', 'Can view menu R3010RECEITAINGRESSOS'))},
        ),
    ]
