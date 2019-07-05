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


import os
import base64
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.s1005.models import *
from emensageriapro.s1005.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from django.template.loader import get_template
from emensageriapro.functions import get_xmlns


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def gerar_xml_s1005_func(pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    s1005_evttabestab = get_object_or_404(
        s1005evtTabEstab,
        id=pk)

    if not versao or versao == '|':
        versao = s1005_evttabestab.versao

    evento = 's1005evtTabEstab'[5:]
    arquivo = '/xsd/esocial/%s/%s.xsd' % (versao, evento)

    import os.path

    if os.path.isfile(BASE_DIR + arquivo):

        xmlns = get_xmlns(arquivo)

    else:

        xmlns = ''

    s1005_evttabestab_lista = s1005evtTabEstab.objects. \
        filter(id=pk).all()


    s1005_inclusao_lista = s1005inclusao.objects. \
        filter(s1005_evttabestab_id__in=listar_ids(s1005_evttabestab_lista)).all()

    s1005_inclusao_procadmjudrat_lista = s1005inclusaoprocAdmJudRat.objects. \
        filter(s1005_inclusao_id__in=listar_ids(s1005_inclusao_lista)).all()

    s1005_inclusao_procadmjudfap_lista = s1005inclusaoprocAdmJudFap.objects. \
        filter(s1005_inclusao_id__in=listar_ids(s1005_inclusao_lista)).all()

    s1005_inclusao_infocaepf_lista = s1005inclusaoinfoCaepf.objects. \
        filter(s1005_inclusao_id__in=listar_ids(s1005_inclusao_lista)).all()

    s1005_inclusao_infoobra_lista = s1005inclusaoinfoObra.objects. \
        filter(s1005_inclusao_id__in=listar_ids(s1005_inclusao_lista)).all()

    s1005_inclusao_infoenteduc_lista = s1005inclusaoinfoEntEduc.objects. \
        filter(s1005_inclusao_id__in=listar_ids(s1005_inclusao_lista)).all()

    s1005_inclusao_infopcd_lista = s1005inclusaoinfoPCD.objects. \
        filter(s1005_inclusao_id__in=listar_ids(s1005_inclusao_lista)).all()

    s1005_alteracao_lista = s1005alteracao.objects. \
        filter(s1005_evttabestab_id__in=listar_ids(s1005_evttabestab_lista)).all()

    s1005_alteracao_procadmjudrat_lista = s1005alteracaoprocAdmJudRat.objects. \
        filter(s1005_alteracao_id__in=listar_ids(s1005_alteracao_lista)).all()

    s1005_alteracao_procadmjudfap_lista = s1005alteracaoprocAdmJudFap.objects. \
        filter(s1005_alteracao_id__in=listar_ids(s1005_alteracao_lista)).all()

    s1005_alteracao_infocaepf_lista = s1005alteracaoinfoCaepf.objects. \
        filter(s1005_alteracao_id__in=listar_ids(s1005_alteracao_lista)).all()

    s1005_alteracao_infoobra_lista = s1005alteracaoinfoObra.objects. \
        filter(s1005_alteracao_id__in=listar_ids(s1005_alteracao_lista)).all()

    s1005_alteracao_infoenteduc_lista = s1005alteracaoinfoEntEduc.objects. \
        filter(s1005_alteracao_id__in=listar_ids(s1005_alteracao_lista)).all()

    s1005_alteracao_infopcd_lista = s1005alteracaoinfoPCD.objects. \
        filter(s1005_alteracao_id__in=listar_ids(s1005_alteracao_lista)).all()

    s1005_alteracao_novavalidade_lista = s1005alteracaonovaValidade.objects. \
        filter(s1005_alteracao_id__in=listar_ids(s1005_alteracao_lista)).all()

    s1005_exclusao_lista = s1005exclusao.objects. \
        filter(s1005_evttabestab_id__in=listar_ids(s1005_evttabestab_lista)).all()


    context = {
        'xmlns': xmlns,
        'versao': versao,
        'base': s1005_evttabestab,
        's1005_evttabestab_lista': s1005_evttabestab_lista,
        'pk': int(pk),
        's1005_evttabestab': s1005_evttabestab,
        's1005_inclusao_lista': s1005_inclusao_lista,
        's1005_inclusao_procadmjudrat_lista': s1005_inclusao_procadmjudrat_lista,
        's1005_inclusao_procadmjudfap_lista': s1005_inclusao_procadmjudfap_lista,
        's1005_inclusao_infocaepf_lista': s1005_inclusao_infocaepf_lista,
        's1005_inclusao_infoobra_lista': s1005_inclusao_infoobra_lista,
        's1005_inclusao_infoenteduc_lista': s1005_inclusao_infoenteduc_lista,
        's1005_inclusao_infopcd_lista': s1005_inclusao_infopcd_lista,
        's1005_alteracao_lista': s1005_alteracao_lista,
        's1005_alteracao_procadmjudrat_lista': s1005_alteracao_procadmjudrat_lista,
        's1005_alteracao_procadmjudfap_lista': s1005_alteracao_procadmjudfap_lista,
        's1005_alteracao_infocaepf_lista': s1005_alteracao_infocaepf_lista,
        's1005_alteracao_infoobra_lista': s1005_alteracao_infoobra_lista,
        's1005_alteracao_infoenteduc_lista': s1005_alteracao_infoenteduc_lista,
        's1005_alteracao_infopcd_lista': s1005_alteracao_infopcd_lista,
        's1005_alteracao_novavalidade_lista': s1005_alteracao_novavalidade_lista,
        's1005_exclusao_lista': s1005_exclusao_lista,
    }

    t = get_template('s1005_evttabestab.xml')
    xml = t.render(context)
    return xml



def gerar_xml_s1005(request, pk, versao=None):

    from emensageriapro.settings import BASE_DIR
    s1005_evttabestab = get_object_or_404(
        s1005evtTabEstab,
        id=pk)
    return gerar_xml_s1005_func(pk, versao)


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes import salvar_arquivo_esocial
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s1005_evttabestab = get_object_or_404(
        s1005evtTabEstab,
        id=pk)

    if s1005_evttabestab.arquivo_original:
        xml = ler_arquivo(s1005_evttabestab.arquivo)

    else:
        xml = gerar_xml_s1005(request, pk)

    if 'Signature' in xml:
        xml_assinado = xml
        s1005evtTabEstab.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    else:

        if not s1005_evttabestab.transmissor_lote_esocial:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_esocial \
                import vincular_transmissor_esocial, criar_transmissor_esocial, get_grupo

            grupo = get_grupo(s1005evtTabEstab)

            criar_transmissor_esocial(request,
                grupo,
                s1005_evttabestab.nrinsc,
                s1005_evttabestab.tpinsc)

            vincular_transmissor_esocial(request,
                grupo,
                s1005evtTabEstab,
                s1005_evttabestab)

        s1005_evttabestab = get_object_or_404(
            s1005evtTabEstab,
            id=pk)

        xml_assinado = assinar_esocial(
            request,
            xml,
            s1005_evttabestab.transmissor_lote_esocial_id)

        if 'Signature' in xml_assinado:

            s1005evtTabEstab.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)
        else:

            s1005evtTabEstab.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_GERADO)

    arquivo = '/arquivos/Eventos/s1005_evttabestab/%s.xml' % (s1005_evttabestab.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s1005_evttabestab/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):

        salvar_arquivo_esocial(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)

    return xml_assinado


@login_required
def gerar_xml(request, pk):

    if pk:

        xml_assinado = gerar_xml_assinado(request, pk)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.now(),}

    return render(request, 'permissao_negada.html', context)