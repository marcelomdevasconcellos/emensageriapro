# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2410', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2410homologtc',
            options={'managed': True, 'ordering': ['s2410_evtcdbenin', 'dthomol', 'nratolegal'], 'permissions': (('can_see_list_s2410homologTC', 'Pode ver listagem do modelo S2410HOMOLOGTC'), ('can_see_data_s2410homologTC', 'Pode visualizar o conte\xfado do modelo S2410HOMOLOGTC'), ('can_see_menu_s2410homologTC', 'Pode visualizar no menu o modelo S2410HOMOLOGTC'), ('can_print_list_s2410homologTC', 'Pode imprimir listagem do modelo S2410HOMOLOGTC'), ('can_print_data_s2410homologTC', 'Pode imprimir o conte\xfado do modelo S2410HOMOLOGTC'))},
        ),
        migrations.AlterModelOptions(
            name='s2410infopenmorte',
            options={'managed': True, 'ordering': ['s2410_evtcdbenin', 'tppenmorte'], 'permissions': (('can_see_list_s2410infoPenMorte', 'Pode ver listagem do modelo S2410INFOPENMORTE'), ('can_see_data_s2410infoPenMorte', 'Pode visualizar o conte\xfado do modelo S2410INFOPENMORTE'), ('can_see_menu_s2410infoPenMorte', 'Pode visualizar no menu o modelo S2410INFOPENMORTE'), ('can_print_list_s2410infoPenMorte', 'Pode imprimir listagem do modelo S2410INFOPENMORTE'), ('can_print_data_s2410infoPenMorte', 'Pode imprimir o conte\xfado do modelo S2410INFOPENMORTE'))},
        ),
        migrations.AlterModelOptions(
            name='s2410instpenmorte',
            options={'managed': True, 'ordering': ['s2410_infopenmorte', 'cpfinst', 'dtinst', 'intaposentado'], 'permissions': (('can_see_list_s2410instPenMorte', 'Pode ver listagem do modelo S2410INSTPENMORTE'), ('can_see_data_s2410instPenMorte', 'Pode visualizar o conte\xfado do modelo S2410INSTPENMORTE'), ('can_see_menu_s2410instPenMorte', 'Pode visualizar no menu o modelo S2410INSTPENMORTE'), ('can_print_list_s2410instPenMorte', 'Pode imprimir listagem do modelo S2410INSTPENMORTE'), ('can_print_data_s2410instPenMorte', 'Pode imprimir o conte\xfado do modelo S2410INSTPENMORTE'))},
        ),
    ]
