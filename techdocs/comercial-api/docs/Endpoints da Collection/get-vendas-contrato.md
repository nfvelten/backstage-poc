# get-vendas-contrato.bru

- Rota: `GET /contrato/{{id}}/venda`
- Collection: `air-api-collection/comercial/get-vendas-contrato.bru`
- Codigo: `ContratoController.vendas` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java:200`

## Queries e operacoes

Nenhuma query/operacao foi resolvida automaticamente para este endpoint.

## Chamadas ainda nao resolvidas

- `VendaAdicionalService.findAll`
- `VendaService.findAll`

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
