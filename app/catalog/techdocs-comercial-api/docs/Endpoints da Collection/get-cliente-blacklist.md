# get-cliente-blacklist.bru

- Rota: `GET /cliente/{{id}}/blacklist`
- Collection: `air-api-collection/comercial/get-cliente-blacklist.bru`
- Codigo: `ClienteController.blacklist` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:269`

## Queries e operacoes

Nenhuma query/operacao foi resolvida automaticamente para este endpoint.

## Chamadas ainda nao resolvidas

- `BlacklistService.findAll`

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
