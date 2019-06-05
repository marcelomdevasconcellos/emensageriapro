# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2240', '0016_auto_20190530_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2240altexprisco',
            options={'managed': True, 'ordering': ['s2240_evtexprisco', 'dtaltcondicao'], 'permissions': (('can_view_s2240altExpRisco', 'Can view S2240ALTEXPRISCO'), ('can_view_menu_s2240altExpRisco', 'Can view menu S2240ALTEXPRISCO'))},
        ),
        migrations.AlterModelOptions(
            name='s2240altexpriscoepc',
            options={'managed': True, 'ordering': ['s2240_altexprisco_fatrisco', 'dscepc'], 'permissions': (('can_view_s2240altExpRiscoepc', 'Can view S2240ALTEXPRISCOEPC'), ('can_view_menu_s2240altExpRiscoepc', 'Can view menu S2240ALTEXPRISCOEPC'))},
        ),
        migrations.AlterModelOptions(
            name='s2240altexpriscoepi',
            options={'managed': True, 'ordering': ['s2240_altexprisco_fatrisco', 'eficepi', 'medprotecao', 'condfuncto', 'przvalid', 'periodictroca', 'higienizacao'], 'permissions': (('can_view_s2240altExpRiscoepi', 'Can view S2240ALTEXPRISCOEPI'), ('can_view_menu_s2240altExpRiscoepi', 'Can view menu S2240ALTEXPRISCOEPI'))},
        ),
        migrations.AlterModelOptions(
            name='s2240altexpriscofatrisco',
            options={'managed': True, 'ordering': ['s2240_altexprisco_infoamb', 'codfatris', 'utilizepc', 'utilizepi'], 'permissions': (('can_view_s2240altExpRiscofatRisco', 'Can view S2240ALTEXPRISCOFATRISCO'), ('can_view_menu_s2240altExpRiscofatRisco', 'Can view menu S2240ALTEXPRISCOFATRISCO'))},
        ),
        migrations.AlterModelOptions(
            name='s2240altexpriscoinfoamb',
            options={'managed': True, 'ordering': ['s2240_altexprisco', 'codamb', 'dscativdes'], 'permissions': (('can_view_s2240altExpRiscoinfoAmb', 'Can view S2240ALTEXPRISCOINFOAMB'), ('can_view_menu_s2240altExpRiscoinfoAmb', 'Can view menu S2240ALTEXPRISCOINFOAMB'))},
        ),
        migrations.AlterModelOptions(
            name='s2240fimexprisco',
            options={'managed': True, 'ordering': ['s2240_evtexprisco', 'dtfimcondicao'], 'permissions': (('can_view_s2240fimExpRisco', 'Can view S2240FIMEXPRISCO'), ('can_view_menu_s2240fimExpRisco', 'Can view menu S2240FIMEXPRISCO'))},
        ),
        migrations.AlterModelOptions(
            name='s2240fimexpriscoinfoamb',
            options={'managed': True, 'ordering': ['s2240_fimexprisco', 'codamb'], 'permissions': (('can_view_s2240fimExpRiscoinfoAmb', 'Can view S2240FIMEXPRISCOINFOAMB'), ('can_view_menu_s2240fimExpRiscoinfoAmb', 'Can view menu S2240FIMEXPRISCOINFOAMB'))},
        ),
        migrations.AlterModelOptions(
            name='s2240fimexpriscorespreg',
            options={'managed': True, 'ordering': ['s2240_evtexprisco', 'dtini', 'nisresp', 'nroc'], 'permissions': (('can_view_s2240fimExpRiscorespReg', 'Can view S2240FIMEXPRISCORESPREG'), ('can_view_menu_s2240fimExpRiscorespReg', 'Can view menu S2240FIMEXPRISCORESPREG'))},
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscoativpericinsal',
            options={'managed': True, 'ordering': ['s2240_evtexprisco', 'codativ'], 'permissions': (('can_view_s2240iniExpRiscoativPericInsal', 'Can view S2240INIEXPRISCOATIVPERICINSAL'), ('can_view_menu_s2240iniExpRiscoativPericInsal', 'Can view menu S2240INIEXPRISCOATIVPERICINSAL'))},
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscoepc',
            options={'managed': True, 'ordering': ['s2240_iniexprisco_fatrisco', 'codep', 'dscepc'], 'permissions': (('can_view_s2240iniExpRiscoepc', 'Can view S2240INIEXPRISCOEPC'), ('can_view_menu_s2240iniExpRiscoepc', 'Can view menu S2240INIEXPRISCOEPC'))},
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscoepi',
            options={'managed': True, 'ordering': ['s2240_iniexprisco_fatrisco', 'eficepi', 'medprotecao', 'condfuncto', 'usoinint', 'przvalid', 'periodictroca', 'higienizacao'], 'permissions': (('can_view_s2240iniExpRiscoepi', 'Can view S2240INIEXPRISCOEPI'), ('can_view_menu_s2240iniExpRiscoepi', 'Can view menu S2240INIEXPRISCOEPI'))},
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscofatrisco',
            options={'managed': True, 'ordering': ['s2240_evtexprisco', 'codfatris', 'tpaval', 'utilizepc', 'utilizepi'], 'permissions': (('can_view_s2240iniExpRiscofatRisco', 'Can view S2240INIEXPRISCOFATRISCO'), ('can_view_menu_s2240iniExpRiscofatRisco', 'Can view menu S2240INIEXPRISCOFATRISCO'))},
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscoinfoamb',
            options={'managed': True, 'ordering': ['s2240_evtexprisco', 'codamb'], 'permissions': (('can_view_s2240iniExpRiscoinfoAmb', 'Can view S2240INIEXPRISCOINFOAMB'), ('can_view_menu_s2240iniExpRiscoinfoAmb', 'Can view menu S2240INIEXPRISCOINFOAMB'))},
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscoobs',
            options={'managed': True, 'ordering': ['s2240_evtexprisco'], 'permissions': (('can_view_s2240iniExpRiscoobs', 'Can view S2240INIEXPRISCOOBS'), ('can_view_menu_s2240iniExpRiscoobs', 'Can view menu S2240INIEXPRISCOOBS'))},
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscorespreg',
            options={'managed': True, 'ordering': ['s2240_evtexprisco', 'cpfresp', 'nisresp', 'nmresp', 'ideoc', 'nroc', 'ufoc'], 'permissions': (('can_view_s2240iniExpRiscorespReg', 'Can view S2240INIEXPRISCORESPREG'), ('can_view_menu_s2240iniExpRiscorespReg', 'Can view menu S2240INIEXPRISCORESPREG'))},
        ),
    ]