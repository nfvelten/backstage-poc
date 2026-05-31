---
tags: [trabalho, air, api, documentacao, comercial-api, banco]
gerado_em: 2026-05-29 21:07:41
fonte: airdb-prod-main/air_comercial
---
# Banco - air_comercial

Schema introspectado de `airdb-prod-main` usando `information_schema`. A documentacao inclui metadados, nao dados de negocio.

## Tabelas

| Tabela | Tipo | Engine | Rows aprox. | Criada | Atualizada | Comentario |
|---|---|---|---:|---|---|---|
| `base_condominios_serasa` | BASE TABLE | InnoDB | 45514 | 2026-03-23 07:48:56 |  |  |
| `cnpj_cnaes_secundarios` | BASE TABLE | InnoDB | 0 | 2026-03-23 07:48:56 |  |  |
| `cnpj_empresas` | BASE TABLE | InnoDB | 41484210 | 2026-03-23 07:48:56 |  |  |
| `cnpj_socios` | BASE TABLE | InnoDB | 0 | 2026-03-23 07:48:56 |  |  |
| `contrato_produto_temp` | BASE TABLE | InnoDB | 4618 | 2026-03-23 07:48:56 |  |  |
| `contrato_ultima_reativacao` | VIEW |  | 0 |  |  | VIEW |
| `contrato_ultima_suspensao` | VIEW |  | 0 |  |  | VIEW |
| `schema_version` | BASE TABLE | InnoDB | 188 | 2026-03-23 07:48:56 |  |  |
| `stg_contratos_sydle` | BASE TABLE | InnoDB | 211118 | 2026-03-23 07:48:56 |  |  |
| `stg_faturas_sydle` | BASE TABLE | InnoDB | 586832 | 2026-03-23 07:48:56 |  |  |
| `STG_SUSPENSAO_CLIENTE` | BASE TABLE | InnoDB | 90801 | 2026-03-23 07:48:56 |  |  |
| `tbl_analise_credito` | BASE TABLE | InnoDB | 430890 | 2026-03-23 07:48:56 |  |  |
| `tbl_analise_credito_atributo` | BASE TABLE | InnoDB | 6220053 | 2026-03-23 07:48:56 |  |  |
| `tbl_analise_credito_restricao` | BASE TABLE | InnoDB | 1099938 | 2026-03-23 07:48:56 |  |  |
| `tbl_auditoria_habilitar_confianca` | BASE TABLE | InnoDB | 2873752 | 2026-03-23 07:48:56 |  |  |
| `tbl_audit_contato` | BASE TABLE | InnoDB | 2973556 | 2026-03-23 07:48:56 | 2026-05-29 21:07:40 |  |
| `tbl_aviso_migracao` | BASE TABLE | InnoDB | 3071225 | 2026-03-23 07:48:56 | 2026-05-29 20:55:45 |  |
| `tbl_blacklist` | BASE TABLE | InnoDB | 641 | 2026-03-23 07:48:56 | 2026-05-06 08:33:26 |  |
| `tbl_blacklist_evento` | BASE TABLE | InnoDB | 674 | 2026-03-23 07:48:56 | 2026-05-06 08:33:26 |  |
| `tbl_bloqueio_generico` | BASE TABLE | InnoDB | 0 | 2026-03-23 07:48:56 |  |  |
| `tbl_campanha` | BASE TABLE | InnoDB | 786 | 2026-03-23 07:48:56 |  |  |
| `tbl_campanha_equipe` | BASE TABLE | InnoDB | 8550 | 2026-03-23 07:48:56 |  |  |
| `tbl_campanha_pacote` | BASE TABLE | InnoDB | 11673 | 2026-03-23 07:48:56 | 2026-05-14 10:26:17 |  |
| `tbl_campanha_pacote_adicional` | BASE TABLE | InnoDB | 7377 | 2026-03-23 07:48:56 |  |  |
| `tbl_campanha_unidade` | BASE TABLE | InnoDB | 34647 | 2026-03-23 07:48:56 |  |  |
| `tbl_carteira` | BASE TABLE | InnoDB | 8099 | 2026-03-23 07:48:56 | 2026-05-29 17:24:54 |  |
| `tbl_classificar_risco` | BASE TABLE | InnoDB | 4253863 | 2026-03-23 07:48:56 |  |  |
| `tbl_cliente` | BASE TABLE | InnoDB | 3577535 | 2026-03-23 07:48:56 | 2026-05-29 21:07:41 |  |
| `tbl_cliente_anexo` | BASE TABLE | InnoDB | 3339148 | 2026-03-23 07:48:56 | 2026-05-29 21:07:41 |  |
| `tbl_cliente_contato` | BASE TABLE | InnoDB | 10265844 | 2026-03-23 07:48:56 | 2026-05-29 21:07:40 |  |
| `tbl_cliente_evento` | BASE TABLE | InnoDB | 48516790 | 2026-03-23 07:48:56 | 2026-05-29 21:07:40 |  |
| `tbl_cliente_fisico` | BASE TABLE | InnoDB | 3259079 | 2026-03-23 07:48:56 | 2026-05-29 21:05:48 |  |
| `tbl_cliente_juridico` | BASE TABLE | InnoDB | 69263 | 2026-03-23 07:48:56 | 2026-05-29 20:56:45 |  |
| `tbl_cliente_orientacao` | BASE TABLE | InnoDB | 0 | 2026-03-23 07:48:56 |  |  |
| `tbl_cliente_routethis` | BASE TABLE | InnoDB | 1012800 | 2026-03-23 07:48:56 |  |  |
| `tbl_condominio` | BASE TABLE | InnoDB | 1599 | 2026-03-23 07:48:56 |  |  |
| `tbl_condominio_evento` | BASE TABLE | InnoDB | 1862 | 2026-03-23 07:48:56 |  |  |
| `tbl_contrato` | BASE TABLE | InnoDB | 4060324 | 2026-03-23 07:48:56 | 2026-05-29 21:07:40 |  |
| `tbl_contrato_campanha` | BASE TABLE | InnoDB | 7185932 | 2026-03-23 07:48:56 | 2026-05-29 21:05:48 |  |
| `tbl_contrato_dia_utilizacao` | BASE TABLE | InnoDB | 15633172 | 2026-03-23 07:48:56 |  | Tabela atualizada pela procedure de atualização de contratos |
| `tbl_contrato_dia_utilizacao_2019` | BASE TABLE | InnoDB | 84165 | 2026-03-23 07:48:56 |  | Tabela atualizada pela procedure de atualização de contratos |
| `tbl_contrato_dia_utilizacao_provisao` | BASE TABLE | InnoDB | 1527676 | 2026-03-23 07:48:56 |  | Tabela atualizada pela procedure de atualização de contratos |
| `tbl_contrato_entrega` | BASE TABLE | InnoDB | 4368924 | 2026-03-23 07:48:56 | 2026-05-29 21:05:48 |  |
| `tbl_contrato_faturamento` | BASE TABLE | InnoDB | 382583 | 2026-03-23 07:48:56 |  |  |
| `tbl_contrato_forma_pagamento` | BASE TABLE | InnoDB | 21147 | 2026-03-23 07:48:56 |  |  |
| `tbl_contrato_hero` | BASE TABLE | InnoDB | 48861 | 2026-03-23 07:48:56 |  |  |
| `tbl_contrato_historico_reserva` | BASE TABLE | InnoDB | 0 | 2026-03-23 07:48:56 |  |  |
| `tbl_contrato_item` | BASE TABLE | InnoDB | 39500051 | 2026-03-23 07:48:56 | 2026-05-29 21:05:48 |  |
| `tbl_contrato_migracao` | BASE TABLE | InnoDB | 3339157 | 2026-03-23 07:48:56 | 2026-05-29 20:55:42 |  |
| `tbl_contrato_onu_aviso` | BASE TABLE | InnoDB | 2113185 | 2026-03-23 07:48:56 | 2026-05-29 21:07:41 |  |
| `tbl_contrato_produto` | BASE TABLE | InnoDB | 35648650 | 2026-03-23 07:48:56 | 2026-05-29 21:05:48 |  |
| `tbl_contrato_reajuste` | BASE TABLE | InnoDB | 1518364 | 2026-03-23 07:48:56 | 2026-05-27 03:35:57 |  |
| `tbl_contrato_retencao` | BASE TABLE | InnoDB | 1371269 | 2026-03-23 07:48:56 | 2026-05-29 15:57:19 |  |
| `tbl_contrato_retencao_contato` | BASE TABLE | InnoDB | 1046171 | 2026-03-23 07:48:56 |  |  |
| `tbl_contrato_suspensao` | BASE TABLE | InnoDB | 4022527 | 2026-03-23 07:48:56 | 2026-05-29 15:57:19 |  |
| `tbl_contrato_suspensao_blacklist` | BASE TABLE | InnoDB | 3 | 2026-03-23 07:48:56 |  |  |
| `tbl_contrato_suspensao_tarefa` | BASE TABLE | InnoDB | 790682 | 2026-03-23 07:48:56 | 2026-05-29 16:15:50 |  |
| `tbl_contrato_sydle` | BASE TABLE | InnoDB | 189054 | 2026-03-23 07:48:56 |  |  |
| `tbl_contrato_termo_central_assinante` | BASE TABLE | InnoDB | 163863 | 2026-03-23 07:48:56 |  |  |
| `tbl_desconto` | BASE TABLE | InnoDB | 6146909 | 2026-03-23 07:48:56 | 2026-05-29 20:55:50 |  |
| `tbl_endereco` | BASE TABLE | InnoDB | 4752499 | 2026-03-23 07:48:56 | 2026-05-29 21:05:48 |  |
| `tbl_endereco_bairro` | BASE TABLE | InnoDB | 4134 | 2026-03-23 07:48:56 |  |  |
| `tbl_endereco_cidade` | BASE TABLE | InnoDB | 648 | 2026-03-23 07:48:56 | 2026-05-13 09:12:56 |  |
| `tbl_endereco_cidade_unidade` | BASE TABLE | InnoDB | 469 | 2026-03-23 07:48:56 | 2026-05-13 09:12:56 |  |
| `tbl_endereco_estado` | BASE TABLE | InnoDB | 27 | 2026-03-23 07:48:56 |  |  |
| `tbl_endereco_logradouro` | BASE TABLE | InnoDB | 49906 | 2026-03-23 07:48:56 |  |  |
| `tbl_eventos_site` | BASE TABLE | InnoDB | 4275469 | 2026-03-23 07:48:56 | 2026-05-29 21:05:58 |  |
| `tbl_habilitar_confianca` | BASE TABLE | InnoDB | 510720 | 2026-03-23 07:48:56 |  |  |
| `tbl_historico_vencimento` | BASE TABLE | InnoDB | 153296 | 2026-03-23 07:48:56 |  |  |
| `tbl_historico_viabilidades_venda` | BASE TABLE | InnoDB | 670023 | 2026-03-23 07:48:56 |  |  |
| `tbl_lead` | BASE TABLE | InnoDB | 3493762 | 2026-03-23 07:48:56 | 2026-05-29 21:05:48 |  |
| `tbl_lead_obs` | BASE TABLE | InnoDB | 355230 | 2026-03-23 07:48:56 | 2026-05-29 18:29:14 |  |
| `tbl_marcador_contrato` | BASE TABLE | InnoDB | 94288 | 2026-03-23 07:48:56 | 2026-05-20 17:58:12 |  |
| `tbl_mensagem_central` | BASE TABLE | InnoDB | 4820 | 2026-03-23 07:48:56 |  |  |
| `tbl_mensagem_usuario_central` | BASE TABLE | InnoDB | 33696215 | 2026-03-23 07:48:56 |  |  |
| `tbl_outros_marcadores` | BASE TABLE | InnoDB | 1514529 | 2026-03-23 07:48:56 | 2026-05-11 16:27:44 |  |
| `tbl_perfilacao_cobranca` | BASE TABLE | InnoDB | 2202107 | 2026-03-23 07:48:56 |  |  |
| `tbl_perfilacao_comercial` | BASE TABLE | InnoDB | 3614 | 2026-03-23 07:48:56 |  |  |
| `tbl_perfilacao_motivo` | BASE TABLE | InnoDB | 12 | 2026-03-23 07:48:56 |  |  |
| `tbl_perfilacao_ouvidoria` | BASE TABLE | InnoDB | 2 | 2026-03-23 07:48:56 |  |  |
| `tbl_perfilacao_retencao` | BASE TABLE | InnoDB | 1886664 | 2026-03-23 07:48:56 |  |  |
| `tbl_perfilacao_submotivo` | BASE TABLE | InnoDB | 83 | 2026-03-23 07:48:56 |  |  |
| `tbl_regra_suspensao` | BASE TABLE | InnoDB | 11 | 2026-03-23 07:48:56 |  |  |
| `tbl_regra_suspensao_unidade` | BASE TABLE | InnoDB | 2204 | 2026-03-23 07:48:56 |  |  |
| `tbl_renegociacao` | BASE TABLE | InnoDB | 2684 | 2026-03-23 07:48:56 |  |  |
| `tbl_renegociacao_titulo` | BASE TABLE | InnoDB | 4139 | 2026-03-23 07:48:56 |  |  |
| `tbl_termo` | BASE TABLE | InnoDB | 58 | 2026-03-23 07:48:56 |  |  |
| `tbl_termo_servico` | BASE TABLE | InnoDB | 1757 | 2026-03-23 07:48:56 |  |  |
| `tbl_vencimento` | BASE TABLE | InnoDB | 98 | 2026-03-23 07:48:56 | 2026-05-13 09:09:50 |  |
| `tbl_venda` | BASE TABLE | InnoDB | 7424718 | 2026-03-23 07:48:56 | 2026-05-29 21:05:48 |  |
| `tbl_venda_adicional` | BASE TABLE | InnoDB | 12784 | 2026-03-23 07:48:56 | 2026-05-27 10:11:08 |  |
| `tbl_venda_fase` | BASE TABLE | InnoDB | 0 | 2026-03-23 07:48:56 |  |  |
| `tbl_venda_origem` | BASE TABLE | InnoDB | 86276 | 2026-03-23 07:48:56 | 2026-05-29 21:05:48 |  |
| `tbl_vendedor` | BASE TABLE | InnoDB | 7958 | 2026-03-23 07:48:56 | 2026-05-29 17:24:54 |  |
| `tmp_ativacao_sydle` | BASE TABLE | InnoDB | 0 | 2026-03-23 07:48:56 |  |  |
| `tmp_atualizacao_dados_cliente` | BASE TABLE | InnoDB | 2330509 | 2026-04-06 12:44:27 | 2026-04-06 12:45:55 |  |
| `tmp_aviso_cliente_troca_onu` | BASE TABLE | InnoDB | 26498 | 2026-03-23 07:48:56 |  |  |
| `tmp_base_reajuste_hotsite` | BASE TABLE | InnoDB | 31878 | 2026-03-23 07:48:56 |  |  |
| `tmp_boleto_quitado_sap` | BASE TABLE | InnoDB | 2126289 | 2026-03-23 07:48:56 |  |  |
| `tmp_boleto_sap` | BASE TABLE | InnoDB | 43788 | 2026-03-23 07:48:56 |  |  |
| `tmp_cobranca_pontual` | BASE TABLE | InnoDB | 1860567 | 2026-03-23 07:48:56 | 2026-05-29 20:02:16 |  |
| `tmp_contrato_excecao_inadimplencia` | BASE TABLE | InnoDB | 20 | 2026-03-23 07:48:56 |  |  |
| `tmp_contrato_sap` | BASE TABLE | InnoDB | 513498 | 2026-03-23 07:48:56 |  |  |
| `tmp_desconto_agendado` | BASE TABLE | InnoDB | 321462 | 2026-03-23 07:48:56 |  |  |
| `tmp_evento_contrato_sydle` | BASE TABLE | InnoDB | 2468506 | 2026-03-23 07:48:56 |  |  |
| `tmp_evento_fatura` | BASE TABLE | InnoDB | 33112122 | 2026-03-23 07:48:56 | 2026-05-29 21:07:41 |  |
| `tmp_evento_financeiro_sydle` | BASE TABLE | InnoDB | 1024377 | 2026-03-23 07:48:56 |  |  |
| `tmp_falhas_integracoes` | BASE TABLE | InnoDB | 8278569 | 2026-03-23 07:48:56 |  |  |
| `tmp_faturas_sfmc` | BASE TABLE | InnoDB | 19624286 | 2026-03-23 07:48:56 |  |  |
| `tmp_item_sap` | BASE TABLE | InnoDB | 3127 | 2026-03-23 07:48:56 | 2026-05-29 17:18:32 |  |
| `tmp_mapeamento_pacotes` | BASE TABLE | InnoDB | 2592 | 2026-03-23 07:48:56 |  |  |
| `tmp_mapear_pacotes_adicionais` | BASE TABLE | InnoDB | 22 | 2026-03-23 07:48:56 |  |  |
| `tmp_nota_aberto_sap` | BASE TABLE | InnoDB | 0 | 2026-03-23 07:48:56 |  |  |
| `tmp_pacote_produto_sap` | BASE TABLE | InnoDB | 37261 | 2026-03-23 07:48:56 | 2026-05-14 10:18:34 |  |
| `tmp_pacote_sap` | BASE TABLE | InnoDB | 7947 | 2026-03-23 07:48:56 | 2026-05-14 10:18:34 |  |
| `tmp_produto_item_sap` | BASE TABLE | InnoDB | 7280 | 2026-03-23 07:48:56 | 2026-05-14 10:17:35 |  |
| `tmp_produto_sap` | BASE TABLE | InnoDB | 6540 | 2026-03-23 07:48:56 | 2026-05-14 10:17:35 |  |
| `tmp_suspensao_sydle` | BASE TABLE | InnoDB | 0 | 2026-03-23 07:48:56 |  |  |
| `tmp_tbl_app_adicional` | BASE TABLE | InnoDB | 848 | 2026-03-23 07:48:56 |  |  |
| `tmp_tbl_app_upgrade` | BASE TABLE | InnoDB | 752 | 2026-03-23 07:48:56 |  |  |
| `tmp_tbl_app_venda` | BASE TABLE | InnoDB | 8705 | 2026-03-23 07:48:56 |  |  |
| `tmp_tbl_controle_sms_churn` | BASE TABLE | InnoDB | 33904 | 2026-03-23 07:48:56 |  |  |
| `tmp_tbl_faturas_gi` | BASE TABLE | InnoDB | 30734 | 2026-03-23 07:48:56 |  |  |
| `tmp_telefones_invaido` | BASE TABLE | InnoDB | 84864 | 2026-03-23 07:48:56 |  |  |
| `tmp_update_status` | BASE TABLE | InnoDB | 1398 | 2026-03-23 07:48:56 |  |  |
| `vw_ativacao` | VIEW |  | 0 |  |  | VIEW |
| `vw_ativacoes_eps` | VIEW |  | 0 |  |  | VIEW |
| `vw_contrato_migracao_pendente` | VIEW |  | 0 |  |  | VIEW |
| `vw_contrato_ultimo_evento_ativacao` | VIEW |  | 0 |  |  | VIEW |
| `vw_contrato_ultimo_evento_suspensao` | VIEW |  | 0 |  |  | VIEW |
| `vw_desconto_contrato` | VIEW |  | 0 |  |  | VIEW |
| `vw_infancia` | VIEW |  | 0 |  |  | VIEW |
| `vw_suspensao_sem_ativacao` | VIEW |  | 0 |  |  | VIEW |
| `vw_valor_contrato` | VIEW |  | 0 |  |  | VIEW |

## `base_condominios_serasa`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `cep` | `varchar(255)` | YES |  | `` |  |  |
| 3 | `endereco` | `varchar(255)` | YES | MUL | `` |  |  |
| 4 | `regra` | `int(11)` | YES |  | `` |  |  |
| 5 | `qtd_cpf` | `int(11)` | YES |  | `` |  |  |
| 6 | `bairro` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `cidade` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `uf` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `base_condominios_serasa_endereco_cidade_cep_uf_idx` | NON_UNIQUE | 1 | `endereco` |
| `base_condominios_serasa_endereco_cidade_cep_uf_idx` | NON_UNIQUE | 2 | `cidade` |
| `base_condominios_serasa_endereco_cidade_cep_uf_idx` | NON_UNIQUE | 3 | `cep` |
| `base_condominios_serasa_endereco_cidade_cep_uf_idx` | NON_UNIQUE | 4 | `uf` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `cnpj_cnaes_secundarios`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `cnpj` | `varchar(14)` | YES | MUL | `` |  |  |
| 3 | `cnae_ordem` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `cnae` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cnpj_idx` | NON_UNIQUE | 1 | `cnpj` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `cnpj_empresas`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `cnpj` | `varchar(14)` | NO | MUL | `` |  |  |
| 3 | `matriz_filial` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `razao_social` | `varchar(255)` | YES |  | `` |  |  |
| 5 | `nome_fantasia` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `situacao` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `data_situacao` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `motivo_situacao` | `varchar(255)` | YES |  | `` |  |  |
| 9 | `nm_cidade_exterior` | `varchar(255)` | YES |  | `` |  |  |
| 10 | `cod_pais` | `varchar(255)` | YES |  | `` |  |  |
| 11 | `nome_pais` | `varchar(255)` | YES |  | `` |  |  |
| 12 | `cod_nat_juridica` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `data_inicio_ativ` | `varchar(255)` | YES |  | `` |  |  |
| 14 | `cnae_fiscal` | `varchar(255)` | YES |  | `` |  |  |
| 15 | `tipo_logradouro` | `varchar(255)` | YES |  | `` |  |  |
| 16 | `logradouro` | `varchar(255)` | YES | MUL | `` |  |  |
| 17 | `numero` | `varchar(255)` | YES | MUL | `` |  |  |
| 18 | `complemento` | `varchar(255)` | YES |  | `` |  |  |
| 19 | `bairro` | `varchar(255)` | YES | MUL | `` |  |  |
| 20 | `cep` | `varchar(255)` | YES |  | `` |  |  |
| 21 | `uf` | `varchar(255)` | YES |  | `` |  |  |
| 22 | `cod_municipio` | `varchar(255)` | YES |  | `` |  |  |
| 23 | `municipio` | `varchar(255)` | YES | MUL | `` |  |  |
| 24 | `ddd_1` | `varchar(255)` | YES |  | `` |  |  |
| 25 | `telefone_1` | `varchar(255)` | YES |  | `` |  |  |
| 26 | `ddd_2` | `varchar(255)` | YES |  | `` |  |  |
| 27 | `telefone_2` | `varchar(255)` | YES |  | `` |  |  |
| 28 | `ddd_fax` | `varchar(255)` | YES |  | `` |  |  |
| 29 | `num_fax` | `varchar(255)` | YES |  | `` |  |  |
| 30 | `email` | `varchar(255)` | YES |  | `` |  |  |
| 31 | `qualif_resp` | `varchar(255)` | YES |  | `` |  |  |
| 32 | `capital_social` | `varchar(255)` | YES |  | `` |  |  |
| 33 | `porte` | `varchar(255)` | YES |  | `` |  |  |
| 34 | `opc_simples` | `varchar(255)` | YES |  | `` |  |  |
| 35 | `data_opc_simples` | `varchar(255)` | YES |  | `` |  |  |
| 36 | `data_exc_simples` | `varchar(255)` | YES |  | `` |  |  |
| 37 | `opc_mei` | `varchar(255)` | YES |  | `` |  |  |
| 38 | `sit_especial` | `varchar(255)` | YES |  | `` |  |  |
| 39 | `data_sit_especial` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `bairro_idx` | NON_UNIQUE | 1 | `bairro` |
| `cnpj_empresas_logradouro_numero_bairro_municipio_idx` | NON_UNIQUE | 1 | `logradouro` |
| `cnpj_empresas_logradouro_numero_bairro_municipio_idx` | NON_UNIQUE | 2 | `numero` |
| `cnpj_empresas_logradouro_numero_bairro_municipio_idx` | NON_UNIQUE | 3 | `bairro` |
| `cnpj_empresas_logradouro_numero_bairro_municipio_idx` | NON_UNIQUE | 4 | `municipio` |
| `cnpj_idx` | NON_UNIQUE | 1 | `cnpj` |
| `logradouro_idx` | NON_UNIQUE | 1 | `logradouro` |
| `municipio_idx` | NON_UNIQUE | 1 | `municipio` |
| `numero_idx` | NON_UNIQUE | 1 | `numero` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `cnpj_socios`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `cnpj` | `varchar(14)` | NO | MUL | `` |  |  |
| 3 | `tipo_socio` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `nome_socio` | `varchar(255)` | YES |  | `` |  |  |
| 5 | `cnpj_cpf_socio` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `cod_qualificacao` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `perc_capital` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `data_entrada` | `varchar(255)` | YES |  | `` |  |  |
| 9 | `cod_pais_ext` | `varchar(255)` | YES |  | `` |  |  |
| 10 | `nome_pais_ext` | `varchar(255)` | YES |  | `` |  |  |
| 11 | `cpf_repres` | `varchar(255)` | YES |  | `` |  |  |
| 12 | `nome_repres` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `cod_qualif_repres` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cnpj_idx` | NON_UNIQUE | 1 | `cnpj` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `contrato_produto_temp`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `int(20)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `contrato_ultima_reativacao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_contrato` | `bigint(20)` | NO |  | `0` |  |  |
| 2 | `ultima_reativacao` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `contrato_ultima_suspensao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_contrato` | `bigint(20)` | NO |  | `0` |  |  |
| 2 | `ultima_suspensao` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `schema_version`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `version_rank` | `int(11)` | NO | MUL | `` |  |  |
| 2 | `installed_rank` | `int(11)` | NO | MUL | `` |  |  |
| 3 | `version` | `varchar(50)` | NO | PRI | `` |  |  |
| 4 | `description` | `varchar(200)` | NO |  | `` |  |  |
| 5 | `type` | `varchar(20)` | NO |  | `` |  |  |
| 6 | `script` | `varchar(1000)` | NO |  | `` |  |  |
| 7 | `checksum` | `int(11)` | YES |  | `` |  |  |
| 8 | `installed_by` | `varchar(100)` | NO |  | `` |  |  |
| 9 | `installed_on` | `timestamp` | NO |  | `CURRENT_TIMESTAMP` |  |  |
| 10 | `execution_time` | `int(11)` | NO |  | `` |  |  |
| 11 | `success` | `tinyint(1)` | NO | MUL | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `version` |
| `schema_version_ir_idx` | NON_UNIQUE | 1 | `installed_rank` |
| `schema_version_s_idx` | NON_UNIQUE | 1 | `success` |
| `schema_version_vr_idx` | NON_UNIQUE | 1 | `version_rank` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `stg_contratos_sydle`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `Codigo` | `int(11)` | YES |  | `` |  |  |
| 2 | `Codigo_externo` | `int(11)` | YES |  | `` |  |  |
| 3 | `ID` | `varchar(30)` | YES |  | `` |  |  |
| 4 | `Comprador_ID` | `varchar(150)` | YES |  | `` |  |  |
| 5 | `Comprador_Nome` | `varchar(150)` | YES |  | `` |  |  |
| 6 | `Plano_Identificador` | `varchar(150)` | YES |  | `` |  |  |
| 7 | `Plano_Nome` | `varchar(150)` | YES |  | `` |  |  |
| 8 | `Status_Faturamento` | `varchar(150)` | YES |  | `` |  |  |
| 9 | `Status_Servico` | `varchar(30)` | YES |  | `` |  |  |
| 10 | `dt_extracao` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `stg_faturas_sydle`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `Codigo` | `int(11)` | YES |  | `` |  |  |
| 2 | `Valor` | `decimal(10,2)` | YES |  | `` |  |  |
| 3 | `Valor_pago` | `decimal(10,2)` | YES |  | `` |  |  |
| 4 | `Data_Vencimento` | `date` | YES |  | `` |  |  |
| 5 | `Data_Pagamento` | `date` | YES |  | `` |  |  |
| 6 | `Data_Criacao` | `date` | YES |  | `` |  |  |
| 7 | `status` | `varchar(50)` | YES |  | `` |  |  |
| 8 | `Classificacao` | `varchar(15)` | YES |  | `` |  |  |
| 9 | `Itens_contrato_codigo` | `varchar(30)` | YES |  | `` |  |  |
| 10 | `Id_Itens_contrato_produto` | `varchar(80)` | YES |  | `` |  |  |
| 11 | `Itens_produto` | `varchar(100)` | YES |  | `` |  |  |
| 12 | `Itens_valor` | `decimal(19,6)` | YES |  | `` |  |  |
| 13 | `Pagador_nome` | `varchar(150)` | YES |  | `` |  |  |
| 14 | `Pagador_id` | `varchar(150)` | YES |  | `` |  |  |
| 15 | `dt_extracao` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `STG_SUSPENSAO_CLIENTE`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `CODIGO_FATURA` | `int(11)` | YES |  | `` |  |  |
| 2 | `DIAS_ATRASO` | `int(11)` | YES |  | `` |  |  |
| 3 | `CARD_CODE` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `CLIENTE` | `varchar(100)` | YES |  | `` |  |  |
| 5 | `SALDO` | `decimal(19,6)` | YES |  | `` |  |  |
| 6 | `CONTRATO_AIR` | `int(11)` | YES |  | `` |  |  |
| 7 | `DOC` | `varchar(14)` | YES |  | `` |  |  |
| 8 | `DT_SUSPENSAO` | `datetime` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_analise_credito`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_lead` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `cpf_cnpj_consulta` | `varchar(18)` | NO | MUL | `` |  |  |
| 4 | `data_analise` | `datetime` | YES |  | `` |  |  |
| 5 | `numero_restricoes` | `int(11)` | YES |  | `` |  |  |
| 6 | `valor_total` | `decimal(10,2)` | YES |  | `` |  |  |
| 7 | `autorizado` | `tinyint(1)` | NO |  | `` |  |  |
| 8 | `usuario_autorizador` | `varchar(10)` | YES |  | `` |  |  |
| 9 | `data_autorizacao` | `datetime` | YES |  | `` |  |  |
| 10 | `justificativa_autorizacao` | `text` | YES |  | `` |  |  |
| 11 | `xml` | `longtext` | YES |  | `` |  |  |
| 12 | `integracao_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `integracao_transacao` | `varchar(255)` | YES |  | `` |  |  |
| 14 | `integracao_status` | `varchar(255)` | NO | MUL | `` |  |  |
| 15 | `integracao_mensagem` | `varchar(255)` | YES |  | `` |  |  |
| 16 | `validacao_nome` | `varchar(100)` | YES |  | `` |  |  |
| 17 | `validacao_nome_mae` | `varchar(100)` | YES |  | `` |  |  |
| 18 | `validacao_data_nascimento` | `varchar(100)` | YES |  | `` |  |  |
| 19 | `situacao_documento` | `varchar(100)` | YES |  | `` |  |  |
| 20 | `nota_serasa` | `int(11)` | YES |  | `` |  |  |
| 21 | `aprovado_serasa` | `tinyint(1)` | YES |  | `` |  |  |
| 22 | `status_serasa` | `varchar(100)` | YES |  | `` |  |  |
| 23 | `aprovado_spc` | `tinyint(1)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `analise_credito_lead_idx` | NON_UNIQUE | 1 | `id_lead` |
| `idx_tbl_analise_credito_integracao_status` | NON_UNIQUE | 1 | `integracao_status` |
| `ix_tbl_analise_credito_01` | NON_UNIQUE | 1 | `cpf_cnpj_consulta` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_analise_credito_lead` | `id_lead` | `tbl_lead` | `id` |

## `tbl_analise_credito_atributo`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_analise_credito` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `codigo` | `varchar(20)` | NO |  | `` |  |  |
| 4 | `nome` | `varchar(60)` | NO |  | `` |  |  |
| 5 | `valor` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `analise_credito_atributo_analise_credito_idx` | NON_UNIQUE | 1 | `id_analise_credito` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_analise_credito_atributo_analise_credito` | `id_analise_credito` | `tbl_analise_credito` | `id` |

## `tbl_analise_credito_restricao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_analise_credito` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `cidade_associado` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `nome_associado` | `varchar(255)` | NO |  | `` |  |  |
| 5 | `codigo_entidade` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `nome_entidade` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `contrato` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `data_vencimento` | `date` | YES |  | `` |  |  |
| 9 | `data_inclusao` | `date` | NO |  | `` |  |  |
| 10 | `valor` | `decimal(10,2)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `analise_credito_restricao_analise_credito_idx` | NON_UNIQUE | 1 | `id_analise_credito` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_analise_credito_restricao_analise_credito` | `id_analise_credito` | `tbl_analise_credito` | `id` |

## `tbl_auditoria_habilitar_confianca`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `momento` | `datetime` | NO |  | `` |  |  |
| 3 | `id_habilitacao` | `bigint(20)` | YES | MUL | `` |  |  |
| 4 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 5 | `saldo` | `int(11)` | NO |  | `` |  |  |
| 6 | `canal` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `auditoria_habilitar_confianca_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `auditoria_hab_conf_hab_conf_habilitacao_idx` | NON_UNIQUE | 1 | `id_habilitacao` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_audit_contato`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 4 | `data` | `datetime` | NO |  | `` |  |  |
| 5 | `confirmado` | `tinyint(1)` | YES |  | `0` |  |  |
| 6 | `status` | `varchar(45)` | YES |  | `` |  |  |
| 7 | `codigo_confirmacao` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `canal_confirmacao` | `varchar(50)` | YES |  | `` |  |  |
| 9 | `origem_alteracao` | `varchar(50)` | YES |  | `` |  |  |
| 10 | `usuario` | `varchar(10)` | NO |  | `` |  |  |
| 11 | `operacao` | `varchar(1)` | NO |  | `` |  |  |
| 12 | `contato` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `tipo_contato` | `varchar(20)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tac_cliente` | NON_UNIQUE | 1 | `id_cliente` |
| `tac_contato` | NON_UNIQUE | 1 | `id_contato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_aviso_migracao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 4 | `pacote_atual` | `varchar(255)` | NO |  | `` |  |  |
| 5 | `pacote_ofertado_1` | `varchar(255)` | NO |  | `` |  |  |
| 6 | `valor_ofertado_1` | `decimal(10,2)` | NO |  | `` |  |  |
| 7 | `pacote_ofertado_2` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `valor_ofertado_2` | `decimal(10,2)` | YES |  | `` |  |  |
| 9 | `validade_promocao` | `date` | NO |  | `` |  |  |
| 10 | `migracao_compulsoria` | `tinyint(1)` | NO |  | `0` |  |  |
| 11 | `reajuste` | `tinyint(1)` | NO |  | `0` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `alterta_migracao_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `alterta_migracao_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `aviso_migracao_id_cliente_migracao_compulsoria_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `aviso_migracao_id_cliente_migracao_compulsoria_idx` | NON_UNIQUE | 2 | `migracao_compulsoria` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_blacklist`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `cpf_cnpj` | `varchar(18)` | NO | UNI | `` |  |  |
| 8 | `nome` | `varchar(255)` | NO |  | `` |  |  |
| 9 | `id_cliente` | `bigint(20)` | YES | MUL | `` |  |  |
| 10 | `motivo` | `varchar(255)` | YES |  | `` |  |  |
| 11 | `bloqueado` | `tinyint(1)` | NO |  | `1` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `cpf_cnpj_UNIQUE` | UNIQUE | 1 | `cpf_cnpj` |
| `fk_tbl_blacklist_cliente` | NON_UNIQUE | 1 | `id_cliente` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_blacklist_cliente` | `id_cliente` | `tbl_cliente` | `id` |

## `tbl_blacklist_evento`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_blacklist` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `momento` | `datetime` | NO |  | `` |  |  |
| 4 | `usuario` | `varchar(10)` | NO |  | `` |  |  |
| 5 | `tipo` | `varchar(255)` | NO |  | `` |  |  |
| 6 | `observacao` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `blacklist_idx` | NON_UNIQUE | 1 | `id_blacklist` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_blacklist_evento_blacklist` | `id_blacklist` | `tbl_blacklist` | `id` |

## `tbl_bloqueio_generico`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `momento` | `datetime` | NO |  | `` |  |  |
| 3 | `identificacao` | `varchar(255)` | NO | UNI | `` |  |  |
| 4 | `bloqueio_ativo` | `tinyint(1)` | NO |  | `0` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `identificacao_UNIQUE` | UNIQUE | 1 | `identificacao` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_campanha`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `codigo` | `varchar(10)` | NO | UNI | `` |  |  |
| 8 | `NOME` | `varchar(150)` | NO |  | `` |  |  |
| 9 | `recorrencia_desconto` | `decimal(10,2)` | YES |  | `` |  |  |
| 10 | `recorrencia_vigencia` | `int(11)` | YES |  | `` |  |  |
| 11 | `up_operacional_vigencia` | `int(11)` | YES |  | `` |  |  |
| 12 | `numero_restricoes_spc` | `int(11)` | YES |  | `` |  |  |
| 13 | `valor_restricoes_spc` | `decimal(10,2)` | YES |  | `` |  |  |
| 14 | `fideliza` | `tinyint(1)` | NO |  | `` |  |  |
| 15 | `termo_aceite` | `longtext` | NO |  | `` |  |  |
| 16 | `instalacao_empresa_cnpj` | `varchar(16)` | YES |  | `` |  |  |
| 17 | `instalacao_empresa_nome` | `varchar(255)` | YES |  | `` |  |  |
| 18 | `instalacao_item_codigo` | `varchar(12)` | YES |  | `` |  |  |
| 19 | `instalacao_item_nome` | `varchar(60)` | YES |  | `` |  |  |
| 20 | `instalacao_valor` | `decimal(10,2)` | NO |  | `` |  |  |
| 21 | `instalacao_desconto_prazo` | `decimal(10,2)` | YES |  | `` |  |  |
| 22 | `instalacao_desconto_avista` | `decimal(10,2)` | YES |  | `` |  |  |
| 23 | `instalacao_limite_parcela` | `int(11)` | NO |  | `1` |  |  |
| 24 | `disponivel_site` | `tinyint(1)` | NO |  | `` |  |  |
| 25 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |
| 26 | `recorrencia_desconto_data_venda` | `tinyint(1)` | NO |  | `0` |  |  |
| 27 | `b2b` | `tinyint(1)` | NO |  | `0` |  |  |
| 28 | `data_inicio` | `date` | YES |  | `` |  |  |
| 29 | `data_fim` | `date` | YES |  | `` |  |  |
| 30 | `pme` | `tinyint(1)` | NO |  | `0` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `codigo_UNIQUE` | UNIQUE | 1 | `codigo` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_campanha_equipe`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_campanha` | `bigint(20)` | NO | MUL | `` |  |  |
| 2 | `equipes` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `tbl_campanha_equipe_idx` | NON_UNIQUE | 1 | `id_campanha` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_campanha_equipe` | `id_campanha` | `tbl_campanha` | `id` |

## `tbl_campanha_pacote`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_campanha` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `pacote_base_codigo` | `varchar(255)` | NO |  | `` |  |  |
| 4 | `pacote_base_nome` | `varchar(255)` | NO |  | `` |  |  |
| 5 | `pacote_up_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `pacote_up_nome` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `valor_total` | `decimal(10,2)` | NO |  | `` |  |  |
| 8 | `url_imagem` | `varchar(255)` | YES |  | `` |  |  |
| 9 | `porcentagem_comissao` | `decimal(10,2)` | NO |  | `` |  |  |
| 10 | `possui_internet` | `tinyint(1)` | NO |  | `` |  |  |
| 11 | `possui_tv` | `tinyint(1)` | NO |  | `` |  |  |
| 12 | `possui_telefone` | `tinyint(1)` | NO |  | `` |  |  |
| 13 | `recorrencia_percentual_desconto` | `decimal(10,4)` | YES |  | `` |  |  |
| 14 | `recorrencia_meses_desconto` | `int(11)` | YES |  | `` |  |  |
| 15 | `pacote_up_meses_desconto` | `int(11)` | YES |  | `` |  |  |
| 16 | `agendamento_instalacao_obrigatorio` | `tinyint(1)` | NO |  | `0` |  |  |
| 17 | `taxa_instalacao_antecipada` | `decimal(10,2)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `campanha_pacote_campanha_idx` | NON_UNIQUE | 1 | `id_campanha` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_campanha_pacote_campanha` | `id_campanha` | `tbl_campanha` | `id` |

## `tbl_campanha_pacote_adicional`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_pacote` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `produto_codigo` | `varchar(60)` | NO |  | `` |  |  |
| 4 | `produto_nome` | `varchar(255)` | NO |  | `` |  |  |
| 5 | `produto_grupo` | `varchar(60)` | NO |  | `` |  |  |
| 6 | `valor_total` | `decimal(10,2)` | NO |  | `` |  |  |
| 7 | `url_imagem` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `quantidade_limite` | `int(11)` | YES |  | `` |  |  |
| 9 | `porcentagem_comissao` | `decimal(10,2)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `campanha_pacote_adicional_campanha_pacote_idx` | NON_UNIQUE | 1 | `id_pacote` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_campanha_pacote_adicional_campanha_pacote` | `id_pacote` | `tbl_campanha_pacote` | `id` |

## `tbl_campanha_unidade`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_campanha` | `bigint(20)` | NO | MUL | `` |  |  |
| 2 | `unidades` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `campanha_unidade_campanha_idx` | NON_UNIQUE | 1 | `id_campanha` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_campanha_unidade_campanha` | `id_campanha` | `tbl_campanha` | `id` |

## `tbl_carteira`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_vendedor` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `tipo` | `varchar(20)` | NO |  | `` |  |  |
| 9 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `carteira_vendedor_idx` | NON_UNIQUE | 1 | `id_vendedor` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_carteira_vendedor` | `id_vendedor` | `tbl_vendedor` | `id` |

## `tbl_classificar_risco`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_classificacao` | `datetime` | NO |  | `` |  |  |
| 3 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 4 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 5 | `classificacao` | `varchar(255)` | NO |  | `` |  |  |
| 6 | `subclassificacao` | `varchar(255)` | NO |  | `` |  |  |
| 7 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_classificar_risco_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `tbl_classificar_risco_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_cliente`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO | MUL | `` |  |  |
| 7 | `id_carteira` | `bigint(20)` | YES | MUL | `` |  |  |
| 8 | `tipo` | `varchar(20)` | NO |  | `` |  |  |
| 9 | `nome` | `varchar(100)` | NO | MUL | `` |  |  |
| 10 | `tratamento` | `varchar(20)` | NO |  | `` |  |  |
| 11 | `grupo` | `varchar(20)` | NO |  | `` |  |  |
| 12 | `codigo` | `varchar(20)` | NO | UNI | `` |  |  |
| 13 | `senha_sac` | `varchar(20)` | NO | MUL | `` |  |  |
| 14 | `fonte` | `varchar(20)` | NO |  | `` |  |  |
| 15 | `avaliacao` | `varchar(45)` | YES |  | `` |  |  |
| 16 | `legado_id` | `bigint(20)` | YES | MUL | `` |  |  |
| 17 | `legado_sistema` | `varchar(20)` | YES |  | `` |  |  |
| 18 | `integracao_status` | `varchar(20)` | NO |  | `` |  |  |
| 19 | `integracao_mensagem` | `varchar(255)` | YES |  | `` |  |  |
| 20 | `integracao_codigo` | `varchar(255)` | YES | MUL | `` |  |  |
| 21 | `integracao_transacao` | `varchar(255)` | YES | MUL | `` |  |  |
| 22 | `marcador` | `varchar(20)` | YES |  | `` |  |  |
| 23 | `cliente_b2b` | `tinyint(1)` | NO |  | `0` |  |  |
| 24 | `integracao_status_sydle` | `varchar(20)` | NO |  | `NOVO` |  |  |
| 25 | `integracao_mensagem_sydle` | `varchar(255)` | YES |  | `` |  |  |
| 26 | `integracao_codigo_sydle` | `varchar(255)` | YES |  | `` |  |  |
| 27 | `integracao_transacao_sydle` | `varchar(255)` | YES |  | `` |  |  |
| 28 | `id_suporte_sumicity_virtual_um` | `varchar(255)` | YES |  | `` |  |  |
| 29 | `id_suporte_sumicity_virtual_dois` | `varchar(255)` | YES |  | `` |  |  |
| 30 | `id_oauth` | `varchar(255)` | YES |  | `` |  |  |
| 31 | `id_oauth_giga_mais` | `varchar(255)` | YES |  | `` |  |  |
| 32 | `id_oauth_click` | `varchar(255)` | YES |  | `` |  |  |
| 33 | `cupom` | `varchar(50)` | YES | MUL | `` |  |  |
| 34 | `id_oauth_univox` | `varchar(255)` | YES |  | `` |  |  |
| 35 | `id_oauth_ligue` | `varchar(255)` | YES |  | `` |  |  |
| 36 | `nome_social` | `varchar(100)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cliente_carteira_idx` | NON_UNIQUE | 1 | `id_carteira` |
| `cliente_nome_idx` | NON_UNIQUE | 1 | `nome` |
| `codigo_integracao_idx` | NON_UNIQUE | 1 | `integracao_codigo` |
| `codigo_transacao_idx` | NON_UNIQUE | 1 | `integracao_transacao` |
| `codigo_UNIQUE` | UNIQUE | 1 | `codigo` |
| `cupom_idx` | NON_UNIQUE | 1 | `cupom` |
| `fk_cliente_carteira` | NON_UNIQUE | 1 | `id_carteira` |
| `ix_tbl_cliente_01` | NON_UNIQUE | 1 | `senha_sac` |
| `ix_tbl_cliente_02` | NON_UNIQUE | 1 | `legado_id` |
| `ix_tbl_cliente_02` | NON_UNIQUE | 2 | `id` |
| `ix_tbl_cliente_03` | NON_UNIQUE | 1 | `excluido` |
| `ix_tbl_cliente_03` | NON_UNIQUE | 2 | `integracao_status` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_cliente_carteira` | `id_carteira` | `tbl_carteira` | `id` |

## `tbl_cliente_anexo`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `arquivo` | `varchar(255)` | NO |  | `` |  |  |
| 9 | `extensao` | `varchar(255)` | NO |  | `` |  |  |
| 10 | `nome` | `varchar(255)` | NO |  | `` |  |  |
| 11 | `diretorio` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cliente_anexo_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_cliente_anexo_cliente` | `id_cliente` | `tbl_cliente` | `id` |

## `tbl_cliente_contato`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO | MUL | `` |  |  |
| 7 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `tipo` | `varchar(20)` | NO |  | `` |  |  |
| 9 | `contato` | `varchar(255)` | NO | MUL | `` |  |  |
| 10 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |
| 11 | `confirmado` | `tinyint(1)` | YES |  | `0` |  |  |
| 12 | `status` | `varchar(45)` | YES |  | `` |  |  |
| 13 | `codigo_confirmacao` | `varchar(255)` | YES |  | `` |  |  |
| 14 | `favorito` | `tinyint(1)` | YES |  | `0` |  |  |
| 15 | `canal_confirmacao` | `varchar(50)` | YES |  | `` |  |  |
| 16 | `data_alter_contato` | `datetime` | YES |  | `` |  |  |
| 17 | `data_confirmacao` | `datetime` | YES |  | `` |  |  |
| 18 | `origem` | `varchar(50)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cliente_contato_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `cliente_contrato_excluido_idx` | NON_UNIQUE | 1 | `excluido` |
| `fk_cliente_contato_cliente` | NON_UNIQUE | 1 | `id_cliente` |
| `ix_tbl_cliente_contato_01` | NON_UNIQUE | 1 | `contato` |
| `ix_tbl_cliente_contato_02` | NON_UNIQUE | 1 | `excluido` |
| `ix_tbl_cliente_contato_02` | NON_UNIQUE | 2 | `contato` |
| `ix_tbl_cliente_contato_03` | NON_UNIQUE | 1 | `id_cliente` |
| `ix_tbl_cliente_contato_03` | NON_UNIQUE | 2 | `excluido` |
| `ix_tbl_cliente_contato_03` | NON_UNIQUE | 3 | `ativo` |
| `ix_tbl_cliente_contato_03` | NON_UNIQUE | 4 | `tipo` |
| `ix_tbl_cliente_contato_03` | NON_UNIQUE | 5 | `contato` |
| `ix_tbl_cliente_contato_04` | NON_UNIQUE | 1 | `id_cliente` |
| `ix_tbl_cliente_contato_04` | NON_UNIQUE | 2 | `contato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_cliente_contato_cliente` | `id_cliente` | `tbl_cliente` | `id` |

## `tbl_cliente_evento`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `momento` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `id_contrato` | `bigint(20)` | YES | MUL | `` |  |  |
| 5 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 6 | `tipo` | `varchar(255)` | NO |  | `` |  |  |
| 7 | `observacao` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `motivo_associado` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cliente_evento_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `cliente_evento_contrato` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_cliente_fisico`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_cliente` | `bigint(20)` | NO | PRI | `` |  |  |
| 2 | `cpf` | `varchar(14)` | NO | UNI | `` |  |  |
| 3 | `data_nascimento` | `date` | NO |  | `` |  |  |
| 4 | `rg_numero` | `varchar(45)` | NO | MUL | `` |  |  |
| 5 | `rg_orgao` | `varchar(45)` | NO |  | `` |  |  |
| 6 | `estado_civil` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `nome_pai` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `nome_mae` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cliente_fisico_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `cpf_UNIQUE` | UNIQUE | 1 | `cpf` |
| `ix_tbl_cliente_fisico_01` | NON_UNIQUE | 1 | `rg_numero` |
| `PRIMARY` | UNIQUE | 1 | `id_cliente` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_cliente_fisico_cliente` | `id_cliente` | `tbl_cliente` | `id` |

## `tbl_cliente_juridico`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_cliente` | `bigint(20)` | NO | PRI | `` |  |  |
| 2 | `cnpj` | `varchar(18)` | NO | UNI | `` |  |  |
| 3 | `inscricao_estadual` | `varchar(50)` | NO |  | `` |  |  |
| 4 | `inscricao_municipal` | `varchar(50)` | NO |  | `` |  |  |
| 5 | `nome_fantasia` | `varchar(255)` | NO |  | `` |  |  |
| 6 | `atividade_principal` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cliente_juridico_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `cnpj_UNIQUE` | UNIQUE | 1 | `cnpj` |
| `PRIMARY` | UNIQUE | 1 | `id_cliente` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_cliente_juridico_cliente` | `id_cliente` | `tbl_cliente` | `id` |

## `tbl_cliente_orientacao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 4 | `orientacao` | `text` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `fk_cliente_orientacao` | NON_UNIQUE | 1 | `id_cliente` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_cliente_orientacao` | `id_cliente` | `tbl_cliente` | `id` |

## `tbl_cliente_routethis`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `id_cliente_routethis` | `varchar(255)` | NO | MUL | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_cliente_routethis_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `tbl_tbl_cliente_routethis_routethis_idx` | NON_UNIQUE | 1 | `id_cliente_routethis` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_cliente_routethis_cliente` | `id_cliente` | `tbl_cliente` | `id` |

## `tbl_condominio`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `nome` | `varchar(255)` | NO |  | `` |  |  |
| 8 | `logradouro` | `varchar(255)` | NO |  | `` |  |  |
| 9 | `bairro` | `varchar(255)` | NO |  | `` |  |  |
| 10 | `numero` | `varchar(10)` | NO |  | `` |  |  |
| 11 | `complemento` | `varchar(255)` | YES |  | `` |  |  |
| 12 | `id_cidade` | `bigint(20)` | NO | MUL | `` |  |  |
| 13 | `referencia` | `varchar(255)` | NO |  | `` |  |  |
| 14 | `nome_sindico` | `varchar(255)` | NO |  | `` |  |  |
| 15 | `telefone_sindico` | `varchar(255)` | NO |  | `` |  |  |
| 16 | `status_atual` | `varchar(255)` | NO | MUL | `` |  |  |
| 17 | `data_vistoria_prevista` | `date` | YES |  | `` |  |  |
| 18 | `data_vistoria_executada` | `date` | YES |  | `` |  |  |
| 19 | `data_construcao_prevista` | `date` | YES |  | `` |  |  |
| 20 | `data_construcao_realizada` | `date` | YES |  | `` |  |  |
| 21 | `tipo_condominio` | `varchar(50)` | YES |  | `` |  |  |
| 22 | `cep` | `varchar(10)` | YES |  | `` |  |  |
| 23 | `end_completo` | `varchar(255)` | YES |  | `` |  |  |
| 24 | `tipo_logradouro` | `varchar(255)` | YES |  | `` |  |  |
| 25 | `unidade` | `varchar(255)` | YES |  | `` |  |  |
| 26 | `end_latitude` | `decimal(10,8)` | YES |  | `` |  |  |
| 27 | `end_longitude` | `decimal(10,8)` | YES |  | `` |  |  |
| 28 | `email_sindico` | `varchar(255)` | YES |  | `` |  |  |
| 29 | `nome_zelador` | `varchar(255)` | YES |  | `` |  |  |
| 30 | `telefone_zelador` | `varchar(255)` | YES |  | `` |  |  |
| 31 | `email_zelador` | `varchar(255)` | YES |  | `` |  |  |
| 32 | `end_certificado` | `tinyint(1)` | NO |  | `0` |  |  |
| 33 | `end_verificado` | `tinyint(1)` | NO |  | `0` |  |  |
| 34 | `status_visita` | `varchar(255)` | YES |  | `` |  |  |
| 35 | `prioridade` | `varchar(255)` | YES |  | `` |  |  |
| 36 | `quantidade_blocos` | `int(11)` | YES |  | `` |  |  |
| 37 | `quantidade_prumadas_bloco` | `int(11)` | YES |  | `` |  |  |
| 38 | `quantidade_apartamentos_bloco` | `int(11)` | YES |  | `` |  |  |
| 39 | `quantidade_andares` | `int(11)` | YES |  | `` |  |  |
| 40 | `cenario` | `varchar(255)` | YES |  | `` |  |  |
| 41 | `link_mapa` | `varchar(255)` | YES |  | `` |  |  |
| 42 | `link_diagrama` | `varchar(255)` | YES |  | `` |  |  |
| 43 | `endereco_entroncamento` | `varchar(255)` | YES |  | `` |  |  |
| 44 | `fibra_facilidade_area` | `varchar(255)` | YES |  | `` |  |  |
| 45 | `material_gasto` | `varchar(255)` | YES |  | `` |  |  |
| 46 | `tipo_servico` | `varchar(255)` | YES |  | `` |  |  |
| 47 | `metragem_lancamento` | `varchar(255)` | YES |  | `` |  |  |
| 48 | `data_solicitacao` | `date` | YES |  | `` |  |  |
| 49 | `data_inicio` | `date` | YES |  | `` |  |  |
| 50 | `registro_planilha` | `tinyint(1)` | NO |  | `0` |  |  |
| 51 | `perfil` | `varchar(255)` | YES |  | `` |  |  |
| 52 | `andares_uteis` | `varchar(255)` | YES |  | `` |  |  |
| 53 | `quantidade_apartamentos_andar` | `varchar(255)` | YES |  | `` |  |  |
| 54 | `hps_bloco` | `varchar(255)` | YES |  | `` |  |  |
| 55 | `descricao_tubulacao` | `varchar(255)` | YES |  | `` |  |  |
| 56 | `concorrentes` | `varchar(255)` | YES |  | `` |  |  |
| 57 | `tecnologia_concorrente` | `varchar(255)` | YES |  | `` |  |  |
| 58 | `servico_oferecido` | `varchar(255)` | YES |  | `` |  |  |
| 59 | `avaliacao_breve` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cidade_idx` | NON_UNIQUE | 1 | `id_cidade` |
| `condominio_status_atual_logradouro_bairro_numero_idx` | NON_UNIQUE | 1 | `status_atual` |
| `condominio_status_atual_logradouro_bairro_numero_idx` | NON_UNIQUE | 2 | `logradouro` |
| `condominio_status_atual_logradouro_bairro_numero_idx` | NON_UNIQUE | 3 | `bairro` |
| `condominio_status_atual_logradouro_bairro_numero_idx` | NON_UNIQUE | 4 | `numero` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_condominio_cidade` | `id_cidade` | `tbl_endereco_cidade` | `id` |

## `tbl_condominio_evento`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `momento` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `tipo` | `varchar(255)` | YES |  | `` |  |  |
| 5 | `id_condominio` | `bigint(20)` | NO | MUL | `` |  |  |
| 6 | `observacao` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `status_antigo` | `varchar(255)` | NO |  | `` |  |  |
| 8 | `status_novo` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `condominio_idx` | NON_UNIQUE | 1 | `id_condominio` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_condominio_condominio` | `id_condominio` | `tbl_condominio` | `id` |

## `tbl_contrato`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO | MUL | `` |  |  |
| 7 | `versao` | `int(11)` | NO |  | `` |  |  |
| 8 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 9 | `pacote_codigo` | `varchar(255)` | NO |  | `` |  |  |
| 10 | `pacote_nome` | `varchar(255)` | NO |  | `` |  |  |
| 11 | `valor_base` | `decimal(10,2)` | NO |  | `` |  |  |
| 12 | `valor_final` | `decimal(10,2)` | NO |  | `` |  |  |
| 13 | `status` | `varchar(255)` | NO | MUL | `` |  |  |
| 14 | `id_vencimento` | `bigint(20)` | NO | MUL | `` |  |  |
| 15 | `id_regra_suspensao` | `bigint(20)` | NO | MUL | `` |  |  |
| 16 | `id_endereco_cobranca` | `bigint(20)` | NO | MUL | `` |  |  |
| 17 | `data_ultimo_faturamento` | `date` | YES |  | `` |  |  |
| 18 | `data_proximo_reajuste` | `date` | YES |  | `` |  |  |
| 19 | `data_primeira_ativacao` | `date` | YES |  | `` |  |  |
| 20 | `data_cancelamento` | `date` | YES | MUL | `` |  |  |
| 21 | `data_ativacao_agendada` | `date` | YES |  | `` |  |  |
| 22 | `codigo_tipo_cobranca` | `varchar(255)` | NO |  | `` |  |  |
| 23 | `unidade_atendimento` | `varchar(10)` | NO | MUL | `` |  |  |
| 24 | `cancelamento_motivo` | `varchar(255)` | YES |  | `` |  |  |
| 25 | `versao_motivo` | `varchar(255)` | NO |  | `` |  |  |
| 26 | `legado_id` | `bigint(20)` | YES | MUL | `` |  |  |
| 27 | `legado_sistema` | `varchar(20)` | YES | MUL | `` |  |  |
| 28 | `observacao_internet` | `text` | YES |  | `` |  |  |
| 29 | `observacao_telefonia` | `text` | YES |  | `` |  |  |
| 30 | `observacao_tv` | `text` | YES |  | `` |  |  |
| 31 | `marcador` | `varchar(255)` | YES |  | `` |  |  |
| 32 | `b2b` | `tinyint(1)` | NO |  | `0` |  |  |
| 33 | `integracao_status` | `varchar(20)` | NO | MUL | `NOVO` |  |  |
| 34 | `integracao_mensagem` | `varchar(255)` | YES |  | `` |  |  |
| 35 | `integracao_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 36 | `integracao_transacao` | `varchar(255)` | YES |  | `` |  |  |
| 37 | `pme` | `tinyint(1)` | NO |  | `0` |  |  |
| 38 | `reserva_connectmaster_cancelada` | `tinyint(1)` | NO |  | `0` |  |  |
| 39 | `telefone` | `varchar(15)` | YES | MUL | `` |  |  |
| 40 | `status_consolidado` | `varchar(100)` | YES |  | `` |  |  |
| 41 | `utiliza_app` | `tinyint(1)` | YES |  | `` |  |  |
| 42 | `gigatv_colab` | `tinyint(1)` | NO |  | `0` |  |  |
| 43 | `metodo_pagamento` | `varchar(100)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `contrato_data_cancelamento_reserva_connectmaster_cancelada_idx` | NON_UNIQUE | 1 | `data_cancelamento` |
| `contrato_data_cancelamento_reserva_connectmaster_cancelada_idx` | NON_UNIQUE | 2 | `reserva_connectmaster_cancelada` |
| `contrato_endereco_cobranca_idx` | NON_UNIQUE | 1 | `id_endereco_cobranca` |
| `contrato_excluido_id_cliente_status_idx` | NON_UNIQUE | 1 | `excluido` |
| `contrato_excluido_id_cliente_status_idx` | NON_UNIQUE | 2 | `id_cliente` |
| `contrato_excluido_id_cliente_status_idx` | NON_UNIQUE | 3 | `status` |
| `contrato_id_cliente_data_cancelamento_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `contrato_id_cliente_data_cancelamento_idx` | NON_UNIQUE | 2 | `data_cancelamento` |
| `contrato_regra_suspensao_idx` | NON_UNIQUE | 1 | `id_regra_suspensao` |
| `contrato_status_idx` | NON_UNIQUE | 1 | `status` |
| `contrato_unidade_atendimento_idx` | NON_UNIQUE | 1 | `unidade_atendimento` |
| `contrato_vencimento_idx` | NON_UNIQUE | 1 | `id_vencimento` |
| `ix_tbl_contrato_01` | NON_UNIQUE | 1 | `integracao_status` |
| `ix_tbl_contrato_02` | NON_UNIQUE | 1 | `telefone` |
| `ix_tbl_contrato_03` | NON_UNIQUE | 1 | `status` |
| `ix_tbl_contrato_03` | NON_UNIQUE | 2 | `unidade_atendimento` |
| `ix_tbl_contrato_03` | NON_UNIQUE | 3 | `id` |
| `ix_tbl_contrato_04` | NON_UNIQUE | 1 | `legado_id` |
| `ix_tbl_contrato_05` | NON_UNIQUE | 1 | `id` |
| `ix_tbl_contrato_05` | NON_UNIQUE | 2 | `versao` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `UK_tbl_contrato_01` | UNIQUE | 1 | `legado_sistema` |
| `UK_tbl_contrato_01` | UNIQUE | 2 | `legado_id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_contrato_campanha`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `id_campanha` | `bigint(20)` | NO | MUL | `` |  |  |
| 4 | `recorrencia_vigencia` | `date` | YES |  | `` |  |  |
| 5 | `cancelada` | `tinyint(1)` | NO |  | `` |  |  |
| 6 | `pacote_up_codigo` | `varchar(12)` | YES |  | `` |  |  |
| 7 | `pacote_up_nome` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `pacote_up_vigencia` | `date` | YES |  | `` |  |  |
| 9 | `id_venda` | `bigint(20)` | YES | MUL | `` |  |  |
| 10 | `recorrencia_percentual_desconto` | `decimal(10,4)` | YES |  | `` |  |  |
| 11 | `recorrencia_meses_desconto` | `int(11)` | YES |  | `` |  |  |
| 12 | `pacote_up_meses_desconto` | `int(11)` | YES |  | `` |  |  |
| 13 | `instalacao_item_codigo` | `varchar(12)` | YES |  | `` |  |  |
| 14 | `instalacao_item_nome` | `varchar(60)` | YES |  | `` |  |  |
| 15 | `instalacao_empresa_nome` | `varchar(255)` | YES |  | `` |  |  |
| 16 | `instalacao_empresa_cnpj` | `varchar(16)` | YES |  | `` |  |  |
| 17 | `instalacao_quantidade_parcela` | `int(11)` | YES |  | `` |  |  |
| 18 | `instalacao_valor` | `decimal(10,2)` | YES |  | `` |  |  |
| 19 | `instalacao_desconto_percentual` | `decimal(10,2)` | YES |  | `` |  |  |
| 20 | `recorrencia_desconto_aplicado` | `tinyint(1)` | NO |  | `0` |  |  |
| 21 | `recorrencia_desconto_data_venda` | `tinyint(1)` | NO |  | `0` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_campanha_campanha_idx` | NON_UNIQUE | 1 | `id_campanha` |
| `contrato_campanha_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `fk_contrato_campanha_campanha` | NON_UNIQUE | 1 | `id_campanha` |
| `fk_contrato_campanha_contrato` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_contrato_campanha_tbl_venda_index` | NON_UNIQUE | 1 | `id_venda` |
| `tbl_contratp_campanha_tbl_venda_fk` | NON_UNIQUE | 1 | `id_venda` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_contrato_campanha_campanha` | `id_campanha` | `tbl_campanha` | `id` |
| `fk_contrato_campanha_contrato` | `id_contrato` | `tbl_contrato` | `id` |
| `tbl_contratp_campanha_tbl_venda_fk` | `id_venda` | `tbl_venda` | `id` |

## `tbl_contrato_dia_utilizacao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `pacote` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `ano` | `int(11)` | NO |  | `` |  |  |
| 5 | `mes` | `int(11)` | NO |  | `` |  |  |
| 6 | `qtd_dias` | `int(11)` | NO |  | `` |  |  |
| 7 | `inicio` | `date` | NO |  | `` |  |  |
| 8 | `fim` | `date` | NO |  | `` |  |  |
| 9 | `ciclo` | `int(11)` | NO | MUL | `` |  |  |
| 10 | `valor` | `decimal(16,4)` | NO |  | `` |  |  |
| 11 | `desconto` | `decimal(16,4)` | NO |  | `` |  |  |
| 12 | `classificacao` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `qtd_dias_periodo` | `int(11)` | YES |  | `` |  |  |
| 14 | `ultima_campanha` | `varchar(255)` | YES |  | `` |  |  |
| 15 | `ativacao` | `date` | YES |  | `` |  |  |
| 16 | `valor_contrato` | `decimal(16,4)` | YES |  | `` |  |  |
| 17 | `valor_adicionais` | `decimal(16,4)` | YES |  | `` |  |  |
| 18 | `desconto_validade` | `date` | YES |  | `` |  |  |
| 19 | `desconto_qtd_dias` | `int(11)` | YES |  | `` |  |  |
| 20 | `desconto_valor_dia` | `decimal(16,4)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `ix_tbl_contrato_dia_utilizacao_01` | NON_UNIQUE | 1 | `ciclo` |
| `ix_tbl_contrato_dia_utilizacao_01` | NON_UNIQUE | 2 | `ano` |
| `ix_tbl_contrato_dia_utilizacao_01` | NON_UNIQUE | 3 | `mes` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_contrato_dia_utilizacao_id_contrato_index` | NON_UNIQUE | 1 | `id_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_contrato_dia_utilizacao_2019`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO |  | `` |  |  |
| 3 | `pacote` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `ano` | `int(11)` | NO |  | `` |  |  |
| 5 | `mes` | `int(11)` | NO |  | `` |  |  |
| 6 | `qtd_dias` | `int(11)` | NO |  | `` |  |  |
| 7 | `inicio` | `date` | NO |  | `` |  |  |
| 8 | `fim` | `date` | NO |  | `` |  |  |
| 9 | `ciclo` | `int(11)` | NO |  | `` |  |  |
| 10 | `valor` | `decimal(16,4)` | NO |  | `` |  |  |
| 11 | `desconto` | `decimal(16,4)` | NO |  | `` |  |  |
| 12 | `classificacao` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `qtd_dias_periodo` | `int(11)` | YES |  | `` |  |  |
| 14 | `ultima_campanha` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_contrato_dia_utilizacao_provisao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `pacote` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `ano` | `int(11)` | NO |  | `` |  |  |
| 5 | `mes` | `int(11)` | NO |  | `` |  |  |
| 6 | `qtd_dias` | `int(11)` | NO |  | `` |  |  |
| 7 | `inicio` | `date` | NO |  | `` |  |  |
| 8 | `fim` | `date` | NO |  | `` |  |  |
| 9 | `ciclo` | `int(11)` | NO |  | `` |  |  |
| 10 | `valor` | `decimal(16,4)` | NO |  | `` |  |  |
| 11 | `desconto` | `decimal(16,4)` | NO |  | `` |  |  |
| 12 | `classificacao` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `qtd_dias_periodo` | `int(11)` | YES |  | `` |  |  |
| 14 | `ultima_campanha` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_contrato_dia_utilizacao_provisao_id_contrato_index` | NON_UNIQUE | 1 | `id_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_contrato_entrega`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO | MUL | `` |  |  |
| 7 | `codigo` | `varchar(20)` | NO | UNI | `` |  |  |
| 8 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 9 | `id_endereco` | `bigint(20)` | NO | MUL | `` |  |  |
| 10 | `area` | `int(11)` | YES |  | `` |  |  |
| 11 | `caixa` | `int(11)` | YES |  | `` |  |  |
| 12 | `porta` | `varchar(2)` | YES |  | `` |  |  |
| 13 | `serial_onu` | `varchar(45)` | YES |  | `` |  |  |
| 14 | `instalado` | `tinyint(1)` | NO |  | `` |  |  |
| 15 | `data_ativacao` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `codigo_UNIQUE` | UNIQUE | 1 | `codigo` |
| `contrato_entrega_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `contrato_entrega_endereco_idx` | NON_UNIQUE | 1 | `id_endereco` |
| `contrato_entrega_excluido_idx` | NON_UNIQUE | 1 | `excluido` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_contrato_faturamento`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `versao_contrato` | `int(11)` | NO |  | `` |  |  |
| 4 | `ano_referencia` | `int(4)` | NO |  | `` |  |  |
| 5 | `mes_referencia` | `int(2)` | NO |  | `` |  |  |
| 6 | `dia_fechamento` | `int(2)` | NO |  | `` |  |  |
| 7 | `dia_vencimento` | `int(2)` | NO |  | `` |  |  |
| 8 | `data_esboco_validado` | `datetime` | YES |  | `` |  |  |
| 9 | `esboco_gerado` | `tinyint(1)` | YES |  | `` |  |  |
| 10 | `esboco_codigo` | `bigint(20)` | YES |  | `` |  |  |
| 11 | `data_fim_medicao_excedente` | `datetime` | YES |  | `` |  |  |
| 12 | `valor_excedente` | `decimal(10,2)` | YES |  | `` |  |  |
| 13 | `data_integracao_contrato_sap` | `datetime` | YES |  | `` |  |  |
| 14 | `data_nota_fatura_criacao` | `datetime` | YES |  | `` |  |  |
| 15 | `nota_fatura_docentry` | `bigint(20)` | YES |  | `` |  |  |
| 16 | `boleto_valor` | `decimal(10,2)` | YES |  | `` |  |  |
| 17 | `data_boleto_gerado` | `datetime` | YES |  | `` |  |  |
| 18 | `data_boleto_remessa` | `datetime` | YES |  | `` |  |  |
| 19 | `data_boleto_confirmado` | `datetime` | YES |  | `` |  |  |
| 20 | `data_boleto_cancelado` | `datetime` | YES |  | `` |  |  |
| 21 | `data_boleto_rejeitado` | `datetime` | YES |  | `` |  |  |
| 22 | `data_nota_fiscal_criacao` | `datetime` | YES |  | `` |  |  |
| 23 | `data_faturamento_concluido` | `datetime` | YES |  | `` |  |  |
| 24 | `faturamento_status` | `varchar(20)` | NO |  | `` |  |  |
| 25 | `motivo_falha` | `text` | YES |  | `` |  |  |
| 26 | `possui_servico_telefonia` | `tinyint(1)` | NO |  | `` |  |  |
| 27 | `vsc_ctrl_number` | `int(11)` | YES |  | `` |  |  |
| 28 | `email_enviado` | `tinyint(1)` | NO |  | `0` |  |  |
| 29 | `data_boleto_baixado` | `datetime` | YES |  | `` |  |  |
| 30 | `nota_fiscal_gerada` | `tinyint(1)` | NO |  | `0` |  |  |
| 31 | `valor_contrato` | `decimal(10,2)` | NO |  | `` |  |  |
| 32 | `valor_desconto` | `decimal(10,2)` | NO |  | `0.00` |  |  |
| 33 | `faturamento_manual` | `tinyint(1)` | NO |  | `0` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_faturamento_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_contrato_faturamento_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_contrato_forma_pagamento`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `codigo_forma_pagamento` | `varchar(50)` | NO |  | `` |  |  |
| 9 | `status` | `varchar(255)` | NO |  | `FP_PENDENTE_AUTORIZACAO` |  |  |
| 10 | `vigente` | `tinyint(1)` | NO |  | `` |  |  |
| 11 | `banco_nome` | `varchar(255)` | YES |  | `` |  |  |
| 12 | `banco_codigo` | `varchar(20)` | YES |  | `` |  |  |
| 13 | `agencia` | `varchar(20)` | YES |  | `` |  |  |
| 14 | `conta_corrente` | `varchar(20)` | YES |  | `` |  |  |
| 15 | `integracao_status` | `varchar(20)` | NO |  | `NOVO` |  |  |
| 16 | `integracao_mensagem` | `varchar(255)` | YES |  | `` |  |  |
| 17 | `integracao_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 18 | `integracao_transacao` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `idx_contrato_forma_pagamento` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_contrato_forma_pagamento_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_contrato_hero`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_associacao` | `datetime` | YES |  | `` |  |  |
| 3 | `data_ativacao` | `datetime` | YES |  | `` |  |  |
| 4 | `licenca_hero` | `varchar(255)` | NO |  | `` |  |  |
| 5 | `codigo_pacote` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `id_contrato` | `bigint(20)` | YES | UNI | `` |  |  |
| 7 | `em_tratamento` | `tinyint(1)` | NO |  | `0` |  |  |
| 8 | `valida` | `tinyint(1)` | NO |  | `1` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `id_contrato_UNIQUE` | UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_contrato_hero_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_contrato_historico_reserva`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data` | `datetime` | NO |  | `` |  |  |
| 3 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 4 | `id_reserva` | `bigint(20)` | NO | MUL | `` |  |  |
| 5 | `id_ponto` | `bigint(20)` | NO | MUL | `` |  |  |
| 6 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_contrato_historico_reserva_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `tbl_contrato_historico_reserva_ponto_idx` | NON_UNIQUE | 1 | `id_ponto` |
| `tbl_contrato_historico_reserva_reserva_idx` | NON_UNIQUE | 1 | `id_reserva` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_contrato_historico_reserva_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_contrato_item`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_contrato_produto` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `valor_unitario` | `decimal(10,4)` | NO |  | `` |  |  |
| 9 | `valor_base` | `decimal(10,4)` | NO |  | `` |  |  |
| 10 | `quantidade` | `int(11)` | NO |  | `` |  |  |
| 11 | `valor_final` | `decimal(10,4)` | NO |  | `` |  |  |
| 12 | `item_codigo` | `varchar(255)` | NO | MUL | `` |  |  |
| 13 | `item_nome` | `varchar(255)` | NO |  | `` |  |  |
| 14 | `empresa_cnpj` | `varchar(16)` | NO |  | `` |  |  |
| 15 | `empresa_nome` | `varchar(60)` | NO |  | `` |  |  |
| 16 | `regra_desconto` | `int(11)` | YES |  | `` |  |  |
| 17 | `valor_unitario_sap` | `decimal(10,4)` | YES |  | `` |  |  |
| 18 | `indice_reajuste_sap` | `decimal(10,4)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_item_contrato_produto` | NON_UNIQUE | 1 | `id_contrato_produto` |
| `contrato_item_id_contrato_produto_excluido_idx` | NON_UNIQUE | 1 | `id_contrato_produto` |
| `contrato_item_id_contrato_produto_excluido_idx` | NON_UNIQUE | 2 | `excluido` |
| `fk_contrato_item_contrato_produto` | NON_UNIQUE | 1 | `id_contrato_produto` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_contrato_item_item_codigo_index` | NON_UNIQUE | 1 | `item_codigo` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_contrato_item_contrato_produto` | `id_contrato_produto` | `tbl_contrato_produto` | `id` |

## `tbl_contrato_migracao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_venda` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 4 | `antigo_pacote_codigo` | `varchar(255)` | NO |  | `` |  |  |
| 5 | `antigo_pacote_nome` | `varchar(255)` | NO |  | `` |  |  |
| 6 | `antigo_valor` | `decimal(10,2)` | NO |  | `` |  |  |
| 7 | `antigo_versao` | `int(11)` | NO |  | `` |  |  |
| 8 | `novo_pacote_codigo` | `varchar(255)` | NO |  | `` |  |  |
| 9 | `novo_pacote_nome` | `varchar(255)` | NO |  | `` |  |  |
| 10 | `novo_valor` | `decimal(10,2)` | NO |  | `` |  |  |
| 11 | `novo_versao` | `int(11)` | NO |  | `` |  |  |
| 12 | `reprovada` | `tinyint(1)` | NO |  | `0` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_migracao_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `contrato_migracao_venda_idx` | NON_UNIQUE | 1 | `id_venda` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_contrato_onu_aviso`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `aviso_data` | `datetime` | YES |  | `` |  |  |
| 3 | `aviso_descricao` | `text` | YES |  | `` |  |  |
| 4 | `onu_serial` | `varchar(255)` | NO | MUL | `` |  |  |
| 5 | `onu_olt` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `onu_slot` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `onu_pon` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `onu_index` | `varchar(255)` | YES |  | `` |  |  |
| 9 | `onu_rx_power` | `varchar(255)` | YES |  | `` |  |  |
| 10 | `onu_descricao` | `text` | YES |  | `` |  |  |
| 11 | `id_contrato` | `bigint(20)` | YES | UNI | `` |  |  |
| 12 | `id_problema` | `varchar(100)` | YES | MUL | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_onu_aviso_id_problema_idx` | NON_UNIQUE | 1 | `id_problema` |
| `contrato_onu_aviso_onu_serial_idx` | NON_UNIQUE | 1 | `onu_serial` |
| `id_contrato_UNIQUE` | UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_contrato_onu_aviso` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_contrato_produto`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `versao_contrato` | `int(11)` | NO | MUL | `` |  |  |
| 9 | `item_codigo` | `varchar(255)` | NO | MUL | `` |  |  |
| 10 | `item_nome` | `varchar(255)` | NO |  | `` |  |  |
| 11 | `item_grupo` | `varchar(60)` | NO |  | `` |  |  |
| 12 | `data_instalacao` | `datetime` | YES |  | `` |  |  |
| 13 | `data_cancelamento` | `datetime` | YES |  | `` |  |  |
| 14 | `adicional` | `tinyint(1)` | NO | MUL | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_produto_contrato_excluido_adicional_versao` | NON_UNIQUE | 1 | `versao_contrato` |
| `contrato_produto_contrato_excluido_adicional_versao` | NON_UNIQUE | 2 | `excluido` |
| `contrato_produto_contrato_excluido_adicional_versao` | NON_UNIQUE | 3 | `adicional` |
| `contrato_produto_contrato_excluido_adicional_versao` | NON_UNIQUE | 4 | `id_contrato` |
| `contrato_produto_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `fk_contrato_produto_contrato` | NON_UNIQUE | 1 | `id_contrato` |
| `ix_tbl_contrato_produto_01` | NON_UNIQUE | 1 | `item_codigo` |
| `ix_tbl_contrato_produto_02` | NON_UNIQUE | 1 | `adicional` |
| `ix_tbl_contrato_produto_02` | NON_UNIQUE | 2 | `excluido` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_contrato_produto_versao_contrato_index` | NON_UNIQUE | 1 | `versao_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_contrato_produto_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_contrato_reajuste`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `data_processamento` | `datetime` | NO |  | `` |  |  |
| 4 | `valor_anterior` | `decimal(10,2)` | NO |  | `` |  |  |
| 5 | `valor_indice` | `decimal(10,4)` | NO |  | `` |  |  |
| 6 | `valor_final` | `decimal(10,2)` | NO |  | `` |  |  |
| 7 | `versao_contrato` | `int(11)` | NO |  | `` |  |  |
| 8 | `data_primeira_consulta` | `datetime` | YES |  | `` |  |  |
| 9 | `data_segunda_consulta` | `datetime` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_reajuste_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_contrato_reajuste_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_contrato_retencao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `quantidade_contato` | `int(11)` | NO |  | `0` |  |  |
| 9 | `status` | `varchar(255)` | NO |  | `RT_NOVO` |  |  |
| 10 | `usuario_atribuido` | `varchar(10)` | YES |  | `` |  |  |
| 11 | `motivo_solicitacao` | `varchar(255)` | NO |  | `` |  |  |
| 12 | `oferta_incentivo` | `tinyint(1)` | NO |  | `` |  |  |
| 13 | `setor_origem` | `varchar(255)` | NO |  | `` |  |  |
| 14 | `observacao` | `text` | YES |  | `` |  |  |
| 15 | `motivo_investigado` | `varchar(255)` | YES |  | `` |  |  |
| 16 | `data_reversao_cancelamento` | `datetime` | YES |  | `` |  |  |
| 17 | `id_contrato_migracao` | `bigint(20)` | YES | MUL | `` |  |  |
| 18 | `desconto_aplicado` | `decimal(10,2)` | YES |  | `` |  |  |
| 19 | `sub_motivo_cancelamento` | `varchar(255)` | YES |  | `` |  |  |
| 20 | `origem_contato` | `varchar(10)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `retencao_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `retencao_contrato_migracao_idx` | NON_UNIQUE | 1 | `id_contrato_migracao` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_contrato_retencao_contato`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_contato_retencao` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `telefone` | `varchar(255)` | YES |  | `` |  |  |
| 9 | `descricao` | `text` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contato_retencao_idx` | NON_UNIQUE | 1 | `id_contato_retencao` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_contato_retencao` | `id_contato_retencao` | `tbl_contrato_retencao` | `id` |

## `tbl_contrato_suspensao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `data_suspensao` | `date` | NO |  | `` |  |  |
| 4 | `data_ativacao` | `date` | YES |  | `` |  |  |
| 5 | `dias_desconto_faturamento` | `int(11)` | NO |  | `` |  |  |
| 6 | `dias_suspenso` | `int(11)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_suspensao_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_contrato_suspensao_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_contrato_suspensao_blacklist`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | UNI | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_contrato_suspensao_blacklist_id_contrato_index` | NON_UNIQUE | 1 | `id_contrato` |
| `tbl_contrato_suspensao_blacklist_id_contrato_uindex` | UNIQUE | 1 | `id_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_contrato_suspensao_tarefa`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `data_suspensao` | `date` | NO |  | `` |  |  |
| 4 | `status` | `varchar(255)` | NO |  | `ST_CONT_NAO_INTEGRADO` |  |  |
| 5 | `integracao_retorno` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `fk_contrato_suspensao_tarefa_contrato` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_contrato_suspensao_tarefa_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_contrato_sydle`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `codigo_sydle` | `bigint(20)` | YES |  | `` |  |  |
| 2 | `codigo_air` | `bigint(20)` | YES |  | `` |  |  |
| 3 | `id` | `tinytext` | YES |  | `` |  |  |
| 4 | `id_cliente` | `tinytext` | YES |  | `` |  |  |
| 5 | `cliente` | `tinytext` | YES |  | `` |  |  |
| 6 | `id_plano` | `tinytext` | YES |  | `` |  |  |
| 7 | `plano` | `tinytext` | YES |  | `` |  |  |
| 8 | `status_faturamento` | `tinytext` | YES |  | `` |  |  |
| 9 | `status_servico` | `tinytext` | YES |  | `` |  |  |
| 10 | `ciclo` | `bigint(20)` | YES |  | `` |  |  |
| 11 | `vencimento` | `bigint(20)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_contrato_termo_central_assinante`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_aceite_termo` | `datetime` | NO |  | `` |  |  |
| 3 | `versao_termo` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_termo_central_assinante_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_contrato_termo_central_assinante_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_desconto`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `2024-07-17 12:00:00` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `AIR00015` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `2024-07-17 12:00:00` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `AIR0001` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `0` |  |  |
| 7 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `desconto` | `decimal(19,4)` | NO |  | `` |  |  |
| 9 | `data_validade` | `date` | NO | MUL | `2050-01-01` |  |  |
| 10 | `dia_aplicar` | `date` | NO |  | `2024-03-01` |  |  |
| 11 | `item_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 12 | `item_nome` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `tipo` | `varchar(20)` | NO |  | `PERCENTUAL` |  |  |
| 14 | `categoria` | `varchar(20)` | YES |  | `AJUSTE_COMERCIAL` |  |  |
| 15 | `observacao` | `varchar(255)` | YES |  | `AJUS VALORES B2B` |  |  |
| 16 | `id_desconto_sydle` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_desconto_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `tbl_desconto_data_exc_idx` | NON_UNIQUE | 1 | `data_validade` |
| `tbl_desconto_data_exc_idx` | NON_UNIQUE | 2 | `excluido` |
| `tbl_desconto_data_idx` | NON_UNIQUE | 1 | `data_validade` |
| `tbl_desconto_data_idx` | NON_UNIQUE | 2 | `excluido` |
| `tbl_desconto_data_idx` | NON_UNIQUE | 3 | `categoria` |
| `tbl_desconto_data_idx` | NON_UNIQUE | 4 | `usuario_criacao` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_endereco`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO | MUL | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO | MUL | `` |  |  |
| 7 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `id_logradouro` | `bigint(20)` | YES | MUL | `` |  |  |
| 9 | `codigo` | `varchar(40)` | YES | MUL | `` |  |  |
| 10 | `numero` | `varchar(255)` | NO |  | `` |  |  |
| 11 | `complemento` | `varchar(255)` | YES |  | `` |  |  |
| 12 | `referencia` | `varchar(255)` | NO |  | `` |  |  |
| 13 | `latitude` | `decimal(10,8)` | YES |  | `` |  |  |
| 14 | `longitude` | `decimal(10,8)` | YES |  | `` |  |  |
| 15 | `unidade` | `varchar(10)` | NO |  | `` |  |  |
| 16 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |
| 17 | `legado_id` | `bigint(20)` | YES |  | `` |  |  |
| 18 | `legado_sistema` | `varchar(20)` | YES |  | `` |  |  |
| 19 | `codigo_sap` | `varchar(45)` | YES |  | `` |  |  |
| 20 | `viabilidade_autorizada` | `tinyint(1)` | NO |  | `` |  |  |
| 21 | `viabilidade_usuario` | `varchar(10)` | YES |  | `` |  |  |
| 22 | `viabilidade_data` | `datetime` | YES |  | `` |  |  |
| 23 | `viabilidade_justificativa` | `text` | YES |  | `` |  |  |
| 24 | `logradouro_tipo` | `varchar(255)` | YES |  | `` |  |  |
| 25 | `logradouro` | `varchar(255)` | YES |  | `` |  |  |
| 26 | `bairro` | `varchar(255)` | YES |  | `` |  |  |
| 27 | `cep` | `varchar(12)` | YES |  | `` |  |  |
| 28 | `id_cidade` | `bigint(20)` | YES | MUL | `` |  |  |
| 29 | `integracao_status_estoque` | `varchar(20)` | NO |  | `NOVO` |  |  |
| 30 | `integracao_mensagem_estoque` | `varchar(255)` | YES |  | `` |  |  |
| 31 | `integracao_codigo_estoque` | `varchar(255)` | YES |  | `` |  |  |
| 32 | `integracao_transacao_estoque` | `varchar(255)` | YES |  | `` |  |  |
| 33 | `certificado` | `tinyint(1)` | YES |  | `0` |  |  |
| 34 | `verificado` | `tinyint(1)` | YES |  | `0` |  |  |
| 35 | `completo` | `varchar(255)` | YES |  | `` |  |  |
| 36 | `ftta` | `tinyint(1)` | NO |  | `0` |  |  |
| 37 | `id_condominio` | `bigint(20)` | YES |  | `` |  |  |
| 38 | `google_maps_resposta` | `text` | YES |  | `` |  |  |
| 39 | `google_maps_status` | `varchar(100)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `codigo_idx` | NON_UNIQUE | 1 | `codigo` |
| `endereco_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `endereco_logradouro_idx` | NON_UNIQUE | 1 | `id_logradouro` |
| `fk_endereco_cliente` | NON_UNIQUE | 1 | `id_cliente` |
| `fk_endereco_logradouro` | NON_UNIQUE | 1 | `id_logradouro` |
| `idx` | NON_UNIQUE | 1 | `excluido` |
| `ix_tbl_endereco_01` | NON_UNIQUE | 1 | `data_criacao` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_endereco_cidade_fk` | NON_UNIQUE | 1 | `id_cidade` |
| `tbl_endereco_cidade_index` | NON_UNIQUE | 1 | `id_cidade` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_endereco_cliente` | `id_cliente` | `tbl_cliente` | `id` |
| `fk_endereco_logradouro` | `id_logradouro` | `tbl_endereco_logradouro` | `id` |
| `tbl_endereco_cidade_fk` | `id_cidade` | `tbl_endereco_cidade` | `id` |

## `tbl_endereco_bairro`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_cidade` | `bigint(20)` | YES | MUL | `` |  |  |
| 8 | `nome` | `varchar(60)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `bairro_cidade_idx` | NON_UNIQUE | 1 | `id_cidade` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_bairro_cidade` | `id_cidade` | `tbl_endereco_cidade` | `id` |

## `tbl_endereco_cidade`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `nome` | `varchar(60)` | NO |  | `` |  |  |
| 8 | `estado` | `varchar(2)` | NO |  | `` |  |  |
| 9 | `codigo_ibge` | `int(11)` | NO |  | `` |  |  |
| 10 | `ddd` | `int(11)` | NO |  | `` |  |  |
| 11 | `atendida` | `tinyint(1)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_endereco_cidade_unidade`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_cidade` | `bigint(20)` | NO | MUL | `` |  |  |
| 2 | `unidades` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `endereco_cidade_unidade_idx` | NON_UNIQUE | 1 | `id_cidade` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_endereco_cidade_unidade` | `id_cidade` | `tbl_endereco_cidade` | `id` |

## `tbl_endereco_estado`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `uf` | `varchar(2)` | NO | UNI | `` |  |  |
| 3 | `nome` | `varchar(255)` | NO |  | `` |  |  |
| 4 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `uf` | UNIQUE | 1 | `uf` |
| `uf_idx` | NON_UNIQUE | 1 | `uf` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_endereco_logradouro`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_bairro` | `bigint(20)` | YES | MUL | `` |  |  |
| 8 | `tipo` | `varchar(45)` | NO |  | `` |  |  |
| 9 | `nome` | `varchar(255)` | NO |  | `` |  |  |
| 10 | `cep` | `varchar(10)` | NO |  | `` |  |  |
| 11 | `qtd_pon_disponivel` | `int(11)` | NO |  | `` |  |  |
| 12 | `qtd_pon_ocupada` | `int(11)` | NO |  | `` |  |  |
| 13 | `atendido` | `tinyint(1)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `logradouro_bairro_idx` | NON_UNIQUE | 1 | `id_bairro` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_logradouro_bairro` | `id_bairro` | `tbl_endereco_bairro` | `id` |

## `tbl_eventos_site`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `id_cliente` | `bigint(20)` | NO |  | `` |  |  |
| 4 | `tipo_evento` | `varchar(35)` | NO |  | `` |  |  |
| 5 | `valor_alterado` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_habilitar_confianca`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | UNI | `` |  |  |
| 3 | `saldo` | `int(11)` | NO |  | `` |  |  |
| 4 | `canal` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `habilitar_confianca_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `id_contrato_UNIQUE` | UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_habilitar_confianca_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_historico_vencimento`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `id_vencimento` | `bigint(20)` | NO |  | `` |  |  |
| 4 | `data_alteracao_vencimento` | `datetime` | NO |  | `` |  |  |
| 5 | `id_vencimento_anterior` | `bigint(20)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `ix_historicovencimento_idcontrato` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_historico_viabilidades_venda`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `momento` | `datetime` | NO |  | `` |  |  |
| 3 | `id_lead` | `bigint(20)` | YES | MUL | `` |  |  |
| 4 | `id_venda` | `bigint(20)` | YES | MUL | `` |  |  |
| 5 | `id_contrato` | `bigint(20)` | YES | MUL | `` |  |  |
| 6 | `bloqueio_ativo` | `tinyint(1)` | NO |  | `0` |  |  |
| 7 | `id_viabilidade_cm` | `bigint(20)` | NO |  | `` |  |  |
| 8 | `resultado_viabilidade` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `fk_tbl_historico_viabilidades_venda_contrato` | NON_UNIQUE | 1 | `id_contrato` |
| `fk_tbl_historico_viabilidades_venda_lead` | NON_UNIQUE | 1 | `id_lead` |
| `fk_tbl_historico_viabilidades_venda_venda` | NON_UNIQUE | 1 | `id_venda` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_historico_viabilidades_venda_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `tbl_historico_viabilidades_venda_lead_idx` | NON_UNIQUE | 1 | `id_lead` |
| `tbl_historico_viabilidades_venda_venda_idx` | NON_UNIQUE | 1 | `id_venda` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_historico_viabilidades_venda_contrato` | `id_contrato` | `tbl_contrato` | `id` |
| `fk_tbl_historico_viabilidades_venda_lead` | `id_lead` | `tbl_lead` | `id` |
| `fk_tbl_historico_viabilidades_venda_venda` | `id_venda` | `tbl_venda` | `id` |

## `tbl_lead`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `tipo` | `varchar(20)` | NO |  | `` |  |  |
| 8 | `id_carteira` | `bigint(20)` | YES | MUL | `` |  |  |
| 9 | `id_cliente` | `bigint(20)` | YES | UNI | `` |  |  |
| 10 | `nome` | `varchar(100)` | NO |  | `` |  |  |
| 11 | `telefone` | `varchar(20)` | NO |  | `` |  |  |
| 12 | `email` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `email_status` | `varchar(45)` | YES |  | `` |  |  |
| 14 | `end_id_cidade` | `bigint(20)` | YES | MUL | `` |  |  |
| 15 | `end_cidade_nome` | `varchar(255)` | YES |  | `` |  |  |
| 16 | `end_unidade` | `varchar(20)` | YES |  | `` |  |  |
| 17 | `end_cod_ibge` | `int(11)` | YES |  | `` |  |  |
| 18 | `end_id_bairro` | `bigint(20)` | YES | MUL | `` |  |  |
| 19 | `end_bairro_nome` | `varchar(255)` | YES |  | `` |  |  |
| 20 | `end_tipo_logradouro` | `varchar(50)` | YES |  | `` |  |  |
| 21 | `end_id_logradouro` | `bigint(20)` | YES | MUL | `` |  |  |
| 22 | `end_logradouro_nome` | `varchar(255)` | YES |  | `` |  |  |
| 23 | `end_cep` | `varchar(10)` | YES |  | `` |  |  |
| 24 | `end_referencia` | `varchar(255)` | YES |  | `` |  |  |
| 25 | `end_complemento` | `varchar(255)` | YES |  | `` |  |  |
| 26 | `end_numero` | `varchar(10)` | YES |  | `` |  |  |
| 27 | `end_latitude` | `decimal(10,8)` | YES |  | `` |  |  |
| 28 | `end_longitude` | `decimal(10,8)` | YES |  | `` |  |  |
| 29 | `cpf_cnpj` | `varchar(18)` | YES | UNI | `` |  |  |
| 30 | `pf_data_nascimento` | `date` | YES |  | `` |  |  |
| 31 | `pf_tratamento` | `varchar(50)` | YES |  | `` |  |  |
| 32 | `pf_estado_civil` | `varchar(15)` | YES |  | `` |  |  |
| 33 | `pf_rg_numero` | `varchar(255)` | YES |  | `` |  |  |
| 34 | `pf_rg_orgao` | `varchar(255)` | YES |  | `` |  |  |
| 35 | `pj_nome_fantasia` | `varchar(255)` | YES |  | `` |  |  |
| 36 | `pj_inscricao_estadual` | `varchar(50)` | YES |  | `` |  |  |
| 37 | `pj_inscricao_municipal` | `varchar(50)` | YES |  | `` |  |  |
| 38 | `pj_atividade_principal` | `varchar(255)` | YES |  | `` |  |  |
| 39 | `legado_id` | `bigint(20)` | YES |  | `` |  |  |
| 40 | `legado_sistema` | `varchar(20)` | YES |  | `` |  |  |
| 41 | `data_validade_carteira` | `date` | YES |  | `` |  |  |
| 42 | `fonte` | `varchar(50)` | YES |  | `` |  |  |
| 43 | `nivel_interesse` | `int(11)` | YES |  | `` |  |  |
| 44 | `grupo` | `varchar(50)` | YES |  | `` |  |  |
| 45 | `telefone_adicional` | `varchar(255)` | YES |  | `` |  |  |
| 46 | `email_adicional` | `varchar(255)` | YES |  | `` |  |  |
| 47 | `email_adicional_status` | `varchar(45)` | YES |  | `` |  |  |
| 48 | `senha_sac` | `varchar(255)` | YES |  | `` |  |  |
| 49 | `site` | `varchar(255)` | YES |  | `` |  |  |
| 50 | `twitter` | `varchar(255)` | YES |  | `` |  |  |
| 51 | `facebook` | `varchar(255)` | YES |  | `` |  |  |
| 52 | `concorrentes` | `varchar(255)` | YES |  | `` |  |  |
| 53 | `interesses` | `varchar(255)` | YES |  | `` |  |  |
| 54 | `qualificacao` | `varchar(255)` | NO |  | `LQ_NOVO` |  |  |
| 55 | `pf_nome_pai` | `varchar(255)` | YES |  | `` |  |  |
| 56 | `pf_nome_mae` | `varchar(255)` | YES |  | `` |  |  |
| 57 | `pf_sexo` | `varchar(255)` | YES |  | `` |  |  |
| 58 | `pf_profissao` | `varchar(255)` | YES |  | `` |  |  |
| 59 | `condominio_nome` | `varchar(255)` | YES |  | `` |  |  |
| 60 | `condominio_qtd_apto` | `int(11)` | YES |  | `` |  |  |
| 61 | `observacao` | `text` | YES |  | `` |  |  |
| 62 | `credito_autorizado` | `tinyint(1)` | NO |  | `0` |  |  |
| 63 | `viabilidade_autorizada` | `tinyint(1)` | NO |  | `0` |  |  |
| 64 | `viabilidade_usuario` | `varchar(10)` | YES |  | `` |  |  |
| 65 | `viabilidade_data` | `datetime` | YES |  | `` |  |  |
| 66 | `viabilidade_justificativa` | `text` | YES |  | `` |  |  |
| 67 | `tipo_residencia` | `varchar(255)` | YES |  | `` |  |  |
| 68 | `id_condominio` | `bigint(20)` | YES | MUL | `` |  |  |
| 69 | `bloco` | `varchar(50)` | YES |  | `` |  |  |
| 70 | `apartamento` | `varchar(50)` | YES |  | `` |  |  |
| 71 | `end_certificado` | `tinyint(1)` | YES |  | `0` |  |  |
| 72 | `end_verificado` | `tinyint(1)` | YES |  | `0` |  |  |
| 73 | `end_completo` | `varchar(255)` | YES |  | `` |  |  |
| 74 | `uuid_lead_rd_station` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `id_cliente_UNIQUE` | UNIQUE | 1 | `id_cliente` |
| `lead_bairro_idx` | NON_UNIQUE | 1 | `end_id_bairro` |
| `lead_carteira_idx` | NON_UNIQUE | 1 | `id_carteira` |
| `lead_cidade_idx` | NON_UNIQUE | 1 | `end_id_cidade` |
| `lead_cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `lead_logradouro_idx` | NON_UNIQUE | 1 | `end_id_logradouro` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_lead_condominio_index` | NON_UNIQUE | 1 | `id_condominio` |
| `tbl_lead_cpf_cnpj_uindex` | UNIQUE | 1 | `cpf_cnpj` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_lead_obs`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_lead` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `texto` | `text` | NO |  | `` |  |  |
| 9 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `lead_obs_lead_idx` | NON_UNIQUE | 1 | `id_lead` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_lead_obs_lead` | `id_lead` | `tbl_lead` | `id` |

## `tbl_marcador_contrato`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | UNI | `` |  |  |
| 3 | `marcador` | `varchar(255)` | YES | MUL | `` |  |  |
| 4 | `data_validade` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `marcador_idx` | NON_UNIQUE | 1 | `marcador` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `unique_id_contrato_index` | UNIQUE | 1 | `id_contrato` |
| `unique_id_contrato_marcador_index` | UNIQUE | 1 | `id_contrato` |
| `unique_id_contrato_marcador_index` | UNIQUE | 2 | `marcador` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_cliente_marcador_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tbl_mensagem_central`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_hora_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(100)` | YES |  | `` |  |  |
| 4 | `titulo` | `text` | NO |  | `` |  |  |
| 5 | `descricao` | `text` | YES |  | `` |  |  |
| 6 | `imagem_url` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `obrigatorio` | `tinyint(1)` | NO |  | `0` |  |  |
| 8 | `enviar_todos` | `tinyint(1)` | NO | MUL | `0` |  |  |
| 9 | `origem` | `enum('NOTIFICATION','MESSAGE')` | NO |  | `NOTIFICATION` |  |  |
| 10 | `usuario_criacao_email` | `varchar(255)` | NO |  | `` |  |  |
| 11 | `usuario_criacao_nome` | `varchar(255)` | NO |  | `` |  |  |
| 12 | `total_destinatarios` | `bigint(20)` | NO |  | `` |  |  |
| 13 | `total_leituras` | `bigint(20)` | YES |  | `0` |  |  |
| 14 | `lancamento_url` | `varchar(255)` | YES |  | `` |  |  |
| 15 | `marca` | `varchar(50)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `ix_msgcentral_enviartodos` | NON_UNIQUE | 1 | `enviar_todos` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_mensagem_usuario_central`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `id_mensagem` | `bigint(20)` | NO | MUL | `` |  |  |
| 4 | `visualizado` | `tinyint(1)` | NO |  | `0` |  |  |
| 5 | `excluido_pelo_cliente` | `tinyint(1)` | NO |  | `0` |  |  |
| 6 | `data_hora_leitura` | `datetime` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `ix_msgusrcentral_idcliente_excluido` | NON_UNIQUE | 1 | `id_cliente` |
| `ix_msgusrcentral_idcliente_excluido` | NON_UNIQUE | 2 | `excluido_pelo_cliente` |
| `ix_msgusrcentral_idcliente_idmensagem_excluido` | NON_UNIQUE | 1 | `id_cliente` |
| `ix_msgusrcentral_idcliente_idmensagem_excluido` | NON_UNIQUE | 2 | `id_mensagem` |
| `ix_msgusrcentral_idcliente_idmensagem_excluido` | NON_UNIQUE | 3 | `excluido_pelo_cliente` |
| `ix_msgusrcentral_idmensagem_idcliente` | NON_UNIQUE | 1 | `id_mensagem` |
| `ix_msgusrcentral_idmensagem_idcliente` | NON_UNIQUE | 2 | `id_cliente` |
| `mensagem_usuario` | UNIQUE | 1 | `id_cliente` |
| `mensagem_usuario` | UNIQUE | 2 | `id_mensagem` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_mensagem_central` | `id_mensagem` | `tbl_mensagem_central` | `id` |

## `tbl_outros_marcadores`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `marcador` | `varchar(255)` | YES | MUL | `ELEG_DIGITAL` |  |  |
| 4 | `data_validade` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `marcador_idx` | NON_UNIQUE | 1 | `marcador` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `unique_client_id_marcador_index` | UNIQUE | 1 | `id_cliente` |
| `unique_client_id_marcador_index` | UNIQUE | 2 | `marcador` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_perfilacao_cobranca`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `servico` | `varchar(255)` | NO |  | `` |  |  |
| 4 | `resultado_chamada` | `varchar(255)` | NO |  | `` |  |  |
| 5 | `motivo_nao_pagamento` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `aceitou_negociar` | `tinyint(1)` | YES |  | `` |  |  |
| 7 | `submotivo` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `observacao` | `varchar(255)` | YES |  | `` |  |  |
| 9 | `data_criacao` | `datetime` | NO |  | `CURRENT_TIMESTAMP` |  |  |
| 10 | `usuario_criacao` | `varchar(10)` | NO |  | `AIR0001` |  |  |
| 11 | `data_alteracao` | `datetime` | NO |  | `CURRENT_TIMESTAMP` |  |  |
| 12 | `usuario_alteracao` | `varchar(10)` | NO |  | `AIR0001` |  |  |
| 13 | `excluido` | `tinyint(4)` | NO |  | `0` |  |  |
| 14 | `id_chamado` | `bigint(20)` | YES |  | `` |  |  |
| 15 | `id_motivo` | `bigint(20)` | YES |  | `` |  |  |
| 16 | `negociacao` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_perfilacao_cobranca_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_perfilacao_comercial`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `fonte` | `varchar(255)` | NO |  | `` |  |  |
| 8 | `nome` | `varchar(255)` | NO |  | `` |  |  |
| 9 | `telefone` | `varchar(255)` | NO |  | `` |  |  |
| 10 | `cidade` | `varchar(255)` | NO |  | `` |  |  |
| 11 | `classificacao` | `varchar(255)` | NO |  | `` |  |  |
| 12 | `observacao` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_perfilacao_motivo`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `setor` | `varchar(255)` | NO |  | `` |  |  |
| 8 | `motivo` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_perfilacao_ouvidoria`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `CURRENT_TIMESTAMP` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `AIR0001` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `CURRENT_TIMESTAMP` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `AIR0001` |  |  |
| 6 | `excluido` | `tinyint(4)` | NO |  | `0` |  |  |
| 7 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `id_chamado` | `bigint(20)` | NO |  | `` |  |  |
| 9 | `id_motivo` | `bigint(20)` | NO | MUL | `` |  |  |
| 10 | `servico` | `varchar(255)` | NO |  | `` |  |  |
| 11 | `submotivo` | `varchar(255)` | NO |  | `` |  |  |
| 12 | `observacao` | `varchar(255)` | NO |  | `` |  |  |
| 13 | `protocolo` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `fk_tbl_perfilacao_ouvidoria_tbl_perfilacao_motivo` | NON_UNIQUE | 1 | `id_motivo` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `ttbl_perfilacao_ouvidoria_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_perfilacao_ouvidoria_tbl_perfilacao_motivo` | `id_motivo` | `tbl_perfilacao_motivo` | `id` |

## `tbl_perfilacao_retencao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `primeiro_nivel` | `varchar(255)` | NO |  | `` |  |  |
| 9 | `segundo_nivel` | `varchar(255)` | YES |  | `` |  |  |
| 10 | `motivo` | `varchar(255)` | NO |  | `` |  |  |
| 11 | `submotivo` | `varchar(255)` | NO |  | `` |  |  |
| 12 | `observacao` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `servico` | `varchar(255)` | NO |  | `` |  |  |
| 14 | `tipo_cliente` | `varchar(255)` | YES |  | `` |  |  |
| 15 | `origem_contato` | `varchar(10)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tbl_perfilacao_retencao_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_perfilacao_submotivo`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_motivo` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `submotivo` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `fk_tbl_perfilacao_submotivo_tbl_perfilacao_motivo` | NON_UNIQUE | 1 | `id_motivo` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_perfilacao_submotivo_tbl_perfilacao_motivo` | `id_motivo` | `tbl_perfilacao_motivo` | `id` |

## `tbl_regra_suspensao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `nome` | `varchar(45)` | NO | UNI | `` |  |  |
| 8 | `grupo_cliente` | `varchar(20)` | NO |  | `` |  |  |
| 9 | `dias_atraso` | `int(11)` | YES |  | `` |  |  |
| 10 | `ativo` | `tinyint(1)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `nome_UNIQUE` | UNIQUE | 1 | `nome` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_regra_suspensao_unidade`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_regra_suspensao` | `bigint(20)` | NO | MUL | `` |  |  |
| 2 | `unidades` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `regra_suspensao_unidade_regra_suspensao_idx` | NON_UNIQUE | 1 | `id_regra_suspensao` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_regra_suspensao_unidade_regra_suspensao` | `id_regra_suspensao` | `tbl_regra_suspensao` | `id` |

## `tbl_renegociacao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `parcelas` | `int(11)` | NO |  | `` |  |  |
| 9 | `valor_renegociado` | `decimal(10,2)` | NO |  | `` |  |  |
| 10 | `valor_multa` | `decimal(10,2)` | NO |  | `` |  |  |
| 11 | `valor_juros` | `decimal(10,2)` | NO |  | `` |  |  |
| 12 | `valor_desconto` | `decimal(10,2)` | NO |  | `` |  |  |
| 13 | `status` | `varchar(40)` | NO |  | `` |  |  |
| 14 | `telefone_confirmacao` | `varchar(40)` | NO |  | `` |  |  |
| 15 | `email_confirmacao` | `varchar(40)` | NO |  | `` |  |  |
| 16 | `validade` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `cliente_idx` | NON_UNIQUE | 1 | `id_cliente` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_renegociacao_cliente` | `id_cliente` | `tbl_cliente` | `id` |

## `tbl_renegociacao_titulo`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_renegociacao` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `codigo_sap` | `varchar(45)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `renegociacao_idx` | NON_UNIQUE | 1 | `id_renegociacao` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tbl_renegociacao_boletos` | `id_renegociacao` | `tbl_renegociacao` | `id` |

## `tbl_termo`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `nome` | `varchar(128)` | NO |  | `` |  |  |
| 8 | `empresa_cnpj` | `varchar(16)` | NO |  | `` |  |  |
| 9 | `empresa_nome` | `varchar(60)` | NO |  | `` |  |  |
| 10 | `texto_juridico` | `text` | NO |  | `` |  |  |
| 11 | `url_pdf` | `varchar(255)` | YES |  | `` |  |  |
| 12 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_termo_servico`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_termo` | `bigint(20)` | NO | MUL | `` |  |  |
| 2 | `servicos` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `tbl_termo_servico_termo_idx` | NON_UNIQUE | 1 | `id_termo` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_termo_servico_termo` | `id_termo` | `tbl_termo` | `id` |

## `tbl_vencimento`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `dia` | `int(11)` | NO |  | `` |  |  |
| 8 | `fechamento` | `int(11)` | NO | MUL | `` |  |  |
| 9 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `ix_tbl_vencimento_01` | NON_UNIQUE | 1 | `fechamento` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_venda`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `natureza` | `varchar(255)` | NO |  | `` |  |  |
| 8 | `fase_atual` | `varchar(255)` | NO |  | `` |  |  |
| 9 | `id_vendedor` | `bigint(20)` | YES | MUL | `` |  |  |
| 10 | `id_campanha` | `bigint(20)` | YES | MUL | `` |  |  |
| 11 | `id_lead` | `bigint(20)` | NO | MUL | `` |  |  |
| 12 | `id_contrato` | `bigint(20)` | YES | MUL | `` |  |  |
| 13 | `id_regra_suspensao` | `bigint(20)` | YES | MUL | `` |  |  |
| 14 | `id_vencimento` | `bigint(20)` | YES | MUL | `` |  |  |
| 15 | `id_endereco` | `bigint(20)` | YES | MUL | `` |  |  |
| 16 | `id_analise_credito` | `bigint(20)` | YES | MUL | `` |  |  |
| 17 | `unidade_atendimento` | `varchar(20)` | YES |  | `` |  |  |
| 18 | `cod_tipo_cobranca` | `varchar(255)` | YES |  | `` |  |  |
| 19 | `data_venda` | `date` | NO |  | `` |  |  |
| 20 | `data_agendamento` | `date` | YES |  | `` |  |  |
| 21 | `data_confirmacao_entrega` | `date` | YES |  | `` |  |  |
| 22 | `observacao` | `text` | YES |  | `` |  |  |
| 23 | `portabilidade_numero` | `varchar(20)` | YES |  | `` |  |  |
| 24 | `pacote_base_nome` | `varchar(255)` | YES |  | `` |  |  |
| 25 | `pacote_base_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 26 | `pacote_up_nome` | `varchar(255)` | YES |  | `` |  |  |
| 27 | `pacote_up_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 28 | `pacote_valor_total` | `decimal(10,2)` | YES |  | `` |  |  |
| 29 | `pacote_url_imagem` | `varchar(255)` | YES |  | `` |  |  |
| 30 | `valor_comissao` | `decimal(10,2)` | NO |  | `` |  |  |
| 31 | `concretizada` | `tinyint(1)` | NO |  | `` |  |  |
| 32 | `confirmada` | `tinyint(1)` | NO |  | `` |  |  |
| 33 | `valor_total` | `decimal(10,2)` | NO |  | `` |  |  |
| 34 | `possui_internet` | `tinyint(1)` | NO |  | `0` |  |  |
| 35 | `possui_tv` | `tinyint(1)` | NO |  | `0` |  |  |
| 36 | `possui_telefone` | `tinyint(1)` | NO |  | `0` |  |  |
| 37 | `quantidade_parcela_instalacao` | `int(11)` | YES |  | `` |  |  |
| 38 | `cancelada` | `tinyint(1)` | NO |  | `0` |  |  |
| 39 | `recorrencia_percentual_desconto` | `decimal(10,4)` | YES |  | `` |  |  |
| 40 | `recorrencia_meses_desconto` | `int(11)` | YES |  | `` |  |  |
| 41 | `pacote_up_meses_desconto` | `int(11)` | YES |  | `` |  |  |
| 42 | `equipe` | `varchar(255)` | YES | MUL | `` |  |  |
| 43 | `upgrade_logico` | `tinyint(1)` | YES |  | `` |  |  |
| 44 | `modelo_onu_anterior` | `varchar(45)` | YES |  | `` |  |  |
| 45 | `possui_taxa_instalacao_antecipada` | `tinyint(1)` | NO |  | `0` |  |  |
| 46 | `agencia` | `varchar(20)` | YES |  | `` |  |  |
| 47 | `conta_corrente` | `varchar(20)` | YES |  | `` |  |  |
| 48 | `id_processo_venda_sydle` | `varchar(255)` | YES | MUL | `` |  |  |
| 49 | `valor_referencia_b2b` | `decimal(10,2)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `ix_tbl_venda_01` | NON_UNIQUE | 1 | `id_processo_venda_sydle` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `venda_analise_credito_idx` | NON_UNIQUE | 1 | `id_analise_credito` |
| `venda_campanha_idx` | NON_UNIQUE | 1 | `id_campanha` |
| `venda_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `venda_endereco_idx` | NON_UNIQUE | 1 | `id_endereco` |
| `venda_equipe_idx` | NON_UNIQUE | 1 | `equipe` |
| `venda_lead_idx` | NON_UNIQUE | 1 | `id_lead` |
| `venda_regra_suspensao_idx` | NON_UNIQUE | 1 | `id_regra_suspensao` |
| `venda_vencimento_idx` | NON_UNIQUE | 1 | `id_vencimento` |
| `venda_vendedor_idx` | NON_UNIQUE | 1 | `id_vendedor` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tbl_venda_adicional`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_venda` | `bigint(20)` | YES | MUL | `` |  |  |
| 8 | `produto_codigo` | `varchar(60)` | NO |  | `` |  |  |
| 9 | `produto_nome` | `varchar(60)` | NO |  | `` |  |  |
| 10 | `produto_grupo` | `varchar(60)` | NO |  | `` |  |  |
| 11 | `valor_total` | `decimal(10,2)` | NO |  | `` |  |  |
| 12 | `url_imagem` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `quantidade` | `int(11)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `venda_adicional_idx` | NON_UNIQUE | 1 | `id_venda` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_venda_adicional` | `id_venda` | `tbl_venda` | `id` |

## `tbl_venda_fase`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_venda` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `usuario` | `varchar(10)` | YES |  | `` |  |  |
| 4 | `fase` | `varchar(20)` | NO |  | `` |  |  |
| 5 | `data_inicio` | `datetime` | NO |  | `` |  |  |
| 6 | `data_fim` | `datetime` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `venda_fase_venda_idx` | NON_UNIQUE | 1 | `id_venda` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_venda_fase_venda` | `id_venda` | `tbl_venda` | `id` |

## `tbl_venda_origem`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_venda` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `origem` | `varchar(100)` | YES |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | YES |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | YES |  | `` |  |  |
| 6 | `data_criacao` | `datetime` | YES |  | `` |  |  |
| 7 | `usuario_criacao` | `varchar(10)` | YES |  | `` |  |  |
| 8 | `excluido` | `tinyint(1)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `id_venda` | NON_UNIQUE | 1 | `id_venda` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `tbl_venda_origem_ibfk_1` | `id_venda` | `tbl_venda` | `id` |

## `tbl_vendedor`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `usuario` | `varchar(10)` | NO | UNI | `` |  |  |
| 8 | `equipe` | `varchar(255)` | NO |  | `` |  |  |
| 9 | `terceirizada` | `varchar(255)` | YES |  | `` |  |  |
| 10 | `id_supervisor` | `bigint(20)` | YES | MUL | `` |  |  |
| 11 | `ativo` | `tinyint(1)` | NO |  | `` |  |  |
| 12 | `id_vendedor_sydle` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `fk_vendedor_vendedor` | NON_UNIQUE | 1 | `id_supervisor` |
| `PRIMARY` | UNIQUE | 1 | `id` |
| `usuario_UNIQUE` | UNIQUE | 1 | `usuario` |
| `vendedor_usuario_idx` | NON_UNIQUE | 1 | `usuario` |
| `vendedor_vendedor_idx` | NON_UNIQUE | 1 | `id_supervisor` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_vendedor_vendedor` | `id_supervisor` | `tbl_vendedor` | `id` |

## `tmp_ativacao_sydle`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `int(11)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `int(11)` | YES |  | `` |  |  |
| 3 | `is_sucesso` | `int(11)` | YES |  | `` |  |  |
| 4 | `data_ativacao` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_atualizacao_dados_cliente`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `varchar(500)` | YES |  | `` |  |  |
| 2 | `username` | `varchar(500)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_aviso_cliente_troca_onu`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_cliente` | `bigint(20)` | NO | MUL | `` |  |  |
| 3 | `titulo_aviso` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `texto_aviso` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `aviso_cliente_troca_onu_id_cliente` | NON_UNIQUE | 1 | `id_cliente` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_base_reajuste_hotsite`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_contrato` | `bigint(20)` | NO |  | `` |  |  |
| 2 | `link_hotsite` | `varchar(255)` | NO |  | `` |  |  |
| 3 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_boleto_quitado_sap`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` |  |  |
| 2 | `codigo` | `varchar(100)` | YES |  | `` |  |  |
| 3 | `faturamento` | `datetime` | YES |  | `` |  |  |
| 4 | `vencimento` | `datetime` | YES |  | `` |  |  |
| 5 | `linha_digitavel` | `varchar(254)` | YES |  | `` |  |  |
| 6 | `status` | `varchar(200)` | YES |  | `` |  |  |
| 7 | `valor` | `decimal(16,2)` | YES |  | `` |  |  |
| 8 | `forma_pgto` | `varchar(15)` | YES |  | `` |  |  |
| 9 | `contrato_sap` | `int(11)` | YES |  | `` |  |  |
| 10 | `codigo_nf` | `int(11)` | YES |  | `` |  |  |
| 11 | `cliente_sap` | `varchar(15)` | YES | MUL | `` |  |  |
| 12 | `pagamento` | `datetime` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tmp_boleto_quitado_sap_cliente_sap_index` | NON_UNIQUE | 1 | `cliente_sap` |
| `tmp_boleto_quitado_sap_id_uindex` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_boleto_sap`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` |  |  |
| 2 | `codigo` | `varchar(100)` | YES |  | `` |  |  |
| 3 | `faturamento` | `datetime` | YES |  | `` |  |  |
| 4 | `vencimento` | `datetime` | YES |  | `` |  |  |
| 5 | `linha_digitavel` | `varchar(254)` | YES |  | `` |  |  |
| 6 | `status` | `varchar(200)` | YES |  | `` |  |  |
| 7 | `valor` | `decimal(19,6)` | YES |  | `` |  |  |
| 8 | `forma_pgto` | `varchar(15)` | YES |  | `` |  |  |
| 9 | `contrato_sap` | `int(11)` | YES |  | `` |  |  |
| 10 | `codigo_nf` | `int(11)` | YES |  | `` |  |  |
| 11 | `cliente_sap` | `varchar(15)` | YES | MUL | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tmp_boleto_sap_cliente_sap_index` | NON_UNIQUE | 1 | `cliente_sap` |
| `tmp_boleto_sap_id_uindex` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_cobranca_pontual`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_cliente` | `bigint(20)` | NO |  | `` |  |  |
| 8 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 9 | `valor` | `decimal(19,2)` | NO |  | `` |  |  |
| 10 | `numero_parcelas` | `int(11)` | YES |  | `` |  |  |
| 11 | `vencimento` | `datetime` | YES |  | `` |  |  |
| 12 | `sap_produto_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `sap_produto_nome` | `varchar(255)` | YES |  | `` |  |  |
| 14 | `sap_produto_subgrupo` | `varchar(255)` | YES |  | `` |  |  |
| 15 | `sap_empresa_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 16 | `sap_empresa_nome` | `varchar(255)` | YES |  | `` |  |  |
| 17 | `modelo_nota_fiscal` | `int(2)` | YES |  | `` |  |  |
| 18 | `status_integracao` | `varchar(20)` | NO |  | `` |  |  |
| 19 | `mensagem_integracao` | `varchar(255)` | YES |  | `` |  |  |
| 20 | `codigo_integracao` | `varchar(255)` | YES |  | `` |  |  |
| 21 | `codigo_transacao` | `varchar(255)` | YES |  | `` |  |  |
| 22 | `integracao_status_sydle` | `varchar(20)` | NO |  | `NOVO` |  |  |
| 23 | `integracao_mensagem_sydle` | `varchar(255)` | YES |  | `` |  |  |
| 24 | `integracao_codigo_sydle` | `varchar(255)` | YES |  | `` |  |  |
| 25 | `integracao_transacao_sydle` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tmp_cobranca_pontual_id_contrato_index` | NON_UNIQUE | 1 | `id_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_contrato_excecao_inadimplencia`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `contrato_excecao_inadimplencia_contrato_idx` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_contrato_sap`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 8 | `versao` | `int(11)` | NO |  | `1` |  |  |
| 9 | `codigo_sap` | `int(11)` | YES | MUL | `` |  |  |
| 10 | `contrato_origem_versao` | `int(11)` | YES |  | `` |  |  |
| 11 | `contrato_origem_codigo_sap` | `int(11)` | YES | MUL | `` |  |  |
| 12 | `tipo_cancelamento` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `integracao_status` | `varchar(255)` | NO |  | `INTEGRADO` |  |  |
| 14 | `integracao_mensagem` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tmp_codigo_sap` | NON_UNIQUE | 1 | `codigo_sap` |
| `tmp_contrato_origem_codigo_sap` | NON_UNIQUE | 1 | `contrato_origem_codigo_sap` |
| `tmp_contrato_sap_contrato` | NON_UNIQUE | 1 | `id_contrato` |
| `tmp_contrato_sap_id_contrato_versao_uindex` | UNIQUE | 1 | `id_contrato` |
| `tmp_contrato_sap_id_contrato_versao_uindex` | UNIQUE | 2 | `versao` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tmp_contrato_sap_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tmp_desconto_agendado`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `id_cliente` | `bigint(20)` | NO |  | `` |  |  |
| 8 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 9 | `desconto` | `decimal(19,4)` | NO |  | `` |  |  |
| 10 | `data_validade` | `date` | NO |  | `` |  |  |
| 11 | `dia_aplicar` | `date` | NO |  | `` |  |  |
| 12 | `sap_item_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `sap_item_nome` | `varchar(255)` | YES |  | `` |  |  |
| 14 | `sap_item_subgrupo` | `varchar(255)` | YES |  | `` |  |  |
| 15 | `quantidade` | `decimal(19,2)` | YES |  | `` |  |  |
| 16 | `status_integracao` | `varchar(20)` | NO |  | `` |  |  |
| 17 | `mensagem_integracao` | `varchar(255)` | YES |  | `` |  |  |
| 18 | `codigo_integracao` | `varchar(255)` | YES |  | `` |  |  |
| 19 | `codigo_transacao` | `varchar(255)` | YES |  | `` |  |  |
| 20 | `integracao_status_sydle` | `varchar(20)` | NO |  | `NOVO` |  |  |
| 21 | `integracao_mensagem_sydle` | `varchar(255)` | YES |  | `` |  |  |
| 22 | `integracao_codigo_sydle` | `varchar(255)` | YES |  | `` |  |  |
| 23 | `integracao_transacao_sydle` | `varchar(255)` | YES |  | `` |  |  |
| 24 | `desconto_valor` | `decimal(10,2)` | YES |  | `` |  |  |
| 25 | `ajuste_preco` | `tinyint(1)` | NO |  | `0` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tmp_desconto_agendado_id_contrato_index` | NON_UNIQUE | 1 | `id_contrato` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_evento_contrato_sydle`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `momento` | `datetime` | NO |  | `` |  |  |
| 3 | `data_evento` | `date` | NO |  | `` |  |  |
| 4 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 5 | `id_evento` | `bigint(20)` | NO |  | `` |  |  |
| 6 | `versao_contrato` | `int(11)` | NO |  | `` |  |  |
| 7 | `tipo` | `varchar(255)` | NO |  | `` |  |  |
| 8 | `integracao_status` | `varchar(255)` | YES |  | `` |  |  |
| 9 | `integracao_mensagem` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `idx_tmp_evento_suspensao_reativacao_sydle` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_tmp_evento_suspensao_reativacao_sydle` | `id_contrato` | `tbl_contrato` | `id` |

## `tmp_evento_fatura`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `momento` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `id_cliente` | `bigint(20)` | NO |  | `` |  |  |
| 5 | `origem` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_evento_financeiro_sydle`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `momento` | `datetime` | NO |  | `` |  |  |
| 3 | `data_validade` | `date` | NO |  | `` |  |  |
| 4 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 5 | `id_evento_financeiro` | `bigint(20)` | NO |  | `` |  |  |
| 6 | `versao_contrato` | `int(11)` | NO |  | `` |  |  |
| 7 | `tipo` | `varchar(255)` | NO |  | `` |  |  |
| 8 | `valor` | `decimal(10,2)` | NO |  | `` |  |  |
| 9 | `observacao` | `varchar(255)` | YES |  | `` |  |  |
| 10 | `item_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 11 | `item_nome` | `varchar(255)` | YES |  | `` |  |  |
| 12 | `ciclo` | `int(11)` | YES |  | `` |  |  |
| 13 | `ano` | `int(11)` | YES |  | `` |  |  |
| 14 | `mes` | `int(11)` | YES |  | `` |  |  |
| 15 | `payload` | `longtext` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `idx_evento_financeiro_contrato` | NON_UNIQUE | 1 | `id_contrato` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `fk_evento_financeiro_contrato` | `id_contrato` | `tbl_contrato` | `id` |

## `tmp_falhas_integracoes`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `dataFalha` | `date` | NO |  | `` |  |  |
| 3 | `statusIntegracao` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `statusCorrecao` | `varchar(255)` | NO |  | `` |  |  |
| 5 | `falha` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `motivoCorrecao` | `varchar(255)` | YES |  | `` |  |  |
| 7 | `idContrato` | `bigint(20)` | YES |  | `` |  |  |
| 8 | `idCliente` | `bigint(20)` | YES |  | `` |  |  |
| 9 | `fechamentoContrato` | `bigint(20)` | YES |  | `` |  |  |
| 10 | `tipoFalha` | `varchar(255)` | YES |  | `` |  |  |
| 11 | `valor` | `decimal(10,2)` | YES |  | `` |  |  |
| 12 | `itemCodigo` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_faturas_sfmc`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `codigo_fatura` | `bigint(20)` | NO |  | `` |  |  |
| 3 | `integracao_status` | `varchar(20)` | NO |  | `` |  |  |
| 4 | `momento` | `datetime` | NO |  | `` |  |  |
| 5 | `status_fatura` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `classificacao_fatura` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_item_sap`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `item_codigo` | `varchar(255)` | NO | UNI | `` |  |  |
| 3 | `item_nome` | `varchar(255)` | NO |  | `` |  |  |
| 4 | `valor_unitario` | `decimal(19,6)` | NO |  | `` |  |  |
| 5 | `grupo` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `valor_total` | `decimal(19,6)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `item_codigo_UNIQUE` | UNIQUE | 1 | `item_codigo` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_mapeamento_pacotes`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `pacote_codigo` | `varchar(255)` | NO |  | `` |  |  |
| 3 | `nome_comunicacao` | `text` | NO |  | `` |  |  |
| 4 | `velocidade_internet` | `varchar(255)` | YES |  | `` |  |  |
| 5 | `banda` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `minutagem_movel` | `int(11)` | YES |  | `` |  |  |
| 7 | `plano_telefonia` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `plano_tv` | `varchar(255)` | YES |  | `` |  |  |
| 9 | `lista_sva` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_mapear_pacotes_adicionais`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `produto_codigo` | `varchar(10)` | NO |  | `` |  |  |
| 2 | `adicional` | `varchar(150)` | NO |  | `` |  |  |
| 3 | `nome_amigavel` | `varchar(150)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_nota_aberto_sap`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `int(11)` | YES |  | `` |  |  |
| 2 | `empresa` | `varchar(100)` | YES |  | `` |  |  |
| 3 | `valor` | `decimal(19,6)` | YES |  | `` |  |  |
| 4 | `valorPago` | `decimal(19,6)` | YES |  | `` |  |  |
| 5 | `data` | `datetime` | YES |  | `` |  |  |
| 6 | `metodoPagamento` | `varchar(15)` | YES |  | `` |  |  |
| 7 | `qtEmailEnviado` | `int(11)` | YES |  | `` |  |  |
| 8 | `disponivelImpressao` | `tinyint(1)` | YES |  | `` |  |  |
| 9 | `contratoSap` | `int(11)` | YES |  | `` |  |  |
| 10 | `cliente_sap` | `varchar(15)` | YES | MUL | `` |  |  |
| 11 | `negociada` | `tinyint(1)` | NO |  | `0` |  |  |
| 12 | `codigo_parcela` | `int(11)` | NO |  | `1` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `tmp_nota_aberto_sap_cliente_sap_index` | NON_UNIQUE | 1 | `cliente_sap` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_pacote_produto_sap`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_pacote` | `bigint(20)` | NO |  | `` |  |  |
| 3 | `produto_codigo` | `varchar(255)` | YES | MUL | `` |  |  |
| 4 | `produto_nome` | `varchar(255)` | YES |  | `` |  |  |
| 5 | `produto_grupo` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `ix_tmp_pacote_produto_sap_codigo` | NON_UNIQUE | 1 | `produto_codigo` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_pacote_sap`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `pacote_codigo` | `varchar(255)` | YES | UNI | `` |  |  |
| 3 | `pacote_nome` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `pacote_valor` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `pacote_codigo` | UNIQUE | 1 | `pacote_codigo` |
| `pacote_sap_pacote_codigo_idx` | NON_UNIQUE | 1 | `pacote_codigo` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_produto_item_sap`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `produto_codigo` | `varchar(255)` | NO | MUL | `` |  |  |
| 3 | `item_codigo` | `varchar(255)` | YES |  | `` |  |  |
| 4 | `item_nome` | `varchar(255)` | YES |  | `` |  |  |
| 5 | `valor_unitario` | `decimal(19,6)` | YES |  | `` |  |  |
| 6 | `quantidade` | `bigint(20)` | YES |  | `` |  |  |
| 7 | `empresa_nome` | `varchar(255)` | YES |  | `` |  |  |
| 8 | `empresa_cnpj` | `varchar(255)` | YES |  | `` |  |  |
| 9 | `valor_total` | `decimal(19,6)` | YES |  | `` |  |  |
| 10 | `regra_desconto` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `ix_tmp_produto_item_sap_cod` | NON_UNIQUE | 1 | `produto_codigo` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_produto_sap`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `codigo_produto` | `varchar(255)` | NO | UNI | `` |  |  |
| 3 | `nome_produto` | `varchar(255)` | NO |  | `` |  |  |
| 4 | `valor_total` | `decimal(19,6)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `codigo_produto_UNIQUE` | UNIQUE | 1 | `codigo_produto` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_suspensao_sydle`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `int(11)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `int(11)` | YES |  | `` |  |  |
| 3 | `is_sucesso` | `int(11)` | YES |  | `` |  |  |
| 4 | `data_suspensao` | `date` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_tbl_app_adicional`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `codigo` | `varchar(50)` | NO |  | `` |  |  |
| 3 | `nome` | `varchar(255)` | NO |  | `` |  |  |
| 4 | `valor` | `decimal(19,2)` | NO |  | `` |  |  |
| 5 | `id_upgrade` | `bigint(20)` | YES | MUL | `` |  |  |
| 6 | `id_cadastro_venda` | `bigint(20)` | YES | MUL | `` |  |  |
| 7 | `status` | `varchar(50)` | YES |  | `PENDENTE` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `fk_tbl_solicitacao_adicional_cadastro_venda` | NON_UNIQUE | 1 | `id_cadastro_venda` |
| `fk_tbl_solicitacao_adicional_contrato_upgrade` | NON_UNIQUE | 1 | `id_upgrade` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_tbl_app_upgrade`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `data_criacao` | `datetime` | NO |  | `` |  |  |
| 3 | `usuario_criacao` | `varchar(10)` | NO |  | `` |  |  |
| 4 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 5 | `usuario_alteracao` | `varchar(10)` | NO |  | `` |  |  |
| 6 | `excluido` | `tinyint(1)` | NO |  | `` |  |  |
| 7 | `plano_valor` | `decimal(19,2)` | YES |  | `` |  |  |
| 8 | `sap_item_codigo` | `varchar(50)` | YES |  | `` |  |  |
| 9 | `sap_item_nome` | `varchar(255)` | YES |  | `` |  |  |
| 10 | `observacao` | `varchar(255)` | YES |  | `` |  |  |
| 11 | `id_contrato` | `bigint(20)` | NO | MUL | `` |  |  |
| 12 | `email_vendedor` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `id_venda` | `bigint(20)` | YES | MUL | `` |  |  |
| 14 | `status` | `varchar(50)` | YES |  | `PENDENTE` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `fk_tbl_contrato_upgrade_contrato` | NON_UNIQUE | 1 | `id_contrato` |
| `fk_tbl_contrato_upgrade_venda` | NON_UNIQUE | 1 | `id_venda` |
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_tbl_app_venda`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `qtd_unidade` | `int(10)` | YES |  | `` |  |  |
| 3 | `nome_condominio` | `varchar(128)` | YES |  | `` |  |  |
| 4 | `inscricao_estadual` | `varchar(50)` | YES |  | `` |  |  |
| 5 | `nome_cliente` | `varchar(128)` | YES |  | `` |  |  |
| 6 | `estado_civil` | `varchar(45)` | YES |  | `` |  |  |
| 7 | `cpf` | `varchar(14)` | YES |  | `` |  |  |
| 8 | `cnpj` | `varchar(18)` | YES |  | `` |  |  |
| 9 | `rg` | `varchar(18)` | YES |  | `` |  |  |
| 10 | `data_nascimento` | `varchar(10)` | YES |  | `` |  |  |
| 11 | `sexo` | `varchar(10)` | YES |  | `` |  |  |
| 12 | `nome_mae` | `varchar(128)` | YES |  | `` |  |  |
| 13 | `nome_pai` | `varchar(128)` | YES |  | `` |  |  |
| 14 | `profissao` | `varchar(128)` | YES |  | `` |  |  |
| 15 | `email` | `varchar(255)` | YES |  | `` |  |  |
| 16 | `rua_instalacao` | `varchar(255)` | YES |  | `` |  |  |
| 17 | `numero` | `varchar(20)` | YES |  | `` |  |  |
| 18 | `bairro` | `varchar(60)` | YES |  | `` |  |  |
| 19 | `cep` | `varchar(10)` | YES |  | `` |  |  |
| 20 | `cidade` | `varchar(60)` | YES |  | `` |  |  |
| 21 | `unidade_instalacao` | `varchar(5)` | YES |  | `` |  |  |
| 22 | `ref_instalacao` | `varchar(255)` | YES |  | `` |  |  |
| 23 | `tel_res` | `varchar(20)` | YES |  | `` |  |  |
| 24 | `tel_com` | `varchar(20)` | YES |  | `` |  |  |
| 25 | `cel` | `varchar(20)` | YES |  | `` |  |  |
| 26 | `latitude` | `decimal(10,8)` | YES |  | `` |  |  |
| 27 | `longitude` | `decimal(10,8)` | YES |  | `` |  |  |
| 28 | `portabilidade` | `tinyint(1)` | YES |  | `` |  |  |
| 29 | `numero_portado` | `varchar(20)` | YES |  | `` |  |  |
| 30 | `operadora_doadora` | `varchar(128)` | YES |  | `` |  |  |
| 31 | `dia_vencimento` | `int(2)` | YES |  | `` |  |  |
| 32 | `email_vendedor` | `varchar(255)` | YES |  | `` |  |  |
| 33 | `data_venda` | `datetime` | YES |  | `` |  |  |
| 34 | `orgao_emissor` | `varchar(10)` | YES |  | `` |  |  |
| 35 | `taxa_adesao` | `decimal(10,2)` | YES |  | `` |  |  |
| 36 | `pacote_codigo` | `varchar(10)` | YES |  | `` |  |  |
| 37 | `pacote_nome` | `varchar(255)` | YES |  | `` |  |  |
| 38 | `pacote_valor` | `decimal(10,2)` | YES |  | `` |  |  |
| 39 | `observacao` | `varchar(255)` | NO |  | `Sem observaÃƒÂ§ÃƒÂ£o.` |  |  |
| 40 | `cidade_nome` | `varchar(60)` | YES |  | `` |  |  |
| 41 | `uf` | `varchar(2)` | YES |  | `` |  |  |
| 42 | `status` | `varchar(20)` | YES |  | `PENDENTE` |  |  |
| 43 | `id_venda` | `bigint(20)` | YES | MUL | `` |  |  |
| 44 | `tipo_logradouro` | `varchar(45)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |
| `tmp_tbl_venda_tbl_venda_id_fk` | NON_UNIQUE | 1 | `id_venda` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| `tmp_tbl_venda_tbl_venda_id_fk` | `id_venda` | `tbl_venda` | `id` |

## `tmp_tbl_controle_sms_churn`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `id_contrato` | `bigint(20)` | YES |  | `` |  |  |
| 3 | `id_cliente` | `bigint(20)` | YES |  | `` |  |  |
| 4 | `id_chamado` | `bigint(20)` | YES |  | `` |  |  |
| 5 | `cancelamento_motivo` | `varchar(255)` | YES |  | `` |  |  |
| 6 | `data_cancelamento` | `date` | YES |  | `` |  |  |
| 7 | `controle_sms` | `tinyint(1)` | YES |  | `0` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_tbl_faturas_gi`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO | PRI | `` | auto_increment |  |
| 2 | `codigo` | `bigint(20)` | NO |  | `` |  |  |
| 3 | `vencimento` | `datetime` | YES |  | `` |  |  |
| 4 | `valor` | `decimal(10,2)` | YES |  | `` |  |  |
| 5 | `numero` | `int(20)` | YES |  | `` |  |  |
| 6 | `valor_pago` | `decimal(10,2)` | YES |  | `` |  |  |
| 7 | `cancelada` | `tinyint(1)` | YES |  | `` |  |  |
| 8 | `pagamento` | `datetime` | YES |  | `` |  |  |
| 9 | `vencimento_original` | `datetime` | YES |  | `` |  |  |
| 10 | `processamento` | `datetime` | YES |  | `` |  |  |
| 11 | `cancelamento` | `datetime` | YES |  | `` |  |  |
| 12 | `motivo_cancelamento` | `varchar(255)` | YES |  | `` |  |  |
| 13 | `protesto` | `varchar(45)` | YES |  | `` |  |  |
| 14 | `pagamento_online` | `tinyint(1)` | YES |  | `` |  |  |
| 15 | `taxa_online` | `decimal(10,2)` | YES |  | `` |  |  |
| 16 | `status_remessa` | `varchar(45)` | YES |  | `` |  |  |
| 17 | `cliente_nome` | `varchar(255)` | NO |  | `` |  |  |
| 18 | `cpf_cnpj` | `varchar(45)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| `PRIMARY` | UNIQUE | 1 | `id` |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_telefones_invaido`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `documento` | `varchar(255)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `tmp_update_status`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `contrato_air` | `double` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `vw_ativacao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `nome_cliente` | `varchar(100)` | NO |  | `` |  |  |
| 2 | `primeira_ativacao` | `varchar(10)` | YES |  | `` |  |  |
| 3 | `unidade` | `varchar(10)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `vw_ativacoes_eps`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `CONTRATO_CÓDIGO` | `bigint(20)` | NO |  | `0` |  |  |
| 2 | `CLIENTE_CÓDIGO` | `bigint(20)` | NO |  | `0` |  |  |
| 3 | `OS` | `bigint(20)` | YES |  | `0` |  |  |
| 4 | `CONTRATO_STATUS` | `varchar(255)` | NO |  | `` |  |  |
| 5 | `DIA_ATIVAÇÃO_CONTRATO` | `int(2)` | YES |  | `` |  |  |
| 6 | `MÊS_ATIVAÇÃO_CONTRATO` | `int(2)` | YES |  | `` |  |  |
| 7 | `ANO_ATIVAÇÃO_CONTRATO` | `int(4)` | YES |  | `` |  |  |
| 8 | `TERCEIRIZADA` | `varchar(45)` | NO |  | `` |  |  |
| 9 | `TÉCNICO` | `varchar(255)` | YES |  | `` |  |  |
| 10 | `NOME_CLIENTE` | `varchar(100)` | NO |  | `` |  |  |
| 11 | `CPF_CNPJ` | `varchar(18)` | YES |  | `` |  |  |
| 12 | `ESTADO` | `varchar(2)` | NO |  | `` |  |  |
| 13 | `UNIDADE` | `varchar(10)` | NO |  | `` |  |  |
| 14 | `CIDADE` | `varchar(60)` | NO |  | `` |  |  |
| 15 | `BAIRRO` | `varchar(255)` | YES |  | `` |  |  |
| 16 | `RUA` | `varchar(255)` | YES |  | `` |  |  |
| 17 | `COMPLEMENTO` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `vw_contrato_migracao_pendente`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_contrato` | `bigint(20)` | NO |  | `0` |  |  |
| 2 | `data_alteracao` | `datetime` | NO |  | `` |  |  |
| 3 | `fechamento` | `int(11)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `vw_contrato_ultimo_evento_ativacao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_contrato` | `bigint(20)` | YES |  | `` |  |  |
| 2 | `ultima_ativacao` | `datetime` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `vw_contrato_ultimo_evento_suspensao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_contrato` | `bigint(20)` | YES |  | `` |  |  |
| 2 | `ultima_suspensao` | `datetime` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `vw_desconto_contrato`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id_contrato` | `bigint(20)` | NO |  | `` |  |  |
| 2 | `desconto` | `decimal(19,4)` | NO |  | `` |  |  |
| 3 | `data_validade` | `date` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `vw_infancia`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `CONTRATO_CODIGO` | `bigint(20)` | NO |  | `0` |  |  |
| 2 | `CLIENTE_CODIGO` | `bigint(20)` | NO |  | `` |  |  |
| 3 | `OS_ID` | `bigint(20)` | NO |  | `0` |  |  |
| 4 | `ULTIMA_FILA` | `varchar(60)` | NO |  | `` |  |  |
| 5 | `DATA_ATIVACAO` | `date` | YES |  | `` |  |  |
| 6 | `STATUS_CONTRATO` | `varchar(255)` | NO |  | `` |  |  |
| 7 | `CHAMADO_ABERTURA` | `datetime` | NO |  | `` |  |  |
| 8 | `CHAMADO_CONCLUSAO` | `datetime` | YES |  | `` |  |  |
| 9 | `DIAS` | `int(7)` | YES |  | `` |  |  |
| 10 | `CHAMADO_MOTIVO_CONCLUSAO` | `varchar(255)` | YES |  | `` |  |  |
| 11 | `TERCEIRIZADA_ATIVAÇÃO` | `varchar(45)` | YES |  | `` |  |  |
| 12 | `TECNICO_ATIVAÇÃO` | `varchar(45)` | YES |  | `` |  |  |
| 13 | `NOME_CLIENTE` | `varchar(255)` | NO |  | `` |  |  |
| 14 | `CPF_CNPJ` | `varchar(18)` | NO |  | `` |  |  |
| 15 | `ESTADO` | `varchar(2)` | NO |  | `` |  |  |
| 16 | `UNIDADE` | `varchar(10)` | NO |  | `` |  |  |
| 17 | `CIDADE` | `varchar(60)` | NO |  | `` |  |  |
| 18 | `BAIRRO` | `varchar(255)` | NO |  | `` |  |  |
| 19 | `RUA` | `varchar(255)` | YES |  | `` |  |  |
| 20 | `COMPLEMENTO` | `varchar(255)` | YES |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `vw_suspensao_sem_ativacao`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `id` | `bigint(20)` | NO |  | `0` |  |  |
| 2 | `id_contrato` | `bigint(20)` | NO |  | `` |  |  |
| 3 | `data_suspensao` | `date` | NO |  | `` |  |  |
| 4 | `data_ativacao` | `date` | YES |  | `` |  |  |
| 5 | `dias_desconto_faturamento` | `int(11)` | NO |  | `` |  |  |
| 6 | `dias_suspenso` | `int(11)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |

## `vw_valor_contrato`

| Pos | Coluna | Tipo | Null | Key | Default | Extra | Comentario |
|---:|---|---|---|---|---|---|---|
| 1 | `valor` | `decimal(32,4)` | YES |  | `` |  |  |
| 2 | `id_contrato` | `bigint(20)` | NO |  | `` |  |  |
| 3 | `versao_contrato` | `int(11)` | NO |  | `` |  |  |

### Indices

| Indice | Tipo | Seq | Coluna |
|---|---|---:|---|
| - | - | - | - |

### Foreign keys

| Constraint | Coluna | Referencia tabela | Referencia coluna |
|---|---|---|---|
| - | - | - | - |
