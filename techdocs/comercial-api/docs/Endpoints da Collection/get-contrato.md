# get-contrato.bru

- Rota: `GET /contrato/{{id}}`
- Collection: `air-api-collection/comercial/get-contrato.bru`
- Codigo: `ContratoController.buscar` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java:107`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `VendaRepository.findTopByContratoOrderByCriacaoDesc` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#vendarepository-findtopbycontratoorderbycriacaodesc) | - | `ContratoController.buscar -> VendaService.findTopByContratoOrderByCriacaoDesc -> VendaRepository.findTopByContratoOrderByCriacaoDesc` |

## Chamadas ainda nao resolvidas

- `ContratoItemService.findAll`
- `ContratoProdutoService.findAll`

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
