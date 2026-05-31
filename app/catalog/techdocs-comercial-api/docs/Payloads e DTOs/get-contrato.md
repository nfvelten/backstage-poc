# Payload - get-contrato

- Rota: `GET /contrato/{{id}}`
- Collection: `air-api-collection/comercial/get-contrato.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`

## Contexto da collection

Busca contrato por ID com produtos, itens, endereco de entrega e fase da ultima venda.

  Codigo: ContratoController.buscar.
  Efeitos: consulta dados relacionados e bloqueia usuario ANONIMO via Security.
  Uso comum: diagnostico geral de contrato antes de investigar venda, migracao, endereco ou ativacao.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
