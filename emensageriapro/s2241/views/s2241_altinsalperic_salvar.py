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
from emensageriapro.s2241.forms import *
from emensageriapro.s2241.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s2241.models import s2241altInsalPericinfoamb
from emensageriapro.s2241.forms import form_s2241_altinsalperic_infoamb



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    
    if pk:
    
        s2241_altinsalperic = get_object_or_404(s2241altInsalPeric, id=pk)
        dados_evento = s2241_altinsalperic.evento()

    if request.user.has_perm('s2241.can_see_s2241altInsalPeric'):
        
        if pk:
        
            s2241_altinsalperic_form = form_s2241_altinsalperic(
                request.POST or None, 
                instance=s2241_altinsalperic)
                                         
        else:
        
            s2241_altinsalperic_form = form_s2241_altinsalperic(request.POST or None)
                                         
        if request.method == 'POST':
        
            if s2241_altinsalperic_form.is_valid():
            
                obj = s2241_altinsalperic_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    gravar_auditoria(
                        '{}',
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        's2241_altinsalperic', 
                        obj.id, 
                        request.user.id, 1)
                                 
                else:
                
                    gravar_auditoria(
                        json.dumps(
                            model_to_dict(s2241_altinsalperic), 
                            indent=4, 
                            sort_keys=True, 
                            default=str),
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        's2241_altinsalperic', 
                        pk, 
                        request.user.id, 2)
                                     
                if request.session['return_page'] not in (
                    's2241_altinsalperic_apagar', 
                    's2241_altinsalperic_salvar', 
                    's2241_altinsalperic'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'], 
                        tab=request.session['return_tab'])
                    
                if pk != obj.id:
                
                    return redirect(
                        's2241_altinsalperic_salvar', 
                        pk=obj.id, 
                        tab='master')
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        s2241_altinsalperic_form = disabled_form_fields(
            s2241_altinsalperic_form, 
            request.user.has_perm('s2241.change_s2241altInsalPeric'))
        
        if pk:
        
            if dados_evento['status'] != 0:
            
                s2241_altinsalperic_form = disabled_form_fields(s2241_altinsalperic_form, 0)
                
        #s2241_altinsalperic_campos_multiple_passo3
        
        if output:
        
            s2241_altinsalperic_form = disabled_form_for_print(s2241_altinsalperic_form)
            
        
        s2241_altinsalperic_infoamb_lista = None 
        s2241_altinsalperic_infoamb_form = None 
        
        if pk:
        
            s2241_altinsalperic = get_object_or_404(s2241altInsalPeric, id=pk)
            
            s2241_altinsalperic_infoamb_form = form_s2241_altinsalperic_infoamb(
                initial={ 's2241_altinsalperic': s2241_altinsalperic })
            s2241_altinsalperic_infoamb_form.fields['s2241_altinsalperic'].widget.attrs['readonly'] = True
            s2241_altinsalperic_infoamb_lista = s2241altInsalPericinfoamb.objects.\
                filter(s2241_altinsalperic_id=s2241_altinsalperic.id).all()
                
                
        else:
        
            s2241_altinsalperic = None
            
        #s2241_altinsalperic_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        
        if tab or 's2241_altinsalperic' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 's2241_altinsalperic_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2241_altinsalperic').all()
        
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
            's2241_altinsalperic': s2241_altinsalperic, 
            's2241_altinsalperic_form': s2241_altinsalperic_form, 
            'modulos': ['s2241', ],
            'paginas': ['s2241_altinsalperic', ],
            's2241_altinsalperic_infoamb_form': s2241_altinsalperic_infoamb_form,
            's2241_altinsalperic_infoamb_lista': s2241_altinsalperic_infoamb_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s2241_altinsalperic_salvar_custom_variaveis_context#
        }
        
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='s2241_altinsalperic_salvar.html',
                filename="s2241_altinsalperic.pdf",
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
            
            response = render_to_response('s2241_altinsalperic_salvar.html', context)
            filename = "s2241_altinsalperic.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 's2241_altinsalperic_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s2241', ],
            'paginas': ['s2241_altinsalperic', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)