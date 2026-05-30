# get-migracoes-contrato.bru

- Rota: `GET /contrato/{{id}}/migracao`
- Collection: `air-api-collection/comercial/get-migracoes-contrato.bru`
- Codigo: `ContratoController.migracoes` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java:150`

## Queries e operacoes

Nenhuma query/operacao foi resolvida automaticamente para este endpoint.

## Chamadas ainda nao resolvidas

- `ContratoMigracaoService.findAll`

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
