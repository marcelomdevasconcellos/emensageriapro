# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2240', '0008_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s2240altexprisco',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240altexprisco',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240altexpriscoepc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240altexpriscoepc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240altexpriscoepi',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240altexpriscoepi',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240altexpriscofatrisco',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240altexpriscofatrisco',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240altexpriscoinfoamb',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240altexpriscoinfoamb',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240fimexprisco',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240fimexprisco',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240fimexpriscoinfoamb',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240fimexpriscoinfoamb',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240fimexpriscorespreg',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240fimexpriscorespreg',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoativpericinsal',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoativpericinsal',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoepc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoepc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoepi',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoepi',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscofatrisco',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscofatrisco',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoinfoamb',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoinfoamb',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoobs',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscoobs',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscorespreg',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240iniexpriscorespreg',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='s2240altexprisco',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240altexprisco',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240altexpriscoepc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240altexpriscoepc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240altexpriscoepi',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240altexpriscoepi',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240altexpriscofatrisco',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240altexpriscofatrisco',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240altexpriscoinfoamb',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240altexpriscoinfoamb',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240fimexprisco',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240fimexprisco',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240fimexpriscoinfoamb',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240fimexpriscoinfoamb',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240fimexpriscorespreg',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240fimexpriscorespreg',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoativpericinsal',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoativpericinsal',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoepc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoepc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoepi',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoepi',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscofatrisco',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscofatrisco',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoinfoamb',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoinfoamb',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoobs',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscoobs',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscorespreg',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscorespreg',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]