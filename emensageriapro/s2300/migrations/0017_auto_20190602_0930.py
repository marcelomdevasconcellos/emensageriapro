# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2300', '0016_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2300afastamento',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'dtiniafast', 'codmotafast'], 'permissions': (('can_see_list_s2300afastamento', 'Pode ver listagem do modelo S2300AFASTAMENTO'), ('can_see_data_s2300afastamento', 'Pode visualizar o conte\xfado do modelo S2300AFASTAMENTO'), ('can_see_menu_s2300afastamento', 'Pode visualizar no menu o modelo S2300AFASTAMENTO'), ('can_print_list_s2300afastamento', 'Pode imprimir listagem do modelo S2300AFASTAMENTO'), ('can_print_data_s2300afastamento', 'Pode imprimir o conte\xfado do modelo S2300AFASTAMENTO'))},
        ),
        migrations.AlterModelOptions(
            name='s2300ageintegracao',
            options={'managed': True, 'ordering': ['s2300_infoestagiario', 'cnpjagntinteg', 'nmrazao', 'dsclograd', 'nrlograd', 'cep', 'uf'], 'permissions': (('can_see_list_s2300ageIntegracao', 'Pode ver listagem do modelo S2300AGEINTEGRACAO'), ('can_see_data_s2300ageIntegracao', 'Pode visualizar o conte\xfado do modelo S2300AGEINTEGRACAO'), ('can_see_menu_s2300ageIntegracao', 'Pode visualizar no menu o modelo S2300AGEINTEGRACAO'), ('can_print_list_s2300ageIntegracao', 'Pode imprimir listagem do modelo S2300AGEINTEGRACAO'), ('can_print_data_s2300ageIntegracao', 'Pode imprimir o conte\xfado do modelo S2300AGEINTEGRACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s2300brasil',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf'], 'permissions': (('can_see_list_s2300brasil', 'Pode ver listagem do modelo S2300BRASIL'), ('can_see_data_s2300brasil', 'Pode visualizar o conte\xfado do modelo S2300BRASIL'), ('can_see_menu_s2300brasil', 'Pode visualizar no menu o modelo S2300BRASIL'), ('can_print_list_s2300brasil', 'Pode imprimir listagem do modelo S2300BRASIL'), ('can_print_data_s2300brasil', 'Pode imprimir o conte\xfado do modelo S2300BRASIL'))},
        ),
        migrations.AlterModelOptions(
            name='s2300cargofuncao',
            options={'managed': True, 'ordering': ['s2300_infocomplementares', 'codcargo'], 'permissions': (('can_see_list_s2300cargoFuncao', 'Pode ver listagem do modelo S2300CARGOFUNCAO'), ('can_see_data_s2300cargoFuncao', 'Pode visualizar o conte\xfado do modelo S2300CARGOFUNCAO'), ('can_see_menu_s2300cargoFuncao', 'Pode visualizar no menu o modelo S2300CARGOFUNCAO'), ('can_print_list_s2300cargoFuncao', 'Pode imprimir listagem do modelo S2300CARGOFUNCAO'), ('can_print_data_s2300cargoFuncao', 'Pode imprimir o conte\xfado do modelo S2300CARGOFUNCAO'))},
        ),
        migrations.AlterModelOptions(
            name='s2300cnh',
            options={'managed': True, 'ordering': ['s2300_documentos', 'nrregcnh', 'ufcnh', 'dtvalid', 'categoriacnh'], 'permissions': (('can_see_list_s2300CNH', 'Pode ver listagem do modelo S2300CNH'), ('can_see_data_s2300CNH', 'Pode visualizar o conte\xfado do modelo S2300CNH'), ('can_see_menu_s2300CNH', 'Pode visualizar no menu o modelo S2300CNH'), ('can_print_list_s2300CNH', 'Pode imprimir listagem do modelo S2300CNH'), ('can_print_data_s2300CNH', 'Pode imprimir o conte\xfado do modelo S2300CNH'))},
        ),
        migrations.AlterModelOptions(
            name='s2300contato',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio'], 'permissions': (('can_see_list_s2300contato', 'Pode ver listagem do modelo S2300CONTATO'), ('can_see_data_s2300contato', 'Pode visualizar o conte\xfado do modelo S2300CONTATO'), ('can_see_menu_s2300contato', 'Pode visualizar no menu o modelo S2300CONTATO'), ('can_print_list_s2300contato', 'Pode imprimir listagem do modelo S2300CONTATO'), ('can_print_data_s2300contato', 'Pode imprimir o conte\xfado do modelo S2300CONTATO'))},
        ),
        migrations.AlterModelOptions(
            name='s2300ctps',
            options={'managed': True, 'ordering': ['s2300_documentos', 'nrctps', 'seriectps', 'ufctps'], 'permissions': (('can_see_list_s2300CTPS', 'Pode ver listagem do modelo S2300CTPS'), ('can_see_data_s2300CTPS', 'Pode visualizar o conte\xfado do modelo S2300CTPS'), ('can_see_menu_s2300CTPS', 'Pode visualizar no menu o modelo S2300CTPS'), ('can_print_list_s2300CTPS', 'Pode imprimir listagem do modelo S2300CTPS'), ('can_print_data_s2300CTPS', 'Pode imprimir o conte\xfado do modelo S2300CTPS'))},
        ),
        migrations.AlterModelOptions(
            name='s2300dependente',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'tpdep', 'nmdep', 'dtnascto', 'depirrf', 'depsf', 'inctrab'], 'permissions': (('can_see_list_s2300dependente', 'Pode ver listagem do modelo S2300DEPENDENTE'), ('can_see_data_s2300dependente', 'Pode visualizar o conte\xfado do modelo S2300DEPENDENTE'), ('can_see_menu_s2300dependente', 'Pode visualizar no menu o modelo S2300DEPENDENTE'), ('can_print_list_s2300dependente', 'Pode imprimir listagem do modelo S2300DEPENDENTE'), ('can_print_data_s2300dependente', 'Pode imprimir o conte\xfado do modelo S2300DEPENDENTE'))},
        ),
        migrations.AlterModelOptions(
            name='s2300documentos',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio'], 'permissions': (('can_see_list_s2300documentos', 'Pode ver listagem do modelo S2300DOCUMENTOS'), ('can_see_data_s2300documentos', 'Pode visualizar o conte\xfado do modelo S2300DOCUMENTOS'), ('can_see_menu_s2300documentos', 'Pode visualizar no menu o modelo S2300DOCUMENTOS'), ('can_print_list_s2300documentos', 'Pode imprimir listagem do modelo S2300DOCUMENTOS'), ('can_print_data_s2300documentos', 'Pode imprimir o conte\xfado do modelo S2300DOCUMENTOS'))},
        ),
        migrations.AlterModelOptions(
            name='s2300exterior',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'paisresid', 'dsclograd', 'nrlograd', 'nmcid'], 'permissions': (('can_see_list_s2300exterior', 'Pode ver listagem do modelo S2300EXTERIOR'), ('can_see_data_s2300exterior', 'Pode visualizar o conte\xfado do modelo S2300EXTERIOR'), ('can_see_menu_s2300exterior', 'Pode visualizar no menu o modelo S2300EXTERIOR'), ('can_print_list_s2300exterior', 'Pode imprimir listagem do modelo S2300EXTERIOR'), ('can_print_data_s2300exterior', 'Pode imprimir o conte\xfado do modelo S2300EXTERIOR'))},
        ),
        migrations.AlterModelOptions(
            name='s2300fgts',
            options={'managed': True, 'ordering': ['s2300_infocomplementares', 'opcfgts'], 'permissions': (('can_see_list_s2300fgts', 'Pode ver listagem do modelo S2300FGTS'), ('can_see_data_s2300fgts', 'Pode visualizar o conte\xfado do modelo S2300FGTS'), ('can_see_menu_s2300fgts', 'Pode visualizar no menu o modelo S2300FGTS'), ('can_print_list_s2300fgts', 'Pode imprimir listagem do modelo S2300FGTS'), ('can_print_data_s2300fgts', 'Pode imprimir o conte\xfado do modelo S2300FGTS'))},
        ),
        migrations.AlterModelOptions(
            name='s2300infocomplementares',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio'], 'permissions': (('can_see_list_s2300infoComplementares', 'Pode ver listagem do modelo S2300INFOCOMPLEMENTARES'), ('can_see_data_s2300infoComplementares', 'Pode visualizar o conte\xfado do modelo S2300INFOCOMPLEMENTARES'), ('can_see_menu_s2300infoComplementares', 'Pode visualizar no menu o modelo S2300INFOCOMPLEMENTARES'), ('can_print_list_s2300infoComplementares', 'Pode imprimir listagem do modelo S2300INFOCOMPLEMENTARES'), ('can_print_data_s2300infoComplementares', 'Pode imprimir o conte\xfado do modelo S2300INFOCOMPLEMENTARES'))},
        ),
        migrations.AlterModelOptions(
            name='s2300infodeficiencia',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'deffisica', 'defvisual', 'defauditiva', 'defmental', 'defintelectual', 'reabreadap'], 'permissions': (('can_see_list_s2300infoDeficiencia', 'Pode ver listagem do modelo S2300INFODEFICIENCIA'), ('can_see_data_s2300infoDeficiencia', 'Pode visualizar o conte\xfado do modelo S2300INFODEFICIENCIA'), ('can_see_menu_s2300infoDeficiencia', 'Pode visualizar no menu o modelo S2300INFODEFICIENCIA'), ('can_print_list_s2300infoDeficiencia', 'Pode imprimir listagem do modelo S2300INFODEFICIENCIA'), ('can_print_data_s2300infoDeficiencia', 'Pode imprimir o conte\xfado do modelo S2300INFODEFICIENCIA'))},
        ),
        migrations.AlterModelOptions(
            name='s2300infodirigentesindical',
            options={'managed': True, 'ordering': ['s2300_infocomplementares', 'categorig'], 'permissions': (('can_see_list_s2300infoDirigenteSindical', 'Pode ver listagem do modelo S2300INFODIRIGENTESINDICAL'), ('can_see_data_s2300infoDirigenteSindical', 'Pode visualizar o conte\xfado do modelo S2300INFODIRIGENTESINDICAL'), ('can_see_menu_s2300infoDirigenteSindical', 'Pode visualizar no menu o modelo S2300INFODIRIGENTESINDICAL'), ('can_print_list_s2300infoDirigenteSindical', 'Pode imprimir listagem do modelo S2300INFODIRIGENTESINDICAL'), ('can_print_data_s2300infoDirigenteSindical', 'Pode imprimir o conte\xfado do modelo S2300INFODIRIGENTESINDICAL'))},
        ),
        migrations.AlterModelOptions(
            name='s2300infoestagiario',
            options={'managed': True, 'ordering': ['s2300_infocomplementares', 'natestagio', 'nivestagio', 'dtprevterm', 'nmrazao'], 'permissions': (('can_see_list_s2300infoEstagiario', 'Pode ver listagem do modelo S2300INFOESTAGIARIO'), ('can_see_data_s2300infoEstagiario', 'Pode visualizar o conte\xfado do modelo S2300INFOESTAGIARIO'), ('can_see_menu_s2300infoEstagiario', 'Pode visualizar no menu o modelo S2300INFOESTAGIARIO'), ('can_print_list_s2300infoEstagiario', 'Pode imprimir listagem do modelo S2300INFOESTAGIARIO'), ('can_print_data_s2300infoEstagiario', 'Pode imprimir o conte\xfado do modelo S2300INFOESTAGIARIO'))},
        ),
        migrations.AlterModelOptions(
            name='s2300infotrabcedido',
            options={'managed': True, 'ordering': ['s2300_infocomplementares', 'categorig', 'cnpjcednt', 'matricced', 'dtadmced', 'tpregtrab', 'tpregprev', 'infonus'], 'permissions': (('can_see_list_s2300infoTrabCedido', 'Pode ver listagem do modelo S2300INFOTRABCEDIDO'), ('can_see_data_s2300infoTrabCedido', 'Pode visualizar o conte\xfado do modelo S2300INFOTRABCEDIDO'), ('can_see_menu_s2300infoTrabCedido', 'Pode visualizar no menu o modelo S2300INFOTRABCEDIDO'), ('can_print_list_s2300infoTrabCedido', 'Pode imprimir listagem do modelo S2300INFOTRABCEDIDO'), ('can_print_data_s2300infoTrabCedido', 'Pode imprimir o conte\xfado do modelo S2300INFOTRABCEDIDO'))},
        ),
        migrations.AlterModelOptions(
            name='s2300mudancacpf',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'cpfant', 'dtaltcpf'], 'permissions': (('can_see_list_s2300mudancaCPF', 'Pode ver listagem do modelo S2300MUDANCACPF'), ('can_see_data_s2300mudancaCPF', 'Pode visualizar o conte\xfado do modelo S2300MUDANCACPF'), ('can_see_menu_s2300mudancaCPF', 'Pode visualizar no menu o modelo S2300MUDANCACPF'), ('can_print_list_s2300mudancaCPF', 'Pode imprimir listagem do modelo S2300MUDANCACPF'), ('can_print_data_s2300mudancaCPF', 'Pode imprimir o conte\xfado do modelo S2300MUDANCACPF'))},
        ),
        migrations.AlterModelOptions(
            name='s2300oc',
            options={'managed': True, 'ordering': ['s2300_documentos', 'nroc', 'orgaoemissor'], 'permissions': (('can_see_list_s2300OC', 'Pode ver listagem do modelo S2300OC'), ('can_see_data_s2300OC', 'Pode visualizar o conte\xfado do modelo S2300OC'), ('can_see_menu_s2300OC', 'Pode visualizar no menu o modelo S2300OC'), ('can_print_list_s2300OC', 'Pode imprimir listagem do modelo S2300OC'), ('can_print_data_s2300OC', 'Pode imprimir o conte\xfado do modelo S2300OC'))},
        ),
        migrations.AlterModelOptions(
            name='s2300remuneracao',
            options={'managed': True, 'ordering': ['s2300_infocomplementares', 'vrsalfx', 'undsalfixo'], 'permissions': (('can_see_list_s2300remuneracao', 'Pode ver listagem do modelo S2300REMUNERACAO'), ('can_see_data_s2300remuneracao', 'Pode visualizar o conte\xfado do modelo S2300REMUNERACAO'), ('can_see_menu_s2300remuneracao', 'Pode visualizar no menu o modelo S2300REMUNERACAO'), ('can_print_list_s2300remuneracao', 'Pode imprimir listagem do modelo S2300REMUNERACAO'), ('can_print_data_s2300remuneracao', 'Pode imprimir o conte\xfado do modelo S2300REMUNERACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s2300rg',
            options={'managed': True, 'ordering': ['s2300_documentos', 'nrrg', 'orgaoemissor'], 'permissions': (('can_see_list_s2300RG', 'Pode ver listagem do modelo S2300RG'), ('can_see_data_s2300RG', 'Pode visualizar o conte\xfado do modelo S2300RG'), ('can_see_menu_s2300RG', 'Pode visualizar no menu o modelo S2300RG'), ('can_print_list_s2300RG', 'Pode imprimir listagem do modelo S2300RG'), ('can_print_data_s2300RG', 'Pode imprimir o conte\xfado do modelo S2300RG'))},
        ),
        migrations.AlterModelOptions(
            name='s2300ric',
            options={'managed': True, 'ordering': ['s2300_documentos', 'nrric', 'orgaoemissor'], 'permissions': (('can_see_list_s2300RIC', 'Pode ver listagem do modelo S2300RIC'), ('can_see_data_s2300RIC', 'Pode visualizar o conte\xfado do modelo S2300RIC'), ('can_see_menu_s2300RIC', 'Pode visualizar no menu o modelo S2300RIC'), ('can_print_list_s2300RIC', 'Pode imprimir listagem do modelo S2300RIC'), ('can_print_data_s2300RIC', 'Pode imprimir o conte\xfado do modelo S2300RIC'))},
        ),
        migrations.AlterModelOptions(
            name='s2300rne',
            options={'managed': True, 'ordering': ['s2300_documentos', 'nrrne', 'orgaoemissor'], 'permissions': (('can_see_list_s2300RNE', 'Pode ver listagem do modelo S2300RNE'), ('can_see_data_s2300RNE', 'Pode visualizar o conte\xfado do modelo S2300RNE'), ('can_see_menu_s2300RNE', 'Pode visualizar no menu o modelo S2300RNE'), ('can_print_list_s2300RNE', 'Pode imprimir listagem do modelo S2300RNE'), ('can_print_data_s2300RNE', 'Pode imprimir o conte\xfado do modelo S2300RNE'))},
        ),
        migrations.AlterModelOptions(
            name='s2300supervisorestagio',
            options={'managed': True, 'ordering': ['s2300_infoestagiario', 'cpfsupervisor', 'nmsuperv'], 'permissions': (('can_see_list_s2300supervisorEstagio', 'Pode ver listagem do modelo S2300SUPERVISORESTAGIO'), ('can_see_data_s2300supervisorEstagio', 'Pode visualizar o conte\xfado do modelo S2300SUPERVISORESTAGIO'), ('can_see_menu_s2300supervisorEstagio', 'Pode visualizar no menu o modelo S2300SUPERVISORESTAGIO'), ('can_print_list_s2300supervisorEstagio', 'Pode imprimir listagem do modelo S2300SUPERVISORESTAGIO'), ('can_print_data_s2300supervisorEstagio', 'Pode imprimir o conte\xfado do modelo S2300SUPERVISORESTAGIO'))},
        ),
        migrations.AlterModelOptions(
            name='s2300termino',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'dtterm'], 'permissions': (('can_see_list_s2300termino', 'Pode ver listagem do modelo S2300TERMINO'), ('can_see_data_s2300termino', 'Pode visualizar o conte\xfado do modelo S2300TERMINO'), ('can_see_menu_s2300termino', 'Pode visualizar no menu o modelo S2300TERMINO'), ('can_print_list_s2300termino', 'Pode imprimir listagem do modelo S2300TERMINO'), ('can_print_data_s2300termino', 'Pode imprimir o conte\xfado do modelo S2300TERMINO'))},
        ),
        migrations.AlterModelOptions(
            name='s2300trabestrangeiro',
            options={'managed': True, 'ordering': ['s2300_evttsvinicio', 'classtrabestrang', 'casadobr', 'filhosbr'], 'permissions': (('can_see_list_s2300trabEstrangeiro', 'Pode ver listagem do modelo S2300TRABESTRANGEIRO'), ('can_see_data_s2300trabEstrangeiro', 'Pode visualizar o conte\xfado do modelo S2300TRABESTRANGEIRO'), ('can_see_menu_s2300trabEstrangeiro', 'Pode visualizar no menu o modelo S2300TRABESTRANGEIRO'), ('can_print_list_s2300trabEstrangeiro', 'Pode imprimir listagem do modelo S2300TRABESTRANGEIRO'), ('can_print_data_s2300trabEstrangeiro', 'Pode imprimir o conte\xfado do modelo S2300TRABESTRANGEIRO'))},
        ),
    ]
