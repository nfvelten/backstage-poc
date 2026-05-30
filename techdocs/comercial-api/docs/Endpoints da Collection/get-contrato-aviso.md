# get-contrato-aviso.bru

- Rota: `GET /contrato/{{id}}/aviso`
- Collection: `air-api-collection/comercial/get-contrato-aviso.bru`
- Codigo: `ContratoAvisoController.buscarAviso` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoAvisoController.java:35`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `ContratoAvisoOnuRepository.findOneByIdContrato` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#contratoavisoonurepository-findonebyidcontrato) | - | `ContratoAvisoController.buscarAviso -> ContratoAvisoOnuService.findByIdContrato -> ContratoAvisoOnuRepository.findOneByIdContrato` |

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
