# Payload - get-contracts-detail

- Rota: `GET /v1/contracts/detail?contract_number={{contract_number}}`
- Collection: `air-api-collection/comercial/get-contracts-detail.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /v1/contracts/detail (56.671 sucessos no print).

  Codigo: ContractsControllerV1.findContractDetails -> ContractServiceV1.findContractDetails.
  Uso: consulta detalhes do contrato, incluindo SVAs/OTTs e informacoes agregadas usadas por consumidores v1.
  Parametro principal: contract_number.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
