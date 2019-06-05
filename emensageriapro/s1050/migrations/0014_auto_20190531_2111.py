# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1050', '0013_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1050alteracao',
            options={'managed': True, 'ordering': ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'hrentr', 'hrsaida', 'durjornada', 'perhorflexivel'], 'permissions': (('can_view_s1050alteracao', 'Can view S1050ALTERACAO'), ('can_view_menu_s1050alteracao', 'Can view menu S1050ALTERACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1050alteracaohorariointervalo',
            options={'managed': True, 'ordering': ['s1050_alteracao', 'tpinterv', 'durinterv'], 'permissions': (('can_view_s1050alteracaohorarioIntervalo', 'Can view S1050ALTERACAOHORARIOINTERVALO'), ('can_view_menu_s1050alteracaohorarioIntervalo', 'Can view menu S1050ALTERACAOHORARIOINTERVALO'))},
        ),
        migrations.AlterModelOptions(
            name='s1050alteracaonovavalidade',
            options={'managed': True, 'ordering': ['s1050_alteracao', 'inivalid'], 'permissions': (('can_view_s1050alteracaonovaValidade', 'Can view S1050ALTERACAONOVAVALIDADE'), ('can_view_menu_s1050alteracaonovaValidade', 'Can view menu S1050ALTERACAONOVAVALIDADE'))},
        ),
        migrations.AlterModelOptions(
            name='s1050exclusao',
            options={'managed': True, 'ordering': ['s1050_evttabhortur', 'codhorcontrat', 'inivalid'], 'permissions': (('can_view_s1050exclusao', 'Can view S1050EXCLUSAO'), ('can_view_menu_s1050exclusao', 'Can view menu S1050EXCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1050inclusao',
            options={'managed': True, 'ordering': ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'hrentr', 'hrsaida', 'durjornada', 'perhorflexivel'], 'permissions': (('can_view_s1050inclusao', 'Can view S1050INCLUSAO'), ('can_view_menu_s1050inclusao', 'Can view menu S1050INCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1050inclusaohorariointervalo',
            options={'managed': True, 'ordering': ['s1050_inclusao', 'tpinterv', 'durinterv'], 'permissions': (('can_view_s1050inclusaohorarioIntervalo', 'Can view S1050INCLUSAOHORARIOINTERVALO'), ('can_view_menu_s1050inclusaohorarioIntervalo', 'Can view menu S1050INCLUSAOHORARIOINTERVALO'))},
        ),
    ]