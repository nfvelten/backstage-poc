# get-cliente-contrato.bru

- Rota: `GET /cliente/{{id}}/contrato`
- Collection: `air-api-collection/comercial/get-cliente-contrato.bru`
- Codigo: `ClienteController.contratos` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:211`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `MarcadorContratoRepository.findByIdContrato` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#marcadorcontratorepository-findbyidcontrato) | - | `ClienteController.contratos -> MarcadorContratoRepository.findByIdContrato` |
| `VendaRepository.findTopByContratoOrderByCriacaoDesc` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#vendarepository-findtopbycontratoorderbycriacaodesc) | - | `ClienteController.contratos -> VendaService.findTopByContratoOrderByCriacaoDesc -> VendaRepository.findTopByContratoOrderByCriacaoDesc` |
| `sql.contract-brands` | `native-properties` | [sql-contract-brands.sql](../sql-contract-brands.sql) | [sql-contract-brands.md](../Resultados SELECT/sql-contract-brands.md) | `ClienteController.contratos -> ContratoService.buscarMarcaPorContrato` |

## Chamadas ainda nao resolvidas

- `ContratoService.findAll`
- `MySqlRepository.consultarMap`

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
