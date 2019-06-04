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
from emensageriapro.s2200.forms import *
from emensageriapro.s2200.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2200.models import s2200ideEstabVinc
from emensageriapro.s2200.forms import form_s2200_ideestabvinc
from emensageriapro.s2200.models import s2200ideTrabSubstituido
from emensageriapro.s2200.forms import form_s2200_idetrabsubstituido



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    
    if pk:
    
        s2200_trabtemporario = get_object_or_404(s2200trabTemporario, id=pk)
        dados_evento = s2200_trabtemporario.evento()

    if request.user.has_perm('s2200.can_see_s2200trabTemporario'):
        
        if pk:
        
            s2200_trabtemporario_form = form_s2200_trabtemporario(
                request.POST or None, 
                instance=s2200_trabtemporario)
                                         
        else:
        
            s2200_trabtemporario_form = form_s2200_trabtemporario(request.POST or None)
                                         
        if request.method == 'POST':
        
            if s2200_trabtemporario_form.is_valid():
            
                obj = s2200_trabtemporario_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    gravar_auditoria(
                        '{}',
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        's2200_trabtemporario', 
                        obj.id, 
                        request.user.id, 1)
                                 
                else:
                
                    gravar_auditoria(
                        json.dumps(
                            model_to_dict(s2200_trabtemporario), 
                            indent=4, 
                            sort_keys=True, 
                            default=str),
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        's2200_trabtemporario', 
                        pk, 
                        request.user.id, 2)
                                     
                if request.session['return_page'] not in (
                    's2200_trabtemporario_apagar', 
                    's2200_trabtemporario_salvar', 
                    's2200_trabtemporario'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'], 
                        tab=request.session['return_tab'])
                    
                if pk != obj.id:
                
                    return redirect(
                        's2200_trabtemporario_salvar', 
                        pk=obj.id, 
                        tab='master')
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        s2200_trabtemporario_form = disabled_form_fields(
            s2200_trabtemporario_form, 
            request.user.has_perm('s2200.change_s2200trabTemporario'))
        
        if pk:
        
            if dados_evento['status'] != 0:
            
                s2200_trabtemporario_form = disabled_form_fields(s2200_trabtemporario_form, 0)
                
        #s2200_trabtemporario_campos_multiple_passo3
        
        if output:
        
            s2200_trabtemporario_form = disabled_form_for_print(s2200_trabtemporario_form)
            
        
        s2200_ideestabvinc_lista = None 
        s2200_ideestabvinc_form = None 
        s2200_idetrabsubstituido_lista = None 
        s2200_idetrabsubstituido_form = None 
        
        if pk:
        
            s2200_trabtemporario = get_object_or_404(s2200trabTemporario, id=pk)
            
            s2200_ideestabvinc_form = form_s2200_ideestabvinc(
                initial={ 's2200_trabtemporario': s2200_trabtemporario })
            s2200_ideestabvinc_form.fields['s2200_trabtemporario'].widget.attrs['readonly'] = True
            s2200_ideestabvinc_lista = s2200ideEstabVinc.objects.\
                filter(s2200_trabtemporario_id=s2200_trabtemporario.id).all()
                
            s2200_idetrabsubstituido_form = form_s2200_idetrabsubstituido(
                initial={ 's2200_trabtemporario': s2200_trabtemporario })
            s2200_idetrabsubstituido_form.fields['s2200_trabtemporario'].widget.attrs['readonly'] = True
            s2200_idetrabsubstituido_lista = s2200ideTrabSubstituido.objects.\
                filter(s2200_trabtemporario_id=s2200_trabtemporario.id).all()
                
                
        else:
        
            s2200_trabtemporario = None
            
        #s2200_trabtemporario_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if tab or 's2200_trabtemporario' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 's2200_trabtemporario_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2200_trabtemporario').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'ocorrencias': dados_evento['ocorrencias'], 
            'dados_evento': dados_evento,
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            's2200_trabtemporario': s2200_trabtemporario, 
            's2200_trabtemporario_form': s2200_trabtemporario_form, 
            'modulos': ['s2200', ],
            'paginas': ['s2200_trabtemporario', ],
            's2200_ideestabvinc_form': s2200_ideestabvinc_form,
            's2200_ideestabvinc_lista': s2200_ideestabvinc_lista,
            's2200_idetrabsubstituido_form': s2200_idetrabsubstituido_form,
            's2200_idetrabsubstituido_lista': s2200_idetrabsubstituido_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s2200_trabtemporario_salvar_custom_variaveis_context#
        }
        
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='s2200_trabtemporario_salvar.html',
                filename="s2200_trabtemporario.pdf",
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
                             "no-stop-slow-scripts": True}, )
            
            return response
            
        elif output == 'xls':
        
            from django.shortcuts import render_to_response
            
            response = render_to_response('s2200_trabtemporario_salvar.html', context)
            filename = "s2200_trabtemporario.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 's2200_trabtemporario_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s2200', ],
            'paginas': ['s2200_trabtemporario', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)