# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r4010', '0005_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r4010idepgto',
            name='natrend',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforeemb',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - Pessoa Jur\xeddica'), (2, '2 - Pessoa F\xedsica.')], null=True),
        ),
        migrations.AlterField(
            model_name='r4010inforeembdep',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - Pessoa Jur\xeddica'), (2, '2 - Pessoa F\xedsica.')], null=True),
        ),
    ]