# post-contrato-adicionar-aviso.bru

- Rota: `POST /contrato/{{id}}/adicionar_aviso`
- Collection: `air-api-collection/comercial/post-contrato-adicionar-aviso.bru`
- Codigo: `ContratoAvisoController.adicionarAviso` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoAvisoController.java:29`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `ContratoAvisoOnuRepository.findOneByIdContrato` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#contratoavisoonurepository-findonebyidcontrato) | - | `ContratoAvisoController.adicionarAviso -> ContratoAvisoOnuService.criar -> ContratoAvisoOnuRepository.findOneByIdContrato` |

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
