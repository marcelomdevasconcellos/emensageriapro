# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1070', '0013_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1070alteracao',
            options={'managed': True, 'ordering': ['s1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'indmatproc'], 'permissions': (('can_view_s1070alteracao', 'Can view S1070ALTERACAO'), ('can_view_menu_s1070alteracao', 'Can view menu S1070ALTERACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1070alteracaodadosprocjud',
            options={'managed': True, 'ordering': ['s1070_alteracao', 'ufvara', 'codmunic', 'idvara'], 'permissions': (('can_view_s1070alteracaodadosProcJud', 'Can view S1070ALTERACAODADOSPROCJUD'), ('can_view_menu_s1070alteracaodadosProcJud', 'Can view menu S1070ALTERACAODADOSPROCJUD'))},
        ),
        migrations.AlterModelOptions(
            name='s1070alteracaoinfosusp',
            options={'managed': True, 'ordering': ['s1070_alteracao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito'], 'permissions': (('can_view_s1070alteracaoinfoSusp', 'Can view S1070ALTERACAOINFOSUSP'), ('can_view_menu_s1070alteracaoinfoSusp', 'Can view menu S1070ALTERACAOINFOSUSP'))},
        ),
        migrations.AlterModelOptions(
            name='s1070alteracaonovavalidade',
            options={'managed': True, 'ordering': ['s1070_alteracao', 'inivalid'], 'permissions': (('can_view_s1070alteracaonovaValidade', 'Can view S1070ALTERACAONOVAVALIDADE'), ('can_view_menu_s1070alteracaonovaValidade', 'Can view menu S1070ALTERACAONOVAVALIDADE'))},
        ),
        migrations.AlterModelOptions(
            name='s1070exclusao',
            options={'managed': True, 'ordering': ['s1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid'], 'permissions': (('can_view_s1070exclusao', 'Can view S1070EXCLUSAO'), ('can_view_menu_s1070exclusao', 'Can view menu S1070EXCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1070inclusao',
            options={'managed': True, 'ordering': ['s1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'indmatproc'], 'permissions': (('can_view_s1070inclusao', 'Can view S1070INCLUSAO'), ('can_view_menu_s1070inclusao', 'Can view menu S1070INCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1070inclusaodadosprocjud',
            options={'managed': True, 'ordering': ['s1070_inclusao', 'ufvara', 'codmunic', 'idvara'], 'permissions': (('can_view_s1070inclusaodadosProcJud', 'Can view S1070INCLUSAODADOSPROCJUD'), ('can_view_menu_s1070inclusaodadosProcJud', 'Can view menu S1070INCLUSAODADOSPROCJUD'))},
        ),
        migrations.AlterModelOptions(
            name='s1070inclusaoinfosusp',
            options={'managed': True, 'ordering': ['s1070_inclusao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito'], 'permissions': (('can_view_s1070inclusaoinfoSusp', 'Can view S1070INCLUSAOINFOSUSP'), ('can_view_menu_s1070inclusaoinfoSusp', 'Can view menu S1070INCLUSAOINFOSUSP'))},
        ),
    ]
