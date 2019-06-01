# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5001', '0016_auto_20190530_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s5001calcterc',
            options={'managed': True, 'ordering': ['s5001_infocategincid', 'tpcr', 'vrcssegterc', 'vrdescterc'], 'permissions': (('can_view_s5001calcTerc', 'Can view S5001CALCTERC'), ('can_view_menu_s5001calcTerc', 'Can view menu S5001CALCTERC'))},
        ),
        migrations.AlterModelOptions(
            name='s5001ideestablot',
            options={'managed': True, 'ordering': ['s5001_infocp', 'tpinsc', 'nrinsc', 'codlotacao'], 'permissions': (('can_view_s5001ideEstabLot', 'Can view S5001IDEESTABLOT'), ('can_view_menu_s5001ideEstabLot', 'Can view menu S5001IDEESTABLOT'))},
        ),
        migrations.AlterModelOptions(
            name='s5001infobasecs',
            options={'managed': True, 'ordering': ['s5001_infocategincid', 'ind13', 'tpvalor', 'valor'], 'permissions': (('can_view_s5001infoBaseCS', 'Can view S5001INFOBASECS'), ('can_view_menu_s5001infoBaseCS', 'Can view menu S5001INFOBASECS'))},
        ),
        migrations.AlterModelOptions(
            name='s5001infocategincid',
            options={'managed': True, 'ordering': ['s5001_ideestablot', 'codcateg'], 'permissions': (('can_view_s5001infoCategIncid', 'Can view S5001INFOCATEGINCID'), ('can_view_menu_s5001infoCategIncid', 'Can view menu S5001INFOCATEGINCID'))},
        ),
        migrations.AlterModelOptions(
            name='s5001infocp',
            options={'managed': True, 'ordering': ['s5001_evtbasestrab'], 'permissions': (('can_view_s5001infoCp', 'Can view S5001INFOCP'), ('can_view_menu_s5001infoCp', 'Can view menu S5001INFOCP'))},
        ),
        migrations.AlterModelOptions(
            name='s5001infocpcalc',
            options={'managed': True, 'ordering': ['s5001_evtbasestrab', 'tpcr', 'vrcpseg', 'vrdescseg'], 'permissions': (('can_view_s5001infoCpCalc', 'Can view S5001INFOCPCALC'), ('can_view_menu_s5001infoCpCalc', 'Can view menu S5001INFOCPCALC'))},
        ),
        migrations.AlterModelOptions(
            name='s5001procjudtrab',
            options={'managed': True, 'ordering': ['s5001_evtbasestrab', 'nrprocjud', 'codsusp'], 'permissions': (('can_view_s5001procJudTrab', 'Can view S5001PROCJUDTRAB'), ('can_view_menu_s5001procJudTrab', 'Can view menu S5001PROCJUDTRAB'))},
        ),
    ]
