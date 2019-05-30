# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('efdreinf', '0016_auto_20190427_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='r9002infoTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrrecarqbase', models.CharField(blank=True, max_length=52, null=True)),
                ('tpinsc', models.IntegerField(default=0)),
                ('nrinsc', models.CharField(default=b'A', max_length=14)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002infototal_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002infototal_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9002_evtret', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9002infototal_r9002_evtret', to='efdreinf.r9002evtRet')),
            ],
            options={
                'managed': True,
                'ordering': ['r9002_evtret', 'tpinsc', 'nrinsc'],
                'db_table': 'r9002_infototal',
                'permissions': (('can_view_r9002_infototal', 'Can view r9002_infototal'),),
            },
        ),
        migrations.CreateModel(
            name='r9002regOcorrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpocorr', models.IntegerField(default=0)),
                ('localerroaviso', models.CharField(default=b'A', max_length=200)),
                ('codresp', models.CharField(default=b'A', max_length=6)),
                ('dscresp', models.CharField(default=b'A', max_length=999)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002regocorrs_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002regocorrs_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9002_evtret', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9002regocorrs_r9002_evtret', to='efdreinf.r9002evtRet')),
            ],
            options={
                'managed': True,
                'ordering': ['r9002_evtret', 'tpocorr', 'localerroaviso', 'codresp', 'dscresp'],
                'db_table': 'r9002_regocorrs',
                'permissions': (('can_view_r9002_regocorrs', 'Can view r9002_regocorrs'),),
            },
        ),
        migrations.CreateModel(
            name='r9002totApurDec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perapurdec', models.IntegerField(default=0)),
                ('crdec', models.CharField(default=b'A', max_length=6)),
                ('vlrbasecrdec', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrcrdec', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrbasecrdecsusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('vlrcrdecsusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurdec_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurdec_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9002_infototal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurdec_r9002_infototal', to='r9002.r9002infoTotal')),
            ],
            options={
                'managed': True,
                'ordering': ['r9002_infototal', 'perapurdec', 'crdec', 'vlrbasecrdec', 'vlrcrdec'],
                'db_table': 'r9002_totapurdec',
                'permissions': (('can_view_r9002_totapurdec', 'Can view r9002_totapurdec'),),
            },
        ),
        migrations.CreateModel(
            name='r9002totApurDia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perapurdia', models.IntegerField(default=0)),
                ('crdia', models.CharField(default=b'A', max_length=6)),
                ('vlrbasecrdia', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrcrdia', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrbasecrdiasusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('vlrcrdiasusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurdia_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurdia_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9002_infototal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurdia_r9002_infototal', to='r9002.r9002infoTotal')),
            ],
            options={
                'managed': True,
                'ordering': ['r9002_infototal', 'perapurdia', 'crdia', 'vlrbasecrdia', 'vlrcrdia'],
                'db_table': 'r9002_totapurdia',
                'permissions': (('can_view_r9002_totapurdia', 'Can view r9002_totapurdia'),),
            },
        ),
        migrations.CreateModel(
            name='r9002totApurMen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crmen', models.CharField(default=b'A', max_length=6)),
                ('vlrbasecrmen', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrcrmen', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrbasecrmensusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('vlrcrmensusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurmen_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurmen_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9002_infototal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurmen_r9002_infototal', to='r9002.r9002infoTotal')),
            ],
            options={
                'managed': True,
                'ordering': ['r9002_infototal', 'crmen', 'vlrbasecrmen', 'vlrcrmen'],
                'db_table': 'r9002_totapurmen',
                'permissions': (('can_view_r9002_totapurmen', 'Can view r9002_totapurmen'),),
            },
        ),
        migrations.CreateModel(
            name='r9002totApurQui',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perapurqui', models.IntegerField(default=0)),
                ('crqui', models.CharField(default=b'A', max_length=6)),
                ('vlrbasecrqui', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrcrqui', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrbasecrquisusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('vlrcrquisusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurqui_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurqui_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9002_infototal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapurqui_r9002_infototal', to='r9002.r9002infoTotal')),
            ],
            options={
                'managed': True,
                'ordering': ['r9002_infototal', 'perapurqui', 'crqui', 'vlrbasecrqui', 'vlrcrqui'],
                'db_table': 'r9002_totapurqui',
                'permissions': (('can_view_r9002_totapurqui', 'Can view r9002_totapurqui'),),
            },
        ),
        migrations.CreateModel(
            name='r9002totApurSem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perapursem', models.IntegerField(default=0)),
                ('crsem', models.CharField(default=b'A', max_length=6)),
                ('vlrbasecrsem', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrcrsem', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrbasecrsemsusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('vlrcrsemsusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapursem_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapursem_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9002_infototal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9002totapursem_r9002_infototal', to='r9002.r9002infoTotal')),
            ],
            options={
                'managed': True,
                'ordering': ['r9002_infototal', 'perapursem', 'crsem', 'vlrbasecrsem', 'vlrcrsem'],
                'db_table': 'r9002_totapursem',
                'permissions': (('can_view_r9002_totapursem', 'Can view r9002_totapursem'),),
            },
        ),
    ]