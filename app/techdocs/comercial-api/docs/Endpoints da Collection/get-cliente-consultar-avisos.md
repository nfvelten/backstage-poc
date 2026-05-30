# get-cliente-consultar-avisos.bru

- Rota: `GET /cliente/{{id}}/consultar_avisos`
- Collection: `air-api-collection/comercial/get-cliente-consultar-avisos.bru`
- Codigo: `ClienteController.consultarAvisos` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:543`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `ClienteRepository.findClienteResumoAvisoById` | `repository-jpql-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#clienterepository-findclienteresumoavisobyid) | - | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteRepository.findClienteResumoAvisoById` |
| `ContratoRepository.findAllIdByClienteId` | `repository-jpql-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#contratorepository-findallidbyclienteid) | - | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ContratoRepository.findAllIdByClienteId` |
| `sql.aviso-telefonia` | `native-properties` | [sql-aviso-telefonia.sql](../sql-aviso-telefonia.sql) | [sql-aviso-telefonia.md](../Resultados SELECT/sql-aviso-telefonia.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |
| `sql.aviso.rede.backbone` | `native-properties` | [sql-aviso-rede-backbone.sql](../sql-aviso-rede-backbone.sql) | [sql-aviso-rede-backbone.md](../Resultados SELECT/sql-aviso-rede-backbone.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |
| `sql.aviso.rede.manual` | `native-properties` | [sql-aviso-rede-manual.sql](../sql-aviso-rede-manual.sql) | [sql-aviso-rede-manual.md](../Resultados SELECT/sql-aviso-rede-manual.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |
| `sql.aviso.rede.monitorado` | `native-properties` | [sql-aviso-rede-monitorado.sql](../sql-aviso-rede-monitorado.sql) | [sql-aviso-rede-monitorado.md](../Resultados SELECT/sql-aviso-rede-monitorado.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.adicionarAvisosPorMonitoramento -> JdbcRepository.findAvisosRedeContratoMonitorado` |
| `sql.aviso.rede.nao-monitorado` | `native-properties` | [sql-aviso-rede-nao-monitorado.sql](../sql-aviso-rede-nao-monitorado.sql) | [sql-aviso-rede-nao-monitorado.md](../Resultados SELECT/sql-aviso-rede-nao-monitorado.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.adicionarAvisosPorMonitoramento -> JdbcRepository.findAvisosRedeContratoNaoMonitorado` |
| `sql.contratoAvisoMigracao` | `native-properties` | [sql-contratoavisomigracao.sql](../sql-contratoavisomigracao.sql) | [sql-contratoavisomigracao.md](../Resultados SELECT/sql-contratoavisomigracao.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.buildAvisoMigracaoV2` |
| `sql.contratoAvisoMigracaoCompulsoria` | `native-properties` | [sql-contratoavisomigracaocompulsoria.sql](../sql-contratoavisomigracaocompulsoria.sql) | [sql-contratoavisomigracaocompulsoria.md](../Resultados SELECT/sql-contratoavisomigracaocompulsoria.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.buildAvisoMigracaoCompulsoriaV2` |
| `sql.pacotesByClienteId` | `native-properties` | [sql-pacotesbyclienteid.sql](../sql-pacotesbyclienteid.sql) | [sql-pacotesbyclienteid.md](../Resultados SELECT/sql-pacotesbyclienteid.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2 -> ClienteService.buildAvisoMigracaoV2 -> ClienteService.jaMigrouV2` |
| `sql.verifica.cliente-monitorado` | `native-properties` | [sql-verifica-cliente-monitorado.sql](../sql-verifica-cliente-monitorado.sql) | [sql-verifica-cliente-monitorado.md](../Resultados SELECT/sql-verifica-cliente-monitorado.md) | `ClienteController.consultarAvisos -> ClienteService.buildAvisosV2` |

## Chamadas ainda nao resolvidas

- `MySqlRepository.carregar`
- `MySqlRepository.consultar`

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
