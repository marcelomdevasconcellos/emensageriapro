# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-09 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0021_auto_20190227_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transmissorlote',
            name='contribuinte_nrinsc',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='contribuinte_tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='empregador_nrinsc',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='empregador_tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='nome_empresa',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='transmissorlote',
            unique_together=set([('nome_empresa', 'excluido')]),
        ),
    ]
