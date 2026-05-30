---
tags: [trabalho, air, api, documentacao, comercial-api, migrations]
gerado_em: 2026-05-29 21:07:41
---
# Migrations

Historico Flyway em `src/main/resources/db/migration`.

| Versao | Descricao | Operacoes | Tabelas citadas | Arquivo |
|---|---|---|---|---|
| `V01_001` | criar tmp desconto agendado | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V01_001__criar_tmp_desconto_agendado.sql` |
| `V01_002` | criar tmp cobranca pontual | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V01_002__criar_tmp_cobranca_pontual.sql` |
| `V02_001` | criar tbl endereco cidade | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_001__criar_tbl_endereco_cidade.sql` |
| `V02_002` | criar tbl endereco cidade unidade | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_002__criar_tbl_endereco_cidade_unidade.sql` |
| `V02_003` | criar tbl endereco bairro | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_003__criar_tbl_endereco_bairro.sql` |
| `V02_004` | criar tbl endereco logradouro | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_004__criar_tbl_endereco_logradouro.sql` |
| `V02_005` | criar tbl vencimento | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_005__criar_tbl_vencimento.sql` |
| `V02_006` | criar tbl regra suspensao | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_006__criar_tbl_regra_suspensao.sql` |
| `V02_007` | criar tbl regra suspensao unidade | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_007__criar_tbl_regra_suspensao_unidade.sql` |
| `V02_008` | criar tbl termo | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_008__criar_tbl_termo.sql` |
| `V02_009` | criar tbl termo servico | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_009__criar_tbl_termo_servico.sql` |
| `V02_010` | criar tbl vendedor | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_010__criar_tbl_vendedor.sql` |
| `V02_011` | criar tbl carteira | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_011__criar_tbl_carteira.sql` |
| `V02_012` | criar tbl campanha | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_012__criar_tbl_campanha.sql` |
| `V02_013` | criar tbl campanha equipe | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_013__criar_tbl_campanha_equipe.sql` |
| `V02_014` | criar tbl campanha unidade | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_014__criar_tbl_campanha_unidade.sql` |
| `V02_015` | criar tbl campanha pacote | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_015__criar_tbl_campanha_pacote.sql` |
| `V02_016` | criar tbl campanha pacote adicional | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V02_016__criar_tbl_campanha_pacote_adicional.sql` |
| `V03_001` | criar tbl cliente | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_001__criar_tbl_cliente.sql` |
| `V03_002` | criar tbl cliente fisico | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_002__criar_tbl_cliente_fisico.sql` |
| `V03_003` | criar tbl cliente juridico | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_003__criar_tbl_cliente_juridico.sql` |
| `V03_004` | criar tbl lead | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_004__criar_tbl_lead.sql` |
| `V03_005` | criar tbl lead obs | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_005__criar_tbl_lead_obs.sql` |
| `V03_006` | criar tbl cliente contato | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_006__criar_tbl_cliente_contato.sql` |
| `V03_007` | criar tbl cliente anexo | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_007__criar_tbl_cliente_anexo.sql` |
| `V03_008` | criar tbl endereco | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_008__criar_tbl_endereco.sql` |
| `V03_009` | criar tbl contrato | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_009__criar_tbl_contrato.sql` |
| `V03_010` | criar tbl contrato entrega | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_010__criar_tbl_contrato_entrega.sql` |
| `V03_011` | criar tbl analise credito | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_011__criar_tbl_analise_credito.sql` |
| `V03_012` | criar tbl analise credito atributo | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_012__criar_tbl_analise_credito_atributo.sql` |
| `V03_013` | criar tbl analise credito restricao | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_013__criar_tbl_analise_credito_restricao.sql` |
| `V03_014` | criar tbl venda | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_014__criar_tbl_venda.sql` |
| `V03_015` | criar tbl venda adicional | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_015__criar_tbl_venda_adicional.sql` |
| `V03_016` | criar tbl contrato produto | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_016__criar_tbl_contrato_produto.sql` |
| `V03_017` | criar tbl contrato item | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_017__criar_tbl_contrato_item.sql` |
| `V03_018` | criar tbl venda fase | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_018__criar_tbl_venda_fase.sql` |
| `V03_019` | criar tbl contrato campanha | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_019__criar_tbl_contrato_campanha.sql` |
| `V03_020` | criar tbl contrato suspensao | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_020__criar_tbl_contrato_suspensao.sql` |
| `V03_021` | criar tbl contrato migracao | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_021__criar_tbl_contrato_migracao.sql` |
| `V03_022` | criar tbl contrato reajuste | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_022__criar_tbl_contrato_reajuste.sql` |
| `V03_023` | criar tmp contrato sap | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_023__criar_tmp_contrato_sap.sql` |
| `V03_024` | criar tbl cliente evento | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_024__criar_tbl_cliente_evento.sql` |
| `V03_025` | criar tbl contrato retencao | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_025__criar_tbl_contrato_retencao.sql` |
| `V03_026` | criar tbl contrato retencao contato | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_026__criar_tbl_contrato_retencao_contato.sql` |
| `V03_027` | criar tmp tbl app venda | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V03_027__criar_tmp_tbl_app_venda.sql` |
| `V03_028` | criar tmp tbl app upgrade | CREATE:3 | IF | `comercial-api/src/main/resources/db/migration/V03_028__criar_tmp_tbl_app_upgrade.sql` |
| `V03_029` | criar tmp tbl app adicional | CREATE:3 | IF | `comercial-api/src/main/resources/db/migration/V03_029__criar_tmp_tbl_app_adicional.sql` |
| `V04_001` | alterar tbl endereco | ALTER:6, CREATE:1 | tbl_endereco | `comercial-api/src/main/resources/db/migration/V04_001__alterar_tbl_endereco.sql` |
| `V04_002` | alterar tbl campanha pacote | ALTER:3 | tbl_campanha_pacote | `comercial-api/src/main/resources/db/migration/V04_002__alterar_tbl_campanha_pacote.sql` |
| `V04_003` | alterar tbl venda | ALTER:3 | tbl_venda | `comercial-api/src/main/resources/db/migration/V04_003__alterar_tbl_venda.sql` |
| `V04_004` | alterar tbl contrato campanha | ALTER:15, CREATE:1 | tbl_contrato_campanha | `comercial-api/src/main/resources/db/migration/V04_004__alterar_tbl_contrato_campanha.sql` |
| `V04_005` | alterar tbl contrato item | ALTER:3 | tbl_contrato_item | `comercial-api/src/main/resources/db/migration/V04_005__alterar_tbl_contrato_item.sql` |
| `V04_006` | alterar tbl campanha | ALTER:1 | tbl_campanha | `comercial-api/src/main/resources/db/migration/V04_006__alterar_tbl_campanha.sql` |
| `V04_007` | alterar tbl contrato campanha | ALTER:1 | tbl_contrato_campanha | `comercial-api/src/main/resources/db/migration/V04_007__alterar_tbl_contrato_campanha.sql` |
| `V04_008` | criar tmp tbl faturas gi | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V04_008__criar_tmp_tbl_faturas_gi.sql` |
| `V04_009` | alterar tbl endereco | ALTER:4 | tbl_endereco | `comercial-api/src/main/resources/db/migration/V04_009__alterar_tbl_endereco.sql` |
| `V05_001` | criar tbl contrato faturamento | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V05_001__criar_tbl_contrato_faturamento.sql` |
| `V05_002` | alterar tbl contrato faturamento | ALTER:1 | tbl_contrato_faturamento | `comercial-api/src/main/resources/db/migration/V05_002__alterar_tbl_contrato_faturamento.sql` |
| `V06_001` | alterar tbl cliente | ALTER:1 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V06_001__alterar_tbl_cliente.sql` |
| `V06_002` | alterar tbl contrato faturamento | ALTER:3, DROP:2 | tbl_contrato_faturamento | `comercial-api/src/main/resources/db/migration/V06_002__alterar_tbl_contrato_faturamento.sql` |
| `V06_003` | alterar tbl contrato faturamento | ALTER:2 | tbl_contrato_faturamento | `comercial-api/src/main/resources/db/migration/V06_003__alterar_tbl_contrato_faturamento.sql` |
| `V06_004` | alterar tbl contrato faturamento | ALTER:1 | tbl_contrato_faturamento | `comercial-api/src/main/resources/db/migration/V06_004__alterar_tbl_contrato_faturamento.sql` |
| `V06_005` | alterar tbl contrato reajuste | ALTER:1 | tbl_contrato_reajuste | `comercial-api/src/main/resources/db/migration/V06_005__alterar_tbl_contrato_reajuste.sql` |
| `V07_001` | alterar tbl venda | ALTER:1 | tbl_venda | `comercial-api/src/main/resources/db/migration/V07_001__alterar_tbl_venda.sql` |
| `V07_002` | alterar tbl venda | ALTER:2 | tbl_venda | `comercial-api/src/main/resources/db/migration/V07_002__alterar_tbl_venda.sql` |
| `V07_003` | alterar tmp contrato sap | CREATE:1 |  | `comercial-api/src/main/resources/db/migration/V07_003__alterar_tmp_contrato_sap.sql` |
| `V07_005` | adicionar campo reprovada tbl contrato migracao | ALTER:1 | tbl_contrato_migracao | `comercial-api/src/main/resources/db/migration/V07_005__adicionar_campo_reprovada_tbl_contrato_migracao.sql` |
| `V07_006` | alterar tbl cliente | ALTER:1 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V07_006__alterar_tbl_cliente.sql` |
| `V07_007` | criar tbl aviso migracao | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V07_007__criar_tbl_aviso_migracao.sql` |
| `V08_001` | alterar tbl lead | ALTER:1 | tbl_lead | `comercial-api/src/main/resources/db/migration/V08_001__alterar_tbl_lead.sql` |
| `V08_002` | criar tbl condominio | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V08_002__criar_tbl_condominio.sql` |
| `V08_003` | adicionar campo marcador tbl contrato | ALTER:1 | tbl_contrato | `comercial-api/src/main/resources/db/migration/V08_003__adicionar_campo_marcador_tbl_contrato.sql` |
| `V08_004` | criar tbl condominio evento | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V08_004__criar_tbl_condominio_evento.sql` |
| `V08_005` | alterar tbl lead | ALTER:4, CREATE:1 | tbl_lead | `comercial-api/src/main/resources/db/migration/V08_005__alterar_tbl_lead.sql` |
| `V08_006` | alterar tbl condominio | ALTER:1 | tbl_condominio | `comercial-api/src/main/resources/db/migration/V08_006__alterar_tbl_condominio.sql` |
| `V09_001` | criar tbl blacklist | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V09_001__criar_tbl_blacklist.sql` |
| `V09_002` | criar tbl blacklist evento | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V09_002__criar_tbl_blacklist_evento.sql` |
| `V09_003` | alterar tbl campanha | ALTER:3 | tbl_campanha | `comercial-api/src/main/resources/db/migration/V09_003__alterar_tbl_campanha.sql` |
| `V09_004` | alterar tbl contrato | ALTER:1 | tbl_contrato | `comercial-api/src/main/resources/db/migration/V09_004__alterar_tbl_contrato.sql` |
| `V09_005` | alterar tbl condominio | ALTER:1 | tbl_condominio | `comercial-api/src/main/resources/db/migration/V09_005__alterar_tbl_condominio.sql` |
| `V09_006` | criar tbl renegociacao | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V09_006__criar_tbl_renegociacao.sql` |
| `V09_007` | criar tbl renegociacao titulo | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V09_007__criar_tbl_renegociacao_titulo.sql` |
| `V09_008` | adicionar campo tbl contrato retencao | ALTER:1 | tbl_contrato_retencao | `comercial-api/src/main/resources/db/migration/V09_008__adicionar_campo_tbl_contrato_retencao.sql` |
| `V09_009` | criar tbl enventos site | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V09_009__criar_tbl_enventos_site.sql` |
| `V09_010` | alterar tbl cliente contato | ALTER:1 | tbl_cliente_contato | `comercial-api/src/main/resources/db/migration/V09_010__alterar_tbl_cliente_contato.sql` |
| `V10_001` | alterar tbl contrato add campos integracao | ALTER:4 | tbl_contrato | `comercial-api/src/main/resources/db/migration/V10_001__alterar_tbl_contrato_add_campos_integracao.sql` |
| `V10_002` | alterar tbl cliente add campos integracao sydle | ALTER:4 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V10_002__alterar_tbl_cliente_add_campos_integracao_sydle.sql` |
| `V10_003` | alterar tmp cobranca pontual add campos integracao sydle | ALTER:4 | tmp_cobranca_pontual | `comercial-api/src/main/resources/db/migration/V10_003__alterar_tmp_cobranca_pontual_add_campos_integracao_sydle.sql` |
| `V10_004` | alterar tmp desconto agendado add campos integracao sydle | ALTER:5 | tmp_desconto_agendado | `comercial-api/src/main/resources/db/migration/V10_004__alterar_tmp_desconto_agendado_add_campos_integracao_sydle.sql` |
| `V11_001` | alterar tbl eventos site | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V11_001__alterar_tbl_eventos_site.sql` |
| `V11_002` | alterar tbl cliente contato | ALTER:2 | air_comercial | `comercial-api/src/main/resources/db/migration/V11_002__alterar_tbl_cliente_contato.sql` |
| `V12_001` | alterar tbl contrato item add campos regra desconto | ALTER:1 | tbl_contrato_item | `comercial-api/src/main/resources/db/migration/V12_001__alterar_tbl_contrato_item_add_campos_regra_desconto.sql` |
| `V12_002` | criar tmp evento financeiro sydle | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V12_002__criar_tmp_evento_financeiro_sydle.sql` |
| `V13_001` | alterar tbl enventos site nome para tbl eventos site |  | air_comercial | `comercial-api/src/main/resources/db/migration/V13_001__alterar_tbl_enventos_site_nome_para_tbl_eventos_site.sql` |
| `V13_002` | alterar tbl lead adicionar campos email status e email adicional status | ALTER:2 | air_comercial | `comercial-api/src/main/resources/db/migration/V13_002__alterar_tbl_lead_adicionar_campos_email_status_e_email_adicional_status.sql` |
| `V14_001` | alterar tmp desconto agendado adcionar campo ajuste preco | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V14_001__alterar_tmp_desconto_agendado_adcionar_campo_ajuste_preco.sql` |
| `V15_001` | alterar tmp evento financeiro sydle adcionar campos item codigo item nome | ALTER:2 | tmp_evento_financeiro_sydle | `comercial-api/src/main/resources/db/migration/V15_001__alterar_tmp_evento_financeiro_sydle_adcionar_campos_item_codigo_item_nome.sql` |
| `V16_001` | alterar tbl endereco add campos certificado | ALTER:2 | tbl_endereco | `comercial-api/src/main/resources/db/migration/V16_001__alterar_tbl_endereco_add_campos_certificado.sql` |
| `V16_002` | alterar tbl lead add campos certificado | ALTER:2 | tbl_lead | `comercial-api/src/main/resources/db/migration/V16_002__alterar_tbl_lead_add_campos_certificado.sql` |
| `V16_003` | alterar tbl lead add campo end completo | ALTER:1 | tbl_lead | `comercial-api/src/main/resources/db/migration/V16_003__alterar_tbl_lead_add_campo_end_completo.sql` |
| `V16_004` | alterar tbl endereco add campo end completo | ALTER:1 | tbl_endereco | `comercial-api/src/main/resources/db/migration/V16_004__alterar_tbl_endereco_add_campo_end_completo.sql` |
| `V16_005` | alterar tbl condominio | ALTER:30 | air_comercial | `comercial-api/src/main/resources/db/migration/V16_005__alterar_tbl_condominio.sql` |
| `V16_006` | alterar tbl condominio evento | ALTER:2 | air_comercial | `comercial-api/src/main/resources/db/migration/V16_006__alterar_tbl_condominio_evento.sql` |
| `V17_001` | criar tbl contrato forma pagamento | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V17_001__criar_tbl_contrato_forma_pagamento.sql` |
| `V18_001` | criar tbl contrato termo central assinante | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V18_001__criar_tbl_contrato_termo_central_assinante.sql` |
| `V18_002` | alterar tbl analise credito campos validacao | ALTER:4 | tbl_analise_credito | `comercial-api/src/main/resources/db/migration/V18_002__alterar_tbl_analise_credito_campos_validacao.sql` |
| `V18_003` | criar tbl contrato hero | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V18_003__criar_tbl_contrato_hero.sql` |
| `V19_001` | alterar tbl condominio | ALTER:8 | air_comercial | `comercial-api/src/main/resources/db/migration/V19_001__alterar_tbl_condominio.sql` |
| `V20_001` | criar tbl cnpj empresas | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V20_001__criar_tbl_cnpj_empresas.sql` |
| `V20_002` | criar tbl cnpj socios | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V20_002__criar_tbl_cnpj_socios.sql` |
| `V20_003` | criar tbl cnpj cnaes secundarios | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V20_003__criar_tbl_cnpj_cnaes_secundarios.sql` |
| `V21_001` | alterar tbl campanha add pme | ALTER:1 | tbl_campanha | `comercial-api/src/main/resources/db/migration/V21_001__alterar_tbl_campanha_add_pme.sql` |
| `V21_002` | alterar tbl contrato add pme | ALTER:1 | tbl_contrato | `comercial-api/src/main/resources/db/migration/V21_002__alterar_tbl_contrato_add_pme.sql` |
| `V21_003` | alterar tbl campanha pacote add  agendamento instalacao obrigatorio | ALTER:1 | tbl_campanha_pacote | `comercial-api/src/main/resources/db/migration/V21_003__alterar_tbl_campanha_pacote_add__agendamento_instalacao_obrigatorio.sql` |
| `V21_004` | alterar tbl cliente add id suporte sumicity virtual | ALTER:1 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V21_004__alterar_tbl_cliente_add_id_suporte_sumicity_virtual.sql` |
| `V21_005` | alterar tbl cliente add id suporte sumicity virtual dois | ALTER:2 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V21_005__alterar_tbl_cliente_add_id_suporte_sumicity_virtual_dois.sql` |
| `V22_001` | alterar tbl endereco add id condominio and ftta | ALTER:2 | tbl_endereco | `comercial-api/src/main/resources/db/migration/V22_001__alterar_tbl_endereco_add_id_condominio_and_ftta.sql` |
| `V23_001` | alterar tbl lead add uuid lead rd station | ALTER:1 | tbl_lead | `comercial-api/src/main/resources/db/migration/V23_001__alterar_tbl_lead_add_uuid_lead_rd_station.sql` |
| `V24_001` | alterar tbl cliente add id oauth | ALTER:1 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V24_001__alterar_tbl_cliente_add_id_oauth.sql` |
| `V25_001` | criar tbl habilitar confianca | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V25_001__criar_tbl_habilitar_confianca.sql` |
| `V25_002` | criar tbl auditoria habilitar confianca | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V25_002__criar_tbl_auditoria_habilitar_confianca.sql` |
| `V26_001` | criar tbl desconto | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V26_001__criar_tbl_desconto.sql` |
| `V27_001` | alterar tbl analise credito add columns serasa | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V27_001__alterar_tbl_analise_credito_add_columns_serasa.sql` |
| `V28_001` | criar tbl perfilacao cobranca | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V28_001__criar_tbl_perfilacao_cobranca.sql` |
| `V29_001` | alterar tbl perfilacao cobranca | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V29_001__alterar_tbl_perfilacao_cobranca.sql` |
| `V30_001` | alterar tbl analise credito add column aprovado spc | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V30_001__alterar_tbl_analise_credito_add_column_aprovado_spc.sql` |
| `V31_001` | alterar tbl perfilacao cobranca add columns log | ALTER:5 | air_comercial | `comercial-api/src/main/resources/db/migration/V31_001__alterar_tbl_perfilacao_cobranca_add_columns_log.sql` |
| `V32_001` | alterar tbl campanha pacote add taxa instalacao antecipada | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V32_001__alterar_tbl_campanha_pacote_add_taxa_instalacao_antecipada.sql` |
| `V32_002` | alterar tbl venda add possui taxa instalacao antecipada | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V32_002__alterar_tbl_venda_add_possui_taxa_instalacao_antecipada.sql` |
| `V32_003` | alterar tbl aviso migracao add migracao compulsoria | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V32_003__alterar_tbl_aviso_migracao_add_migracao_compulsoria.sql` |
| `V33_001` | criar tbl contrato historico reserva | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V33_001__criar_tbl_contrato_historico_reserva.sql` |
| `V33_002` | criar tbl perfilacao retencao | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V33_002__criar_tbl_perfilacao_retencao.sql` |
| `V34_001` | criar tbl classificar risco | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V34_001__criar_tbl_classificar_risco.sql` |
| `V35_001` | alterar tbl cliente contato | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V35_001__alterar_tbl_cliente_contato.sql` |
| `V36_001` | alterar tbl venda add informacoes bancarias | ALTER:2 | air_comercial | `comercial-api/src/main/resources/db/migration/V36_001__alterar_tbl_venda_add_informacoes_bancarias.sql` |
| `V36_002` | alterar tbl contrato produto | ALTER:2 | tbl_contrato_produto | `comercial-api/src/main/resources/db/migration/V36_002__alterar_tbl_contrato_produto.sql` |
| `V36_003` | alterar tbl venda add id processo venda sydle | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V36_003__alterar_tbl_venda_add_id_processo_venda_sydle.sql` |
| `V36_004` | alterar tbl contrato item | ALTER:2 | tbl_contrato_item | `comercial-api/src/main/resources/db/migration/V36_004__alterar_tbl_contrato_item.sql` |
| `V36_005` | alterar tbl venda modify limite pacote base | ALTER:4 | tbl_venda | `comercial-api/src/main/resources/db/migration/V36_005__alterar_tbl_venda_modify_limite_pacote_base.sql` |
| `V36_006` | alterar tbl campanha pacote modify limite pacote base | ALTER:2 | tbl_campanha_pacote | `comercial-api/src/main/resources/db/migration/V36_006__alterar_tbl_campanha_pacote_modify_limite_pacote_base.sql` |
| `V36_007` | alterar tbl vendedor add id sydle | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V36_007__alterar_tbl_vendedor_add_id_sydle.sql` |
| `V37_001` | criar tbl bloqueio generico | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V37_001__criar_tbl_bloqueio_generico.sql` |
| `V37_002` | criar tbl historico viabilidades venda | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V37_002__criar_tbl_historico_viabilidades_venda.sql` |
| `V37_003` | alterar tbl contrato add reserva connectmaster cancelada | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V37_003__alterar_tbl_contrato_add_reserva_connectmaster_cancelada.sql` |
| `V38_001` | criar tbl cliente routethis | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V38_001__criar_tbl_cliente_routethis.sql` |
| `V39_001` | alterar tbl contrato migracao | ALTER:2 | tbl_contrato_migracao | `comercial-api/src/main/resources/db/migration/V39_001__alterar_tbl_contrato_migracao.sql` |
| `V40_001` | alterar tbl contrato add column telefone | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V40_001__alterar_tbl_contrato_add_column_telefone.sql` |
| `V40_002` | alterar tbl contato add column canal confirmacao | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V40_002__alterar_tbl_contato_add_column_canal_confirmacao.sql` |
| `V41_001` | criar tbl perfilacao comercial | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V41_001__criar_tbl_perfilacao_comercial.sql` |
| `V42_001` | criar tbl historico vencimento | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V42_001__criar_tbl_historico_vencimento.sql` |
| `V42_002` | criar tbl mensagem central | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V42_002__criar_tbl_mensagem_central.sql` |
| `V42_003` | criar tbl mensagem usuario central | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V42_003__criar_tbl_mensagem_usuario_central.sql` |
| `V43_001` | alterar tbl endereco add column maps resposta | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V43_001__alterar_tbl_endereco_add_column_maps_resposta.sql` |
| `V43_002` | alterar tbl endereco add column maps status | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V43_002__alterar_tbl_endereco_add_column_maps_status.sql` |
| `V44_001` | alterar tbl perfilacao retencao add column tipo cliente | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V44_001__alterar_tbl_perfilacao_retencao_add_column_tipo_cliente.sql` |
| `V45_001` | alterar tbl cliente add id oauth giga mais | ALTER:1 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V45_001__alterar_tbl_cliente_add_id_oauth_giga_mais.sql` |
| `V46_001` | alterar tbl mensagem central add marca | ALTER:1 | tbl_mensagem_central | `comercial-api/src/main/resources/db/migration/V46_001__alterar_tbl_mensagem_central_add_marca.sql` |
| `V46_002` | alterar tbl cliente contato | ALTER:3 | air_comercial | `comercial-api/src/main/resources/db/migration/V46_002__alterar_tbl_cliente_contato.sql` |
| `V46_003` | criar tbl audit contato | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V46_003__criar_tbl_audit_contato.sql` |
| `V47_001` | criar tbl tmp item sap | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V47_001__criar_tbl_tmp_item_sap.sql` |
| `V47_002` | criar tbl tmp produto sap | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V47_002__criar_tbl_tmp_produto_sap.sql` |
| `V48_001` | criar tbl perfilacao motivo | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V48_001__criar_tbl_perfilacao_motivo.sql` |
| `V48_002` | criar tbl perfilacao submotivo | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V48_002__criar_tbl_perfilacao_submotivo.sql` |
| `V48_003` | alterar tbl perfilacao cobranca add column id chamado id motivo negociacao | ALTER:3 | tbl_perfilacao_cobranca | `comercial-api/src/main/resources/db/migration/V48_003__alterar_tbl_perfilacao_cobranca_add_column_id_chamado_id_motivo_negociacao.sql` |
| `V48_004` | criar tbl perfilacao ouvidoria | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V48_004__criar_tbl_perfilacao_ouvidoria.sql` |
| `V49_001` | criar tbl contrato suspensao tarefa | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V49_001__criar_tbl_contrato_suspensao_tarefa.sql` |
| `V50_001` | criar tbl outros marcadores | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V50_001__criar_tbl_outros_marcadores.sql` |
| `V50_002` | alterar tbl cliente add id oauth click | ALTER:1 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V50_002__alterar_tbl_cliente_add_id_oauth_click.sql` |
| `V51_001` | alterar tbl cliente add cupom | ALTER:1 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V51_001__alterar_tbl_cliente_add_cupom.sql` |
| `V51_002` | alterar tbl venda add valor ilustrativo b2b | ALTER:1 | tbl_venda | `comercial-api/src/main/resources/db/migration/V51_002__alterar_tbl_venda_add_valor_ilustrativo_b2b.sql` |
| `V52_001` | alterar tbl cliente add id oauth univox | ALTER:1 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V52_001__alterar_tbl_cliente_add_id_oauth_univox.sql` |
| `V53_001` | alterar tbl cliente add id oauth ligue | ALTER:1 | tbl_cliente | `comercial-api/src/main/resources/db/migration/V53_001__alterar_tbl_cliente_add_id_oauth_ligue.sql` |
| `V54_001` | alterar tbl campanha alter nome | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V54_001__alterar_tbl_campanha_alter_nome.sql` |
| `V54_002` | alterar tbl contrato aviso | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V54_002__alterar_tbl_contrato_aviso.sql` |
| `V55_001` | criar tbl orientacao clientes | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V55_001__criar_tbl_orientacao_clientes.sql` |
| `V56_001` | criar tbl endereco estado | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V56_001__criar_tbl_endereco_estado.sql` |
| `V57_001` | alterar tbl aviso migracao add column reajuste | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V57_001__alterar_tbl_aviso_migracao_add_column_reajuste.sql` |
| `V58_001` | alterar tbl outros marcadores add unique index marcador | ALTER:1 | tbl_outros_marcadores | `comercial-api/src/main/resources/db/migration/V58_001__alterar_tbl_outros_marcadores_add_unique_index_marcador.sql` |
| `V59_001` | criar tbl marcador contrato | CREATE:1 | IF | `comercial-api/src/main/resources/db/migration/V59_001__criar_tbl_marcador_contrato.sql` |
| `V59_002` | alterar tbl marcador contrato add unique index marcador | ALTER:1 | tbl_marcador_contrato | `comercial-api/src/main/resources/db/migration/V59_002__alterar_tbl_marcador_contrato_add_unique_index_marcador.sql` |
| `V59_003` | alterar tbl marcador contrato add unique id contrato | ALTER:1 | tbl_marcador_contrato | `comercial-api/src/main/resources/db/migration/V59_003__alterar_tbl_marcador_contrato_add_unique_id_contrato.sql` |
| `V60_001` | alterar tbl contrato retencao add column origem contato | ALTER:1 | tbl_contrato_retencao | `comercial-api/src/main/resources/db/migration/V60_001__alterar_tbl_contrato_retencao_add_column_origem_contato.sql` |
| `V60_002` | alterar tbl perfilacao retencao add column origem contato | ALTER:1 | tbl_perfilacao_retencao | `comercial-api/src/main/resources/db/migration/V60_002__alterar_tbl_perfilacao_retencao_add_column_origem_contato.sql` |
| `V61_001` | alterar tbl outros marcadores add column data validade | ALTER:1 | tbl_marcador_contrato | `comercial-api/src/main/resources/db/migration/V61_001__alterar_tbl_outros_marcadores_add_column_data_validade.sql` |
| `V61_002` | alterar tbl marcador contrato add column data validade | ALTER:1 | tbl_outros_marcadores | `comercial-api/src/main/resources/db/migration/V61_002__alterar_tbl_marcador_contrato_add_column_data_validade.sql` |
| `V62_001` | alterar tbl contrato add column status consolidado | ALTER:1 | tbl_contrato | `comercial-api/src/main/resources/db/migration/V62_001__alterar_tbl_contrato_add_column_status_consolidado.sql` |
| `V63_001` | alterar tbl contrato add column utiliza app | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V63_001__alterar_tbl_contrato_add_column_utiliza_app.sql` |
| `V64_001` | alterar tbl contrato add column gigatv colab | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V64_001__alterar_tbl_contrato_add_column_gigatv_colab.sql` |
| `V65_001` | alterar tbl contrato add column metodo pagamento | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V65_001__alterar_tbl_contrato_add_column_metodo_pagamento.sql` |
| `V65_002` | alterar tbl cliente add column nome social | ALTER:1 | air_comercial | `comercial-api/src/main/resources/db/migration/V65_002__alterar_tbl_cliente_add_column_nome_social.sql` |
