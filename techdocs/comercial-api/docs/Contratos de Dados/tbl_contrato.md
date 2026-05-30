# tbl_contrato

Contrato comercial do cliente. É uma das tabelas mais centrais: aparece em consulta de cliente, aviso, SVA, ativação, migração, OAuth, venda e integrações externas.

## Resumo

| Item | Valor |
|---|---|
| Domínio | Contrato/serviço |
| Origem schema | [[../Banco - air_comercial]] |
| Classe provável | `cliente/model/Contrato.java` |
| Repository provável | `ContratoRepository` |
| Dados sensíveis | Relação cliente-serviço, pacote, valores, status e unidade |
| Fluxos principais | [[../Fluxos de Negocio/consulta-cliente]], [[../Fluxos de Negocio/criacao-integracao-contrato]], [[../Fluxos de Negocio/avisos-cliente-contrato]], [[../Fluxos de Negocio/contratos-v1-svas]], [[../Fluxos de Negocio/ativacao-servicos]] |

## Campos principais

| Campo | Papel |
|---|---|
| `id` | Identificador do contrato. |
| `id_cliente` | Cliente dono do contrato. |
| `pacote_codigo`, `pacote_nome` | Pacote contratado. |
| `valor_base` | Valor base comercial. |
| `status` | Estado operacional/comercial do contrato. |
| `unidade_atendimento` | Unidade usada em filtros e integrações. |
| `excluido` | Exclusão lógica. |
| `versao` | Versão do contrato; historicamente sensível em mudanças de plano/adicional. |

## Índices e relações

| Tipo | Campos |
|---|---|
| PK | `id` |
| Índices frequentes | `id_cliente`, `status`, `excluido`, campos de pacote/unidade conforme queries |
| Relações fortes | `tbl_cliente`, `tbl_contrato_entrega`, `tbl_contrato_item`, `tbl_contrato_produto`, `tbl_contrato_onu_aviso`, `tbl_venda` |

## Endpoints e queries relacionadas

| Uso | Referência |
|---|---|
| Detalhe e dados básicos de contrato | [[../Endpoints da Collection/get-contracts-detail]], [[../Endpoints da Collection/get-contracts-customer-basic-info]] |
| Contratos por cliente | [[../Endpoints da Collection/get-cliente-contrato]] |
| SVA | [[../Endpoints da Collection/get-contrato-svas-v1]] |
| Avisos | [[../Endpoints da Collection/get-contrato-aviso]], [[../Endpoints da Collection/post-contrato-adicionar-aviso]] |
| Query simples de contrato | [[../Resultados SELECT/sql-buscarclientecontrato]] |
| Pacotes por cliente | [[../Resultados SELECT/sql-pacotesbyclienteid]] |
| Avisos por rede/telefonia | [[../Resultados SELECT/sql-aviso-rede-monitorado]], [[../Resultados SELECT/sql-aviso-telefonia]] |

## Cuidados de mudança

- Qualquer mudança em versão/status/pacote deve revisar fluxos de migração e ativação.
- Queries de aviso fazem joins cross-schema; revisar performance ao alterar filtros de contrato.
- Mudança em `id_cliente`/status/excluído pode afetar grande parte da consulta de cliente.
- Para reprocessamento, sempre consultar [[../Operacional/Mapa de Escrita]] e runbook do fluxo.
