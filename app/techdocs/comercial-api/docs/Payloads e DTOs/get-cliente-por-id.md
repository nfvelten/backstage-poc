# Payload - get-cliente-por-id

- Rota: `GET /cliente/{{id}}`
- Collection: `air-api-collection/comercial/get-cliente-por-id.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`

## Contexto da collection

Busca dados completos do cliente por ID.

  Codigo: ClienteController.buscar.
  Retorna cliente com informacoes relacionadas usadas na tela/atendimento, incluindo avisos e dados de lead quando aplicavel.
  Uso comum: ponto de partida para investigar contrato, contato, blacklist, anexos e avisos do cliente.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
