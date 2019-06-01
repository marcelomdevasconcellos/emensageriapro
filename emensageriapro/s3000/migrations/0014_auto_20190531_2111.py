# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s3000', '0013_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s3000idefolhapagto',
            options={'managed': True, 'ordering': ['s3000_evtexclusao', 'indapuracao', 'perapur'], 'permissions': (('can_view_s3000ideFolhaPagto', 'Can view S3000IDEFOLHAPAGTO'), ('can_view_menu_s3000ideFolhaPagto', 'Can view menu S3000IDEFOLHAPAGTO'))},
        ),
        migrations.AlterModelOptions(
            name='s3000idetrabalhador',
            options={'managed': True, 'ordering': ['s3000_evtexclusao', 'cpftrab'], 'permissions': (('can_view_s3000ideTrabalhador', 'Can view S3000IDETRABALHADOR'), ('can_view_menu_s3000ideTrabalhador', 'Can view menu S3000IDETRABALHADOR'))},
        ),
    ]
