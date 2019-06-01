#coding: utf-8
# © 2018 Marcelo Medeiros de Vasconcellos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__credits__ = ["Marcelo Medeiros de Vasconcellos"]
__version__ = "1.0.0"
__maintainer__ = "Marcelo Medeiros de Vasconcellos"
__email__ = "marcelomdevasconcellos@gmail.com"


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.s2240.models import *
from emensageriapro.s2240.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from datetime import datetime
import base64
import os


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



@login_required
def abrir_evento_para_edicao(request, hash):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_esocial import gravar_nome_arquivo

    dict_hash = get_hash_url(hash)
    s2240_evtexprisco_id = int(dict_hash['id'])
    
    if request.user.has_perm('esocial.can_open_event_s2240evtExpRisco'):

        if s2240_evtexprisco_id:
            s2240_evtexprisco = get_object_or_404(s2240evtExpRisco, excluido=False, id=s2240_evtexprisco_id)
    
            status_list = [
                STATUS_EVENTO_CADASTRADO,
                STATUS_EVENTO_IMPORTADO,
                STATUS_EVENTO_DUPLICADO,
                STATUS_EVENTO_GERADO,
                STATUS_EVENTO_GERADO_ERRO,
                STATUS_EVENTO_ASSINADO,
                STATUS_EVENTO_ASSINADO_ERRO,
                STATUS_EVENTO_VALIDADO,
                STATUS_EVENTO_VALIDADO_ERRO,
                STATUS_EVENTO_AGUARD_PRECEDENCIA,
                STATUS_EVENTO_AGUARD_ENVIO,
                STATUS_EVENTO_ENVIADO_ERRO
            ]
    
            if s2240_evtexprisco.status in status_list:
                s2240evtExpRisco.objects.filter(id=s2240_evtexprisco_id).update(status=STATUS_EVENTO_CADASTRADO,
                                                                              arquivo_original=0)
                arquivo = 'arquivos/Eventos/s2240_evtexprisco/%s.xml' % (s2240_evtexprisco.identidade)
    
                if os.path.exists(BASE_DIR + '/' + arquivo):
    
                    data_hora_atual = str(datetime.now()).replace(':','_').replace(' ','_').replace('.','_')
                    dad = (BASE_DIR, s2240_evtexprisco.identidade, BASE_DIR, s2240_evtexprisco.identidade, data_hora_atual)
                    os.system('mv %s/arquivos/Eventos/s2240_evtexprisco/%s.xml %s/arquivos/Eventos/s2240_evtexprisco/%s_backup_%s.xml' % dad)
                    gravar_nome_arquivo('/arquivos/Eventos/s2240_evtexprisco/%s_backup_%s.xml' % (s2240_evtexprisco.identidade, data_hora_atual),
                        1)
    
                messages.success(request, 'Evento aberto para edição!')
                usuario_id = request.user.id
                gravar_auditoria(u'{}', u'{"funcao": "Evento aberto para edição"}',
                    's2240_evtexprisco', s2240_evtexprisco_id, usuario_id, 1)
    
                url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s2240_evtexprisco_id )
                return redirect('s2240_evtexprisco_salvar', hash=url_hash)
                
            else:
            
                messages.error(request, u'''
                    Não foi possível abrir o evento para edição! Somente é possível
                    abrir eventos com os seguintes status: "Cadastrado", "Importado", "Validado",
                    "Duplicado", "Erro na validação", "XML Assinado" ou "XML Gerado"
                     ou com o status "Enviado com sucesso" e os seguintes códigos de resposta do servidor:
                     "401 - Lote Incorreto - Erro preenchimento" ou "402 - Lote Incorreto - schema Inválido"!''')
                return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    
        messages.error(request, 'Erro ao abrir evento para edição!')
        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
        
    else:
    
        messages.error(request, u'''Você não possui permissão para abrir evento para edição. 
                                    Entre em contato com o administrador do sistema!''')
        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])