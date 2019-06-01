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
from emensageriapro.s2205.forms import *
from emensageriapro.s2205.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2205.models import s2205CTPS
from emensageriapro.s2205.forms import form_s2205_ctps
from emensageriapro.s2205.models import s2205RIC
from emensageriapro.s2205.forms import form_s2205_ric
from emensageriapro.s2205.models import s2205RG
from emensageriapro.s2205.forms import form_s2205_rg
from emensageriapro.s2205.models import s2205RNE
from emensageriapro.s2205.forms import form_s2205_rne
from emensageriapro.s2205.models import s2205OC
from emensageriapro.s2205.forms import form_s2205_oc
from emensageriapro.s2205.models import s2205CNH
from emensageriapro.s2205.forms import form_s2205_cnh



@login_required
def salvar(request, hash):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    try: 
    
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        s2205_documentos_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except: 
    
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    
    if s2205_documentos_id:
    
        s2205_documentos = get_object_or_404(s2205documentos, id=s2205_documentos_id)
        dados_evento = s2205_documentos.evento()

    if request.user.has_perm('s2205.can_view_s2205documentos'):
        
        if s2205_documentos_id:
        
            s2205_documentos_form = form_s2205_documentos(request.POST or None, 
                                                          instance=s2205_documentos,  
                                                          initial={'excluido': False})
                                         
        else:
        
            s2205_documentos_form = form_s2205_documentos(request.POST or None, 
                                         initial={'excluido': False})
                                         
        if request.method == 'POST':
        
            if s2205_documentos_form.is_valid():
            
                dados = s2205_documentos_form.cleaned_data
                obj = s2205_documentos_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s2205_documentos_id:
                
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's2205_documentos', obj.id, usuario_id, 1)
                                 
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s2205_documentos), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's2205_documentos', s2205_documentos_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('s2205_documentos_apagar', 's2205_documentos_salvar', 's2205_documentos'):
                    
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if s2205_documentos_id != obj.id:
                
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2205_documentos_salvar', hash=url_hash)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        s2205_documentos_form = disabled_form_fields(s2205_documentos_form, request.user.has_perm('s2205.change_s2205documentos'))
        
        if s2205_documentos_id:
        
            if dados_evento['status'] != 0:
            
                s2205_documentos_form = disabled_form_fields(s2205_documentos_form, 0)
                
        #s2205_documentos_campos_multiple_passo3
        
        if int(dict_hash['print']):
        
            s2205_documentos_form = disabled_form_for_print(s2205_documentos_form)
            
        
        s2205_ctps_lista = None 
        s2205_ctps_form = None 
        s2205_ric_lista = None 
        s2205_ric_form = None 
        s2205_rg_lista = None 
        s2205_rg_form = None 
        s2205_rne_lista = None 
        s2205_rne_form = None 
        s2205_oc_lista = None 
        s2205_oc_form = None 
        s2205_cnh_lista = None 
        s2205_cnh_form = None 
        
        if s2205_documentos_id:
        
            s2205_documentos = get_object_or_404(s2205documentos, id=s2205_documentos_id)
            
            s2205_ctps_form = form_s2205_ctps(
                initial={ 's2205_documentos': s2205_documentos })
            s2205_ctps_form.fields['s2205_documentos'].widget.attrs['readonly'] = True
            s2205_ctps_lista = s2205CTPS.objects.\
                filter(s2205_documentos_id=s2205_documentos.id).all()
            s2205_ric_form = form_s2205_ric(
                initial={ 's2205_documentos': s2205_documentos })
            s2205_ric_form.fields['s2205_documentos'].widget.attrs['readonly'] = True
            s2205_ric_lista = s2205RIC.objects.\
                filter(s2205_documentos_id=s2205_documentos.id).all()
            s2205_rg_form = form_s2205_rg(
                initial={ 's2205_documentos': s2205_documentos })
            s2205_rg_form.fields['s2205_documentos'].widget.attrs['readonly'] = True
            s2205_rg_lista = s2205RG.objects.\
                filter(s2205_documentos_id=s2205_documentos.id).all()
            s2205_rne_form = form_s2205_rne(
                initial={ 's2205_documentos': s2205_documentos })
            s2205_rne_form.fields['s2205_documentos'].widget.attrs['readonly'] = True
            s2205_rne_lista = s2205RNE.objects.\
                filter(s2205_documentos_id=s2205_documentos.id).all()
            s2205_oc_form = form_s2205_oc(
                initial={ 's2205_documentos': s2205_documentos })
            s2205_oc_form.fields['s2205_documentos'].widget.attrs['readonly'] = True
            s2205_oc_lista = s2205OC.objects.\
                filter(s2205_documentos_id=s2205_documentos.id).all()
            s2205_cnh_form = form_s2205_cnh(
                initial={ 's2205_documentos': s2205_documentos })
            s2205_cnh_form.fields['s2205_documentos'].widget.attrs['readonly'] = True
            s2205_cnh_lista = s2205CNH.objects.\
                filter(s2205_documentos_id=s2205_documentos.id).all()
                
        else:
        
            s2205_documentos = None
            
        #s2205_documentos_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if dict_hash['tab'] or 's2205_documentos' in request.session['retorno_pagina']:
        
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2205_documentos_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=s2205_documentos_id, tabela='s2205_documentos').all()
        
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'dados_evento': dados_evento,
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            's2205_documentos': s2205_documentos, 
            's2205_documentos_form': s2205_documentos_form, 
            's2205_documentos_id': int(s2205_documentos_id),
            'usuario': usuario, 
            'modulos': ['s2205', ],
            'paginas': ['s2205_documentos', ],
            'hash': hash, 
            
            's2205_ctps_form': s2205_ctps_form,
            's2205_ctps_lista': s2205_ctps_lista,
            's2205_ric_form': s2205_ric_form,
            's2205_ric_lista': s2205_ric_lista,
            's2205_rg_form': s2205_rg_form,
            's2205_rg_lista': s2205_rg_lista,
            's2205_rne_form': s2205_rne_form,
            's2205_rne_lista': s2205_rne_lista,
            's2205_oc_form': s2205_oc_form,
            's2205_oc_lista': s2205_oc_lista,
            's2205_cnh_form': s2205_cnh_form,
            's2205_cnh_lista': s2205_cnh_lista,
            'data': datetime.datetime.now(),
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2205_documentos_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 's2205_documentos_salvar.html', context)
            
        elif for_print == 2:
        
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2205_documentos_salvar.html',
                filename="s2205_documentos.pdf",
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
            response = render_to_response('s2205_documentos_salvar.html', context)
            filename = "s2205_documentos.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['s2205', ],
            'paginas': ['s2205_documentos', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)
