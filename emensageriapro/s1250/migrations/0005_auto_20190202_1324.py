# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1250', '0004_auto_20181213_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1250infoprocj',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1250tpaquis',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]