#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64
from emensageriapro.esocial.models import s1000evtInfoEmpregador
from emensageriapro.esocial.models import s1005evtTabEstab
from emensageriapro.esocial.models import s1010evtTabRubrica
from emensageriapro.esocial.models import s1020evtTabLotacao
from emensageriapro.esocial.models import s1030evtTabCargo
from emensageriapro.esocial.models import s1035evtTabCarreira
from emensageriapro.esocial.models import s1040evtTabFuncao
from emensageriapro.esocial.models import s1050evtTabHorTur
from emensageriapro.esocial.models import s1060evtTabAmbiente
from emensageriapro.esocial.models import s1070evtTabProcesso
from emensageriapro.esocial.models import s1080evtTabOperPort
from emensageriapro.esocial.models import s1200evtRemun
from emensageriapro.esocial.models import s1202evtRmnRPPS
from emensageriapro.esocial.models import s1207evtBenPrRP
from emensageriapro.esocial.models import s1210evtPgtos
from emensageriapro.esocial.models import s1250evtAqProd
from emensageriapro.esocial.models import s1260evtComProd
from emensageriapro.esocial.models import s1270evtContratAvNP
from emensageriapro.esocial.models import s1280evtInfoComplPer
from emensageriapro.esocial.models import s1295evtTotConting
from emensageriapro.esocial.models import s1298evtReabreEvPer
from emensageriapro.esocial.models import s1299evtFechaEvPer
from emensageriapro.esocial.models import s1300evtContrSindPatr
from emensageriapro.esocial.models import s2190evtAdmPrelim
from emensageriapro.esocial.models import s2200evtAdmissao
from emensageriapro.esocial.models import s2205evtAltCadastral
from emensageriapro.esocial.models import s2206evtAltContratual
from emensageriapro.esocial.models import s2210evtCAT
from emensageriapro.esocial.models import s2220evtMonit
from emensageriapro.esocial.models import s2230evtAfastTemp
from emensageriapro.esocial.models import s2240evtExpRisco
from emensageriapro.esocial.models import s2241evtInsApo
from emensageriapro.esocial.models import s2250evtAvPrevio
from emensageriapro.esocial.models import s2260evtConvInterm
from emensageriapro.esocial.models import s2298evtReintegr
from emensageriapro.esocial.models import s2299evtDeslig
from emensageriapro.esocial.models import s2300evtTSVInicio
from emensageriapro.esocial.models import s2306evtTSVAltContr
from emensageriapro.esocial.models import s2399evtTSVTermino
from emensageriapro.esocial.models import s2400evtCdBenPrRP
from emensageriapro.esocial.models import s3000evtExclusao
from emensageriapro.esocial.models import s5001evtBasesTrab
from emensageriapro.esocial.models import s5002evtIrrfBenef
from emensageriapro.esocial.models import s5011evtCS
from emensageriapro.esocial.models import s5012evtIrrf
from emensageriapro.esocial.forms import form_s1000_evtinfoempregador
from emensageriapro.esocial.forms import form_s1005_evttabestab
from emensageriapro.esocial.forms import form_s1010_evttabrubrica
from emensageriapro.esocial.forms import form_s1020_evttablotacao
from emensageriapro.esocial.forms import form_s1030_evttabcargo
from emensageriapro.esocial.forms import form_s1035_evttabcarreira
from emensageriapro.esocial.forms import form_s1040_evttabfuncao
from emensageriapro.esocial.forms import form_s1050_evttabhortur
from emensageriapro.esocial.forms import form_s1060_evttabambiente
from emensageriapro.esocial.forms import form_s1070_evttabprocesso
from emensageriapro.esocial.forms import form_s1080_evttaboperport
from emensageriapro.esocial.forms import form_s1200_evtremun
from emensageriapro.esocial.forms import form_s1202_evtrmnrpps
from emensageriapro.esocial.forms import form_s1207_evtbenprrp
from emensageriapro.esocial.forms import form_s1210_evtpgtos
from emensageriapro.esocial.forms import form_s1250_evtaqprod
from emensageriapro.esocial.forms import form_s1260_evtcomprod
from emensageriapro.esocial.forms import form_s1270_evtcontratavnp
from emensageriapro.esocial.forms import form_s1280_evtinfocomplper
from emensageriapro.esocial.forms import form_s1295_evttotconting
from emensageriapro.esocial.forms import form_s1298_evtreabreevper
from emensageriapro.esocial.forms import form_s1299_evtfechaevper
from emensageriapro.esocial.forms import form_s1300_evtcontrsindpatr
from emensageriapro.esocial.forms import form_s2190_evtadmprelim
from emensageriapro.esocial.forms import form_s2200_evtadmissao
from emensageriapro.esocial.forms import form_s2205_evtaltcadastral
from emensageriapro.esocial.forms import form_s2206_evtaltcontratual
from emensageriapro.esocial.forms import form_s2210_evtcat
from emensageriapro.esocial.forms import form_s2220_evtmonit
from emensageriapro.esocial.forms import form_s2230_evtafasttemp
from emensageriapro.esocial.forms import form_s2240_evtexprisco
from emensageriapro.esocial.forms import form_s2241_evtinsapo
from emensageriapro.esocial.forms import form_s2250_evtavprevio
from emensageriapro.esocial.forms import form_s2260_evtconvinterm
from emensageriapro.esocial.forms import form_s2298_evtreintegr
from emensageriapro.esocial.forms import form_s2299_evtdeslig
from emensageriapro.esocial.forms import form_s2300_evttsvinicio
from emensageriapro.esocial.forms import form_s2306_evttsvaltcontr
from emensageriapro.esocial.forms import form_s2399_evttsvtermino
from emensageriapro.esocial.forms import form_s2400_evtcdbenprrp
from emensageriapro.esocial.forms import form_s3000_evtexclusao
from emensageriapro.esocial.forms import form_s5001_evtbasestrab
from emensageriapro.esocial.forms import form_s5002_evtirrfbenef
from emensageriapro.esocial.forms import form_s5011_evtcs
from emensageriapro.esocial.forms import form_s5012_evtirrf

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        retornos_eventos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='retornos_eventos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    retornos_eventos = get_object_or_404(RetornosEventos.objects.using( db_slug ), excluido = False, id = retornos_eventos_id)
    if request.method == 'POST':
        RetornosEventos.objects.using( db_slug ).filter(id = retornos_eventos_id).update(excluido = True)
        #retornos_eventos_apagar_custom
        #retornos_eventos_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'retornos_eventos_salvar':
            return redirect('retornos_eventos', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,

        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'retornos_eventos_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        retornos_eventos_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='retornos_eventos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if retornos_eventos_id:
        retornos_eventos = get_object_or_404(RetornosEventos.objects.using( db_slug ), excluido = False, id = retornos_eventos_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if retornos_eventos_id:
            retornos_eventos_form = form_retornos_eventos(request.POST or None, instance = retornos_eventos, slug = db_slug)
        else:
            retornos_eventos_form = form_retornos_eventos(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if retornos_eventos_form.is_valid():
                dados = retornos_eventos_form.cleaned_data
                if retornos_eventos_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #retornos_eventos_campos_multiple_passo1
                    RetornosEventos.objects.using(db_slug).filter(id=retornos_eventos_id).update(**dados)
                    obj = RetornosEventos.objects.using(db_slug).get(id=retornos_eventos_id)
                    #retornos_eventos_editar_custom
                    #retornos_eventos_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #retornos_eventos_cadastrar_campos_multiple_passo1
                    obj = RetornosEventos(**dados)
                    obj.save(using = db_slug)
                    #retornos_eventos_cadastrar_custom
                    #retornos_eventos_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('retornos_eventos_apagar', 'retornos_eventos_salvar', 'retornos_eventos'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if retornos_eventos_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('retornos_eventos_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        retornos_eventos_form = disabled_form_fields(retornos_eventos_form, permissao.permite_editar)
        #retornos_eventos_campos_multiple_passo3

        for field in retornos_eventos_form.fields.keys():
            retornos_eventos_form.fields[field].widget.attrs['ng-model'] = 'retornos_eventos_'+field
        if int(dict_hash['print']):
            retornos_eventos_form = disabled_form_for_print(retornos_eventos_form)

        retornos_eventos_ocorrencias_form = None
        retornos_eventos_ocorrencias_lista = None
        if retornos_eventos_id:
            retornos_eventos = get_object_or_404(RetornosEventos.objects.using( db_slug ), excluido = False, id = retornos_eventos_id)

            retornos_eventos_ocorrencias_form = form_retornos_eventos_ocorrencias(initial={ 'retornos_eventos': retornos_eventos }, slug=db_slug)
            retornos_eventos_ocorrencias_form.fields['retornos_eventos'].widget.attrs['readonly'] = True
            retornos_eventos_ocorrencias_lista = RetornosEventosOcorrencias.objects.using( db_slug ).filter(excluido = False, retornos_eventos_id=retornos_eventos.id).all()
        else:
            retornos_eventos = None
        #retornos_eventos_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'retornos_eventos' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'retornos_eventos_salvar'
        context = {
            'retornos_eventos': retornos_eventos,
            'retornos_eventos_form': retornos_eventos_form,
            'mensagem': mensagem,
            'retornos_eventos_id': int(retornos_eventos_id),
            'usuario': usuario,

            'hash': hash,

            'retornos_eventos_ocorrencias_form': retornos_eventos_ocorrencias_form,
            'retornos_eventos_ocorrencias_lista': retornos_eventos_ocorrencias_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #retornos_eventos_salvar_custom_variaveis_context#
        }
        return render(request, 'retornos_eventos_salvar.html', context)
    else:
        context = {
            'usuario': usuario,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #retornos_eventos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='retornos_eventos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_tmpparc': 0,
            'show_dsctpjorn': 0,
            'show_tpjornada': 0,
            'show_qtdhrssem': 0,
            'show_horarios_contratuais': 0,
            'show_local_cnae': 0,
            'show_local_nrinsc': 0,
            'show_local_tpinsc': 0,
            'show_local_trab': 0,
            'show_clauassec': 0,
            'show_dtterm': 0,
            'show_tpcontr': 0,
            'show_duracao': 0,
            'show_dscsalvar': 0,
            'show_undsalfixo': 0,
            'show_vrsalfx': 0,
            'show_remuneracao': 0,
            'show_codcateg': 0,
            'show_categoria': 0,
            'show_codcbo': 0,
            'show_dscfuncao': 0,
            'show_codfuncao': 0,
            'show_funcao': 0,
            'show_codcbo': 0,
            'show_nmcargo': 0,
            'show_codcargo': 0,
            'show_cargo': 0,
            'show_dtexercicio': 0,
            'show_dtposse': 0,
            'show_estatutario': 0,
            'show_cnpjsindcategprof': 0,
            'show_dtbase': 0,
            'show_tpregjor': 0,
            'show_dtadm': 0,
            'show_celetista': 0,
            'show_matricula': 0,
            'show_vinculo': 0,
            'show_infocota': 0,
            'show_deficiencia': 0,
            'show_nmtrab': 1,
            'show_nistrab': 0,
            'show_cpftrab': 1,
            'show_trabalhador': 0,
            'show_nrinsc': 1,
            'show_tpinsc': 1,
            'show_empregador': 0,
            'show_recibo_hash': 0,
            'show_recibo_numero': 0,
            'show_recibo': 0,
            'show_processamento_data_hora': 0,
            'show_processamento_versao_app_processamento': 0,
            'show_processamento_descricao_resposta': 0,
            'show_processamento_codigo_resposta': 1,
            'show_processamento': 0,
            'show_recepcao_protocolo_envio_lote': 0,
            'show_recepcao_versao_app': 0,
            'show_recepcao_data_hora': 0,
            'show_recepcao_tp_amb': 0,
            'show_processamento': 0,
            'show_identidade': 1,
            'show_transmissor_lote_esocial': 1, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'tmpparc': 'tmpparc',
                'dsctpjorn__icontains': 'dsctpjorn__icontains',
                'tpjornada': 'tpjornada',
                'qtdhrssem': 'qtdhrssem',
                'horarios_contratuais': 'horarios_contratuais',
                'local_cnae': 'local_cnae',
                'local_nrinsc__icontains': 'local_nrinsc__icontains',
                'local_tpinsc': 'local_tpinsc',
                'local_trab': 'local_trab',
                'clauassec__icontains': 'clauassec__icontains',
                'dtterm__range': 'dtterm__range',
                'tpcontr': 'tpcontr',
                'duracao': 'duracao',
                'dscsalvar__icontains': 'dscsalvar__icontains',
                'undsalfixo': 'undsalfixo',
                'vrsalfx': 'vrsalfx',
                'remuneracao': 'remuneracao',
                'codcateg': 'codcateg',
                'categoria': 'categoria',
                'codcbo__icontains': 'codcbo__icontains',
                'dscfuncao__icontains': 'dscfuncao__icontains',
                'codfuncao__icontains': 'codfuncao__icontains',
                'funcao': 'funcao',
                'codcbo__icontains': 'codcbo__icontains',
                'nmcargo__icontains': 'nmcargo__icontains',
                'codcargo__icontains': 'codcargo__icontains',
                'cargo': 'cargo',
                'dtexercicio__range': 'dtexercicio__range',
                'dtposse__range': 'dtposse__range',
                'estatutario': 'estatutario',
                'cnpjsindcategprof__icontains': 'cnpjsindcategprof__icontains',
                'dtbase': 'dtbase',
                'tpregjor': 'tpregjor',
                'dtadm__range': 'dtadm__range',
                'celetista': 'celetista',
                'matricula__icontains': 'matricula__icontains',
                'vinculo': 'vinculo',
                'infocota__icontains': 'infocota__icontains',
                'deficiencia': 'deficiencia',
                'nmtrab__icontains': 'nmtrab__icontains',
                'nistrab__icontains': 'nistrab__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'trabalhador': 'trabalhador',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'empregador': 'empregador',
                'recibo_hash__icontains': 'recibo_hash__icontains',
                'recibo_numero__icontains': 'recibo_numero__icontains',
                'recibo': 'recibo',
                'processamento_data_hora__range': 'processamento_data_hora__range',
                'processamento_versao_app_processamento__icontains': 'processamento_versao_app_processamento__icontains',
                'processamento_descricao_resposta__icontains': 'processamento_descricao_resposta__icontains',
                'processamento_codigo_resposta': 'processamento_codigo_resposta',
                'processamento': 'processamento',
                'recepcao_protocolo_envio_lote__icontains': 'recepcao_protocolo_envio_lote__icontains',
                'recepcao_versao_app__icontains': 'recepcao_versao_app__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'recepcao_tp_amb': 'recepcao_tp_amb',
                'processamento': 'processamento',
                'identidade__icontains': 'identidade__icontains',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'tmpparc': 'tmpparc',
                'dsctpjorn__icontains': 'dsctpjorn__icontains',
                'tpjornada': 'tpjornada',
                'qtdhrssem': 'qtdhrssem',
                'horarios_contratuais': 'horarios_contratuais',
                'local_cnae': 'local_cnae',
                'local_nrinsc__icontains': 'local_nrinsc__icontains',
                'local_tpinsc': 'local_tpinsc',
                'local_trab': 'local_trab',
                'clauassec__icontains': 'clauassec__icontains',
                'dtterm__range': 'dtterm__range',
                'tpcontr': 'tpcontr',
                'duracao': 'duracao',
                'dscsalvar__icontains': 'dscsalvar__icontains',
                'undsalfixo': 'undsalfixo',
                'vrsalfx': 'vrsalfx',
                'remuneracao': 'remuneracao',
                'codcateg': 'codcateg',
                'categoria': 'categoria',
                'codcbo__icontains': 'codcbo__icontains',
                'dscfuncao__icontains': 'dscfuncao__icontains',
                'codfuncao__icontains': 'codfuncao__icontains',
                'funcao': 'funcao',
                'codcbo__icontains': 'codcbo__icontains',
                'nmcargo__icontains': 'nmcargo__icontains',
                'codcargo__icontains': 'codcargo__icontains',
                'cargo': 'cargo',
                'dtexercicio__range': 'dtexercicio__range',
                'dtposse__range': 'dtposse__range',
                'estatutario': 'estatutario',
                'cnpjsindcategprof__icontains': 'cnpjsindcategprof__icontains',
                'dtbase': 'dtbase',
                'tpregjor': 'tpregjor',
                'dtadm__range': 'dtadm__range',
                'celetista': 'celetista',
                'matricula__icontains': 'matricula__icontains',
                'vinculo': 'vinculo',
                'infocota__icontains': 'infocota__icontains',
                'deficiencia': 'deficiencia',
                'nmtrab__icontains': 'nmtrab__icontains',
                'nistrab__icontains': 'nistrab__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'trabalhador': 'trabalhador',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'empregador': 'empregador',
                'recibo_hash__icontains': 'recibo_hash__icontains',
                'recibo_numero__icontains': 'recibo_numero__icontains',
                'recibo': 'recibo',
                'processamento_data_hora__range': 'processamento_data_hora__range',
                'processamento_versao_app_processamento__icontains': 'processamento_versao_app_processamento__icontains',
                'processamento_descricao_resposta__icontains': 'processamento_descricao_resposta__icontains',
                'processamento_codigo_resposta': 'processamento_codigo_resposta',
                'processamento': 'processamento',
                'recepcao_protocolo_envio_lote__icontains': 'recepcao_protocolo_envio_lote__icontains',
                'recepcao_versao_app__icontains': 'recepcao_versao_app__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'recepcao_tp_amb': 'recepcao_tp_amb',
                'processamento': 'processamento',
                'identidade__icontains': 'identidade__icontains',
                'transmissor_lote_esocial': 'transmissor_lote_esocial',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        retornos_eventos_lista = RetornosEventos.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(retornos_eventos_lista) > 100:
            filtrar = True
            retornos_eventos_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(excluido = False).all()
        #retornos_eventos_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'retornos_eventos'
        context = {
            'retornos_eventos_lista': retornos_eventos_lista,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,

            'transmissor_lote_esocial_lista': transmissor_lote_esocial_lista,
        }
        return render(request, 'retornos_eventos_listar.html', context)
    else:
        context = {
            'usuario': usuario,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)
