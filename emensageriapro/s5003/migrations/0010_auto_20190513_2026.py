# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s5003', '0009_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5003baseperante',
            name='remfgtse',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5003baseperante',
            name='s5003_infobaseperante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003baseperante_s5003_infobaseperante', to='s5003.s5003infoBasePerAntE'),
        ),
        migrations.AlterField(
            model_name='s5003baseperante',
            name='tpvalore',
            field=models.IntegerField(choices=[(13, '13 - Base de C\xe1lculo do FGTS Diss\xeddio'), (14, '14 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (17, '17 - Base de C\xe1lculo do FGTS Diss\xeddio - Aprendiz'), (18, '18 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (24, '24 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio'), (25, '25 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (26, '26 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (30, '30 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (31, '31 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (32, '32 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz'), (91, '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5003baseperapur',
            name='remfgts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5003baseperapur',
            name='s5003_infobasefgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003baseperapur_s5003_infobasefgts', to='s5003.s5003infoBaseFGTS'),
        ),
        migrations.AlterField(
            model_name='s5003baseperapur',
            name='tpvalor',
            field=models.IntegerField(choices=[(11, '11 - Base de C\xe1lculo do FGTS'), (12, '12 - Base de C\xe1lculo do FGTS 13\xb0 Sal\xe1rio'), (13, '13 - Base de C\xe1lculo do FGTS Diss\xeddio'), (14, '14 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (15, '15 - Base de C\xe1lculo do FGTS - Aprendiz'), (16, '16 - Base de C\xe1lculo do FGTS 13\xb0 Sal\xe1rio - Aprendiz'), (17, '17 - Base de C\xe1lculo do FGTS Diss\xeddio - Aprendiz'), (18, '18 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (21, '21 - Base de C\xe1lculo do FGTS Rescis\xf3rio'), (22, '22 - Base de C\xe1lculo do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio'), (23, '23 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Aviso Pr\xe9vio'), (24, '24 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio'), (25, '25 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (26, '26 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (27, '27 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Aprendiz'), (28, '28 - Base de C\xe1lculo do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio Aprendiz'), (29, '29 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Aviso Pr\xe9vio Aprendiz'), (30, '30 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (31, '31 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (32, '32 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz'), (91, '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5003dpsperante',
            name='dpsfgtse',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5003dpsperante',
            name='s5003_infodpsperante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003dpsperante_s5003_infodpsperante', to='s5003.s5003infoDpsPerAntE'),
        ),
        migrations.AlterField(
            model_name='s5003dpsperante',
            name='tpdpse',
            field=models.IntegerField(choices=[(53, '53 - Dep\xf3sito do FGTS Diss\xeddio'), (54, '54 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (57, '57 - Dep\xf3sito do FGTS Diss\xeddio - Aprendiz'), (58, '58 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (64, '64 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio'), (65, '65 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (66, '66 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (70, '70 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (71, '71 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (72, '72 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5003dpsperapur',
            name='dpsfgts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5003dpsperapur',
            name='s5003_infotrabdps',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003dpsperapur_s5003_infotrabdps', to='s5003.s5003infoTrabDps'),
        ),
        migrations.AlterField(
            model_name='s5003dpsperapur',
            name='tpdps',
            field=models.IntegerField(choices=[(51, '51 - Dep\xf3sito do FGTS'), (52, '52 - Dep\xf3sito do FGTS 13\xb0 Sal\xe1rio'), (53, '53 - Dep\xf3sito do FGTS Diss\xeddio'), (54, '54 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (55, '55 - Dep\xf3sito do FGTS - Aprendiz'), (56, '56 - Dep\xf3sito do FGTS 13\xb0 Sal\xe1rio - Aprendiz'), (57, '57 - Dep\xf3sito do FGTS Diss\xeddio - Aprendiz'), (58, '58 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (61, '61 - Dep\xf3sito do FGTS Rescis\xf3rio'), (62, '62 - Dep\xf3sito do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio'), (63, '63 - Dep\xf3sito do FGTS Rescis\xf3rio - Aviso Pr\xe9vio'), (64, '64 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio'), (65, '65 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (66, '66 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (67, '67 - Dep\xf3sito do FGTS Rescis\xf3rio - Aprendiz'), (68, '68 - Dep\xf3sito do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio Aprendiz'), (69, '69 - Dep\xf3sito do FGTS Rescis\xf3rio - Aviso Pr\xe9vio Aprendiz'), (70, '70 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (71, '71 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (72, '72 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5003ideestablot',
            name='codlotacao',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s5003ideestablot',
            name='nrinsc',
            field=models.CharField(default=b'A', max_length=15),
        ),
        migrations.AlterField(
            model_name='s5003ideestablot',
            name='s5003_evtbasesfgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003ideestablot_s5003_evtbasesfgts', to='esocial.s5003evtBasesFGTS'),
        ),
        migrations.AlterField(
            model_name='s5003ideestablot',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')], default=0),
        ),
        migrations.AlterField(
            model_name='s5003infobasefgts',
            name='s5003_infotrabfgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infobasefgts_s5003_infotrabfgts', to='s5003.s5003infoTrabFGTS'),
        ),
        migrations.AlterField(
            model_name='s5003infobaseperante',
            name='perref',
            field=models.CharField(default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='s5003infobaseperante',
            name='s5003_infobasefgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infobaseperante_s5003_infobasefgts', to='s5003.s5003infoBaseFGTS'),
        ),
        migrations.AlterField(
            model_name='s5003infodpsfgts',
            name='s5003_evtbasesfgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infodpsfgts_s5003_evtbasesfgts', to='esocial.s5003evtBasesFGTS'),
        ),
        migrations.AlterField(
            model_name='s5003infodpsperante',
            name='perref',
            field=models.CharField(default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='s5003infodpsperante',
            name='s5003_infotrabdps',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infodpsperante_s5003_infotrabdps', to='s5003.s5003infoTrabDps'),
        ),
        migrations.AlterField(
            model_name='s5003infotrabdps',
            name='codcateg',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='s5003infotrabdps',
            name='s5003_infodpsfgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infotrabdps_s5003_infodpsfgts', to='s5003.s5003infoDpsFGTS'),
        ),
        migrations.AlterField(
            model_name='s5003infotrabfgts',
            name='codcateg',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='s5003infotrabfgts',
            name='mtvdeslig',
            field=models.CharField(blank=True, choices=[(b'01', '01 - Rescis\xe3o com justa causa, por iniciativa do empregador'), (b'02', '02 - Rescis\xe3o sem justa causa, por iniciativa do empregador'), (b'03', '03 - Rescis\xe3o antecipada do contrato a termo por iniciativa do empregador'), (b'04', '04 - Rescis\xe3o antecipada do contrato a termo por iniciativa do empregado'), (b'05', '05 - Rescis\xe3o por culpa rec\xedproca'), (b'06', '06 - Rescis\xe3o por t\xe9rmino do contrato a termo'), (b'07', '07 - Rescis\xe3o do contrato de trabalho por iniciativa do empregado'), (b'08', '08 - Rescis\xe3o do contrato de trabalho por interesse do(a) empregado(a), nas hip\xf3teses previstas nos arts. 394 e 483, \xa7 1\xba da CLT'), (b'09', '09 - Rescis\xe3o por op\xe7\xe3o do empregado em virtude de falecimento do empregador individual ou empregador dom\xe9stico'), (b'10', '10 - Rescis\xe3o por falecimento do empregado'), (b'11', '11 - Transfer\xeancia de empregado para empresa do mesmo grupo empresarial que tenha assumido os encargos trabalhistas, sem que tenha havido rescis\xe3o do contrato de trabalho'), (b'12', '12 - Transfer\xeancia de empregado da empresa consorciada para o cons\xf3rcio que tenha assumido os encargos trabalhistas, e vice-versa, sem que tenha havido rescis\xe3o do contrato de trabalho'), (b'13', '13 - Transfer\xeancia de empregado de empresa ou cons\xf3rcio, para outra empresa ou cons\xf3rcio que tenha assumido os encargos trabalhistas por motivo de sucess\xe3o (fus\xe3o, cis\xe3o ou incorpora\xe7\xe3o), sem que tenha havido rescis\xe3o do contrato de trabalho'), (b'14', '14 - Rescis\xe3o do contrato de trabalho por encerramento da empresa, de seus estabelecimentos ou supress\xe3o de parte de suas atividades ou falecimento do empregador individual ou empregador dom\xe9stico sem continua\xe7\xe3o da atividade'), (b'15', '15 - Rescis\xe3o do contrato de aprendizagem por desempenho insuficiente, inadapta\xe7\xe3o ou aus\xeancia injustificada do aprendiz \xe0 escola que implique perda do ano letivo'), (b'16', '16 - Declara\xe7\xe3o de nulidade do contrato de trabalho por infring\xeancia ao inciso II do art. 37 da Constitui\xe7\xe3o Federal, quando mantido o direito ao sal\xe1rio'), (b'17', '17 - Rescis\xe3o Indireta do Contrato de Trabalho'), (b'18', '18 - Aposentadoria Compuls\xf3ria (somente para categorias de trabalhadores 301 a 309)'), (b'19', '19 - Aposentadoria por idade (somente para categorias de trabalhadores 301 a 309)'), (b'20', '20 - Aposentadoria por idade e tempo de contribui\xe7\xe3o (somente categorias 301 a 309)'), (b'21', '21 - Reforma Militar (somente para categorias de trabalhadores 301 a 309)'), (b'22', '22 - Reserva Militar (somente para categorias de trabalhadores 301 a 309)'), (b'23', '23 - Exonera\xe7\xe3o (somente para categorias de trabalhadores 301 a 309)'), (b'24', '24 - Demiss\xe3o (somente para categorias de trabalhadores 301 a 309)'), (b'25', '25 - Vac\xe2ncia para assumir outro cargo efetivo (somente para categorias de trabalhadores 301 a 309)'), (b'26', '26 - Rescis\xe3o do contrato de trabalho por paralisa\xe7\xe3o tempor\xe1ria ou definitiva da empresa, estabelecimento ou parte das atividades motivada por atos de autoridade municipal, estadual ou federal'), (b'27', '27 - Rescis\xe3o por motivo de for\xe7a maior'), (b'28', '28 - T\xe9rmino da Cess\xe3o/Requisi\xe7\xe3o'), (b'29', '29 - Redistribui\xe7\xe3o'), (b'30', '30 - Mudan\xe7a de Regime Trabalhista'), (b'31', '31 - Revers\xe3o de Reintegra\xe7\xe3o'), (b'32', '32 - Extravio de Militar'), (b'33', '33 - Rescis\xe3o por acordo entre as partes (art. 484-A da CLT)'), (b'34', '34 - Transfer\xeancia de titularidade do empregado dom\xe9stico para outro representante da mesma unidade familiar'), (b'35', '35 - Extin\xe7\xe3o do contrato de trabalho intermitente'), (b'36', '36 - Mudan\xe7a de CPF')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infotrabfgts',
            name='mtvdesligtsv',
            field=models.CharField(blank=True, choices=[(b'01', '01'), (b'02', '02'), (b'03', '03'), (b'04', '04'), (b'05', '05'), (b'06', '06'), (b'07', '07'), (b'99', '99')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s5003infotrabfgts',
            name='s5003_ideestablot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infotrabfgts_s5003_ideestablot', to='s5003.s5003ideEstabLot'),
        ),
    ]