# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-15 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1200', '0023_auto_20191219_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1200infomv',
            name='indmv',
            field=models.IntegerField(choices=[(1, '1 - O declarante aplica a(s) al\xedquota(s) de desconto do segurado sobre a remunera\xe7\xe3o por ele informada (o percentual da(s) al\xedquota(s) ser\xe1(\xe3o) obtido(s) considerando a remunera\xe7\xe3o total do trabalhador)'), (2, '2 - O declarante aplica a(s) al\xedquota(s) de desconto do segurado sobre a diferen\xe7a entre o limite m\xe1ximo do sal\xe1rio de contribui\xe7\xe3o e a remunera\xe7\xe3o de outra(s) empresa(s) para as quais o trabalhador informou que houve o desconto'), (3, '3 - O declarante n\xe3o realiza desconto do segurado, uma vez que houve desconto sobre o limite m\xe1ximo de sal\xe1rio de contribui\xe7\xe3o em outra(s) empresa(s).')], null=True),
        ),
    ]
