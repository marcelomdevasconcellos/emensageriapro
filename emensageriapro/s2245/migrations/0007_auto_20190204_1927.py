# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2245', '0006_auto_20190202_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2245ideprofresp',
            options={'managed': True, 'ordering': ['s2245_infocomplem', 'nmprof', 'tpprof', 'formprof', 'codcbo', 'nacprof'], 'permissions': (('can_view_s2245_ideprofresp', 'Can view s2245_ideprofresp'),)},
        ),
        migrations.AlterModelOptions(
            name='s2245infocomplem',
            options={'managed': True, 'ordering': ['s2245_evttreicap', 'dttreicap', 'durtreicap', 'modtreicap', 'tptreicap'], 'permissions': (('can_view_s2245_infocomplem', 'Can view s2245_infocomplem'),)},
        ),
    ]