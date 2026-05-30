---
tags:
  - trabalho
  - air
  - comercial-api
  - rastreabilidade
---
# Mapa Endpoint Service Repository Tabela - comercial-api

Visão única para troubleshooting: da rota até código, queries/operações, tabelas resolvidas manualmente e fluxos.

| Endpoint | Código | Fluxos | Queries/ops | SQLs | SELECT shapes | Tabelas resolvidas manualmente |
|---|---|---|---:|---:|---:|---|
| [[Endpoints da Collection/delete-oauth-remover|DELETE /oauth/remover/{{id}}]] | `OauthController.remover` | OAuth / Keycloak | 3 | 1 | 1 | - |
| [[Endpoints da Collection/get-cliente-por-id|GET /cliente/{{id}}]] | `ClienteController.buscar` | Consulta de cliente | 10 | 9 | 9 | - |
| [[Endpoints da Collection/get-cliente-analise-credito|GET /cliente/{{id}}/analise_credito]] | `ClienteController.analisesCredito` | Análise de crédito | 5 | 5 | 5 | - |
| [[Endpoints da Collection/get-cliente-blacklist|GET /cliente/{{id}}/blacklist]] | `ClienteController.blacklist` | Blacklist | 0 | 0 | 0 | `tbl_blacklist` |
| [[Endpoints da Collection/get-cliente-consultar-avisos|GET /cliente/{{id}}/consultar_avisos]] | `ClienteController.consultarAvisos` | Avisos de cliente e contrato | 11 | 9 | 9 | `air_comercial.tbl_contrato / air_internet.tbl_aviso* / air_telefonia.tbl_reserva` |
| [[Endpoints da Collection/get-cliente-contato|GET /cliente/{{id}}/contato]] | `ClienteController.contatos` | Consulta de cliente | 0 | 0 | 0 | - |
| [[Endpoints da Collection/get-cliente-contrato|GET /cliente/{{id}}/contrato]] | `ClienteController.contratos` | Consulta de cliente | 3 | 1 | 1 | `air_base.tbl_unidade / air_comercial.tbl_contrato`, `tbl_contrato` |
| [[Endpoints da Collection/get-cliente-endereco|GET /cliente/{{id}}/endereco]] | `ClienteController.enderecos` | Consulta de cliente | 1 | 1 | 1 | - |
| [[Endpoints da Collection/get-cliente-por-cpf|GET /cliente?cpfcnpj={{cpf}}]] | `ClienteController.listar` | Consulta de cliente | 3 | 3 | 3 | - |
| [[Endpoints da Collection/get-contrato|GET /contrato/{{id}}]] | `ContratoController.buscar` | - | 1 | 0 | 0 | `tbl_contrato_item`, `tbl_contrato_produto` |
| [[Endpoints da Collection/get-contrato-aviso|GET /contrato/{{id}}/aviso]] | `ContratoAvisoController.buscarAviso` | Avisos de cliente e contrato | 1 | 0 | 0 | - |
| [[Endpoints da Collection/get-migracoes-contrato|GET /contrato/{{id}}/migracao]] | `ContratoController.migracoes` | Vendas e migrações | 0 | 0 | 0 | `tbl_contrato_migracao` |
| [[Endpoints da Collection/get-vendas-contrato|GET /contrato/{{id}}/venda]] | `ContratoController.vendas` | Vendas e migrações | 0 | 0 | 0 | `tbl_venda`, `tbl_venda_adicional` |
| [[Endpoints da Collection/get-contracts-customer-basic-info|GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}]] | `ContractsControllerV1.getCustomerBasicInfoByContractNumber` | Contratos V1 e SVAs | 0 | 0 | 0 | - |
| [[Endpoints da Collection/get-contracts-detail|GET /v1/contracts/detail?contract_number={{contract_number}}]] | `ContractsControllerV1.findContractDetails` | Contratos V1 e SVAs | 2 | 0 | 0 | - |
| [[Endpoints da Collection/get-elegibilidade-confianca|GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}]] | `ContractsControllerV1.sydleContractTrustEnablementBalance` | Contratos V1 e SVAs | 0 | 0 | 0 | - |
| [[Endpoints da Collection/get-contrato-svas-v1|GET /v1/contracts/{{id}}/svas]] | - | Contratos V1 e SVAs | 0 | 0 | 0 | - |
| [[Endpoints da Collection/get-wpp-notificacoes-listar|GET /wpp-notificacoes/listar/{{customerId}}]] | `NotificationController.listar` | Notificações WhatsApp | 0 | 0 | 0 | - |
| [[Endpoints da Collection/post-criar-integracao|POST /contrato/criar-integracao]] | `ContratoController.criarContrato` | Criação de contrato / integração | 10 | 2 | 2 | `tbl_lead`, `tbl_regra_suspensao` |
| [[Endpoints da Collection/test-criar-integracao|POST /contrato/criar-integracao]] | `ContratoController.criarContrato` | Criação de contrato / integração | 10 | 2 | 2 | `tbl_lead`, `tbl_regra_suspensao` |
| [[Endpoints da Collection/post-contrato-adicionar-aviso|POST /contrato/{{id}}/adicionar_aviso]] | `ContratoAvisoController.adicionarAviso` | Avisos de cliente e contrato | 1 | 0 | 0 | - |
| [[Endpoints da Collection/post-oauth-integrar|POST /oauth/integrar]] | `OauthController.integrarManual` | OAuth / Keycloak | 0 | 0 | 0 | `tbl_cliente` |
| [[Endpoints da Collection/get-vendas-by-natureza|PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC]] | `VendaController.naoConfirmadas` | Vendas e migrações | 0 | 0 | 0 | `tbl_venda` |
| [[Endpoints da Collection/ativar-servicos|PUT /venda/{{id_venda}}/ativar_servicos]] | `VendaController.ativarServicos` | Ativação de serviços | 3 | 1 | 1 | `tbl_contrato_campanha` |

## Leitura

- Esta página não substitui a página detalhada de cada endpoint; ela acelera triagem inicial.
- Tabelas resolvidas manualmente vêm de [[Call Graph Manual]].
- Para visão por dado, usar [[Matriz de Escrita por Tabela]].
