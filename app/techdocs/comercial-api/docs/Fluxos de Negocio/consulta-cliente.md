# Consulta de cliente

Gerado em: 2026-05-30 10:11:02

- Objetivo: Consulta dados cadastrais, contratos, contatos e endereços do cliente.
- Risco operacional: `medio`
- Endpoints: 5
- Queries/operações mapeadas: 17
- Tabelas SQL identificadas: 16

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [get-cliente-por-id.md](../Endpoints da Collection/get-cliente-por-id.md) | `GET /cliente/{{id}}` | `ClienteController.buscar` | `-` | `ResponseEntity<Cliente>` |
| [get-cliente-por-cpf.md](../Endpoints da Collection/get-cliente-por-cpf.md) | `GET /cliente?cpfcnpj={{cpf}}` | `ClienteController.listar` | `-` | `ResponseEntity<List<Cliente>>` |
| [get-cliente-contrato.md](../Endpoints da Collection/get-cliente-contrato.md) | `GET /cliente/{{id}}/contrato` | `ClienteController.contratos` | `-` | `ResponseEntity<?>` |
| [get-cliente-contato.md](../Endpoints da Collection/get-cliente-contato.md) | `GET /cliente/{{id}}/contato` | `ClienteController.contatos` | `-` | `ResponseEntity<?>` |
| [get-cliente-endereco.md](../Endpoints da Collection/get-cliente-endereco.md) | `GET /cliente/{{id}}/endereco` | `ClienteController.enderecos` | `-` | `ResponseEntity<?>` |

## Contrato HTTP observado

### `GET /cliente/{{id}}`

- Assinatura: `public ResponseEntity<Cliente> buscar(@PathVariable("id") Cliente entity)`
- Body Bruno: sem body JSON.

### `GET /cliente?cpfcnpj={{cpf}}`

- Assinatura: `public ResponseEntity<List<Cliente>> listar( @RequestParam(value = "limit", defaultValue = "6") Integer limit, @RequestParam(value = "cpfcnpj", required = false) String campoFiscal, @RequestParam(value = "nome", required = false) String nome, @RequestParam(value = "nome_social", required = false) String nomeSocial, @RequestParam(value = "logradouro", required = false) String logradouro, @RequestParam(value = "numero", required = false) String numero, @RequestParam(value = "id_cidade", required = false) Long id_cidade,`
- Body Bruno: sem body JSON.

### `GET /cliente/{{id}}/contrato`

- Assinatura: `public ResponseEntity<?> contratos(@PathVariable("id") Long id)`
- Body Bruno: sem body JSON.

### `GET /cliente/{{id}}/contato`

- Assinatura: `public ResponseEntity<?> contatos(@PathVariable("id") Long id)`
- Body Bruno: sem body JSON.

### `GET /cliente/{{id}}/endereco`

- Assinatura: `public ResponseEntity<?> enderecos(@PathVariable("id") Long id)`
- Body Bruno: sem body JSON.

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|
| `ContratoRepository.findAllByCliente` | `repository-derived-query` | `../JPA%20e%20Repositories.md#contratorepository-findallbycliente` | - | `ClienteController.buscar -> ClienteService.buildAvisos -> ContratoRepository.findAllByCliente` |
| `EnderecoRepository.findAllEnderecosByCliente` | `repository-native-query` | [enderecorepository-findallenderecosbycliente.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/enderecorepository-findallenderecosbycliente.sql) | [enderecorepository-findallenderecosbycliente.md](../Resultados SELECT/enderecorepository-findallenderecosbycliente.md) | `ClienteController.enderecos -> EnderecoService.findAllEnderecosByCliente -> EnderecoRepository.findAllEnderecosByCliente` |
| `MarcadorContratoRepository.findByIdContrato` | `repository-derived-query` | `../JPA%20e%20Repositories.md#marcadorcontratorepository-findbyidcontrato` | - | `ClienteController.contratos -> MarcadorContratoRepository.findByIdContrato` |
| `VendaRepository.findTopByContratoOrderByCriacaoDesc` | `repository-derived-query` | `../JPA%20e%20Repositories.md#vendarepository-findtopbycontratoorderbycriacaodesc` | - | `ClienteController.contratos -> VendaService.findTopByContratoOrderByCriacaoDesc -> VendaRepository.findTopByContratoOrderByCriacaoDesc` |
| `sql.aviso-telefonia` | `native-properties` | [sql-aviso-telefonia.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-telefonia.sql) | [sql-aviso-telefonia.md](../Resultados SELECT/sql-aviso-telefonia.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.findAvisosTelefonia` |
| `sql.aviso.rede.backbone` | `native-properties` | [sql-aviso-rede-backbone.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-backbone.sql) | [sql-aviso-rede-backbone.md](../Resultados SELECT/sql-aviso-rede-backbone.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.findAvisosRedeBackbone` |
| `sql.aviso.rede.manual` | `native-properties` | [sql-aviso-rede-manual.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-manual.sql) | [sql-aviso-rede-manual.md](../Resultados SELECT/sql-aviso-rede-manual.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.findAvisosRedeManual` |
| `sql.aviso.rede.monitorado` | `native-properties` | [sql-aviso-rede-monitorado.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-monitorado.sql) | [sql-aviso-rede-monitorado.md](../Resultados SELECT/sql-aviso-rede-monitorado.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.adicionarAvisosPorMonitoramentoV2 -> JdbcRepository.findAvisosRedeContratoMonitorado` |
| `sql.aviso.rede.nao-monitorado` | `native-properties` | [sql-aviso-rede-nao-monitorado.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-nao-monitorado.sql) | [sql-aviso-rede-nao-monitorado.md](../Resultados SELECT/sql-aviso-rede-nao-monitorado.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.adicionarAvisosPorMonitoramentoV2 -> JdbcRepository.findAvisosRedeContratoNaoMonitorado` |
| `sql.buscarClienteContrato` | `native-properties` | [sql-buscarclientecontrato.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-buscarclientecontrato.sql) | [sql-buscarclientecontrato.md](../Resultados SELECT/sql-buscarclientecontrato.md) | `ClienteController.listar -> ClienteService.findAll` |
| `sql.buscarClienteOSProtocoloUra` | `native-properties` | [sql-buscarclienteosprotocoloura.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-buscarclienteosprotocoloura.sql) | [sql-buscarclienteosprotocoloura.md](../Resultados SELECT/sql-buscarclienteosprotocoloura.md) | `ClienteController.listar -> ClienteService.findAll` |
| `sql.buscarClienteProtocoloUra` | `native-properties` | [sql-buscarclienteprotocoloura.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-buscarclienteprotocoloura.sql) | [sql-buscarclienteprotocoloura.md](../Resultados SELECT/sql-buscarclienteprotocoloura.md) | `ClienteController.listar -> ClienteService.findAll` |
| `sql.contract-brands` | `native-properties` | [sql-contract-brands.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-contract-brands.sql) | [sql-contract-brands.md](../Resultados SELECT/sql-contract-brands.md) | `ClienteController.contratos -> ContratoService.buscarMarcaPorContrato` |
| `sql.contratoAvisoMigracao` | `native-properties` | [sql-contratoavisomigracao.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-contratoavisomigracao.sql) | [sql-contratoavisomigracao.md](../Resultados SELECT/sql-contratoavisomigracao.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.buildAvisoMigracao -> JdbcRepository.findAvisoMigracao` |
| `sql.contratoAvisoMigracaoCompulsoria` | `native-properties` | [sql-contratoavisomigracaocompulsoria.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-contratoavisomigracaocompulsoria.sql) | [sql-contratoavisomigracaocompulsoria.md](../Resultados SELECT/sql-contratoavisomigracaocompulsoria.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.buildAvisoMigracaoCompulsoria -> JdbcRepository.findAvisoMigracaoCompulsoria` |
| `sql.pacotesByClienteId` | `native-properties` | [sql-pacotesbyclienteid.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-pacotesbyclienteid.sql) | [sql-pacotesbyclienteid.md](../Resultados SELECT/sql-pacotesbyclienteid.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.buildAvisoMigracao -> ClienteService.jaMigrou -> JdbcRepository.findPacotes` |
| `sql.verifica.cliente-monitorado` | `native-properties` | [sql-verifica-cliente-monitorado.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-verifica-cliente-monitorado.sql) | [sql-verifica-cliente-monitorado.md](../Resultados SELECT/sql-verifica-cliente-monitorado.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.contratoMonitorado` |

## Tabelas tocadas por SQL nativo

- `air_base.tbl_unidade`
- `air_chamado.tbl_chd_chamado`
- `air_chamado.tbl_os`
- `air_comercial.tbl_aviso_migracao`
- `air_comercial.tbl_cliente`
- `air_comercial.tbl_condominio`
- `air_comercial.tbl_contrato`
- `air_comercial.tbl_contrato_onu_aviso`
- `air_comercial.tbl_endereco`
- `air_internet.tbl_aviso`
- `air_internet.tbl_aviso_unidade`
- `air_internet.tbl_estimativa_conclusao_aviso`
- `air_internet.tbl_login`
- `air_internet.tbl_posicoes_afetadas`
- `air_telefonia.tbl_reserva`
- `tbl_endereco_cidade`

## Efeitos colaterais e integrações

Integrações/sistemas citados no caminho ou SQL:
- Internet
- Telefonia

## Dados sensíveis

Sinais de dados sensíveis encontrados em nomes de campos, queries ou caminho:
- `Endereco`
- `cnpj`
- `cpf`
- `endereco`

## Pendências de mapeamento

- `ContratoService.findAll`
- `MySqlRepository.consultarMap`

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
