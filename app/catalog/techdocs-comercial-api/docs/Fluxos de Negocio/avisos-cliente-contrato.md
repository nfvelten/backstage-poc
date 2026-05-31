# Avisos de cliente e contrato

Gerado em: 2026-05-30 10:11:02

- Objetivo: Consulta e adiciona avisos operacionais, de rede, telefonia, migração e monitoramento.
- Risco operacional: `medio`
- Endpoints: 3
- Queries/operações mapeadas: 13
- Tabelas SQL identificadas: 10

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [get-cliente-consultar-avisos.md](../Endpoints da Collection/get-cliente-consultar-avisos.md) | `GET /cliente/{{id}}/consultar_avisos` | `ClienteController.consultarAvisos` | `-` | `ResponseEntity<Set<AvisoEvent>>` |
| [get-contrato-aviso.md](../Endpoints da Collection/get-contrato-aviso.md) | `GET /contrato/{{id}}/aviso` | `ContratoAvisoController.buscarAviso` | `-` | `ResponseEntity<?>` |
| [post-contrato-adicionar-aviso.md](../Endpoints da Collection/post-contrato-adicionar-aviso.md) | `POST /contrato/{{id}}/adicionar_aviso` | `ContratoAvisoController.adicionarAviso` | `ContratoAvisoOnuDTO` | `ResponseEntity<?>` |

## Contrato HTTP observado

### `GET /cliente/{{id}}/consultar_avisos`

- Assinatura: `public ResponseEntity<Set<AvisoEvent>> consultarAvisos(@PathVariable("id") Long idCliente)`
- Body Bruno: sem body JSON.

### `GET /contrato/{{id}}/aviso`

- Assinatura: `public ResponseEntity<?> buscarAviso(@PathVariable("id") Long contratoId)`
- Body Bruno: sem body JSON.

### `POST /contrato/{{id}}/adicionar_aviso`

- Assinatura: `public ResponseEntity<?> adicionarAviso(@PathVariable("id") Long contratoId, @RequestBody ContratoAvisoOnuDTO dto)`
- Campos do body Bruno: `problemId`, `descricao`, `id`, `onu`, `olt`, `slot`, `pon`, `index`, `serial`, `rx_power`

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|
| `ClienteRepository.findClienteResumoAvisoById` | `repository-jpql-query` | `../JPA%20e%20Repositories.md#clienterepository-findclienteresumoavisobyid` | - | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteRepository.findClienteResumoAvisoById` |
| `ContratoAvisoOnuRepository.findOneByIdContrato` | `repository-derived-query` | `../JPA%20e%20Repositories.md#contratoavisoonurepository-findonebyidcontrato` | - | `ContratoAvisoController.buscarAviso -> ContratoAvisoOnuService.findByIdContrato -> ContratoAvisoOnuRepository.findOneByIdContrato` |
| `ContratoAvisoOnuRepository.findOneByIdContrato` | `repository-derived-query` | `../JPA%20e%20Repositories.md#contratoavisoonurepository-findonebyidcontrato` | - | `ContratoAvisoController.adicionarAviso -> ContratoAvisoOnuService.criar -> ContratoAvisoOnuRepository.findOneByIdContrato` |
| `ContratoRepository.findAllIdByClienteId` | `repository-jpql-query` | `../JPA%20e%20Repositories.md#contratorepository-findallidbyclienteid` | - | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ContratoRepository.findAllIdByClienteId` |
| `sql.aviso-telefonia` | `native-properties` | [sql-aviso-telefonia.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-telefonia.sql) | [sql-aviso-telefonia.md](../Resultados SELECT/sql-aviso-telefonia.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |
| `sql.aviso.rede.backbone` | `native-properties` | [sql-aviso-rede-backbone.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-backbone.sql) | [sql-aviso-rede-backbone.md](../Resultados SELECT/sql-aviso-rede-backbone.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |
| `sql.aviso.rede.manual` | `native-properties` | [sql-aviso-rede-manual.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-manual.sql) | [sql-aviso-rede-manual.md](../Resultados SELECT/sql-aviso-rede-manual.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |
| `sql.aviso.rede.monitorado` | `native-properties` | [sql-aviso-rede-monitorado.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-monitorado.sql) | [sql-aviso-rede-monitorado.md](../Resultados SELECT/sql-aviso-rede-monitorado.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.adicionarAvisosPorMonitoramento -> JdbcRepository.findAvisosRedeContratoMonitorado` |
| `sql.aviso.rede.nao-monitorado` | `native-properties` | [sql-aviso-rede-nao-monitorado.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-aviso-rede-nao-monitorado.sql) | [sql-aviso-rede-nao-monitorado.md](../Resultados SELECT/sql-aviso-rede-nao-monitorado.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.adicionarAvisosPorMonitoramento -> JdbcRepository.findAvisosRedeContratoNaoMonitorado` |
| `sql.contratoAvisoMigracao` | `native-properties` | [sql-contratoavisomigracao.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-contratoavisomigracao.sql) | [sql-contratoavisomigracao.md](../Resultados SELECT/sql-contratoavisomigracao.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.buildAvisoMigracaoV2` |
| `sql.contratoAvisoMigracaoCompulsoria` | `native-properties` | [sql-contratoavisomigracaocompulsoria.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-contratoavisomigracaocompulsoria.sql) | [sql-contratoavisomigracaocompulsoria.md](../Resultados SELECT/sql-contratoavisomigracaocompulsoria.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.buildAvisoMigracaoCompulsoriaV2` |
| `sql.pacotesByClienteId` | `native-properties` | [sql-pacotesbyclienteid.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-pacotesbyclienteid.sql) | [sql-pacotesbyclienteid.md](../Resultados SELECT/sql-pacotesbyclienteid.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.buildAvisoMigracaoV2 -> ClienteService.jaMigrouV2` |
| `sql.verifica.cliente-monitorado` | `native-properties` | [sql-verifica-cliente-monitorado.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-verifica-cliente-monitorado.sql) | [sql-verifica-cliente-monitorado.md](../Resultados SELECT/sql-verifica-cliente-monitorado.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |

## Tabelas tocadas por SQL nativo

- `air_comercial.tbl_aviso_migracao`
- `air_comercial.tbl_cliente`
- `air_comercial.tbl_contrato`
- `air_comercial.tbl_contrato_onu_aviso`
- `air_internet.tbl_aviso`
- `air_internet.tbl_aviso_unidade`
- `air_internet.tbl_estimativa_conclusao_aviso`
- `air_internet.tbl_login`
- `air_internet.tbl_posicoes_afetadas`
- `air_telefonia.tbl_reserva`

## Efeitos colaterais e integrações

Endpoints com potencial efeito colateral:
- `POST /contrato/{{id}}/adicionar_aviso`

Integrações/sistemas citados no caminho ou SQL:
- Internet
- Telefonia

## Dados sensíveis

- Nenhum sinal forte identificado automaticamente.

## Pendências de mapeamento

- `MySqlRepository.carregar`
- `MySqlRepository.consultar`

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
