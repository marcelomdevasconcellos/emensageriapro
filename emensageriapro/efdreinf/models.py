#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



SIM_NAO = (
    (0, u'Não'),
    (1, u'Sim'),
)

TRANSMISSOR_STATUS = (
    (0, u'Cadastrado'),
    (1, u'Importado'),
    (10, u'Assinado'),
    (11, u'Gerado'),
    (12, u'Retorno'),
    (13, u'Erro - Ocorrências'),
    (14, u'Processado'),
    (2, u'Duplicado'),
    (3, u'Erro na validação'),
    (4, u'Validado'),
    (5, u'Erro no envio'),
    (6, u'Aguardando envio'),
    (7, u'Enviado'),
    (8, u'Erro na consulta'),
    (9, u'Consultado'),
)

OPERACOES = (
    (1, u'Incluir'),
    (2, u'Alterar'),
    (3, u'Excluir'),
)

EFDREINF_VERSOES = (
    ('v1_03_02', u'Versão 1.03.02'),
)

CHOICES_R1000_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R1000_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R1000_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R1070_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R1070_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R1070_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R2010_INDCPRB = (
    (0, u'0 - Não é contribuinte da Contribuição Previdenciária sobre a Receita Bruta (CPRB) - Retenção 11%'),
    (1, u'1 - Contribuinte da Contribuição Previdenciária sobre a Receita Bruta (CPRB) - Retenção 3,5%'),
)

CHOICES_R2010_INDOBRA = (
    (0, u'0 - Não é obra de construção civil ou não está sujeita a matrícula de obra'),
    (1, u'1 - Obra de Construção Civil - Empreitada Total'),
    (2, u'2 - Obra de Construção Civil - Empreitada Parcial'),
)

CHOICES_R2010_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_R2010_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R2010_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R2010_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R2010_TPINSCESTAB = (
    (1, u'1 - CNPJ'),
    (4, u'4 - CNO'),
)

CHOICES_R2020_INDOBRA = (
    (0, u'0 - Não é obra de construção civil ou não está sujeita a matrícula de obra'),
    (1, u'1 - Obra de Construção Civil - Empreitada Total'),
    (2, u'2 - Obra de Construção Civil - Empreitada Parcial'),
)

CHOICES_R2020_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_R2020_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R2020_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R2020_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R2020_TPINSCESTABPREST = (
    (1, u'1 - CNPJ'),
)

CHOICES_R2020_TPINSCTOMADOR = (
    (1, u'1 - CNPJ'),
    (4, u'4 - CNO'),
)

CHOICES_R2030_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_R2030_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R2030_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R2030_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R2030_TPINSCESTAB = (
    (1, u'1 - CNPJ'),
)

CHOICES_R2040_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_R2040_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R2040_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R2040_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R2040_TPINSCESTAB = (
    (1, u'1 - CNPJ'),
)

CHOICES_R2050_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_R2050_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R2050_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R2050_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R2050_TPINSCESTAB = (
    (1, u'1 - CNPJ'),
)

CHOICES_R2060_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_R2060_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R2060_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R2060_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R2060_TPINSCESTAB = (
    (1, u'1 - CNPJ'),
    (4, u'4 - CNO'),
)

CHOICES_R2070_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_R2070_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R2070_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R2070_TPINSC = (
    (1, u'1 - CNPJ'),
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (2, u'2 - CPF'),
)

CHOICES_R2070_TPINSCBENEF = (
    (1, u'1 - Pessoa Jurídica'),
    (2, u'2 - Pessoa Física'),
)

CHOICES_R2098_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R2098_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R2098_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R2099_EVTASSDESPREC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R2099_EVTASSDESPREP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R2099_EVTCOMPROD = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R2099_EVTCPRB = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R2099_EVTPGTOS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R2099_EVTSERVPR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R2099_EVTSERVTM = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R2099_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R2099_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R2099_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R3010_INDRETIF = (
    (1, u'1 - Arquivo original'),
    (2, u'2 - Arquivo de retificação'),
)

CHOICES_R3010_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R3010_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R3010_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R5001_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R5011_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R9000_PROCEMI = (
    (1, u'1 - Aplicativo do contribuinte'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_R9000_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_R9000_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

class r1000evtInfoContri(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_R1000_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R1000_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R1000_TPINSC)
    nrinsc = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #r1000_evtinfocontri_custom#
    #r1000_evtinfocontri_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r1000_evtinfocontri'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class r1070evtTabProcesso(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_R1070_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R1070_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R1070_TPINSC)
    nrinsc = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #r1070_evttabprocesso_custom#
    #r1070_evttabprocesso_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r1070_evttabprocesso'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class r2010evtServTom(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_R2010_INDRETIF)
    nrrecibo = models.CharField(max_length=52, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpamb = models.IntegerField(choices=CHOICES_R2010_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R2010_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R2010_TPINSC)
    nrinsc = models.CharField(max_length=14)
    tpinscestab = models.IntegerField(choices=CHOICES_R2010_TPINSCESTAB)
    nrinscestab = models.CharField(max_length=14)
    indobra = models.IntegerField(choices=CHOICES_R2010_INDOBRA)
    cnpjprestador = models.CharField(max_length=14)
    vlrtotalbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    indcprb = models.IntegerField(choices=CHOICES_R2010_INDCPRB)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpinscestab) + ' - ' + unicode(self.nrinscestab) + ' - ' + unicode(self.indobra) + ' - ' + unicode(self.cnpjprestador) + ' - ' + unicode(self.vlrtotalbruto) + ' - ' + unicode(self.vlrtotalbaseret) + ' - ' + unicode(self.vlrtotalretprinc) + ' - ' + unicode(self.vlrtotalretadic) + ' - ' + unicode(self.vlrtotalnretprinc) + ' - ' + unicode(self.vlrtotalnretadic) + ' - ' + unicode(self.indcprb)
    #r2010_evtservtom_custom#
    #r2010_evtservtom_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r2010_evtservtom'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab', 'indobra', 'cnpjprestador', 'vlrtotalbruto', 'vlrtotalbaseret', 'vlrtotalretprinc', 'vlrtotalretadic', 'vlrtotalnretprinc', 'vlrtotalnretadic', 'indcprb']


class r2020evtServPrest(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_R2020_INDRETIF)
    nrrecibo = models.CharField(max_length=52, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpamb = models.IntegerField(choices=CHOICES_R2020_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R2020_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R2020_TPINSC)
    nrinsc = models.CharField(max_length=14)
    tpinscestabprest = models.IntegerField(choices=CHOICES_R2020_TPINSCESTABPREST)
    nrinscestabprest = models.CharField(max_length=14)
    tpinsctomador = models.IntegerField(choices=CHOICES_R2020_TPINSCTOMADOR)
    nrinsctomador = models.CharField(max_length=14)
    indobra = models.IntegerField(choices=CHOICES_R2020_INDOBRA)
    vlrtotalbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpinscestabprest) + ' - ' + unicode(self.nrinscestabprest) + ' - ' + unicode(self.tpinsctomador) + ' - ' + unicode(self.nrinsctomador) + ' - ' + unicode(self.indobra) + ' - ' + unicode(self.vlrtotalbruto) + ' - ' + unicode(self.vlrtotalbaseret) + ' - ' + unicode(self.vlrtotalretprinc) + ' - ' + unicode(self.vlrtotalretadic) + ' - ' + unicode(self.vlrtotalnretprinc) + ' - ' + unicode(self.vlrtotalnretadic)
    #r2020_evtservprest_custom#
    #r2020_evtservprest_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r2020_evtservprest'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestabprest', 'nrinscestabprest', 'tpinsctomador', 'nrinsctomador', 'indobra', 'vlrtotalbruto', 'vlrtotalbaseret', 'vlrtotalretprinc', 'vlrtotalretadic', 'vlrtotalnretprinc', 'vlrtotalnretadic']


class r2030evtAssocDespRec(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_R2030_INDRETIF)
    nrrecibo = models.CharField(max_length=52, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpamb = models.IntegerField(choices=CHOICES_R2030_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R2030_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R2030_TPINSC)
    nrinsc = models.CharField(max_length=14)
    tpinscestab = models.IntegerField(choices=CHOICES_R2030_TPINSCESTAB)
    nrinscestab = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpinscestab) + ' - ' + unicode(self.nrinscestab)
    #r2030_evtassocdesprec_custom#
    #r2030_evtassocdesprec_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r2030_evtassocdesprec'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab']


class r2040evtAssocDespRep(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_R2040_INDRETIF)
    nrrecibo = models.CharField(max_length=52, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpamb = models.IntegerField(choices=CHOICES_R2040_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R2040_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R2040_TPINSC)
    nrinsc = models.CharField(max_length=14)
    tpinscestab = models.IntegerField(choices=CHOICES_R2040_TPINSCESTAB)
    nrinscestab = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpinscestab) + ' - ' + unicode(self.nrinscestab)
    #r2040_evtassocdesprep_custom#
    #r2040_evtassocdesprep_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r2040_evtassocdesprep'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab']


class r2050evtComProd(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_R2050_INDRETIF)
    nrrecibo = models.CharField(max_length=52, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpamb = models.IntegerField(choices=CHOICES_R2050_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R2050_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R2050_TPINSC)
    nrinsc = models.CharField(max_length=14)
    tpinscestab = models.IntegerField(choices=CHOICES_R2050_TPINSCESTAB)
    nrinscestab = models.CharField(max_length=14)
    vlrrecbrutatotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcpapur = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrratapur = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrsenarapur = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcpsusptotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrratsusptotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrsenarsusptotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpinscestab) + ' - ' + unicode(self.nrinscestab) + ' - ' + unicode(self.vlrrecbrutatotal) + ' - ' + unicode(self.vlrcpapur) + ' - ' + unicode(self.vlrratapur) + ' - ' + unicode(self.vlrsenarapur) + ' - ' + unicode(self.vlrcpsusptotal) + ' - ' + unicode(self.vlrratsusptotal) + ' - ' + unicode(self.vlrsenarsusptotal)
    #r2050_evtcomprod_custom#
    #r2050_evtcomprod_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r2050_evtcomprod'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab', 'vlrrecbrutatotal', 'vlrcpapur', 'vlrratapur', 'vlrsenarapur', 'vlrcpsusptotal', 'vlrratsusptotal', 'vlrsenarsusptotal']


class r2060evtCPRB(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_R2060_INDRETIF)
    nrrecibo = models.CharField(max_length=52, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpamb = models.IntegerField(choices=CHOICES_R2060_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R2060_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R2060_TPINSC)
    nrinsc = models.CharField(max_length=14)
    tpinscestab = models.IntegerField(choices=CHOICES_R2060_TPINSCESTAB)
    nrinscestab = models.CharField(max_length=14)
    vlrrecbrutatotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcpapurtotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcprbsusptotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpinscestab) + ' - ' + unicode(self.nrinscestab) + ' - ' + unicode(self.vlrrecbrutatotal) + ' - ' + unicode(self.vlrcpapurtotal) + ' - ' + unicode(self.vlrcprbsusptotal)
    #r2060_evtcprb_custom#
    #r2060_evtcprb_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r2060_evtcprb'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscestab', 'nrinscestab', 'vlrrecbrutatotal', 'vlrcpapurtotal', 'vlrcprbsusptotal']


class r2070evtPgtosDivs(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_R2070_INDRETIF)
    nrrecibo = models.CharField(max_length=52, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpamb = models.IntegerField(choices=CHOICES_R2070_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R2070_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R2070_TPINSC)
    nrinsc = models.CharField(max_length=14)
    codpgto = models.IntegerField()
    tpinscbenef = models.IntegerField(choices=CHOICES_R2070_TPINSCBENEF, blank=True, null=True)
    nrinscbenef = models.CharField(max_length=14, blank=True, null=True)
    nmrazaobenef = models.CharField(max_length=150)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codpgto) + ' - ' + unicode(self.tpinscbenef) + ' - ' + unicode(self.nrinscbenef) + ' - ' + unicode(self.nmrazaobenef)
    #r2070_evtpgtosdivs_custom#
    #r2070_evtpgtosdivs_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r2070_evtpgtosdivs'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'codpgto', 'tpinscbenef', 'nrinscbenef', 'nmrazaobenef']


class r2098evtReabreEvPer(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpamb = models.IntegerField(choices=CHOICES_R2098_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R2098_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R2098_TPINSC)
    nrinsc = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #r2098_evtreabreevper_custom#
    #r2098_evtreabreevper_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r2098_evtreabreevper'
        managed = True
        ordering = ['identidade', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class r2099evtFechaEvPer(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpamb = models.IntegerField(choices=CHOICES_R2099_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R2099_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R2099_TPINSC)
    nrinsc = models.CharField(max_length=14)
    evtservtm = models.CharField(choices=CHOICES_R2099_EVTSERVTM, max_length=1)
    evtservpr = models.CharField(choices=CHOICES_R2099_EVTSERVPR, max_length=1)
    evtassdesprec = models.CharField(choices=CHOICES_R2099_EVTASSDESPREC, max_length=1)
    evtassdesprep = models.CharField(choices=CHOICES_R2099_EVTASSDESPREP, max_length=1)
    evtcomprod = models.CharField(choices=CHOICES_R2099_EVTCOMPROD, max_length=1)
    evtcprb = models.CharField(choices=CHOICES_R2099_EVTCPRB, max_length=1)
    evtpgtos = models.CharField(choices=CHOICES_R2099_EVTPGTOS, max_length=1)
    compsemmovto = models.CharField(max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.evtservtm) + ' - ' + unicode(self.evtservpr) + ' - ' + unicode(self.evtassdesprec) + ' - ' + unicode(self.evtassdesprep) + ' - ' + unicode(self.evtcomprod) + ' - ' + unicode(self.evtcprb) + ' - ' + unicode(self.evtpgtos) + ' - ' + unicode(self.compsemmovto)
    #r2099_evtfechaevper_custom#
    #r2099_evtfechaevper_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r2099_evtfechaevper'
        managed = True
        ordering = ['identidade', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'evtservtm', 'evtservpr', 'evtassdesprec', 'evtassdesprep', 'evtcomprod', 'evtcprb', 'evtpgtos', 'compsemmovto']


class r3010evtEspDesportivo(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_R3010_INDRETIF)
    nrrecibo = models.CharField(max_length=52, blank=True, null=True)
    dtapuracao = models.DateField()
    tpamb = models.IntegerField(choices=CHOICES_R3010_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R3010_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R3010_TPINSC)
    nrinsc = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.dtapuracao) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #r3010_evtespdesportivo_custom#
    #r3010_evtespdesportivo_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r3010_evtespdesportivo'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'dtapuracao', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class r5001evtTotal(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpinsc = models.IntegerField(choices=CHOICES_R5001_TPINSC)
    nrinsc = models.CharField(max_length=14)
    cdretorno = models.CharField(max_length=6)
    descretorno = models.CharField(max_length=255)
    nrprotentr = models.CharField(max_length=49, blank=True, null=True)
    dhprocess = models.DateField()
    tpev = models.CharField(max_length=6)
    idev = models.CharField(max_length=36)
    hash = models.CharField(max_length=60)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cdretorno) + ' - ' + unicode(self.descretorno) + ' - ' + unicode(self.nrprotentr) + ' - ' + unicode(self.dhprocess) + ' - ' + unicode(self.tpev) + ' - ' + unicode(self.idev) + ' - ' + unicode(self.hash)
    #r5001_evttotal_custom#
    #r5001_evttotal_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r5001_evttotal'
        managed = True
        ordering = ['identidade', 'perapur', 'tpinsc', 'nrinsc', 'cdretorno', 'descretorno', 'nrprotentr', 'dhprocess', 'tpev', 'idev', 'hash']


class r5011evtTotalContrib(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    perapur = models.CharField(max_length=10)
    tpinsc = models.IntegerField(choices=CHOICES_R5011_TPINSC)
    nrinsc = models.CharField(max_length=14)
    cdretorno = models.CharField(max_length=6)
    descretorno = models.CharField(max_length=255)
    nrprotentr = models.CharField(max_length=49)
    dhprocess = models.DateField()
    tpev = models.CharField(max_length=6)
    idev = models.CharField(max_length=36)
    hash = models.CharField(max_length=60)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cdretorno) + ' - ' + unicode(self.descretorno) + ' - ' + unicode(self.nrprotentr) + ' - ' + unicode(self.dhprocess) + ' - ' + unicode(self.tpev) + ' - ' + unicode(self.idev) + ' - ' + unicode(self.hash)
    #r5011_evttotalcontrib_custom#
    #r5011_evttotalcontrib_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r5011_evttotalcontrib'
        managed = True
        ordering = ['identidade', 'perapur', 'tpinsc', 'nrinsc', 'cdretorno', 'descretorno', 'nrprotentr', 'dhprocess', 'tpev', 'idev', 'hash']


class r9000evtExclusao(models.Model):
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, default='v1_03_02')
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_R9000_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_R9000_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_R9000_TPINSC)
    nrinsc = models.CharField(max_length=14)
    tpevento = models.CharField(max_length=6)
    nrrecevt = models.CharField(max_length=52)
    perapur = models.CharField(max_length=10)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    retornos_evttotal = models.ForeignKey('r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    ocorrencias = models.TextField(blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, default=0)
    cdretorno = models.CharField(max_length=6, blank=True, null=True)
    descretorno = models.CharField(max_length=255, blank=True, null=True)
    dhprocess = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpevento) + ' - ' + unicode(self.nrrecevt) + ' - ' + unicode(self.perapur)
    #r9000_evtexclusao_custom#
    #r9000_evtexclusao_custom#
    def evento(self): return self.__dict__
    class Meta:
        db_table = r'r9000_evtexclusao'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpevento', 'nrrecevt', 'perapur']


#VIEWS_MODELS