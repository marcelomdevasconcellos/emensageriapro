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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r3010.models import r3010boletim
from emensageriapro.r3010.forms import form_r3010_boletim
from emensageriapro.r3010.models import r3010infoProc
from emensageriapro.r3010.forms import form_r3010_infoproc


@login_required
def salvar(request, hash):

    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    
    try:
    
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r3010_evtespdesportivo_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
        
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    
    if r3010_evtespdesportivo_id:
    
        r3010_evtespdesportivo = get_object_or_404(r3010evtEspDesportivo, id=r3010_evtespdesportivo_id)

        if r3010_evtespdesportivo.status != STATUS_EVENTO_CADASTRADO:
        
            dict_permissoes = {}
            dict_permissoes['r3010_evtespdesportivo_apagar'] = 0
            dict_permissoes['r3010_evtespdesportivo_editar'] = 0
            
    if request.user.has_perm('efdreinf.can_view_r3010evtEspDesportivo'):
    
        if r3010_evtespdesportivo_id:
        
            r3010_evtespdesportivo_form = form_r3010_evtespdesportivo(request.POST or None, instance = r3010_evtespdesportivo, 
                                         initial={'excluido': False})
                                         
        else:
        
            r3010_evtespdesportivo_form = form_r3010_evtespdesportivo(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
                                                  
        if request.method == 'POST':
        
            if r3010_evtespdesportivo_form.is_valid():
            
                dados = r3010_evtespdesportivo_form.cleaned_data
                obj = r3010_evtespdesportivo_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not r3010_evtespdesportivo_id:
                
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r3010_evtespdesportivo', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r3010_evtespdesportivo), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r3010_evtespdesportivo', r3010_evtespdesportivo_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('r3010_evtespdesportivo_apagar', 'r3010_evtespdesportivo_salvar', 'r3010_evtespdesportivo'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    
                if r3010_evtespdesportivo_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r3010_evtespdesportivo_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
                
        r3010_evtespdesportivo_form = disabled_form_fields(r3010_evtespdesportivo_form, request.user.has_perm('efdreinf.change_r3010evtEspDesportivo'))
        
        if r3010_evtespdesportivo_id:
            if r3010_evtespdesportivo.status != 0:
                r3010_evtespdesportivo_form = disabled_form_fields(r3010_evtespdesportivo_form, False)
        #r3010_evtespdesportivo_campos_multiple_passo3

        for field in r3010_evtespdesportivo_form.fields.keys():
            r3010_evtespdesportivo_form.fields[field].widget.attrs['ng-model'] = 'r3010_evtespdesportivo_'+field
            
        if int(dict_hash['print']):
            r3010_evtespdesportivo_form = disabled_form_for_print(r3010_evtespdesportivo_form)

        
        r3010_boletim_lista = None 
        r3010_boletim_form = None 
        r3010_infoproc_lista = None 
        r3010_infoproc_form = None 
        
        if r3010_evtespdesportivo_id:
        
            r3010_evtespdesportivo = get_object_or_404(r3010evtEspDesportivo, id = r3010_evtespdesportivo_id)
            
            r3010_boletim_form = form_r3010_boletim(
                initial={ 'r3010_evtespdesportivo': r3010_evtespdesportivo })
            r3010_boletim_form.fields['r3010_evtespdesportivo'].widget.attrs['readonly'] = True
            r3010_boletim_lista = r3010boletim.objects.\
                filter(r3010_evtespdesportivo_id=r3010_evtespdesportivo.id).all()
            r3010_infoproc_form = form_r3010_infoproc(
                initial={ 'r3010_evtespdesportivo': r3010_evtespdesportivo })
            r3010_infoproc_form.fields['r3010_evtespdesportivo'].widget.attrs['readonly'] = True
            r3010_infoproc_lista = r3010infoProc.objects.\
                filter(r3010_evtespdesportivo_id=r3010_evtespdesportivo.id).all()
                
        else:
            r3010_evtespdesportivo = None
            
        #r3010_evtespdesportivo_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if 'r3010_evtespdesportivo'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 'r3010_evtespdesportivo' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r3010_evtespdesportivo_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=r3010_evtespdesportivo_id, tabela='r3010_evtespdesportivo').all()
        
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r3010_evtespdesportivo': r3010_evtespdesportivo, 
            'r3010_evtespdesportivo_form': r3010_evtespdesportivo_form, 
            'r3010_evtespdesportivo_id': int(r3010_evtespdesportivo_id),
            'usuario': usuario, 
            'hash': hash, 
            
            'r3010_boletim_form': r3010_boletim_form,
            'r3010_boletim_lista': r3010_boletim_lista,
            'r3010_infoproc_form': r3010_infoproc_form,
            'r3010_infoproc_lista': r3010_infoproc_lista,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r3010_evtespdesportivo', ],
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r3010_evtespdesportivo_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
        
            return render(request, 'r3010_evtespdesportivo_salvar.html', context)
            
        elif for_print == 2:
        
            response = PDFTemplateResponse(
                request=request,
                template='r3010_evtespdesportivo_salvar.html',
                filename="r3010_evtespdesportivo.pdf",
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
        
            response = render_to_response('r3010_evtespdesportivo_salvar.html', context)
            filename = "r3010_evtespdesportivo.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
    else:
    
        context = {
            'usuario': usuario, 
            'modulos': ['efdreinf', ],
            'paginas': ['r3010_evtespdesportivo', ],
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)
