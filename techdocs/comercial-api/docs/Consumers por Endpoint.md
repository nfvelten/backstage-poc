---
tags:
  - trabalho
  - air
  - comercial-api
  - consumers
---
# Consumers por Endpoint - comercial-api

Busca estatica em repositorios de trabalho conhecidos. O resultado indica referencia em codigo/configuracao, nao prova trafego real. Confirmar com logs/APM/gateway antes de remover rota.

## `DELETE /oauth/remover/{{id}}`

- Endpoint doc: [[Endpoints da Collection/delete-oauth-remover]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /cliente/{{id}}`

- Endpoint doc: [[Endpoints da Collection/get-cliente-por-id]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /cliente/{{id}}/analise_credito`

- Endpoint doc: [[Endpoints da Collection/get-cliente-analise-credito]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /cliente/{{id}}/blacklist`

- Endpoint doc: [[Endpoints da Collection/get-cliente-blacklist]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /cliente/{{id}}/consultar_avisos`

- Endpoint doc: [[Endpoints da Collection/get-cliente-consultar-avisos]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /cliente/{{id}}/contato`

- Endpoint doc: [[Endpoints da Collection/get-cliente-contato]]

| Repo | Referencia |
|---|---|
| `crm-service-api` | `crm-service-api/src/main/java/br/com/alloha/crmserviceapi/esbproxyura/client/air/comercial/ComercialApiClient.java:29:    @GetMapping("/cliente/{customerId}/contato")` |
| `customer-support-service-api` | `customer-support-service-api/src/main/java/br/com/alloha/customersupportserviceapi/client/air/comercial/ComercialApiClient.java:20:    @GetMapping("/cliente/{customerId}/contato")` |
| `device-service-api` | `device-service-api/src/main/java/br/com/alloha/deviceserviceapi/client/air/comercial/ComercialApiClient.java:21:    @GetMapping("/cliente/{customerId}/contato")` |
| `financial-service-api` | `financial-service-api/src/main/java/br/com/alloha/financialserviceapi/client/air/comercial/ComercialApiClient.java:21:    @GetMapping("/cliente/{customerId}/contato")` |
| `chamado-api` | `chamado-api/src/main/java/br/net/air/cst/service/OrdemServicoService.java:592:        List<LinkedHashMap> resContatos = restTemplate.exchange(hostAirComercial + "/cliente/" + idCliente + "/contato", HttpMethod.GET, entity, List.class).getBody();` |
| `chamado-api` | `chamado-api/src/main/java/br/net/air/ofs/service/AtividadeWFMService.java:1039:        List<LinkedHashMap> resContatos = restTemplate.exchange(hostAirComercial + "/cliente/" + idCliente + "/contato", HttpMethod.GET, entity, List.class).getBody();` |
| `base-api` | `base-api/src/main/java/br/net/air/crm/controller/ClienteCrmController.java:145:    @GetMapping("/{id}/contato")` |
| `service-order-api` | `service-order-api/src/main/java/br/com/alloha/serviceorderapi/client/air/comercial/ComercialApiClient.java:24:    @GetMapping("/cliente/{customerId}/contato")` |

## `GET /cliente/{{id}}/contrato`

- Endpoint doc: [[Endpoints da Collection/get-cliente-contrato]]

| Repo | Referencia |
|---|---|
| `crm-service-api` | `crm-service-api/src/main/java/br/com/alloha/crmserviceapi/esbproxyura/client/ura/UraApiClient.java:87:    @GetMapping("/ura/contrato/cliente/{codigoCliente}")` |
| `customer-support-service-api` | `customer-support-service-api/src/main/java/br/com/alloha/customersupportserviceapi/client/ura/UraApiClient.java:87:    @GetMapping("/ura/contrato/cliente/{codigoCliente}")` |
| `device-service-api` | `device-service-api/src/main/java/br/com/alloha/deviceserviceapi/client/ura/UraApiClient.java:87:    @GetMapping("/ura/contrato/cliente/{codigoCliente}")` |
| `financial-service-api` | `financial-service-api/src/main/java/br/com/alloha/financialserviceapi/client/ura/UraApiClient.java:87:    @GetMapping("/ura/contrato/cliente/{codigoCliente}")` |
| `base-api` | `base-api/src/main/java/br/net/air/crm/controller/ClienteCrmController.java:174:    @GetMapping("/{id}/contrato/info")` |
| `base-api` | `base-api/src/main/java/br/net/air/crm/controller/ClienteCrmController.java:183:    @GetMapping("/{id}/contrato")` |
| `service-order-api` | `service-order-api/src/main/java/br/com/alloha/serviceorderapi/client/ura/UraApiClient.java:89:    @GetMapping("/ura/contrato/cliente/{codigoCliente}")` |

## `GET /cliente/{{id}}/endereco`

- Endpoint doc: [[Endpoints da Collection/get-cliente-endereco]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /cliente?cpfcnpj={{cpf}}`

- Endpoint doc: [[Endpoints da Collection/get-cliente-por-cpf]]

| Repo | Referencia |
|---|---|
| `chamado-api` | `chamado-api/src/main/java/br/net/air/cst/service/OrdemServicoService.java:177:    @Value("${sql.cpfcnpj.byid.cliente}")` |
| `chamado-api` | `chamado-api/src/main/resources/native-queries.properties:389:sql.cpfcnpj.byid.cliente=select ifnull(cpf, cnpj) cpfcnpj \` |
| `chamado-api` | `chamado-api/src/main/resources/native-queries.properties:630:sql.documento-by-id-cliente=select cf.cpf as cpfcnpj \` |

## `GET /contrato/{{id}}`

- Endpoint doc: [[Endpoints da Collection/get-contrato]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /contrato/{{id}}/aviso`

- Endpoint doc: [[Endpoints da Collection/get-contrato-aviso]]

| Repo | Referencia |
|---|---|
| `crm-service-api` | `crm-service-api/src/main/java/br/com/alloha/crmserviceapi/esbproxyura/client/air/comercial/ComercialApiClient.java:49:    @GetMapping("/contrato/{contractNumber}/aviso")` |
| `customer-support-service-api` | `customer-support-service-api/src/main/java/br/com/alloha/customersupportserviceapi/client/air/comercial/ComercialApiClient.java:40:    @GetMapping("/contrato/{contractNumber}/aviso")` |
| `device-service-api` | `device-service-api/src/main/java/br/com/alloha/deviceserviceapi/client/air/comercial/ComercialApiClient.java:42:    @GetMapping("/contrato/{contractNumber}/aviso")` |
| `financial-service-api` | `financial-service-api/src/main/java/br/com/alloha/financialserviceapi/client/air/comercial/ComercialApiClient.java:41:    @GetMapping("/contrato/{contractNumber}/aviso")` |
| `chamado-api` | `chamado-api/src/main/java/br/net/air/service/ContratoAvisoOnuService.java:31:                hostAirComercial + "/contrato/" + contratoId + "/aviso",` |
| `service-order-api` | `service-order-api/src/main/java/br/com/alloha/serviceorderapi/client/air/comercial/ComercialApiClient.java:44:    @GetMapping("/contrato/{contractNumber}/aviso")` |

## `GET /contrato/{{id}}/migracao`

- Endpoint doc: [[Endpoints da Collection/get-migracoes-contrato]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /contrato/{{id}}/venda`

- Endpoint doc: [[Endpoints da Collection/get-vendas-contrato]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}`

- Endpoint doc: [[Endpoints da Collection/get-contracts-customer-basic-info]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /v1/contracts/detail?contract_number={{contract_number}}`

- Endpoint doc: [[Endpoints da Collection/get-contracts-detail]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}`

- Endpoint doc: [[Endpoints da Collection/get-elegibilidade-confianca]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /v1/contracts/{{id}}/svas`

- Endpoint doc: [[Endpoints da Collection/get-contrato-svas-v1]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `GET /wpp-notificacoes/listar/{{customerId}}`

- Endpoint doc: [[Endpoints da Collection/get-wpp-notificacoes-listar]]

| Repo | Referencia |
|---|---|
| `crm-service-api` | `crm-service-api/src/main/java/br/com/alloha/crmserviceapi/esbproxyura/client/air/comercial/ComercialApiClient.java:33:    @GetMapping("/wpp-notificacoes/listar/{customerId}")` |
| `customer-support-service-api` | `customer-support-service-api/src/main/java/br/com/alloha/customersupportserviceapi/client/air/comercial/ComercialApiClient.java:24:    @GetMapping("/wpp-notificacoes/listar/{customerId}")` |
| `device-service-api` | `device-service-api/src/main/java/br/com/alloha/deviceserviceapi/client/air/comercial/ComercialApiClient.java:25:    @GetMapping("/wpp-notificacoes/listar/{customerId}")` |
| `financial-service-api` | `financial-service-api/src/main/java/br/com/alloha/financialserviceapi/client/air/comercial/ComercialApiClient.java:25:    @GetMapping("/wpp-notificacoes/listar/{customerId}")` |
| `tv-api` | `tv-api/src/main/java/br/net/air/external/comercial/clients/ComercialClient.java:17:    @GetMapping("/wpp-notificacoes/listar/{clientId}")` |
| `chamado-api` | `chamado-api/src/main/resources/application-desenvolvimento.properties:123:contatos.wpp=https://nds-teste.sumicity.net.br:8020/wpp-notificacoes/listar/` |
| `chamado-api` | `chamado-api/src/main/resources/application.properties:215:contatos.wpp=https://api.sumicity.net.br:8020/wpp-notificacoes/listar/` |
| `service-order-api` | `service-order-api/src/main/java/br/com/alloha/serviceorderapi/client/air/comercial/ComercialApiClient.java:28:    @GetMapping("/wpp-notificacoes/listar/{customerId}")` |

## `POST /contrato/criar-integracao`

- Endpoint doc: [[Endpoints da Collection/post-criar-integracao]]

| Repo | Referencia |
|---|---|
| `crm-service-api` | `crm-service-api/src/main/java/br/com/alloha/crmserviceapi/esbproxyura/client/air/comercial/ComercialApiClient.java:102:    @PostMapping("/contrato/criar-integracao")` |

## `POST /contrato/criar-integracao`

- Endpoint doc: [[Endpoints da Collection/test-criar-integracao]]

| Repo | Referencia |
|---|---|
| `crm-service-api` | `crm-service-api/src/main/java/br/com/alloha/crmserviceapi/esbproxyura/client/air/comercial/ComercialApiClient.java:102:    @PostMapping("/contrato/criar-integracao")` |

## `POST /contrato/{{id}}/adicionar_aviso`

- Endpoint doc: [[Endpoints da Collection/post-contrato-adicionar-aviso]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `POST /oauth/integrar`

- Endpoint doc: [[Endpoints da Collection/post-oauth-integrar]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC`

- Endpoint doc: [[Endpoints da Collection/get-vendas-by-natureza]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.

## `PUT /venda/{{id_venda}}/ativar_servicos`

- Endpoint doc: [[Endpoints da Collection/ativar-servicos]]

- Nenhuma referencia estatica encontrada nos repositorios-alvo.
