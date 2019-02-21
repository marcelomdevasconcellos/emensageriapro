# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2241', '0006_auto_20190202_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2241altaposentesp',
            options={'managed': True, 'ordering': ['s2241_evtinsapo', 'dtaltcondicao'], 'permissions': (('can_view_s2241_altaposentesp', 'Can view s2241_altaposentesp'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241altaposentespfatrisco',
            options={'managed': True, 'ordering': ['s2241_altaposentesp_infoamb', 'codfatris'], 'permissions': (('can_view_s2241_altaposentesp_fatrisco', 'Can view s2241_altaposentesp_fatrisco'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241altaposentespinfoamb',
            options={'managed': True, 'ordering': ['s2241_altaposentesp', 'codamb'], 'permissions': (('can_view_s2241_altaposentesp_infoamb', 'Can view s2241_altaposentesp_infoamb'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241altinsalperic',
            options={'managed': True, 'ordering': ['s2241_evtinsapo', 'dtaltcondicao'], 'permissions': (('can_view_s2241_altinsalperic', 'Can view s2241_altinsalperic'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241altinsalpericfatrisco',
            options={'managed': True, 'ordering': ['s2241_altinsalperic_infoamb', 'codfatris'], 'permissions': (('can_view_s2241_altinsalperic_fatrisco', 'Can view s2241_altinsalperic_fatrisco'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241altinsalpericinfoamb',
            options={'managed': True, 'ordering': ['s2241_altinsalperic', 'codamb'], 'permissions': (('can_view_s2241_altinsalperic_infoamb', 'Can view s2241_altinsalperic_infoamb'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241fimaposentesp',
            options={'managed': True, 'ordering': ['s2241_evtinsapo', 'dtfimcondicao'], 'permissions': (('can_view_s2241_fimaposentesp', 'Can view s2241_fimaposentesp'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241fimaposentespinfoamb',
            options={'managed': True, 'ordering': ['s2241_fimaposentesp', 'codamb'], 'permissions': (('can_view_s2241_fimaposentesp_infoamb', 'Can view s2241_fimaposentesp_infoamb'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241fiminsalperic',
            options={'managed': True, 'ordering': ['s2241_evtinsapo', 'dtfimcondicao'], 'permissions': (('can_view_s2241_fiminsalperic', 'Can view s2241_fiminsalperic'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241fiminsalpericinfoamb',
            options={'managed': True, 'ordering': ['s2241_fiminsalperic', 'codamb'], 'permissions': (('can_view_s2241_fiminsalperic_infoamb', 'Can view s2241_fiminsalperic_infoamb'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241iniaposentesp',
            options={'managed': True, 'ordering': ['s2241_evtinsapo', 'dtinicondicao'], 'permissions': (('can_view_s2241_iniaposentesp', 'Can view s2241_iniaposentesp'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241iniaposentespfatrisco',
            options={'managed': True, 'ordering': ['s2241_iniaposentesp_infoamb', 'codfatris'], 'permissions': (('can_view_s2241_iniaposentesp_fatrisco', 'Can view s2241_iniaposentesp_fatrisco'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241iniaposentespinfoamb',
            options={'managed': True, 'ordering': ['s2241_iniaposentesp', 'codamb'], 'permissions': (('can_view_s2241_iniaposentesp_infoamb', 'Can view s2241_iniaposentesp_infoamb'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241iniinsalperic',
            options={'managed': True, 'ordering': ['s2241_evtinsapo', 'dtinicondicao'], 'permissions': (('can_view_s2241_iniinsalperic', 'Can view s2241_iniinsalperic'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241iniinsalpericfatrisco',
            options={'managed': True, 'ordering': ['s2241_iniinsalperic_infoamb', 'codfatris'], 'permissions': (('can_view_s2241_iniinsalperic_fatrisco', 'Can view s2241_iniinsalperic_fatrisco'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241iniinsalpericinfoamb',
            options={'managed': True, 'ordering': ['s2241_iniinsalperic', 'codamb'], 'permissions': (('can_view_s2241_iniinsalperic_infoamb', 'Can view s2241_iniinsalperic_infoamb'),)},
        ),
    ]