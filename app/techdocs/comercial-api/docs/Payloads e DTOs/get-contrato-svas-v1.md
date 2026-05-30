# Payload - get-contrato-svas-v1

- Rota: `GET /v1/contracts/{{id}}/svas`
- Collection: `air-api-collection/comercial/get-contrato-svas-v1.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`

## Contexto da collection

Endpoint clean-arch (ContractServiceV1).
  Retorna detalhes do contrato incluindo SVAs/OTTs vinculados e informações de TV.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
