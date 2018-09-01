# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1000', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1000alteracao',
            name='natjurid',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'1015', '1015 - \xd3rg\xe3o P\xfablico do Poder Executivo Federal'), (b'1023', '1023 - \xd3rg\xe3o P\xfablico do Poder Executivo Estadual ou do Distrito Federal'), (b'1031', '1031 - \xd3rg\xe3o P\xfablico do Poder Executivo Municipal'), (b'1040', '1040 - \xd3rg\xe3o P\xfablico do Poder Legislativo Federal'), (b'1058', '1058 - \xd3rg\xe3o P\xfablico do Poder Legislativo Estadual ou do Distrito Federal'), (b'1066', '1066 - \xd3rg\xe3o P\xfablico do Poder Legislativo Municipal'), (b'1074', '1074 - \xd3rg\xe3o P\xfablico do Poder Judici\xe1rio Federal'), (b'1082', '1082 - \xd3rg\xe3o P\xfablico do Poder Judici\xe1rio Estadual'), (b'1104', '1104 - Autarquia Federal'), (b'1112', '1112 - Autarquia Estadual ou do Distrito Federal'), (b'1120', '1120 - Autarquia Municipal'), (b'1139', '1139 - Funda\xe7\xe3o P\xfablica de Direito P\xfablico Federal'), (b'1147', '1147 - Funda\xe7\xe3o P\xfablica de Direito P\xfablico Estadual ou do Distrito Federal'), (b'1155', '1155 - Funda\xe7\xe3o P\xfablica de Direito P\xfablico Municipal'), (b'1163', '1163 - \xd3rg\xe3o P\xfablico Aut\xf4nomo Federal'), (b'1171', '1171 - \xd3rg\xe3o P\xfablico Aut\xf4nomo Estadual ou do Distrito Federal'), (b'1180', '1180 - \xd3rg\xe3o P\xfablico Aut\xf4nomo Municipal'), (b'1198', '1198 - Comiss\xe3o Polinacional'), (b'1201', '1201 - Fundo P\xfablico'), (b'1210', '1210 - Cons\xf3rcio P\xfablico de Direito P\xfablico (Associa\xe7\xe3o P\xfablica)'), (b'1228', '1228 - Cons\xf3rcio P\xfablico de Direito Privado'), (b'1236', '1236 - Estado ou Distrito Federal'), (b'1244', '1244 - Munic\xedpio'), (b'1252', '1252 - Funda\xe7\xe3o P\xfablica de Direito Privado Federal'), (b'1260', '1260 - Funda\xe7\xe3o P\xfablica de Direito Privado Estadual ou do Distrito Federal'), (b'1279', '1279 - Funda\xe7\xe3o P\xfablica de Direito Privado Municipal'), (b'2011', '2011 - Empresa P\xfablica'), (b'2038', '2038 - Sociedade de Economia Mista'), (b'2046', '2046 - Sociedade An\xf4nima Aberta'), (b'2054', '2054 - Sociedade An\xf4nima Fechada'), (b'2062', '2062 - Sociedade Empres\xe1ria Limitada'), (b'2070', '2070 - Sociedade Empres\xe1ria em Nome Coletivo'), (b'2089', '2089 - Sociedade Empres\xe1ria em Comandita Simples'), (b'2097', '2097 - Sociedade Empres\xe1ria em Comandita por A\xe7\xf5es'), (b'2127', '2127 - Sociedade em Conta de Participa\xe7\xe3o'), (b'2135', '2135 - Empres\xe1rio (Individual)'), (b'2143', '2143 - Cooperativa'), (b'2151', '2151 - Cons\xf3rcio de Sociedades'), (b'2160', '2160 - Grupo de Sociedades'), (b'2178', '2178 - Estabelecimento, no Brasil, de Sociedade Estrangeira'), (b'2194', '2194 - Estabelecimento, no Brasil, de Empresa Binacional Argentino-Brasileira'), (b'2216', '2216 - Empresa Domiciliada no Exterior'), (b'2224', '2224 - Clube/Fundo de Investimento'), (b'2232', '2232 - Sociedade Simples Pura'), (b'2240', '2240 - Sociedade Simples Limitada'), (b'2259', '2259 - Sociedade Simples em Nome Coletivo'), (b'2267', '2267 - Sociedade Simples em Comandita Simples'), (b'2275', '2275 - Empresa Binacional'), (b'2283', '2283 - Cons\xf3rcio de Empregadores'), (b'2291', '2291 - Cons\xf3rcio Simples'), (b'2305', '2305 - Empresa Individual de Responsabilidade Limitada (de Natureza Empres\xe1ria)'), (b'2313', '2313 - Empresa Individual de Responsabilidade Limitada (de Natureza Simples)'), (b'2321', '2321 - Sociedade Unipessoal de Advogados'), (b'2330', '2330 - Cooperativas de Consumo'), (b'3034', '3034 - Servi\xe7o Notarial e Registral (Cart\xf3rio)'), (b'3069', '3069 - Funda\xe7\xe3o Privada'), (b'3077', '3077 - Servi\xe7o Social Aut\xf4nomo'), (b'3085', '3085 - Condom\xednio Edil\xedcio'), (b'3107', '3107 - Comiss\xe3o de Concilia\xe7\xe3o Pr\xe9via'), (b'3115', '3115 - Entidade de Media\xe7\xe3o e Arbitragem'), (b'3131', '3131 - Entidade Sindical'), (b'3204', '3204 - Estabelecimento, no Brasil, de Funda\xe7\xe3o ou Associa\xe7\xe3o Estrangeiras'), (b'3212', '3212 - Funda\xe7\xe3o ou Associa\xe7\xe3o Domiciliada no Exterior'), (b'3220', '3220 - Organiza\xe7\xe3o Religiosa'), (b'3239', '3239 - Comunidade Ind\xedgena'), (b'3247', '3247 - Fundo Privado'), (b'3255', '3255 - \xd3rg\xe3o de Dire\xe7\xe3o Nacional de Partido Pol\xedtico'), (b'3263', '3263 - \xd3rg\xe3o de Dire\xe7\xe3o Regional de Partido Pol\xedtico'), (b'3271', '3271 - \xd3rg\xe3o de Dire\xe7\xe3o Local de Partido Pol\xedtico'), (b'3280', '3280 - Comit\xea Financeiro de Partido Pol\xedtico'), (b'3298', '3298 - Frente Plebiscit\xe1ria ou Referend\xe1ria'), (b'3306', '3306 - Organiza\xe7\xe3o Social (OS)'), (b'3310', '3310 - Demais Condom\xednios'), (b'3999', '3999 - Associa\xe7\xe3o Privada'), (b'4014', '4014 - Empresa Individual Imobili\xe1ria'), (b'4022', '4022 - Segurado Especial'), (b'4081', '4081 - Contribuinte individual'), (b'4090', '4090 - Candidato a Cargo Pol\xedtico Eletivo'), (b'4111', '4111 - Leiloeiro'), (b'4124', '4124 - Produtor Rural (Pessoa F\xedsica)'), (b'5010', '5010 - Organiza\xe7\xe3o Internacional'), (b'5029', '5029 - Representa\xe7\xe3o Diplom\xe1tica Estrangeira'), (b'5037', '5037 - Outras Institui\xe7\xf5es Extraterritoriais')]),
        ),
    ]