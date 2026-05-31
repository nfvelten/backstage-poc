# Payload - get-elegibilidade-confianca

- Rota: `GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}`
- Collection: `air-api-collection/comercial/get-elegibilidade-confianca.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`

## Contexto da collection

Consulta elegibilidade/saldo de habilitacao em confianca por numero de contrato.

  Codigo: ContractsControllerV1.sydleContractTrustEnablementBalance -> ContractServiceV1.checkContractTrustEnablementBalance.
  Integracao: Sydle billing/trust enablement balance.
  Uso comum: validar se contrato pode seguir fluxo de habilitacao em confianca.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
