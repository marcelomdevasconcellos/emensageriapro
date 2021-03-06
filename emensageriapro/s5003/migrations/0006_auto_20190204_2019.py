# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s5003', '0005_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s5003baseperante',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003baseperante',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003baseperapur',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003baseperapur',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003dpsperante',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003dpsperante',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003dpsperapur',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003dpsperapur',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003ideestablot',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003ideestablot',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infobaseperante',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infobaseperante',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infodpsperante',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infodpsperante',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infofgts',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infofgts',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infotrabdps',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infotrabdps',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infotrabfgts',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infotrabfgts',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='s5003baseperante',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003baseperante',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003baseperapur',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003baseperapur',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003dpsperante',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003dpsperante',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003dpsperapur',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003dpsperapur',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003ideestablot',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003ideestablot',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infobaseperante',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infobaseperante',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infodpsperante',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infodpsperante',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infofgts',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infofgts',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infotrabdps',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infotrabdps',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infotrabfgts',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infotrabfgts',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
