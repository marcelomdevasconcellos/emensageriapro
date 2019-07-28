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
from emensageriapro.s2210.forms import *
from emensageriapro.s2210.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def listar(request, output=None):

    if request.user.has_perm('s2210.can_see_s2210atestado'):

        filtrar = False

        dict_fields = {}
        show_fields = {
            'show_s2210_evtcat': 1,
            'show_codcnes': 0,
            'show_dtatendimento': 0,
            'show_hratendimento': 0,
            'show_indinternacao': 0,
            'show_durtrat': 0,
            'show_indafast': 1,
            'show_dsclesao': 0,
            'show_dsccomplesao': 0,
            'show_diagprovavel': 0,
            'show_codcid': 1,
            'show_observacao': 0,
            'show_emitente': 0,
            'show_nmemit': 0,
            'show_ideoc': 0,
            'show_nroc': 0,
            'show_ufoc': 0, }

        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                's2210_evtcat__icontains': 's2210_evtcat__icontains',
                'codcnes__icontains': 'codcnes__icontains',
                'dtatendimento__range': 'dtatendimento__range',
                'hratendimento__icontains': 'hratendimento__icontains',
                'indinternacao__icontains': 'indinternacao__icontains',
                'durtrat__icontains': 'durtrat__icontains',
                'indafast__icontains': 'indafast__icontains',
                'dsclesao__icontains': 'dsclesao__icontains',
                'dsccomplesao__icontains': 'dsccomplesao__icontains',
                'diagprovavel__icontains': 'diagprovavel__icontains',
                'codcid__icontains': 'codcid__icontains',
                'observacao__icontains': 'observacao__icontains',
                'emitente': 'emitente',
                'nmemit__icontains': 'nmemit__icontains',
                'ideoc__icontains': 'ideoc__icontains',
                'nroc__icontains': 'nroc__icontains',
                'ufoc__icontains': 'ufoc__icontains', }

            for a in dict_fields:

                dict_fields[a] = request.POST.get(a or None)

            for a in show_fields:

                show_fields[a] = request.POST.get(a or None)

            if request.method == 'POST':

                dict_fields = {
                    's2210_evtcat__icontains': 's2210_evtcat__icontains',
                    'codcnes__icontains': 'codcnes__icontains',
                    'dtatendimento__range': 'dtatendimento__range',
                    'hratendimento__icontains': 'hratendimento__icontains',
                    'indinternacao__icontains': 'indinternacao__icontains',
                    'durtrat__icontains': 'durtrat__icontains',
                    'indafast__icontains': 'indafast__icontains',
                    'dsclesao__icontains': 'dsclesao__icontains',
                    'dsccomplesao__icontains': 'dsccomplesao__icontains',
                    'diagprovavel__icontains': 'diagprovavel__icontains',
                    'codcid__icontains': 'codcid__icontains',
                    'observacao__icontains': 'observacao__icontains',
                    'emitente': 'emitente',
                    'nmemit__icontains': 'nmemit__icontains',
                    'ideoc__icontains': 'ideoc__icontains',
                    'nroc__icontains': 'nroc__icontains',
                    'ufoc__icontains': 'ufoc__icontains', }

                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        s2210_atestado_lista = s2210atestado.objects.filter(**dict_qs).filter().exclude(id=0).all()

        if not post and len(s2210_atestado_lista) > 100:

            filtrar = True
            s2210_atestado_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #s2210_atestado_listar_custom

        request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            's2210_atestado_lista': s2210_atestado_lista,
            'modulos': ['s2210', ],
            'paginas': ['s2210_atestado', ],
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'filtrar': filtrar,
            #[VARIAVEIS_FILTRO_RELATORIO]
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s2210_atestado_listar.html',
                filename="s2210_atestado.pdf",
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
            response = render_to_response('s2210_atestado_listar.html', context)
            filename = "s2210_atestado.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif output == 'csv':

            from django.shortcuts import render_to_response
            response = render_to_response('csv/s2210_atestado.csv', context)
            filename = "s2210_atestado.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:

            return render(request, 's2210_atestado_listar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'data': datetime.datetime.now(),
            'modulos': ['s2210', ],
            'paginas': ['s2210_atestado', ],
        }

        return render(request,
                      'permissao_negada.html',
                      context)