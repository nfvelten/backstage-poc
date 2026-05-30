# get-cliente-por-id.bru

- Rota: `GET /cliente/{{id}}`
- Collection: `air-api-collection/comercial/get-cliente-por-id.bru`
- Codigo: `ClienteController.buscar` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:187`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `ContratoRepository.findAllByCliente` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#contratorepository-findallbycliente) | - | `ClienteController.buscar -> ClienteService.buildAvisos -> ContratoRepository.findAllByCliente` |
| `sql.aviso-telefonia` | `native-properties` | [sql-aviso-telefonia.sql](../sql-aviso-telefonia.sql) | [sql-aviso-telefonia.md](../Resultados SELECT/sql-aviso-telefonia.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.findAvisosTelefonia` |
| `sql.aviso.rede.backbone` | `native-properties` | [sql-aviso-rede-backbone.sql](../sql-aviso-rede-backbone.sql) | [sql-aviso-rede-backbone.md](../Resultados SELECT/sql-aviso-rede-backbone.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.findAvisosRedeBackbone` |
| `sql.aviso.rede.manual` | `native-properties` | [sql-aviso-rede-manual.sql](../sql-aviso-rede-manual.sql) | [sql-aviso-rede-manual.md](../Resultados SELECT/sql-aviso-rede-manual.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.findAvisosRedeManual` |
| `sql.aviso.rede.monitorado` | `native-properties` | [sql-aviso-rede-monitorado.sql](../sql-aviso-rede-monitorado.sql) | [sql-aviso-rede-monitorado.md](../Resultados SELECT/sql-aviso-rede-monitorado.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.adicionarAvisosPorMonitoramentoV2 -> JdbcRepository.findAvisosRedeContratoMonitorado` |
| `sql.aviso.rede.nao-monitorado` | `native-properties` | [sql-aviso-rede-nao-monitorado.sql](../sql-aviso-rede-nao-monitorado.sql) | [sql-aviso-rede-nao-monitorado.md](../Resultados SELECT/sql-aviso-rede-nao-monitorado.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.adicionarAvisosPorMonitoramentoV2 -> JdbcRepository.findAvisosRedeContratoNaoMonitorado` |
| `sql.contratoAvisoMigracao` | `native-properties` | [sql-contratoavisomigracao.sql](../sql-contratoavisomigracao.sql) | [sql-contratoavisomigracao.md](../Resultados SELECT/sql-contratoavisomigracao.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.buildAvisoMigracao -> JdbcRepository.findAvisoMigracao` |
| `sql.contratoAvisoMigracaoCompulsoria` | `native-properties` | [sql-contratoavisomigracaocompulsoria.sql](../sql-contratoavisomigracaocompulsoria.sql) | [sql-contratoavisomigracaocompulsoria.md](../Resultados SELECT/sql-contratoavisomigracaocompulsoria.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.buildAvisoMigracaoCompulsoria -> JdbcRepository.findAvisoMigracaoCompulsoria` |
| `sql.pacotesByClienteId` | `native-properties` | [sql-pacotesbyclienteid.sql](../sql-pacotesbyclienteid.sql) | [sql-pacotesbyclienteid.md](../Resultados SELECT/sql-pacotesbyclienteid.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> ClienteService.buildAvisoMigracao -> ClienteService.jaMigrou -> JdbcRepository.findPacotes` |
| `sql.verifica.cliente-monitorado` | `native-properties` | [sql-verifica-cliente-monitorado.sql](../sql-verifica-cliente-monitorado.sql) | [sql-verifica-cliente-monitorado.md](../Resultados SELECT/sql-verifica-cliente-monitorado.md) | `ClienteController.buscar -> ClienteService.buildAvisos -> JdbcRepository.contratoMonitorado` |

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
