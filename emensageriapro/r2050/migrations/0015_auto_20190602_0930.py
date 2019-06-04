# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2050', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2050infoproc',
            options={'managed': True, 'ordering': ['r2050_tipocom', 'tpproc', 'nrproc'], 'permissions': (('can_see_list_r2050infoProc', 'Pode ver listagem do modelo R2050INFOPROC'), ('can_see_data_r2050infoProc', 'Pode visualizar o conte\xfado do modelo R2050INFOPROC'), ('can_see_menu_r2050infoProc', 'Pode visualizar no menu o modelo R2050INFOPROC'), ('can_print_list_r2050infoProc', 'Pode imprimir listagem do modelo R2050INFOPROC'), ('can_print_data_r2050infoProc', 'Pode imprimir o conte\xfado do modelo R2050INFOPROC'))},
        ),
        migrations.AlterModelOptions(
            name='r2050tipocom',
            options={'managed': True, 'ordering': ['r2050_evtcomprod', 'indcom', 'vlrrecbruta'], 'permissions': (('can_see_list_r2050tipoCom', 'Pode ver listagem do modelo R2050TIPOCOM'), ('can_see_data_r2050tipoCom', 'Pode visualizar o conte\xfado do modelo R2050TIPOCOM'), ('can_see_menu_r2050tipoCom', 'Pode visualizar no menu o modelo R2050TIPOCOM'), ('can_print_list_r2050tipoCom', 'Pode imprimir listagem do modelo R2050TIPOCOM'), ('can_print_data_r2050tipoCom', 'Pode imprimir o conte\xfado do modelo R2050TIPOCOM'))},
        ),
    ]
