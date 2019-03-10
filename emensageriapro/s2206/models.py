#coding: utf-8

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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



CHOICES_S2206_DIA = (
    (1, u'1 - Segunda-Feira'),
    (2, u'2 - Terça-Feira'),
    (3, u'3 - Quarta-Feira'),
    (4, u'4 - Quinta-Feira'),
    (5, u'5 - Sexta-Feira'),
    (6, u'6 - Sábado'),
    (7, u'7 - Domingo'),
    (8, u'8 - Dia variável'),
)

CHOICES_S2206_INDABONOPERM = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2206_INDPARCREMUN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2206_INDTETORGPS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2206_MTVALTER = (
    (1, u'1 - Promoção'),
    (2, u'2 - Readaptação'),
    (3, u'3 - Aproveitamento'),
    (8, u'8 - Outros'),
    (9, u'9 - Não alterado'),
)

CHOICES_S2206_NATATIVIDADE = (
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural'),
)

CHOICES_S2206_TMPPARC = (
    (0, u'0 - Não é contrato em tempo parcial'),
    (1, u'1 - Limitado a 25 horas semanais'),
    (2, u'2 - Limitado a 30 horas semanais'),
    (3, u'3 - Limitado a 26 horas semanais'),
)

CHOICES_S2206_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2206_TPJORNADA = (
    (1, u'1 - Jornada com horário diário e folga fixos'),
    (2, u'2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)'),
    (3, u'3 - Jornada com horário diário fixo e folga variável'),
    (9, u'9 - Demais tipos de jornada'),
)

CHOICES_S2206_TPPLANRP = (
    (1, u'1 - Plano previdenciário ou único'),
    (2, u'2 - Plano financeiro'),
)

CHOICES_S2206_TPREGJOR = (
    (1, u'1 - Submetidos a Horário de Trabalho (Cap. II da CLT)'),
    (2, u'2 - Atividade Externa especificada no Inciso I do Art. 62 da CLT'),
    (3, u'3 - Funções especificadas no Inciso II do Art. 62 da CLT'),
    (4, u'4 - Teletrabalho, previsto no Inciso III do Art. 62 da CLT'),
)

ESTADOS = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AM', u'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', u'Minas Gerais'),
    ('MS', u'Mato Grosso do Sul'),
    ('MT', u'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('RS', u'Rio Grande do Sul'),
    ('SC', u'Santa Catarina'),
    ('SE', u'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', u'Tocantins'),
)

class s2206alvaraJudicial(SoftDeletionModel):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    def evento(self): return self.s2206_evtaltcontratual.evento()
    nrprocjud = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.nrprocjud)
    #s2206_alvarajudicial_custom#

    class Meta:
        db_table = r's2206_alvarajudicial'       
        managed = True # s2206_alvarajudicial #
        unique_together = (
            #custom_unique_together_s2206_alvarajudicial#
            
        )
        index_together = (
            #custom_index_together_s2206_alvarajudicial
            #index_together_s2206_alvarajudicial
        )
        permissions = (
            ("can_view_s2206_alvarajudicial", "Can view s2206_alvarajudicial"),
            #custom_permissions_s2206_alvarajudicial
        )
        ordering = ['s2206_evtaltcontratual', 'nrprocjud']



class s2206alvaraJudicialSerializer(ModelSerializer):
    class Meta:
        model = s2206alvaraJudicial
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206aprend(SoftDeletionModel):
    s2206_infoceletista = models.OneToOneField('s2206infoCeletista',
        related_name='%(class)s_s2206_infoceletista')
    def evento(self): return self.s2206_infoceletista.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2206_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_infoceletista) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2206_aprend_custom#

    class Meta:
        db_table = r's2206_aprend'       
        managed = True # s2206_aprend #
        unique_together = (
            #custom_unique_together_s2206_aprend#
            
        )
        index_together = (
            #custom_index_together_s2206_aprend
            #index_together_s2206_aprend
        )
        permissions = (
            ("can_view_s2206_aprend", "Can view s2206_aprend"),
            #custom_permissions_s2206_aprend
        )
        ordering = ['s2206_infoceletista', 'tpinsc', 'nrinsc']



class s2206aprendSerializer(ModelSerializer):
    class Meta:
        model = s2206aprend
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206filiacaoSindical(SoftDeletionModel):
    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    def evento(self): return self.s2206_evtaltcontratual.evento()
    cnpjsindtrab = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.cnpjsindtrab)
    #s2206_filiacaosindical_custom#

    class Meta:
        db_table = r's2206_filiacaosindical'       
        managed = True # s2206_filiacaosindical #
        unique_together = (
            #custom_unique_together_s2206_filiacaosindical#
            
        )
        index_together = (
            #custom_index_together_s2206_filiacaosindical
            #index_together_s2206_filiacaosindical
        )
        permissions = (
            ("can_view_s2206_filiacaosindical", "Can view s2206_filiacaosindical"),
            #custom_permissions_s2206_filiacaosindical
        )
        ordering = ['s2206_evtaltcontratual', 'cnpjsindtrab']



class s2206filiacaoSindicalSerializer(ModelSerializer):
    class Meta:
        model = s2206filiacaoSindical
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206horContratual(SoftDeletionModel):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    def evento(self): return self.s2206_evtaltcontratual.evento()
    qtdhrssem = models.DecimalField(max_digits=15, decimal_places=2, max_length=4, blank=True, null=True)
    tpjornada = models.IntegerField(choices=CHOICES_S2206_TPJORNADA)
    dsctpjorn = models.CharField(max_length=100, blank=True, null=True)
    tmpparc = models.IntegerField(choices=CHOICES_S2206_TMPPARC)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.tpjornada) + ' - ' + unicode(self.tmpparc)
    #s2206_horcontratual_custom#

    class Meta:
        db_table = r's2206_horcontratual'       
        managed = True # s2206_horcontratual #
        unique_together = (
            #custom_unique_together_s2206_horcontratual#
            
        )
        index_together = (
            #custom_index_together_s2206_horcontratual
            #index_together_s2206_horcontratual
        )
        permissions = (
            ("can_view_s2206_horcontratual", "Can view s2206_horcontratual"),
            #custom_permissions_s2206_horcontratual
        )
        ordering = ['s2206_evtaltcontratual', 'tpjornada', 'tmpparc']



class s2206horContratualSerializer(ModelSerializer):
    class Meta:
        model = s2206horContratual
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206horario(SoftDeletionModel):
    s2206_horcontratual = models.ForeignKey('s2206horContratual',
        related_name='%(class)s_s2206_horcontratual')
    def evento(self): return self.s2206_horcontratual.evento()
    dia = models.IntegerField(choices=CHOICES_S2206_DIA)
    codhorcontrat = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_horcontratual) + ' - ' + unicode(self.dia) + ' - ' + unicode(self.codhorcontrat)
    #s2206_horario_custom#

    class Meta:
        db_table = r's2206_horario'       
        managed = True # s2206_horario #
        unique_together = (
            #custom_unique_together_s2206_horario#
            
        )
        index_together = (
            #custom_index_together_s2206_horario
            #index_together_s2206_horario
        )
        permissions = (
            ("can_view_s2206_horario", "Can view s2206_horario"),
            #custom_permissions_s2206_horario
        )
        ordering = ['s2206_horcontratual', 'dia', 'codhorcontrat']



class s2206horarioSerializer(ModelSerializer):
    class Meta:
        model = s2206horario
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206infoCeletista(SoftDeletionModel):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    def evento(self): return self.s2206_evtaltcontratual.evento()
    tpregjor = models.IntegerField(choices=CHOICES_S2206_TPREGJOR)
    natatividade = models.IntegerField(choices=CHOICES_S2206_NATATIVIDADE)
    dtbase = models.IntegerField(blank=True, null=True)
    cnpjsindcategprof = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.tpregjor) + ' - ' + unicode(self.natatividade) + ' - ' + unicode(self.cnpjsindcategprof)
    #s2206_infoceletista_custom#

    class Meta:
        db_table = r's2206_infoceletista'       
        managed = True # s2206_infoceletista #
        unique_together = (
            #custom_unique_together_s2206_infoceletista#
            
        )
        index_together = (
            #custom_index_together_s2206_infoceletista
            #index_together_s2206_infoceletista
        )
        permissions = (
            ("can_view_s2206_infoceletista", "Can view s2206_infoceletista"),
            #custom_permissions_s2206_infoceletista
        )
        ordering = ['s2206_evtaltcontratual', 'tpregjor', 'natatividade', 'cnpjsindcategprof']



class s2206infoCeletistaSerializer(ModelSerializer):
    class Meta:
        model = s2206infoCeletista
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206infoEstatutario(SoftDeletionModel):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    def evento(self): return self.s2206_evtaltcontratual.evento()
    tpplanrp = models.IntegerField(choices=CHOICES_S2206_TPPLANRP)
    indtetorgps = models.CharField(choices=CHOICES_S2206_INDTETORGPS, max_length=1, blank=True, null=True)
    indabonoperm = models.CharField(choices=CHOICES_S2206_INDABONOPERM, max_length=1, blank=True, null=True)
    indparcremun = models.CharField(choices=CHOICES_S2206_INDPARCREMUN, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.tpplanrp)
    #s2206_infoestatutario_custom#

    class Meta:
        db_table = r's2206_infoestatutario'       
        managed = True # s2206_infoestatutario #
        unique_together = (
            #custom_unique_together_s2206_infoestatutario#
            
        )
        index_together = (
            #custom_index_together_s2206_infoestatutario
            #index_together_s2206_infoestatutario
        )
        permissions = (
            ("can_view_s2206_infoestatutario", "Can view s2206_infoestatutario"),
            #custom_permissions_s2206_infoestatutario
        )
        ordering = ['s2206_evtaltcontratual', 'tpplanrp']



class s2206infoEstatutarioSerializer(ModelSerializer):
    class Meta:
        model = s2206infoEstatutario
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206localTrabDom(SoftDeletionModel):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    def evento(self): return self.s2206_evtaltcontratual.evento()
    tplograd = models.TextField(max_length=4)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2206_localtrabdom_custom#

    class Meta:
        db_table = r's2206_localtrabdom'       
        managed = True # s2206_localtrabdom #
        unique_together = (
            #custom_unique_together_s2206_localtrabdom#
            
        )
        index_together = (
            #custom_index_together_s2206_localtrabdom
            #index_together_s2206_localtrabdom
        )
        permissions = (
            ("can_view_s2206_localtrabdom", "Can view s2206_localtrabdom"),
            #custom_permissions_s2206_localtrabdom
        )
        ordering = ['s2206_evtaltcontratual', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf']



class s2206localTrabDomSerializer(ModelSerializer):
    class Meta:
        model = s2206localTrabDom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206localTrabGeral(SoftDeletionModel):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    def evento(self): return self.s2206_evtaltcontratual.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2206_TPINSC)
    nrinsc = models.CharField(max_length=15)
    desccomp = models.CharField(max_length=80, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2206_localtrabgeral_custom#

    class Meta:
        db_table = r's2206_localtrabgeral'       
        managed = True # s2206_localtrabgeral #
        unique_together = (
            #custom_unique_together_s2206_localtrabgeral#
            
        )
        index_together = (
            #custom_index_together_s2206_localtrabgeral
            #index_together_s2206_localtrabgeral
        )
        permissions = (
            ("can_view_s2206_localtrabgeral", "Can view s2206_localtrabgeral"),
            #custom_permissions_s2206_localtrabgeral
        )
        ordering = ['s2206_evtaltcontratual', 'tpinsc', 'nrinsc']



class s2206localTrabGeralSerializer(ModelSerializer):
    class Meta:
        model = s2206localTrabGeral
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206observacoes(SoftDeletionModel):
    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    def evento(self): return self.s2206_evtaltcontratual.evento()
    observacao = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.observacao)
    #s2206_observacoes_custom#

    class Meta:
        db_table = r's2206_observacoes'       
        managed = True # s2206_observacoes #
        unique_together = (
            #custom_unique_together_s2206_observacoes#
            
        )
        index_together = (
            #custom_index_together_s2206_observacoes
            #index_together_s2206_observacoes
        )
        permissions = (
            ("can_view_s2206_observacoes", "Can view s2206_observacoes"),
            #custom_permissions_s2206_observacoes
        )
        ordering = ['s2206_evtaltcontratual', 'observacao']



class s2206observacoesSerializer(ModelSerializer):
    class Meta:
        model = s2206observacoes
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206servPubl(SoftDeletionModel):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    def evento(self): return self.s2206_evtaltcontratual.evento()
    mtvalter = models.IntegerField(choices=CHOICES_S2206_MTVALTER)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.mtvalter)
    #s2206_servpubl_custom#

    class Meta:
        db_table = r's2206_servpubl'       
        managed = True # s2206_servpubl #
        unique_together = (
            #custom_unique_together_s2206_servpubl#
            
        )
        index_together = (
            #custom_index_together_s2206_servpubl
            #index_together_s2206_servpubl
        )
        permissions = (
            ("can_view_s2206_servpubl", "Can view s2206_servpubl"),
            #custom_permissions_s2206_servpubl
        )
        ordering = ['s2206_evtaltcontratual', 'mtvalter']



class s2206servPublSerializer(ModelSerializer):
    class Meta:
        model = s2206servPubl
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2206trabTemp(SoftDeletionModel):
    s2206_infoceletista = models.OneToOneField('s2206infoCeletista',
        related_name='%(class)s_s2206_infoceletista')
    def evento(self): return self.s2206_infoceletista.evento()
    justprorr = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2206_infoceletista) + ' - ' + unicode(self.justprorr)
    #s2206_trabtemp_custom#

    class Meta:
        db_table = r's2206_trabtemp'       
        managed = True # s2206_trabtemp #
        unique_together = (
            #custom_unique_together_s2206_trabtemp#
            
        )
        index_together = (
            #custom_index_together_s2206_trabtemp
            #index_together_s2206_trabtemp
        )
        permissions = (
            ("can_view_s2206_trabtemp", "Can view s2206_trabtemp"),
            #custom_permissions_s2206_trabtemp
        )
        ordering = ['s2206_infoceletista', 'justprorr']



class s2206trabTempSerializer(ModelSerializer):
    class Meta:
        model = s2206trabTemp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
