#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.s2200.forms import *
from emensageriapro.s2200.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2200_dependente_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_dependente')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2200_dependente_id:
        s2200_dependente = get_object_or_404(s2200dependente.objects.using( db_slug ), excluido = False, id = s2200_dependente_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if s2200_dependente_id:
        dados_evento = s2200_dependente.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s2200_dependente_apagar'] = 0
            dict_permissoes['s2200_dependente_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2200_dependente_id:
            s2200_dependente_form = form_s2200_dependente(request.POST or None, instance = s2200_dependente, slug = db_slug)
        else:
            s2200_dependente_form = form_s2200_dependente(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if s2200_dependente_form.is_valid():
                dados = s2200_dependente_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s2200_dependente_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s2200_dependente_campos_multiple_passo1
                        s2200dependente.objects.using(db_slug).filter(id=s2200_dependente_id).update(**dados)
                        obj = s2200dependente.objects.using(db_slug).get(id=s2200_dependente_id)
                        #s2200_dependente_editar_custom
                        #s2200_dependente_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s2200_dependente), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's2200_dependente', s2200_dependente_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s2200_dependente_cadastrar_campos_multiple_passo1
                    obj = s2200dependente(**dados)
                    obj.save(using = db_slug)
                    #s2200_dependente_cadastrar_custom
                    #s2200_dependente_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2200_dependente', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('s2200_dependente_apagar', 's2200_dependente_salvar', 's2200_dependente'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if s2200_dependente_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('s2200_dependente_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s2200_dependente_form = disabled_form_fields(s2200_dependente_form, permissao.permite_editar)
        if s2200_dependente_id:
            if dados_evento['status'] != 0:
                s2200_dependente_form = disabled_form_fields(s2200_dependente_form, 0)
        #s2200_dependente_campos_multiple_passo3

        for field in s2200_dependente_form.fields.keys():
            s2200_dependente_form.fields[field].widget.attrs['ng-model'] = 's2200_dependente_'+field
        if int(dict_hash['print']):
            s2200_dependente_form = disabled_form_for_print(s2200_dependente_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if s2200_dependente_id:
            s2200_dependente = get_object_or_404(s2200dependente.objects.using( db_slug ), excluido = False, id = s2200_dependente_id)
            pass
        else:
            s2200_dependente = None
        #s2200_dependente_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's2200_dependente' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2200_dependente_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2200_dependente_id, tabela='s2200_dependente').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's2200_dependente': s2200_dependente,
            's2200_dependente_form': s2200_dependente_form,
            'mensagem': mensagem,
            's2200_dependente_id': int(s2200_dependente_id),
            'usuario': usuario,
       
            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2200_dependente_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's2200_dependente_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2200_dependente_salvar.html',
                filename="s2200_dependente.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('s2200_dependente_salvar.html', context)
            filename = "s2200_dependente.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

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

@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2200_dependente_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_dependente')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2200_dependente = get_object_or_404(s2200dependente.objects.using( db_slug ), excluido = False, id = s2200_dependente_id)
    dados_evento = {}
    if s2200_dependente_id:
        dados_evento = s2200_dependente.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s2200_dependente_apagar'] = 0
            dict_permissoes['s2200_dependente_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2200_dependente), indent=4, sort_keys=True, default=str)
            s2200dependente.objects.using( db_slug ).filter(id = s2200_dependente_id).delete()
            #s2200_dependente_apagar_custom
            #s2200_dependente_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2200_dependente', s2200_dependente_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
   
        if request.session['retorno_pagina']== 's2200_dependente_salvar':
            return redirect('s2200_dependente', hash=request.session['retorno_hash'])
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
    return render(request, 's2200_dependente_apagar.html', context)

def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s2200_dependente_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_dependente')
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
            'show_depfinsprev': 0,
            'show_inctrab': 1,
            'show_depsf': 1,
            'show_depirrf': 1,
            'show_sexodep': 0,
            'show_cpfdep': 0,
            'show_dtnascto': 1,
            'show_nmdep': 1,
            'show_tpdep': 1,
            'show_s2200_evtadmissao': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'depfinsprev__icontains': 'depfinsprev__icontains',
                'inctrab__icontains': 'inctrab__icontains',
                'depsf__icontains': 'depsf__icontains',
                'depirrf__icontains': 'depirrf__icontains',
                'sexodep__icontains': 'sexodep__icontains',
                'cpfdep__icontains': 'cpfdep__icontains',
                'dtnascto__range': 'dtnascto__range',
                'nmdep__icontains': 'nmdep__icontains',
                'tpdep__icontains': 'tpdep__icontains',
                's2200_evtadmissao': 's2200_evtadmissao',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'depfinsprev__icontains': 'depfinsprev__icontains',
                'inctrab__icontains': 'inctrab__icontains',
                'depsf__icontains': 'depsf__icontains',
                'depirrf__icontains': 'depirrf__icontains',
                'sexodep__icontains': 'sexodep__icontains',
                'cpfdep__icontains': 'cpfdep__icontains',
                'dtnascto__range': 'dtnascto__range',
                'nmdep__icontains': 'nmdep__icontains',
                'tpdep__icontains': 'tpdep__icontains',
                's2200_evtadmissao': 's2200_evtadmissao',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2200_dependente_lista = s2200dependente.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2200_dependente_lista) > 100:
            filtrar = True
            s2200_dependente_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        s2200_evtadmissao_lista = s2200evtAdmissao.objects.using( db_slug ).filter(excluido = False).all()
        #s2200_dependente_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2200_dependente'
        context = {
            's2200_dependente_lista': s2200_dependente_lista,
       
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
  
            's2200_evtadmissao_lista': s2200_evtadmissao_lista,
        }
        if for_print in (0,1):
            return render(request, 's2200_dependente_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2200_dependente_listar.html',
                filename="s2200_dependente.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('s2200_dependente_listar.html', context)
            filename = "s2200_dependente.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s2200_dependente_csv.html', context)
            filename = "s2200_dependente.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
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

