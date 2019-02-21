# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('r1070', '0008_auto_20190204_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='r1070alteracao',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracao_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070alteracao',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracao_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070alteracaodadosprocjud',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracaodadosprocjud_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070alteracaodadosprocjud',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracaodadosprocjud_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070alteracaoinfosusp',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracaoinfosusp_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070alteracaoinfosusp',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracaoinfosusp_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070alteracaonovavalidade',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracaonovavalidade_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070alteracaonovavalidade',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracaonovavalidade_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070exclusao',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070exclusao_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070exclusao',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070exclusao_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070inclusao',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070inclusao_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070inclusao',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070inclusao_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070inclusaodadosprocjud',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070inclusaodadosprocjud_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070inclusaodadosprocjud',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070inclusaodadosprocjud_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070inclusaoinfosusp',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070inclusaoinfosusp_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r1070inclusaoinfosusp',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070inclusaoinfosusp_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]