# Payload - get-cliente-contrato

- Rota: `GET /cliente/{{id}}/contrato`
- Collection: `air-api-collection/comercial/get-cliente-contrato.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /cliente/{id}/contrato (2.730 sucessos no print).

  Codigo: ClienteController.contratos.
  Uso: lista contratos do cliente, com dados usados para atendimento e navegacao para detalhes do contrato.
  Variavel: id = ID do cliente.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
