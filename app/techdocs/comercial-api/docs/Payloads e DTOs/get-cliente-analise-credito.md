# Payload - get-cliente-analise-credito

- Rota: `GET /cliente/{{id}}/analise_credito`
- Collection: `air-api-collection/comercial/get-cliente-analise-credito.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /cliente/{id}/analise_credito (1.685 sucessos no print).

  Codigo: ClienteController.analisesCredito.
  Uso: lista analises de credito relacionadas ao cliente.
  Variavel: id = ID do cliente.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
