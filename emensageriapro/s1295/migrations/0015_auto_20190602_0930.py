# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1295', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1295iderespinf',
            options={'managed': True, 'ordering': ['s1295_evttotconting', 'nmresp', 'cpfresp', 'telefone'], 'permissions': (('can_see_list_s1295ideRespInf', 'Pode ver listagem do modelo S1295IDERESPINF'), ('can_see_data_s1295ideRespInf', 'Pode visualizar o conte\xfado do modelo S1295IDERESPINF'), ('can_see_menu_s1295ideRespInf', 'Pode visualizar no menu o modelo S1295IDERESPINF'), ('can_print_list_s1295ideRespInf', 'Pode imprimir listagem do modelo S1295IDERESPINF'), ('can_print_data_s1295ideRespInf', 'Pode imprimir o conte\xfado do modelo S1295IDERESPINF'))},
        ),
    ]
