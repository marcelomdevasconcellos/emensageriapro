# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 20:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0036_auto_20190620_1524'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='transmissoreventosefdreinf',
            table='vw_transmissor_eventos_efdreinf',
        ),
        migrations.AlterModelTable(
            name='transmissoreventosefdreinftotalizacoes',
            table='vw_transmissor_eventos_efdreinf_totalizacoes',
        ),
        migrations.AlterModelTable(
            name='transmissoreventosesocial',
            table='vw_transmissor_eventos_esocial',
        ),
        migrations.AlterModelTable(
            name='transmissoreventosesocialtotalizacoes',
            table='vw_transmissor_eventos_esocial_totalizacoes',
        ),
    ]
