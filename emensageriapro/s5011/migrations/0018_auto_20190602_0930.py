# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5011', '0017_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s5011basesaquis',
            options={'managed': True, 'ordering': ['s5011_ideestab', 'indaquis', 'vlraquis', 'vrcpdescpr', 'vrcpnret', 'vrratnret', 'vrsenarnret', 'vrcpcalcpr', 'vrratdescpr', 'vrratcalcpr', 'vrsenardesc', 'vrsenarcalc'], 'permissions': (('can_see_list_s5011basesAquis', 'Pode ver listagem do modelo S5011BASESAQUIS'), ('can_see_data_s5011basesAquis', 'Pode visualizar o conte\xfado do modelo S5011BASESAQUIS'), ('can_see_menu_s5011basesAquis', 'Pode visualizar no menu o modelo S5011BASESAQUIS'), ('can_print_list_s5011basesAquis', 'Pode imprimir listagem do modelo S5011BASESAQUIS'), ('can_print_data_s5011basesAquis', 'Pode imprimir o conte\xfado do modelo S5011BASESAQUIS'))},
        ),
        migrations.AlterModelOptions(
            name='s5011basesavnport',
            options={'managed': True, 'ordering': ['s5011_idelotacao', 'vrbccp00', 'vrbccp15', 'vrbccp20', 'vrbccp25', 'vrbccp13', 'vrbcfgts', 'vrdesccp'], 'permissions': (('can_see_list_s5011basesAvNPort', 'Pode ver listagem do modelo S5011BASESAVNPORT'), ('can_see_data_s5011basesAvNPort', 'Pode visualizar o conte\xfado do modelo S5011BASESAVNPORT'), ('can_see_menu_s5011basesAvNPort', 'Pode visualizar no menu o modelo S5011BASESAVNPORT'), ('can_print_list_s5011basesAvNPort', 'Pode imprimir listagem do modelo S5011BASESAVNPORT'), ('can_print_data_s5011basesAvNPort', 'Pode imprimir o conte\xfado do modelo S5011BASESAVNPORT'))},
        ),
        migrations.AlterModelOptions(
            name='s5011basescomerc',
            options={'managed': True, 'ordering': ['s5011_ideestab', 'indcomerc', 'vrbccompr'], 'permissions': (('can_see_list_s5011basesComerc', 'Pode ver listagem do modelo S5011BASESCOMERC'), ('can_see_data_s5011basesComerc', 'Pode visualizar o conte\xfado do modelo S5011BASESCOMERC'), ('can_see_menu_s5011basesComerc', 'Pode visualizar no menu o modelo S5011BASESCOMERC'), ('can_print_list_s5011basesComerc', 'Pode imprimir listagem do modelo S5011BASESCOMERC'), ('can_print_data_s5011basesComerc', 'Pode imprimir o conte\xfado do modelo S5011BASESCOMERC'))},
        ),
        migrations.AlterModelOptions(
            name='s5011basesremun',
            options={'managed': True, 'ordering': ['s5011_idelotacao', 'indincid', 'codcateg', 'vrbccp00', 'vrbccp15', 'vrbccp20', 'vrbccp25', 'vrsuspbccp00', 'vrsuspbccp15', 'vrsuspbccp20', 'vrsuspbccp25', 'vrdescsest', 'vrcalcsest', 'vrdescsenat', 'vrcalcsenat', 'vrsalfam', 'vrsalmat'], 'permissions': (('can_see_list_s5011basesRemun', 'Pode ver listagem do modelo S5011BASESREMUN'), ('can_see_data_s5011basesRemun', 'Pode visualizar o conte\xfado do modelo S5011BASESREMUN'), ('can_see_menu_s5011basesRemun', 'Pode visualizar no menu o modelo S5011BASESREMUN'), ('can_print_list_s5011basesRemun', 'Pode imprimir listagem do modelo S5011BASESREMUN'), ('can_print_data_s5011basesRemun', 'Pode imprimir o conte\xfado do modelo S5011BASESREMUN'))},
        ),
        migrations.AlterModelOptions(
            name='s5011dadosopport',
            options={'managed': True, 'ordering': ['s5011_idelotacao', 'cnpjopportuario', 'aliqrat', 'fap', 'aliqratajust'], 'permissions': (('can_see_list_s5011dadosOpPort', 'Pode ver listagem do modelo S5011DADOSOPPORT'), ('can_see_data_s5011dadosOpPort', 'Pode visualizar o conte\xfado do modelo S5011DADOSOPPORT'), ('can_see_menu_s5011dadosOpPort', 'Pode visualizar no menu o modelo S5011DADOSOPPORT'), ('can_print_list_s5011dadosOpPort', 'Pode imprimir listagem do modelo S5011DADOSOPPORT'), ('can_print_data_s5011dadosOpPort', 'Pode imprimir o conte\xfado do modelo S5011DADOSOPPORT'))},
        ),
        migrations.AlterModelOptions(
            name='s5011ideestab',
            options={'managed': True, 'ordering': ['s5011_evtcs', 'tpinsc', 'nrinsc'], 'permissions': (('can_see_list_s5011ideEstab', 'Pode ver listagem do modelo S5011IDEESTAB'), ('can_see_data_s5011ideEstab', 'Pode visualizar o conte\xfado do modelo S5011IDEESTAB'), ('can_see_menu_s5011ideEstab', 'Pode visualizar no menu o modelo S5011IDEESTAB'), ('can_print_list_s5011ideEstab', 'Pode imprimir listagem do modelo S5011IDEESTAB'), ('can_print_data_s5011ideEstab', 'Pode imprimir o conte\xfado do modelo S5011IDEESTAB'))},
        ),
        migrations.AlterModelOptions(
            name='s5011idelotacao',
            options={'managed': True, 'ordering': ['s5011_ideestab', 'codlotacao', 'fpas', 'codtercs'], 'permissions': (('can_see_list_s5011ideLotacao', 'Pode ver listagem do modelo S5011IDELOTACAO'), ('can_see_data_s5011ideLotacao', 'Pode visualizar o conte\xfado do modelo S5011IDELOTACAO'), ('can_see_menu_s5011ideLotacao', 'Pode visualizar no menu o modelo S5011IDELOTACAO'), ('can_print_list_s5011ideLotacao', 'Pode imprimir listagem do modelo S5011IDELOTACAO'), ('can_print_data_s5011ideLotacao', 'Pode imprimir o conte\xfado do modelo S5011IDELOTACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infoatconc',
            options={'managed': True, 'ordering': ['s5011_infopj', 'fatormes', 'fator13'], 'permissions': (('can_see_list_s5011infoAtConc', 'Pode ver listagem do modelo S5011INFOATCONC'), ('can_see_data_s5011infoAtConc', 'Pode visualizar o conte\xfado do modelo S5011INFOATCONC'), ('can_see_menu_s5011infoAtConc', 'Pode visualizar no menu o modelo S5011INFOATCONC'), ('can_print_list_s5011infoAtConc', 'Pode imprimir listagem do modelo S5011INFOATCONC'), ('can_print_data_s5011infoAtConc', 'Pode imprimir o conte\xfado do modelo S5011INFOATCONC'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infocomplobra',
            options={'managed': True, 'ordering': ['s5011_infoestab', 'indsubstpatrobra'], 'permissions': (('can_see_list_s5011infoComplObra', 'Pode ver listagem do modelo S5011INFOCOMPLOBRA'), ('can_see_data_s5011infoComplObra', 'Pode visualizar o conte\xfado do modelo S5011INFOCOMPLOBRA'), ('can_see_menu_s5011infoComplObra', 'Pode visualizar no menu o modelo S5011INFOCOMPLOBRA'), ('can_print_list_s5011infoComplObra', 'Pode imprimir listagem do modelo S5011INFOCOMPLOBRA'), ('can_print_data_s5011infoComplObra', 'Pode imprimir o conte\xfado do modelo S5011INFOCOMPLOBRA'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infocpseg',
            options={'managed': True, 'ordering': ['s5011_evtcs', 'vrdesccp', 'vrcpseg'], 'permissions': (('can_see_list_s5011infoCPSeg', 'Pode ver listagem do modelo S5011INFOCPSEG'), ('can_see_data_s5011infoCPSeg', 'Pode visualizar o conte\xfado do modelo S5011INFOCPSEG'), ('can_see_menu_s5011infoCPSeg', 'Pode visualizar no menu o modelo S5011INFOCPSEG'), ('can_print_list_s5011infoCPSeg', 'Pode imprimir listagem do modelo S5011INFOCPSEG'), ('can_print_data_s5011infoCPSeg', 'Pode imprimir o conte\xfado do modelo S5011INFOCPSEG'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infocrcontrib',
            options={'managed': True, 'ordering': ['s5011_evtcs', 'tpcr', 'vrcr'], 'permissions': (('can_see_list_s5011infoCRContrib', 'Pode ver listagem do modelo S5011INFOCRCONTRIB'), ('can_see_data_s5011infoCRContrib', 'Pode visualizar o conte\xfado do modelo S5011INFOCRCONTRIB'), ('can_see_menu_s5011infoCRContrib', 'Pode visualizar no menu o modelo S5011INFOCRCONTRIB'), ('can_print_list_s5011infoCRContrib', 'Pode imprimir listagem do modelo S5011INFOCRCONTRIB'), ('can_print_data_s5011infoCRContrib', 'Pode imprimir o conte\xfado do modelo S5011INFOCRCONTRIB'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infocrestab',
            options={'managed': True, 'ordering': ['s5011_ideestab', 'tpcr', 'vrcr'], 'permissions': (('can_see_list_s5011infoCREstab', 'Pode ver listagem do modelo S5011INFOCRESTAB'), ('can_see_data_s5011infoCREstab', 'Pode visualizar o conte\xfado do modelo S5011INFOCRESTAB'), ('can_see_menu_s5011infoCREstab', 'Pode visualizar no menu o modelo S5011INFOCRESTAB'), ('can_print_list_s5011infoCREstab', 'Pode imprimir listagem do modelo S5011INFOCRESTAB'), ('can_print_data_s5011infoCREstab', 'Pode imprimir o conte\xfado do modelo S5011INFOCRESTAB'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infoemprparcial',
            options={'managed': True, 'ordering': ['s5011_idelotacao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop', 'cnoobra'], 'permissions': (('can_see_list_s5011infoEmprParcial', 'Pode ver listagem do modelo S5011INFOEMPRPARCIAL'), ('can_see_data_s5011infoEmprParcial', 'Pode visualizar o conte\xfado do modelo S5011INFOEMPRPARCIAL'), ('can_see_menu_s5011infoEmprParcial', 'Pode visualizar no menu o modelo S5011INFOEMPRPARCIAL'), ('can_print_list_s5011infoEmprParcial', 'Pode imprimir listagem do modelo S5011INFOEMPRPARCIAL'), ('can_print_data_s5011infoEmprParcial', 'Pode imprimir o conte\xfado do modelo S5011INFOEMPRPARCIAL'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infoestab',
            options={'managed': True, 'ordering': ['s5011_ideestab', 'cnaeprep', 'aliqrat', 'fap', 'aliqratajust'], 'permissions': (('can_see_list_s5011infoEstab', 'Pode ver listagem do modelo S5011INFOESTAB'), ('can_see_data_s5011infoEstab', 'Pode visualizar o conte\xfado do modelo S5011INFOESTAB'), ('can_see_menu_s5011infoEstab', 'Pode visualizar no menu o modelo S5011INFOESTAB'), ('can_print_list_s5011infoEstab', 'Pode imprimir listagem do modelo S5011INFOESTAB'), ('can_print_data_s5011infoEstab', 'Pode imprimir o conte\xfado do modelo S5011INFOESTAB'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infopj',
            options={'managed': True, 'ordering': ['s5011_evtcs', 'indconstr'], 'permissions': (('can_see_list_s5011infoPJ', 'Pode ver listagem do modelo S5011INFOPJ'), ('can_see_data_s5011infoPJ', 'Pode visualizar o conte\xfado do modelo S5011INFOPJ'), ('can_see_menu_s5011infoPJ', 'Pode visualizar no menu o modelo S5011INFOPJ'), ('can_print_list_s5011infoPJ', 'Pode imprimir listagem do modelo S5011INFOPJ'), ('can_print_data_s5011infoPJ', 'Pode imprimir o conte\xfado do modelo S5011INFOPJ'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infosubstpatropport',
            options={'managed': True, 'ordering': ['s5011_idelotacao', 'cnpjopportuario'], 'permissions': (('can_see_list_s5011infoSubstPatrOpPort', 'Pode ver listagem do modelo S5011INFOSUBSTPATROPPORT'), ('can_see_data_s5011infoSubstPatrOpPort', 'Pode visualizar o conte\xfado do modelo S5011INFOSUBSTPATROPPORT'), ('can_see_menu_s5011infoSubstPatrOpPort', 'Pode visualizar no menu o modelo S5011INFOSUBSTPATROPPORT'), ('can_print_list_s5011infoSubstPatrOpPort', 'Pode imprimir listagem do modelo S5011INFOSUBSTPATROPPORT'), ('can_print_data_s5011infoSubstPatrOpPort', 'Pode imprimir o conte\xfado do modelo S5011INFOSUBSTPATROPPORT'))},
        ),
        migrations.AlterModelOptions(
            name='s5011infotercsusp',
            options={'managed': True, 'ordering': ['s5011_idelotacao', 'codterc'], 'permissions': (('can_see_list_s5011infoTercSusp', 'Pode ver listagem do modelo S5011INFOTERCSUSP'), ('can_see_data_s5011infoTercSusp', 'Pode visualizar o conte\xfado do modelo S5011INFOTERCSUSP'), ('can_see_menu_s5011infoTercSusp', 'Pode visualizar no menu o modelo S5011INFOTERCSUSP'), ('can_print_list_s5011infoTercSusp', 'Pode imprimir listagem do modelo S5011INFOTERCSUSP'), ('can_print_data_s5011infoTercSusp', 'Pode imprimir o conte\xfado do modelo S5011INFOTERCSUSP'))},
        ),
    ]
