# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r4099', '0006_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r4099iderespinf',
            options={'managed': True, 'ordering': ['r4099_evtfech', 'nmresp', 'cpfresp'], 'permissions': (('can_see_list_r4099ideRespInf', 'Pode ver listagem do modelo R4099IDERESPINF'), ('can_see_data_r4099ideRespInf', 'Pode visualizar o conte\xfado do modelo R4099IDERESPINF'), ('can_see_menu_r4099ideRespInf', 'Pode visualizar no menu o modelo R4099IDERESPINF'), ('can_print_list_r4099ideRespInf', 'Pode imprimir listagem do modelo R4099IDERESPINF'), ('can_print_data_r4099ideRespInf', 'Pode imprimir o conte\xfado do modelo R4099IDERESPINF'))},
        ),
    ]