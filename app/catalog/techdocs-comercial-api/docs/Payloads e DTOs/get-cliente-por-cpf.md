# Payload - get-cliente-por-cpf

- Rota: `GET /cliente?cpfcnpj={{cpf}}`
- Collection: `air-api-collection/comercial/get-cliente-por-cpf.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`

## Contexto da collection

Busca cliente pelo documento informado em query string.

  Codigo: ClienteController.listar (GET /cliente).
  Uso: localizar ID do cliente AIR a partir de CPF/CNPJ para investigacoes e chamadas seguintes.
  Observacao: a rota aceita filtros adicionais no controller; este request documenta o uso por documento.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
