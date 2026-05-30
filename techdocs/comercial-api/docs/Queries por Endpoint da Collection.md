---
tags: [trabalho, air, api, comercial-api, sql, bruno]
---
# Queries por Endpoint da Collection

Gerado em: 2026-05-29 22:13:23

Mapeamento dos requests em `air-api-collection/comercial` para queries usadas pelos endpoints, seguindo chamadas transitivas no codigo.

Inclui SQL nativo, JPQL em repositories, metodos derivados Spring Data e operacoes CRUD herdadas.

Limites: analise estatica; chamadas dinamicas e queries montadas fora dos padroes conhecidos podem precisar de revisao manual. Queries derivadas sao aproximacoes semanticas.

Entrada principal: [[Endpoints da Collection/Index]].

Shape dos SELECTs no prod main: [[Resultado das Queries SELECT]].

## `ativar-servicos.bru`

- Rota: `PUT /venda/{{id_venda}}/ativar_servicos`
- Codigo: `VendaController.ativarServicos` em `comercial-api/src/main/java/br/net/air/venda/controller/VendaController.java:269`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` | `JPA e Repositories.md#contratocampanharepository-findtopbycontratoandcanceladaisfalseorderbyiddesc` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoCampanhaRepository.java:12` | `VendaController.ativarServicos -> ContratoService.salvarDescontoRecorrenteCampanha -> ContratoCampanhaService.buscarContratoCampanhaVigente -> ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` |
| `VendaOrigemRepository.findTopByVenda` | `JPA e Repositories.md#vendaorigemrepository-findtopbyvenda` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaOrigemRepository.java:8` | `VendaController.ativarServicos -> VendaService.ativarServicos -> VendaOrigemService.getOrigemByVenda -> VendaOrigemRepository.findTopByVenda` |
| `sql.customer-brands` | `sql-customer-brands.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:639` | `VendaController.ativarServicos -> VendaService.processarAtivacao -> VendaService.montarAtivacaoNotificationDTO -> OauthIntegracaoService.getBrands` |

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `ContratoCampanhaService.save`

## `delete-oauth-remover.bru`

- Rota: `DELETE /oauth/remover/{{id}}`
- Codigo: `OauthController.remover` em `comercial-api/src/main/java/br/net/air/oauth/Controller/OauthController.java:41`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `ClienteFisicoRepository.findOne` | `JPA e Repositories.md#clientefisicorepository-findone` | `repository-crud-operation` | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteFisicoRepository.java:1` | `OauthController.remover -> OauthIntegracaoService.removerClientePorBrands -> ClienteService.getDocumentoPorCliente -> ClienteFisicoRepository.findOne` |
| `ClienteJuridicoRepository.findOne` | `JPA e Repositories.md#clientejuridicorepository-findone` | `repository-crud-operation` | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteJuridicoRepository.java:1` | `OauthController.remover -> OauthIntegracaoService.removerClientePorBrands -> ClienteService.getDocumentoPorCliente -> ClienteJuridicoRepository.findOne` |
| `sql.customer-brands` | `sql-customer-brands.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:639` | `OauthController.remover -> OauthIntegracaoService.removerClientePorBrands -> OauthIntegracaoService.getBrands` |

## `get-cliente-analise-credito.bru`

- Rota: `GET /cliente/{{id}}/analise_credito`
- Codigo: `ClienteController.analisesCredito` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:310`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `AnaliseCreditoAtributoRepository.findAllByAnaliseCredito_id` | `analisecreditoatributorepository-findallbyanalisecredito_id.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoAtributoRepository.java:20` | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> AnaliseCreditoAtributoRepository.findAllByAnaliseCredito_id` |
| `AnaliseCreditoRepository.findAllByLeadClienteId` | `analisecreditorepository-findallbyleadclienteid.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoRepository.java:115` | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> AnaliseCreditoRepository.findAllByLeadClienteId` |
| `AnaliseCreditoRestricaoRepository.findAllByAnaliseCredito_id` | `analisecreditorestricaorepository-findallbyanalisecredito_id.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoRestricaoRepository.java:24` | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> AnaliseCreditoRestricaoRepository.findAllByAnaliseCredito_id` |
| `CarteiraRepository.findCarteiraById` | `carteirarepository-findcarteirabyid.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/configuracoes/repository/CarteiraRepository.java:51` | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> ClienteService.findClienteLeadByCodigo -> ClienteService.toClienteFisicoDto -> CarteiraService.findCarteiraById -> CarteiraRepository.findCarteiraById` |
| `ClienteRepository.findClienteById` | `clienterepository-findclientebyid.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:66` | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> ClienteService.findClienteLeadByCodigo -> ClienteRepository.findClienteById` |

## `get-cliente-blacklist.bru`

- Rota: `GET /cliente/{{id}}/blacklist`
- Codigo: `ClienteController.blacklist` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:269`
- Queries identificadas: nenhuma

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `BlacklistService.findAll`

## `get-cliente-consultar-avisos.bru`

- Rota: `GET /cliente/{{id}}/consultar_avisos`
- Codigo: `ClienteController.consultarAvisos` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:543`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `ClienteRepository.findClienteResumoAvisoById` | `JPA e Repositories.md#clienterepository-findclienteresumoavisobyid` | `repository-jpql-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:85` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteRepository.findClienteResumoAvisoById` |
| `ContratoRepository.findAllIdByClienteId` | `JPA e Repositories.md#contratorepository-findallidbyclienteid` | `repository-jpql-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:52` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ContratoRepository.findAllIdByClienteId` |
| `sql.aviso-telefonia` | `sql-aviso-telefonia.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:823` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |
| `sql.aviso.rede.backbone` | `sql-aviso-rede-backbone.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:740` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |
| `sql.aviso.rede.manual` | `sql-aviso-rede-manual.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:714` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |
| `sql.aviso.rede.monitorado` | `sql-aviso-rede-monitorado.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:657` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.adicionarAvisosPorMonitoramento -> JdbcRepository.findAvisosRedeContratoMonitorado` |
| `sql.aviso.rede.nao-monitorado` | `sql-aviso-rede-nao-monitorado.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:690` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.adicionarAvisosPorMonitoramento -> JdbcRepository.findAvisosRedeContratoNaoMonitorado` |
| `sql.contratoAvisoMigracao` | `sql-contratoavisomigracao.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:221` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.buildAvisoMigracaoV2` |
| `sql.contratoAvisoMigracaoCompulsoria` | `sql-contratoavisomigracaocompulsoria.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:236` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.buildAvisoMigracaoCompulsoriaV2` |
| `sql.pacotesByClienteId` | `sql-pacotesbyclienteid.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:252` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.buildAvisoMigracaoV2 -> ClienteService.jaMigrouV2` |
| `sql.verifica.cliente-monitorado` | `sql-verifica-cliente-monitorado.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:684` | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `MySqlRepository.carregar`
- `MySqlRepository.consultar`

## `get-cliente-contato.bru`

- Rota: `GET /cliente/{{id}}/contato`
- Codigo: `ClienteController.contatos` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:263`
- Queries identificadas: nenhuma

## `get-cliente-contrato.bru`

- Rota: `GET /cliente/{{id}}/contrato`
- Codigo: `ClienteController.contratos` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:211`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `MarcadorContratoRepository.findByIdContrato` | `JPA e Repositories.md#marcadorcontratorepository-findbyidcontrato` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/MarcadorContratoRepository.java:14` | `ClienteController.contratos -> MarcadorContratoRepository.findByIdContrato` |
| `VendaRepository.findTopByContratoOrderByCriacaoDesc` | `JPA e Repositories.md#vendarepository-findtopbycontratoorderbycriacaodesc` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:23` | `ClienteController.contratos -> VendaService.findTopByContratoOrderByCriacaoDesc -> VendaRepository.findTopByContratoOrderByCriacaoDesc` |
| `sql.contract-brands` | `sql-contract-brands.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:652` | `ClienteController.contratos -> ContratoService.buscarMarcaPorContrato` |

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `ContratoService.findAll`
- `MySqlRepository.consultarMap`

## `get-cliente-endereco.bru`

- Rota: `GET /cliente/{{id}}/endereco`
- Codigo: `ClienteController.enderecos` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:257`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `EnderecoRepository.findAllEnderecosByCliente` | `enderecorepository-findallenderecosbycliente.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:124` | `ClienteController.enderecos -> EnderecoService.findAllEnderecosByCliente -> EnderecoRepository.findAllEnderecosByCliente` |

## `get-cliente-por-cpf.bru`

- Rota: `GET /cliente?cpfcnpj={{cpf}}`
- Codigo: `ClienteController.listar` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:80`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `sql.buscarClienteContrato` | `sql-buscarclientecontrato.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:457` | `ClienteController.listar -> ClienteService.findAll` |
| `sql.buscarClienteOSProtocoloUra` | `sql-buscarclienteosprotocoloura.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:452` | `ClienteController.listar -> ClienteService.findAll` |
| `sql.buscarClienteProtocoloUra` | `sql-buscarclienteprotocoloura.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:447` | `ClienteController.listar -> ClienteService.findAll` |

## `get-cliente-por-id.bru`

- Rota: `GET /cliente/{{id}}`
- Codigo: `ClienteController.buscar` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:187`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `ContratoRepository.findAllByCliente` | `JPA e Repositories.md#contratorepository-findallbycliente` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:20` | `ClienteController.buscar -> ClienteService.buildAvisos -> ContratoRepository.findAllByCliente` |
| `sql.aviso-telefonia` | `sql-aviso-telefonia.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:823` | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.findAvisosTelefonia` |
| `sql.aviso.rede.backbone` | `sql-aviso-rede-backbone.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:740` | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.findAvisosRedeBackbone` |
| `sql.aviso.rede.manual` | `sql-aviso-rede-manual.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:714` | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.findAvisosRedeManual` |
| `sql.aviso.rede.monitorado` | `sql-aviso-rede-monitorado.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:657` | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.adicionarAvisosPorMonitoramentoV2 -> JdbcRepository.findAvisosRedeContratoMonitorado` |
| `sql.aviso.rede.nao-monitorado` | `sql-aviso-rede-nao-monitorado.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:690` | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.adicionarAvisosPorMonitoramentoV2 -> JdbcRepository.findAvisosRedeContratoNaoMonitorado` |
| `sql.contratoAvisoMigracao` | `sql-contratoavisomigracao.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:221` | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.buildAvisoMigracao -> JdbcRepository.findAvisoMigracao` |
| `sql.contratoAvisoMigracaoCompulsoria` | `sql-contratoavisomigracaocompulsoria.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:236` | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.buildAvisoMigracaoCompulsoria -> JdbcRepository.findAvisoMigracaoCompulsoria` |
| `sql.pacotesByClienteId` | `sql-pacotesbyclienteid.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:252` | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.buildAvisoMigracao -> ClienteService.jaMigrou -> JdbcRepository.findPacotes` |
| `sql.verifica.cliente-monitorado` | `sql-verifica-cliente-monitorado.sql` | `native-properties` | `comercial-api/src/main/resources/native-queries.properties:684` | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.contratoMonitorado` |

## `get-contracts-customer-basic-info.bru`

- Rota: `GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}`
- Codigo: `ContractsControllerV1.getCustomerBasicInfoByContractNumber` em `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java:46`
- Queries identificadas: nenhuma

## `get-contracts-detail.bru`

- Rota: `GET /v1/contracts/detail?contract_number={{contract_number}}`
- Codigo: `ContractsControllerV1.findContractDetails` em `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java:32`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `ContratoRepository.findContractProductsAndItems` | `JPA e Repositories.md#contratorepository-findcontractproductsanditems` | `repository-jpql-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:41` | `ContractsControllerV1.findContractDetails -> ContractServiceV1.findContractDetails -> ContratoRepository.findContractProductsAndItems` |
| `ContratoRepository.findPacoteById` | `JPA e Repositories.md#contratorepository-findpacotebyid` | `repository-jpql-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:47` | `ContractsControllerV1.findContractDetails -> ContractServiceV1.findContractDetails -> ContratoRepository.findPacoteById` |

## `get-contrato-aviso.bru`

- Rota: `GET /contrato/{{id}}/aviso`
- Codigo: `ContratoAvisoController.buscarAviso` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoAvisoController.java:35`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `ContratoAvisoOnuRepository.findOneByIdContrato` | `JPA e Repositories.md#contratoavisoonurepository-findonebyidcontrato` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoAvisoOnuRepository.java:11` | `ContratoAvisoController.buscarAviso -> ContratoAvisoOnuService.findByIdContrato -> ContratoAvisoOnuRepository.findOneByIdContrato` |

## `get-contrato-svas-v1.bru`

- Rota: `GET /v1/contracts/{{id}}/svas`
- Codigo: sem correspondencia estatica
- Queries identificadas: nenhuma

## `get-contrato.bru`

- Rota: `GET /contrato/{{id}}`
- Codigo: `ContratoController.buscar` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java:107`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `VendaRepository.findTopByContratoOrderByCriacaoDesc` | `JPA e Repositories.md#vendarepository-findtopbycontratoorderbycriacaodesc` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:23` | `ContratoController.buscar -> VendaService.findTopByContratoOrderByCriacaoDesc -> VendaRepository.findTopByContratoOrderByCriacaoDesc` |

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `ContratoItemService.findAll`
- `ContratoProdutoService.findAll`

## `get-elegibilidade-confianca.bru`

- Rota: `GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}`
- Codigo: `ContractsControllerV1.sydleContractTrustEnablementBalance` em `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java:26`
- Queries identificadas: nenhuma

## `get-migracoes-contrato.bru`

- Rota: `GET /contrato/{{id}}/migracao`
- Codigo: `ContratoController.migracoes` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java:150`
- Queries identificadas: nenhuma

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `ContratoMigracaoService.findAll`

## `get-vendas-by-natureza.bru`

- Rota: `PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC`
- Codigo: `VendaController.naoConfirmadas` em `comercial-api/src/main/java/br/net/air/venda/controller/VendaController.java:100`
- Queries identificadas: nenhuma

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `VendaService.findAll`

## `get-vendas-contrato.bru`

- Rota: `GET /contrato/{{id}}/venda`
- Codigo: `ContratoController.vendas` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java:200`
- Queries identificadas: nenhuma

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `VendaAdicionalService.findAll`
- `VendaService.findAll`

## `get-wpp-notificacoes-listar.bru`

- Rota: `GET /wpp-notificacoes/listar/{{customerId}}`
- Codigo: `NotificationController.listar` em `comercial-api/src/main/java/br/net/air/notification/controller/NotificationController.java:49`
- Queries identificadas: nenhuma

## `post-contrato-adicionar-aviso.bru`

- Rota: `POST /contrato/{{id}}/adicionar_aviso`
- Codigo: `ContratoAvisoController.adicionarAviso` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoAvisoController.java:29`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `ContratoAvisoOnuRepository.findOneByIdContrato` | `JPA e Repositories.md#contratoavisoonurepository-findonebyidcontrato` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoAvisoOnuRepository.java:11` | `ContratoAvisoController.adicionarAviso -> ContratoAvisoOnuService.criar -> ContratoAvisoOnuRepository.findOneByIdContrato` |

## `post-criar-integracao.bru`

- Rota: `POST /contrato/criar-integracao`
- Codigo: `ContratoController.criarContrato` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java:591`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `ClienteFisicoRepository.findTopByCpf` | `JPA e Repositories.md#clientefisicorepository-findtopbycpf` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteFisicoRepository.java:12` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ClienteService.criar -> ClienteFisicoRepository.findTopByCpf` |
| `ClienteJuridicoRepository.findTopByCnpj` | `JPA e Repositories.md#clientejuridicorepository-findtopbycnpj` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteJuridicoRepository.java:11` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ClienteService.criar -> ClienteJuridicoRepository.findTopByCnpj` |
| `ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` | `JPA e Repositories.md#contratocampanharepository-findtopbycontratoandcanceladaisfalseorderbyiddesc` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoCampanhaRepository.java:12` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ContratoService.criarContratoBaseNovoCRM -> ContratoCampanhaService.criar -> ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` |
| `EnderecoCidadeRepository.findCidadeBySigla` | `enderecocidaderepository-findcidadebysigla.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoCidadeRepository.java:43` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> EnderecoService.criarNovoCRM -> EnderecoCidadeRepository.findCidadeBySigla` |
| `VendaAdicionalRepository.save` | `JPA e Repositories.md#vendaadicionalrepository-save` | `repository-crud-operation` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaAdicionalRepository.java:1` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaAdicionalRepository.save` |
| `VendaOrigemRepository.save` | `JPA e Repositories.md#vendaorigemrepository-save` | `repository-crud-operation` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaOrigemRepository.java:1` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaOrigemRepository.save` |
| `VendaRepository.buscarVendaNoAIR` | `vendarepository-buscarvendanoair.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:47` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.buscarVendaNoAIR -> VendaRepository.buscarVendaNoAIR` |
| `VendaRepository.findTopByIdProcessoVendaSydle` | `JPA e Repositories.md#vendarepository-findtopbyidprocessovendasydle` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:24` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaBuilder.buildVendaNovoCRMIntegracao -> VendaService.findTopByIdProcessoVendaSydle -> VendaRepository.findTopByIdProcessoVendaSydle` |
| `VendedorRepository.findAllByIdVendedorSydle` | `JPA e Repositories.md#vendedorrepository-findallbyidvendedorsydle` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/configuracoes/repository/VendedorRepository.java:16` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendedorService.buscarVendedorAir -> VendedorRepository.findAllByIdVendedorSydle` |
| `VendedorRepository.findTopByUsuarioStartingWithAndAtivoIsTrue` | `JPA e Repositories.md#vendedorrepository-findtopbyusuariostartingwithandativoistrue` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/configuracoes/repository/VendedorRepository.java:18` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendedorService.buscarVendedorAir -> VendedorRepository.findTopByUsuarioStartingWithAndAtivoIsTrue` |

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `LeadService.save`
- `RegraSuspensaoService.findOne`

## `post-oauth-integrar.bru`

- Rota: `POST /oauth/integrar`
- Codigo: `OauthController.integrarManual` em `comercial-api/src/main/java/br/net/air/oauth/Controller/OauthController.java:35`
- Queries identificadas: nenhuma

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `ClienteService.findOne`
- `ClienteService.save`

## `test-criar-integracao.bru`

- Rota: `POST /contrato/criar-integracao`
- Codigo: `ContratoController.criarContrato` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java:591`

| Query | Artefato | Tipo | Fonte | Caminho de chamada |
|---|---|---|---|---|
| `ClienteFisicoRepository.findTopByCpf` | `JPA e Repositories.md#clientefisicorepository-findtopbycpf` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteFisicoRepository.java:12` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ClienteService.criar -> ClienteFisicoRepository.findTopByCpf` |
| `ClienteJuridicoRepository.findTopByCnpj` | `JPA e Repositories.md#clientejuridicorepository-findtopbycnpj` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteJuridicoRepository.java:11` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ClienteService.criar -> ClienteJuridicoRepository.findTopByCnpj` |
| `ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` | `JPA e Repositories.md#contratocampanharepository-findtopbycontratoandcanceladaisfalseorderbyiddesc` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoCampanhaRepository.java:12` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ContratoService.criarContratoBaseNovoCRM -> ContratoCampanhaService.criar -> ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` |
| `EnderecoCidadeRepository.findCidadeBySigla` | `enderecocidaderepository-findcidadebysigla.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoCidadeRepository.java:43` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> EnderecoService.criarNovoCRM -> EnderecoCidadeRepository.findCidadeBySigla` |
| `VendaAdicionalRepository.save` | `JPA e Repositories.md#vendaadicionalrepository-save` | `repository-crud-operation` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaAdicionalRepository.java:1` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaAdicionalRepository.save` |
| `VendaOrigemRepository.save` | `JPA e Repositories.md#vendaorigemrepository-save` | `repository-crud-operation` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaOrigemRepository.java:1` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaOrigemRepository.save` |
| `VendaRepository.buscarVendaNoAIR` | `vendarepository-buscarvendanoair.sql` | `repository-native-query` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:47` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.buscarVendaNoAIR -> VendaRepository.buscarVendaNoAIR` |
| `VendaRepository.findTopByIdProcessoVendaSydle` | `JPA e Repositories.md#vendarepository-findtopbyidprocessovendasydle` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:24` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaBuilder.buildVendaNovoCRMIntegracao -> VendaService.findTopByIdProcessoVendaSydle -> VendaRepository.findTopByIdProcessoVendaSydle` |
| `VendedorRepository.findAllByIdVendedorSydle` | `JPA e Repositories.md#vendedorrepository-findallbyidvendedorsydle` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/configuracoes/repository/VendedorRepository.java:16` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendedorService.buscarVendedorAir -> VendedorRepository.findAllByIdVendedorSydle` |
| `VendedorRepository.findTopByUsuarioStartingWithAndAtivoIsTrue` | `JPA e Repositories.md#vendedorrepository-findtopbyusuariostartingwithandativoistrue` | `repository-derived-query` | `comercial-api/src/main/java/br/net/air/configuracoes/repository/VendedorRepository.java:18` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendedorService.buscarVendedorAir -> VendedorRepository.findTopByUsuarioStartingWithAndAtivoIsTrue` |

Chamadas relacionadas ainda nao resolvidas automaticamente:
- `LeadService.save`
- `RegraSuspensaoService.findOne`
