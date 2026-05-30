# get-cliente-por-cpf.bru

- Rota: `GET /cliente?cpfcnpj={{cpf}}`
- Collection: `air-api-collection/comercial/get-cliente-por-cpf.bru`
- Codigo: `ClienteController.listar` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:80`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `sql.buscarClienteContrato` | `native-properties` | [sql-buscarclientecontrato.sql](../sql-buscarclientecontrato.sql) | [sql-buscarclientecontrato.md](../Resultados SELECT/sql-buscarclientecontrato.md) | `ClienteController.listar -> ClienteService.findAll` |
| `sql.buscarClienteOSProtocoloUra` | `native-properties` | [sql-buscarclienteosprotocoloura.sql](../sql-buscarclienteosprotocoloura.sql) | [sql-buscarclienteosprotocoloura.md](../Resultados SELECT/sql-buscarclienteosprotocoloura.md) | `ClienteController.listar -> ClienteService.findAll` |
| `sql.buscarClienteProtocoloUra` | `native-properties` | [sql-buscarclienteprotocoloura.sql](../sql-buscarclienteprotocoloura.sql) | [sql-buscarclienteprotocoloura.md](../Resultados SELECT/sql-buscarclienteprotocoloura.md) | `ClienteController.listar -> ClienteService.findAll` |

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
