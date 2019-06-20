# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 14:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s2240', '0018_auto_20190602_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='s2240altexprisco',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240altexprisco',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240altexprisco',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240altexprisco_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240altexpriscoepc',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240altexpriscoepc',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240altexpriscoepc',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240altexpriscoepc_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240altexpriscoepi',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240altexpriscoepi',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240altexpriscoepi',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240altexpriscoepi_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240altexpriscofatrisco',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240altexpriscofatrisco',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240altexpriscofatrisco',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240altexpriscofatrisco_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240altexpriscoinfoamb',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240altexpriscoinfoamb',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240altexpriscoinfoamb',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240altexpriscoinfoamb_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240fimexprisco',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240fimexprisco',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240fimexprisco',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240fimexprisco_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240fimexpriscoinfoamb',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240fimexpriscoinfoamb',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240fimexpriscoinfoamb',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240fimexpriscoinfoamb_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240fimexpriscorespreg',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240fimexpriscorespreg',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240fimexpriscorespreg',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240fimexpriscorespreg_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoativpericinsal',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoativpericinsal',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoativpericinsal',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240iniexpriscoativpericinsal_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoepc',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoepc',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoepc',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240iniexpriscoepc_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoepi',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoepi',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoepi',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240iniexpriscoepi_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscofatrisco',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscofatrisco',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscofatrisco',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240iniexpriscofatrisco_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoinfoamb',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoinfoamb',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoinfoamb',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240iniexpriscoinfoamb_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoobs',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoobs',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoobs',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240iniexpriscoobs_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscorespreg',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscorespreg',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2240iniexpriscorespreg',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2240iniexpriscorespreg_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
