# get-vendas-by-natureza.bru

- Rota: `PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC`
- Collection: `air-api-collection/comercial/get-vendas-by-natureza.bru`
- Codigo: `VendaController.naoConfirmadas` em `comercial-api/src/main/java/br/net/air/venda/controller/VendaController.java:100`

## Queries e operacoes

Nenhuma query/operacao foi resolvida automaticamente para este endpoint.

## Chamadas ainda nao resolvidas

- `VendaService.findAll`

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
