#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



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

CHOICES_S2220_INDRESULT = (
    (1, u'1 - Normal'),
    (2, u'2 - Alterado'),
    (3, u'3 - Estável'),
    (4, u'4 - Agravamento'),
)

CHOICES_S2220_INTERPREXM = (
    (1, u'1 - EE'),
    (2, u'2 - SC'),
    (3, u'3 - SC+'),
)

CHOICES_S2220_ORDEXAME = (
    (1, u'1 - Referencial'),
    (2, u'2 - Sequencial'),
)

class s2220exame(models.Model):
    s2220_evtmonit = models.ForeignKey('esocial.s2220evtMonit',
        related_name='%(class)s_s2220_evtmonit')
    def evento(self): return self.s2220_evtmonit.evento()
    dtexm = models.DateField()
    procrealizado = models.IntegerField(blank=True, null=True)
    obsproc = models.CharField(max_length=200, blank=True, null=True)
    interprexm = models.IntegerField(choices=CHOICES_S2220_INTERPREXM)
    ordexame = models.IntegerField(choices=CHOICES_S2220_ORDEXAME)
    dtinimonit = models.DateField()
    dtfimmonit = models.DateField(blank=True, null=True)
    indresult = models.IntegerField(choices=CHOICES_S2220_INDRESULT, blank=True, null=True)
    nisresp = models.CharField(max_length=11)
    nrconsclasse = models.CharField(max_length=8)
    ufconsclasse = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2220_evtmonit) + ' - ' + unicode(self.dtexm) + ' - ' + unicode(self.procrealizado) + ' - ' + unicode(self.obsproc) + ' - ' + unicode(self.interprexm) + ' - ' + unicode(self.ordexame) + ' - ' + unicode(self.dtinimonit) + ' - ' + unicode(self.dtfimmonit) + ' - ' + unicode(self.indresult) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nrconsclasse) + ' - ' + unicode(self.ufconsclasse)
    #s2220_exame_custom#
    #s2220_exame_custom#
    class Meta:
        db_table = r's2220_exame'
        managed = True
        ordering = ['s2220_evtmonit', 'dtexm', 'procrealizado', 'obsproc', 'interprexm', 'ordexame', 'dtinimonit', 'dtfimmonit', 'indresult', 'nisresp', 'nrconsclasse', 'ufconsclasse']


#VIEWS_MODELS