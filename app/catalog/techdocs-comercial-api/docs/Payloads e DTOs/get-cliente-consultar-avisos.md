# Payload - get-cliente-consultar-avisos

- Rota: `GET /cliente/{{id}}/consultar_avisos`
- Collection: `air-api-collection/comercial/get-cliente-consultar-avisos.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /cliente/{id}/consultar_avisos (1.844 sucessos no print).

  Codigo: ClienteController.consultarAvisos.
  Uso: consulta avisos/massivas/rede associados ao cliente/contratos.
  Variavel: id = ID do cliente.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
