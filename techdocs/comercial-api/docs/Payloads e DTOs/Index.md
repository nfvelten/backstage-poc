---
tags:
  - trabalho
  - air
  - comercial-api
  - payloads
---
# Payloads e DTOs - comercial-api

Documentacao derivada da collection Bruno. Registra estrutura, tipos inferidos e sensibilidade por campo, sem valores reais.

| Endpoint | Metodo | Body | Campos sensiveis | Documento |
|---|---|---|---|---|
| `PUT /venda/{{id_venda}}/ativar_servicos` | `PUT` | nao | - | [[ativar-servicos]] |
| `DELETE /oauth/remover/{{id}}` | `DELETE` | nao | - | [[delete-oauth-remover]] |
| `GET /cliente/{{id}}/analise_credito` | `GET` | nao | - | [[get-cliente-analise-credito]] |
| `GET /cliente/{{id}}/blacklist` | `GET` | nao | - | [[get-cliente-blacklist]] |
| `GET /cliente/{{id}}/consultar_avisos` | `GET` | nao | - | [[get-cliente-consultar-avisos]] |
| `GET /cliente/{{id}}/contato` | `GET` | nao | - | [[get-cliente-contato]] |
| `GET /cliente/{{id}}/contrato` | `GET` | nao | - | [[get-cliente-contrato]] |
| `GET /cliente/{{id}}/endereco` | `GET` | nao | - | [[get-cliente-endereco]] |
| `GET /cliente?cpfcnpj={{cpf}}` | `GET` | nao | - | [[get-cliente-por-cpf]] |
| `GET /cliente/{{id}}` | `GET` | nao | - | [[get-cliente-por-id]] |
| `GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}` | `GET` | nao | - | [[get-contracts-customer-basic-info]] |
| `GET /v1/contracts/detail?contract_number={{contract_number}}` | `GET` | nao | - | [[get-contracts-detail]] |
| `GET /contrato/{{id}}` | `GET` | nao | - | [[get-contrato]] |
| `GET /contrato/{{id}}/aviso` | `GET` | nao | - | [[get-contrato-aviso]] |
| `GET /v1/contracts/{{id}}/svas` | `GET` | nao | - | [[get-contrato-svas-v1]] |
| `GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}` | `GET` | nao | - | [[get-elegibilidade-confianca]] |
| `GET /contrato/{{id}}/migracao` | `GET` | nao | - | [[get-migracoes-contrato]] |
| `PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC` | `PUT` | sim | - | [[get-vendas-by-natureza]] |
| `GET /contrato/{{id}}/venda` | `GET` | nao | - | [[get-vendas-contrato]] |
| `GET /wpp-notificacoes/listar/{{customerId}}` | `GET` | nao | - | [[get-wpp-notificacoes-listar]] |
| `POST /contrato/{{id}}/adicionar_aviso` | `POST` | sim | - | [[post-contrato-adicionar-aviso]] |
| `POST /contrato/criar-integracao` | `POST` | sim | contato, documento, endereco, financeiro | [[post-criar-integracao]] |
| `POST /oauth/integrar` | `POST` | sim | - | [[post-oauth-integrar]] |
| `POST /contrato/criar-integracao` | `POST` | sim | contato, documento, endereco, financeiro | [[test-criar-integracao]] |
