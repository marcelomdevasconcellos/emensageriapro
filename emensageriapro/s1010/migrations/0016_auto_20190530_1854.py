# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1010', '0015_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1010alteracao',
            name='codinccp',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='codinccprp',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='codincirrf',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='natrubr',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='codinccp',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='codinccprp',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='codincirrf',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='natrubr',
            field=models.IntegerField(null=True),
        ),
    ]