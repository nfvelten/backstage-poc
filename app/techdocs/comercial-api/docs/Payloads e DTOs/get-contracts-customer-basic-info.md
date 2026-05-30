# Payload - get-contracts-customer-basic-info

- Rota: `GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}`
- Collection: `air-api-collection/comercial/get-contracts-customer-basic-info.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /v1/contracts/customer-basic-info (6.562 sucessos no print).

  Codigo: ContractsControllerV1.getCustomerBasicInfoByContractNumber -> ContractServiceV1.getCustomerBasicInfo.
  Uso: consulta dados basicos do cliente por contrato ou documento.
  Parametros aceitos no codigo: contract_number e document. Este request usa contract_number.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
