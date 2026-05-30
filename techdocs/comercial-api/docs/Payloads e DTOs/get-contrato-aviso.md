# Payload - get-contrato-aviso

- Rota: `GET /contrato/{{id}}/aviso`
- Collection: `air-api-collection/comercial/get-contrato-aviso.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /contrato/{id}/aviso (10.208 sucessos no print).

  Codigo: ContratoAvisoController.buscarAviso.
  Uso: consulta aviso ONU associado ao contrato e retorna dados da ONU, data e descricao.
  Variavel: id = ID do contrato.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
