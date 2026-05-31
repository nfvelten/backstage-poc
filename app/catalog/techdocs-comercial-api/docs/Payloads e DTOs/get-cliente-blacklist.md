# Payload - get-cliente-blacklist

- Rota: `GET /cliente/{{id}}/blacklist`
- Collection: `air-api-collection/comercial/get-cliente-blacklist.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /cliente/{id}/blacklist (1.683 sucessos no print).

  Codigo: ClienteController.blacklist.
  Uso: lista registros de blacklist associados ao cliente.
  Variavel: id = ID do cliente.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
