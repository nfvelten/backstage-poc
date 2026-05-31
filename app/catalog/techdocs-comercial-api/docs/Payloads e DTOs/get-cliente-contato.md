# Payload - get-cliente-contato

- Rota: `GET /cliente/{{id}}/contato`
- Collection: `air-api-collection/comercial/get-cliente-contato.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /cliente/{id}/contato (2.052 sucessos no print).

  Codigo: ClienteController.contatos.
  Uso: lista contatos cadastrados para o cliente.
  Variavel: id = ID do cliente.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
