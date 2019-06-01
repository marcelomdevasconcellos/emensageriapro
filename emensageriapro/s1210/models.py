#coding:utf-8
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
from emensageriapro.s1210.choices import *
get_model = apps.get_model


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


STATUS_EVENTO_CADASTRADO = 0
STATUS_EVENTO_IMPORTADO = 1
STATUS_EVENTO_DUPLICADO = 2
STATUS_EVENTO_GERADO = 3
STATUS_EVENTO_GERADO_ERRO = 4
STATUS_EVENTO_ASSINADO = 5
STATUS_EVENTO_ASSINADO_ERRO = 6
STATUS_EVENTO_VALIDADO = 7
STATUS_EVENTO_VALIDADO_ERRO = 8
STATUS_EVENTO_AGUARD_PRECEDENCIA = 9
STATUS_EVENTO_AGUARD_ENVIO = 10
STATUS_EVENTO_ENVIADO = 11
STATUS_EVENTO_ENVIADO_ERRO = 12
STATUS_EVENTO_PROCESSADO = 13





class s1210deps(SoftDeletionModel):

    s1210_evtpgtos = models.ForeignKey('esocial.s1210evtPgtos', 
        related_name='%(class)s_s1210_evtpgtos', )
    
    def evento(self): 
        return self.s1210_evtpgtos.evento()
    vrdeddep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_evtpgtos),
            unicode(self.vrdeddep),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de dependentes do beneficiário do pagamento'
        db_table = r's1210_deps'       
        managed = True # s1210_deps #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210deps", "Can view S1210DEPS"),
            ("can_view_menu_s1210deps", "Can view menu S1210DEPS"),)
            
        ordering = [
            's1210_evtpgtos',
            'vrdeddep',]



class s1210depsSerializer(ModelSerializer):

    class Meta:
    
        model = s1210deps
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoAnt(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto', 
        related_name='%(class)s_s1210_infopgto', )
    
    def evento(self): 
        return self.s1210_infopgto.evento()
    codcateg = models.IntegerField(null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_infopgto),
            unicode(self.codcateg),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Pagamento relativo a competências anteriores ao início de obrigatoriedade do eSocial'
        db_table = r's1210_detpgtoant'       
        managed = True # s1210_detpgtoant #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoAnt", "Can view S1210DETPGTOANT"),
            ("can_view_menu_s1210detPgtoAnt", "Can view menu S1210DETPGTOANT"),)
            
        ordering = [
            's1210_infopgto',
            'codcateg',]



class s1210detPgtoAntSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoAnt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoAntinfoPgtoAnt(SoftDeletionModel):

    s1210_detpgtoant = models.ForeignKey('s1210.s1210detPgtoAnt', 
        related_name='%(class)s_s1210_detpgtoant', )
    
    def evento(self): 
        return self.s1210_detpgtoant.evento()
    tpbcirrf = models.TextField(null=True, )
    vrbcirrf = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_detpgtoant),
            unicode(self.tpbcirrf),
            unicode(self.vrbcirrf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento do pagamento'
        db_table = r's1210_detpgtoant_infopgtoant'       
        managed = True # s1210_detpgtoant_infopgtoant #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoAntinfoPgtoAnt", "Can view S1210DETPGTOANTINFOPGTOANT"),
            ("can_view_menu_s1210detPgtoAntinfoPgtoAnt", "Can view menu S1210DETPGTOANTINFOPGTOANT"),)
            
        ordering = [
            's1210_detpgtoant',
            'tpbcirrf',
            'vrbcirrf',]



class s1210detPgtoAntinfoPgtoAntSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoAntinfoPgtoAnt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoBenPr(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto', 
        related_name='%(class)s_s1210_infopgto', )
    
    def evento(self): 
        return self.s1210_infopgto.evento()
    perref = models.CharField(max_length=7, null=True, )
    idedmdev = models.CharField(max_length=30, null=True, )
    indpgtott = models.CharField(choices=CHOICES_S1210_INDPGTOTT_DETPGTOBENPR, max_length=1, null=True, )
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_infopgto),
            unicode(self.perref),
            unicode(self.idedmdev),
            unicode(self.indpgtott),
            unicode(self.vrliq),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento de pagamentos relativos a benefícios previdenciários'
        db_table = r's1210_detpgtobenpr'       
        managed = True # s1210_detpgtobenpr #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoBenPr", "Can view S1210DETPGTOBENPR"),
            ("can_view_menu_s1210detPgtoBenPr", "Can view menu S1210DETPGTOBENPR"),)
            
        ordering = [
            's1210_infopgto',
            'perref',
            'idedmdev',
            'indpgtott',
            'vrliq',]



class s1210detPgtoBenPrSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoBenPr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoBenPrinfoPgtoParc(SoftDeletionModel):

    s1210_detpgtobenpr = models.ForeignKey('s1210.s1210detPgtoBenPr', 
        related_name='%(class)s_s1210_detpgtobenpr', )
    
    def evento(self): 
        return self.s1210_detpgtobenpr.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_detpgtobenpr),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.vrrubr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações complentares relacionadas ao pagamento efetuado em valor menor que o apurado no demonstrativo.'
        db_table = r's1210_detpgtobenpr_infopgtoparc'       
        managed = True # s1210_detpgtobenpr_infopgtoparc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoBenPrinfoPgtoParc", "Can view S1210DETPGTOBENPRINFOPGTOPARC"),
            ("can_view_menu_s1210detPgtoBenPrinfoPgtoParc", "Can view menu S1210DETPGTOBENPRINFOPGTOPARC"),)
            
        ordering = [
            's1210_detpgtobenpr',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoBenPrinfoPgtoParcSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoBenPrinfoPgtoParc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoBenPrretPgtoTot(SoftDeletionModel):

    s1210_detpgtobenpr = models.ForeignKey('s1210.s1210detPgtoBenPr', 
        related_name='%(class)s_s1210_detpgtobenpr', )
    
    def evento(self): 
        return self.s1210_detpgtobenpr.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_detpgtobenpr),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.vrrubr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Retenções efetuadas no ato do pagamento pelo valor total do demonstrativo.'
        db_table = r's1210_detpgtobenpr_retpgtotot'       
        managed = True # s1210_detpgtobenpr_retpgtotot #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoBenPrretPgtoTot", "Can view S1210DETPGTOBENPRRETPGTOTOT"),
            ("can_view_menu_s1210detPgtoBenPrretPgtoTot", "Can view menu S1210DETPGTOBENPRRETPGTOTOT"),)
            
        ordering = [
            's1210_detpgtobenpr',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoBenPrretPgtoTotSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoBenPrretPgtoTot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoFer(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto', 
        related_name='%(class)s_s1210_infopgto', )
    
    def evento(self): 
        return self.s1210_infopgto.evento()
    codcateg = models.IntegerField(null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    dtinigoz = models.DateField(null=True, )
    qtdias = models.IntegerField(null=True, )
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_infopgto),
            unicode(self.codcateg),
            unicode(self.dtinigoz),
            unicode(self.qtdias),
            unicode(self.vrliq),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento dos pagamentos efetuados relativos a férias'
        db_table = r's1210_detpgtofer'       
        managed = True # s1210_detpgtofer #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoFer", "Can view S1210DETPGTOFER"),
            ("can_view_menu_s1210detPgtoFer", "Can view menu S1210DETPGTOFER"),)
            
        ordering = [
            's1210_infopgto',
            'codcateg',
            'dtinigoz',
            'qtdias',
            'vrliq',]



class s1210detPgtoFerSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoFer
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoFerdetRubrFer(SoftDeletionModel):

    s1210_detpgtofer = models.ForeignKey('s1210.s1210detPgtoFer', 
        related_name='%(class)s_s1210_detpgtofer', )
    
    def evento(self): 
        return self.s1210_detpgtofer.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_detpgtofer),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.vrrubr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento das rubricas do Recibo Antecipado de Férias'
        db_table = r's1210_detpgtofer_detrubrfer'       
        managed = True # s1210_detpgtofer_detrubrfer #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoFerdetRubrFer", "Can view S1210DETPGTOFERDETRUBRFER"),
            ("can_view_menu_s1210detPgtoFerdetRubrFer", "Can view menu S1210DETPGTOFERDETRUBRFER"),)
            
        ordering = [
            's1210_detpgtofer',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoFerdetRubrFerSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoFerdetRubrFer
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoFerpenAlim(SoftDeletionModel):

    s1210_detpgtofer_detrubrfer = models.ForeignKey('s1210.s1210detPgtoFerdetRubrFer', 
        related_name='%(class)s_s1210_detpgtofer_detrubrfer', )
    
    def evento(self): 
        return self.s1210_detpgtofer_detrubrfer.evento()
    cpfbenef = models.CharField(max_length=11, null=True, )
    dtnasctobenef = models.DateField(blank=True, null=True, )
    nmbenefic = models.CharField(max_length=70, null=True, )
    vlrpensao = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_detpgtofer_detrubrfer),
            unicode(self.cpfbenef),
            unicode(self.nmbenefic),
            unicode(self.vlrpensao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre beneficiários de pensão alimentícia.'
        db_table = r's1210_detpgtofer_penalim'       
        managed = True # s1210_detpgtofer_penalim #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoFerpenAlim", "Can view S1210DETPGTOFERPENALIM"),
            ("can_view_menu_s1210detPgtoFerpenAlim", "Can view menu S1210DETPGTOFERPENALIM"),)
            
        ordering = [
            's1210_detpgtofer_detrubrfer',
            'cpfbenef',
            'nmbenefic',
            'vlrpensao',]



class s1210detPgtoFerpenAlimSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoFerpenAlim
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoFl(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto', 
        related_name='%(class)s_s1210_infopgto', )
    
    def evento(self): 
        return self.s1210_infopgto.evento()
    perref = models.CharField(max_length=7, blank=True, null=True, )
    idedmdev = models.CharField(max_length=30, null=True, )
    indpgtott = models.CharField(choices=CHOICES_S1210_INDPGTOTT_DETPGTOFL, max_length=1, null=True, )
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    nrrecarq = models.CharField(max_length=40, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_infopgto),
            unicode(self.idedmdev),
            unicode(self.indpgtott),
            unicode(self.vrliq),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento dos pagamentos efetuados, relativos a folha de pagamento e rescisões contratuais, apurados em S-1200, S-1202, S-2299 e S-2399'
        db_table = r's1210_detpgtofl'       
        managed = True # s1210_detpgtofl #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoFl", "Can view S1210DETPGTOFL"),
            ("can_view_menu_s1210detPgtoFl", "Can view menu S1210DETPGTOFL"),)
            
        ordering = [
            's1210_infopgto',
            'idedmdev',
            'indpgtott',
            'vrliq',]



class s1210detPgtoFlSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoFl
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoFlinfoPgtoParc(SoftDeletionModel):

    s1210_detpgtofl = models.ForeignKey('s1210.s1210detPgtoFl', 
        related_name='%(class)s_s1210_detpgtofl', )
    
    def evento(self): 
        return self.s1210_detpgtofl.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_detpgtofl),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.vrrubr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações complentares relacionadas ao pagamento efetuado em valor menor que o apurado no demonstrativo.'
        db_table = r's1210_detpgtofl_infopgtoparc'       
        managed = True # s1210_detpgtofl_infopgtoparc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoFlinfoPgtoParc", "Can view S1210DETPGTOFLINFOPGTOPARC"),
            ("can_view_menu_s1210detPgtoFlinfoPgtoParc", "Can view menu S1210DETPGTOFLINFOPGTOPARC"),)
            
        ordering = [
            's1210_detpgtofl',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoFlinfoPgtoParcSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoFlinfoPgtoParc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoFlpenAlim(SoftDeletionModel):

    s1210_detpgtofl_retpgtotot = models.ForeignKey('s1210.s1210detPgtoFlretPgtoTot', 
        related_name='%(class)s_s1210_detpgtofl_retpgtotot', )
    
    def evento(self): 
        return self.s1210_detpgtofl_retpgtotot.evento()
    cpfbenef = models.CharField(max_length=11, null=True, )
    dtnasctobenef = models.DateField(blank=True, null=True, )
    nmbenefic = models.CharField(max_length=70, null=True, )
    vlrpensao = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_detpgtofl_retpgtotot),
            unicode(self.cpfbenef),
            unicode(self.nmbenefic),
            unicode(self.vlrpensao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre beneficiários de pensão alimentícia.'
        db_table = r's1210_detpgtofl_penalim'       
        managed = True # s1210_detpgtofl_penalim #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoFlpenAlim", "Can view S1210DETPGTOFLPENALIM"),
            ("can_view_menu_s1210detPgtoFlpenAlim", "Can view menu S1210DETPGTOFLPENALIM"),)
            
        ordering = [
            's1210_detpgtofl_retpgtotot',
            'cpfbenef',
            'nmbenefic',
            'vlrpensao',]



class s1210detPgtoFlpenAlimSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoFlpenAlim
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210detPgtoFlretPgtoTot(SoftDeletionModel):

    s1210_detpgtofl = models.ForeignKey('s1210.s1210detPgtoFl', 
        related_name='%(class)s_s1210_detpgtofl', )
    
    def evento(self): 
        return self.s1210_detpgtofl.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_detpgtofl),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.vrrubr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Retenções efetuadas no ato do pagamento pelo valor total do demonstrativo.'
        db_table = r's1210_detpgtofl_retpgtotot'       
        managed = True # s1210_detpgtofl_retpgtotot #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210detPgtoFlretPgtoTot", "Can view S1210DETPGTOFLRETPGTOTOT"),
            ("can_view_menu_s1210detPgtoFlretPgtoTot", "Can view menu S1210DETPGTOFLRETPGTOTOT"),)
            
        ordering = [
            's1210_detpgtofl',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoFlretPgtoTotSerializer(ModelSerializer):

    class Meta:
    
        model = s1210detPgtoFlretPgtoTot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210idePgtoExt(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto', 
        related_name='%(class)s_s1210_infopgto', )
    
    def evento(self): 
        return self.s1210_infopgto.evento()
    codpais = models.TextField(null=True, )
    indnif = models.IntegerField(choices=CHOICES_S1210_INDNIF_IDEPGTOEXT, null=True, )
    nifbenef = models.CharField(max_length=20, blank=True, null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, blank=True, null=True, )
    complem = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    nmcid = models.CharField(max_length=50, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_infopgto),
            unicode(self.codpais),
            unicode(self.indnif),
            unicode(self.dsclograd),
            unicode(self.nmcid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações complementares relativas a pagamentos efetuados a beneficiário residente fiscal no exterior.'
        db_table = r's1210_idepgtoext'       
        managed = True # s1210_idepgtoext #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210idePgtoExt", "Can view S1210IDEPGTOEXT"),
            ("can_view_menu_s1210idePgtoExt", "Can view menu S1210IDEPGTOEXT"),)
            
        ordering = [
            's1210_infopgto',
            'codpais',
            'indnif',
            'dsclograd',
            'nmcid',]



class s1210idePgtoExtSerializer(ModelSerializer):

    class Meta:
    
        model = s1210idePgtoExt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1210infoPgto(SoftDeletionModel):

    s1210_evtpgtos = models.ForeignKey('esocial.s1210evtPgtos', 
        related_name='%(class)s_s1210_evtpgtos', )
    
    def evento(self): 
        return self.s1210_evtpgtos.evento()
    dtpgto = models.DateField(null=True, )
    tppgto = models.IntegerField(choices=CHOICES_S1210_TPPGTO, null=True, )
    indresbr = models.CharField(choices=CHOICES_S1210_INDRESBR, max_length=1, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1210_evtpgtos),
            unicode(self.dtpgto),
            unicode(self.tppgto),
            unicode(self.indresbr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações dos pagamentos efetuados'
        db_table = r's1210_infopgto'       
        managed = True # s1210_infopgto #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1210infoPgto", "Can view S1210INFOPGTO"),
            ("can_view_menu_s1210infoPgto", "Can view menu S1210INFOPGTO"),)
            
        ordering = [
            's1210_evtpgtos',
            'dtpgto',
            'tppgto',
            'indresbr',]



class s1210infoPgtoSerializer(ModelSerializer):

    class Meta:
    
        model = s1210infoPgto
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()