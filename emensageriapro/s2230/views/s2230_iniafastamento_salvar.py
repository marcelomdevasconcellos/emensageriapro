#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"


"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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
import json
import base64
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.s2230.forms import *
from emensageriapro.s2230.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2230.models import s2230infoAtestado
from emensageriapro.s2230.forms import form_s2230_infoatestado
from emensageriapro.s2230.models import s2230infoCessao
from emensageriapro.s2230.forms import form_s2230_infocessao
from emensageriapro.s2230.models import s2230infoMandSind
from emensageriapro.s2230.forms import form_s2230_infomandsind



@login_required
def salvar(request, hash):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    try: 
    
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        s2230_iniafastamento_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except: 
    
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    
    if s2230_iniafastamento_id:
    
        s2230_iniafastamento = get_object_or_404(s2230iniAfastamento, id=s2230_iniafastamento_id)
        dados_evento = s2230_iniafastamento.evento()

    if request.user.has_perm('s2230.can_view_s2230iniAfastamento'):
        
        if s2230_iniafastamento_id:
        
            s2230_iniafastamento_form = form_s2230_iniafastamento(request.POST or None, 
                                                          instance=s2230_iniafastamento,  
                                                          initial={'excluido': False})
                                         
        else:
        
            s2230_iniafastamento_form = form_s2230_iniafastamento(request.POST or None, 
                                         initial={'excluido': False})
                                         
        if request.method == 'POST':
        
            if s2230_iniafastamento_form.is_valid():
            
                dados = s2230_iniafastamento_form.cleaned_data
                obj = s2230_iniafastamento_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s2230_iniafastamento_id:
                
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2230_iniafastamento', obj.id, usuario_id, 1)
                                 
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2230_iniafastamento), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2230_iniafastamento', s2230_iniafastamento_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('s2230_iniafastamento_apagar', 's2230_iniafastamento_salvar', 's2230_iniafastamento'):
                    
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if s2230_iniafastamento_id != obj.id:
                
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2230_iniafastamento_salvar', hash=url_hash)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        s2230_iniafastamento_form = disabled_form_fields(s2230_iniafastamento_form, request.user.has_perm('s2230.change_s2230iniAfastamento'))
        
        if s2230_iniafastamento_id:
        
            if dados_evento['status'] != 0:
            
                s2230_iniafastamento_form = disabled_form_fields(s2230_iniafastamento_form, 0)
                
        #s2230_iniafastamento_campos_multiple_passo3
        
        if int(dict_hash['print']):
        
            s2230_iniafastamento_form = disabled_form_for_print(s2230_iniafastamento_form)
            
        
        s2230_infoatestado_lista = None 
        s2230_infoatestado_form = None 
        s2230_infocessao_lista = None 
        s2230_infocessao_form = None 
        s2230_infomandsind_lista = None 
        s2230_infomandsind_form = None 
        
        if s2230_iniafastamento_id:
        
            s2230_iniafastamento = get_object_or_404(s2230iniAfastamento, id=s2230_iniafastamento_id)
            
            s2230_infoatestado_form = form_s2230_infoatestado(
                initial={ 's2230_iniafastamento': s2230_iniafastamento })
            s2230_infoatestado_form.fields['s2230_iniafastamento'].widget.attrs['readonly'] = True
            s2230_infoatestado_lista = s2230infoAtestado.objects.\
                filter(s2230_iniafastamento_id=s2230_iniafastamento.id).all()
            s2230_infocessao_form = form_s2230_infocessao(
                initial={ 's2230_iniafastamento': s2230_iniafastamento })
            s2230_infocessao_form.fields['s2230_iniafastamento'].widget.attrs['readonly'] = True
            s2230_infocessao_lista = s2230infoCessao.objects.\
                filter(s2230_iniafastamento_id=s2230_iniafastamento.id).all()
            s2230_infomandsind_form = form_s2230_infomandsind(
                initial={ 's2230_iniafastamento': s2230_iniafastamento })
            s2230_infomandsind_form.fields['s2230_iniafastamento'].widget.attrs['readonly'] = True
            s2230_infomandsind_lista = s2230infoMandSind.objects.\
                filter(s2230_iniafastamento_id=s2230_iniafastamento.id).all()
                
        else:
        
            s2230_iniafastamento = None
            
        #s2230_iniafastamento_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if dict_hash['tab'] or 's2230_iniafastamento' in request.session['retorno_pagina']:
        
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2230_iniafastamento_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=s2230_iniafastamento_id, tabela='s2230_iniafastamento').all()
        
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'dados_evento': dados_evento,
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            's2230_iniafastamento': s2230_iniafastamento, 
            's2230_iniafastamento_form': s2230_iniafastamento_form, 
            's2230_iniafastamento_id': int(s2230_iniafastamento_id),
            'usuario': usuario, 
            'modulos': ['s2230', ],
            'paginas': ['s2230_iniafastamento', ],
            'hash': hash, 
            
            's2230_infoatestado_form': s2230_infoatestado_form,
            's2230_infoatestado_lista': s2230_infoatestado_lista,
            's2230_infocessao_form': s2230_infocessao_form,
            's2230_infocessao_lista': s2230_infocessao_lista,
            's2230_infomandsind_form': s2230_infomandsind_form,
            's2230_infomandsind_lista': s2230_infomandsind_lista,
            'data': datetime.datetime.now(),
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2230_iniafastamento_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 's2230_iniafastamento_salvar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2230_iniafastamento_salvar.html',
                filename="s2230_iniafastamento.pdf",
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
            response = render_to_response('s2230_iniafastamento_salvar.html', context)
            filename = "s2230_iniafastamento.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['s2230', ],
            'paginas': ['s2230_iniafastamento', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)
