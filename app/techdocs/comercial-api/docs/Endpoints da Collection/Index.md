# Endpoints da Collection - comercial-api

Gerado em: 2026-05-29 22:13:23

Indice navegavel por endpoint. Cada pagina aponta para SQL, JPQL/repository, shape de retorno dos SELECTs e chamadas ainda nao resolvidas.

| Endpoint | Rota | Queries/operações | Pendencias |
|---|---|---:|---:|
| [ativar-servicos.bru](ativar-servicos.md) | `PUT /venda/{{id_venda}}/ativar_servicos` | 3 | 1 |
| [delete-oauth-remover.bru](delete-oauth-remover.md) | `DELETE /oauth/remover/{{id}}` | 3 | 0 |
| [get-cliente-analise-credito.bru](get-cliente-analise-credito.md) | `GET /cliente/{{id}}/analise_credito` | 5 | 0 |
| [get-cliente-blacklist.bru](get-cliente-blacklist.md) | `GET /cliente/{{id}}/blacklist` | 0 | 1 |
| [get-cliente-consultar-avisos.bru](get-cliente-consultar-avisos.md) | `GET /cliente/{{id}}/consultar_avisos` | 11 | 2 |
| [get-cliente-contato.bru](get-cliente-contato.md) | `GET /cliente/{{id}}/contato` | 0 | 0 |
| [get-cliente-contrato.bru](get-cliente-contrato.md) | `GET /cliente/{{id}}/contrato` | 3 | 2 |
| [get-cliente-endereco.bru](get-cliente-endereco.md) | `GET /cliente/{{id}}/endereco` | 1 | 0 |
| [get-cliente-por-cpf.bru](get-cliente-por-cpf.md) | `GET /cliente?cpfcnpj={{cpf}}` | 3 | 0 |
| [get-cliente-por-id.bru](get-cliente-por-id.md) | `GET /cliente/{{id}}` | 10 | 0 |
| [get-contracts-customer-basic-info.bru](get-contracts-customer-basic-info.md) | `GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}` | 0 | 0 |
| [get-contracts-detail.bru](get-contracts-detail.md) | `GET /v1/contracts/detail?contract_number={{contract_number}}` | 2 | 0 |
| [get-contrato-aviso.bru](get-contrato-aviso.md) | `GET /contrato/{{id}}/aviso` | 1 | 0 |
| [get-contrato-svas-v1.bru](get-contrato-svas-v1.md) | `GET /v1/contracts/{{id}}/svas` | 0 | 0 |
| [get-contrato.bru](get-contrato.md) | `GET /contrato/{{id}}` | 1 | 2 |
| [get-elegibilidade-confianca.bru](get-elegibilidade-confianca.md) | `GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}` | 0 | 0 |
| [get-migracoes-contrato.bru](get-migracoes-contrato.md) | `GET /contrato/{{id}}/migracao` | 0 | 1 |
| [get-vendas-by-natureza.bru](get-vendas-by-natureza.md) | `PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC` | 0 | 1 |
| [get-vendas-contrato.bru](get-vendas-contrato.md) | `GET /contrato/{{id}}/venda` | 0 | 2 |
| [get-wpp-notificacoes-listar.bru](get-wpp-notificacoes-listar.md) | `GET /wpp-notificacoes/listar/{{customerId}}` | 0 | 0 |
| [post-contrato-adicionar-aviso.bru](post-contrato-adicionar-aviso.md) | `POST /contrato/{{id}}/adicionar_aviso` | 1 | 0 |
| [post-criar-integracao.bru](post-criar-integracao.md) | `POST /contrato/criar-integracao` | 10 | 2 |
| [post-oauth-integrar.bru](post-oauth-integrar.md) | `POST /oauth/integrar` | 0 | 2 |
| [test-criar-integracao.bru](test-criar-integracao.md) | `POST /contrato/criar-integracao` | 10 | 2 |
