# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1299', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1299iderespinf',
            options={'managed': True, 'ordering': ['s1299_evtfechaevper', 'nmresp', 'cpfresp', 'telefone'], 'permissions': (('can_see_list_s1299ideRespInf', 'Pode ver listagem do modelo S1299IDERESPINF'), ('can_see_data_s1299ideRespInf', 'Pode visualizar o conte\xfado do modelo S1299IDERESPINF'), ('can_see_menu_s1299ideRespInf', 'Pode visualizar no menu o modelo S1299IDERESPINF'), ('can_print_list_s1299ideRespInf', 'Pode imprimir listagem do modelo S1299IDERESPINF'), ('can_print_data_s1299ideRespInf', 'Pode imprimir o conte\xfado do modelo S1299IDERESPINF'))},
        ),
    ]
