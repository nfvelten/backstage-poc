---
tags:
  - trabalho
  - air
  - comercial-api
  - impacto
---
# Matriz de Impacto - comercial-api

Mapa endpoint -> fluxo -> codigo -> queries -> dados -> operacao. Use em review para saber o que revisar ao alterar rota, DTO, query ou tabela.

| Endpoint | Fluxos | Escrita | Body | Queries/ops | SELECTs | Resolvidas manualmente | Pendencias |
|---|---|---|---|---:|---:|---:|---:|
| [[Endpoints da Collection/delete-oauth-remover|DELETE /oauth/remover/{{id}}]] | OAuth / Keycloak | sim | nao | 3 | 1 | 0 | 0 |
| [[Endpoints da Collection/get-cliente-por-id|GET /cliente/{{id}}]] | Consulta de cliente | nao | nao | 10 | 9 | 0 | 0 |
| [[Endpoints da Collection/get-cliente-analise-credito|GET /cliente/{{id}}/analise_credito]] | Análise de crédito | nao | nao | 5 | 5 | 0 | 0 |
| [[Endpoints da Collection/get-cliente-blacklist|GET /cliente/{{id}}/blacklist]] | Blacklist | nao | nao | 0 | 0 | 1 | 0 |
| [[Endpoints da Collection/get-cliente-consultar-avisos|GET /cliente/{{id}}/consultar_avisos]] | Avisos de cliente e contrato | nao | nao | 11 | 9 | 2 | 0 |
| [[Endpoints da Collection/get-cliente-contato|GET /cliente/{{id}}/contato]] | Consulta de cliente | nao | nao | 0 | 0 | 0 | 0 |
| [[Endpoints da Collection/get-cliente-contrato|GET /cliente/{{id}}/contrato]] | Consulta de cliente | nao | nao | 3 | 1 | 2 | 0 |
| [[Endpoints da Collection/get-cliente-endereco|GET /cliente/{{id}}/endereco]] | Consulta de cliente | nao | nao | 1 | 1 | 0 | 0 |
| [[Endpoints da Collection/get-cliente-por-cpf|GET /cliente?cpfcnpj={{cpf}}]] | Consulta de cliente | nao | nao | 3 | 3 | 0 | 0 |
| [[Endpoints da Collection/get-contrato|GET /contrato/{{id}}]] | - | nao | nao | 1 | 0 | 2 | 0 |
| [[Endpoints da Collection/get-contrato-aviso|GET /contrato/{{id}}/aviso]] | Avisos de cliente e contrato | nao | nao | 1 | 0 | 0 | 0 |
| [[Endpoints da Collection/get-migracoes-contrato|GET /contrato/{{id}}/migracao]] | Vendas e migrações | nao | nao | 0 | 0 | 1 | 0 |
| [[Endpoints da Collection/get-vendas-contrato|GET /contrato/{{id}}/venda]] | Vendas e migrações | nao | nao | 0 | 0 | 2 | 0 |
| [[Endpoints da Collection/get-contracts-customer-basic-info|GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}]] | Contratos V1 e SVAs | nao | nao | 0 | 0 | 0 | 0 |
| [[Endpoints da Collection/get-contracts-detail|GET /v1/contracts/detail?contract_number={{contract_number}}]] | Contratos V1 e SVAs | nao | nao | 2 | 0 | 0 | 0 |
| [[Endpoints da Collection/get-elegibilidade-confianca|GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}]] | Contratos V1 e SVAs | nao | nao | 0 | 0 | 0 | 0 |
| [[Endpoints da Collection/get-contrato-svas-v1|GET /v1/contracts/{{id}}/svas]] | Contratos V1 e SVAs | nao | nao | 0 | 0 | 0 | 0 |
| [[Endpoints da Collection/get-wpp-notificacoes-listar|GET /wpp-notificacoes/listar/{{customerId}}]] | Notificações WhatsApp | nao | nao | 0 | 0 | 0 | 0 |
| [[Endpoints da Collection/post-criar-integracao|POST /contrato/criar-integracao]] | Criação de contrato / integração | sim | sim | 10 | 2 | 2 | 0 |
| [[Endpoints da Collection/test-criar-integracao|POST /contrato/criar-integracao]] | Criação de contrato / integração | sim | sim | 10 | 2 | 2 | 0 |
| [[Endpoints da Collection/post-contrato-adicionar-aviso|POST /contrato/{{id}}/adicionar_aviso]] | Avisos de cliente e contrato | sim | sim | 1 | 0 | 0 | 0 |
| [[Endpoints da Collection/post-oauth-integrar|POST /oauth/integrar]] | OAuth / Keycloak | sim | sim | 0 | 0 | 2 | 0 |
| [[Endpoints da Collection/get-vendas-by-natureza|PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC]] | Vendas e migrações | sim | sim | 0 | 0 | 1 | 0 |
| [[Endpoints da Collection/ativar-servicos|PUT /venda/{{id_venda}}/ativar_servicos]] | Ativação de serviços | sim | nao | 3 | 1 | 1 | 0 |

## Leitura

- `Escrita`: inferido pelo metodo HTTP.
- `Body`: existe body JSON na collection.
- `Queries/ops`: inclui SQL nativo, queries JPA/repository e operacoes CRUD mapeadas.
- `Resolvidas manualmente`: chamadas do call graph documentadas em [[Call Graph Manual]].
- `Pendencias`: chamadas que o call graph estatico nao resolveu.
