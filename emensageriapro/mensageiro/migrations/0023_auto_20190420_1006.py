# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0022_auto_20190309_1943'),
    ]

    operations = [
        migrations.RunSQL("""
        
CREATE OR REPLACE VIEW transmissor_eventos_esocial AS
SELECT id, 's1000' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1000_evtinfoempregador' as tabela, 's1000_evtinfoempregador_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1000_evtinfoempregador_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1000_evtinfoempregador WHERE excluido=False UNION
SELECT id, 's1005' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1005_evttabestab' as tabela, 's1005_evttabestab_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1005_evttabestab_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1005_evttabestab WHERE excluido=False UNION
SELECT id, 's1010' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1010_evttabrubrica' as tabela, 's1010_evttabrubrica_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1010_evttabrubrica_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1010_evttabrubrica WHERE excluido=False UNION
SELECT id, 's1020' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1020_evttablotacao' as tabela, 's1020_evttablotacao_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1020_evttablotacao_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1020_evttablotacao WHERE excluido=False UNION
SELECT id, 's1030' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1030_evttabcargo' as tabela, 's1030_evttabcargo_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1030_evttabcargo_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1030_evttabcargo WHERE excluido=False UNION
SELECT id, 's1035' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1035_evttabcarreira' as tabela, 's1035_evttabcarreira_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1035_evttabcarreira_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1035_evttabcarreira WHERE excluido=False UNION
SELECT id, 's1040' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1040_evttabfuncao' as tabela, 's1040_evttabfuncao_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1040_evttabfuncao_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1040_evttabfuncao WHERE excluido=False UNION
SELECT id, 's1050' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1050_evttabhortur' as tabela, 's1050_evttabhortur_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1050_evttabhortur_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1050_evttabhortur WHERE excluido=False UNION
SELECT id, 's1060' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1060_evttabambiente' as tabela, 's1060_evttabambiente_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1060_evttabambiente_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1060_evttabambiente WHERE excluido=False UNION
SELECT id, 's1070' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1070_evttabprocesso' as tabela, 's1070_evttabprocesso_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1070_evttabprocesso_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1070_evttabprocesso WHERE excluido=False UNION
SELECT id, 's1080' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 1 as grupo, 's1080_evttaboperport' as tabela, 's1080_evttaboperport_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1080_evttaboperport_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1080_evttaboperport WHERE excluido=False UNION
SELECT id, 's1200' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1200_evtremun' as tabela, 's1200_evtremun_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1200_evtremun_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1200_evtremun WHERE excluido=False UNION
SELECT id, 's1202' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1202_evtrmnrpps' as tabela, 's1202_evtrmnrpps_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1202_evtrmnrpps_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1202_evtrmnrpps WHERE excluido=False UNION
SELECT id, 's1207' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1207_evtbenprrp' as tabela, 's1207_evtbenprrp_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1207_evtbenprrp_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1207_evtbenprrp WHERE excluido=False UNION
SELECT id, 's1210' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1210_evtpgtos' as tabela, 's1210_evtpgtos_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1210_evtpgtos_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1210_evtpgtos WHERE excluido=False UNION
SELECT id, 's1250' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1250_evtaqprod' as tabela, 's1250_evtaqprod_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1250_evtaqprod_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1250_evtaqprod WHERE excluido=False UNION
SELECT id, 's1260' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1260_evtcomprod' as tabela, 's1260_evtcomprod_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1260_evtcomprod_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1260_evtcomprod WHERE excluido=False UNION
SELECT id, 's1270' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1270_evtcontratavnp' as tabela, 's1270_evtcontratavnp_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1270_evtcontratavnp_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1270_evtcontratavnp WHERE excluido=False UNION
SELECT id, 's1280' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1280_evtinfocomplper' as tabela, 's1280_evtinfocomplper_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1280_evtinfocomplper_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1280_evtinfocomplper WHERE excluido=False UNION
SELECT id, 's1295' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1295_evttotconting' as tabela, 's1295_evttotconting_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1295_evttotconting_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1295_evttotconting WHERE excluido=False UNION
SELECT id, 's1298' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1298_evtreabreevper' as tabela, 's1298_evtreabreevper_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1298_evtreabreevper_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1298_evtreabreevper WHERE excluido=False UNION
SELECT id, 's1299' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1299_evtfechaevper' as tabela, 's1299_evtfechaevper_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1299_evtfechaevper_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1299_evtfechaevper WHERE excluido=False UNION
SELECT id, 's1300' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 3 as grupo, 's1300_evtcontrsindpatr' as tabela, 's1300_evtcontrsindpatr_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's1300_evtcontrsindpatr_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s1300_evtcontrsindpatr WHERE excluido=False UNION
SELECT id, 's2190' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2190_evtadmprelim' as tabela, 's2190_evtadmprelim_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2190_evtadmprelim_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2190_evtadmprelim WHERE excluido=False UNION
SELECT id, 's2200' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2200_evtadmissao' as tabela, 's2200_evtadmissao_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2200_evtadmissao_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2200_evtadmissao WHERE excluido=False UNION
SELECT id, 's2205' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2205_evtaltcadastral' as tabela, 's2205_evtaltcadastral_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2205_evtaltcadastral_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2205_evtaltcadastral WHERE excluido=False UNION
SELECT id, 's2206' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2206_evtaltcontratual' as tabela, 's2206_evtaltcontratual_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2206_evtaltcontratual_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2206_evtaltcontratual WHERE excluido=False UNION
SELECT id, 's2210' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2210_evtcat' as tabela, 's2210_evtcat_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2210_evtcat_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2210_evtcat WHERE excluido=False UNION
SELECT id, 's2220' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2220_evtmonit' as tabela, 's2220_evtmonit_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2220_evtmonit_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2220_evtmonit WHERE excluido=False UNION
SELECT id, 's2221' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2221_evttoxic' as tabela, 's2221_evttoxic_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2221_evttoxic_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2221_evttoxic WHERE excluido=False UNION
SELECT id, 's2230' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2230_evtafasttemp' as tabela, 's2230_evtafasttemp_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2230_evtafasttemp_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2230_evtafasttemp WHERE excluido=False UNION
SELECT id, 's2231' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2231_evtcessao' as tabela, 's2231_evtcessao_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2231_evtcessao_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2231_evtcessao WHERE excluido=False UNION
SELECT id, 's2240' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2240_evtexprisco' as tabela, 's2240_evtexprisco_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2240_evtexprisco_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2240_evtexprisco WHERE excluido=False UNION
SELECT id, 's2241' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2241_evtinsapo' as tabela, 's2241_evtinsapo_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2241_evtinsapo_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2241_evtinsapo WHERE excluido=False UNION
SELECT id, 's2245' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2245_evttreicap' as tabela, 's2245_evttreicap_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2245_evttreicap_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2245_evttreicap WHERE excluido=False UNION
SELECT id, 's2250' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2250_evtavprevio' as tabela, 's2250_evtavprevio_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2250_evtavprevio_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2250_evtavprevio WHERE excluido=False UNION
SELECT id, 's2260' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2260_evtconvinterm' as tabela, 's2260_evtconvinterm_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2260_evtconvinterm_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2260_evtconvinterm WHERE excluido=False UNION
SELECT id, 's2298' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2298_evtreintegr' as tabela, 's2298_evtreintegr_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2298_evtreintegr_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2298_evtreintegr WHERE excluido=False UNION
SELECT id, 's2299' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2299_evtdeslig' as tabela, 's2299_evtdeslig_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2299_evtdeslig_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2299_evtdeslig WHERE excluido=False UNION
SELECT id, 's2300' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2300_evttsvinicio' as tabela, 's2300_evttsvinicio_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2300_evttsvinicio_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2300_evttsvinicio WHERE excluido=False UNION
SELECT id, 's2306' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2306_evttsvaltcontr' as tabela, 's2306_evttsvaltcontr_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2306_evttsvaltcontr_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2306_evttsvaltcontr WHERE excluido=False UNION
SELECT id, 's2399' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2399_evttsvtermino' as tabela, 's2399_evttsvtermino_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2399_evttsvtermino_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2399_evttsvtermino WHERE excluido=False UNION
SELECT id, 's2400' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2400_evtcdbenefin' as tabela, 's2400_evtcdbenefin_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2400_evtcdbenefin_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2400_evtcdbenefin WHERE excluido=False UNION
SELECT id, 's2405' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2405_evtcdbenefalt' as tabela, 's2405_evtcdbenefalt_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2405_evtcdbenefalt_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2405_evtcdbenefalt WHERE excluido=False UNION
SELECT id, 's2410' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2410_evtcdbenin' as tabela, 's2410_evtcdbenin_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2410_evtcdbenin_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2410_evtcdbenin WHERE excluido=False UNION
SELECT id, 's2416' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2416_evtcdbenalt' as tabela, 's2416_evtcdbenalt_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2416_evtcdbenalt_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2416_evtcdbenalt WHERE excluido=False UNION
SELECT id, 's2420' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's2420_evtcdbenterm' as tabela, 's2420_evtcdbenterm_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's2420_evtcdbenterm_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s2420_evtcdbenterm WHERE excluido=False UNION
SELECT id, 's3000' as evento, identidade, transmissor_lote_esocial_id, criado_em, criado_por_id, modificado_em, modificado_por_id, excluido, 2 as grupo, 's3000_evtexclusao' as tabela, 's3000_evtexclusao_salvar' as tabela_salvar, id as ordem, tpinsc, nrinsc, 's3000_evtexclusao_recibo' as url_recibo, validacao_precedencia, validacoes, status, retornos_eventos_id, ocorrencias FROM public.s3000_evtexclusao WHERE excluido=False;
        
        
        """)
    ]
