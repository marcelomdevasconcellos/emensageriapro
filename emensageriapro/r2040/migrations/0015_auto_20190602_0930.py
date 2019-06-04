# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2040', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2040infoproc',
            options={'managed': True, 'ordering': ['r2040_recursosrep', 'tpproc', 'nrproc', 'vlrnret'], 'permissions': (('can_see_list_r2040infoProc', 'Pode ver listagem do modelo R2040INFOPROC'), ('can_see_data_r2040infoProc', 'Pode visualizar o conte\xfado do modelo R2040INFOPROC'), ('can_see_menu_r2040infoProc', 'Pode visualizar no menu o modelo R2040INFOPROC'), ('can_print_list_r2040infoProc', 'Pode imprimir listagem do modelo R2040INFOPROC'), ('can_print_data_r2040infoProc', 'Pode imprimir o conte\xfado do modelo R2040INFOPROC'))},
        ),
        migrations.AlterModelOptions(
            name='r2040inforecurso',
            options={'managed': True, 'ordering': ['r2040_recursosrep', 'tprepasse', 'descrecurso', 'vlrbruto', 'vlrretapur'], 'permissions': (('can_see_list_r2040infoRecurso', 'Pode ver listagem do modelo R2040INFORECURSO'), ('can_see_data_r2040infoRecurso', 'Pode visualizar o conte\xfado do modelo R2040INFORECURSO'), ('can_see_menu_r2040infoRecurso', 'Pode visualizar no menu o modelo R2040INFORECURSO'), ('can_print_list_r2040infoRecurso', 'Pode imprimir listagem do modelo R2040INFORECURSO'), ('can_print_data_r2040infoRecurso', 'Pode imprimir o conte\xfado do modelo R2040INFORECURSO'))},
        ),
        migrations.AlterModelOptions(
            name='r2040recursosrep',
            options={'managed': True, 'ordering': ['r2040_evtassocdesprep', 'cnpjassocdesp', 'vlrtotalrep', 'vlrtotalret'], 'permissions': (('can_see_list_r2040recursosRep', 'Pode ver listagem do modelo R2040RECURSOSREP'), ('can_see_data_r2040recursosRep', 'Pode visualizar o conte\xfado do modelo R2040RECURSOSREP'), ('can_see_menu_r2040recursosRep', 'Pode visualizar no menu o modelo R2040RECURSOSREP'), ('can_print_list_r2040recursosRep', 'Pode imprimir listagem do modelo R2040RECURSOSREP'), ('can_print_data_r2040recursosRep', 'Pode imprimir o conte\xfado do modelo R2040RECURSOSREP'))},
        ),
    ]
