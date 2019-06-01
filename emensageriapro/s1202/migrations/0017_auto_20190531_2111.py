# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1202', '0016_auto_20190530_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1202dmdev',
            options={'managed': True, 'ordering': ['s1202_evtrmnrpps', 'idedmdev', 'codcateg'], 'permissions': (('can_view_s1202dmDev', 'Can view S1202DMDEV'), ('can_view_menu_s1202dmDev', 'Can view menu S1202DMDEV'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperant',
            options={'managed': True, 'ordering': ['s1202_dmdev'], 'permissions': (('can_view_s1202infoPerAnt', 'Can view S1202INFOPERANT'), ('can_view_menu_s1202infoPerAnt', 'Can view menu S1202INFOPERANT'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantideadc',
            options={'managed': True, 'ordering': ['s1202_infoperant', 'dtlei', 'nrlei', 'tpacconv', 'dsc'], 'permissions': (('can_view_s1202infoPerAntideADC', 'Can view S1202INFOPERANTIDEADC'), ('can_view_menu_s1202infoPerAntideADC', 'Can view menu S1202INFOPERANTIDEADC'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantideestab',
            options={'managed': True, 'ordering': ['s1202_infoperant_ideperiodo', 'tpinsc', 'nrinsc'], 'permissions': (('can_view_s1202infoPerAntideEstab', 'Can view S1202INFOPERANTIDEESTAB'), ('can_view_menu_s1202infoPerAntideEstab', 'Can view menu S1202INFOPERANTIDEESTAB'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantideperiodo',
            options={'managed': True, 'ordering': ['s1202_infoperant_ideadc', 'perref'], 'permissions': (('can_view_s1202infoPerAntidePeriodo', 'Can view S1202INFOPERANTIDEPERIODO'), ('can_view_menu_s1202infoPerAntidePeriodo', 'Can view menu S1202INFOPERANTIDEPERIODO'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantitensremun',
            options={'managed': True, 'ordering': ['s1202_infoperant_remunperant', 'codrubr', 'idetabrubr', 'vrrubr'], 'permissions': (('can_view_s1202infoPerAntitensRemun', 'Can view S1202INFOPERANTITENSREMUN'), ('can_view_menu_s1202infoPerAntitensRemun', 'Can view menu S1202INFOPERANTITENSREMUN'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantremunperant',
            options={'managed': True, 'ordering': ['s1202_infoperant_ideestab', 'codcateg'], 'permissions': (('can_view_s1202infoPerAntremunPerAnt', 'Can view S1202INFOPERANTREMUNPERANT'), ('can_view_menu_s1202infoPerAntremunPerAnt', 'Can view menu S1202INFOPERANTREMUNPERANT'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapur',
            options={'managed': True, 'ordering': ['s1202_dmdev'], 'permissions': (('can_view_s1202infoPerApur', 'Can view S1202INFOPERAPUR'), ('can_view_menu_s1202infoPerApur', 'Can view menu S1202INFOPERAPUR'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurdetoper',
            options={'managed': True, 'ordering': ['s1202_infoperapur_infosaudecolet', 'cnpjoper', 'regans', 'vrpgtit'], 'permissions': (('can_view_s1202infoPerApurdetOper', 'Can view S1202INFOPERAPURDETOPER'), ('can_view_menu_s1202infoPerApurdetOper', 'Can view menu S1202INFOPERAPURDETOPER'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurdetplano',
            options={'managed': True, 'ordering': ['s1202_infoperapur_detoper', 'tpdep', 'nmdep', 'dtnascto', 'vlrpgdep'], 'permissions': (('can_view_s1202infoPerApurdetPlano', 'Can view S1202INFOPERAPURDETPLANO'), ('can_view_menu_s1202infoPerApurdetPlano', 'Can view menu S1202INFOPERAPURDETPLANO'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurideestab',
            options={'managed': True, 'ordering': ['s1202_infoperapur', 'tpinsc', 'nrinsc'], 'permissions': (('can_view_s1202infoPerApurideEstab', 'Can view S1202INFOPERAPURIDEESTAB'), ('can_view_menu_s1202infoPerApurideEstab', 'Can view menu S1202INFOPERAPURIDEESTAB'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurinfosaudecolet',
            options={'managed': True, 'ordering': ['s1202_infoperapur_remunperapur'], 'permissions': (('can_view_s1202infoPerApurinfoSaudeColet', 'Can view S1202INFOPERAPURINFOSAUDECOLET'), ('can_view_menu_s1202infoPerApurinfoSaudeColet', 'Can view menu S1202INFOPERAPURINFOSAUDECOLET'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapuritensremun',
            options={'managed': True, 'ordering': ['s1202_infoperapur_remunperapur', 'codrubr', 'idetabrubr', 'vrrubr'], 'permissions': (('can_view_s1202infoPerApuritensRemun', 'Can view S1202INFOPERAPURITENSREMUN'), ('can_view_menu_s1202infoPerApuritensRemun', 'Can view menu S1202INFOPERAPURITENSREMUN'))},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurremunperapur',
            options={'managed': True, 'ordering': ['s1202_infoperapur_ideestab', 'codcateg'], 'permissions': (('can_view_s1202infoPerApurremunPerApur', 'Can view S1202INFOPERAPURREMUNPERAPUR'), ('can_view_menu_s1202infoPerApurremunPerApur', 'Can view menu S1202INFOPERAPURREMUNPERAPUR'))},
        ),
        migrations.AlterModelOptions(
            name='s1202procjudtrab',
            options={'managed': True, 'ordering': ['s1202_evtrmnrpps', 'tptrib', 'nrprocjud'], 'permissions': (('can_view_s1202procJudTrab', 'Can view S1202PROCJUDTRAB'), ('can_view_menu_s1202procJudTrab', 'Can view menu S1202PROCJUDTRAB'))},
        ),
    ]
