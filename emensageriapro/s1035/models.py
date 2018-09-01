#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



PERIODOS = (
    ('2018-01', u'Janeiro/2018'),
    ('2018-02', u'Fevereiro/2018'),
    ('2018-03', u'Março/2018'),
    ('2018-04', u'Abril/2018'),
    ('2018-05', u'Maio/2018'),
    ('2018-06', u'Junho/2018'),
    ('2018-07', u'Julho/2018'),
    ('2018-08', u'Agosto/2018'),
    ('2018-09', u'Setembro/2018'),
    ('2018-10', u'Outubro/2018'),
    ('2018-11', u'Novembro/2018'),
    ('2018-12', u'Dezembro/2018'),
)

CHOICES_S1035_ALTERACAO_SITCARR = (
    (1, u'1 - Criação'),
    (2, u'2 - Extinção'),
    (3, u'3 - Reestruturação'),
)

CHOICES_S1035_INCLUSAO_SITCARR = (
    (1, u'1 - Criação'),
    (2, u'2 - Extinção'),
    (3, u'3 - Reestruturação'),
)

class s1035alteracao(models.Model):
    s1035_evttabcarreira = models.OneToOneField('esocial.s1035evtTabCarreira',
        related_name='%(class)s_s1035_evttabcarreira')
    def evento(self): return self.s1035_evttabcarreira.evento()
    codcarreira = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dsccarreira = models.CharField(max_length=100)
    leicarr = models.CharField(max_length=12, blank=True, null=True)
    dtleicarr = models.DateField()
    sitcarr = models.IntegerField(choices=CHOICES_S1035_ALTERACAO_SITCARR)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1035_evttabcarreira) + ' - ' + unicode(self.codcarreira) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.dsccarreira) + ' - ' + unicode(self.leicarr) + ' - ' + unicode(self.dtleicarr) + ' - ' + unicode(self.sitcarr)
    #s1035_alteracao_custom#
    #s1035_alteracao_custom#
    class Meta:
        db_table = r's1035_alteracao'
        managed = True
        ordering = ['s1035_evttabcarreira', 'codcarreira', 'inivalid', 'fimvalid', 'dsccarreira', 'leicarr', 'dtleicarr', 'sitcarr']


class s1035alteracaonovaValidade(models.Model):
    s1035_alteracao = models.OneToOneField('s1035alteracao',
        related_name='%(class)s_s1035_alteracao')
    def evento(self): return self.s1035_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1035_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1035_alteracao_novavalidade_custom#
    #s1035_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1035_alteracao_novavalidade'
        managed = True
        ordering = ['s1035_alteracao', 'inivalid', 'fimvalid']


class s1035exclusao(models.Model):
    s1035_evttabcarreira = models.OneToOneField('esocial.s1035evtTabCarreira',
        related_name='%(class)s_s1035_evttabcarreira')
    def evento(self): return self.s1035_evttabcarreira.evento()
    codcarreira = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1035_evttabcarreira) + ' - ' + unicode(self.codcarreira) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1035_exclusao_custom#
    #s1035_exclusao_custom#
    class Meta:
        db_table = r's1035_exclusao'
        managed = True
        ordering = ['s1035_evttabcarreira', 'codcarreira', 'inivalid', 'fimvalid']


class s1035inclusao(models.Model):
    s1035_evttabcarreira = models.OneToOneField('esocial.s1035evtTabCarreira',
        related_name='%(class)s_s1035_evttabcarreira')
    def evento(self): return self.s1035_evttabcarreira.evento()
    codcarreira = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dsccarreira = models.CharField(max_length=100)
    leicarr = models.CharField(max_length=12, blank=True, null=True)
    dtleicarr = models.DateField()
    sitcarr = models.IntegerField(choices=CHOICES_S1035_INCLUSAO_SITCARR)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1035_evttabcarreira) + ' - ' + unicode(self.codcarreira) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.dsccarreira) + ' - ' + unicode(self.leicarr) + ' - ' + unicode(self.dtleicarr) + ' - ' + unicode(self.sitcarr)
    #s1035_inclusao_custom#
    #s1035_inclusao_custom#
    class Meta:
        db_table = r's1035_inclusao'
        managed = True
        ordering = ['s1035_evttabcarreira', 'codcarreira', 'inivalid', 'fimvalid', 'dsccarreira', 'leicarr', 'dtleicarr', 'sitcarr']


#VIEWS_MODELS