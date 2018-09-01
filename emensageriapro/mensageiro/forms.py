# coding: utf-8
from django import forms
from emensageriapro.mensageiro.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_retornos_eventos_intervalos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_retornos_eventos_intervalos,self ).__init__(*args,**kwargs)
        self.fields['retornos_eventos_horarios'].queryset = RetornosEventosHorarios.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = RetornosEventosIntervalos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_retornos_eventos_horarios(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_retornos_eventos_horarios,self ).__init__(*args,**kwargs)
        self.fields['retornos_eventos'].queryset = RetornosEventos.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = RetornosEventosHorarios
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_retornos_eventos_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_retornos_eventos_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['retornos_eventos'].queryset = RetornosEventos.objects.using( slug ).filter(excluido=False).all()
        self.fields['retornos_eventos'].widget.attrs['required'] = True
        self.fields['retornos_eventos'].widget.attrs['readonly'] = True

    class Meta:
        model = RetornosEventosOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_retornos_eventos(forms.ModelForm):
    qtdhrssem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_retornos_eventos,self ).__init__(*args,**kwargs)
        
        self.fields['tmpparc'].widget.attrs['readonly'] = True
        
        self.fields['dsctpjorn'].widget.attrs['readonly'] = True
        
        self.fields['tpjornada'].widget.attrs['readonly'] = True
        
        self.fields['qtdhrssem'].widget.attrs['readonly'] = True
        
        self.fields['local_cnae'].widget.attrs['readonly'] = True
        
        self.fields['local_nrinsc'].widget.attrs['readonly'] = True
        
        self.fields['local_tpinsc'].widget.attrs['readonly'] = True
        
        self.fields['clauasseg'].widget.attrs['readonly'] = True
        
        self.fields['dtterm'].widget.attrs['readonly'] = True
        
        self.fields['tpcontr'].widget.attrs['readonly'] = True
        
        self.fields['dscsalvar'].widget.attrs['readonly'] = True
        
        self.fields['undsalfixo'].widget.attrs['readonly'] = True
        
        self.fields['vrsalfx'].widget.attrs['readonly'] = True
        
        self.fields['codcateg'].widget.attrs['readonly'] = True
        
        self.fields['codcbofuncao'].widget.attrs['readonly'] = True
        
        self.fields['dscfuncao'].widget.attrs['readonly'] = True
        
        self.fields['codfuncao'].widget.attrs['readonly'] = True
        
        self.fields['codcbocargo'].widget.attrs['readonly'] = True
        
        self.fields['nmcargo'].widget.attrs['readonly'] = True
        
        self.fields['codcargo'].widget.attrs['readonly'] = True
        
        self.fields['dtexercicio'].widget.attrs['readonly'] = True
        
        self.fields['dtposse'].widget.attrs['readonly'] = True
        
        self.fields['cnpjsindcategprof'].widget.attrs['readonly'] = True
        
        self.fields['dtbase'].widget.attrs['readonly'] = True
        
        self.fields['tpregjor'].widget.attrs['readonly'] = True
        
        self.fields['dtadm'].widget.attrs['readonly'] = True
        
        self.fields['matricula'].widget.attrs['readonly'] = True
        
        self.fields['infocota'].widget.attrs['readonly'] = True
        
        self.fields['nmtrab'].widget.attrs['readonly'] = True
        
        self.fields['nistrab'].widget.attrs['readonly'] = True
        
        self.fields['cpftrab'].widget.attrs['readonly'] = True
        
        self.fields['empregador_nrinsc'].widget.attrs['readonly'] = True
        
        self.fields['empregador_tpinsc'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['nrinsc'].widget.attrs['readonly'] = True
        
        self.fields['tpinsc'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['processamento_descricao_resposta'].widget.attrs['readonly'] = True
        
        self.fields['processamento_codigo_resposta'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_versao_app'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_tp_amb'].widget.attrs['readonly'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['required'] = True

    class Meta:
        model = RetornosEventos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_arquivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_arquivos,self ).__init__(*args,**kwargs)
        
        self.fields['permite_recuperacao'].widget.attrs['required'] = True
        
        self.fields['data_criacao'].widget.attrs['required'] = True
        
        self.fields['arquivo'].widget.attrs['required'] = True

    class Meta:
        model = Arquivos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_transmissor_lote_efdreinf_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_transmissor_lote_efdreinf_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['required'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        
        self.fields['resposta_codigo'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['required'] = True

    class Meta:
        model = TransmissorLoteEfdreinfOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_transmissor_lote_efdreinf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_transmissor_lote_efdreinf,self ).__init__(*args,**kwargs)
        
        self.fields['tempo_estimado_conclusao'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_aplicativo'].widget.attrs['readonly'] = True
        
        self.fields['numero_protocolo_fechamento'].widget.attrs['readonly'] = True
        
        self.fields['protocolo'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_versao_aplicativo'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['codigo_status'].widget.attrs['readonly'] = True
        self.fields['codigo_status'].widget.attrs['readonly'] = True
        
        self.fields['identidade_transmissor'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True
        
        self.fields['contribuinte_nrinsc'].widget.attrs['required'] = True
        
        self.fields['contribuinte_tpinsc'].widget.attrs['required'] = True
        self.fields['transmissor'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = TransmissorLoteEfdreinf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'retorno_descricao',
 
        ]


class form_transmissor_lote_esocial_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_transmissor_lote_esocial_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['required'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        
        self.fields['resposta_codigo'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['required'] = True

    class Meta:
        model = TransmissorLoteEsocialOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_transmissor_lote_esocial(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_transmissor_lote_esocial,self ).__init__(*args,**kwargs)
        
        self.fields['tempo_estimado_conclusao'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_aplicativo'].widget.attrs['readonly'] = True
        
        self.fields['protocolo'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_versao_aplicativo'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['resposta_codigo'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['grupo'].widget.attrs['required'] = True
        
        self.fields['empregador_nrinsc'].widget.attrs['required'] = True
        
        self.fields['empregador_tpinsc'].widget.attrs['required'] = True
        self.fields['transmissor'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = TransmissorLoteEsocial
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'resposta_descricao',
 
        ]


class form_importacao_arquivos_eventos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_importacao_arquivos_eventos,self ).__init__(*args,**kwargs)
        
        self.fields['validacoes'].widget.attrs['readonly'] = True
        
        self.fields['data_hora'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['identidade_evento'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True
        
        self.fields['evento'].widget.attrs['readonly'] = True
        
        self.fields['arquivo'].widget.attrs['readonly'] = True
        self.fields['importacao_arquivos'].queryset = ImportacaoArquivos.objects.using( slug ).filter(excluido=False).all()
        self.fields['importacao_arquivos'].widget.attrs['required'] = True
        self.fields['importacao_arquivos'].widget.attrs['readonly'] = True

    class Meta:
        model = ImportacaoArquivosEventos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_importacao_arquivos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_importacao_arquivos,self ).__init__(*args,**kwargs)
        
        self.fields['quant_erros'].widget.attrs['readonly'] = True
        
        self.fields['quant_importado'].widget.attrs['readonly'] = True
        
        self.fields['quant_aguardando'].widget.attrs['readonly'] = True
        
        self.fields['quant_total'].widget.attrs['readonly'] = True
        self.fields['importado_por'].queryset = Usuarios.objects.using( slug ).filter(excluido=False).all()
        self.fields['importado_por'].widget.attrs['readonly'] = True
        
        self.fields['data_hora'].widget.attrs['required'] = True
        self.fields['data_hora'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['arquivo'].widget.attrs['required'] = True
        self.fields['arquivo'].widget.attrs['readonly'] = True

    class Meta:
        model = ImportacaoArquivos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'quant_processado',
 
        ]


class form_regras_validacao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_regras_validacao,self ).__init__(*args,**kwargs)
        
        self.fields['validacoes'].widget.attrs['readonly'] = True
        
        self.fields['validacoes_precedencia'].widget.attrs['readonly'] = True
        
        self.fields['valores_validos'].widget.attrs['readonly'] = True
        
        self.fields['tabela'].widget.attrs['readonly'] = True
        
        self.fields['descricao'].widget.attrs['required'] = True
        self.fields['descricao'].widget.attrs['readonly'] = True
        
        self.fields['obrigatorio'].widget.attrs['required'] = True
        self.fields['obrigatorio'].widget.attrs['readonly'] = True
        
        self.fields['casas_decimais'].widget.attrs['required'] = True
        
        self.fields['tamanho'].widget.attrs['required'] = True
        
        self.fields['ocorrencias'].widget.attrs['required'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        
        self.fields['elemento'].widget.attrs['required'] = True
        
        self.fields['registro_pai'].widget.attrs['required'] = True
        
        self.fields['registro_campo'].widget.attrs['required'] = True
        
        self.fields['numero'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        
        self.fields['evento'].widget.attrs['required'] = True

    class Meta:
        model = RegrasDeValidacao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_transmissores(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_transmissores,self ).__init__(*args,**kwargs)
        
        self.fields['efdreinf_tempo_prox_envio'].widget.attrs['readonly'] = True
        
        self.fields['efdreinf_intervalo'].widget.attrs['required'] = True
        
        self.fields['efdreinf_timeout'].widget.attrs['required'] = True
        
        self.fields['efdreinf_lote_max'].widget.attrs['required'] = True
        
        self.fields['efdreinf_lote_min'].widget.attrs['required'] = True
        
        self.fields['esocial_tempo_prox_envio'].widget.attrs['readonly'] = True
        
        self.fields['esocial_intervalo'].widget.attrs['required'] = True
        
        self.fields['esocial_timeout'].widget.attrs['required'] = True
        
        self.fields['esocial_lote_max'].widget.attrs['required'] = True
        
        self.fields['esocial_lote_min'].widget.attrs['required'] = True
        
        self.fields['endereco_completo'].widget.attrs['required'] = True
        
        self.fields['envio_automatico'].widget.attrs['required'] = True
        
        self.fields['validar_eventos'].widget.attrs['required'] = True
        
        self.fields['data_abertura'].widget.attrs['required'] = True
        
        self.fields['tipo_inscricao'].widget.attrs['required'] = True
        
        self.fields['cpf_cnpj'].widget.attrs['required'] = True
        
        self.fields['nome_empresa'].widget.attrs['required'] = True

    class Meta:
        model = TransmissorLote
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'efdreinf_pasta',
            'efdreinf_senha',
            'efdreinf_certificado',
            'esocial_pasta',
            'esocial_senha',
            'esocial_certificado',
 
        ]


class form_relatorios(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_relatorios,self ).__init__(*args,**kwargs)
        
        self.fields['campos'].widget.attrs['required'] = True
        
        self.fields['titulo'].widget.attrs['required'] = True

    class Meta:
        model = Relatorios
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]
