# Payload - get-vendas-contrato

- Rota: `GET /contrato/{{id}}/venda`
- Collection: `air-api-collection/comercial/get-vendas-contrato.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`

## Contexto da collection

Lista vendas vinculadas ao contrato e adiciona produtos adicionais de cada venda.

  Codigo: ContratoController.vendas.
  Uso comum: verificar vendas confirmadas, adicionais, migracoes e fase da venda associada ao contrato.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
