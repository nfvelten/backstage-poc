# get-contracts-customer-basic-info.bru

- Rota: `GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}`
- Collection: `air-api-collection/comercial/get-contracts-customer-basic-info.bru`
- Codigo: `ContractsControllerV1.getCustomerBasicInfoByContractNumber` em `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java:46`

## Queries e operacoes

Nenhuma query/operacao foi resolvida automaticamente para este endpoint.

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
