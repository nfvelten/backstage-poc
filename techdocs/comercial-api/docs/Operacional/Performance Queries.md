# Performance Queries - comercial-api

Gerado em: 2026-05-30 10:20:55

Análise inicial baseada em SQL exportado: largura de resultado, quantidade de joins, tabelas e colunas de filtro.

| Query | Colunas | Joins | Tabelas | Filtros WHERE | Sinal |
|---|---:|---:|---|---|---|
| [sql-aviso-rede-monitorado.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-monitorado.sql) | 14 | 4 | `air_comercial.tbl_contrato`, `air_comercial.tbl_contrato_onu_aviso`, `air_internet.tbl_aviso`, `air_internet.tbl_estimativa_conclusao_aviso` | `av.afeta_internet`, `av.excluido`, `av.vigente`, `ct.id`, `ct.status` | muitos joins, cross-schema |
| [sql-aviso-rede-manual.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-manual.sql) | 12 | 4 | `air_comercial.tbl_cliente`, `air_comercial.tbl_contrato`, `air_internet.tbl_aviso`, `air_internet.tbl_login`, `air_internet.tbl_posicoes_afetadas` | `a.afeta_internet`, `a.excluido`, `a.vigente`, `ct.id_cliente`, `ct.status`, `tpa.pon`, `tpa.slot` | muitos joins, cross-schema |
| [sql-aviso-telefonia.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-telefonia.sql) | 12 | 3 | `air_comercial.tbl_contrato`, `air_internet.tbl_aviso`, `air_internet.tbl_aviso_unidade`, `air_telefonia.tbl_reserva` | `a.afeta_internet`, `a.afeta_telefonia`, `a.excluido`, `a.vigente`, `ct.id_cliente`, `ct.status` | cross-schema |
| [vendarepository-buscarvendanoair.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/vendarepository-buscarvendanoair.sql) | 3 | 3 | `air_chamado.tbl_chd_chamado`, `air_chamado.tbl_os`, `air_comercial.tbl_contrato`, `air_comercial.tbl_venda` | `v.id_processo_venda_sydle` | cross-schema |
| [enderecorepository-findallenderecosbycliente.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/enderecorepository-findallenderecosbycliente.sql) | 96 | 2 | `air_comercial.tbl_condominio`, `air_comercial.tbl_endereco`, `tbl_endereco_cidade` | `e.excluido`, `e.id_cliente` | resultado largo |
| [clienterepository-findclientebyid.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/clienterepository-findclientebyid.sql) | 42 | 2 | `tbl_cliente`, `tbl_cliente_fisico`, `tbl_cliente_juridico` | `cliente.id` | - |
| [carteirarepository-findcarteirabyid.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/carteirarepository-findcarteirabyid.sql) | 28 | 2 | `tbl_carteira`, `tbl_vendedor` | `carteira.id` | - |
| [sql-aviso-rede-backbone.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-backbone.sql) | 12 | 2 | `air_comercial.tbl_contrato`, `air_internet.tbl_aviso`, `air_internet.tbl_aviso_unidade` | `a.afeta_internet`, `a.aviso_backbone`, `a.excluido`, `a.vigente`, `ct.id_cliente`, `ct.status` | cross-schema |
| [sql-aviso-rede-nao-monitorado.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-nao-monitorado.sql) | 12 | 2 | `air_comercial.tbl_contrato`, `air_internet.tbl_aviso`, `air_internet.tbl_aviso_unidade` | `a.afeta_internet`, `a.excluido`, `a.ura_ativa`, `a.vigente`, `ct.id`, `ct.status` | cross-schema |
| [sql-verifica-cliente-monitorado.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-verifica-cliente-monitorado.sql) | 1 | 2 | `air_comercial.tbl_contrato`, `air_comercial.tbl_contrato_onu_aviso`, `air_internet.tbl_login` | `ct.id` | cross-schema |
| [analisecreditorepository-findallbyleadclienteid.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/analisecreditorepository-findallbyleadclienteid.sql) | 90 | 1 | `tbl_analise_credito`, `tbl_lead` | `ld.id_cliente` | resultado largo |
| [enderecocidaderepository-findcidadebysigla.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/enderecocidaderepository-findcidadebysigla.sql) | 13 | 1 | `air_comercial.tbl_endereco_cidade`, `air_comercial.tbl_endereco_cidade_unidade` | `tec.excluido`, `tecu.unidades` | - |
| [sql-contratoavisomigracaocompulsoria.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-contratoavisomigracaocompulsoria.sql) | 6 | 1 | `air_comercial.tbl_aviso_migracao`, `air_comercial.tbl_contrato` | `c.pacote_codigo`, `m.id_cliente` | - |
| [sql-contract-brands.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-contract-brands.sql) | 2 | 1 | `air_base.tbl_unidade`, `air_comercial.tbl_contrato` | `contrato.id` | cross-schema |
| [sql-customer-brands.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-customer-brands.sql) | 2 | 1 | `air_base.tbl_unidade`, `air_comercial.tbl_contrato` | `contrato.id_cliente` | cross-schema |
| [analisecreditorestricaorepository-findallbyanalisecredito_id.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/analisecreditorestricaorepository-findallbyanalisecredito_id.sql) | 8 | 0 | `tbl_analise_credito_restricao` | `tacr.id_analise_credito` | - |
| [sql-contratoavisomigracao.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-contratoavisomigracao.sql) | 8 | 0 | `air_comercial.tbl_aviso_migracao` | `id_cliente`, `migracao_compulsoria` | - |
| [analisecreditoatributorepository-findallbyanalisecredito_id.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/analisecreditoatributorepository-findallbyanalisecredito_id.sql) | 4 | 0 | `tbl_analise_credito_atributo` | `taca.id_analise_credito` | - |
| [sql-buscarclientecontrato.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-buscarclientecontrato.sql) | 1 | 0 | `air_comercial.tbl_contrato` | `id` | - |
| [sql-buscarclienteosprotocoloura.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-buscarclienteosprotocoloura.sql) | 1 | 0 | `air_chamado.tbl_os` | `tbl_os.protocolo_secundario` | cross-schema |
| [sql-buscarclienteprotocoloura.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-buscarclienteprotocoloura.sql) | 1 | 0 | `air_chamado.tbl_chd_chamado` | `protocolo_primario` | cross-schema |
| [sql-pacotesbyclienteid.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-pacotesbyclienteid.sql) | 1 | 0 | `air_comercial.tbl_contrato` | `id_cliente` | - |

## Próximos passos

- Cruzar filtros com índices reais do `Banco - air_comercial`.
- Priorizar queries de rotas mais usadas: `/v1/contracts/detail`, `/cliente/{id}/consultar_avisos`, `/cliente/{id}/analise_credito`.
- Para queries cross-schema, validar latência no banco e planos de execução fora desta documentação.
