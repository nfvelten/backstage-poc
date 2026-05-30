# Payload - get-cliente-endereco

- Rota: `GET /cliente/{{id}}/endereco`
- Collection: `air-api-collection/comercial/get-cliente-endereco.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /cliente/{id}/endereco (1.853 sucessos no print).

  Codigo: ClienteController.enderecos.
  Uso: lista enderecos vinculados ao cliente.
  Variavel: id = ID do cliente.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
